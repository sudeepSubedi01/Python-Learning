store =[("shirt", 20.00),
        ("pants", 25.00),
        ("jacket", 50.00),
        ("socks", 10.00)]

toEuros = lambda data: (data[0], data[1] * 0.82)
toDollars = lambda data:(data[0], data[1]*2.0)

storeEuros = list(map(toEuros, store))
storeDollars = list(map(toDollars, store))

for i in storeEuros:
  print(i)
print( type (storeEuros))  #class list

for i in storeDollars:
  print(i)
