from sense_hat import SenseHat
from networktables import NetworkTables
import time

NetworkTables.initialize(server='roborio-2022-frc.local')
hat = SenseHat()
table = NetworkTables.getTable("sensors")
clock = time.time()

while True:
    if time.time() - clock >= 0.33:
        hat.load_image("pixart/{}.png".format(table.getString("display", "dead")))
        clock = time.time()
    acceleration = hat.get_accelerometer_raw()
    table.putNumberArray("shAccel", [acceleration["x"], acceleration["y"], acceleration["z"]])
    time.sleep(0.02)
