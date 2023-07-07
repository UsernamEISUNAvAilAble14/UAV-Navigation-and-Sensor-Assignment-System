# UAV-Navigation-and-Sensor-Assignment-System
Project Documentation
Welcome to the documentation for the project. This document provides an overview of the project and its components, along with instructions on how to use them. The project involves the simulation of Unmanned Aerial Vehicles (UAVs) navigating to various events while considering battery constraints and assigned sensors. Let's dive into the details!

Table of Contents
Introduction
Project Structure
Components
Sensor
Event
UAV
Usage
Example
Conclusion
Introduction<a name="introduction"></a>
The project focuses on simulating the behavior of UAVs navigating to different events while considering the range of the UAVs, battery constraints, and assigned sensors. The goal is to optimize the paths of the UAVs and efficiently complete the events.

Project Structure<a name="project-structure"></a>
The project consists of two Python files: main.py and UAV.py. The main.py file serves as the entry point for the simulation, while UAV.py contains the implementation of the UAV class.

Components<a name="components"></a>
Let's explore the components of the project in detail.

Sensor<a name="sensor"></a>
The Sensor class represents a sensor used by the UAVs. Each sensor has a specific type, battery percentage, sensor range, location, and sensor ID. The sensor types are defined using the SensorType enum, and the corresponding range values are stored in the sensor_range_values list. The sensors are randomly generated with unique IDs and locations.

Event<a name="event"></a>
The Event class represents an event that the UAVs need to navigate to. Each event has a specific type, event range, location, time interval, and event duration. The event types are defined using the EventType enum, and the corresponding range and duration values are stored in the event_range_values and event_duration_values lists, respectively. The events are randomly generated with increasing time intervals.

UAV<a name="uav"></a>
The UAV class represents an Unmanned Aerial Vehicle. Each UAV has a name, start position, range limit, battery percentage, assigned sensors, and a path. The UAVs navigate to events based on the assigned sensors and the optimal path calculated using the nearest neighbor algorithm. The UAVs consider battery constraints during navigation and recharge if necessary. The total distance traveled by a UAV can be calculated using the calculate_total_distance() method.

Usage<a name="usage"></a>
To use the project, follow these steps:

Import the necessary classes and enums from the project files.
Create instances of the Sensor, Event, and UAV classes as required.
Define sensor details by generating Sensor objects with random sensor types and battery percentages.
Display the sensor details using the display_details() method.
Define event details by generating Event objects with random event types, time intervals, and event times.
Create instances of the UAV class by providing a name, start position, range limit, and battery percentage.
Assign sensors to the UAVs using the assign_sensors() method, passing the sensor details as an argument.
Calculate optimal paths for the UAVs using the find_optimal_path() method, passing the sensor details as an argument.
Display the UAV details and paths using the display_details() method.
Start the UAV navigation by calling the navigate() method.
Run events using threads by calling the run_events() function and passing the event details as an argument.
Example<a name="example"></a>
Here's an example demonstrating the usage of the project:

python
Copy code
Conclusion<a name="conclusion"></a>
Congratulations! You have successfully learned about the project and its components. The simulation of UAV navigation to events with battery constraints and assigned sensors can be a valuable tool in various applications. Feel free to explore and modify the code to suit your specific requirements.

If you have any further questions or need assistance, please don't hesitate to reach out. Happy coding!
