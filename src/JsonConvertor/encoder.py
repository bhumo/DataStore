from json import JSONEncoder

"""
Class ObjToJsonEncoder extends JSONEncoder class
and over-rides default() method
The object of this class is useful for encoding any python object
and returns the dictionary where property of the object is key and the value is the address of object that porperty holds 



"""

class ObjToJsonEncoder(JSONEncoder):
    def default(self,object):
        return object.__dict__