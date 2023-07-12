class Restaurant(object):
    def __init__(self, id, menu, tables) -> None:
        self.id = id
        self.menu = menu
        self.tables = tables

    def getTables(self):
        return self.tables

    def __repr__(self) -> str:
        return f"id={self.id}, \n\tmenu={self.menu} \n\ttables={self.tables}"