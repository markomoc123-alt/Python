"""A class that holds one transaction."""


class TransactionRecord:
    def __init__(self, fields):
        self.branch = fields[0]
        self.date = fields[1]
        self.tier = fields[2]
        self.items = int(fields[3])
        self.sales = float(fields[4])
        self.cost = float(fields[5])
        self.active = fields[6] == "YES"
        self.margin = 0.0
        self.tax = 0.0
