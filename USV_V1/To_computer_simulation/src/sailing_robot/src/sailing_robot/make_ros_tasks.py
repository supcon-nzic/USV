import expand_task_dict
import make_tasks


def expand_ros_task(taskdict, nav, name = '', index = None):
    """
        Turn a task dict from params (or from tasks_from_wps) into a task object
    """
    task = make_tasks.expand_task(taskdict, nav, name, index)
    return task


def make_ros_tasks(wp_params, nav, name = ''):
    return [expand_ros_task(taskdict = task, nav = nav, name = name, index = index) for index, task in
            enumerate(expand_task_dict.expand_task_dict(wp_params))]
