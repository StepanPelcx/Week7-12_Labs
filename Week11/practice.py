class Student:
    def __init__(self, name, MISIS, mark):
        self.name = name
        self.MISIS = MISIS
        self.mark = mark


    def result(self):
        if self.mark > 40:
            return "pass"
        return "fail"
    

    def __str__(self):
        return f"{self.name}, {self.MISIS}, {self.mark}"


class PG(Student):
    def __init__(self, name, MISIS, mark, diploma):
        super().__init__(name, MISIS, mark)
        self.__id = id
        self.diploma = diploma
    
    def get_diploma(self):
        return f"{self.diploma}"


std1 = PG("Anna", "M01042893", 89, "diploma")
std2 = Student("Nick", "M0104213", 76)

#print(std1)
#print(std1.result())
#print(std1.get_diploma())
#print(std2.MISIS)






class Animal:    
    def __init__(self, name, age, address):        
        self.__name = name        
        self.__age = age
        self.address = address

    def get_name(self):        
        return self.__name   
    
    def get_age(self):        
        return self.__age    
    
    def __str__(self):        
        return f'the Animal name is: {self.__name} and he is: {self.__age} years old\n{self.address}'
    

class Dog(Animal):
    def __init__(self, name, age, breed, address):            
        super().__init__(name, age, breed, address)
        self.__id = id
        

class Cat(Animal):  
    def __init__(self, name, age, address, id):          
        super().__init__(name, age, address)  
        self.__id = id   

    def hunts(self):        
        return f' it is: {True} cuts are hunting '    
    
    def __str__(self):        
        return super().__str__() + self.hunts()
    
class Address:    
    def __init__(self, number, street, postcode, country):        
        self.number = number        
        self.street = street        
        self.postcode = postcode        
        self.country = country    
    def __str__(self):        
        return f'The address is:\n{self.number} {self.street} \n{self.postcode} \n{self.country}'



def main():       
    bark = Dog('Bark', 4, 'Hasky')    
    piko = Cat('Piko', 2, 'Ragdool')    
    vuk = Dog('Vuk', 5, Address(1, 'Station Road', 'ES4', 'UK'))    
    princess = Dog('Princess', 2, Address(2, 'Hendon Lane', 'N4', 'UK'))    
    poko = Cat('Poko',1, Address(1, 'Dog lane', 'NW1', 'UK'))

    dogs_list = [vuk, princess, bark]    
    cats_list = [piko, poko]    
    animals  = dogs_list +cats_list    
    
    for i in animals:        
        if isinstance(i, Cat):            
            print(i)       
            print('----------------------')      


if __name__=='__main__':    
    main()

 

