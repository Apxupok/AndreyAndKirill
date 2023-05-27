#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

#Объявляем моторы
motor_left = Motor(Port.A)
motorb_right = Motor(Port.B)
motord_grip = Motor(Port.D)

#Объявляем датчики
ultra = UltrasonicSensor(Port.S1)
touch = TouchSensor(Port.S2)й
gyro = GyroSensor(Port.S3)

#Переменная для подсчета расстояния на обратную езду
revers = 0

while True:
    #Сброс энкодера мотора 
    motora.reset_angle(0)

    #Ждем объекта перед датчиком
    if Ultra.distance() <= 200:

        motord_grip.run_angle(30, 200)
        wait(1000)

        motor_left.run(200)
        motorb.angle_run(180, -200)
        wait(1000)

        while not Touch.presseed():
            motor_left.run(200)
            motorb_right.run(200)

        revers = motora.angle(0)

        motord.run_angle(30, -200)

        if Ultra.distance() <= 201:
            motor_left.run(-200)
            motorb_right.run_angle(180, -200)
            wait(1000)
            
            motor_left.run_target(revers,-200)
            motorb_right.run_target(revers,-200)


