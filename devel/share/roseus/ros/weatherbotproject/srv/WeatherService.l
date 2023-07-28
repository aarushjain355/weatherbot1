;; Auto-generated. Do not edit!


(when (boundp 'weatherbotproject::WeatherService)
  (if (not (find-package "WEATHERBOTPROJECT"))
    (make-package "WEATHERBOTPROJECT"))
  (shadow 'WeatherService (find-package "WEATHERBOTPROJECT")))
(unless (find-package "WEATHERBOTPROJECT::WEATHERSERVICE")
  (make-package "WEATHERBOTPROJECT::WEATHERSERVICE"))
(unless (find-package "WEATHERBOTPROJECT::WEATHERSERVICEREQUEST")
  (make-package "WEATHERBOTPROJECT::WEATHERSERVICEREQUEST"))
(unless (find-package "WEATHERBOTPROJECT::WEATHERSERVICERESPONSE")
  (make-package "WEATHERBOTPROJECT::WEATHERSERVICERESPONSE"))

(in-package "ROS")





(defclass weatherbotproject::WeatherServiceRequest
  :super ros::object
  :slots (_Weather ))

(defmethod weatherbotproject::WeatherServiceRequest
  (:init
   (&key
    ((:Weather __Weather) "")
    )
   (send-super :init)
   (setq _Weather (string __Weather))
   self)
  (:Weather
   (&optional __Weather)
   (if __Weather (setq _Weather __Weather)) _Weather)
  (:serialization-length
   ()
   (+
    ;; string _Weather
    4 (length _Weather)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _Weather
       (write-long (length _Weather) s) (princ _Weather s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _Weather
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _Weather (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass weatherbotproject::WeatherServiceResponse
  :super ros::object
  :slots (_ok ))

(defmethod weatherbotproject::WeatherServiceResponse
  (:init
   (&key
    ((:ok __ok) 0)
    )
   (send-super :init)
   (setq _ok (round __ok))
   self)
  (:ok
   (&optional __ok)
   (if __ok (setq _ok __ok)) _ok)
  (:serialization-length
   ()
   (+
    ;; uint32 _ok
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _ok
       (write-long _ok s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _ok
     (setq _ok (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass weatherbotproject::WeatherService
  :super ros::object
  :slots ())

(setf (get weatherbotproject::WeatherService :md5sum-) "456b4033dd09be069e0eb63a859d7454")
(setf (get weatherbotproject::WeatherService :datatype-) "weatherbotproject/WeatherService")
(setf (get weatherbotproject::WeatherService :request) weatherbotproject::WeatherServiceRequest)
(setf (get weatherbotproject::WeatherService :response) weatherbotproject::WeatherServiceResponse)

(defmethod weatherbotproject::WeatherServiceRequest
  (:response () (instance weatherbotproject::WeatherServiceResponse :init)))

(setf (get weatherbotproject::WeatherServiceRequest :md5sum-) "456b4033dd09be069e0eb63a859d7454")
(setf (get weatherbotproject::WeatherServiceRequest :datatype-) "weatherbotproject/WeatherServiceRequest")
(setf (get weatherbotproject::WeatherServiceRequest :definition-)
      "string Weather
---
uint32 ok

")

(setf (get weatherbotproject::WeatherServiceResponse :md5sum-) "456b4033dd09be069e0eb63a859d7454")
(setf (get weatherbotproject::WeatherServiceResponse :datatype-) "weatherbotproject/WeatherServiceResponse")
(setf (get weatherbotproject::WeatherServiceResponse :definition-)
      "string Weather
---
uint32 ok

")



(provide :weatherbotproject/WeatherService "456b4033dd09be069e0eb63a859d7454")


