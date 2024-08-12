print("This is a price to buy and sell the stock to make more profit")

days = 6
price_list = []

for i in range (days + 1):
    if i != 0:
        input_price = int(input("Enter the price for the day here: "))
        price_list.append(input_price)
print(price_list)

StockBuyDay = int(input("When did you buy the stock, enter the day: "))

for a in price_list:
    if a.max:
        sellday = a.max - StockBuyDay
print(f"This is the day you'll make max profit when you sell the stock at price"+ a.max +"and make profit of"+ sellday)

#getting an error need to re-verify 