class People:

    nationality = "CN"

    def __init__(self, name, age, sex):
        self.name = name 
        self.age = age
        self.sex = sex
        

p = People("Mjj", 22, "M")
p2 = People("Yilin", 22, "M")

print(p.nationality)

p.nationality = "USA"
print(p.nationality)

/*
CN
USA
*/
