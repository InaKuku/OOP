# 2 Lab
# Classes and Objects

# Create a class called PizzaDelivery. Upon initialization it should receive name(string), price(float) and ingredients (dict). The class should also have an instance attribute ordered set to False by default. You should also create 3 instance methods:
# ⦁	add_extra(ingredient: str, quantity: int, price_per_ingredient: float):
# ⦁	if we already have this ingredient in our pizza, increase the ingredient quantity with the given one and update the pizza price by adding the ingredient price for the given quantity
# ⦁	if we do not have this ingredient in our pizza, we should add it and update the pizza price
#
# ⦁	remove_ingredient(ingredient: str, quantity: int, price_per_ingredient: float):
# ⦁	if we do not have this ingredient in our pizza, we should return the following message "Wrong ingredient selected! We do not use {ingredient} in {pizza_name}!"
# ⦁	if we have the ingredient, but we try to remove more than we have available, we should return the following message "Please check again the desired quantity of {ingredient}!"
# ⦁	otherwise remove the given quantity of the ingredient and update the pizza price by removing the ingredient price for the given quantity
#
# ⦁	make_order() - set the attribute ordered to True and return the following message "You've ordered pizza {pizza_name} prepared with {ingredient: quantity (separated with ", ")} and the price will be {price}lv.". Have in mind that once the pizza is ordered, no further changes are allowed. We should return the following message if the customer tries to change it: "Pizza {name} already prepared, and we can't make any changes!"

class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if not self.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
                self.price += price_per_ingredient * quantity
            else:
                self.ingredients[ingredient] = quantity
                self.price += price_per_ingredient * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if not self.ordered:
            if not ingredient in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            else:
                if quantity > self.ingredients[ingredient]:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.ingredients[ingredient] -= quantity
                    self.price -= price_per_ingredient * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"


    def make_order(self):
        self.ordered = True
        result = ""
        result += f"You've ordered pizza {self.name} prepared with "
        for ingr, quant in self.ingredients.items():
            if not ingr == list(self.ingredients.keys())[-1]:
                result += f"{ingr}: {quant}, "
            else:
                result += f"{ingr}: {quant} "
        result += f"and the price will be {self.price}lv."
        return result


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))