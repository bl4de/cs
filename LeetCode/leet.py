#!/usr/bin/env python
import sys
import re
import shutil

if len(sys.argv) < 2:
    exit("[-] Uh oh, problem name is missing")
problem = sys.argv[1]

lang = 'py' if len(sys.argv) == 2 else sys.argv[2]

problem_filename = re.sub(
    r"[^a-z0-9\s]", "", problem.lower()).replace(" ", "_") + "." + lang
shutil.copy(f"./template.{lang}", problem_filename)

print(f"[+] {problem_filename} created!")
