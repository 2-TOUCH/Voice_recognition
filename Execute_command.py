import command_function
def Execution(command_obj):
    command = command_obj.command
    details = command_obj.details  # This can be used for commands that require additional information

    print("Trying to run", command)
    if command == 'unknown':
        print("Unable to detect a real command")
        
    if command == 'mute_device_sound' or command == 'unmute_device_sound':
        command_function.mute_unmute_device_sound()

    if command == 'volume_up':
        command_function.increase_volume()

    if command == 'volume_down':
        command_function.decrease_volume()

    if command == 'open_google':
        command_function.open_google()

    if command == 'search_google':
        command_function.search_google(details)
    # Add more command handling as needed
