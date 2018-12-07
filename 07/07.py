class Worker:
    def __init__(self, task=None, start=None):
        self.task = task
        self.start = start

    @property
    def end(self):
        return self.start + 60 + ord(self.task) - 64

def find_possibilities(instr_map, req_map, performed):
    poss = [x for x in instr_map if x not in req_map]
    for task in performed:
        if task not in instr_map:
            poss += [task]
        else:
            poss += instr_map[task]
    poss = list(set(poss))
    poss = [x for x in poss
            if len(performed) == len(set(req_map.get(x, []) + performed)) and x not in performed]
    return poss

def find_task_order(instr_map, req_map):
    performed = []
    possible = find_possibilities(instr_map, req_map, performed)
    while possible:
        next_task = min(possible)
        performed += [next_task]
        possible = find_possibilities(instr_map, req_map, performed)
    print("".join(performed))

def any_working(workers):
    for worker in workers:
        if worker.task:
            return True
    return False

def find_order_with_workers(instr_map, req_map, workers):
    performed = []
    time = 0
    possible = find_possibilities(instr_map, req_map, performed)
    workers[0].task = min(possible)
    workers[0].start = 0
    in_progress = [min(possible)]
    possible.remove(min(possible))
    while any_working(workers) or possible:
        for i, worker in enumerate(workers):
            if worker.task and worker.end == time:
                performed += [worker.task]
                worker.task = None
                # print("Finished!", i)
        possible = find_possibilities(instr_map, req_map, performed)
        possible = [p for p in possible if p not in in_progress]
        for i, worker in enumerate(workers):
            if not worker.task and possible:
                worker.task = min(possible)
                in_progress += [worker.task]
                worker.start = time
                # print(i, worker.task, worker.start, worker.end)
                possible.remove(worker.task)
        time += 1
    # print("".join(performed))
    print(time - 1)

if __name__ == "__main__":
    f = open("07.txt", "r")
    instructions_txt = f.read().splitlines()

    instruction_map = {}
    requirement_map = {}
    for instruction in instructions_txt:
        prereq, task = instruction.split(" ")[1], instruction.split(" ")[7]
        instruction_map[prereq] = instruction_map.get(prereq, []) + [task]
        requirement_map[task] = requirement_map.get(task, []) + [prereq]
    for key in instruction_map:
        instruction_map[key] = sorted(instruction_map[key])

    # -- Part 1 --
    find_task_order(instruction_map, requirement_map)

    # -- Part 2 --
    workers = [Worker() for i in range(5)]
    find_order_with_workers(instruction_map, requirement_map, workers)
