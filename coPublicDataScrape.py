# Created by Kassrah Rezagholi @ OIT
# Purpose: This script will scrape designated
# data from the urls provided.  Targeting Colorado Open Data for GIS.  This is not a final product.
# Future Enhancements - Continuous "Machine learning / AI" with logs
# Specific Enhancements - Authentication capabilities, Change folder from URL to page title,
# Building a scraper for web services, Build into proper seperation for python / Modularization
# Add logic to handle non complete hrefs, sometimes there is not full links in the href and only partial forwarding.

from bs4 import BeautifulSoup
import urllib3.contrib.pyopenssl
import requests
import os
import time
from urlparse import urljoin
# VARIABLES
# Define all the sites to scrape data from
urls = ['https://yoursite.com/downloads/']  #Enter URLS here
# Save location
save_folder = r'C:\where\am\i\saving'

# Defines pool manager
https = urllib3.PoolManager()

# Checks for specified directory, if folder is not already created it will create one
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
else:
    print "Directory " + save_folder + " already exists"

# Creates Logs with static text
logTxtFail = open(save_folder + r'\fail_log.txt', 'w')
logTxtFail.write("Colorado Public Data Web Scraper \n" + "Created by Kassrah Rezagholi \n"
                "github - @rezaGIS \n" + "This log is of files that were flagged for download but failed due to some issue in the strings, use "
                "this file to refine logic. \n" + "#####################################################################################################"
                "################## \n"
                )
logTxtReject = open(save_folder + r'\reject_log.txt', 'w')
logTxtReject.write("Colorado Public Data Web Scraper \n" + "Created by Kassrah Rezagholi \n"
                    "github - @rezaGIS \n" + "This log is of files that were rejected from prospected scraping. Review entries to find missing data and refine logic \n" +
                    "####################################################################################################################### \n"
                    )
# Will iterate through URLS defined and find all the data on the site and filter out the a hrefs
for url in urls:
    # opens connection to url
    response = https.request('GET', url)
    # BeautifulSoup returns response
    soup = BeautifulSoup(response.data, "html.parser")
    # BeautifulSoup parses for 'a' tag
    links = soup.find_all('a', href=True)
    # Establish save location for data
    #parseURL = urlparse(url)
    saveFolderFormat = url
    # Formats urls to create a save directory that is logical for finding later
    saveFolderFormat = saveFolderFormat.replace(':', '_')
    saveFolderFormat = saveFolderFormat.replace('//', '')
    saveFolderFormat = saveFolderFormat.replace('/', '_')
    saveFolderFormat = saveFolderFormat.replace('.', '_')
    saveFolderFormat = saveFolderFormat.replace('?', '')
    # Creates folder for saving files after formatting name
    createFolderPath = os.path.join(save_folder, saveFolderFormat)
    if not os.path.exists(createFolderPath):
        os.makedirs(createFolderPath)
        print "Directory Created: " + createFolderPath
    # Iterates through all a tags with an href
    for link in links:
        href = link.get('href')
        # If these words are found in the href it will pass and begin download
        if '.zip' in href or '.shp' in href or '.kml' in href or '.kmz' in href or '.dwf' in href:
            fileDL = href.rsplit('/', 1)[-1]
            try:
                urlJoin = urljoin(url, href)
                r = requests.get(urlJoin)
                timeStamp = time.strftime("%Y%m%d_%H%M%S")
                newSaveTime = os.path.join(createFolderPath, timeStamp + fileDL)
                with open(newSaveTime, 'wb') as fd:
                    for chunk in r.iter_content(chunk_size=128):
                        fd.write(chunk)
                    print "Downloading: " + href
            except:

                logTxtFail.write("URL: \t" + url + "\t Failed Href: \t" + href + "\n")
                print href + " Failed."
        else:
            # Rejected hrefs

            logTxtReject.write("URL: \t" + url + "\t Rejected Href: \t" + href + "\n")
            print href + " Rejected."
# Release locks on logs
logTxtFail.close()
logTxtReject.close()
