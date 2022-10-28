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

    def to_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.className[arg]()
            HBNBCommand.className[arg].save(obj)
            print(obj, id)

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
