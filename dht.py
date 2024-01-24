import Adafruit_DHT
import time

sensor = Adafruit_DHT._____
pin = __


while ____:

    humidity = Adafruit_DHT.read_retry(sensor, pin)[0]
    temperature = Adafruit_DHT.read_retry(sensor, pin)[1]
    
    if ________ is not ____ and ___________ is not ____:
         
        print('      ___________:', temperature, '__')
        print('_________________:', humidity, '_')
    else:
        print('Fehler bei der Messung. Versuche es erneut.')
        
    print()
    time.sleep(_)
