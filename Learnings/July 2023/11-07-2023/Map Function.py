# map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]


to_dollars = lambda data: (data[0], data[1]*1.10)

store_dollars = map(to_dollars, store)

for i in store_dollars:
    print(i)

# 11/07/23