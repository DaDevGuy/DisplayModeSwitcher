import os
import subprocess
import time
import ctypes
import customtkinter as ctk

def switch_display_mode(mode="clone"):
    mode_options = {
        "clone": "/clone",
        "extend": "/extend",
        "internal": "/internal",
        "external": "/external"
    }
    if mode not in mode_options:
        print(f"Invalid mode: {mode}. Available modes: {list(mode_options.keys())}")
        return
    subprocess.run(["C:\\Windows\\System32\\DisplaySwitch.exe", mode_options[mode]])

def switch_monitor_input(input_number):
    clickmonitor_ddc_path = "C:\\Path\\To\\ClickMonitorDDC.exe"  
    try:
        subprocess.run([clickmonitor_ddc_path, f"input:{input_number}"], check=True)
    except FileNotFoundError:
        print("ClickMonitorDDC not found. Ensure the path is correct")

def is_ps5_active(input_number):
    clickmonitor_ddc_path = "C:\\Path\\To\\ClickMonitorDDC.exe"  
    try:
        result = subprocess.check_output([clickmonitor_ddc_path, "/get"], text=True)
        active_input_line = [line for line in result.splitlines() if "Input" in line]
        if active_input_line and str(input_number) in active_input_line[0]:
            return True
    except Exception as e:
        print(f"Error checking input status: {e}")
    return False

def put_pc_to_sleep():
    ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)

def pc_to_ps5(ps5_input):
    print("Switching to duplicate display mode")
    switch_display_mode("clone")
    time.sleep(2)  
    print("Putting PC to sleep")
    put_pc_to_sleep()
    print("PC is now in sleep mode")
    print("Switching monitor input to PS5")
    switch_monitor_input(ps5_input)
    print("PS5 mode enabled.")

def ps5_to_pc():
    print("Switching back to extended display mode")
    switch_display_mode("extend")
    print("PC is back to extended mode.")

def on_switch_to_ps5():
    try:
        ps5_input = int(ps5_input_entry.get())
        pc_to_ps5(ps5_input)
    except ValueError:
        print("Please enter a valid input number")

def on_switch_to_pc():
    ps5_to_pc()

app = ctk.CTk()
app.title("Display Mode Switcher")
app.geometry("400x300")
app.resizable(False, False)

frame = ctk.CTkFrame(app)
frame.place(relx=0.5, rely=0.5, anchor="center")




switch_ps5_button = ctk.CTkButton(frame, text="Switch to PS5", command=on_switch_to_ps5)
switch_ps5_button.pack(pady=10, padx=20)

switch_pc_button = ctk.CTkButton(frame, text="Switch to PC", command=on_switch_to_pc)
switch_pc_button.pack(pady=10, padx=20)

exit_button = ctk.CTkButton(frame, text="Exit", command=app.destroy)
exit_button.pack(pady=20, padx=20)

app.mainloop()
