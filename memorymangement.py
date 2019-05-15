def readfile():
    memory_file = open("memory.dat", "r")
    memory = []
    page = []
    line = memory_file.readline()
    while line:
        line = line.split()
        memory.append(Job(int(line[0]), str(line[1]), int(line[2])))
        line = memory_file.readline()
    return memory
    #memory is an array that stores the PID, ACTION, and PAGE to take
def printResult(x):
    print("PROCESS ID: ", end= " ")
    print(x.process_id)
    #print("\t", end="\t")
    for i in range(0, len(x.virtual)):
        print("Virtual: ", end=" ")
        print(x.virtual[i], end="\t")
        print("Physical: ", end=" ")
        print(x.physical[i])
        print("\n")

def fullPhysicalFIFO(x):
    #FIFO Handler if physical is full
    pass         

def freePage(x):
    pass

def terminateProcess(x):
    pass

class Job:
    def __init__(self, process_id, action, page):
        self.process_id = process_id
        self.action= action
        self.page = page

        self.R = 0
        self.W= 0
        self.virtual = []
        self.physical = []
    def __repr__(self):
        return "process_id : {}, action: {},page: {}"\
            .format(self.process_id, self.action, self.page)

if __name__== "__main__":
    memory = readfile()
    physical = []
    activeProcess = []
    for i in range (0, len(memory)):
        if(memory[i].action == 'C'):
            activeProcess.append(memory[i])
    for i in range (0, len(activeProcess)):
        for j in range (0, len(memory)):
            if(memory[j].process_id == activeProcess[i].process_id):
                if(memory[j].action == 'A'):
                    activeProcess[i].virtual.append(memory[j].page)
                    physical.append(memory[i].process_id)
                    activeProcess[i].physical.append(len(physical) - 1)
                if(memory[j].action == 'R'):
                    activeProcess[i].R = 1
                if(memory[j].action == 'W'):
                    activeProcess[i].W = 1
                if(memory[j].action == 'F'):
                    freePage(memory[i])
                if(memory[j].action == 'T'):
                    terminateProcess(memory[i])
    
    for i in range (0, len(activeProcess)):
            #printResult(memory[i])
            printResult(activeProcess[i])
    '''
    memory = readfile()
    physical = []
    for i in range (0, len(memory)):
        if(len(physical) == 20):
            fullPhysical(physical[i])
        elif(memory[i].action == 'A'):
            physical.append(memory[i])
            memory[i].virtual.append(memory[i].page)
            memory[i].physical.append(len(physical))
    for i in range (0, len(physical)):
       print(physical[i])
    '''
