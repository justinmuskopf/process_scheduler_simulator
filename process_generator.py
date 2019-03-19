"""
Course: CSCE 4600, Spring 2019
Authors: Fischer Davis, Jacob Montes, Justin Muskopf
Instructor: A.Mikler
Assignment: Project 1
"""
from random import randint

KB = 1024
MB = KB * 1024
GB = MB * 1024

PID = 0
FOOTPRINT = 1
CPU_CYCLES = 2


class ProcessGenerator:
    MINIMUM_MEMORY_FOOTPRINT = 0.25 * MB
    MAXIMUM_MEMORY_FOOTPRINT = 8 * GB

    MINIMUM_CPU_CYCLES = 10e6
    MAXIMUM_CPU_CYCLES = 50e12

    MIN_PID = 1
    MAX_PID = pow(2, 15)

    DESC_STRINGS = ["PID", "Memory Footprint", "CPU Cycles"]

    def __init__(self):
        self.generated_pids = []

    def _get_random_memory_footprint(self):
        return randint(self.MINIMUM_MEMORY_FOOTPRINT, self.MAXIMUM_MEMORY_FOOTPRINT)

    def _get_random_cpu_cycles(self):
        return randint(self.MINIMUM_CPU_CYCLES, self.MAXIMUM_CPU_CYCLES)

    def _get_random_pid(self):
        pid = randint(self.MIN_PID, self.MAX_PID)
        while pid in self.generated_pids:
            pid = randint(self.MIN_PID, self.MAX_PID)

        return pid

    def get_new_process(self):
        pid = self._get_random_pid()
        memory_footprint = self._get_random_memory_footprint()
        cpu_cycles = self._get_random_cpu_cycles()

        process = (pid, memory_footprint, cpu_cycles)

        self.generated_pids.append(pid)

        return process

    def get_n_new_processes(self, n):
        processes = [self.get_new_process() for _ in range(n)]

        return processes
