import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 17


while True:

    humidity = Adafruit_DHT.read_retry(sensor, pin)[0]
    temperature = Adafruit_DHT.read_retry(sensor, pin)[1]
    
    if humidity is not None and temperature is not None:
         
        print('      Temperatur:', temperature, '°C')
        print('Luftfeuchtigkeit:', humidity, '%')
    else:
        print('Fehler bei der Messung. Versuche es erneut.')
        
    print()
    time.sleep(1)