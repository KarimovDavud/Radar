from random import randint, choice


class Radar:
    def __init__(self, road_name, road_limit, max_speed):
        self.road_name = road_name
        self.road_limit = road_limit
        self.max_speed = max_speed
        self.car_speed = None
        self.speed_result = None
        self.belt_result = None
    
    def check_speed(self):
        self.car_speed = randint(0, 240)  
        if self.road_limit <= self.car_speed <= self.max_speed:
            self.speed_result = "No fine"
        elif self.road_limit <= self.car_speed <= self.max_speed + 10:
            self.speed_result = "You were fined 10 manats"
        elif self.road_limit <= self.car_speed <= self.max_speed + 60:
            self.speed_result = "You were fined 50 manats and 2 points"
        elif self.road_limit <= self.car_speed <= self.max_speed + 120:
            self.speed_result = "You were fined 200 manats and 4 points"
        elif self.car_speed > self.max_speed + 120:
            self.speed_result = "You were fined 300 manats and 15 days in prison"
        return self.speed_result
        
    def check_seat_belt(self):
        if choice([True, False]):
            self.belt_result = "Belt is on"
        else:
            self.belt_result = "You were fined 40 manats for not wearing a seat belt"
        return self.belt_result