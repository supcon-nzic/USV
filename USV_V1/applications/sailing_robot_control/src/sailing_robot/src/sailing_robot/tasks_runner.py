"""Machinery to step through tasks.

This can be tested without ROS; ros_tasks_runner.py contains a subclass which
integrates with ROS to publish logging and debugging topics.
"""

from __future__ import print_function

import time


class TimedEnd(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.ends_at = None

    def start(self):
        self.ends_at = time.time() + self.seconds

    def check(self):
        return time.time() > self.ends_at


class TasksRunner(object):
    def __init__(self, tasks, nav):
        self.task_ix = -1
        self.active_task = None
        self.nav = nav
        self._jump_next = None
        self.tasks = tasks
        self.check_jump_labels()

    def update_tasks(self, tasks, task_ix = 0):
        self.task_ix = task_ix
        self.tasks = tasks
        self.active_task = self.tasks[task_ix]

    def check_jump_labels(self):
        jump_labels = set([t.jump_label for t in self.tasks if t.jump_label is not None])
        for t in self.tasks:
            if t.task_kind == 'start_timer':
                if t.jump_to not in jump_labels:
                    raise ValueError('Timer tries to jump to %r, label not found' % t.jump_to)

    @staticmethod
    def log(level, msg, *values):
        print(msg % values)

    on_temporary_task = False

    def start_next_task(self):
        """Step to the next task, making it the active task.
        """
        self.task_ix += 1
        if self.task_ix >= len(self.tasks):
            self.log('warning', "Run all tasks, returning to start")
            self.task_ix = 0

        self.active_task = self.tasks[self.task_ix]
        self.on_temporary_task = False
        endcond = ''  # TODO
        self.log('info', "Running task {}: {} with end condition {}".format(self.task_ix, self.active_task.task_kind,
                                                                            '/'.join(endcond)))
        self.active_task.start()

    def set_jump(self, label):
        """Jump callback to jump to task on next time step."""
        self._jump_next = label

    def process_jump(self):
        """If a jump is set, go to that task, and clear the jump.

        Returns True if a jump occurred.
        """
        if self._jump_next is None:
            return False

        label = self._jump_next
        self._jump_next = None
        for i, task in enumerate(self.tasks):
            if task.jump_label == label:
                self.task_ix = i
                self.on_temporary_task = False
                self.active_task = self.tasks[self.task_ix]
                self.active_task.start()
                self.log('warning', "Jumped to task {}: {}".format(self.task_ix, self.active_task.task_kind))
                return True

        self.log('error', "Couldn't find jump label %r", label)
        return False

    def insert_task(self, taskdict):
        """Do a temporary task.

        After completing the temporary task, control will be return to the
        regular task that was active before the temporary task was started.
        """
        # Decrease task_ix so we go back to the current task when this is done.
        if not self.on_temporary_task:
            self.task_ix -= 1
        self.on_temporary_task = True
        self.active_task = self._make_task(taskdict)
        self.active_task.start()
        self.log('info', "Running intermediate task: {}".format(taskdict['kind']))

    def calculate_state_and_goal(self):
        """Use the active task to calculate what to do now.
        
        Before using the active task, checks if it should go to the next task.

        If a safety zone is specified, also checks if we're (nearly) out of it.
        """
        self.process_jump()

        if self.active_task.check_end_condition():
            self.start_next_task()

        if self.nav.check_safety_zone() and self.active_task.task_kind != 'return_to_safety_zone':
            # We're about to wander out of the safety zone!
            self.log('warning', 'At edge of safety zone')
            self.insert_task({'kind': 'return_to_safety_zone'})

        self.debug_pub(self.name + '/task_ix', self.task_ix)
        self.debug_pub(self.name + '/active_task_kind', self.active_task.task_kind)

        return self.active_task.calculate_state_and_goal()

    def debug_pub(self, topic, value):
        pass  # Overridden in subclass to send ROS message
