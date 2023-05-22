***
## BGP bird zabbix monitoring
***
## Description
Works with the zabbix agent in passive mode. Must be installed.  

bgp_bird_zabbix_monitoring.json     - Template from zabbix6. It has not been tested for import, but it is very simple and you can read the necessary parameters from it.  

bgp_bird_discovery.py               - Script for lld. Run command "sudo birdc show protocols | grep BGP" and get json with BGP peers.  

bgp_bird_peer_status.py             - Run command "sudo birdc show protocols | grep {arg} ". BGP peers are substituted. If is "Established" - peer is up, if not (any other value) - peer is down.  

userparameter_bird.conf             - zabbix agent userparameter   
***
## Installation
- copy scripts to /etc/zabbix/
- set the execute permission
```
sudo chmod +x /etc/zabbix/bgp_bird_discovery.py
sudo chmod +x /etc/zabbix/bgp_bird_peer_status.py
```
- copy userparameter_bird.conf to /etc/zabbix/zabbix_agentd.d/
- provide bird acces to zabbix user
```
sudo usermod -a -G bird zabbix
```
- restart zabbix-agent
```
systemctl restart zabbix-agent
```
- create zabbix template and assigne to host
***
