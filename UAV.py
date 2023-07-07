import math
import heapq
import time


class UAV:
    total_uavs = 0

    def __init__(self, name, start_position, range_limit, battery_percentage):
        UAV.total_uavs += 1
        self.name = name
        self.start_position = start_position
        self.range_limit = range_limit
        self.battery_percentage = battery_percentage
        self.path = []
        self.sensors_assigned = []

    def calculate_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def update_path(self, path):
        self.path = path

    def display_details(self):
        print("UAV Name:", self.name)
        print("Start Position:", self.start_position)
        print("Range Limit:", self.range_limit)
        print("Battery Percentage:", self.battery_percentage)
        print("Sensors Assigned:", self.sensors_assigned)
        print("Path:", self.path)
        print()

    def find_optimal_path(self, sensors):
        current_position = self.start_position
        remaining_sensors = sensors.copy()
        path = [current_position]

        while remaining_sensors:
            nearest_sensor = None
            nearest_distance = float("inf")

            for sensor in remaining_sensors:
                distance = self.calculate_distance(current_position, sensor.location)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_sensor = sensor

            if nearest_sensor:
                path.append(nearest_sensor.location)
                remaining_sensors.remove(nearest_sensor)
                current_position = nearest_sensor.location

        path.append(self.start_position)  # Return to the starting position
        self.update_path(path)

    def assign_sensors(self, sensors):
        remaining_sensors = list(sensors)

        while remaining_sensors:
            nearest_sensor = None
            nearest_distance = float("inf")
            for sensor in remaining_sensors:
                distance = self.calculate_distance(self.start_position, sensor.location)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_sensor = sensor

            if nearest_sensor:
                self.sensors_assigned.append(nearest_sensor)
                remaining_sensors.remove(nearest_sensor)

    def navigate(self):
        print(f"{self.name} is navigating.")

        for i in range(len(self.path) - 1):
            start = self.path[i]
            end = self.path[i + 1]
            distance = self.calculate_distance(start, end)

            # Check if the UAV can reach the next location
            if distance > self.range_limit * (self.battery_percentage / 100):
                print(f"{self.name} needs to recharge.")
                # Perform recharge process here
                time.sleep(5)  # Simulating recharge process
                print(f"{self.name} recharged.")

            self.battery_percentage -= distance / self.range_limit * 100
            print(f"{self.name} traveled from {start} to {end}. Battery remaining: {self.battery_percentage}%.")

        print(f"{self.name} completed navigation.")

    def calculate_total_distance(self):
        total_distance = 0
        for i in range(len(self.path) - 1):
            start = self.path[i]
            end = self.path[i + 1]
            total_distance += self.calculate_distance(start, end)
        return total_distance
