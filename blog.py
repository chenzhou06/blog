#! /usr/bin/env python3
import subprocess
import sys

PYTHON = "D:\\projects\\web\\blog\\venv\\Scripts\\python.exe"

MANAGER = "D:\\projects\\web\\blog\\manage.py"

if __name__ == "__main__":
    cmd = [PYTHON, MANAGER] + sys.argv[1:]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True, shell=True)
    print(p.stdout.read())
