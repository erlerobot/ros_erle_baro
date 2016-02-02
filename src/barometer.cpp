#include "ros/ros.h"
#include "ros_barometer/bar.h"
#include "MS5611.h"

#include <sstream>


int main(int argc, char **argv){
	ros::init(argc, argv, "ros_barometer");

	ros::NodeHandle n;
	ros::Publisher pub=n.advertise<ros_barometer::bar>("barometer", 1000);

	ros::Rate loop_rate(10);

	MS5611 barometer;
	barometer.initialize();

	while (ros::ok()){
		ros_barometer::bar msg;

		barometer.refreshPressure();
        	usleep(10000); // Waiting for pressure data ready
        	barometer.readPressure();

	        barometer.refreshTemperature();
        	usleep(10000); // Waiting for temperature data ready
        	barometer.readTemperature();

        	barometer.calculatePressureAndTemperature();

		msg.TEMP = barometer.getTemperature();
		msg.PRES = barometer.getPressure();
		pub.publish(msg);

		ros::spinOnce();
		loop_rate.sleep();
	}
	return 0;
}
