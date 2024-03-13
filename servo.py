from gpiozero import AngularServo

class Servo(AngularServo):
    def __init__(self, initial_angle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.angle, self.current_angle = initial_angle
    
    def set_angle(self, angle):
        if angle != self.current_angle:
            self.angle = angle
            self.current_angle = angle
        else:
            pass