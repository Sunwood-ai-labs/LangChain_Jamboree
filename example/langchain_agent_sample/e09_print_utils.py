from termcolor import colored

def print_progress(message):
    """Print a progress message in a stylish way."""
    print(colored(message, "green"))

def print_error(message):
    """Print an error message in a stylish way."""
    print(colored(message, "red"))

def print_success(message):
    """Print a success message in a stylish way."""
    print(colored(message, "blue"))

if __name__ == "__main__":
    print_progress("This is a progress message.")
    print_error("This is an error message.")
    print_success("This is a success message.")