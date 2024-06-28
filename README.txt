Zarys projektu:

Jest to automatyczne narzędzie, gdzie użytkownik podaje nazwę instytucji a dostaje wykres prognozy na 14 dni.
Głównym modelem prognozowania jest ARIMA.

Działanie programu:
1) pytamy użytkownika o podanie nazwy firmy, której akcje chce przewidywać (funkcja ask_for_ticker)
2) pobieramy z alphavantage sugestie co do tego, co to za firma i wyświetlamy je użytkownikowi (dalej ask_for_ticker)
3) użytkownik podaje którą pozycję z listy wybiera (dalej ask ask_for_ticker)
4) pobieramy dane z alphavantage tejże firmy (funkcja download_data)
5) uczymy 3 modele na danych z ostatnich 300 dni, ale poza najnowszymi 14 dniami (funkcja make_model_predictions z argumentem train) i robimy prognozę na te 14 dni
6) sprawdzamy jak te modele poradziły sobie z prognozą na ostatnie 14 dni, porównując ich przewidywania z rzeczywistymi wartościami (funkcja save_prediction_summary)
7) uczymy 3 modele na danych z ostatnich 300 dni (funkcja make_model_predictions z argumentem data['close']) i robimy prognozę na przyszłe 14 dni 
8) zapisujemy i wyświetlamy wyniki modeli (funkcja save forecast)
9) rysujemy i zapisujemy dwa wykresy (funkcja make_plot), pierwszy przedstawia przewidywania na ostatnie 14 dni, a drugi na przyszłe 14 dni

Pliki wynikowe programu:
- lista sugestii alphavantage (search_list.csv)
- dane pobrane z alphavantage ('ticker firmy'.csv)
- RMSE i MAPE przewidywań 3 modeli dla ostatnich 14 dni (prediction_summary.csv) 
- prognoza 3 modeli dla przyszłych 14 dni (forecast.csv)
- wykresy przewidywań ostatnich i przyszłych 14 dni (prediction_forecast_plot.png)

Używane modele:
1) model krótkoterminowego trendu:
	- liczymy średnią zwrotów z ostatnich 20 dni (zwrot[dziś] = wartość[dziś]/wartość[wczoraj] - 1)
	- zakładamy, że kurs będzie rósł codziennie o średni zwrot, czyli prognoza[jutro] = wartość[dziś] * (1 + średni_zwrot); prognoza[t + n] = wartość[t] * (1 + średni_zwrot) ^ n
2) model długoterminowego trendu:
	- liczymy średnią zwrotów z ostatnich 100 dni
	- zakładamy, że kurs będzie rósł codziennie o średni zwrot
3) model ARIMA (Autoregressive Integrated Moving Average):
	- zaawansowany model do prognozowania szeregów czasowych
	- AR odnosi się do tego od jak wielu poprzednich wartość zależy wartość aktualna (przyjmujemy w modelu 2)
	- I odnosi się do tego, że zamiast bezpośrednio prognozować wartość, prognozujemy różnice wartości, stopień odnosi się do tego jak odległych wartości różnicę rozważamy (przyjmujemy 1)
	- MA odnosi się do tego, jak bardzo losowość aktualnej wartości zależy od losowości wartości poprzednich (przyjmujemy w modelu 1, czyli że aktualna losowość zależy tylko od poprzedniej)

LINKI:
1) Żródło danych: https://www.alphavantage.co/documentation/
2) Podstawy uczenia maszynowego: https://www.kaggle.com/learn/intro-to-machine-learning
3) Inspiracja: https://neptune.ai/blog/predicting-stock-prices-using-machine-learning
4) ARIMA model: https://www.investopedia.com/terms/a/autoregressive-integrated-moving-average-arima.asp
5) dokumentacja bibliotek pandas, numpy, matplotlib, statsmodels