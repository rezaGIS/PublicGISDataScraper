#Created by Kassrah Rezagholi @ OIT
#Purpose: This script will scrape designated
#data from the urls provided.  This is not a final product.
#Future Enhancements - Continuous "Machine learning / AI" with logs
#Specific Enhancements - Authentication capabilities, Change folder from URL to page title,
#Building a scraper for web services, Build into proper seperation for python / Modularization


from bs4 import BeautifulSoup
import urllib3.contrib.pyopenssl
import requests
import os
import shutil

https = urllib3.PoolManager()
# Define all the sites to scrape data from
urls = ['https://www.adcogov.org/gisdata', 'http://emap.mesacounty.us/DownloadData/']
# Save location
save_folder = r'C:\Users\Kassr\Desktop\SaveFolder'
#Creates Logs with static text
logTxtFail = open(r'C:\Users\Kassr\Desktop\SaveFolder\fail_log.txt', 'w')
logTxtFail.write("OIT - GCDP Web Scraper \n" + "Created by Kassrah Rezagholi \n" +
             "This log is of files that were flagged for download but failed due to some issue in the strings, use this file to refine logic. \n" +
             "####################################################################################################################### \n"
             )
logTxtReject = open(r'C:\Users\Kassr\Desktop\SaveFolder\reject_log.txt', 'w')
logTxtReject.write("OIT - GCDP Web Scraper \n" + "Created by Kassrah Rezagholi \n" +
             "This log is of files that were rejected from prospected scraping. Review entries to find missing data and refine logic \n" +
             "####################################################################################################################### \n"
             )
### Will iterate through URLS defined and find all the data on the site and filter out the a hrefs
for url in urls:
    #opens connection to url
    response = https.request('GET', url)
    #BeautifulSoup returns resonse
    soup = BeautifulSoup(response.data)
    #BeautifulSoup parses for 'a' tag
    links = soup.find_all( 'a', href=True )
    #Establish save location for data
    saveFolderFormat = url
    #Formats urls to create a save directory that is logical for finding later
    saveFolderFormat = saveFolderFormat.replace(':','_')
    saveFolderFormat = saveFolderFormat.replace('//','')
    saveFolderFormat = saveFolderFormat.replace('/','_')
    saveFolderFormat = saveFolderFormat.replace('.','_')
    #Creates folder for saving files after formatting name
    createFolderPath = os.path.join(save_folder, saveFolderFormat)
    if not os.path.exists(createFolderPath):
        os.makedirs(createFolderPath)
        print "Directory Created: " + createFolderPath
    for link in links:
        href = link.get( 'href' )
        if '.zip' in href or '.shp' in href:
           fileDL = href.rsplit('/', 1)[-1]
           newSave = os.path.join(createFolderPath, fileDL)
           try:
               r = requests.get(href)
               with open(newSave, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
           except:
                logTxtFail.write("URL: \t" + url + "\t Failed Href: \t" + href + "\n")
                print href + " Failed."
           print href
           #print r
        else:
            #Rejected hrefs
            logTxtReject.write("URL: \t" + url + "\t Rejected Href: \t" + href + "\n")
            print href + " rejected"
#Release locks on logs
logTxtFail.close()
logTxtReject.close()