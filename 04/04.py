
class Guard:
    def __init__(self, guard_id):
        self.guard_id = guard_id
        self.sleep_times = [] # list of ranges
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


