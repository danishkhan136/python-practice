class Employee:
    a =1
    @classmethod
    def show(self):
        print(f"the vlaue of a class is : {self.a}")


e=Employee()
e.a =45 

e.show()