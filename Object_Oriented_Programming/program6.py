# 6. Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint

class Train:

    def __init__(slf, train_no):
        slf.train_no = train_no

    def book(slf, source, destination):
        print(f"Ticket is booked in Train no : {slf.train_no} from {source} to {destination}")

    def getstatus(slf):
        print(f"Train no: {slf.train_no} is running on time")

    def getfare(slf, source, destination):
        print(f"Ticket fare in train no: {slf.train_no} from {source} to {destination} is {randint(222, 5555)}")
        

t = Train(1239)
t.book("Nagpur", "Bengraluru")
t.getstatus()
t.getfare("Nagpur", "Bengraluru")