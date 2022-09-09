import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

class GpuInfluxClient():
    '''
    This class contains the various method which are needed to: 
      * Connect to an influx datbase handle the connection
      * Write the multiple data points to the connected influxdb.
    '''

    def __init__(self, influxhost: str, token: str, bucketname: str, org: str = 'org'):
       self.__bucketname = bucketname
       self.__org = org
       self.__connectToInflux(influxhost, token)

    def write_data(self, prices: dict, source: str):
        for key, val in prices.items():
            point = influxdb_client.Point("prices")\
                        .tag('source', source)\
                        .field(key, val)
            
            print('Writing Points to influx...')
            self.__influxwriter.write(bucket=self.__bucketname, org=self.__org, record=point)

    def __connectToInflux(self, influxhost: str, token: str):
        print(f'Connecting to Influxdb on: {influxhost}')
        self.__influxclient = influxdb_client.InfluxDBClient(influxhost, token, self.__org, ssl=True)
        self.__influxwriter = self.__influxclient.write_api(write_options=SYNCHRONOUS)
        print('Connected!')

