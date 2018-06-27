# coding=utf-8
import os
import shutil
import platform
import img
import beauty360
import db360


basePath = r"./360photo"
if platform.system() == 'Windows':
    basePath = r"D:/360photo"

if os.path.isdir(basePath):
    shutil.rmtree(basePath)

if not os.path.isdir(basePath):
    os.mkdir(basePath)

print('spider start......',basePath)

for i in range(10) :
    db360.db_insert(i*30,'./beauty360.db')
for i in range(10):
    beauty360.spider360(i*30,basePath)

#db360.db_girlsall('./beauty360.db')

print('spider done ...... savecount ',img.savecount)
