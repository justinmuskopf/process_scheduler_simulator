"""
Course: CSCE 4600, Spring 2019
Authors: Fischer Davis, Jacob Montes, Justin Muskopf
Instructor: A.Mikler
Assignment: Project 1
"""
from process_generator import CPU_CYCLES, FOOTPRINT
from processor import Processor

class ProcessScheduler:
    def __init__(self, question_number):
        self.processors = []
        self.queued_processes = []
        self.question_number = question_number

    # Adds a processor to the scheduler
    def add_processor(self, speed_in_ghz=4, memory_in_gb=8):
        proc_num = len(self.processors) + 1

        processor = Processor(proc_num, speed_in_ghz, memory_in_gb)

        self.processors.append(processor)

    # Adds n processors of the same characteristics to the scheduler
    def add_n_processors(self, n, speed_in_ghz=4, memory_in_gb=8):
        for _ in range(n):
            self.add_processor(speed_in_ghz, memory_in_gb)

    # Adds a single process to the scheduler, and schedules
    def add_process(self, process):
        self._schedule_4(process)

    # Adds a list of processes to the scheduler, and schedules
    def add_processes(self, processes):
        self.queued_processes = processes

        self._schedule()

    def get_processors(self):
        return self.processors

    def print_processors(self):
        for processor in self.processors:
            processor.print_statistics()

    # Returns the list of processors sorted by cycles (min -> max)
    def _cpus_sorted_by_cycles(self):
        return sorted(self.processors, key=lambda x: x.total_cpu_cycles())

    # Returns the processor with the least cycles
    def _cpu_with_least_cycles(self):
        return self._cpus_sorted_by_cycles()[0]

    # Returns the processor with the most cycles
    def _cpu_with_most_cycles(self):
        return self._cpus_sorted_by_cycles()[-1]

    # Returns the processor with the least cycles that has sufficient memory
    def _cpu_with_least_cycles_and_sufficient_memory(self, memory_required):
        for cpu in self._cpus_sorted_by_cycles():
            if cpu.memory_in_bytes >= memory_required:
                return cpu

    # Returns processors sorted by their total execution time
    def _cpus_sorted_by_execution_time(self):
        return sorted(self.processors, key=lambda x: x.total_execution_time())

    # Returns the processor with the shortest total execution time
    def _cpu_with_shortest_total_execution_time(self):
        return self._cpus_sorted_by_execution_time()[0]

    # Returns the processor with the longest total execution time
    def _cpu_with_longest_total_execution_time(self):
        return self._cpus_sorted_by_execution_time()[-1]

    # Returns the processor with the shortest execution time after adding
    # the time it takes for the processor to execute it to its current total
    def _cpu_with_shortest_added_execution_time(self, process):
        cpus_with_added_times = []

        for cpu in self.processors:
            # Total execution time of cpu after adding new process
            time_after_add = cpu.total_execution_time() + cpu.process_execution_time(process)

            cpu_dict = {'time': time_after_add, 'cpu': cpu}

            cpus_with_added_times.append(cpu_dict)

        # Sort cpus by time after adding new process and get first
        cpus_sorted_by_added_time = sorted(cpus_with_added_times, key=lambda x: x['time'])
        first_cpu_in_sort = cpus_sorted_by_added_time[0]

        return first_cpu_in_sort['cpu']

    # Returns the queued processes sorted by cycles
    def _processes_sorted_by_cycles(self):
        return sorted(self.queued_processes, key=lambda x: x[CPU_CYCLES])

    # Returns the cpu with the greatest total execution time
    def limiting_cpu(self):
        return self._cpu_with_longest_total_execution_time()

    # Prints the processor that has the greatest total execution time
    def print_limiting_cpu(self):
        print("-Limiting Processor:")
        self.limiting_cpu().print_statistics()

    # Chooses which schedule function to call based on question number
    def _schedule(self):
        print("Scheduling processes...")
        q = self.question_number
        if q == 1:
            self._schedule_1()
        elif q == 2:
            self._schedule_2()
        elif q == 3:
            self._schedule_3()

    # The first question's scheduling function
    def _schedule_1(self):
        sorted_by_cycles = self._processes_sorted_by_cycles()

        # Until all processes have been scheduled
        while sorted_by_cycles:
            processor = self._cpu_with_least_cycles()
            process = sorted_by_cycles.pop(0)

            processor.add_process(process)

        self.print_limiting_cpu()

    # The second question's scheduling function
    def _schedule_2(self):
        sorted_by_cycles = self._processes_sorted_by_cycles()

        # Until all processes have been scheduled
        while sorted_by_cycles:
            process = sorted_by_cycles.pop(0)
            processor = self._cpu_with_least_cycles_and_sufficient_memory(process[FOOTPRINT])

            processor.add_process(process)

        self.print_limiting_cpu()

    # The third question's scheduling function
    def _schedule_3(self):
        sorted_by_cycles = self._processes_sorted_by_cycles()

        # Until all processes have been scheduled
        while sorted_by_cycles:
            process = sorted_by_cycles.pop(0)
            processor = self._cpu_with_shortest_added_execution_time(process)

            processor.add_process(process)

        self.print_limiting_cpu()

    # The fourth question's scheduling function
    def _schedule_4(self, process):
        processor = self._cpu_with_shortest_added_execution_time(process)

        processor.add_process(process)
