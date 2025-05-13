def getLocation(ip, location_data):
    ip_data = location_data.record_by_name(ip)

    try:
        ip_data["longitude"]
    except TypeError:
        return ("%s not avalibable in dataset")%(ip)

    ip_logitude = ip_data["longitude"]
    ip_latitude = ip_data["latitude"]
    ip_city = ip_data["city"]
    return(("%s,%3f,%3f")%(ip, ip_latitude, ip_logitude) )
    