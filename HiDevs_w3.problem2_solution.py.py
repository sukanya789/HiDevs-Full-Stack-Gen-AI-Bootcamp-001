#!/usr/bin/env python
# coding: utf-8

# # Problem Statement 2: Compact Address Book Management

# In[1]:


import pickle

class AddressBook:
    def __init__(self):
        self.data = []
        self.file_name = "problem2_data_file.pickle"
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.data, file)

    def add_contact(self, fname, lname, street, city, state, country, mobile, email):
        for contact in self.data:
            if contact.get('email') == email or contact.get('mobile') == mobile:
                print("Duplicate email or phone number. Contact not added.")
                return

        new_contact = {
            'Fname': fname,
            'LName': lname,
            'StreetAddress': street,
            'City': city,
            'State': state,
            'Country': country,
            'Mobile': mobile,
            'email': email
        }
        self.data.append(new_contact)
        self.save_data()

    def find_occurrences(self, field, value):
        count = sum(1 for contact in self.data if contact.get(field) == value)
        return count

    def find_occurrences_all(self, fname=None, lname=None, street=None):
        counts = {}
        if fname:
            counts['Fname'] = self.find_occurrences('Fname', fname)
        if lname:
            counts['LName'] = self.find_occurrences('LName', lname)
        if street:
            counts['StreetAddress'] = self.find_occurrences('StreetAddress', street)
        return counts

    def run(self):
        while True:
            fname = input("Enter first name: ")
            if fname.lower() == "exit":
                break

            lname = input("Enter last name: ")
            street = input("Enter street address: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            country = input("Enter country: ")
            mobile = input("Enter mobile number: ")
            email = input("Enter email: ")

            self.add_contact(fname, lname, street, city, state, country, mobile, email)
            print("Contact added successfully!")

    def find_occurrences_menu(self):
        while True:
            print("1. Find number of occurrences of a Fname")
            print("2. Find number of occurrences of a Lname")
            print("3. Find number of occurrences of a street")
            print("4. Find occurrences of all fields")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                fname = input("Enter first name: ")
                print("Occurrences:", self.find_occurrences('Fname', fname))
            elif choice == "2":
                lname = input("Enter last name: ")
                print("Occurrences:", self.find_occurrences('LName', lname))
            elif choice == "3":
                street = input("Enter street address: ")
                print("Occurrences:", self.find_occurrences('StreetAddress', street))
            elif choice == "4":
                fname = input("Enter first name (optional): ")
                lname = input("Enter last name (optional): ")
                street = input("Enter street address (optional): ")
                occurrences = self.find_occurrences_all(fname, lname, street)
                for field, count in occurrences.items():
                    print(f"Occurrences of {field}: {count}")
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    address_book = AddressBook()
    address_book.run()
    address_book.find_occurrences_menu()


# In[ ]:




