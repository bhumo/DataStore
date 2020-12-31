import src.Manager as manager

class Department:
    def __init__(self,name,code):
        self.name=name
        self.code=code

class Student:
    def __init__(self,name,rollNumber,department):
        self.name=name
        self.rollNumber=rollNumber
        self.department=department


if __name__ == "__main__":
    department1=Department("Computer Science","CS101")
    student1=Student("Bhumika Gupta",10,department1)
    student2 = dict()
    student2["name"] = "Rekha Gupta"
    student2["rollNumber"] = 20
    student2["department"] = "IT"
    student2["subject"] = [ "DSA","DBMS","OS","OOPS"]
    managerDB = manager.DataStoreManager.getInstance("demo.json","C:\\DataStore\\dataFile\\")
    print(type(managerDB))
    print(managerDB.insertRecord("0704CS",student1))
    print(managerDB.readRecord("0704CS"))
    print(managerDB.keyExists("0704CS"))
    print(managerDB.getAllRecords())
    print(managerDB.deleteRecord("recordNotExists"))