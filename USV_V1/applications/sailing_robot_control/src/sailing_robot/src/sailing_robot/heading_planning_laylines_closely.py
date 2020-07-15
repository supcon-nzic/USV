import LatLon as ll
import heading_planning_laylines
import json


class HeadingPlan(heading_planning_laylines.HeadingPlan):

    def __init__(self, nav, waypoint = ll.LatLon(50.742810, 1.014469),  # somewhere in the solent
                 target_radius = 2, close_factor = 0.8, waypoint_id = None, *args, **kwargs):
        self.target = waypoint
        self.target_id = waypoint_id
        self.target_radius = target_radius
        self.accept_radius = target_radius
        self.close_factor = close_factor
        self.nav = nav
        super(HeadingPlan, self).__init__(nav, self.calculate_real_waypoint(), target_radius, *args, **kwargs)
        self.debug_topics.append(('dbg_real_waypoint', 'String'))

    def update_target(self, waypoint, waypoint_id = None):
        self.target = waypoint
        self.target_id = waypoint_id

    def calculate_real_waypoint(self):
        return self.target.offset(self.nav.position_ll.heading_initial(self.target),
                                  min(self.accept_radius * self.close_factor / 1000.0,
                                      self.nav.position_ll.distance(self.target)))

    def calculate_target_radius(self):
        return self.accept_radius * (1 - self.close_factor) + min(self.accept_radius * self.close_factor,
                                                                  self.nav.position_ll.distance(self.target) * 1000)

    def calculate_state_and_goal(self):
        self.update_waypoint(self.calculate_real_waypoint())
        self.update_target_radius(self.calculate_target_radius())
        self.debug_pub('dbg_real_waypoint',
                       json.dumps([self.waypoint.lat.decimal_degree, self.waypoint.lon.decimal_degree]))
        return super(HeadingPlan, self).calculate_state_and_goal()
