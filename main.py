import subprocess
import sys
import os

def main():
    PATH = os.environ.get('PATH')
    valid_commands = ["echo", "pwd", "exit", "type" , "pwd"]

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
    
    def cd(command_array):
        if len(command_array) < 2:
            # If no argument is provided, change to the home directory
            new_dir = os.path.expanduser("~")
        else:
            target_dir = command_array[1]
            # Resolve relative paths to absolute paths
            if target_dir.startswith(("./", "../")) or not target_dir.startswith("/"):
                new_dir = os.path.abspath(os.path.join(os.getcwd(), target_dir))
            else:
                new_dir = target_dir  # Absolute path
        
        try:
            # Attempt to change the directory
            os.chdir(new_dir)
        except FileNotFoundError:
            sys.stderr.write(f"cd: {new_dir}: No such file or directory\n")
            sys.stderr.flush()
        except NotADirectoryError:
            sys.stderr.write(f"cd: {new_dir}: Not a directory\n")
            sys.stderr.flush()
        except PermissionError:
            sys.stderr.write(f"cd: {new_dir}: Permission denied\n")
            sys.stderr.flush()
        except Exception as e:
            sys.stderr.write(f"cd: {str(e)}\n")
            sys.stderr.flush()


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
            case "pwd":
                print(f"{os.getcwd()}")
            case "cd":
                cd(command_array)
            case _:  # Default case
                if not execute_command(command_array):
                    sys.stdout.write(f"{command}: command not found\n")
                    sys.stdout.flush()
            
if __name__ == "__main__":
    main()
