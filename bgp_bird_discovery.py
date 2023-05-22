import subprocess,re,json

# execute the command, capture the output and make it as a string
result      = subprocess.run( "sudo birdc show protocols | grep BGP", capture_output=True, text=True, shell=True).stdout
# we separate the output into different lines, each with a description of one bgp peer
peers_list  = re.split(r'\n', result)

# create a variable in the format for lld zabbix
out = {"data": []}
# parse each line with peers
for peer in peers_list:
    try:
        # in the string, the first value is the name of the peer, so we split the string and take the 0 element
        peer_name = peer.split()[0]
        # add to variable for lld zabbix
        out["data"].append({ "{#BGPPEER}": peer_name})
    except:
        None
print(json.dumps(out, indent=4, sort_keys=True))