# Q10: Create three Hospital patient objects.
class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

patients = [Hospital("Asha", 20, "Fever", "Dr. Raj"), Hospital("Ravi", 30, "Cold", "Dr. Sam"), Hospital("Mina", 25, "Cough", "Dr. Lee")]
for patient in patients:
    print(patient.patient_name, patient.age, patient.disease, patient.doctor_name)
