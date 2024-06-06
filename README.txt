Zarys projektu:

Chcemy, żeby to było automatyczne narzędzie, gdzie użytkownik podaje nazwę instytucji a dostaje wykres prognozy na rok.
Chcemy, żeby to był jakiś model, dlatego ARIMA może być dobrym docelowym modelem.

I. Pobieranie danych z alphavantage:
	- DONE: użytkonik podaje nazwę instytucji, której akcje chce przewidywać
	- TODO (przydałoby się): wyświetlamy wyniki wyszukiwań i pytamy, którą chce wybrać (Ticker Search z alphavantage)
II. Przetwarzanie pobranych danych: 
	- DONE: uzupełnianie i przygotowanie danych - dane są w dobrej postaci ogółem
	- TODO: wydzielenie zbioru testowego (ostatni rok), zbioru walidacyjnego (1-2 lata temu), treningowego (5 ostatnich lat bez ostatnich 2 lat)
III. Uczenie modeli:
	- DONE: prosty model w postaci średniej z ostatniego okresu (np. roku, 2 lat, itp)
	- TODO: zrobienie ARIMA z odpowidnimi parametrami:
		- wstępne wybranie rozsądnych parametrów: p (lag order), d (difference order), q (moving average order)
IV. Wybieranie najlepszego modelu:
	- TODO: policzyć MSE, RMSE dla kilku rozsądnych modeli (prosta średnia, ARIMA z różnymi parametrami) i wybranie najlepszego z nich na podstawie zbioru walidacyjnego
	- TODO: podanie jak dobrze poszło naszemu modelowi na postawie zbioru testowego
V. Wykorzystanie modelu:
	- TODO: nauczenie najlepszego modelu z całych dostępnych danych
	- TODO: wygenerowanie predykcji
VI. Ogarnięcie kodu:
	- TODO: dodanie komentarzy
	- TODO: podzielenie kodu na moduły?
VII. Przygotowanie dokumentacji:
	- TODO: opisanie co robi kod
	- TODO: opisanie wyników dla jakiegoś przykładu 

LINKI:
1) Żródło danych: https://www.alphavantage.co/documentation/
2) Podstawy uczenia maszynowego: https://www.kaggle.com/learn/intro-to-machine-learning
3) Inspiracja: https://neptune.ai/blog/predicting-stock-prices-using-machine-learning
4) ARIMA model: https://www.investopedia.com/terms/a/autoregressive-integrated-moving-average-arima.asp#:~:text=An%20autoregressive%20integrated%20moving%20average%2C%20or%20ARIMA%2C%20is,it%20predicts%20future%20values%20based%20on%20past%20values
