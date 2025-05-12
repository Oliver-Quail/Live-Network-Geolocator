from geolocator import *
from CustomThread import *
from filter import filter_local_ips
from scapy.all import *
import pygeoip


data = []
searching = []
geo_data = pygeoip.GeoIP("GeoLiteCity.dat")


def wrapper(pkt):
    if IP in pkt:
        # Filter out local ip addresses and as we cannot geolocate them
        if filter_local_ips(pkt[IP].src):
            if pkt[IP].src not in data:
                data.append(pkt[IP].src)
                process(pkt[IP].src)

def process(ip):
    thread = CustomThread(target=getLocation, args=(ip, geo_data))
    thread.start()
    print(thread.join())
    pass    




sniff(prn=wrapper) 