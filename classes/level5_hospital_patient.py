# Q10: Display hospital patient information.
class HospitalPatient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def display(self):
        print(self.name, self.age, self.disease)

HospitalPatient("Mina", 25, "Fever").display()
