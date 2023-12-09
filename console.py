#!/usr/bin/python3
"""Module contains the entry point of the command interpreter"""

from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """a class to the command interpreter"""

    prompt = '(hbnb) '
    __cls = ["BaseModel"]

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
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.__cls:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{line[0]}()")
            print(new_instance.id)
            storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.__cls:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif f"{line[0]}.{line[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{line[0]}.{line[1]}"])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
