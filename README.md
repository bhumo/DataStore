# DataStore
DataStore is written in Python Language and supportes multi threading.

# Table Of Contents
- [Dependencies](#dependencies)
- [SetUp](#setup)
- [How to Use](#how-to-use)
- [Documentation](#documentation)

# Dependencies
* Python version 3.1.4 or above

# SetUp
* Install the above dependencies

# How To Use

1. Import the module src.Manager
2. To get the reference of data store object, call the method src.Manager.DataStore.getInstance(fileName,location)
3. To perform the operations simple place a call to the functions provided by the DataStore class

# Documentation

The DataStore class (pacakge src.Manager) provides various methods for performing various operations on the data store

| Method Name | Argument(s) | Return Type | Description |
| :-- | :-- | :-- | :-- |
| getInstance| fileName, location(optional) | DataStoreManager | Used to initialise the dataStore |
| insertRecord | key, value| boolean | Insert the record in datastore as key(str) and value(JSON object) pair, if key exists throws an error and if inserted true else false|
| readRecord | key | str/None | If given key is present then return the assosiated json object in str form else return None |
| deleteRecord | key | str/None | If given key is present then delete the record and return true else returns false |
| getAllRecords | - | dict | Returns all the records in form of dictionary, with key(str) and assosiated value as json object |
| keyExists | key | boolean | Returns True if the given key is found in datastore else returns False |

