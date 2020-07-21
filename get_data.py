"""
Created by Neel Gokhale at 2020-07-20
File get_data.py from project week4_coursera
Built using PyCharm

"""

# NOTE: run this py program once before running validation.py.

import urllib.request
import os
import zipfile

# Downloading zip folder

# Training
URL = 'https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip'
urllib.request.urlretrieve(URL, '/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human.zip')
# Validation
val_URL = 'https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip'
urllib.request.urlretrieve(val_URL, '/Users/Owner/PycharmProjects/week4_coursera/img/validation-horse-or-human.zip')

# Un-zipping

# Training
local_zip = '/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human')
os.remove(local_zip)
# Validation
val_local_zip = '/Users/Owner/PycharmProjects/week4_coursera/img/validation-horse-or-human.zip'
zip_ref = zipfile.Zipfile(val_local_zip, 'r')
zip_ref.extractall('/Users/Owner/PycharmProjects/week4_coursera/img/validation-horse-or-human')
zip_ref.close()
os.remove(val_local_zip)

# Splitting directories

# Training
train_horse_dir = os.path.join('/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human/horses')
train_human_dir = os.path.join('/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human/humans')
# Validation
val_horse_dir = os.path.join('/Users/Owner/PycharmProjects/week4_coursera/img/validation-horse-or-human/horses')
val_human_dir = os.path.join('/Users/Owner/PycharmProjects/week4_coursera/img/validation-horse-or-human/humans')