def unpack_tuple():
    """
    This function unpack tuple
    :return: unpacked tuple
    """
    stock_prices = [('AAPL', 200), ('GOOG', 300), ('MSFT', 400)]
    for s,p in stock_prices:
        print(s)

unpack_tuple()