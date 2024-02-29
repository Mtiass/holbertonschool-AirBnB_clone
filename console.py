#!/usr/bin/python3
"""
This module defines a program that contains the entry point of
the command interpreter.
"""
import cmd
from shlex import split as sp
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is a class that works as command interpreter.
    """
    prompt = "(hbnb) "
    class_mapping = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }

    def do_quit(self, arg):
        """
        This method exits the program.
        """
        return (True)

    def do_EOF(self, arg):
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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.class_mapping:
            print("** class doesn't exist **")
            return
        obj = self.class_mapping[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj_id = class_name + '.' + instance_id
        if obj_id not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[obj_id])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj_id = class_name + '.' + instance_id
        if obj_id not in storage.all():
            print("** no instance found **")
            return
        storage.all().pop(obj_id)
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.
        """
        args = arg.split()
        if not args:
            lists = [str(obj) for obj in storage.all().values()]
            print(lists)
            return
        class_name = args[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return
        lists = [str(obj) for obj in storage.all().values()]
        print(lists)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return
        args = sp(arg)
        class_name = args[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj_id = class_name + '.' + instance_id
        if obj_id not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = self.class_mapping[class_name]
        if attr_name == 'my_number':
            setattr(storage.all()[obj_id], attr_name, int(attr_value))
        else:
            setattr(storage.all()[obj_id], attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
