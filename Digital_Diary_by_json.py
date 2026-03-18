# inporting JSON
import json
# importing OS
import os


# Creating a class i.e. blue for every object.
class ContactBook:
    # Initial method
    def __init__(self, name):
        self.name = name 
        self.file = f"{name}_contacts.json"

        # Check that is the file in the folder or not?
        if os.path.exists(self.file):
            with open (self.file, "r") as file:
                self.info = json.load(file)
                print(self.info)
        else:
            with open (self.file, "w") as file:
                json.dump({},file)

    # Function used to add new data in the file
    def add(self, user_input_name, user_input_no):
        self.user_input_name = user_input_name
        self.user_input_no = user_input_no
        
        with open(self.file, "r")as file:
            self.data =json.load(file)

        self.data[user_input_name] = user_input_no
        
        with open (self.file , "w") as file:
            json.dump(self.data, file, indent = 4)
            print("Data entry successful!")

    # Help in searching of contacts
    def search(self,target):
        
        with open(self.file, "+r") as f1:
            data = json.load(f1)
            if target in data:
                return (data[target])
                 
            else:
                return "Contact not found!"
                




