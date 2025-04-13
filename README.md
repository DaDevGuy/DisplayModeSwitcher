# Display Mode Switcher

A Python GUI application to seamlessly switch between display modes and monitor inputs, making it convenient to toggle between PC and gaming console setups (e.g., PS5) without manually adjusting display settings or inputs. This tool is especially useful for dual-purpose setups where a single monitor is shared between a PC and a gaming console.

## Features

- **Switch Display Modes**: Automatically toggle between `clone` and `extend` display modes using Windows' `DisplaySwitch.exe`.
- **Monitor Input Control**: Change the active input on the monitor (e.g., HDMI 1 for PS5) using [ClickMonitorDDC](https://clickmonitorddc.bplaced.net/).
- **Sleep Mode**: Put the PC into sleep mode when switching to the PS5.
- **PS5 Activity Monitoring**: Ensure smooth transitions by monitoring PS5 input activity.

## Requirements

1. **Windows Operating System**
   - Tested on Windows 10/11.
2. **Python Libraries**
   - `customtkinter`: For the modern GUI design.
   - Pre-installed modules: `os`, `subprocess`, `time`, `ctypes`.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/username/displaymodeswitcher.git
   cd displaymodeswitcher

## Usage

This application is designed to help users seamlessly switch between using their PC and a PS5 connected to the same monitor. Below are step-by-step instructions for each mode.

---

### Switching to PS5
1. Launch the application.
2. Click the **Switch to PS5** button.
3. The application will:
   - Change the display mode to "Clone," so the PC display is mirrored.
   - Put the PC into sleep mode.
   - Switch the monitor's input to the specified PS5 input.
4. You should now see your PS5 displayed on the monitor.

---

### Switching to PC
1. Click the **Switch to PC** button in the application.
2. The application will:
   - Change the display mode back to "Extend," restoring the PC's original setup.
3. The monitor will switch back to displaying your PC.

---

### Notes
- Ensure the `ClickMonitorDDC.exe` path is correctly set in the script for monitor input switching to work. Update the path as needed in the code.
- If the **Switch to PS5** or **Switch to PC** functionality is not working, ensure all dependencies (e.g., `DisplaySwitch.exe` and `ClickMonitorDDC.exe`) are installed and functional.
- Use the **Exit** button to close the application.

### Screenshot
![image](https://github.com/user-attachments/assets/2cd5a514-f411-47c8-9b4b-82d7d24afcb5)

### Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or create a pull request.



