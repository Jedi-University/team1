# Team1
The most friendly team
========================

## Tasks

* Используя api.coingecko.com забрать ohlcv информацию о монетах за 365 дней.
* После разложить информацию по файлам по 30 записей в файле.

* Пример вызова API для BTC:
```bazaar
curl -X 'GET' \
  'https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=365' \
  -H 'accept: application/json'
```

* Документация на API:
```bazaar
https://www.coingecko.com/en/api/documentation
```

* Название используемого API:
```bazaar
/coins/{id}/ohlc
```

* Монеты для команд:
```bazaar
team-1: aave
team-2: ethereum
team-3: binancecoin
```

* Примечание к исполнению:
```bazaar
Нужно сделать аналог ETL дата пайплайна. 
Должно быть несколько скриптов, которые управляются общим оркестратором. 
Скрипт, который забирает все данные и кладет в файл, скрипт который ""дробит"" 
  данные и раскладывает по файлам. 
После работы скрипта оркестратора в папке должно лежать 1 файл со всеми данными
  и n файлов с дробленными данными.
Язык реализации любой, при одном условии, что все члены команды его знают.
```

* По полученным данным посчитать 30ое скользящее стреднее(SMA30) 
* В отдельный файл вывести те ohlcv, в которых цена закрытия выше чем SMA30 в данном временном блоке.

---

### Requirements by setup

```bazaar
Python3.9

python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt

```