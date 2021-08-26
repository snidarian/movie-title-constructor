#!/usr/bin/python3

# This program will:
# 1. Take a list of titles and release years ("[MOVIE TITLE], [YEAR]") from csv file
# 2. reach the imdb pages of the .csv rows with advanced search, take the urls and create a "url_list.csv" file in the CWD
# 3. Create a titles_metadata.csv file delimited by spaces in the CWD using the urls in url_list.csv.

# IMPORTS
from selenium import webdriver
# Service class fix taken from https://dev.to/t00m/testing-selenium-4-0-0a5-pre-release-with-python-42h7
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# For using special keys like enter, alt, F1, etc...
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
# HTML parsing
from bs4 import BeautifulSoup as bs
# CSV library for writing data into and using data from .csv files
import csv
# colored terminal output for highlighting certain pieces of information useful to the user


# SETTING UP SELENIUM ON FIREFOX BROWSER
# setting up the Firefox browser with global scope
options = Options()

# set this to the path of your firefox profile file in the .mozilla folder in home dir
options.profile = '/home/cn1d4r14n/.mozilla/firefox/t8oqdk41.default-esr'
# allows you to run the browser as a background process I believe
options.headless = False

# link this to a web browser driver - here I'm using the geckodriver web driver file I downloaded online
service = Service('/home/cn1d4r14n/Documents/geckodriver')

driver = webdriver.Firefox(options=options, service=service)


# Takes title string and year and returns URL string of first result
def advanced_search_to_grab_url(title_string, year) -> str:
    print(f"{title_string} ({year})")

    driver.get('https://www.imdb.com/search/title/?ref_=kw_asr_tt')
    search_box = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/form/div/div[1]/div[2]/input")
    from_year_box = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/form/div/div[3]/div[2]/input[1]")
    to_year_box = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/form/div/div[3]/div[2]/input[2]")
    # enter details into the three boxes
    search_box.send_keys(title_string)
    from_year_box.send_keys(year)
    to_year_box.send_keys(year)
    # Press ENTER
    to_year_box.send_keys(Keys.RETURN)
    time.sleep(3)
    # click on the top search result and navigate to that page.
    first_search_result = driver.find_element_by_class_name("lister-item-header").find_element_by_tag_name('a')
    # click the link and navigate to the movie-listing page
    first_search_result.click()
    # return the recovered URL
    return driver.current_url


# Use search_titles.csv file to create a url_list.csv file
def search_titles_and_create_url_list_csv() -> None:
    # Open the search_titles.csv file (created by user prior to search)
    with open('search_titles.csv') as csv_search_data:
            csv_reader = csv.reader(csv_search_data, delimiter=',')
            url_list = []
            for row in csv_reader:
                url = advanced_search_to_grab_url(row[0], row[1])
                url_list.append(url)
            print(url_list)
    # create url_list.csv file
    with open('url_list.csv', mode='w') as url_data_file:
        url_list_writer = csv.writer(url_data_file, delimiter=',')
        for url_item in url_list:
            # important that the row item(s) be included as list items or else it will make every single character a different row-field
            url_list_writer.writerow([url_item])

def scrape_movie_data_with_urls_csv() -> list:
    # use url_list.csv to reach each page
    with open('url_list.csv') as url_data_file:
        csv_reader = csv.reader(url_data_file, delimiter='\n')
        # for each url: .get() method and then scrape [Title, year, three top actors, genres]
        titles_metadata_list = []
        for url in csv_reader:
            print(f"Getting url: {url}")
            driver.get(f"{url[0]}")
            movie_title = driver.find_element_by_xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1").text
            movie_year = driver.find_element_by_xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[1]/a").text
            #lead_actors_list = driver.find_elements_by_class_name("ipc-inline-list__item")
            actor_1 = driver.find_element_by_xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li[1]/a").text
            actor_2 = driver.find_element_by_xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li[2]/a").text
            actor_3 = driver.find_element_by_xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li[3]/a").text
            genre_list = []
            for _ in range(5):
                try:
                    genre = driver.find_element_by_xpath(f"/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/a[{_}]").text
                    genre_list.append(genre)
                except:
                    # out of listed genres
                    pass
            # make list item
            title_metadata = [movie_title, movie_year, actor_1, actor_2, actor_3, genre_list]
            # add list item to 'list of lists' title_metadata_list
            titles_metadata_list.append(title_metadata)
        return titles_metadata_list

            
            

def contruct_formatted_titles_and_save_to_csv(metadata_list_of_lists) -> None:
    with open('titles_list.csv', mode='w') as title_metadata_file:
        metadata_writer = csv.writer(title_metadata_file, delimiter=",")
        metadata_writer.writerows()


def main():
    # use search_titles.csv to create url_list.csv
    search_titles_and_create_url_list_csv()
    # use url_list.csv to reach each movie page and scrape relevant data
    titles_data = scrape_movie_data_with_urls_csv()
    # format and place list of lists in title_metadata.csv
    contruct_formatted_titles_and_save_to_csv(titles_data)
              


    
if __name__ == "__main__":
    main()








