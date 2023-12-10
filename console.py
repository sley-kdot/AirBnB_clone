#!/usr/bin/python3
"""Module contains the entry point of the command interpreter"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """a class to the command interpreter"""

    prompt = '(hbnb) '
    __cls = [
            "BaseModel", "User", "State",
            "City", "Amenity", "Place", "Review"
            ]

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

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
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
            for key in storage.all():
                if key == f"{line[0]}.{line[1]}":
                    del storage.all()[key]
                    break
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        line = line.split()
        if len(line) == 0:
            new_list = [str(value) for value in storage.all().values()]
            print(new_list)
        elif line[0] not in self.__cls:
            print("** class doesn't exist **")
        else:
            new_list = []
            for key, value in storage.all().items():
                cls_name, cls_id = key.split(".")
                if line[0] != cls_name:
                    continue
                new_list.append(str(value))
            print(new_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
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
        elif len(line) < 3:
            print("** attribute name missing **")
        elif len(line) < 4:
            print("** value missing **")
        else:
            obj_cls = line[0]
            obj_id = line[1]
            obj_key = f"{obj_cls}.{obj_id}"
            obj = storage.all()[obj_key]
            
            attr_name = line[2]
            attr_val = line[3]
            if attr_val[0] == '"':
                attr_val = attr_val[1:-1]
            
            if hasattr(obj, attr_name):
                value_type = type(getattr(obj, attr_name))
                if value_type in [str, int, float]:
                    attr_val = value_type(attr_val)
                    setattr(obj, attr_name, attr_val)
            else:
                setattr(obj, attr_name, attr_val)
            storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
