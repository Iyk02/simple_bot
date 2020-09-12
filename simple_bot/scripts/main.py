#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from time import sleep

def mover():
    pub = rospy.Publisher('/joint_states', JointState, queue_size=1)
    rospy.init_node('bot_mover', anonymous=True)

    #rate = rospy.Rate(8)

    joint_state = JointState()
    #joint_state.header.stamp = rospy.Time.now()
    joint_state.name = ["joint_1", "joint_2"]
    
    joint_state.position = [3.14, 0.5]
    rospy.loginfo(joint_state)


    while not rospy.is_shutdown():
        joint_state.header.stamp = rospy.Time.now()
        pub.publish(joint_state)
        #rate.sleep()
        sleep(5)
  
if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass