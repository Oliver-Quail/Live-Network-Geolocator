from geolocator import *
from CustomThread import *
from filter import filter_local_ips
from scapy.all import *
import pygeoip
from dbHandler import dbHandler
data = []
searching = []
geo_data = pygeoip.GeoIP("GeoLiteCity.dat")


handler = dbHandler()


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
    data = thread.join()
    if data == "a":
        return
    print(data)
    data = str(data)
    data = data.split(",")
    handler.add(data[0],data[1],data[2])    




sniff(prn=wrapper) 