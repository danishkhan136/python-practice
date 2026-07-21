from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"The Ticket is booked in Train no : {self.trainNo} from {fro} to {to} .")

    def setStatus(self):
        print(f"Train no : {self.trainNo} is running on time .")

    def getFare(self,fro,to):
        print(f"Ticket fare in Train No : {self.trainNo} from {fro} to {to} is {randint(2222,9999)}");

t = Train("25B97N")
t.book("hyderabad","karachi")
t.setStatus()
t.getFare("hyderabad","karachi")

t = Train("97N25B")
t.book("karachi","hyderabad")
t.setStatus()
t.getFare("karachi","hyderabad")