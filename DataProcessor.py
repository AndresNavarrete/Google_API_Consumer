from datetime import datetime,time

class DataProcessor:

    def __init__(self, consumer):
        self.consumer = consumer
        self.output = pd.DataFrame()
    
    def readInput(self, inputManager):
        self.data = inputManager.df
    
    def proccesData(self):
        for row in self.data.iterrows():
            self.processRow(row)
            
    def processRow(self, row):
        origin = {
            'lat': row['origin_lat'],
            'lng': row['origin_lng']
        }

        destiny = {
            'lat': row['destiny_lat'],
            'lng': row['destiny_lng']
        }
        response = self.getResponse(origen, destiny)
        self.updateOutput(row, response)
    
    def getResponse(self, origen, destiny):
        mode = 'driving'
        return self.consumer.getMetrics(origin, destiny, mode)
    
    def updateOutput(self, row ,response):
        outputRow = {
            'id': row['id'],
            'origin_lat': row['origin_lat'],
            'origin_lng': row['origin_lng'],
            'destiny_lat': row['destiny_lat'],
            'destiny_lng': row['destiny_lng'],
            'time': response['time'],
            'distance': response['time']
        }
        self.output.append(outputRow, ignore_index = True)
    
    def exportExcel(self):
        self.output.to_excel('data_response.xlsx', sheet_name='ProcessedData', index = False)

