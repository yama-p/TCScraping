# coding: UTF-8
import csv
import argparse
import Resume


parser = argparse.ArgumentParser(description = "description goes here")
parser.add_argument("-u",
                    type=str,
                    help = "help text goes here. This option is required",
                    required=True)


command_arguments = parser.parse_args()
scraping_url = command_arguments.u


with open('scraping.csv','w') as f:
    writer = csv.writer(f, lineterminator='\n')
    Resume.scraping(scraping_url, writer)
