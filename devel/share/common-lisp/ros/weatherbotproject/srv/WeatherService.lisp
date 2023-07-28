; Auto-generated. Do not edit!


(cl:in-package weatherbotproject-srv)


;//! \htmlinclude WeatherService-request.msg.html

(cl:defclass <WeatherService-request> (roslisp-msg-protocol:ros-message)
  ((Weather
    :reader Weather
    :initarg :Weather
    :type cl:string
    :initform ""))
)

(cl:defclass WeatherService-request (<WeatherService-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WeatherService-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WeatherService-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name weatherbotproject-srv:<WeatherService-request> is deprecated: use weatherbotproject-srv:WeatherService-request instead.")))

(cl:ensure-generic-function 'Weather-val :lambda-list '(m))
(cl:defmethod Weather-val ((m <WeatherService-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weatherbotproject-srv:Weather-val is deprecated.  Use weatherbotproject-srv:Weather instead.")
  (Weather m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WeatherService-request>) ostream)
  "Serializes a message object of type '<WeatherService-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'Weather))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'Weather))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WeatherService-request>) istream)
  "Deserializes a message object of type '<WeatherService-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Weather) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'Weather) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WeatherService-request>)))
  "Returns string type for a service object of type '<WeatherService-request>"
  "weatherbotproject/WeatherServiceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WeatherService-request)))
  "Returns string type for a service object of type 'WeatherService-request"
  "weatherbotproject/WeatherServiceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WeatherService-request>)))
  "Returns md5sum for a message object of type '<WeatherService-request>"
  "456b4033dd09be069e0eb63a859d7454")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WeatherService-request)))
  "Returns md5sum for a message object of type 'WeatherService-request"
  "456b4033dd09be069e0eb63a859d7454")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WeatherService-request>)))
  "Returns full string definition for message of type '<WeatherService-request>"
  (cl:format cl:nil "string Weather~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WeatherService-request)))
  "Returns full string definition for message of type 'WeatherService-request"
  (cl:format cl:nil "string Weather~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WeatherService-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'Weather))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WeatherService-request>))
  "Converts a ROS message object to a list"
  (cl:list 'WeatherService-request
    (cl:cons ':Weather (Weather msg))
))
;//! \htmlinclude WeatherService-response.msg.html

(cl:defclass <WeatherService-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:integer
    :initform 0))
)

(cl:defclass WeatherService-response (<WeatherService-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WeatherService-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WeatherService-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name weatherbotproject-srv:<WeatherService-response> is deprecated: use weatherbotproject-srv:WeatherService-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <WeatherService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weatherbotproject-srv:ok-val is deprecated.  Use weatherbotproject-srv:ok instead.")
  (ok m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WeatherService-response>) ostream)
  "Serializes a message object of type '<WeatherService-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ok)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ok)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'ok)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'ok)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WeatherService-response>) istream)
  "Deserializes a message object of type '<WeatherService-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ok)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ok)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'ok)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'ok)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WeatherService-response>)))
  "Returns string type for a service object of type '<WeatherService-response>"
  "weatherbotproject/WeatherServiceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WeatherService-response)))
  "Returns string type for a service object of type 'WeatherService-response"
  "weatherbotproject/WeatherServiceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WeatherService-response>)))
  "Returns md5sum for a message object of type '<WeatherService-response>"
  "456b4033dd09be069e0eb63a859d7454")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WeatherService-response)))
  "Returns md5sum for a message object of type 'WeatherService-response"
  "456b4033dd09be069e0eb63a859d7454")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WeatherService-response>)))
  "Returns full string definition for message of type '<WeatherService-response>"
  (cl:format cl:nil "uint32 ok~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WeatherService-response)))
  "Returns full string definition for message of type 'WeatherService-response"
  (cl:format cl:nil "uint32 ok~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WeatherService-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WeatherService-response>))
  "Converts a ROS message object to a list"
  (cl:list 'WeatherService-response
    (cl:cons ':ok (ok msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'WeatherService)))
  'WeatherService-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'WeatherService)))
  'WeatherService-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WeatherService)))
  "Returns string type for a service object of type '<WeatherService>"
  "weatherbotproject/WeatherService")