"""Code for staying near a target point (2016 station keeping challenge)"""
from sailing_robot.pid_control import PID

import station_keeping
import rospy

class StationKeeping(station_keeping.StationKeeping):
    def __init__(self, radius = 3, min_radius = 1, max_radius = 5, accept_radius = 20, linger = 180,
                 kind = 'keep_station_obstacle', *args, **kwargs):
        rospy.logwarn("keep_station3333333333333333333")
        """Machinery to stay near a given point.

        This is meant to be started when we're already close to the waypoint; we'll
        normally put it immediately after a to_waypoint task to go to the waypoint.

        nav : a Navigation object for common machinery.
        marker_ll : a (lat, lon) point marking where we'll try to stay close to.
        linger : time in seconds to stay there
        radius : distance in metres which we'll try to bounce around the waypoint
        wind_angle : the absolute wind angle to sail (in degrees) when inside
           radius. This will automatically be flipped according to the tack.
        """
        self.min_radius = min_radius
        self.max_radius = max_radius
        super(StationKeeping, self).__init__(radius = radius, accept_radius = accept_radius, linger = linger, *args,
                                             **kwargs)

        self.controller = PID(self.nav.rudder_param['control']['Kp'], self.nav.rudder_param['control']['Ki'],
                              self.nav.rudder_param['control']['Kd'], self.nav.rudder_param['maxAngle'],
                              -self.nav.rudder_param['maxAngle'])

    def calculate_task_direct_rudder_control(self, dwp, hwp):
        rudder_control = self.controller.update_PID(dwp - self.radius)
        rudder_control *= 1 if hwp > 0 else -1
        return rudder_control
