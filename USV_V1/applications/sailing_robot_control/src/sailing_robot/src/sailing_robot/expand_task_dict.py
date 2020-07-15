import LatLon


def expand_id(wp_params):
    if 'table' not in wp_params:
        return wp_params
    coordinates = wp_params['table']
    if 'tasks' in wp_params:
        # Long specification: list of tasks
        for wp_task in wp_params['tasks']:
            if isinstance(wp_task['waypoint'], str):
                wp_task['waypoint_id'] = wp_task['waypoint']
                wp_task['waypoint'] = coordinates[wp_task['waypoint']]
    else:
        # Short specification: just a series of waypoints to go around
        if isinstance(wp_params['list'][0], str):
            wp_params['id_list'] = wp_params['list']
            wp_params['list'] = [coordinates[wpid] for wpid in wp_params['list']]

    return wp_params


def expand_task_dict(wp_params):
    wp_params = expand_id(wp_params)
    target_radius = wp_params['target_radius']
    tack_voting_radius = wp_params['tack_voting_radius']

    def expand_to_waypoint(wp, wpid = ''):
        return {
            'kind': 'to_waypoint',
            'waypoint': LatLon.LatLon(*wp),
            'waypoint_id': wpid,
            'target_radius': target_radius,
            'tack_voting_radius': tack_voting_radius
        }

    res = []
    if 'tasks' in wp_params:
        # Long specification: list of tasks
        for wp_task in wp_params['tasks']:
            kind = wp_task['kind']
            expanded_task = {
                'kind': kind,
                'waypoint': LatLon.LatLon(*wp_task['waypoint']),
                'waypoint_id': wp_task.get('waypoint_id', None),
                'target_radius': wp_task.get('target_radius', target_radius),
                'tack_voting_radius': wp_task.get('tack_voting_radius', tack_voting_radius)
            }
            if kind == 'to_waypoint':
                pass
            elif kind == 'to_waypoint_keep_station_obstacle':
                expanded_task.update({
                    'target_radius': wp_task.get('target_radius', 2)
                })
            elif kind == 'to_waypoint_close':
                expanded_task.update({
                    'close_factor': wp_task.get('close_factor', 0.8)
                })
            elif kind == 'to_waypoint_offset':
                expanded_task.update({
                    'offset_distance': wp_task.get('offset_distance', 0.0),
                    'offset_heading': wp_task.get('offset_heading', 0.0),
                })
            elif kind == 'keep_station':
                expanded_task.update({
                    'linger': wp_task.get('linger', 300),
                    'radius': wp_task.get('radius', 3),
                    'accept_radius': wp_task.get('accept_radius', 15)
                })
            elif kind == 'keep_station_obstacle':
                expanded_task.update({
                    'linger': wp_task.get('linger', 180),
                    'radius': wp_task.get('radius', 3),
                    'min_radius': wp_task.get('min_radius', 1),
                    'max_radius': wp_task.get('max_radius', 5),
                    'accept_radius': wp_task.get('accept_radius', 20)
                })
            elif kind == 'start_timer':
                expanded_task = wp_task.copy()
            else:
                continue

            # Copy over any jump label
            expanded_task['jump_label'] = wp_task.get('jump_label', None)
            res.append(expanded_task)
    else:
        # Short specification: just a series of waypoints to go around
        if 'id_list' not in wp_params:
            wp_params['id_list'] = [''] * len(wp_params['list'])
        for wp, wpid in zip(wp_params['list'], wp_params['id_list']):
            res.append(expand_to_waypoint(wp, wpid))

    return res
