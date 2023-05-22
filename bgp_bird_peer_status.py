import subprocess,sys

# read the first argument, it should be the name of the peer. set in userparameter
arg     = sys.argv[1]
# execute the command, capture the output, and render it as a string. grep on each name of the peer
result  = subprocess.run( f"sudo birdc show protocols | grep {arg} ", capture_output=True, text=True, shell=True).stdout
# if the line contains "Established", then the peer is up, if some other value, then we consider the peer is not working
if "Established" in result:
    print(1)
else:
    print(0)
