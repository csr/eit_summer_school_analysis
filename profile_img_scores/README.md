# Profile images score
This folder contains script to:

- 1 Scrape Twitter profile images of users (provided as a csv)
- 2 Feed each image to Google reverse image search and grab how many 'search results' Google tool has found.
- 3 A csv with two columns (id and score) is produced. Score is how many 'search results' where found.

## Instructions
Install the required stuff to run selenium (https://selenium-python.readthedocs.io/installation.html)

First run `download_profile_imgs.py` and check it correctly downloads the images.
Then run selenium_scraper.py