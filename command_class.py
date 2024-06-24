class Command:
    def __init__(self, command_class, command, details=None):
        self.command_class = command_class  # Type or category of the command
        self.command = command  # Specific command
        self.details = details  # Additional information or metadata

    def __repr__(self):
        return f"Command({self.command_class}, {self.command}, {self.details})"
