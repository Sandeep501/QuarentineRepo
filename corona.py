import requests

url='https://pomber.github.io/covid19/timeseries.json'

data=(requests.get(url)).json()

data=data['India'][-1]

date=data['date']

confirmed=data['confirmed']

recovered=data['recovered']

deaths=data['deaths']

print('As of {0} confirmed Corona cases in India are {1}'.format(date,confirmed))

print('out of this {0} were recovered and {1} are dead'.format(recovered,deaths))
# made some change
