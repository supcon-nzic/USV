"""Code for staying near a target point (2016 station keeping challenge)"""
from LatLon import LatLon
from shapely.geometry import Point
import time
import json

import taskbase


def angleAbsDistance(a, b):
    """Magnitude of the difference between two angles.

    Result should always be between 0 and 180.
    """
    distanceA = abs((a - b) % 360)
    distanceB = abs((b - a) % 360)
    return min(distanceA, distanceB)


class StationKeeping(taskbase.ComplexTaskBase):
    def __init__(self, nav, waypoint, radius = 5, accept_radius = 15, linger = 300, waypoint_id = None,
                 kind = 'keep_station', name = '', *args, **kwargs):
        """Machinery to stay near a given point.

        This is meant to be started when we're already close to the waypoint; we'll
        normally put it immediately after a to_waypoint task to go to the waypoint.

        nav : a Navigation object for common machinery.
        waypoint_ll : a (lat, lon) point marking where we'll try to stay close to.
        linger : time in seconds to stay there
        radius : distance in metres which we'll try to bounce around the waypoint
        wind_angle : the absolute wind angle to sail (in degrees) when inside
           radius. This will automatically be flipped according to the tack.
        """
        self.nav = nav
        self.waypoint = waypoint
        self.waypoint_id = waypoint_id
        self.waypoint_xy = Point(
            self.nav.latlon_to_utm(self.waypoint.lat.decimal_degree, self.waypoint.lon.decimal_degree))
        self.linger = linger
        self.radius = radius
        self.accept_radius = accept_radius
        self.start_time = None
        self.name = name
        self.debug_topics = [('dbg_station_time', 'Float32'), ]
        super(StationKeeping, self).__init__(**kwargs)
        self.last_wind_direction = None

    def update_waypoint(self, waypoint, waypoint_id = None):
        self.waypoint = waypoint
        self.waypoint_id = waypoint_id
        self.waypoint_xy = Point(
            self.nav.latlon_to_utm(self.waypoint.lat.decimal_degree, self.waypoint.lon.decimal_degree))

    def calculate_waypoint_ll(self):
        return self.waypoint

    def calculate_waypoint(self, waypoints_ll = None):
        waypoints, waypoints_ll = super(StationKeeping, self).calculate_waypoint(waypoints_ll)
        self.taskdict['tasks'] = [{
            'kind': 'to_waypoint_close', 'waypoint': waypoints
        }]
        return waypoints, waypoints_ll

    def calculate_tasks(self):
        self.calculate_waypoint()

    def need_update(self):
        return False

    def calculate_task_direct_rudder_control(self, dwp, hwp):
        return -hwp * 4.0 / 3

    def check_position(self):
        if self.start_time is not None:
            self.debug_pub('dbg_station_time', time.time() - self.start_time)
        if self.start_time is None and self.nav.position_ll.distance(self.waypoint) * 1000 <= self.accept_radius:
            self.start_time = time.time()
        if self.nav.position_ll.distance(self.waypoint) * 1000 <= self.radius:
            self.nav.direct = True
            dwp, hwp = self.nav.distance_and_heading(self.waypoint_xy)
            hwp -= self.nav.heading
            if hwp < -180:
                hwp += 360
            if hwp > 180:
                hwp -= 360
            self.nav.task_direct_rudder_control = self.calculate_task_direct_rudder_control(dwp, hwp)
            if abs(self.nav.task_direct_rudder_control) > self.nav.rudder_param['maxAngle']:
                self.nav.task_direct_rudder_control = self.nav.rudder_param[
                    'maxAngle'] if self.nav.task_direct_rudder_control > 0 else -self.nav.rudder_param['maxAngle']
            self.nav.task_direct_sailsheet_normalized = 0
        else:
            self.nav.direct = False
            self.nav.task_direct_rudder_control = 0
            self.nav.task_direct_sailsheet_normalized = 0

    def check_end_condition(self):
        "Are we done yet?"
        return self.start_time is not None and time.time() - self.start_time > self.linger
