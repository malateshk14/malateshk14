import subprocess
#result = subprocess.run(command, shell=True, capture_output=True, text=True)
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("command executed.")
print("output \n",result.stdout)

if result.stderr:
    print("error \n", result.stderr)

"""
-------------------------------------------------------
command = "grep -i -n args basic1.py"
$ python linux_command.py
command executed.
output
 8:def manyArguments(*args):
10:    for val in args:
-------------------------------------------------------




"""
