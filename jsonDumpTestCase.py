
import src.JsonConvertor.JsonDump as js
import src.JsonConvertor.Jsonio as jsio
import src.JsonConvertor.JSONUtil as jsutil


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
    jsonDump = js.JsonDump(student1)
    #print(jsonDump.dumps())
    jsonUtilObj=jsutil.JsonUtil("demo.js",'C:\\DataStore\\dataFile\\')
    #isInserted = jsonUtilObj.insertRecord("0704CS",student1)
    #print(isInserted)
    #isInserted = jsonUtilObj.insertRecord("3450IT",student2)
    #print(isInserted)
    #print(jsonUtilObj.getDictionary())
    #read the data from the file based on the given key
    #print(jsonUtilObj.readRecord("928"))
    #print(jsonUtilObj.keyExists("0704CS"))
    #print(jsonUtilObj.readRecord("0704CS"))
    #print(type(jsonUtilObj.readRecord("0704CS")))
    print(jsonUtilObj.deleteRecord("0704CS"))
    print(jsonUtilObj.readRecord("3450IT"))