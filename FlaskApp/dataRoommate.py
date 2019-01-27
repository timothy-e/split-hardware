class Roommate:

    def __init__(self, name):
        self.roommate = name
        self.purchases = []
        self.balance = 0

    def add_item(self, item):
        self.purchases.append(item)
        self.accumulate()
        return self.balance

    def accumulate(self):
        self.balance = 0
        for purchase in self.purchases:
            self.balance += purchase.amount
        return self.balance
    
    def set_to_zero(self):
        self.balance = 0
    
    def get_owing(self, average):
        owe = average - self.balance
        if average - self.balance < 0:
            print(f"Everyone owes {self.roommate} ${abs(owe)}")

        else:
            print(f"{self.roommate} owes everyone ${owe}")
        return owe

class House:

    def __init__(self, name):
        self.unit = name
        self.members = []

    def add_member(self, item):
        self.members.append(item)

    def get_total_amount(self):
        total = 0
        for member in self.members:
            total += member.accumulate()

        return total

    def get_average(self):
        return self.get_total_amount()/len(self.members)

class Purchase:

    def __init__(self, name, amount):
        self.item = name
        self.amount = amount

def main():
    bread = Purchase("Bread", 20)
    toiletPaper = Purchase("Toilet Paper", 50)
    rice = Purchase("Rice", 100)

    Evan = Roommate("Evan bot")
    Tristan = Roommate("Tristan bot")
    Tim = Roommate("Tim bot")
    Emmy = Roommate("Emmy bot")

    print("Each member's spending:")
    print(Evan.add_item(bread))
    print(Evan.add_item(toiletPaper))
    print(Tristan.add_item(rice))
    print(Emmy.add_item(toiletPaper))
    print(Tim.add_item(bread))

    home = House("R204")
    home.add_member(Evan)
    home.add_member(Tim)
    home.add_member(Tristan)
    home.add_member(Emmy)

    total = 0
    for members in home.members:
        total += members.accumulate()
    print(home.get_average())

    get_owing("Evan", Evan.balance, home.get_average())
    get_owing("Emmy", Emmy.balance, home.get_average())
    get_owing("Tim", Tim.balance, home.get_average())
    get_owing("Tristan", Tristan.balance, home.get_average())

if __name__ == "__main__":
    main()
