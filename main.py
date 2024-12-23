import sys


def main():

    valid_commands = ["echo", "pwd", "exit", "type"]

    def echo(command_array):
        for word in command_array[1:]:
            print(word, end=" ")
        print()  # To ensure a newline after echoing

    def type(command_array):
        if len(command_array) < 2:
            print("type: missing command name")
            return
        
        evaled_command = command_array[1]  # Get the second part of the command
        if evaled_command in valid_commands:
            print(f"{evaled_command} is a shell builtin")
        else:
            print(f"{evaled_command} not found")

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        command_array = command.split()
        
        if not command_array:  # Handle empty input
            continue
        
        if command_array[0] == "exit":
            sys.exit(0)
        elif command_array[0] == "echo":
            echo(command_array)
        elif command_array[0] == "type":
            type(command_array)
        else:
            print(command + ": command not found")


if __name__ == "__main__":
    main()
