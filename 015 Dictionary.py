capitals = {
  'USA' : 'Washington DC',
  'India' : 'New Dehli',
  'Nepal': 'Kathmandu',
  'China': 'Beijing'
}
capitals['India'] = 'NewDehli'
capitals['Bhutan'] = 'Thimpu'

print(capitals)
print(capitals['India'])
print(len(capitals))

print(capitals.get('Nepal'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Nepal': 'KTM'})
capitals.update({'Russia': 'Moscow'}) #merges the given dictionary with the original
capitals.pop('China') #pops out and removes it from the dictionary

for key,value in capitals.items():
  print(key,value)