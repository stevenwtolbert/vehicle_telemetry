import IMU
import obd

def init_sensors():
	IMU.detectIMU()
	if(IMU.BerryIMUversion == 99):
	        IMU = None

	IMU.initIMU()
	try:
		OBD = obd.OBD()
	except:
		OBD = None

	return(IMU, OBD)
