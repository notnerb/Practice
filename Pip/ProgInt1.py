from random import randint


class TradingDay:
    def __init__(self, day, price):
        self.day = day
        self.price = price
    def show(self):
        print( "%i - %i" % (self.day, self.price))
def TradingAlgo(list = []):
    m = 9999999999;
    maxProfit = 0;
    for day in list:
        if day.price < m:
            m = day.price
        maxProfit = day.price - m
    print(maxProfit)

#lookup list comprehension.
print("hip hop")
days = []
for i in range(0,10):
    days.append( TradingDay(i, randint(1, 80)))
for day in days:
    day.show()
TradingAlgo(days)
