
import datetime, requests
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from exchangeratesapi import Api

def get_yearly_rates(amount, currency, converted_currency, amount_of_date):
    #set start params
    today_date = datetime.datetime.now()

    date_1year = (today_date - datetime.timedelta(days=1*amount_of_date))
    date_1year=date_1year.date()
    print(date_1year)
    # requests
    access_key = "02d6cfa7ddcb34bef662e95b78f08a3f"
    url = f'https://api.exchangerate.host/timeseries'
    payload = {"base": currency, "amount": amount, "start_date": date_1year.date(), "end_date": today_date.date(),  "access_key": access_key}
    response = requests.get(url, params=payload)

    data = response.json()
    print(data)
    # create dict to store data
    currency_history = {}
    rate_history_array = []

    for item in data["rates"]:
        current_date = item
        currency_rate = data["rates"][item][converted_currency]
        currency_history[current_date] = [currency_rate]
        rate_history_array.append(currency_rate)

    # clean data
    pd_data = pd.DataFrame(currency_history).transpose()
    pd_data.columns = ['Rate']
    pd.set_option('display.max_rows', None)
    print(pd_data)


    plt.plot(rate_history_array)
    plt.ylabel(f'{amount} {currency} to {converted_currency}')
    plt.xlabel('Days')
    plt.title(f'Current rate for {amount} {currency} to {converted_currency} is {rate_history_array[-1]}')
    plt.show()

get_yearly_rates(1, 'EUR', 'GBP', 90)

