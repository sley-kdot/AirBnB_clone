#!/usr/bin/python3
"""Module contains the entry point of the command interpreter"""

from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """a class to the command interpreter"""
    
    prompt = '(hbnb) '
    __classes = ["BaseModel"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """Handles emplyline"""
        pass

    def do_create(self, line):
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{line[0]}()")
            print(new_instance.id)

    def do_show(self, line):
        line = line.split()
        print(line)
        print(len(line))
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
