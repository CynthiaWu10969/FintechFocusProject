import requests

def shares_calculator(symbol, initial_balance, initial_day):
    result = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=' + symbol + '&apikey=6NRP03K3NSL2U5UK')
    dict = result.json()
    result_dict = dict["Weekly Adjusted Time Series"]
    initial_price = 0
    for key in result_dict.keys():
        if (initial_day == key):
            initial_price = float(result_dict[initial_day]["5. adjusted close"])
    print(result_dict)
    print (initial_balance)
    print(initial_price)
    shares_all = initial_balance // initial_price
    return shares_all
    
def balance_calculator(shares_all, shares, symbol, initial_balance, initial_day, sell_day):
    result = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=' + symbol + '&apikey=6NRP03K3NSL2U5UK')
    dict = result.json()
    result_dict = dict["Weekly Adjusted Time Series"]
    for key in result_dict.keys():
        if (initial_day == key):
            initial_price = float(result_dict[initial_day]["5. adjusted close"])
    if shares < shares_all:
        for key in result_dict.keys():
            if (sell_day == key):
                sell_price = float(result_dict[sell_day]["5. adjusted close"])
        profit = (sell_price - initial_price) * shares
        balance = initial_balance + profit
        return balance
    else:
        return "Please enter a valid shares"
        
        
# print(shares_calculator('AAPL', 2900, "1990"))
# print(balance_calculator(29, 25, 'AAPL', 2900, "1990", "2019"))

climate_products = [
    {'product': "Coral Reef Safe Sunscreen", 'price': 17, 'increaseindex': 6},
    {'product': "Metal Straws", 'price': 8, 'increaseindex': 3},
    {'product': "Recycled Pencils", 'price': 11, 'increaseindex': 4},
    {'product': "Reusable Water Bottles", 'price': 6, 'increaseindex': 2},
    {'product': "Tote Bag", 'price': 5, 'increaseindex ': 1}
    ]
    
def weathercalculator(balance, health_index, product1, product2):
    climate_products = [
    {'product': "coralreef", 'price': 17, 'increaseindex': 6},
    {'product': "metalstraws", 'price': 8, 'increaseindex': 3},
    {'product': "pencils", 'price': 11, 'increaseindex': 4},
    {'product': "bottles", 'price': 6, 'increaseindex': 2}, 
    {'product': "bag", 'price': 5, 'increaseindex': 1}
    ]
    for product in climate_products:
        if product1 == product['product']:
            balance = balance - product['price']
            health_index = health_index + product['increaseindex']
    for product in climate_products:    
        if product2 == product['product']:
            balance = balance - product['price']
            health_index = health_index + product['increaseindex']
    return ([balance, health_index])