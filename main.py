from Functions import Patients_functions as pf
from Functions import Visits_functions as vf
import json
from Functions.Patients_functions import generate_patient_id
from Functions import File_handling as fh

patients ="D:\courses\AMIT_AI\Assignments\Assignment\patients_data.json"
with open(patients, 'r') as f:
    patients = json.load(f)

while True :
    print("\nHospital Management System")
    print("1. Add New Patient")
    print("2. Show All Patients")
    print("3. View Patient Details")
    print("4. Update Patient Information")
    print("5. Delete Patient Record")
    print("6. Add Visit for Patient")
    print("7. View Patient Visits")
    print("8. View patient billing information")
    print("9. View Apointments")
    print("10. Save & Exit")
    
    choice = input("Enter your choice (1-10): ")    

    if choice == '1':
        pf.new_patient(patients)
    elif choice == '2':     
        pf.show_all_patients(patients)
    elif choice == '3':
        pf.show_patient_info(patients)
    elif choice == '4':
        pf.update_patient_info(patients)
    elif choice == '5':
        pf.delete_patient(patients)
    elif choice == '6':
        vf.add_visit(patients)
    elif choice == '7':
        vf.view_patient_visits(patients)
    elif choice == '8':
        vf.view_patient_billing_info(patients)
    elif choice == '9':
        vf.view_appointments(patients)
    elif choice == '10':
        fh.save_patients_to_file(patients)
        print("Data saved. Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

