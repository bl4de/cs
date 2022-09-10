#!/usr/bin/env python
import sys
import re
import shutil

problem = sys.argv[1]

problem_filename = re.sub(
    r"[^a-z0-9\s]", "", problem.lower()).replace(" ", "_") + ".py"
shutil.copy("./template.py", problem_filename)
