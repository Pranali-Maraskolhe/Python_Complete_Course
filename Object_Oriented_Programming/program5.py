# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

from random import randint

class Train:

    def __init__(self, train_no):
        self.train_no = train_no

    def book(self, source, destination):
        print(f"Ticket is booked in Train no : {self.train_no} from {source} to {destination}")

    def getstatus(self):
        print(f"Train no: {self.train_no} is running on time")

    def getfare(self, source, destination):
        print(f"Ticket fare in train no: {self.train_no} from {source} to {destination} is {randint(222, 5555)}")
        

t = Train(1239)
t.book("Nagpur", "Bengraluru")
t.getstatus()
t.getfare("Nagpur", "Bengraluru")