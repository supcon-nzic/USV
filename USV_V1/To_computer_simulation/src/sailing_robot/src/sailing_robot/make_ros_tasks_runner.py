import make_ros_tasks
import ros_tasks_runner


def make_ros_tasks_runner(wp_params, nav, name = ''):
    return ros_tasks_runner.RosTasksRunner(make_ros_tasks.make_ros_tasks(wp_params, nav, name), nav = nav, name = name)
