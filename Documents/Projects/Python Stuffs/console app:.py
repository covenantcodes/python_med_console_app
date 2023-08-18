class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Physician:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

class Prescription:
    def __init__(self, patient_name, physician_name, medication):
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
