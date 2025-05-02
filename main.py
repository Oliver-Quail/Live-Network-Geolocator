import pyshark
import re
from CustomThread import CustomThread
import pygeoip

geo_data = pygeoip.GeoIP("GeoLiteCity.dat")

capture = pyshark.FileCapture("./samples/evidence01.pcap", keep_packets=False)

ip_identified = {}
ip_extenernal_identified = []
local_ips = []
extenarl_ips = []

for packet in capture:
    try:
        packet_source_ip = packet.ip.src
    except AttributeError:
        print("Packet contained no IP addres")
        continue
    # Filter out all packets will local ip addresses
    if re.match("(^127\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)", packet_source_ip):
        if packet_source_ip not in local_ips:
            local_ips.append(packet_source_ip)
    elif not (re.match("(^127\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)", packet_source_ip)):
        if packet_source_ip not in extenarl_ips: 
            extenarl_ips.append(packet_source_ip)


print(local_ips)
print(extenarl_ips)


def getLocation(ip, location_data):
    ip_data = location_data.record_by_name(ip)
    ip_logitude = ip_data["longitude"]
    ip_latitude = ip_data["latitude"]
    ip_city = ip_data["city"]
    print("Ip address location: (%3f, %3f)", (ip_latitude, ip_logitude) )
    pass


getLocation(extenarl_ips[0], geo_data)

