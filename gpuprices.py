import configargparse

from src import scrapers
from src.gpu_influx_client import GpuInfluxClient

from src.scraperconfig import scrapers

def parseArguments():
    parser = configargparse.ArgParser(default_config_files=['config.conf'])

    parser.add_argument('--gpumodel', type=str, help='The name of the nvidia rtx gpu module to look for.')

    influxgroup = parser.add_argument_group('influx connection')
    influxgroup.add_argument('--influxurl', type=str, help='Url to the influxdb to use')
    influxgroup.add_argument('--influxtoken', type=str, help='Token for the Influxdb connection')
    influxgroup.add_argument('--influxorg', type=str, help='Orga String')
    influxgroup.add_argument('--influxbucket', type=str, help='Name of the Bucket to use.')

    return parser.parse_args()

def printResults(results: dict, source: str):
    print('Got the following results:')
    print(source)
    print(10 * ' - ')

    for model, price in results.items():
        print(f'\t{model}\t\t--> {price}€')

def scrape(scrapers: dict, model: str, influxclient: GpuInfluxClient):
 for source, scraper in scrapers.items():
    print(f'Scraping from: {source}...')
    prices = scraper.getPrices(model)
    printResults(prices, source)

    influxclient.write_data(prices, source)

def main():
    arguments = parseArguments()
    influxclient = GpuInfluxClient(arguments.influxurl, arguments.influxtoken,
                                    arguments.influxbucket, org=arguments.influxorg)

    # Scrape the prices using the registered scrapers
    scrape(scrapers, arguments.gpumodel, influxclient)        

main()
