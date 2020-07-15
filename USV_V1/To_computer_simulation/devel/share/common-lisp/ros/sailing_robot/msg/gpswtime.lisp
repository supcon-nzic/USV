; Auto-generated. Do not edit!


(cl:in-package sailing_robot-msg)


;//! \htmlinclude gpswtime.msg.html

(cl:defclass <gpswtime> (roslisp-msg-protocol:ros-message)
  ((fix
    :reader fix
    :initarg :fix
    :type sensor_msgs-msg:NavSatFix
    :initform (cl:make-instance 'sensor_msgs-msg:NavSatFix))
   (time_h
    :reader time_h
    :initarg :time_h
    :type cl:fixnum
    :initform 0)
   (time_m
    :reader time_m
    :initarg :time_m
    :type cl:fixnum
    :initform 0)
   (time_s
    :reader time_s
    :initarg :time_s
    :type cl:fixnum
    :initform 0))
)

(cl:defclass gpswtime (<gpswtime>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gpswtime>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gpswtime)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sailing_robot-msg:<gpswtime> is deprecated: use sailing_robot-msg:gpswtime instead.")))

(cl:ensure-generic-function 'fix-val :lambda-list '(m))
(cl:defmethod fix-val ((m <gpswtime>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sailing_robot-msg:fix-val is deprecated.  Use sailing_robot-msg:fix instead.")
  (fix m))

(cl:ensure-generic-function 'time_h-val :lambda-list '(m))
(cl:defmethod time_h-val ((m <gpswtime>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sailing_robot-msg:time_h-val is deprecated.  Use sailing_robot-msg:time_h instead.")
  (time_h m))

(cl:ensure-generic-function 'time_m-val :lambda-list '(m))
(cl:defmethod time_m-val ((m <gpswtime>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sailing_robot-msg:time_m-val is deprecated.  Use sailing_robot-msg:time_m instead.")
  (time_m m))

(cl:ensure-generic-function 'time_s-val :lambda-list '(m))
(cl:defmethod time_s-val ((m <gpswtime>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sailing_robot-msg:time_s-val is deprecated.  Use sailing_robot-msg:time_s instead.")
  (time_s m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gpswtime>) ostream)
  "Serializes a message object of type '<gpswtime>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'fix) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time_h)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time_h)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time_m)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time_m)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time_s)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time_s)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gpswtime>) istream)
  "Deserializes a message object of type '<gpswtime>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'fix) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time_h)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time_h)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time_m)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time_m)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time_s)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time_s)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gpswtime>)))
  "Returns string type for a message object of type '<gpswtime>"
  "sailing_robot/gpswtime")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gpswtime)))
  "Returns string type for a message object of type 'gpswtime"
  "sailing_robot/gpswtime")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gpswtime>)))
  "Returns md5sum for a message object of type '<gpswtime>"
  "40d5a21afc2b40bb67f25cf656a9b364")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gpswtime)))
  "Returns md5sum for a message object of type 'gpswtime"
  "40d5a21afc2b40bb67f25cf656a9b364")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gpswtime>)))
  "Returns full string definition for message of type '<gpswtime>"
  (cl:format cl:nil "# Message for GPS fix with time~%sensor_msgs/NavSatFix fix~%uint16 time_h~%uint16 time_m~%uint16 time_s~%~%================================================================================~%MSG: sensor_msgs/NavSatFix~%# Navigation Satellite fix for any Global Navigation Satellite System~%#~%# Specified using the WGS 84 reference ellipsoid~%~%# header.stamp specifies the ROS time for this measurement (the~%#        corresponding satellite time may be reported using the~%#        sensor_msgs/TimeReference message).~%#~%# header.frame_id is the frame of reference reported by the satellite~%#        receiver, usually the location of the antenna.  This is a~%#        Euclidean frame relative to the vehicle, not a reference~%#        ellipsoid.~%Header header~%~%# satellite fix status information~%NavSatStatus status~%~%# Latitude [degrees]. Positive is north of equator; negative is south.~%float64 latitude~%~%# Longitude [degrees]. Positive is east of prime meridian; negative is west.~%float64 longitude~%~%# Altitude [m]. Positive is above the WGS 84 ellipsoid~%# (quiet NaN if no altitude is available).~%float64 altitude~%~%# Position covariance [m^2] defined relative to a tangential plane~%# through the reported position. The components are East, North, and~%# Up (ENU), in row-major order.~%#~%# Beware: this coordinate system exhibits singularities at the poles.~%~%float64[9] position_covariance~%~%# If the covariance of the fix is known, fill it in completely. If the~%# GPS receiver provides the variance of each measurement, put them~%# along the diagonal. If only Dilution of Precision is available,~%# estimate an approximate covariance from that.~%~%uint8 COVARIANCE_TYPE_UNKNOWN = 0~%uint8 COVARIANCE_TYPE_APPROXIMATED = 1~%uint8 COVARIANCE_TYPE_DIAGONAL_KNOWN = 2~%uint8 COVARIANCE_TYPE_KNOWN = 3~%~%uint8 position_covariance_type~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/NavSatStatus~%# Navigation Satellite fix status for any Global Navigation Satellite System~%~%# Whether to output an augmented fix is determined by both the fix~%# type and the last time differential corrections were received.  A~%# fix is valid when status >= STATUS_FIX.~%~%int8 STATUS_NO_FIX =  -1        # unable to fix position~%int8 STATUS_FIX =      0        # unaugmented fix~%int8 STATUS_SBAS_FIX = 1        # with satellite-based augmentation~%int8 STATUS_GBAS_FIX = 2        # with ground-based augmentation~%~%int8 status~%~%# Bits defining which Global Navigation Satellite System signals were~%# used by the receiver.~%~%uint16 SERVICE_GPS =     1~%uint16 SERVICE_GLONASS = 2~%uint16 SERVICE_COMPASS = 4      # includes BeiDou.~%uint16 SERVICE_GALILEO = 8~%~%uint16 service~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gpswtime)))
  "Returns full string definition for message of type 'gpswtime"
  (cl:format cl:nil "# Message for GPS fix with time~%sensor_msgs/NavSatFix fix~%uint16 time_h~%uint16 time_m~%uint16 time_s~%~%================================================================================~%MSG: sensor_msgs/NavSatFix~%# Navigation Satellite fix for any Global Navigation Satellite System~%#~%# Specified using the WGS 84 reference ellipsoid~%~%# header.stamp specifies the ROS time for this measurement (the~%#        corresponding satellite time may be reported using the~%#        sensor_msgs/TimeReference message).~%#~%# header.frame_id is the frame of reference reported by the satellite~%#        receiver, usually the location of the antenna.  This is a~%#        Euclidean frame relative to the vehicle, not a reference~%#        ellipsoid.~%Header header~%~%# satellite fix status information~%NavSatStatus status~%~%# Latitude [degrees]. Positive is north of equator; negative is south.~%float64 latitude~%~%# Longitude [degrees]. Positive is east of prime meridian; negative is west.~%float64 longitude~%~%# Altitude [m]. Positive is above the WGS 84 ellipsoid~%# (quiet NaN if no altitude is available).~%float64 altitude~%~%# Position covariance [m^2] defined relative to a tangential plane~%# through the reported position. The components are East, North, and~%# Up (ENU), in row-major order.~%#~%# Beware: this coordinate system exhibits singularities at the poles.~%~%float64[9] position_covariance~%~%# If the covariance of the fix is known, fill it in completely. If the~%# GPS receiver provides the variance of each measurement, put them~%# along the diagonal. If only Dilution of Precision is available,~%# estimate an approximate covariance from that.~%~%uint8 COVARIANCE_TYPE_UNKNOWN = 0~%uint8 COVARIANCE_TYPE_APPROXIMATED = 1~%uint8 COVARIANCE_TYPE_DIAGONAL_KNOWN = 2~%uint8 COVARIANCE_TYPE_KNOWN = 3~%~%uint8 position_covariance_type~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/NavSatStatus~%# Navigation Satellite fix status for any Global Navigation Satellite System~%~%# Whether to output an augmented fix is determined by both the fix~%# type and the last time differential corrections were received.  A~%# fix is valid when status >= STATUS_FIX.~%~%int8 STATUS_NO_FIX =  -1        # unable to fix position~%int8 STATUS_FIX =      0        # unaugmented fix~%int8 STATUS_SBAS_FIX = 1        # with satellite-based augmentation~%int8 STATUS_GBAS_FIX = 2        # with ground-based augmentation~%~%int8 status~%~%# Bits defining which Global Navigation Satellite System signals were~%# used by the receiver.~%~%uint16 SERVICE_GPS =     1~%uint16 SERVICE_GLONASS = 2~%uint16 SERVICE_COMPASS = 4      # includes BeiDou.~%uint16 SERVICE_GALILEO = 8~%~%uint16 service~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gpswtime>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'fix))
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gpswtime>))
  "Converts a ROS message object to a list"
  (cl:list 'gpswtime
    (cl:cons ':fix (fix msg))
    (cl:cons ':time_h (time_h msg))
    (cl:cons ':time_m (time_m msg))
    (cl:cons ':time_s (time_s msg))
))
