from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, budget=salary_one + salary_two, members_count =2 + len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = self.members_count*[TV(), Fridge(), Laptop()]
        self.calculate_expenses(self.appliances, self.children)


# child = Child(20, 3, 4, 5)
# room1 = YoungCoupleWithChildren("FamName", 200, 200, child)
# print(room1.calculate_expenses())
