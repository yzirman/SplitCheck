class Food(object):

    def __init__(self, id, name, price) -> None:
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"id={self.id}, name={self.name}, price={self.price}"