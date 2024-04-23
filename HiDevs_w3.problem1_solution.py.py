#!/usr/bin/env python
# coding: utf-8

# # Problem Statement 1(A): Managing Personal Informatin with Python

# In[2]:


import pickle

class Person:
    def __init__(self, name, dob, is_secret = False):
        self.name = name
        self.dob = dob
        self.is_secret = is_secret
        
    def display_info(self):
        if self.is_secret:
            print("Secret")
        else:
            print(f"Name: {self.name}")
            print(f"Date of Birth: {self.dob}")
            
def load_data():
    try:
        with open("problrm1_data_file.pickle", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
            return []
        
def save_data(data):
    with open("problem1_data_file.pickle", "wb") as f:
        pickle.dump(data,f)
        
def main():
    people = load_data()
    
    while True:
        name = input("Enter person's name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
            
        found = False
        for person in people:
            if person.name.lower() == name.lower():
                person.display_info()
                found = True
                break
                
        if not found:
            secret = input(f"Person '{name}' not found. Mark as secret? (y/n): ")
            if secret.lower() == 'y':
                dob = input("Enter date of birth (YYYY-MM-DD): ")
                people.append(Person(name, dob, True))
                print(f"Person '{name}' marked as secret.")
            else:
                dob = input("Enter date of birth (YYYY-MM-DD): ")
                people.append(Person(name, dob))
                print(f"Person '{name}' added.")
                
        save_data(people)
        
if __name__ == "__main__":
    main()
            


# # Problem Statement 1(B): Managing Personal Information with Python

# In[3]:


import pickle
import os

class PersonalInfoManager:
    def __init__(self):
        self.file_name = "problem1_data_file.pickle"
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'rb') as file:
                    return pickle.load(file)
            except (EOFError, pickle.UnpicklingError):
                return {}
        else:
            return {}

    def save_data(self):
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.data, file)

    def add_person(self, name, dob):
        self.data[name] = dob
        self.save_data()

    def display_dob(self, name):
        dob = self.data.get(name)
        if dob:
            return dob
        else:
            return "Secret"

    def run(self):
        attempts = 0
        while attempts < 3:
            try:
                name = input("Enter name: ")
                if name.lower() == "exit":
                    break

                dob = input("Enter date of birth (YYYY-MM-DD): ")
                self.add_person(name, dob)

                print("Data added successfully!")

                choice = input("Do you want to display dob? (yes/no): ")
                if choice.lower() == "yes":
                    dob = self.display_dob(name)
                    print("Date of birth:", dob)
            except Exception as e:
                attempts += 1
                print("Error:", e)
        else:
            print("Maximum attempts reached. Exiting.")

if __name__ == "__main__":
    manager = PersonalInfoManager()
    manager.run()

