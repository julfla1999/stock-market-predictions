import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import csv

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# YOU CAN ONLY USE API 25 TIMES PER DAY PER EACH KEY
# YOU CAN GET NEW KEY FOR NEW EMAIL ADDRESS
key1 = "5YSSPE77ILAF43HB"
ticker = 'tsco'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=' + ticker + '&datatype=csv&apikey=' + key1
r = requests.get(url)

my_list = []

with requests.Session() as s:
    download = s.get(url)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

df = pd.DataFrame(my_list[1:],columns=my_list[0])

df.to_csv(ticker + '.csv', encoding='utf-8', index=False)
#df.set_index("timestamp")
print(df)

