import os
import keyboard
import shutil
exit = False
conf_to_open = ''
try:
    open("C:\\skryptTeams\\current_config.txt")
    conf_to_open = "C:\\skryptTeams\\current_config.txt"
except:
    path = input("Enter path to config (ex. C:\\Users\\Downloads\\config.txt): ")
    conf_to_open = path
    shutil.copy(path, "C:\\skryptTeams\\current_config.txt")

with open(conf_to_open, 'r') as f:
    path_to_shortcut = f.readline().strip()
    path_to_shortcut = path_to_shortcut[19:]
    k_mute = f.readline().strip()
    k_mute = k_mute[15:]
    k_exit = f.readline().strip()
    k_exit = k_exit[23:]
    print(path_to_shortcut, k_mute, k_exit)

command = 'start ' + path_to_shortcut
os.path.dirname(os.path.abspath(__file__))
while exit is False:
    if(keyboard.is_pressed(k_mute)):
        print("Toggled mute/unmute")
        os.system(command)
    if(keyboard.is_pressed(k_exit)):
        exit = True
close("C:\\skryptTeams\\current_config.txt")
