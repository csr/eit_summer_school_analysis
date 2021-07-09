import time
from random import random

import pandas as pd
import requests
import shutil

followers_csv = "../data/lopezobrador_followers.csv"
csv = pd.read_csv(followers_csv)

for (i, row) in csv.iterrows():
    # uncomment if something goes wrong and you want to resume the script from a certain point
    # if i < 2989:
    #     continue
    img_url_ = row['imgUrl']
    if pd.isna(img_url_):
        continue
    response = requests.get(img_url_, stream=True)
    png_name = "../data/profile_imgs/" + str(int(row['userId'])) + ".png"
    with open(png_name, 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)
    time.sleep(random()*2)