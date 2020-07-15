import make_tasks
import tasks_runner


def make_tasks_runner(wp_params, nav):
    return tasks_runner.TasksRunner(make_tasks.make_tasks(wp_params, nav), nav)
