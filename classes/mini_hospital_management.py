# Mini Project 6: Simple hospital management system.
class Patient:
    def __init__(self, name):
        self.name = name

class Doctor:
    def __init__(self, name):
        self.name = name

class Appointment:
    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor

appointment = Appointment(Patient("Asha"), Doctor("Dr. Raj"))
print(appointment.patient.name, appointment.doctor.name)
