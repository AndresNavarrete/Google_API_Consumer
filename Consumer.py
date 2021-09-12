import googlemaps

class Consumer:

    def __init__(self):
        self.my_key=''
        self.gmaps = googlemaps.Client(key=my_key)
    
    def getMetrics(self, origin, destiny, travel_mode):
        response = self.getResponse(origin, destiny, travel_mode)
        distanceInMeters = response['rows'][0]['elements'][0]['distance']['value']
        timeInSeconds = response['rows'][0]['elements'][0]['duration']['value'] 
        metrics = {
            'time': timeInSeconds,
            'distance': distanceInMeters
        }
        return metrics
        
    def getResponse(self, origin, destiny, travel_mode):
        response = gmaps.distance_matrix(
                                    origin,
                                    destiny,
                                    mode = travel_mode
                                    )
        return response


