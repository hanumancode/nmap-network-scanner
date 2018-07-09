import nmap

ns = nmap.PortScanner()

print(ns.nmap_version)

ns.scan('192.168.0.1','22-445', '-v --version-all')

#print(ns.scaninfo())

#print(ns.csv())

print(ns.scanstats())

#print(ns.all_hosts())

#print(ns['192.168.0.1'].state()) # checks to see if this host is up

print(ns['192.168.0.1'].all_protocols()) # scans for all protocols running. showing tcp protocol running on the specified IP

