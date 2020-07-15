import expand_task_dict

import heading_planning_laylines
import return_to_safety
import jibe_tack_now
import timeout
import station_keeping
import heading_planning_laylines_closely

build_task_dict = {
    'to_waypoint': heading_planning_laylines.HeadingPlan,
    'to_waypoint_close': heading_planning_laylines_closely.HeadingPlan,
    'keep_station': station_keeping.StationKeeping,
    'return_to_safety_zone': return_to_safety.ReturnToSafetyZone,
    'start_timer': timeout.StartTimer,
    'jibe_tack_now': jibe_tack_now.JibeTackNow
}


def expand_task(taskdict, nav, name='', index=None):
    """
        Turn a task dict from params (or from tasks_from_wps) into a task object
    """
    kind = taskdict.get('kind', None)
    jump_label = taskdict.get('jump_label', None)
    name += '/' + kind
    if index is not None:
        name += '_' + str(index)
    if kind in build_task_dict:
        task = build_task_dict[kind](nav=nav, name=name, **taskdict)
    else:
        raise ValueError("Unknown task type: {}".format(kind))

    task.task_kind = kind
    task.jump_label = jump_label
    return task


def make_tasks(wp_params, nav):
    return [expand_task(task, nav) for task in expand_task_dict.expand_task_dict(wp_params)]
