import queue

patient_queue = queue.Queue()

def register_patient():
    name = input("Enter patient's name: ")
    patient_queue.put(name)
    print("Patient registered.")

def remove_patient():
    if not patient_queue.empty():
        patient = patient_queue.get()
        print(f"{patient} has met the doctor. Patient removed.")
    else:
        print("No patients in the queue.")

def display_patient_queue():
    if not patient_queue.empty():
        print("Current Patient Queue:")
        for patient in list(patient_queue.queue):
            print(patient)
    else:
        print("Patient queue is empty.")

while True:
    print("\nMenu:")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        register_patient()
    elif choice == '2':
        remove_patient()
    elif choice == '3':
        display_patient_queue()
    elif choice == '4':
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
