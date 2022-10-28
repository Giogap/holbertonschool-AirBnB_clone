#!/usr/bin/python3
"""
console that contains the entry point of the command interpreter
"""
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """ clas HBNB cmd """
    prompt = '(hbnb) '
    filen = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    cmd.emptyline()
    """ empty line """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
