#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit console"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()