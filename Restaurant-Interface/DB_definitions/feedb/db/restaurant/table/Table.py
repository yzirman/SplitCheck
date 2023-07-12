class Table(object):
    def __init__(self, id) -> None:
        self.id = id
        self.orders = []

    def addToOrder(self, food):
        self.orders.append(food)

    def __repr__(self) -> str:
        return f"id={self.id}, orders={self.orders}"