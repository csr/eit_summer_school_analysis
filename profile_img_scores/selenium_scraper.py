import time
from os import listdir
from os.path import isfile, join
from random import random

from selenium import webdriver
import requests

searchUrl = 'http://www.google.it/searchbyimage/upload'
driver = webdriver.Chrome()

first_iteration = True

imgs = [join("../data/profile_imgs", f) for f in listdir("../data/profile_imgs") if isfile(join("../data/profile_imgs", f))]

count = 0

with open("../data/id_to_score.csv", 'a') as output:
    for img_path in imgs:
        count += 1
        if count < 3:
            continue

        multipart = {'encoded_image': (img_path, open(img_path, 'rb')), 'image_content': ''}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers['Location']
        driver.get(fetchUrl)
        if first_iteration:
            input('You should make sure you have accepted google\'s term manually, '
                  'click on ACCEPT and then press any key to continue')
            output.write("id, score\n")
            first_iteration = False
        try:
            element = driver.find_element_by_id("result-stats")
            html_string = element.get_attribute('innerHTML')
            score = int(html_string.split(' ')[1])
        except Exception:
            # if result-stats not present then score is zero
            score = 0

        user_id = str(img_path).split('/')[-1].split('.')[0]

        output.write(str(user_id) + ", " + str(score) + "\n")
        time.sleep(random()*2)
        # print(str(user_id) + ", " + str(score))
        print(count)

driver.close()