"""Base class for task classes.

This has almost no implementation; the debugging methods are injected by
tasks_ros. This allows us to test task classes outside ROS.
"""

import make_ros_tasks
import make_ros_tasks_runner


class TaskBase(object):
    debug_topics = []

    def start(self):
        pass

    def check_end_condition(self):
        pass

    def calculate_state_and_goal(self):
        pass

    def debug_pub(self, topic, value):
        pass

    def log(self, level, msg, *values):
        print(msg % values)

    def init_ros(self):
        pass


class ComplexTaskBase(TaskBase):
    def __init__(self, *args, **kwargs):
        self.taskdict = kwargs
        self.calculate_tasks()
        self.heading_plan = make_ros_tasks.make_ros_tasks(self.taskdict, self.nav, self.name + '/heading_plan')[0]
        self.debug_topics.extend(self.heading_plan.debug_topics)

    def init_ros(self):
        self.heading_plan.debug_pub = self.debug_pub

    def calculate_waypoint_ll(self):
        pass

    def calculate_waypoint(self, waypoints_ll = None):
        if waypoints_ll is None:
            waypoints_ll = self.calculate_waypoint_ll()
        return (waypoints_ll.lat.decimal_degree, waypoints_ll.lon.decimal_degree), waypoints_ll

    def calculate_tasks(self):
        self.taskdict['list'] = [self.calculate_waypoint()[0]]

    def need_update(self):
        return True

    def update_tasks(self, waypoint = None, waypoint_id = None, target_radius = None):
        if waypoint is not None:
            self.heading_plan.update_waypoint(waypoint, waypoint_id)
        if target_radius is not None:
            self.heading_plan.update_target_radius(target_radius)

    def check_position(self):
        pass

    def calculate_state_and_goal(self):
        """Work out what we want the boat to do
        """
        if self.need_update():
            self.update_tasks()
        self.check_position()
        return self.heading_plan.calculate_state_and_goal()


class TaskRunnerBasedTaskBase(TaskBase):
    def __init__(self, *args, **kwargs):
        self.taskdict = kwargs
        self.calculate_tasks()
        self.task_runner = make_ros_tasks_runner.make_ros_tasks_runner(self.taskdict, self.nav, self.name)
        self.task_runner.start_next_task()

    def calculate_waypoint_ll(self):
        pass

    def calculate_waypoint(self, waypoints_ll = None):
        if waypoints_ll is None:
            waypoints_ll = self.calculate_waypoint_ll()
        return [(waypoint.lat.decimal_degree, waypoint.lon.decimal_degree) for waypoint in waypoints_ll], waypoints_ll

    def calculate_tasks(self):
        pass

    def need_update(self):
        return True

    def update_tasks(self):
        pass

    def check_position(self):
        pass

    def calculate_state_and_goal(self):
        """Work out what we want the boat to do
        """
        if self.need_update():
            self.update_tasks()
        self.check_position()
        return self.task_runner.calculate_state_and_goal()
