from argparse import ArgumentParser
from os import system

import os

class Requirements: 
    __VERSION_REQUIREMENTS_CLI = "1.0.0"
    __DEFAULT_REQUIREMENTS_PATH = ["./requirements.prod.txt", "./requirements.dev.txt", "./requirements.txt"]

    def __init__(self) -> None:
        self.__run()

    def __str__(self) -> str:
        return f"Requirements Installer - {self.__VERSION_REQUIREMENTS_CLI}"

    def __is_path_reqquirements__(self, requirement_path: str) -> bool:
        return os.path.isfile(requirement_path)

    def __install_dependencies(self, python_interpreter: str = "venv", file_name="requirements", env="d") -> bool: 
        if file_name == "requirements":
            for requirement_path in self.__DEFAULT_REQUIREMENTS_PATH:
                if self.__is_path_reqquirements__(requirement_path=requirement_path):
                    file_name = requirement_path

        if ((env == "p") and (".dev" in file_name)) or ((env == "d") and (".prod" in file_name)):
            enviroment = "dev env" if env == "d" else "prod env"
            current_env = "dev env" if "prod" in enviroment else "prod env"
            print(f"ERROR: You passed {enviroment} and the env on project is {current_env}")

        if python_interpreter == "venv":
            try:
                print("Installing requirements...")
                system(f"pip install -r {file_name}")
                
                return True

            except Exception as e:
                print(f"ERROR: {e}")
                return False

        if python_interpreter != "venv":
            aux = python_interpreter
            print("Configuring the pip...")
            
            if os.path.isfile(aux.replace("python.exe", "Scripts\\pip.exe")):
                python_interpreter = python_interpreter.replace("python.exe", "Scripts\\pip.exe")
            else:
                python_interpreter = python_interpreter.replace("\\python.exe", "\\pip.exe")

            try:
                print("Installing requirements...")
                system(f"{python_interpreter} install -r {file_name}")
                
                return True

            except Exception as e:
                print(f"ERROR: {e}")
                return False

    def __run(self):
        self.parser = ArgumentParser(
            prog="Requirements Installer",
            description="Automação para instalação dos requirements",
            epilog="Desenvolvido por: Pedro Augusto Barbosa Aparecido",
            usage="%(prog)s [OPTIONS...] [VALUES...]"

        )

        self.parser.version = self.__str__()
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
                            args.interpreter = "venv"
                            print("\n\nInvalid Interpreter")
                            print(e)
                    else:
                        args.interpreter = "venv"
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
