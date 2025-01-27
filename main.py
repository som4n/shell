import subprocess
import sys
import os

def main():
    PATH = os.environ.get('PATH')
    valid_commands = ["echo", "pwd", "exit", "type"]

    def echo(command_array):
        for word in command_array[1:]:
            print(word, end=" ")
        print()  # To ensure a newline after echoing

    def type(command_array):
        if len(command_array) < 2:
            print("type: missing command name")
            return
        
        cmd = command_array[1]  # Get the second part of the command
        cmd_path= None
        paths= PATH.split(":")
        for i in paths:
            if os.path.isfile(f"{i}/{cmd}"):
                cmd_path=f"{i}/{cmd}"
                
        if cmd in valid_commands:
            print(f"{cmd} is a shell builtin")
        elif cmd_path:
            sys.stdout.write(f"{cmd} is {cmd_path}\n")
        else:
            print(f"{cmd} not found")
    def execute_command(command_array):
        cmd = command_array[0]
        cmd_path = None
        paths = PATH.split(":")
        
        # Search for the executable in PATH
        for path in paths:
            potential_path = f"{path}/{cmd}"
            if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
                cmd_path = potential_path
                break
        
        if cmd_path:
            try:
                # Execute the command with all arguments
                process = subprocess.run(command_array, capture_output=True, text=True)
                # Print the output exactly as received
                sys.stdout.write(process.stdout)
                sys.stdout.flush()
                return True
            except Exception as e:
                sys.stderr.write(f"Error executing {cmd}: {str(e)}\n")
                sys.stderr.flush()
                return False
        return False

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        command_array = command.split()
        
        if not command_array:  # Handle empty input
            continue
        
        match command_array[0]:
            case "exit":
                sys.exit(0)
            case "echo":
                echo(command_array)
            case "type":
                type(command_array)
            case _:  # Default case
                if not execute_command(command_array):
                    sys.stdout.write(f"{command}: command not found\n")
                    sys.stdout.flush()
            
if __name__ == "__main__":
    main()
