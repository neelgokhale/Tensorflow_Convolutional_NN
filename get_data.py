"""
Created by Neel Gokhale at 2020-07-20
File get_data.py from project week4_coursera
Built using PyCharm

"""

# NOTE: all relevant images are already downloaded into the img directory. Only run this function if you want to re-download.

import urllib.request
import os
import zipfile

# Downloading zip folder
URL = 'https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip'
urllib.request.urlretrieve(URL, '/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human.zip')


# Un-zipping
local_zip = '/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human')
zip_ref.close()

# Splitting directories
train_horse_dir = os.path.join('/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human/horses')
train_human_dir = os.path.join('/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human/humans')