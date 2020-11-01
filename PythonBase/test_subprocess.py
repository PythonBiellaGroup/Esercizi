import sys
import string
import subprocess

cmd = "/bin/ping 192.168.1.1"
 
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.decode('utf-8').rstrip())
