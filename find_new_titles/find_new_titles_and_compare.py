#!/usr/bin/python3

# This program will:
# Execute a bash command to compare each title in {user-supplied} imdb list with database


# IMPORTS
from selenium import webdriver
# Service class fix taken from https://dev.to/t00m/testing-selenium-4-0-0a5-pre-release-with-python-42h7
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# For using special keys like enter, alt, F1, etc...
from selenium.webdriver.common.keys import Keys
# for error handling
import selenium.common.exceptions as selenium_errors

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
# HTML parsing
from bs4 import BeautifulSoup as bs, GuessedAtParserWarning
# CSV library for writing data into and using data from .csv files
import csv
# colored terminal output for highlighting certain pieces of information useful to the user

import argparse

# colored terminal output
from colorama import Fore


# SETTING UP SELENIUM ON FIREFOX BROWSER
# setting up the Firefox browser with global scope
options = Options()

# set this to the path of your firefox profile file in the .mozilla folder in home dir
profile0 = '7w5vg7u0.default-esr'
profile1 = '5rz75ch6.default'
options.profile = f'/home/cn1d4r14n/.mozilla/firefox/{profile0}'
# allows you to run the browser as a background process I believe
options.headless = False

# link this to a web browser driver - here I'm using the geckodriver web driver file I downloaded online
# This bit no necessary if you install geckdriver in /usr/bin
#service = Service('/home/cn1d4r14n/Documents/geckodriver')

driver = webdriver.Firefox(options=options)


# Ansi color escape code - constants
RED=Fore.RED
GREEN=Fore.GREEN
RESET=Fore.RESET


def get_titles_from_imdb_list_and_store_in_array() -> None:
    pass


def use_ls_output_to_grep_to_see_if_title_exists_in_database() -> None:
    pass













