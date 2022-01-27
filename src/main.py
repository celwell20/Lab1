"""@file        main.py
   @brief       FSM main program
   @details     Runs encoder and motor drivers to verify their functionality
   @author        Clayton Elwell
   @author        Tyler McCue
   @date          January 27, 2022
"""

import encoder_elwell_mccue as enc
import motor_elwell_mccue as moe
import pyb
import time

if __name__ == '__main__':
    ## Driver object for first motor
    motor1 = moe.MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, 3)
    
    motor1.enable()
    
    ## Driver object for second motor
    motor2 = moe.MotorDriver(pyb.Pin.cpu.C1, pyb.Pin.cpu.A0, pyb.Pin.cpu.A1, 5)
    motor2.enable()
    
    ## Driver object for first encoder
    enc1 = enc.EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, 4)
    ## Driver object for second encoder
    enc2 = enc.EncoderDriver(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, 8)
    
    enc1.set_position(0)
    enc2.set_position(0)
    
    motor1.set_duty_cycle(-30)
    motor2.set_duty_cycle(-30)
                          
    
    while True:
        try:
            print('{:}, {:}'.format(enc1.update(), enc2.update()))
            time.sleep(.1)
        except KeyboardInterrupt:
            motor1.set_duty_cycle(0)
            motor2.set_duty_cycle(0)
            motor1.disable()
            motor2.disable()
            break
    
    
