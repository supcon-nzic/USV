from collections import deque
import LatLon as ll
import math
from shapely.geometry import Point, Polygon

from .navigation import angleSum
from .taskbase import TaskBase
from .heading_planning import TackVoting
import rospy

class HeadingPlan(TaskBase):
    # For calculations, lay lines don't extend to infinity.
    # This is in m; 10km should be plenty for our purposes.
    LAYLINE_EXTENT = 10000

    def __init__(self, nav, waypoint = ll.LatLon(50.742810, 1.014469),  # somewhere in the solent
                 target_radius = 4, tack_voting_radius = 5, waypoint_id = '', name = '', *args, **kwargs):
        """Sail towards a waypoint.

        *nav* is a sailing_robot.navigation.Navigation instance.

        *waypoint* is a LatLon object telling us where to go.

        *target_radius* is how close we need to get to the waypoint, in metres.

        *tack_voting_radius* is the distance within which we use tack voting, to
        avoid too frequent tacks close to the waypoint.
        """
        self.nav = nav
        self.waypoint = waypoint
        self.waypoint_xy = Point(self.nav.latlon_to_utm(waypoint.lat.decimal_degree, waypoint.lon.decimal_degree))
        self.target_radius = target_radius
        self.target_area = self.waypoint_xy.buffer(target_radius)
        self.sailing_state = 'normal'  # sailing state can be 'normal','switch_to_port_tack' or  'switch_to_stbd_tack'
        self.tack_voting = TackVoting(50, 35)
        self.tack_voting_radius = tack_voting_radius
        self.waypoint_id = waypoint_id
        self.name = name
        self.debug_topics = [('dbg_heading_to_waypoint', 'Float32'), ('dbg_distance_to_waypoint', 'Float32'),
                             ('dbg_goal_wind_angle', 'Float32'), ('dbg_latest_waypoint_id', 'String'), ]
        self.model = rospy.get_param('model')

    def update_waypoint(self, waypoint, waypoint_id = None):
        self.waypoint = waypoint
        self.waypoint_id = waypoint_id
        self.waypoint_xy = Point(
            self.nav.latlon_to_utm(self.waypoint.lat.decimal_degree, self.waypoint.lon.decimal_degree))
        self.target_area = self.waypoint_xy.buffer(self.target_radius)

    def update_target_radius(self, target_radius):
        self.target_radius = target_radius
        self.target_area = self.waypoint_xy.buffer(self.target_radius)

    def check_end_condition(self):
        """Are we there yet?"""
        return self.nav.position_xy.within(self.target_area)

    def calculate_state_and_goal(self):
        """Work out what we want the boat to do
        """
        dwp, hwp = self.nav.distance_and_heading(self.waypoint_xy)
        self.debug_pub('dbg_distance_to_waypoint', dwp)
        self.debug_pub('dbg_heading_to_waypoint', hwp)
        self.debug_pub('dbg_latest_waypoint_id', self.waypoint_id)
       # rospy.logwarn('111')
   
        boat_wind_angle = self.nav.angle_to_wind()
        rospy.logwarn(boat_wind_angle)
        rospy.logwarn(self.nav.beating_angle)

       # wp_wind_angle = self.nav.heading_to_wind_angle(hwp)  #120
       # rospy.logwarn('qqq'+str(wp_wind_angle))
       # rospy.logwarn('www'+str(self.nav.absolute_wind_direction()))
       # Detect if the waypoint is downwind, if so head directly to it
        """
        if abs(wp_wind_angle) > 90 or True :
            goal_wind_angle = wp_wind_angle
            self.debug_pub('dbg_goal_wind_angle', goal_wind_angle)
            state = 'normal'
           
            return state, hwp
        """
            
        if self.sailing_state != 'normal':

            # A tack/jibe is in progress
            if self.sailing_state == 'switch_to_port_tack':
                goal_angle = self.nav.beating_angle
                continue_tack = boat_wind_angle < goal_angle or boat_wind_angle > 120
    
            else:  # 'switch_to_stbd_tack'
                goal_angle = -self.nav.beating_angle
                continue_tack = boat_wind_angle > goal_angle or boat_wind_angle < -120
            
            if continue_tack:
                self.debug_pub('dbg_goal_wind_angle', goal_angle)
                return self.sailing_state, self.nav.wind_angle_to_heading(goal_angle)
            else:
                # Tack completed
                self.log('info', 'Finished tack (%s)', self.sailing_state)
                self.tack_voting.reset(boat_wind_angle > 0)
                self.sailing_state = 'normal'
             

        on_port_tack = boat_wind_angle > 0
        
        wp_wind_angle = self.nav.heading_to_wind_angle(hwp)
       # rospy.logwarn('qqq'+str(wp_wind_angle))
       # rospy.logwarn('www'+str(self.nav.absolute_wind_direction()))
        # Detect if the waypoint is downwind, if so head directly to it
        
        if abs(wp_wind_angle) > 90 or self.model :
            rospy.logwarn('model'+str(self.model))
            goal_wind_angle = wp_wind_angle
            self.debug_pub('dbg_goal_wind_angle', goal_wind_angle)
            state = 'normal'
           
            return state, hwp
       
        tack_now = False
        #tack_now = true
        if wp_wind_angle * boat_wind_angle > 0:
            # These two have the same sign, so we're on the better tack already
            self.tack_voting.vote(on_port_tack)
        elif self.nav.position_xy.within(self.lay_triangle()):
            # We're between the laylines; stick to our current tack for now
            self.tack_voting.vote(on_port_tack)
        else:
            tack_now = True
            self.tack_voting.vote(not on_port_tack)

        if dwp < self.tack_voting_radius:
            # Close to the waypoint, use tack voting so we're not constantly
            # tacking.
            tack_now = self.tack_voting.tack_now(on_port_tack)

        if tack_now:
            # Ready about!
            if on_port_tack:
                state = 'switch_to_stbd_tack'
                goal_wind_angle = -self.nav.beating_angle
            else:
                state = 'switch_to_port_tack'
                goal_wind_angle = self.nav.beating_angle
            self.sailing_state = state
            self.log('info', 'Starting tack/jibe (%s)', state)
        else:
            # Stay on our current tack
            if on_port_tack:
                goal_wind_angle = max(wp_wind_angle, self.nav.beating_angle)
            else:
                goal_wind_angle = min(wp_wind_angle, -self.nav.beating_angle)
            state = 'normal'

        self.debug_pub('dbg_goal_wind_angle', goal_wind_angle)
        return state, self.nav.wind_angle_to_heading(goal_wind_angle)

    def lay_triangle(self):
        """Calculate the lay lines for the current waypoint.

        This returns a shapely Polygon with the two lines extended to
        LAYLINE_EXTENT (10km).
        """
        downwind = angleSum(self.nav.absolute_wind_direction(), 180)
        x0, y0 = self.waypoint_xy.x, self.waypoint_xy.y
        l1 = math.radians(angleSum(downwind, -self.nav.beating_angle))
        x1 = x0 + (self.LAYLINE_EXTENT * math.sin(l1))
        y1 = y0 + (self.LAYLINE_EXTENT * math.cos(l1))
        l2 = math.radians(angleSum(downwind, self.nav.beating_angle))
        x2 = x0 + (self.LAYLINE_EXTENT * math.sin(l2))
        y2 = y0 + (self.LAYLINE_EXTENT * math.cos(l2))
        return Polygon([(x0, y0), (x1, y1), (x2, y2)])
