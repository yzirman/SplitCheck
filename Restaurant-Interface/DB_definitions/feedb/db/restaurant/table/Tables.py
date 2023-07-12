class Tables(object):

    def __init__(self) -> None:
        self.tables = []

    def addTable(self, table):
        self.tables.append(table)

    def __repr__(self) -> str:
        return f"tables={self.tables}"