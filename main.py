"""
Course: CSCE 4600, Spring 2019
Authors: Fischer Davis, Jacob Montes, Justin Muskopf
Instructor: A.Mikler
Assignment: Project 1
"""
from process_generator import ProcessGenerator, PID, FOOTPRINT, CPU_CYCLES
from process_scheduler import ProcessScheduler

"""
1. Creates a process generator
2. Generates and returns 200 processes
"""
def Get_200_Processes():
    pg = ProcessGenerator()

    return pg.get_n_new_processes(200)


# Generates "question_`q_num`_processes.txt", which contains all of a scheduler's processes
# Generates "question_`q_num`_processors.txt", which contains all of a scheduler's processors
def output_scheduler_to_file(scheduler, q_num):
    proc_file = open("question_{}_processes.txt".format(q_num), "w")
    proc_file.write("PID\tMEM\tCYCLES\n")
    for process in scheduler.queued_processes:
        line = "{}\t{}\t{}\n".format(process[PID], process[FOOTPRINT], process[CPU_CYCLES])
        proc_file.write(line)
    proc_file.close()

    cpu_file = open("question_{}_processors.txt".format(q_num), "w")
    cpu_file.write("CPU_NUM\tSPEED\tMEMORY\tTOTAL_CYCLES\tTOTAL_TIME\n")
    for cpu in scheduler.get_processors():
        line = "{}\t{}\t{}\t{}\t{}\n".format(
            cpu.number,
            cpu.speed_in_ghz,
            cpu.memory_in_gb,
            cpu.total_cpu_cycles(),
            cpu.total_execution_time()
        )
        cpu_file.write(line)
    cpu_file.close()

"""
1. Gets 200 processes
2. Creates a process scheduler
3. Adds 5 identical processors to scheduler
4. Adds the processes to the scheduler
"""
def Question_1():
    processes = Get_200_Processes()

    scheduler = ProcessScheduler(question_number=1)

    scheduler.add_n_processors(n=5)

    scheduler.add_processes(processes)

    output_scheduler_to_file(scheduler, 1)


"""
1. Gets 200 processes
2. Creates a process scheduler
3. Adds 5 processors to scheduler
    - 2 processors of 4GHz speed and 2GB memory
    - 2 processors of 4GHz speed and 4GB memory
    - 1 processor of 4GHz speed and 8GB memory
4. Adds the processes to the scheduler
"""
def Question_2():
    processes = Get_200_Processes()

    scheduler = ProcessScheduler(question_number=2)

    scheduler.add_n_processors(n=2, speed_in_ghz=4, memory_in_gb=2)
    scheduler.add_n_processors(n=2, speed_in_ghz=4, memory_in_gb=4)
    scheduler.add_processor(speed_in_ghz=4, memory_in_gb=8)

    scheduler.add_processes(processes)

    output_scheduler_to_file(scheduler, 2)
"""
1. Gets 200 processes
2. Creates a process scheduler
3. Adds 5 identical processors to scheduler
    - 2 processors of 2GHz speed and 8GB memory
    - 2 processors of 3GHz speed and 8GB memory
    - 1 processor of 4GHz speed and 8GB memory
4. Adds the processes to the scheduler
"""
def Question_3():
    processes = Get_200_Processes()

    scheduler = ProcessScheduler(question_number=3)

    scheduler.add_n_processors(n=2, speed_in_ghz=2, memory_in_gb=8)
    scheduler.add_n_processors(n=2, speed_in_ghz=3, memory_in_gb=8)
    scheduler.add_processor(speed_in_ghz=4, memory_in_gb=8)

    scheduler.add_processes(processes)

    output_scheduler_to_file(scheduler, 3)

"""
1. Creates a process generator
2. Creates a process scheduler
3. Adds 5 processors to scheduler
    - 2 processors of 2GHz speed and 8GB memory
    - 2 processors of 3GHz speed and 8GB memory
    - 1 processor of 4GHz speed and 8GB memory 
4. Sequentially adds a process to scheduler 200 times
"""
def Question_4():
    pg = ProcessGenerator()

    scheduler = ProcessScheduler(question_number=3)

    scheduler.add_n_processors(n=2, speed_in_ghz=2, memory_in_gb=8)
    scheduler.add_n_processors(n=2, speed_in_ghz=3, memory_in_gb=8)
    scheduler.add_processor(speed_in_ghz=4, memory_in_gb=8)

    # Sequentially generate and add a process, 200 times
    for i in range(200):
        process = pg.get_new_process()
        scheduler.add_process(process)

    scheduler.print_limiting_cpu()

    output_scheduler_to_file(scheduler, 4)

# Waits for TA to press enter or literally anything
def wait():
    print()
    input("Press Enter to Continue...")
    print()


if __name__ == "__main__":
    Question_1()
    wait()
    Question_2()
    wait()
    Question_3()
    wait()
    Question_4()
    wait()
