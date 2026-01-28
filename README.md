# Sysmon

Sysmon is a lightweight Python console application designed to monitor and display real-time hardware and system information. It provides an intuitive terminal-based interface for tracking CPU usage, memory consumption, disk space, network activity, and other critical system metrics without relying on complex external dependencies.

The tool is intended to be simple to use, cross-platform compatible, and suitable both for system administration tasks and as a learning project demonstrating Python system monitoring and terminal UI design.

---

## Overview

Sysmon provides real-time system monitoring using the following workflow:

1. Initializes system monitoring modules
2. Gathers hardware and performance metrics from the operating system
3. Formats data for clear terminal display
4. Updates information at regular intervals
5. Presents statistics in an organized, easy-to-read layout
6. Allows users to monitor system health at a glance

The application runs entirely in the console, making it ideal for remote server monitoring, headless systems, or users who prefer terminal-based tools.

---

## Features

- Real-time CPU usage monitoring
- Memory (RAM) consumption tracking
- Disk space utilization
- Network activity monitoring
- Cross-platform compatibility (Windows, Linux, macOS)
- Terminal-based user interface
- Low resource footprint
- Continuous data refresh
- No complex configuration required
- Modular architecture for easy extension

---

## Installation

### Prerequisites

- Python 3.7 or newer
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/K1kk0MAN/Sysmon.git
cd Sysmon
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

The main dependencies include:
- `psutil` - Cross-platform library for system and process utilities
- Additional terminal UI libraries (if applicable)

---

## Usage

### Running the Application

To start the system monitor, simply run:

```bash
python main.py
```

The application will launch in your terminal and begin displaying real-time system information.

### Basic Controls

- The display updates automatically at regular intervals
- Press `Ctrl+C` to exit the application gracefully

---

## Project Structure

The repository is organized into modular components for maintainability:

```
Sysmon/
├── main.py           # Entry point and application orchestration
├── monitor.py        # Core monitoring logic and data collection
├── ui.py             # Terminal user interface rendering
├── utils.py          # Helper functions and utilities
├── requirements.txt  # Python dependencies
├── main.spec         # PyInstaller specification (for building executables)
└── README.md         # This file
```

---

## Implementation Details

### System Monitoring

The application uses the `psutil` library to gather system metrics in a cross-platform manner. This includes:

- **CPU**: Percentage utilization per core and overall
- **Memory**: Total, used, available, and percentage
- **Disk**: Usage statistics for mounted drives
- **Network**: Real-time upload and download speeds

### User Interface

The terminal interface is designed for clarity and readability:

- Uses formatted text and box-drawing characters for structure
- Updates display periodically without flickering
- Organizes information into logical sections
- Handles different terminal sizes gracefully

### Modular Architecture

The codebase is split into focused modules:

- `monitor.py` - Handles all system data collection
- `ui.py` - Manages terminal rendering and display
- `utils.py` - Provides utility functions for formatting and calculations
- `main.py` - Coordinates the application flow

---

## Building Standalone Executables

The project includes a PyInstaller specification file (`main.spec`) for creating standalone executables.

### Build Process

To create an executable:

```bash
pip install pyinstaller
pyinstaller main.spec
```

The compiled executable will be available in the `dist/` directory.

### Distribution

Standalone executables allow the application to run without requiring Python installation:

- **Windows**: `dist/main.exe`
- **Linux/macOS**: `dist/main` (Unstable)

---

## Configuration

Sysmon is designed to work out of the box with sensible defaults. Advanced users can modify behavior by editing the relevant module files:

- Adjust refresh rate in `main.py`
- Customize display format in `ui.py`
- Add new metrics in `monitor.py`

---

## Cross-Platform Compatibility

Sysmon is designed to work seamlessly across operating systems: (Although it may be unstable outside Windows)

- **Windows**: Full support for all metrics
- **Linux**: Complete functionality using system calls
- **macOS**: Compatible with macOS-specific system interfaces

The `psutil` library abstracts away platform differences, ensuring consistent behavior.

---

## Performance Considerations

Sysmon is designed to have minimal impact on system resources:

- Efficient polling intervals to reduce CPU overhead
- Lightweight terminal rendering
- Optimized data collection methods
- Small memory footprint

---

## Future Enhancements

Potential improvements and features planned for future releases:

- Process-level monitoring (top processes by CPU/memory)
- Historical data visualization with graphs
- Alert thresholds for critical metrics
- Configuration file support
- Temperature monitoring for CPU/GPU
- Export metrics to log files
- Support for monitoring remote systems

---

## Contributing

Contributions are welcome! If you'd like to improve Sysmon:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---
