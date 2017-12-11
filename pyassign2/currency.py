#!/usr/bin/env python3

"""currency.py: Exhange a specific amount of money from one currency to another.

__author__ = "Zhao Jingliang"
__pkuid__  = "1700011787"
__email__  = "Roentgenium@pku.edu.cn"
"""


def get_to(json):
    """To get the numerical value of exchange result from the string.
    """
    json_split = json.split('"')
    json_currency_to = json_split[7]
    json_currency_list = json_currency_to.split()
    json_currency_number = json_currency_list[0]
    return float(json_currency_number)


def error_type(json):
    """To judge which type of error occurs.
    """
    judge = 0
    if json[56:59] == 'Sou':
        judge = 1
    elif json[56:59] == 'Exc':
        judge = 2
    elif json[56:59] == 'Cur':
        judge = 3
    else:
        judge = 0
    return judge


def has_error(json):
    """To judge whether the input value is valid.
    If it's valid,it'll print False.

    For example:
    >>>has_error('{ "from" : "", "to" : "", "success" : false, "error" : "Curr\
ency amount is invalid." }')
    >>>True
    """
    judge_value = error_type(json)
    judge_result = True
    if judge_value > 0:
        judge_result = True
    else:
        judge_result = False
    return judge_result


def exchange(currency_from, currency_to, amount_from):
    """
    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The supported input value of currency_from and currency_to should be in \
the Currency Exchange Table in http://www.cs.cornell.edu/courses/cs1110/\
2016fa/assignments/assignment1/index.php

    For example:
    >>>exchange("USD","EUR",2.5)
    >>>2.0952375
    (This value may change at any specific time)
    """
    from urllib.request import urlopen

    Url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' \
        + str(currency_from) + '&to=' + str(currency_to) + '&amt=' \
        + str(amount_from)
    doc = urlopen(Url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    judge_value = error_type(jstr)
    if judge_value == 1:
        print("Source currency code is invalid")
    elif judge_value == 2:
        print("Exchange currency code is invalid")
    elif judge_value == 3:
        print("Currency amount is invalid")
    else:
        return get_to(jstr)


def test_get_to():
    """To test whether the fuction 'get_to' work or not.
    """
    assert get_to('{ "from" : "2.5 Euros", "to" : "19.467214337277 Chinese Yuan\
","success" : true, "error" : "" }') == 19.467214337277


def test_error_type():
    """To test whether the fuction 'error_type' work or not.
    """
    assert error_type('{ "from" : "", "to" : "", "success" : false, "error" : "\
Source currency code is invalid." }') == 1
    assert error_type('{ "from" : "", "to" : "", "success" : false, "error" : "\
Exchange currency code is invalid." }') == 2
    assert error_type('{ "from" : "", "to" : "", "success" : false, "error" : "\
Currency amount is invalid." }') == 3


def test_exchange():
    """To test whether the fuction 'exchange' can work normally or not.
    """
    exchange_rate = exchange("USD", "EUR", 2.5)
    re_exchange_rate = exchange("EUR", "USD", exchange_rate)
    assert re_exchange_rate == 2.5


def test_all():
    """To test all cases."""
    test_get_to()
    test_error_type()
    test_exchange()
    print("All tests passed.")

if __name__ == "__main__":
    test_all()
    Currency_to = input()
    Currency_from = input()
    Amount_from = input()
    print(exchange(Currency_to, Currency_from, Amount_from))
