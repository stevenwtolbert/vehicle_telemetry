import time
from datetime import datetime
import sys
import database_connector
import obd_telemetry
import vehicle_sensors
import accelerometer
import gyroscope
import gps_data
import magnetometer
import queries

IMU, OBD = vehicle_sensors.init_sensors()
database_connection, cursor = database_connector.connect_mariadb()

while True:
	try:
		if(IMU):
			accelerometer_values = accelerometer.get_gforces(IMU)
			gyroscope_values = gyroscope.get_gyroscope_values(IMU)
			magnetometer_values = magnetometer.get_magnetometer_values(IMU)
			#gps_values = imu_gps(IMU)
			gps_values = (1,1)
		if(OBD):
			obd_values = obd_telemetry.get_snapshot(OBD)
		read_time = datetime.now().strftime('%Y-%M-%d %H:%M:%S')
		query = queries.insert_telemetry_data(read_time,
						      accelerometer_values,
						      gyroscope_values,
						      gps_values,
						      obd_values)
		cursor.execute(query)
		time.sleep(1)
	except:
		database_connection.commit()
		database_connection.close()
		sys.exit(1)
