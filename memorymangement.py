def readfile():
    memory_file = open("memory.dat", "r")
    memory = []
    line = memory_file.readline()
    while line:
        line = line.split()
        memory.append(memory(int(line[0]), str(line[1]), int(line[2])))
        line = memory_file.readline()
    return memory
    #memory is an array that stores the PID, ACTION, and PAGE to take
def fifo(memory):
        page_table=[[],[20]]
        procces_table[page_table]
        for i in range(0, len(memory)):
            page_table.append([1])==memory[:19:1].process_id
            if page_table [[1][-1]]:
                for i in range (20, len(memory)):
                    page_table[0].append



if __name__== "__main__":
    memory = readfile()
    pagetable = []
    for i in range (0, len(memory)):
        if(memory[i].action == 'A'):
            pagetable.append(memory[i].process_id)
    for i in range (0, len(pagetable)):
        print(pagetable[i])

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
fifo(memory)