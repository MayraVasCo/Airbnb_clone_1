import cmd

class HBNBCommand(cmd.Cmd):
    """
    Clase que define un intérprete de comandos para una aplicación hbnb.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Salir del programa.
        """
        return True

    def do_EOF(self, arg):
        """
        Salir del programa al llegar al final del archivo (Ctrl+D).
        """
        return True

    def do_help(self, arg):
        """
        Mostrar la ayuda.
        """
        # Personalizar la implementación del comando help si es necesario
        super().do_help(arg)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
