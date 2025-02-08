# Build Your Own Shell

Welcome to the **Build Your Own Shell** challenge! 🚀

In this project, WE'll implement a custom POSIX-compliant shell capable of interpreting shell commands, running external programs, and handling built-in commands like `cd`, `pwd`, `echo`, and more. This project is a great way to deepen your understanding of command-line interfaces, shell command parsing, and process management.

---
## Features

- **Execute External Commands**: Run external programs directly from your shell.
- **Builtin Commands**: Includes support for commands like:
  - `cd` (Change Directory)
  - `pwd` (Print Working Directory)
  - `echo` (Print Messages)
  - `exit` (Exit the Shell)
- **REPL (Read-Eval-Print Loop)**: A continuous loop that takes input, processes it, and displays output.
- **POSIX Compliance**: Aims to support POSIX standards for maximum compatibility.
- **Error Handling**: Handles invalid commands and provides meaningful error messages.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.7+
- A POSIX-compliant system (Linux, macOS, or WSL on Windows recommended)

---
## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/build-your-own-shell.git
   cd build-your-own-shell
   ```

2. Run the shell:

   ```bash
   python main.py
   ```

3. Start executing commands!

---

## Usage

### Example Commands

- Run an external program:
  ```bash
  ls -la
  ```

- Change directory:
  ```bash
  cd /path/to/directory
  ```

- Print the current working directory:
  ```bash
  pwd
  ```

- Display a message:
  ```bash
  echo "Hello, Shell!"
  ```

- Exit the shell:
  ```bash
  exit
  ```

---

## Project Structure

```
├── main.py              # Entry point for the shell
├── shell/               # Contains core shell implementation
│   ├── parser.py        # Command parsing logic
│   ├── executor.py      # Command execution logic
│   └── builtins.py      # Built-in command implementations
└── README.md            # Project documentation
```

---

## Development

### Installing Dependencies

This project uses Python's standard library, so no external dependencies are required. However, you can create a virtual environment for development:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Running Tests

To test your shell, run:

```bash
python -m unittest discover tests
```

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, feel free to:

- Open an issue
- Submit a pull request

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

This project is inspired by the need to understand the inner workings of shells and command-line interfaces. Thank you to all contributors and resources that made this possible!

---

## Author

[som4n](https://github.com/som4n)  
Feel free to reach out for feedback, questions, or collaborations!
