import time
import board
import busio
import adafruit_lsm303
 
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm303.LSM303(i2c)
 
# work on some fileio improveents, data header, tests to see if
# flight is over (set flag if sudden change in accel
#test if dirty bit AND no change in data for 10 consecutive readings
#
#

while True:
    acc_x, acc_y, acc_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic
    print('{0:10.3f}{1:10.3f}{2:10.3f}'.format(acc_x,acc_y,acc_z), file=open('/home/pi/dinkything/lsmplot.dat', 'a'))
    print('')
    time.sleep(1.0)
