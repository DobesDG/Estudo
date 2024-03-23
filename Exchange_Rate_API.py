import requests
import json

exchange_rate = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
exchange_rate = exchange_rate.json()

def dolar_rate():
    namecode = exchange_rate["USDBRL"]["code"]
    namecodein = exchange_rate["USDBRL"]["codein"]
    exchangename = namecode+"/"+namecodein
    exchange = exchange_rate["USDBRL"]["bid"]
    high = exchange_rate["USDBRL"]["high"]
    low = exchange_rate["USDBRL"]["low"]
    var_exchange = exchange_rate["USDBRL"]["varBid"]
    percentual_var = exchange_rate["USDBRL"]["pctChange"]
    print("-> Exchange Rate Info:" +
          "\n   Name: "+exchangename +
          "\n   Rate: "+ exchange +
          "\n   Hight: "+ high +
          "\n   Low: "+ low +
          "\n   Variation: "+ var_exchange +
          "\n   % Variation: "+percentual_var 
          )

def euro_rate():
    namecode = exchange_rate["EURBRL"]["code"]
    namecodein = exchange_rate["EURBRL"]["codein"]
    exchangename = namecode+"/"+namecodein
    exchange = exchange_rate["EURBRL"]["bid"]
    high = exchange_rate["EURBRL"]["high"]
    low = exchange_rate["EURBRL"]["low"]
    var_exchange = exchange_rate["EURBRL"]["varBid"]
    percentual_var = exchange_rate["EURBRL"]["pctChange"]
    print("-> Exchange Rate Info:" +
          "\n   Name: "+exchangename +
          "\n   Rate: "+ exchange +
          "\n   Hight: "+ high +
          "\n   Low: "+ low +
          "\n   Variation: "+ var_exchange +
          "\n   % Variation: "+percentual_var 
          )

def bitcoin_rate():
    namecode = exchange_rate["BTCBRL"]["code"]
    namecodein = exchange_rate["BTCBRL"]["codein"]
    exchangename = namecode+"/"+namecodein
    exchange = exchange_rate["BTCBRL"]["bid"]
    high = exchange_rate["BTCBRL"]["high"]
    low = exchange_rate["BTCBRL"]["low"]
    var_exchange = exchange_rate["BTCBRL"]["varBid"]
    percentual_var = exchange_rate["BTCBRL"]["pctChange"]
    print("-> Exchange Rate Info:" +
          "\n   Name: "+exchangename +
          "\n   Rate: "+ exchange +
          "\n   Hight: "+ high +
          "\n   Low: "+ low +
          "\n   Variation: "+ var_exchange +
          "\n   % Variation: "+percentual_var 
          )

dolar_rate()
euro_rate()
bitcoin_rate()