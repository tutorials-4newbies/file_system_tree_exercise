from typing import List


def evaluate(parsed_user_input: List[str]) -> str:
    """
    The main evaluation in the loop
    :param parsed_user_input:
    :return: a string with a result
    :rtype: str
    """
    # currently hard coded "string join"
    return '-'.join(parsed_user_input)


def reader(user_input: str) -> List[str]:
    """

    :param user_input:str the string of input from the user
    :return: list of strings
    todo: how should we break it to a list programmatically and not hard coded like now
    """
    return [user_input]


def repl():
    """
    REPL stands for READ EVALUATE PRINT LOOP
    :return:
    """
    while True:
        try:
            user_input = input('>? ')
            if not user_input.strip():
                continue
            parsed_user_input = reader(user_input)
            res = evaluate(parsed_user_input)
            print(res)
        except (EOFError, KeyboardInterrupt):
            break
        except Exception as err:
            print(f'Error: {err}')
    print('Bayush')


if __name__ == "__main__":
    print("Starting")
    repl()
