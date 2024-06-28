import pandas as pd
import requests
import csv

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# YOU CAN ONLY USE API 25 TIMES PER DAY PER EACH KEY
# YOU CAN GET NEW KEY FOR NEW EMAIL ADDRESS

def ask_for_ticker(key="5YSSPE77ILAF43HB"):
    keyword = input("Podaj nazwę firmy: ")

    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + keyword + '&datatype=csv&apikey=' + key

    my_list = []

    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

    df = pd.DataFrame(my_list[1:],columns=my_list[0])

    df.to_csv('search_list.csv', encoding='utf-8')
    print(df)

    index = input("Podaj numer pozycji szukanej firmy: ")

    return df['symbol'][int(index)]

def download_data(ticker, key="5YSSPE77ILAF43HB"):

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=' + ticker + '&datatype=csv&apikey=' + key

    my_list = []

    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

    df = pd.DataFrame(my_list[1:],columns=my_list[0])
    #stockprices = pd.read_csv("ibm.csv", index_col="timestamp")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.sort_values(by=['timestamp'], inplace=True)
    df.set_index('timestamp', inplace=True)
    df = df.apply(pd.to_numeric, errors='ignore')

    df.to_csv(ticker + '.csv', encoding='utf-8')
    
    return df

