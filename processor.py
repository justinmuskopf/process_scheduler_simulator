"""
Course: CSCE 4600, Spring 2019
Authors: Fischer Davis, Jacob Montes, Justin Muskopf
Instructor: A.Mikler
Assignment: Project 1
"""
from process_generator import PID, FOOTPRINT, CPU_CYCLES, GB

class Processor:
    def __init__(self, proc_num, speed_in_ghz, memory_in_gb):
        self.number = proc_num

        self.speed_in_ghz = speed_in_ghz
        self.cycles_per_second = self.speed_in_ghz * 1e9

        self.memory_in_gb = memory_in_gb
        self.memory_in_bytes = self.memory_in_gb * GB

        self.processes = []

    @staticmethod
    def _print_process(process):
        print("| PID: {}".format(process[PID]))
        print("| CPU Cycles: {}".format(process[CPU_CYCLES]))
        print("| Memory Footprint (B): {}".format(process[FOOTPRINT]))

    def print_processes(self):
        for process in self.processes:
            self._print_process(process)

    def total_footprint(self):
        return sum([p[FOOTPRINT] for p in self.processes])

    def total_cpu_cycles(self):
        return sum([p[CPU_CYCLES] for p in self.processes])

    def get_processes(self):
        return self.processes

    def num_processes(self):
        return len(self.processes)

    def process_execution_time(self, process):
        return process[CPU_CYCLES] / self.cycles_per_second

    def total_execution_time(self):
        return sum([self.process_execution_time(p) for p in self.processes])

    def memory_usage(self):
        return round(self.total_footprint() / self.memory_in_bytes, 2)

    def memory_remaining(self):
        return self.memory_in_bytes - self.total_footprint()

    def print_statistics(self):
        total_cycles = self.total_cpu_cycles()

        print("=== PROCESSOR {} ===".format(self.number))
        print("--- Speed: {} GHz".format(self.speed_in_ghz))
        print("--- Total CPU cycles: {}, ({}s to execute all)".format(
            total_cycles,
            round(self.total_execution_time(), 2))
        )
        print()

    def add_process(self, process):
        self.processes.append(process)
