from nltk.tokenize import word_tokenize
import re
from command_class import Command

def parse_command(command):
    commands = {
        'mute_device_sound': r'\bmute\b|\bsound off\b|\bsilent\b|\bquiet\b|\bturn on music\b',
        'unmute_device_sound': r'\bsound on\b|\bunmute\b|\bbring sound back\b|\bturn off music\b',
        'volume_up': r'\bturn up\b|\bincrease volume\b|\blouder\b|\bvolume up\b',
        'volume_down': r'\bturn down\b|\bdecrease volume\b|\bquieter\b|\bvolume down\b',
        'quit_application': r'\bquit\b|\bexit\b|\bclose\b|\bshutdown\b', 
        'open_google': r'\bopen\b.*(\bgoogle\b|\btab\b)',
        'search_google':r'\bsearch\b|\blook up\b|'
    }

    conjunctions = ['then', 'and', 'next', 'than']
    split_commands = re.split('|'.join(conjunctions), command)
    split_commands = [cmd.strip() for cmd in split_commands if cmd.strip()]

    recognized_commands = []
    for cmd in split_commands:
        matched_command = None
        command_details = None
        for command_name, pattern in commands.items():
            match = re.search(pattern, cmd.lower())
            if match:
                matched_command = command_name
                # Extracting details: the part of cmd after the matched command
                command_details = cmd[match.end():].strip()
                break
        else:
            matched_command = 'unknown'

        
        recognized_commands.append(Command('general', matched_command, command_details))

    print(recognized_commands)
    return recognized_commands
