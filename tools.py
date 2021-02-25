# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 02:50:07 2021

@author: angel
"""

class Accuracy_Traker():
    
    def __init__(self):
        self.count = 0
        self.rate = .9
        
    def add(self, amount):
        if(self.count < amount):
            self.count += 1
        
    def remove(self):
        self.count -= 1
        
    def set_rate(self, rate):
        self.rate = rate
        
    def get_rate(self):
        return self.rate
            
    def accuracy(self, amount):
        if (amount > 0):
            return round(self.count / amount, 2)
        else:
            return 0
    
    def get_count(self):
        return self.count
    
    def is_valid(self, amount):
        return self.accuracy(amount) >= self.rate
    
    def get_log(self, amount):
        return "{} / {} | {} / {}".format(self.count, amount, self.accuracy(amount), self.rate)
        
class Price_List():
    import statistics
    
    def __init__(self):
        self.prices = []
    
    def size(self):
        return len(self.prices)
    
    def add(self, price):
        self.prices.append(round(price, 2))
        
    def add_mean(self):
        self.prices.append(self.get_mean())
    
    def update(self, amount):
        if(self.size() > amount):
            self.prices.pop(0)
            
    def current(self):
        return self.prices[-1]
    
    def get_mean(self):
        return round(self.statistics.mean(self.prices), 2)
    
    def get_low_mean(self):
        low = []
        for x in range(self.size()):
            if(self.prices[x] < self.get_mean()):
                low.append(self.prices[x])
        return round(self.statistics.mean(low), 2)
    
    def get_top_mean(self):
        top = []
        for x in range(self.size()):
            if(self.prices[x] > self.get_mean()):
                top.append(self.prices[x])
        return round(self.statistics.mean(top), 2)
    
    def is_low(self):
        return self.get_low_mean() > self.current()
    
    def is_top(self):
        return self.get_top_mean() < self.current()
    
    def get_log(self):
        return "M ${} | T ${} | L ${} | C ${}".format(self.get_mean(), self.get_top_mean(), self.get_low_mean(), self.current())
               
class Balance_Traker():
    
    def __init__(self):
        self.usd = 0
        self.token = 0
        self.current = 0
        self.best = 0
        self.start = 0
        
    def update(self, arr):
        self.set_usd(arr[0])
        self.set_token(arr[1])
        self.set_current()
        
    def set_usd(self, amount):
        self.usd = round(amount, 2)
    
    def set_token(self, amount):
        self.token = round(amount, 2)
        
    def set_current(self):
        self.current = round(self.token + self.usd, 2) 
        if(self.start == 0):
            self.start = self.current
        if(self.current > self.best):
            self.best = self.current
        
    def get_usd(self):
        return self.usd  
        
    def get_token(self):
        return self.token
    
    def get_current(self):
        return self.current
    
    def get_best(self):
        return self.best
    
    def get_start(self):
        return self.start
    
    def get_profit(self):
        return round((self.current - self.start), 2)
    
    def is_best(self):
        return self.best == self.current
    
    def more_usd(self):
        return self.usd > self.token
    
    def more_token(self):
        return self.usd < self.token
    
    def get_log(self):
        return "${} USD + ${} TKN = ${} CURRENT / ${} BEST / ${} START".format(self.usd, self.token, self.current, self.best, self.start)
            
class Logger():
    from datetime import datetime
    
    def get_time(self):
        return '{:%Y-%m-%d %H:%M:%S}'.format(self.datetime.now())
    
    def log(self, text):
        time = self.get_time()
        logtext = "[{}] {}\n".format(time, text)
        print(time, text)
        
        try:
            open("log.txt", "a").write(logtext)
        except:
            print(time, "Error: Unable to Log.")
         
class Timer():
    import time     
        
    def __init__(self):
        self.start_time = 0
        
    def get_current(self):
        return self.time.time()
        
    def start(self):
        self.start_time = self.get_current()
        
    def sleep(self, delay):
        delay = delay - (self.get_current() - self.start_time)
        self.start_time = 0
        if(delay >= 1):
            self.time.sleep(delay)
    
        
        
        
   








     