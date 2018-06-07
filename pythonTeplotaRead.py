from sense_hat import SenseHat
import MySQLdb
from time import sleep

sense = SenseHat()
conn = MySQLdb.connect(host= "35.189.84.124",
                    user="root",
                    passwd="krupice",
                    db="teplota")
x = conn.cursor()

while True:
    sense.clear()
    temp = sense.get_temperature()
    vlhkost = sense.get_humidity()

    print ("%.2f C %.2f %%" % (temp,vlhkost))

    try:
        x.execute("""INSERT INTO zaznam(teplota,vlhkost) VALUES (%s,%s)""",(temp,vlhkost))
        conn.commit()
    except:
       conn.rollback()

    sleep(5)
