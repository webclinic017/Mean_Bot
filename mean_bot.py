# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:25:48 2021

@author: angel
"""

from market import market
import tools
import keys

exchange = market(keys.TRADE_KEYS)
exchange.set_currency("ETH")
amount = 1440

logger = tools.Logger()
prices = tools.Price_List()
accuracy = tools.Accuracy_Traker()
balance = tools.Balance_Traker()
timer = tools.Timer()

def log_balance():
    logger.log("Balance: [{}]".format(balance.get_log()))

def log_prices():
    logger.log("Price: [{}]".format(prices.get_log()))
    
def log_accuracy():
    logger.log("Accuracy: [{}]".format(accuracy.get_log(prices.size())))
    
def log_profits():
    logger.log("Profits: [${}]".format(balance.get_profit()))
    
def log_all():
    log_balance()
    log_prices()
    log_accuracy()
    log_profits()

def capture_price():
    try:
        prices.add(exchange.get_token_price())
        accuracy.add(amount)
    except:
        prices.add_mean()
        accuracy.remove()
        logger.log("Error: Unable to capture price. [{} / {}] [{}%]completed.".format(prices.size(), amount, round((prices.size() / amount) * 100 ,2))) 
        log_accuracy()
    prices.update(amount) # Updates list if it exceeds amount
         
def update_balance():
    if (prices.size() == amount):
        try:
            arr = [exchange.get_balance_usd(), exchange.get_balance_token() * prices.current()]
            balance.update(arr)
        except:
            logger.log("Error: [Unable to update balance.]")
            log_balance()

def buy():
    if(prices.is_low() and balance.more_usd()):
        try:
            logger.log("Buy: [{}]".format(exchange.buy_all()["id"]))
            log_prices()
            update_balance()
            log_profits()
        except:
            logger.log("Error: [Unable to buy.]")
        log_balance()

def sell():
    if(prices.is_top() and balance.more_token() and balance.is_best()):
        try:
            logger.log("Sell: [{}]".format(exchange.sell_all()["id"]))
            log_prices()
            update_balance()
            log_profits()
        except:
            logger.log("Error: [Unable to sell.]")
        log_balance()
        
def trade():
    update_balance()
    if(prices.size() == amount and accuracy.is_valid(prices.size())):
        buy()
        sell()
               
def run():
    days = int(input("How many days to run?: "))
    logger.log("Running mean_bot.py".format(days))
    logger.log("Capturing [{}] data points.".format(amount))
    for x in range(days):
        logger.log("[{} / {}] Days ================================================".format(x + 1, days))
        for y in range(amount):
            timer.start()
            capture_price()
            trade()
            timer.sleep(60)
    log_all()
        
run()   
    
