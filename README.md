# PublicGISDataScraper
Python Script utilizing BeautifulSoup to scrape data from websites, targeting State and Local Govt data for the State of Colorado.

# About
Static data web scraper, this was built as a basic html parser / scraper.  Dynamic data scraping will come later. 

Built using Python 2.7.*   
 
# Getting Started
There are a few libraries to make sure you have installed on your python 2.7.*:

BeautifulSoup - <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#" target="_blank">Details</a>

- $ pip install beautifulsoup4

PyOpenSSL  - <a href="https://pyopenssl.org/en/stable/introduction.html" target="_blank">Details</a>


- $ pip install pyopenssl

Requests - <a href="https://pyopenssl.org/en/stable/introduction.html" target="_blank">Details</a>

- $ pip install requests

urllib3 - <a href="https://urllib3.readthedocs.io/en/latest/#" target="_blank">Details</a>

- $ pip install urllib3

# How to

Set websites to scrape and save folder
```python

urls = ['https://yoursite.com/downloads/']  #Enter URLS here
# Save location
save_folder = r'C:\where\am\i\saving\'
```

Run the script once those are set properly.

**Note**
This will not download dynamic data from sites like ArcGIS Portal, or any dynamically driven content on the website. Data needs to be built with static html.

Have fun, feel free to do as you please with this

# Open-data sites verified that work with this script

- http://www.adcogov.org/gisdata
- http://emap.mesacounty.us/DownloadData/

