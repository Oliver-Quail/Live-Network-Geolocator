from geolocator import *
from CustomThread import *
import pygeoip

data = ['64.12.24.50', '64.12.25.91', '205.188.13.12', '64.236.68.246', "177.4.4.1"]
searching = []
geo_data = pygeoip.GeoIP("GeoLiteCity.dat")

def process(pkt):

    
    thread = CustomThread(target=getLocation, args=(ip, geo_data))
    thread.start()
    print(thread.join())
    pass    

