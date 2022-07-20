def get_snapshot(connection):
	speed = connection.query(obd.commands.SPEED)
	rpm = connection.query(obd.commands.RPM)
	absolute_load = connection.query(obd.commands.ABSOLUTE_LOAD)
	engine_load = connection.query(obd.commands.ENGINE_LOAD)
	absolute_throttle_position = connection.query(obd.commands.THROTTLE_POS)
	relative_throttle_position = connection.query(obd.commands.RELATIVE_THROTTLE_POS)
	throttle_pos_b = connection.query(obd.commands.THROTTLE_POS_B)
	throttle_pos_c = connection.query(obd.commands.THROTTLE_POS_C)
	accelerator_pos_d = connection.query(obd.commands.ACCELERATOR_POS_D)
	accelerator_pos_e = connection.query(obd.commands.ACCELERATOR_POS_E)
	accelerator_pos_f = connection.query(obd.commands.ACCELERATOR_POS_F)
	fuel_level = connection.query(obd.commands.FUEL_LEVEL)

	values = (speed,
<<<<<<< HEAD
	            rpm,
	            absolute_load,
	            engine_load,
	            absolute_throttle_position,
	            relative_throttle_position,
	            throttle_pos_b,
	            throttle_pos_c,
	            accelerator_pos_d,
	            accelerator_pos_e,
	            accelerator_pos_f,
	            fuel_level)
	return values
=======
	            rpm,
	            absolute_load,
	            engine_load,
	            absolute_throttle_position,
	            relative_throttle_position,
	            throttle_pos_b,
	            throttle_pos_c,
	            accelerator_pos_d,
	            accelerator_pos_e,
	            accelerator_pos_f,
	            fuel_level)
	
	return values			
>>>>>>> 267e5bc472f206b1e82290a0fef08609e38e735d
