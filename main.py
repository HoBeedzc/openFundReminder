# App Entry
import argparse
import os
import sys

from src.crawler import get_crawler
from src.api.eastmoney import EastMoneyFundAPI
# from src import app
# from src import config
# from src import logger
# from src import utils

# Parse arguments
parser = argparse.ArgumentParser(description='Run the app')
parser.add_argument('--config', type=str, default='config.yaml', help='Path to config file')
parser.add_argument('--log', type=str, default='logging.yaml', help='Path to logging config file')
parser.add_argument('-q','--query', type=str, default='-1', help='Query fund by code')
parser.add_argument('-v','--version', action='version', version='%(prog)s 0.1.0')
parser.add_argument('--use-api', type=str, default='eastmoney', help='Use specific API to get fund info')

def main():
    args = parser.parse_args()
    if args.query:
        print("Query fund: {}".format(args.query))
        api = EastMoneyFundAPI()
        crawler = get_crawler(fund_api=api)
        fund = crawler.crawler_fund_by_code(args.query)
        if fund:
            print(fund)
        else:
            print("Fund not found")
    # config_path = args.config
    # if not os.path.exists(config_path):
    #     print("Config file not found: {}".format(config_path))
    #     sys.exit(1)
    # config.load_config(config_path)
    # logger.init_logger(config.get_config().get('log'))
    # utils.init_utils(config.get_config().get('utils'))
    # app.run()

if __name__ == "__main__":
    main()

