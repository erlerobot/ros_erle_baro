"""
Provided to you by Emlid Ltd (c) 2014.
twitter.com/emlidtech || www.emlid.com || info@emlid.com

Example: Get pressure from MS5611 barometer onboard of Navio shield for Raspberry Pi

To run this example navigate to the directory containing it and run following commands:
sudo python Barometer_example.py
"""



import time
import rospy


from MS5611 import MS5611
from ros_barometer.msg import bar


def talker():
	pub = rospy.Publisher('barometer',bar, queue_size=10)
	rospy.init_node('ros_barometer', anonymous=True)
	rate = rospy.Rate(10) 

	baro = MS5611()
	baro.initialize()
	
	msg = bar()

	while not rospy.is_shutdown():
		
		baro.refreshPressure()
		baro.readPressure()

		baro.refreshTemperature()
		baro.readTemperature()		

		baro.calculatePressureAndTemperature()
		msg.TEMP=baro.returnTemperature()
		msg.PRES=baro.returnPressure()
		
		pub.publish(msg)
			
		rate.sleep()


if __name__ == '__main__':
	try:
        	talker()
    	except rospy.ROSInterruptException:
        	pass
