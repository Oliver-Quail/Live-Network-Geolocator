def getLocation(ip, location_data):
    ip_data = location_data.record_by_name(ip)
    ip_logitude = ip_data["longitude"]
    ip_latitude = ip_data["latitude"]
    ip_city = ip_data["city"]
    return(("%s address location: (%3f, %3f)")%(ip, ip_latitude, ip_logitude) )
    