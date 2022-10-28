#!/usr/bin/python3
"""
console that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ clas HBNB cmd """
    prompt = '(hbnb) '
    filen = None

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves JSON file"""
        if not arg:
            print('** class name missing **')
        else:
            try:
                new_obj = eval(arg)()
                new_obj.save()
                print(new_obj.id)
            except (NameError, SyntaxError):
                print("** class doesn't exist **")
                pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
