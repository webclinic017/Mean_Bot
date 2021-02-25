# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:39:57 2021

@author: angel
"""

class market:
    import cbpro
    
    def __init__(self, keys):
        self.api = self.cbpro.AuthenticatedClient(keys[0], keys[1], keys[2])
        
    def set_currency(self, token):
        self.token = token
        self.product_id = "{}-USD".format(token)
        
        accounts = self.api.get_accounts()
        search = [self.token, 'USD']
        
        for x in range(len(accounts)):
            if(accounts[x]['currency'] == search[1]):
                self.usd_id = accounts[x]['id']
            if(accounts[x]['currency'] == search[0]):
                self.token_id = accounts[x]['id']

    def get_balance_token(self):
        return float(self.api.get_account(self.token_id)['balance'])

    def get_balance_usd(self):
        return float(self.api.get_account(self.usd_id)['balance'])

    def get_token_price(self):
        return float(self.api.get_product_ticker(product_id=self.product_id)['price'])
    
    def get_cost(self, amount):
        return amount * .005
    
    def buy(self, money):
        return self.api.place_market_order(product_id=self.product_id, side='buy', funds=money)
        
    def sell(self, size):
        return self.api.place_market_order(product_id=self.product_id, side='sell', size=size)
    
    def sell_all(self):
        return self.sell(round(self.get_balance_token(), 8))
    
    def buy_all(self):
        return self.buy(int(self.get_balance_usd()))
    