# Team1
The most friendly team

## Tasks

```bazaar

Используя api.coingecko.com забрать ohlcv информацию о монетах за 365 дней, после разложить информацию по файлам по 30 записей в файле.

Пример вызова API для BTC: curl -X 'GET' \
  'https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=365' \
  -H 'accept: application/json'
  
Документация на API: https://www.coingecko.com/en/api/documentation
Название используемого API: /coins/{id}/ohlc   

Монеты для команд:
team-1: aave
team-2: ethereum
team-3: binancecoin

Примечание к исполнению:
    Нужно сделать аналог ETL дата пайплайна. 
    Должно быть несколько скриптов, которые управляются общим оркестратором. 
    Скрипт, который забирает все данные и кладет в файл, скрипт который ""дробит"" данные и раскладывает по файлам. 
    После работы скрипта оркестратора в папке должно лежать 1 файл со всеми данными и n файлов с дробленными данными.
    Язык реализации любой, при одном условии, что все члены команды его знают."
```

* Requirements by setup

```bazaar
Python3.9

python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt

```