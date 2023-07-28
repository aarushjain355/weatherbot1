
(cl:in-package :asdf)

(defsystem "weatherbotproject-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "WeatherService" :depends-on ("_package_WeatherService"))
    (:file "_package_WeatherService" :depends-on ("_package"))
  ))