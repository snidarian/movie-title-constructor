#!/usr/bin/python3

# This program will:
# 1. Take a list of titles and release years ("[MOVIE TITLE], [YEAR]") from csv file
# 2. reach the imdb pages of the .csv rows with advanced search, take the urls and create a "url_list.csv" file in the CWD
# 3. Create a titles_list.csv file delimited by spaces in the CWD using the urls in url_list.csv.


import argparse

from selenium import webdriver
# Service class fix taken from https://dev.to/t00m/testing-selenium-4-0-0a5-pre-release-with-python-42h7
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# For using special keys like enter, alt, F1, etc...
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# HTML parsing
from bs4 import BeautifulSoup as bs
# CSV library for writing data into and using data from .csv files
import csv
# colored terminal output for highlighting certain pieces of information useful to the user


# setting up the Firefox browser with global scope
options = Options()

# set this to the path of your firefox profile file in the .mozilla folder in home dir
options.profile = '/home/cn1d4r14n/.mozilla/firefox/ct8fbiwt.default'
# allows you to run the browser as a background process I believe
options.headless = False

# link this to a web browser driver
service = Service('/home/cn1d4r14n/Documents/geckodriver')

driver = webdriver.Firefox(options=options, service=service)





def main():
    parser = argparse.ArgumentParser(description='Produces formatted movie title list from string list of titles')
    args = parser.add_argument("title_search_string", help="movie title and year string", nargs="*", type=str)
    args = parser.parse_args()

    for item in args.title_search_string:
        print(item)


    
if __name__ == "__main__":
    main()









