Welcome to the **Build Your Own Shell** challenge! 🚀

I# PyShell: A Lightweight Python Shell 🐍💻

[![GitHub License](https://img.shields.io/github/license/yourusername/pyshell?color=blue)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

A modern implementation of a Unix-style shell in pure Python, featuring built-in commands and external program execution.

![PyShell Demo](demo.mp4) <!-- Replace with your actual video file/link -->

## Features ✨

**Built-in Commands:**
- 🏠 `cd`: Navigate directories (supports absolute paths, relative paths, and `~` home shortcut)
- 📢 `echo`: Display messages with argument parsing
- 📍 `pwd`: Print current working directory
- ℹ️ `type`: Identify command types (builtins vs executables)
- 🚪 `exit`: Terminate the shell session

**Advanced Capabilities:**
- 🛠️ External command execution through `subprocess`
- 🚦 Comprehensive error handling with POSIX-style messages
- 📂 PATH environment variable integration
- 🧹 Input sanitization and whitespace handling

## Installation ⚙️

```bash
# Clone the repository
git clone https://github.com/yourusername/pyshell.git

# Navigate to project directory
cd pyshell

# Run the shell (Python 3.6+ required)
python3 shell.py
```
## Usage Examples 🚀
Basic Navigation:
```bash
$ cd ~/Documents  # Home directory shortcut
$ pwd
/home/user/Documents

$ cd ../Downloads # Relative path
$ pwd
/home/user/Downloads

$ echo "Hello from PyShell!"
Hello from PyShell!

$ type cd
cd is a shell builtin

$ type ls
ls is /usr/bin/ls

$ date  # External command
Wed Aug 23 14:30:00 UTC 2023
```
