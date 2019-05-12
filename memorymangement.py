def readfile():
    memory_file = open("memory.dat", "r")
    memory = []
    line = memory_file.readline()
    while line:
        line = line.split()
        memory.append(memory(int(line[0]), int(line[1]), int(line[2])))
        line = memory_file.readline()
    return memory


class Job:
    def __init__(self, process_id, action, page):
        self.process_id = process_id
        self.action= action
        self.page = page

        self.C = None
        self.T = None
        self.A = None
        self.R = None
        self.W= None
        self.F= None
        self.pages= None

    def __repr__(self):
        return "process_id : {}, action: {},page: {}"\
            .format(self.process_id, self.action, self.page)