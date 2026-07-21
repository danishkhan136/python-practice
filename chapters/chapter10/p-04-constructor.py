class Employee:

    language = "py"#class Attribute
    salary = 1600000

    def __init__(self): #dunder method
        print("I am creating")

    def getinfo(self):
        print(f"the language is {self.language}. the salar is salary is {self.salary}")

        
    @staticmethod
    def greet():
        print("hello world");

Danish = Employee()
Danish.language="javascript"#instance Attribute/object Attribute
print(Danish.salary,Danish.language);


#instance attribute have preference over class attribute

Danish.greet()
Danish.getinfo()
Employee.getinfo(Danish);