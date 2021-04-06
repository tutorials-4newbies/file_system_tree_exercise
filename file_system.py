from typing import List, Union, Optional


# How can we represent the file system?
class FileSystemNode:
    def __init__(self, name: str, parent=None):
        self.parent = parent
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class IllegalCommand(Exception):
    pass


class FileSystem:
    LEGAL_COMMANDS = ["echo"]

    def __init__(self):
        self.file_system_tree = FileSystemNode(name='/')
        self.current = self.file_system_tree

    def dispatch_command(self, cmd: str, args: List[str]) -> Optional[str]:
        # add a check if in legal commands else throw an exception
        func = getattr(self, cmd)
        return func(args)

    def evaluate(self, parsed_user_input: List[str]) -> str:
        """
        The main evaluation in the loop
        :param parsed_user_input:
        :return: a string with a result
        :rtype: str
        """
        # currently hard coded "string join"
        # extract the command (fhe first token in parsed_user_input)
        # Implement pwd
        cmd = parsed_user_input.pop(0)
        args = parsed_user_input
        return self.dispatch_command(cmd, args)

    def echo(self, args: List[str]):
        print(" ".join(args))

    def pwd(self, args: List[str]):
        pwd = self.current.name
        print(pwd)
        return pwd


def reader(user_input: str) -> List[str]:
    """

    :param user_input:str the string of input from the user
    :return: list of strings
    todo: how should we break it to a list programmatically and not hard coded like now
    """
    return user_input.split()


def repl():
    """
    REPL stands for READ EVALUATE PRINT LOOP
    :return:
    """
    file_system = FileSystem()
    while True:
        try:
            user_input = input('>? ')
            if not user_input.strip():
                continue
            parsed_user_input = reader(user_input)
            res = file_system.evaluate(parsed_user_input)
            if res:
                print(res)
        except (EOFError, KeyboardInterrupt):
            break
        except Exception as err:
            print(f'Error: {err}')
    print('Bayush')


if __name__ == "__main__":
    print("Starting")
    repl()
