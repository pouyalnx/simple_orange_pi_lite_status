import re
import json

data='''
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"></head><body style="background-color: black;color:white">
<h1>netstat</h1>

<h3>data</h3>
<pre>   Static hostname: pouyalnx
         Icon name: computer-laptop
           Chassis: laptop
        Machine ID: 98eecf2623de44cab7c700a1899ffac3
           Boot ID: 948e5271415640a2978f461a1dadf035
  Operating System: Ubuntu 18.04.4 LTS
            Kernel: Linux 4.15.0-101-generic
      Architecture: x86-64
wlp3s0    IEEE 802.11  ESSID:"Pouya"  
          Mode:Managed  Frequency:2.412 GHz  Access Point: 74:DA:DA:66:9F:79   
          Bit Rate=39 Mb/s   Tx-Power=16 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off
          Link Quality=54/70  Signal level=-56 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:57   Missed beacon:0

enp4s0f1: flags=4099&lt;UP,BROADCAST,MULTICAST&gt;  mtu 1500
        ether 08:9e:01:d5:fd:8f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73&lt;UP,LOOPBACK,RUNNING&gt;  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10&lt;host&gt;
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 6415  bytes 1237018 (1.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 6415  bytes 1237018 (1.2 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlp3s0: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt;  mtu 1500
        inet 192.168.1.7  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::bedb:fd2a:fb77:6b17  prefixlen 64  scopeid 0x20&lt;link&gt;
        ether 70:18:8b:78:05:db  txqueuelen 1000  (Ethernet)
        RX packets 284701  bytes 343884482 (343.8 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 238865  bytes 30701237 (30.7 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

</pre>


<h3>menu</h3>
<p><a href="http://localhost:8080/">back</a></p>

<h5>pouyalnx 2020</h5>

<pre hidden="">{"menu": {"back": "/"}, "data": "   Static hostname: pouyalnx\n         Icon name: computer-laptop\n           Chassis: laptop\n        Machine ID: 98eecf2623de44cab7c700a1899ffac3\n           Boot ID: 948e5271415640a2978f461a1dadf035\n  Operating System: Ubuntu 18.04.4 LTS\n            Kernel: Linux 4.15.0-101-generic\n      Architecture: x86-64\nwlp3s0    IEEE 802.11  ESSID:\"Pouya\"  \n          Mode:Managed  Frequency:2.412 GHz  Access Point: 74:DA:DA:66:9F:79   \n          Bit Rate=39 Mb/s   Tx-Power=16 dBm   \n          Retry short limit:7   RTS thr:off   Fragment thr:off\n          Power Management:off\n          Link Quality=54/70  Signal level=-56 dBm  \n          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0\n          Tx excessive retries:0  Invalid misc:57   Missed beacon:0\n\nenp4s0f1: flags=4099&lt;UP,BROADCAST,MULTICAST&gt;  mtu 1500\n        ether 08:9e:01:d5:fd:8f  txqueuelen 1000  (Ethernet)\n        RX packets 0  bytes 0 (0.0 B)\n        RX errors 0  dropped 0  overruns 0  frame 0\n        TX packets 0  bytes 0 (0.0 B)\n        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\nlo: flags=73&lt;UP,LOOPBACK,RUNNING&gt;  mtu 65536\n        inet 127.0.0.1  netmask 255.0.0.0\n        inet6 ::1  prefixlen 128  scopeid 0x10&lt;host&gt;\n        loop  txqueuelen 1000  (Local Loopback)\n        RX packets 6415  bytes 1237018 (1.2 MB)\n        RX errors 0  dropped 0  overruns 0  frame 0\n        TX packets 6415  bytes 1237018 (1.2 MB)\n        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\nwlp3s0: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt;  mtu 1500\n        inet 192.168.1.7  netmask 255.255.255.0  broadcast 192.168.1.255\n        inet6 fe80::bedb:fd2a:fb77:6b17  prefixlen 64  scopeid 0x20&lt;link&gt;\n        ether 70:18:8b:78:05:db  txqueuelen 1000  (Ethernet)\n        RX packets 284701  bytes 343884482 (343.8 MB)\n        RX errors 0  dropped 0  overruns 0  frame 0\n        TX packets 238865  bytes 30701237 (30.7 MB)\n        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\n"}</pre>
'''


pat=re.compile('<pre hidden="">[\n {}"A-Za-z0-9:/ \\\,-_&()]*</pre>')


dat=pat.findall(data)
#print(dat)

dat=dat[0]
dat=dat.replace('<pre hidden="">','')
dat=dat.replace('</pre>','')
print(dat)


x=json.loads(dat[0])

