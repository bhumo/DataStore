import src.Manager as manager
from threading import Thread,Lock

class Department:
    def __init__(self,name,code):
        self.name=name
        self.code=code

class Student:
    def __init__(self,name,rollNumber,department):
        self.name=name
        self.rollNumber=rollNumber
        self.department=department


class InsertMultiThread(Thread):

    def __init__(self,dsManager,startValue,end):
        Thread.__init__(self)
        self.lock = Lock()
        self.dsManager = dsManager
        self.startValue = startValue
        self.end=end

    def run(self):
        #try inserting 100 records
        name = "Bhumika"
        rollNumber = 20
        department = "CS101" 
        student1 = Student(name,rollNumber,department)
        for i in range(self.startValue,self.end+1):
            print("Record produced" +str(i))
            self.dsManager.insertRecord(str(i),student1)
            print("Record inserted "+ str(i))
        
         
if __name__ == "__main__":

    dsManager = manager.DataStoreManager.getInstance("demoMulti.json","C:\\DataStore\\dataFile\\")
    t1 = InsertMultiThread(dsManager,1,100)
    print(type(t1))
    t1.start()
    t2 = InsertMultiThread(dsManager,500,600)
    t2.start()
    
    
