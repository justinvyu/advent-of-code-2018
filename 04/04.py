import numpy as np


class Guard:
    def __init__(self, guard_id):
        self.guard_id = guard_id
        self.sleep_times = np.zeros(60)
        self.awake = True

class Log:
    def __init__(self, guard_id, date, time):
        self.guard_id = guard_id
        self.date = date
        self.time = time
        self.year, self.month, self.day = date
        self.hour, self.minute = time

    def __str__(self):
        return "#{0}, date: {1}, time: {2}".format(self.guard_id, self.date, self.time)

def convert_log_str(log, guard=None):
    """
    Parses a log entry to extract data:
        1. Timestamp
        2. Guard ID
        3. Asleep times
    [1518-05-24 23:56] Guard #1721 begins shift
    [1518-08-22 00:09] falls asleep
    """
    timestamp, rest = log[1:].split("] ")
    date, time = timestamp.split(" ")
    year, month, day = [int(x) for x in date.split("-")]
    hour, minute = [int(x) for x in time.split(":")]

    if "#" in rest:
        _, rest = rest.split("#")
        guard_id = int(rest.split(" ", 1)[0])
        return Log(guard_id, (year, month, day), (hour, minute))
    else:
        if rest.split(" ", 1)[0] == "falls": # Falls asleep
            pass
        return Log(None, (year, month, day), (hour, minute))

if __name__ == "__main__":
    f = open("04.txt", "r")
    logs_txt = f.readlines()

    logs_data = [convert_log_str(log) for log in logs_txt]
    logs_data.sort(key=lambda log: log.date + log.time)

    guards = {}
    curr_guard = None
    sleep_start = 0
    sleep_end = 0
    for log in logs_data:
        if type(log.guard_id) == int:
            if log.guard_id not in guards:
                curr_guard = Guard(log.guard_id)
                guards[log.guard_id] = curr_guard
            else:
                curr_guard = guards[log.guard_id]
        else:
            if curr_guard.awake:
                sleep_start = log.minute
                curr_guard.awake = False
            else:
                sleep_end = log.minute
                for t in range(sleep_start, sleep_end):
                    curr_guard.sleep_times[t] = curr_guard.sleep_times[t] + 1
                curr_guard.awake = True

    # -- Part #1: Find sleepiest guard --
    guard_lst = list(guards.values())
    guard_lst.sort(key=lambda guard: -sum(guard.sleep_times))
    sleepiest = guard_lst[0]
    print(sleepiest.guard_id * np.argmax(sleepiest.sleep_times))

    # -- Part #2: Find most frequent guard (at certain minute) --

    guard_lst.sort(key=lambda guard: -max(guard.sleep_times))
    most_frequent = guard_lst[0]
    print(most_frequent.guard_id * np.argmax(most_frequent.sleep_times))
