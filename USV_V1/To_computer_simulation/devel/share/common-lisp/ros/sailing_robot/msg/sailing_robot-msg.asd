
(cl:in-package :asdf)

(defsystem "sailing_robot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BatteryState" :depends-on ("_package_BatteryState"))
    (:file "_package_BatteryState" :depends-on ("_package"))
    (:file "NaVSOL" :depends-on ("_package_NaVSOL"))
    (:file "_package_NaVSOL" :depends-on ("_package"))
    (:file "Velocity" :depends-on ("_package_Velocity"))
    (:file "_package_Velocity" :depends-on ("_package"))
    (:file "gpswtime" :depends-on ("_package_gpswtime"))
    (:file "_package_gpswtime" :depends-on ("_package"))
  ))