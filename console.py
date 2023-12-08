#!/usr/bin/python3
"""Module contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """a class to the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """Handles emplyline"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
