class Roommate(object):

    def __init__(self, name):
        self.roommate = name
        self.purchase = []
        self.balance = 0

    def addItem(self, item):
        self.purchase.append(item)
        self.accumulate()
        return self.balance

    def accumulate(self):
        self.balance = 0
        for count in range(len(self.purchase)):
            self.balance += self.purchase[count].amount
        return self.balance

class House(Roommate):

    def __init__(self, name):
        self.unit = name
        self.members = []

    def addMember(self, item):
        self.members.append(item)

    def getTotalAmount(self):
        total = 0
        for count in range(len(self.members)):
            total += self.members[count].accumulate()
        return total

    def getAverage(self):
        return self.getTotalAmount()/len(self.members)

class Purchase(object):

    def __init__(self, name, amount):
        self.item = name
        self.amount = amount

def getOwing(name, balance, average):
    owe = average - balance
    if average - balance < 0:
        print(f"Everyone owes {name} ${abs(owe)}")
    else:
        print(f"{name} owes everyone ${owe}")

def main():
    bread = Purchase("Bread", 20)
    toiletPaper = Purchase("Toilet Paper", 50)
    rice = Purchase("Rice", 100)

    Evan = Roommate("Evan bot")
    Tristan = Roommate("Tristan bot")
    Tim = Roommate("Tim bot")
    Emmy = Roommate("Emmy bot")

    print("Each member's spending:")
    print(Evan.addItem(bread))
    print(Evan.addItem(toiletPaper))
    print(Tristan.addItem(rice))
    print(Emmy.addItem(toiletPaper))
    print(Tim.addItem(bread))

    home = House("R204")
    home.addMember(Evan)
    home.addMember(Tim)
    home.addMember(Tristan)
    home.addMember(Emmy)

    total = 0
    for count in range(len(home.members)):
        total += home.members[count].accumulate()
    print(home.getAverage())

    getOwing("Evan", Evan.balance, home.getAverage())
    getOwing("Emmy", Emmy.balance, home.getAverage())
    getOwing("Tim", Tim.balance, home.getAverage())
    getOwing("Tristan", Tristan.balance, home.getAverage())

main()
