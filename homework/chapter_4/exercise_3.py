# 3. Sales Performance Tracker: Create a class called SalesRep that stores a representative’s
# name and a list of their sales amounts.
# Include methods to add sales amounts, calculate average sales, and determine if they hit a
# target (parameter).
# # Sample data for creating SalesRep objects
# sales_data = {
# "Alice Johnson": [15000, 18000, 22000, 16000, 19000, 21000],
# "Bob Smith": [12000, 14000, 11000, 13000, 15000, 16000],
# "Carol Davis": [25000, 28000, 30000, 27000, 32000, 29000]
# }
from math import frexp
from typing import List

from numpy.ma.extras import average


class SalesRep:
    def __init__(self, name: str, sale_amounts: List[int]):
        self.name = name
        self.sale_amounts = sale_amounts

    def add(self, sale_amount: int):
        self.sale_amounts.append(sale_amount)

    def average(self):
        return sum(self.sale_amounts)/len(self.sale_amounts)

    def hit(self, target_sale_amount: int):
        return target_sale_amount > average(self)

sales_data = {
"Alice Johnson": [15000, 18000, 22000, 16000, 19000, 21000],
"Bob Smith": [12000, 14000, 11000, 13000, 15000, 16000],
"Carol Davis": [25000, 28000, 30000, 27000, 32000, 29000]
}

reps: List[SalesRep] = []
for name,sales in sales_data.items():
    reps.append(SalesRep(name, sales))

print([rep.average() for rep in reps])