from argparse import ArgumentParser
from os import system

import os

class Requirements: 
    VERSION_REQUIREMENTS_CLI = "1.0.0"

    def __init__(self) -> None:
        self.__run()

    def __str__(self) -> str:
        return f"Requirements Instance Object {self.VERSION_REQUIREMENTS_CLI}"

    def __install_dependencies(self, python_interpreter="venv", file_name="requirements", env="d") -> bool: 
        return True

    def __run(self):
        self.parser = ArgumentParser(
            prog="Requirements Installer",
            description="Automação para instalação dos requirements",
            epilog="Desenvolvido por: Pedro Augusto Barbosa Aparecido",
            usage="%(prog)s [options]"

        )

        self.parser.version = self.VERSION_REQUIREMENTS_CLI
        self.parser.add_argument("-v", "--version", help="Show version of Requirements Installer.", action="version")
        self.parser.add_argument("-d", "--dev", help="Install dev dependencies on files XXXX.prod.txt.", action="store_true", default=False, required=False)
        self.parser.add_argument("-p", "--prod", help="Install prod dependencies on files XXXX.dev.txt.", action="store_true", default=False, required=False)
        self.parser.add_argument("-f", "--file", help="Especify the requirements filename or file path, default is 'requirements.[dev|prod].txt' on '.' of project.", action="store", type=str, default=".", required=False)
        self.parser.add_argument("-i", "--interpreter", help="Especify interpreter path if you don't use virtual enviroment, default is your venv.", action="store", type=str, default="venv", required=False)

        args = self.parser.parse_args()

        if args:
            try:
                if not args.dev and not args.prod:
                    print("ERROR: Especify your enviroment please!!!\nOPTIONS: '-d|--dev', '-p|--prod'")

                if args.interpreter != "venv":
                    if os.path.isfile(args.interpreter):
                        try:
                            print("Testing interpreter")
                            print("-------------------")
                            system(f"{args.interpreter} -V")
                            print("-------------------")
                            print("\n\nValid Interpreter")
                        except Exception as e:
                            print("\n\nInvalid Interpreter")
                            print(e)
                    else:
                        print("Invalid Interpreter!! System using your venv or global python")

                if args.prod:
                    if args.file == ".":
                        if self.__install_dependencies(python_interpreter=args.interpreter, env="p"):
                            print("Prod dependencies has been installed")
                    elif os.path.isfile(args.file):
                        if self.__install_dependencies(python_interpreter=args.interpreter, file_name=args.file, env="p"):
                            print("Prod dependencies has been installed")
                    else:
                        print("ERROR: No such file or directory!!")
                        

                elif args.dev:
                    if args.file == ".":
                        if self.__install_dependencies(python_interpreter=args.interpreter):
                            print("Dev dependencies has been installed")
                    elif os.path.isfile(args.file):
                        if self.__install_dependencies(python_interpreter=args.interpreter, file_name=args.file, env="d"):
                            print("Dev dependencies has been installed")
                    else:
                        print("ERROR: No such file or directory!!")

            except:
                self.parser.print_help()
                exit(1)
