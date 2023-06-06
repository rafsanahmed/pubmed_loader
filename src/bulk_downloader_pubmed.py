# coding=utf-8

import requests
import urllib.request
import time
from tqdm import tqdm, trange

if __name__ == "__main__":

    save_path = "../data/tmp/"
    for i in trange(1,1767):
        url = f'https://data.lhncbc.nlm.nih.gov/public/ii/information/MBR/Baselines/2023/pubmed23n{i:04d}.xml.gz'
        try:
            urllib.request.urlretrieve(url, filename=f"{save_path}pubmed23n{i:04d}.xml.gz")
        except:
            continue
        
        if i%3==0:
            time.sleep(0.5)
        




