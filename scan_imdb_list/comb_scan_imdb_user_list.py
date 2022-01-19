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

# import os for running bash commands
import os


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
YELLOW=Fore.YELLOW
GREEN=Fore.GREEN
RESET=Fore.RESET


# need a list structure that is available to both functions
titles_list = []

# get titles list
def get_titles_from_imdb_list_and_store_in_array(url_list: str) -> None:
    driver.get(f'{url_list}')


    titles_count_text = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[4]/div[5]/div/div/span")))
    string_to_be_cut = f"{titles_count_text.text}"
    index_to_cut = string_to_be_cut.find('of ')
    final_string = string_to_be_cut.
    print(final_string)
    return


    page_break=False
    # for page in imdb-list
    while page_break==False:
        # for link in page
        for link_number in range(1,101, 1):
            try:
                # Try to find the link in div[x], if not found try to move to next page
                title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[4]/div[3]/div[{link_number}]/div[2]/h3/a"))).text
                year = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[4]/div[3]/div[{link_number}]/div[2]/h3/span[2]"))).text
                print(YELLOW)
                print(f"{title} {year}:")
                print(RESET)
                use_ls_output_to_grep_to_see_if_title_exists(f"{title}")
            except:
                # time to change pages
                print("Time to change pages")
        try:
            print("clicking the next page button")
            next_page_button_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[4]/div[5]/div/div/div/a[2]")))
            next_page_button_link.click()
            # Sleep to make sure the page is turned before looking for the next set of titles
            time.sleep(5)
        except:
            # Try the second "next page button xpath"
            try:
                next_page_button_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[4]/div[5]/div/div/a[2]")))
                next_page_button_link.click()
                # Sleep to make sure the page is turned before looking for the next set of titles
                time.sleep(5)
            except:
                # Break from the loop
                print("next page not located")
                page_break=True

    
    
# detemine if title is already possessed
def use_ls_output_to_grep_to_see_if_title_exists(search_term: str) -> None:
    print(GREEN)
    os.system(f'ls "{args.path_to_titles}" | grep -i "{search_term}"')
    print(RESET)


if __name__=='__main__':
    
    parser = argparse.ArgumentParser(description="Finds new titles with supplied imdb list")
    args = parser.add_argument("-l", "--list-url", type=str, help="full url to imdb list")
    args = parser.add_argument("-p", "--path-to-titles", type=str, help="absolute filepath to titles")
    args = parser.parse_args()


    get_titles_from_imdb_list_and_store_in_array(args.list_url)

    
    
    
    










