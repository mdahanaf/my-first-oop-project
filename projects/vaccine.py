class Vaccine:
    def __init__(self, vacName, country, time):
        self.vacName = vacName
        self.country = country
        self.time = time

# ===============================================================

class Person:
    def __init__(self, name, age, ptype="General Citizen"):
        self.name = name
        self.age = age
        self.ptype = ptype

        # my variable
        self.first_dose = False
        self.second_dose = False
        self.which_vac = ""

    def pushVaccine(self, mem_addr, num_of_dose = "1st dose"):
        self.vac_class_addr = mem_addr


        if num_of_dose == "1st dose":
            # 1st dose
            if self.ptype == "Student" or self.age >= 25:
                self.first_dose = True
                self.which_vac = self.vac_class_addr.vacName
                print(f"1st dose done for {self.name}")
            else:
                print(f"Sorry {self.name}, Minimum age for taking vaccines is 25 years now.")
        else:
            # 2nd dose
            if num_of_dose == "2nd dose":
                if self.first_dose == True:
                    if self.vac_class_addr.vacName == self.which_vac:
                        self.second_dose = True
                        print(f"2nd dose done for {self.name}")
                    else:
                        print(f"Sorry {self.name}, you can't take 2 different vaccines.")
                    
                else:
                    print(f"{self.name}, please take 1st dose now.")


    def showDetail(self):
        print(f"Name: {self.name} Age: {self.age} Type: {self.ptype}\nVaccine Name: {self.vac_class_addr.vacName}")
        if self.first_dose == True:
            print("1st dose: Given")
        elif self.first_dose == False:
            print("1st dose: Not Given")
        
        if self.second_dose == True:
            print("2nd dose: Given")
        elif self.second_dose == False:
            print(f"2nd dose: Please come after {self.vac_class_addr.time} days")


# ================================================================


# write your code from here

astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("==============================")
p1.pushVaccine(astra)
print("==============================")
p1.showDetail()
print("==============================")
p1.pushVaccine(sin, "2nd dose")
print("==============================")
p1.pushVaccine(astra, "2nd dose")
print("==============================")
p1.showDetail()
print("==============================")
p2 = Person("Carol", 23, "Actor")
print("==============================")
p2.pushVaccine(sin)
print("==============================")
p3 = Person("David", 34)
print("==============================")
p3.pushVaccine(modr)
print("==============================")
p3.showDetail()
print("==============================")
p3.pushVaccine(modr, "2nd dose")