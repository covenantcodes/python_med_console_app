# Here is a python class named 'Patient':

class Patient:
    """
    This class represents a patient with a name and age.
    """

    def __init__(self, name, age):
        """
        Initializes a new instance of the Patient class with the given name and age.

        Args:
            name (str): The name of the patient.
            age (int): The age of the patient.
        """
        self.name = name
        self.age = age

# Here is a python class named 'Physician':

class Physician:
    """
    Represents a physician with a name and specialization.
    """

    def __init__(self, name, specialization):
        """
        Initializes a new instance of the Physician class with the given name and specialization.

        Args:
            name (str): The name of the physician.
            specialization (str): The specialization of the physician.
        """
        self.name = name
        self.specialization = specialization

    def add_physician(self):
        """
        Allows the user to input the name and specialization of a physician and adds it to a list of physicians.
        """
        # Code to add a physician to the list

    def print_physician_list(self):
        """
        Prints the list of physicians with their names and specializations.
        """
        # Code to print the list of physicians

    def print_prescription_list(self):
        """
        Prints the list of prescriptions with the patient name, physician name, and medication.
        """
        # Code to print the list of prescriptions
        self.name = name
        self.specialization = specialization

# Here is a python class named 'Prescription':

class Prescription:
    """
    Represents a prescription for a patient.

    Attributes:
        patient_name (str): The name of the patient for whom the prescription is written.
        physician_name (str): The name of the physician who prescribed the medication.
        medication (str): The name of the medication prescribed.
    """

    def __init__(self, patient_name, physician_name, medication):
        """
        Initializes a new Prescription object with the given patient name, physician name, and medication.

        Args:
            patient_name (str): The name of the patient.
            physician_name (str): The name of the physician.
            medication (str): The name of the medication.
        """
        self.patient_name = patient_name
        self.physician_name = physician_name
        self.medication = medication

patients = []
physicians = []
prescriptions = []

def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    patients.append(Patient(name, age))
    print("Patient added successfully!")

def add_physician():
    name = input("Enter physician name: ")
    specialization = input("Enter physician specialization: ")
    physicians.append(Physician(name, specialization))
    print("Physician added successfully!")

def add_prescription():
    patient_name = input("Enter patient name: ")
    physician_name = input("Enter physician name: ")
    medication = input("Enter medication: ")
    prescriptions.append(Prescription(patient_name, physician_name, medication))
    print("Prescription added successfully!")

def print_patient_list():
    print("Patient List:")
    for patient in patients:
        print(f"Name: {patient.name}, Age: {patient.age}")

def print_physician_list():
    print("Physician List:")
    for physician in physicians:
        print(f"Name: {physician.name}, Specialization: {physician.specialization}")

def print_prescription_list():
    print("Prescription List:")
    for prescription in prescriptions:
        print(f"Patient: {prescription.patient_name}, Physician: {prescription.physician_name}, Medication: {prescription.medication}")

def print_patient_names():
    print("Patient Names:")
    for patient in patients:
        print(patient.name)


def main():
    """
    The main function is the entry point of the program. It displays a menu of options to the user and performs different actions based on the user's choice.

    Options:
    1. Add new patient
    2. Add physician
    3. Add prescription
    4. Print patient list
    5. Print physician list
    6. Print prescription list
    7. Print patient names
    8. Exit

    The function continues to display the menu until the user chooses to exit the program.
    """

    while True:
        print("\nMenu:")
        print("1. Add new patient")
        print("2. Add physician")
        print("3. Add prescription")
        print("4. Print patient list")
        print("5. Print physician list")
        print("6. Print prescription list")
        print("7. Print patient names")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            add_physician()
        elif choice == '3':
            add_prescription()
        elif choice == '4':
            print_patient_list()
        elif choice == '5':
            print_physician_list()
        elif choice == '6':
            print_prescription_list()
        elif choice == '7':
            print_patient_names()
        elif choice == '8':
            print("We'll miss you, Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
