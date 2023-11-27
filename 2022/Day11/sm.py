from dataclasses import dataclass
from math import floor
@dataclass
class StateMachine:
    memory: dict[str,int]
    program: list[str]

    def run(self):
        current_line = 0
        while current_line < len(self.program):
            instruction = self.program[current_line]

            #set register to a value
            if instruction.startswith("set "):
                register,value = instruction[4], int(instruction[6:])
                self.memory[register] = value

            elif instruction.startswith("inc "):
                register = instruction[4]
                self.memory[register] += 1
            
            current_line += 1

@dataclass 
class Monkey:
    ID: int
    PackofItems: list[int]
    Operation: str
    Test: str
    IftrueTest: str
    IffalseTest: str
    handleCount: int = 0 
    currentItem: int = 0 
    opdValue: int = 0

    def runTest(self):
        if self.Test.lower().startswith('div'):
            modVal = int(self.Test.split(" ")[2])
            if (self.opdValue % modVal) == 0:
                return self.IftrueTest.split(' ')[3]
            else:
                return self.IffalseTest.split(' ')[3]

    def OpRun(self):
        exp = self.Operation.replace("new = ","").replace("old",str(self.currentItem))
        newval = self.numeric(exp)
        
        self.opdValue = floor(newval / 3)

    def removeitem(self,item):
        #self.PackofItems.remove(item)
        self.PackofItems.remove(item)
        return self.PackofItems
    
    def additem(self,item):
        self.PackofItems.append(item)
        return self.PackofItems
    
    def incrHandleCount(self):
        self.handleCount += 1
        return self.handleCount
    
    def numeric(self, equation):
        if '+' in equation:
            y = equation.split('+')
            x = int(y[0])+int(y[1])
        elif '-' in equation:
            y = equation.split('-')
            x = int(y[0])-int(y[1])
        elif '*' in equation:
            y = equation.split('*')
            x = int(y[0])*int(y[1])
        
        return x
    
    def getItem(self):
        if len(self.PackofItems) > 0:
            tmpItem = self.PackofItems[0]
            self.removeitem(tmpItem)
            self.currentItem = tmpItem
            
        else:
            self.currentItem = -1
            

    