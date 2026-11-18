# Steron Labs – Autonomous Mobile Robotics Platform

A simulation-first autonomous mobile robotics R&D project built with ROS 2 Humble and Gazebo Fortress.

The project aims to develop a modular differential-drive mobile robot platform, starting with simulation, closed-loop motion control, and progressively expanding toward autonomous navigation and real-world deployment.

## Current Features

- Custom differential-drive robot model developed using URDF/Xacro.
- Gazebo Fortress simulation environment.
- ROS 2 and Gazebo communication through `ros_gz_bridge`.
- Odometry monitoring using a custom ROS 2 Python node.
- Odometry-based closed-loop proportional (P) distance controller.
- Configurable robot simulation launched through a single ROS 2 launch file.
- Tested 2-meter forward movement with a 5 cm position tolerance.

## Technology Stack

| Category | Technologies |
|---|---|
| Operating System | Ubuntu 22.04 LTS |
| Robotics Middleware | ROS 2 Humble |
| Simulation | Gazebo Fortress |
| Programming | Python |
| Robot Description | URDF, Xacro |
| Communication | ros_gz_bridge |
| Version Control | Git, GitHub |

## Additional Hardware Experience

Previous hands-on experience with physical mobile robot development,
including C++ programming and microcontroller-based motor control.

## Project Architecture

The repository is organized into three ROS 2 packages:

- `steron_description` – Robot model, URDF/Xacro descriptions, and visualization.
- `steron_control` – Odometry monitoring and motion control nodes.
- `steron_bringup` – Simulation launch configuration and system integration.

## Project Structure

```text
steron-autonomous-robot/
├── ros2_ws/
│   └── src/
│       ├── steron_bringup/
│       ├── steron_control/
│       └── steron_description/
├── simulation/
│   ├── test_assets/
│   └── worlds/
└── README.md
```

## Development Roadmap

- [x] Robot modeling with URDF/Xacro.
- [x] Gazebo simulation integration.
- [x] ROS 2-Gazebo communication bridges.
- [x] Odometry monitoring.
- [x] Closed-loop proportional distance control.
- [ ] TF2 integration.
- [ ] 2D LiDAR integration.
- [ ] SLAM and autonomous mapping.
- [ ] Nav2 navigation stack.
- [ ] Physical robot integration using Raspberry Pi and ESP32.

## Project Status

**Active Development – Simulation Phase**

The current focus is improving motion control, system architecture, and simulation reliability before transitioning to autonomous navigation and physical hardware.

---

Developed as part of the Steron Labs robotics R&D initiative.
