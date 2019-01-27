import json


class Serializable:
    def as_json(self):
        return json.dumps(dir(self))


class Roommate(Serializable):
    def __init__(self, name):
        self.name = name
        self.purchases = []
        self.balance = 0
        self.cleared_index = 0

    def add_item(self, item):
        self.purchases.append(item)
        self.accumulate()
        return self.balance

    @property
    def cleared_purchases(self):
        return self.purchases[: self.cleared_index]

    @property
    def uncleared_purchases(self):
        return self.purchases[self.cleared_index :]

    def accumulate(self):
        self.balance = sum(purchase.amount for purchase in self.purchases[self.cleared_index :])
        return self.balance

    def set_to_zero(self):
        self.balance = 0
        self.cleared_index = len(self.purchases)
        print(self.purchases)

    def get_owing(self, average):
        owe = average - self.balance
        if average - self.balance < 0:
            print(f"Everyone owes {self.name} ${abs(owe)}")

        else:
            print(f"{self.name} owes everyone ${owe}")
        return owe

    def pretty_owing(self, average):
        owe = self.get_owing(average)
        pretty_owe = f"${abs(owe):0.02f}"
        if owe <= 0:
            return f"The house hold owes {self.name} {pretty_owe}."
        else:
            return f"{self.name} owes the house hold {pretty_owe}."


class House(Serializable):
    def __init__(self, name):
        self.unit = name
        self.members = []

    def add_member(self, item):
        self.members.append(item)

    def get_total_amount(self):
        return sum(member.accumulate() for member in self.members)

    def get_average(self):
        return self.get_total_amount() / len(self.members)

    def get_owed(self, name):
        my_balance = next(m for m in self.members if m.name == name).balance
        others = [m for m in self.members if m.name != name]

        return {other.name: f"${(my_balance - other.balance) / len(self.members):0.02f}" for other in others}


class Purchase(Serializable):
    def __init__(self, name, amount):
        self.item = name
        self.amount = amount

    @property
    def pretty_amount(self):
        return f"${self.amount:0.2f}"
