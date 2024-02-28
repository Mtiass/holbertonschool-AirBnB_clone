#!/usr/bin/python3
"""
This module defines a program that contains the entry point of
the command interpreter.
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This is a class that works as command interpreter.
    """
    prompt = "(hbnb)"

    def _quit(self, arg):
        """
        This method exits the program.
        """
        return (True)

    def _EOF(self, arg):
        """
        This method exits the program.
        """
        return (True)

    def emptyline(self):
        """
        This method is for when an empty line + Enter is pressed
        to do nothing.
        """
        pass

    def _create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
