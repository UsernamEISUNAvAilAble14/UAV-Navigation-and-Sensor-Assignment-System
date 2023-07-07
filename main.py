import random
import time
import threading
from UAV import UAV
from enum import Enum

class SensorType(Enum):
    TYPE_1 = 0
    TYPE_2 = 1
    TYPE_3 = 2
    TYPE_4 = 3
    TYPE_5 = 4


class Sensor:
    sensor_range_values = [20, 22, 28, 25, 35]

    def __init__(self, sensor_type, battery_percentage):
        self.sensor_type = sensor_type
        self.battery_percentage = battery_percentage
        self.sensor_range = self.sensor_range_values[sensor_type.value]
        self.location = self.generate_location()
        self.sensor_id = self.generate_sensor_id()

    def generate_location(self):
        x = random.randint(0, 50)
        y = random.randint(0, 50)
        return x, y

    def generate_sensor_id(self):
        return random.randint(1000, 9999)

    def display_details(self):
        print("Sensor ID:", self.sensor_id)
        print("Sensor Type:", self.sensor_type)
        print("Battery Percentage:", self.battery_percentage)
        print("Sensor Range:", self.sensor_range)
        print("Location:", self.location)
        print()


class EventType(Enum):
    TYPE_1 = 0
    TYPE_2 = 1
    TYPE_3 = 2
    TYPE_4 = 3
    TYPE_5 = 4


class Event:
    event_range_values = [10, 12, 8, 5, 15]
    event_duration_values = [9, 10, 6, 15, 11]

    def __init__(self, event_type, time_interval, event_time):
        self.event_type = event_type
        self.event_range = self.event_range_values[event_type.value]
        self.event_duration = self.event_duration_values[event_type.value]
        self.location = self.generate_location()
        self.time_interval = time_interval
        self.event_time = event_time

    def generate_location(self):
        x = random.randint(0, 50)
        y = random.randint(0, 50)
        return x, y

    def display_details(self):
        print("Event Type:", self.event_type)
        print("Event Range:", self.event_range)
        print("Location:", self.location)
        print("Time Interval:", self.time_interval)
        print("Event Duration:", self.event_duration)
        print()

    def run(self):
        time.sleep(self.event_duration)
        # Event completed

    def generate_next(self):
        time.sleep(self.time_interval)
        new_event_type = random.choice(list(EventType))
        new_event_time = self.event_time + self.time_interval
        new_event = Event(new_event_type, self.time_interval, new_event_time)
        new_event.run()
        new_event.generate_next()


# Define sensor details
sensor_details = []
for _ in range(15):
    sensor_type = random.choice(list(SensorType))
    battery_percentage = random.randint(50, 100)
    sensor = Sensor(sensor_type, battery_percentage)
    sensor_details.append(sensor)

# Display sensor details
print("Sensor Details:")
for sensor in sensor_details:
    sensor.display_details()

# Define event details
event_type = random.choice(list(EventType))
event_time = 0
event1 = Event(event_type, 5, event_time)
event_details = [event1]

# Generate 10 events during simulation time
for _ in range(9):
    event_type = random.choice(list(EventType))
    event_time += random.uniform(0.5, 2.0)
    event = Event(event_type, 5, event_time)
    event_details.append(event)

# Create UAVs
uav1 = UAV("UAV1", (0, 0), 500, 100)  # Example range_limit and battery_percentage values
uav2 = UAV("UAV2", (100, 100), 800, 80)  # Example range_limit and battery_percentage values

# Assign sensors to the closest UAV
uav1.assign_sensors(sensor_details)
uav2.assign_sensors(sensor_details)

# Calculate optimal paths for UAVs
uav1.find_optimal_path(sensor_details)
uav2.find_optimal_path(sensor_details)

# Display UAV details and paths
print("UAV Details:")
uav1.display_details()
uav2.display_details()

# Start UAV navigation
uav1.navigate()
uav2.navigate()

# Function to run events using threads
def run_events(events):
    threads = []
    for event in events:
        event_thread = threading.Thread(target=event.run)
        threads.append(event_thread)
        event_thread.start()

    # Wait for all threads to complete before moving forward
    for thread in threads:
        thread.join()

# Run events using threads
run_events(event_details)
