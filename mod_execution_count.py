import json
import sys

infile = json.load(open(sys.argv[1]))
execution_count = 1
for cell in infile["cells"]:
    if cell["cell_type"] == "code":
        cell["execution_count"] = execution_count
        execution_count += 1

json.dump(infile, open(sys.argv[1], "w"))
