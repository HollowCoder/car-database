class Vehicle:
    def __init__(self, model, licensePlate, color, maxSpeed):
        self.model = model
        self.licensePlate = licensePlate
        self.color = color
        self.maxSpeed = maxSpeed

    def get_vehicle_model(self):
        return self.model
    
    def get_vehicle_license_plate(self):
        return self.licensePlate

    def get_color(self):
        return self.color

    def get_vehicle_max_speed(self):
        return self.maxSpeed