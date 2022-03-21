'''
Created on Jun 10, 2021
Starting code based on code from stack overflow question response: 
https://stackoverflow.com/questions/57205531/python-how-to-download-multiple-files-in-parallel-using-multiprocessing-pool
@author: meghan
Goal: download specified zip files from PharaGKB
'''

import requests
from zipfile import ZipFile
from io import BytesIO

def zip_downloader (url, filePath):
    '''
    The goal is to download and unzip the files from the PharmGKB Downloads page 
    @param url - link to the download file from PharmGKB
    @param filePath- where the files will be unzipped to (the output folder)
    '''
    file_name = url.split("/")[-1]
    r = requests.get(url)
    sourceZip = ZipFile(BytesIO(r.content))
    print(" Downloaded {} ".format(file_name))
    sourceZip.extractall(filePath)
    print(" extracted {}".format(file_name))
    sourceZip.close()

    
