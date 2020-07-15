;; Auto-generated. Do not edit!


(when (boundp 'sailing_robot::gpswtime)
  (if (not (find-package "SAILING_ROBOT"))
    (make-package "SAILING_ROBOT"))
  (shadow 'gpswtime (find-package "SAILING_ROBOT")))
(unless (find-package "SAILING_ROBOT::GPSWTIME")
  (make-package "SAILING_ROBOT::GPSWTIME"))

(in-package "ROS")
;;//! \htmlinclude gpswtime.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass sailing_robot::gpswtime
  :super ros::object
  :slots (_fix _time_h _time_m _time_s ))

(defmethod sailing_robot::gpswtime
  (:init
   (&key
    ((:fix __fix) (instance sensor_msgs::NavSatFix :init))
    ((:time_h __time_h) 0)
    ((:time_m __time_m) 0)
    ((:time_s __time_s) 0)
    )
   (send-super :init)
   (setq _fix __fix)
   (setq _time_h (round __time_h))
   (setq _time_m (round __time_m))
   (setq _time_s (round __time_s))
   self)
  (:fix
   (&rest __fix)
   (if (keywordp (car __fix))
       (send* _fix __fix)
     (progn
       (if __fix (setq _fix (car __fix)))
       _fix)))
  (:time_h
   (&optional __time_h)
   (if __time_h (setq _time_h __time_h)) _time_h)
  (:time_m
   (&optional __time_m)
   (if __time_m (setq _time_m __time_m)) _time_m)
  (:time_s
   (&optional __time_s)
   (if __time_s (setq _time_s __time_s)) _time_s)
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/NavSatFix _fix
    (send _fix :serialization-length)
    ;; uint16 _time_h
    2
    ;; uint16 _time_m
    2
    ;; uint16 _time_s
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/NavSatFix _fix
       (send _fix :serialize s)
     ;; uint16 _time_h
       (write-word _time_h s)
     ;; uint16 _time_m
       (write-word _time_m s)
     ;; uint16 _time_s
       (write-word _time_s s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/NavSatFix _fix
     (send _fix :deserialize buf ptr-) (incf ptr- (send _fix :serialization-length))
   ;; uint16 _time_h
     (setq _time_h (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _time_m
     (setq _time_m (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _time_s
     (setq _time_s (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get sailing_robot::gpswtime :md5sum-) "40d5a21afc2b40bb67f25cf656a9b364")
(setf (get sailing_robot::gpswtime :datatype-) "sailing_robot/gpswtime")
(setf (get sailing_robot::gpswtime :definition-)
      "# Message for GPS fix with time
sensor_msgs/NavSatFix fix
uint16 time_h
uint16 time_m
uint16 time_s

================================================================================
MSG: sensor_msgs/NavSatFix
# Navigation Satellite fix for any Global Navigation Satellite System
#
# Specified using the WGS 84 reference ellipsoid

# header.stamp specifies the ROS time for this measurement (the
#        corresponding satellite time may be reported using the
#        sensor_msgs/TimeReference message).
#
# header.frame_id is the frame of reference reported by the satellite
#        receiver, usually the location of the antenna.  This is a
#        Euclidean frame relative to the vehicle, not a reference
#        ellipsoid.
Header header

# satellite fix status information
NavSatStatus status

# Latitude [degrees]. Positive is north of equator; negative is south.
float64 latitude

# Longitude [degrees]. Positive is east of prime meridian; negative is west.
float64 longitude

# Altitude [m]. Positive is above the WGS 84 ellipsoid
# (quiet NaN if no altitude is available).
float64 altitude

# Position covariance [m^2] defined relative to a tangential plane
# through the reported position. The components are East, North, and
# Up (ENU), in row-major order.
#
# Beware: this coordinate system exhibits singularities at the poles.

float64[9] position_covariance

# If the covariance of the fix is known, fill it in completely. If the
# GPS receiver provides the variance of each measurement, put them
# along the diagonal. If only Dilution of Precision is available,
# estimate an approximate covariance from that.

uint8 COVARIANCE_TYPE_UNKNOWN = 0
uint8 COVARIANCE_TYPE_APPROXIMATED = 1
uint8 COVARIANCE_TYPE_DIAGONAL_KNOWN = 2
uint8 COVARIANCE_TYPE_KNOWN = 3

uint8 position_covariance_type

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: sensor_msgs/NavSatStatus
# Navigation Satellite fix status for any Global Navigation Satellite System

# Whether to output an augmented fix is determined by both the fix
# type and the last time differential corrections were received.  A
# fix is valid when status >= STATUS_FIX.

int8 STATUS_NO_FIX =  -1        # unable to fix position
int8 STATUS_FIX =      0        # unaugmented fix
int8 STATUS_SBAS_FIX = 1        # with satellite-based augmentation
int8 STATUS_GBAS_FIX = 2        # with ground-based augmentation

int8 status

# Bits defining which Global Navigation Satellite System signals were
# used by the receiver.

uint16 SERVICE_GPS =     1
uint16 SERVICE_GLONASS = 2
uint16 SERVICE_COMPASS = 4      # includes BeiDou.
uint16 SERVICE_GALILEO = 8

uint16 service

")



(provide :sailing_robot/gpswtime "40d5a21afc2b40bb67f25cf656a9b364")


