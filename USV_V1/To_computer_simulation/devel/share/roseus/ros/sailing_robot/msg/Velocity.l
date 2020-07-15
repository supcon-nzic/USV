;; Auto-generated. Do not edit!


(when (boundp 'sailing_robot::Velocity)
  (if (not (find-package "SAILING_ROBOT"))
    (make-package "SAILING_ROBOT"))
  (shadow 'Velocity (find-package "SAILING_ROBOT")))
(unless (find-package "SAILING_ROBOT::VELOCITY")
  (make-package "SAILING_ROBOT::VELOCITY"))

(in-package "ROS")
;;//! \htmlinclude Velocity.msg.html


(defclass sailing_robot::Velocity
  :super ros::object
  :slots (_speed _heading ))

(defmethod sailing_robot::Velocity
  (:init
   (&key
    ((:speed __speed) 0.0)
    ((:heading __heading) 0.0)
    )
   (send-super :init)
   (setq _speed (float __speed))
   (setq _heading (float __heading))
   self)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:heading
   (&optional __heading)
   (if __heading (setq _heading __heading)) _heading)
  (:serialization-length
   ()
   (+
    ;; float32 _speed
    4
    ;; float32 _heading
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _heading
       (sys::poke _heading (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _heading
     (setq _heading (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sailing_robot::Velocity :md5sum-) "d0661ebd150249ab8f58a7b5063ee3b9")
(setf (get sailing_robot::Velocity :datatype-) "sailing_robot/Velocity")
(setf (get sailing_robot::Velocity :definition-)
      "# message for publishing GPS velocity
float32 speed # [m/s]
float32 heading # [degrees]


")



(provide :sailing_robot/Velocity "d0661ebd150249ab8f58a7b5063ee3b9")


