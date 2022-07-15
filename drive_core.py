import time
import IMU
import sys
import database_connector

IMU.detectIMU()     #Detect if BerryIMU is connected.
if(IMU.BerryIMUversion == 99):
	print(" No BerryIMU found... exiting ")
	sys.exit()

IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass
conn = database_connector.connect_mariadb()
cur = conn.cursor()

while True:
	try:
		#Read the accelerometer,gyroscope and magnetometer values
		ACCx = IMU.readACCx()
		ACCy = IMU.readACCy()
		ACCz = IMU.readACCz()
		xG = (ACCx * 0.244)/1000
		yG = (ACCy * 0.244)/1000
		zG = (ACCz * 0.244)/1000

		query = f"""INSERT INTO g_forces (xG, yG, zG) VALUES ({xG},{yG},{zG})""" 
		cur.execute(query)

		time.sleep(1)
	except:
		conn.commit()
		conn.close()
		sys.exit(1)
