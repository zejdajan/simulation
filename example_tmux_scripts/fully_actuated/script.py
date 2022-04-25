from shutil import move
import rospy
from mavros_msgs.msg import PositionTarget

def talk():

    movement_publisher= rospy.Publisher('/uav11/mavros/setpoint_raw/local', PositionTarget , queue_size=10)
    rospy.init_node('test', anonymous=True)
    rate=rospy.Rate(30)
    rospy.loginfo("Started publisher node")
    movement_cmd = PositionTarget()
    movement_cmd.coordinate_frame=1
    movement_cmd.type_mask=2552
    movement_cmd.position.x=0.0
    movement_cmd.position.y=0.0
    movement_cmd.position.z=2.0
    
    movement_cmd.velocity.x=0.5
    movement_cmd.velocity.y=0.5
    movement_cmd.velocity.z=1.0

    movement_cmd.acceleration_or_force.x=0.0
    movement_cmd.acceleration_or_force.y=0.0
    movement_cmd.acceleration_or_force.z=0.0
    movement_cmd.yaw=0.0
    movement_cmd.yaw_rate=0.0
    while not rospy.is_shutdown(): 
        movement_publisher.publish(movement_cmd)
        rospy.loginfo("Published")
        rate.sleep()

    print("Publishing")
    rospy.spin()



if __name__=='__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass
