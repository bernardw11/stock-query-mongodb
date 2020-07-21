import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://student:PqyqrY2aEC22B5SB@cluster0-ya1yr.mongodb.net/stock-prices?retryWrites=true")
db = client['stock-prices'] #Make sure to replace this with the name of the database ('stock-prices')!
collection = db.prices

# write your queries here
stocks = list(collection.find({}))
print(stocks)

# 1. List all entries in the prices collection in the stock-prices database.
for stock in stocks:
    print(stock['price'])

# 2. List all historical Microsoft stock prices
microsoft_stocks = list(collection.find({'symbol': 'MSFT'}))
for stock in microsoft_stocks:
    print(stock['price'])

# 3. List all historical stock prices from 2004

year_stocks = list(collection.find({'year': 2004}))
for stock in year_stocks:
    print(stock["price"])

# 4. List all historical stock prices from September
print("4")
sep_stocks = list(collection.find({'month': 'Sep'}))
for stock in sep_stocks:
    print(stock["price"])
# 5. List all historical stock prices from September 2004
print("5")
sep2004_stocks = collection.find({'month': 'Sep', 'year': 2004})
for stock in sep2004_stocks:
    print(stock["price"])
# 6. List all historical stock prices in order from lowest value to highest value
print("6")
for stock in collection.find().sort('price',1):
    print(stock['price'])
# 7. List all historical stock prices in order from highest value to lowest value
print("7")
for stock in collection.find().sort('price',-1):
    print(stock['price'])
# 8. List the first 5 historical stocks in the database.
print("8")
for stock in collection.find().limit(5):
    print(stock)

# 9. Find an historical stock that was valued at $100.52.
print("9")
for stock in collection.find({'price': 100.52}):
    print(stock)
# 10. How many entries are there in the database for Apple stock prices?
print("10")
print(collection.find({"symbol":"AAPL"}).count())

# 11. List the first 10 Apple entries in the database.
print("11")
for stock in collection.find({'symbol': 'AAPL'}).limit(10):
    print(stock)
# 12. List the January IBM stock prices from lowest to highest.
print("12")
for stock in collection.find({'symbol': 'IBM', 'month': 'Jan'}).sort('price',1):
    print(stock['price'])
# 13. List all historical stock prices over $200.00
print("13")
for stock in collection.find({'price': {'$gt': 200}}):
    print(stock['price'])
# 14. List all historical stock prices less than $10.00.
print("14")
for stock in collection.find({'price': {'$lt': 10}}):
    print(stock['price'])
# 15. What company's (or companies') stock was valued at $9.78 in October, 2000? Return only the name of the company.
print("15")
for stock in collection.find({'price': 9.78, 'month': 'Oct', 'year': 2000}):
    print(stock['symbol'])
# 16. What was the price of Amazon's Stock in August, 2006? Return only the price.
print("16")
for stock in collection.find({'symbol': 'AMZN', 'month': 'Aug', 'year': 2006}):
    print(stock['price'])
# 17. What was the highest historical price of Microsoft's stock? Return only the price.
print("17")
for stock in collection.find({'symbol': 'MSFT'}).sort('price',-1).limit(1):
    print(stock['price'])
# 18. For how many months (in the historical database) has Apple's stock price been greater than $100.00? Return only the number of months.
print("18")
print(collection.find({'symbol': 'AAPL', 'price': {'$gt': 100}}).count())