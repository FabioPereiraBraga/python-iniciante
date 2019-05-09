cars = {}
cars['corola'] = 'red'
cars['fiat'] = 'green'
cars['320'] = 'black'

cars.keys()
cars.values()

people = dict(fabio='Father',Celma='Mother',Alice='baby')

for key, value in cars.items():
    print(key +" = "+ value);