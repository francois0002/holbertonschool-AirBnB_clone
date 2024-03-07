#!/usr/bin/python3
"Module of the class HBNBCommand"


import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models import classes
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit console"""
        print('')
        return True

    def emptyline(self):
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arguments_list = arg.split()

        if len(arguments_list) == 0:
            print("** class name missing **")
            return

        class_name = arguments_list[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(arguments_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments_list[1]

        key = "{}.{}".format(class_name, instance_id)

        instances_json = storage.all()

        if key not in instances_json:
            print("** no instance found **")
            return

        del instances_json[key]
        storage.save()
        return

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        file_storage_objs = storage.all()
        if len(arg) == 0:
            print([str(instance) for instance in file_storage_objs.values()])

        else:
            argument_list = arg.split()
            class_name = argument_list[0]
            if class_name not in classes:
                print("** class doesn't exist **")
                return

            list_all_instances = []
            for instance in file_storage_objs.values():
                if instance.__class__.__name__ == class_name:
                    list_all_instances.append(str(instance))
            print(list_all_instances)

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        token = arg.split()
        try:
            """create a new instance of a class based on the argument arg"""
            new_instance = eval(token[0])()
            """save in a Json File"""
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        """divise arg in keyword list"""
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            """Retrieve all objects from the storage with all()"""
            file_storage_objs = storage.all()
            for key, value in file_storage_objs.items():
                if arg[1] in key and arg[0] in key:
                    print(value)
        except KeyError:
            print("** no instance found **")

    def do_update(self, arg):
        """Update the value of a instance of a class"""
        argument_list = arg.split()

        if len(argument_list) == 0:
            print("** class name missing **")
            return

        class_name = argument_list[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(argument_list) < 2:
            print("** instance id missing **")
            return

        if len(argument_list) < 3:
            print("** attribute name missing **")
            return

        if len(argument_list) < 4:
            print("** value missing **")
            return

        id_instance = argument_list[1]
        key = "{}.{}".format(class_name, id_instance)
        list_instances = storage.all()

        if key not in list_instances:
            print("** no instance found **")
            return

        attribute_name = argument_list[2]
        attribute_value = argument_list[3]
        instance = list_instances[key]

        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
