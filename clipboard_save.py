"""
Saves clipboard items to a json file. You can also load an item to the clipboard
by using its associated key, as well as list all of the items you have saved


"""

from fileinput import close
import clipboard
import sys
import json
from os.path import exists

DATA_FILE = "clipboard_data.json"  #Global variable for the name of the json file


#Function to save an entry into the created json file
def save_data(filepath, data):
    data_file = open(filepath, "w")
    json.dump(data, data_file)
    data_file.close()
   
#Function to load the json file as a python dictionary
def load_data(filepath):
    if exists(DATA_FILE) == False: #Returns empty dictionary if save_data function hasn't been ran
        return {}

    data_file = open(filepath, "r")
    data = json.load(data_file)
    data_file.close()
    return data


if len(sys.argv) == 2:  #Makes sure the only args given are the file and a command
    command = sys.argv[1]       
    data = load_data(DATA_FILE) 

    #If statements for each valid command
    if command == "save":
        key = input("Enter a key to associate with this entry: ")
        data[key] = clipboard.paste() #Adds the inputed key and current clipboard item to the dictionary
        save_data(DATA_FILE, data) 
    
    if command == "load":
        key = input("Enter key associated with desired entry: ")
        if key in data:
            clipboard.copy(data[key]) #Adds data associated with key to the clipboard
            print("Data copied")
        else:
            print("Data not found")

    elif command == "list":
        print(data)


