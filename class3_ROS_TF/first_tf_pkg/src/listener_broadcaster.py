#! /usr/bin/env python
import rospy
import tf


class TfListenerBroadCaster(object):
    def __init__(self):
        self._listener = tf.TransformListener()
        self._listener_rate = rospy.Rate(10) # 10Hz
        self._broad_caster_tf = tf.TransformBroadcaster()
        
    def Run(self):
        
        while not rospy.is_shutdown():
            try:
                '''
                동작 방식:

                waitForTransform: 이 함수는 특정한 변환 데이터를 기다립니다. 즉, 지정된 변환 데이터가 사용 가능할 때까지 대기하며, 사용 가능해질 때까지 프로그램 실행이 차단됩니다.
                lookupTransform: 이 함수는 현재 사용 가능한 변환 데이터를 즉시 검색하고 반환합니다. 만약 변환 데이터를 찾을 수 없으면 예외가 발생합니다.
                사용 사례:

                waitForTransform: 이 함수는 대개 변환 데이터가 아직 발생하지 않은 상황에서 대기할 때 사용됩니다. 예를 들어, 로봇이 시작하고 TF 변환 데이터가 아직 발생하지 않았을 때 대기하는 데 사용할 수 있습니다.
                lookupTransform: 이 함수는 현재 변환 데이터를 빠르게 검색하고 처리할 때 사용됩니다. 예를 들어, 로봇이 이미 이동 중이고 현재의 변환 데이터를 필요로 할 때 사용할 수 있습니다.
                '''
                # listener.waitForTransform(
                #    self._follower_model_frame, self._model_to_be_followed_frame, rospy.Time(0), rospy.Duration(0.5))
                (trans, rot) = self._listener.lookupTransform('gazebo_odom', 'base_link', rospy.Time(0))
                print("Translation: ", trans)
                print("Rotation: ", rot)
                
                self._broad_caster_tf.sendTransform((trans[0], trans[1], trans[2]),
                                            (rot[0], rot[1],
                                            rot[2], rot[3]),
                                            rospy.Time.now(),
                                            '/rviz_base_link',
                                            '/world')
                
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue

            self._listener_rate.sleep()

        
        
def main():
    rospy.init_node('tf_listener')
    TL = TfListenerBroadCaster()
    TL.Run()
    
if __name__ == '__main__':
    main()