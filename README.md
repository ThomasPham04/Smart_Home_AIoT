"# Gateway_Smart_Home" 
# AIoT Smart Home System with Yolo:Bit

## Overview
This project implements a smart home system using the **Yolo:Bit** microcontroller, integrating **AIoT** technologies to monitor and control home appliances. The system connects to **Adafruit IO** via a gateway for real-time data exchange and supports features like environmental monitoring, door access control, LED lighting, and fan speed adjustment. All data is displayed on an LCD for user-friendly interaction.

The project is designed to demonstrate the application of embedded systems, IoT protocols, and sensor integration in creating a scalable and secure smart home solution.

## Features
- **Environmental Monitoring**: Collects temperature, humidity, and light intensity data using DHT11 and LDR sensors.
- **Door Access Control**: Simulates door opening/closing with an RC servo motor, secured by password input via an IR remote.
- **LED Control**: Controls RGB LED for customizable lighting colors.
- **Fan Speed Adjustment**: Adjusts fan speed based on environmental conditions or user input.
- **Real-time Display**: Shows sensor data and system status on a 16x2 LCD.
- **IoT Integration**: Connects to Adafruit IO using MQTT for remote monitoring and control.

## Hardware Requirements
- **Yolo:Bit** microcontroller
- **DHT11** temperature and humidity sensor
- **LDR** (Light Dependent Resistor) for light intensity
- **RC Servo Motor** (e.g., SG90) for door simulation
- **RGB LED** for lighting
- **DC Motor** with driver (e.g., L298N) for fan simulation
- **16x2 LCD** with I2C module
- **IR Remote** and receiver for password input
- **Wi-Fi Module** (integrated in Yolo:Bit or external)
- Breadboard, jumper wires, and power supply

## Software Requirements
- **MicroPython**: Programming language for Yolo:Bit.
- **Adafruit IO Account**: For MQTT-based cloud connectivity.
- **OhStem App/Library**: For Yolo:Bit configuration and sensor integration.
- **Thonny IDE**: For coding and uploading firmware to Yolo:Bit.

## System Architecture
The system follows an **AIoT architecture**:
1. **Sensors** collect environmental data (temperature, humidity, light).
2. **Yolo:Bit** processes inputs and controls outputs (servo, LED, fan).
3. **Gateway** connects Yolo:Bit to Adafruit IO using MQTT for data publishing/subscribing.
4. **LCD** displays real-time sensor data and system status.
5. **IR Remote** enables secure password input for door access.

## Installation and Setup
1. **Hardware Setup**:
   - Connect sensors, servo, RGB LED, motor, and LCD to Yolo:Bit as per the pin configuration (refer to `pin_config.md` in the repo).
   - Ensure a stable power supply for all components.
2. **Software Setup**:
   - Install MicroPython firmware on Yolo:Bit using MicroPython IDE.
   - Clone this repository:
     ```bash
     git clone https://github.com/[your-username]/smart-home-yolobit.git
