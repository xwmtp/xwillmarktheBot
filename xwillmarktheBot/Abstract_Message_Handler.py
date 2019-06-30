from xwillmarktheBot.Utils import *

class Message_handler():
    """Abstract class defining a general message handler.
       Takes a 'connection' object which should have a 'send' method to send messages."""

    def __init__(self):
        # commands in the class
        self.commands = {}
        # triggers in the class (words anywhere in message that may trigger the bot, like blue tunic)
        self.triggers = {}

    def handle_message(self, msg, sender):
        """Abstract method. Each message handler has to implement a way to handle incoming messages."""
        raise NotImplementedError('Subclasses must override handle_message()!')


    def get_commands(self):
        """
        Get all the commands of this class, including aliases.
        Each message handler has to define commands, otherwise an error will be raised.
        """
        if self.commands == {}:
            raise NotImplementedError('Subclasses must have self.commands attribute.')
        return flatten(self.commands.values())

    def get_triggers(self):
        """Get all the trigger of this class, including aliases. Won't throw error if no triggers present."""
        return flatten(self.triggers.values())