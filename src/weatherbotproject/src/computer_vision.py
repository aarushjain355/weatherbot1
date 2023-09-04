
#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import cv2
import mediapipe as mp
import numpy as np
from cv_bridge import CvBridge, CvBridgeError


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

message = "don't know"

def calculate_angle(first, second, third):

    first = np.array(first)
    second = np.array(second)
    third = np.array(third)

    radians = np.arctan2(third[1] - second[1], third[0] - second[0]) - np.arctan2(first[1] - second[1], first[0] - second[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle > 180.0:
        angle = 360 - angle
    
    return angle

if __name__ == "__main__":

    rospy.init_node("Emergency Detection")
    motion_publisher = rospy.Publisher('position', String, queue_size=10)

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
        
            results = pose.process(image)
        
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            try:
                landmarks = results.pose_landmarks.landmark

                  # Get coordinates
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE].y]
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP].y]
                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE].y]
                left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE].y]

                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].y]
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST].y]

                right_angle_leg = calculate_angle(right_hip, right_knee, right_ankle)
                left_angle_leg = calculate_angle(left_hip, left_knee, left_ankle)
                right_angle_arm = calculate_angle(right_shoulder, right_elbow, right_wrist)
                left_angle_arm = calculate_angle(left_shoulder, left_elbow, left_wrist)
                diff1 = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x - landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x
                diff2 = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x - landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x
                diff3 = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y - landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
                diff4 = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y - landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x
                
    
                
                if right_angle_leg < 100 and left_angle_leg < 100: #and right_angle_arm < 80 and left_angle_arm < 80 and abs(diff1) > abs(diff2) and diff3 > 0 and diff4 > 0:

                    message = "fire"

                elif diff4 > 0 and diff3 > 0 and diff2 < 0:
                    message = "cold"
                elif right_angle_arm > 150 and left_angle_arm > 150 and diff3 > 0 and diff4 > 0:
                    message = "neutral"
                
                elif right_angle_arm < 90 and left_angle_arm < 90 and diff3 < 0 and diff4 < 0:# and right_angle_leg > 160 and left_angle_leg > 160:
                   # print(landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y)
                   # print(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y)
                
                    message = "hot"

                cv2.putText(image, message, 
                           tuple(np.multiply(left_shoulder, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                
                motion_publisher.publish(message)
                
                print(message)
            except:

                pass
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )               
            
            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

