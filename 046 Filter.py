friends = [("Rachel",19),
            ("Monica", 18),
            ("Phoebe", 17),
            ("Joey", 16),
            ("Chandler",21),
            ("Ross", 20)]

ageCheck = lambda data:data[1]>=18      #returns 'data' tuple if the condition is true
adult = list(filter(ageCheck,friends))

print(adult)