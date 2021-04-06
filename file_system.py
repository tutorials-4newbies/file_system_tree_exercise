import logging
from typing import List, Union, Optional

logging.basicConfig()
logger = logging.getLogger(__name__)


# How can we represent the file system?

class FileSystemNode:
    def __init__(self, name: str, parent=None):
        self.parent = parent
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_path(self):
        path = [self.name]
        if self.parent:
            return path + self.parent.get_path()
        return path


class IllegalCommand(Exception):
    pass


class NoSuchFolder(Exception):
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

        path = self.current.get_path()
        path.reverse()
        pwd = '/'.join(path)
        print(pwd)
        return pwd

    def ls(self, args: List[str]):
        children = self.current.children
        for child in children:
            print(f"* {child.name}")

    def mkdir(self, args: List[str]):
        folder = FileSystemNode(parent=self.current, name=args[0])
        self.current.add_child(folder)

    def cd(self, args: List[str]):
        folder_name = args[0]
        for child in self.current.children:
            if folder_name == child.name:
                self.current = child
                return
        if folder_name == '..':
            if self.current.parent:
                self.current = self.current.parent
                return

        raise NoSuchFolder()


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
            logger.exception(msg=err)
            print(f'Error: {err.__class__.__name__}')
    print('Bayush')


if __name__ == "__main__":
    print("Starting")
    repl()
