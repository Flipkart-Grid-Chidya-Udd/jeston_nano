import rospy
from mavros_msgs.msg import HilGPS

def talker():
    rospy.init_node("talker")

    pub = HilGPS()
    pub1 = rospy.Publisher("/mavros/hil/gps", HilGPS, queue_size=1)

    pub.header.stamp = rospy.Time.now()
    pub.header.frame_id = "global"
    pub.fix_type = 3
    pub.geo.latitude = 25.26
    pub.geo.longitude = 82.99
    pub.geo.altitude = 0
    pub.satellites_visible = 4
    pub1.publish(pub)

while True:
    talker()
#    break



