from Detection.wake_word import detect_wake_word_and_command
from Execute_command import Execution
from Detection.NLP import parse_command
import sys
from collections import deque
from command_class import Command

if __name__ == "__main__":
    while True:
        input = detect_wake_word_and_command()
        if input != "no_command":
            recognized_commands = parse_command(input)  # This now returns a list of Command objects
            print(f"Commands recognized: {[cmd.command for cmd in recognized_commands]}")

            commands_queue = deque(recognized_commands)
            while commands_queue:
                command_obj = commands_queue.popleft()
                if command_obj.command == 'quit_application':
                    print("Closing app...")
                    sys.exit(0)
                else:
                    Execution(command_obj)
