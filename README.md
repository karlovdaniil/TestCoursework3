# SkyPro / Test new Coursework 3

New feature for bank widget.

## Usage

Run "main.py" to run the application.

## App features

* Getting bank transactions data from JSON like this:
```
[
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    ...
  }
]
```
* As a result, the output consists of the last 5 executed (state = EXECUTED) operations
```
08.12.2019 Открытие вклада
Пополнение  -> Счет **5907
41096.24 USD

07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012  -> Счет **3655
48150.39 USD
```


## Run tests

```
pytest .
```
