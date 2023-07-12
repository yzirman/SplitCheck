class Menu(object):
    def __init__(self):
        self.foods = []

    def addFood(self, food):
        self.foods.append(food)

    def __repr__(self) -> str:
        return f"foods={self.foods}"