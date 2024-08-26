
Projekt Analizy Satysfakcji Pasażerów Linii Lotniczych

Przegląd Projektu

Celem tego projektu jest analiza oraz predykcja satysfakcji pasażerów linii lotniczych przy użyciu regresji logistycznej.
Projekt obejmuje przetwarzanie danych, trenowanie modelu, przeprowadzanie predykcji na nowych danych, integrację wyników z bazą danych MySQL, a także wizualizację i analizę wyników przy użyciu Tableau.
---------------------------------------------------------------------------------------------------------------------------------------

Struktura Projektu

Pliki Danych:

- airline_passenger_satisfaction.csv: Surowy zbiór danych zawierający różne cechy związane z satysfakcją pasażerów.

- flight_satisfaction_preprocessed.csv: Wstępnie przetworzone dane używane do trenowania i testowania modelu.

- data_to_module.csv: Nowe dane używane do przeprowadzania predykcji przy użyciu utworzonego modelu oraz do integracji z bazą danych MySQL.

- data_dictionary.csv: Plik ze słownikiem danych opisujący zmienne w zbiorze danych.

- raw_data_dictionary.txt oraz preprocessed_data_dictionary.txt: Słowniki danych dla surowych i przetworzonych danych.

Notebooki Jupyter:

- DATA_PREPROCESSING.ipynb: Notebook do czyszczenia danych, przetwarzania wstępnego oraz inżynierii cech.

- data_ML.ipynb: Notebook do trenowania modelu, ewaluacji oraz strojenia hiperparametrów przy użyciu regresji logistycznej.

- Integration_with_mysql.ipynb: Notebook pokazujący, jak zintegrować nowe dane (data_to_module.csv) oraz wyniki modelu z bazą danych MySQL.

Pliki PDF:

- DATA_PREPROCESSING.pdf, data_ML.pdf, Integration_with_mysql.pdf, FS_VISUALIZATION.pdf: Wersje PDF notebooków Jupyter i wizualizacji.

Moduły Pythona:

- satisfaction_module2.py: Własny moduł Python zawierający funkcje do przetwarzania danych oraz przewidywania satysfakcji pasażerów.

- modell oraz scalerr: Seryjny model regresji logistycznej oraz obiekt skali używany do przewidywania satysfakcji pasażerów.

Wizualizacja Danych i Analiza:

- FS_VISUALIZATION.twb: Plik Tableau zawierający wizualizacje i analizy danych, prezentujący kluczowe wnioski z przeprowadzonej analizy.

-------------------------------------------------------------------------------------------------------------------

Instalacja i Konfiguracja

Klonowanie Repozytorium:

git clone <repository-url>
cd <repository-directory>

Konfiguracja Bazy Danych:

Upewnij się, że masz zainstalowaną i uruchomioną bazę danych MySQL.
Zaktualizuj konfigurację bazy danych w pliku Integration_with_mysql.ipynb, aby pasowała do Twojej konfiguracji MySQL.
Uruchom notebook, aby utworzyć niezbędne tabele i wypełnić je danymi.

---------------------------------------------------------------------------------------------------------------------

Użycie

Przetwarzanie Danych:

Uruchom notebook DATA_PREPROCESSING.ipynb, aby oczyścić i wstępnie przetworzyć surowe dane.
Przetworzone dane zostaną zapisane jako flight_satisfaction_preprocessed.csv.

Trenowanie Modelu i Ewaluacja:

Użyj notebooka data_ML.ipynb, aby wytrenować model regresji logistycznej na wstępnie przetworzonych danych.
Notebook zawiera sekcje do oceny wydajności modelu oraz strojenia hiperparametrów.

Predykcja i Integracja z Bazą Danych:

Nowe dane z pliku data_to_module.csv mogą być użyte do przeprowadzania predykcji przy użyciu wytrenowanego modelu (tak jak w pliku integration_with_mysql).
Uruchom notebook Integration_with_mysql.ipynb, aby zintegrować te dane oraz wyniki predykcji z bazą danych MySQL.

Wizualizacja i Analiza:

plik Tableau (FS_VISUALIZATION.twb), aby zobaczyć wizualizacje i analizy wyników predykcji oraz danych dotyczących satysfakcji pasażerów.
