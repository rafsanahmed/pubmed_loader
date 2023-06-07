# coding=utf-8

import requests
import urllib.request
import time
import os
from tqdm import tqdm, trange

if __name__ == "__main__":

    save_path = "../data/tmp/update_files/"
    os.makedirs(save_path, exist_ok=True)

    f = open(f"{save_path}err.txt", "w", encoding="utf8")
    for i in trange(1167,1371):
        # url = f'https://data.lhncbc.nlm.nih.gov/public/ii/information/MBR/Baselines/2023/pubmed23n{i:04d}.xml.gz'
        url = f'https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/pubmed23n{i:04d}.xml.gz'
        try:
            urllib.request.urlretrieve(url, filename=f"{save_path}pubmed23n{i:04d}.xml.gz")
        except:
            f.write(f"{i}\n")
            continue

        if i%3==0:
            time.sleep(0.5)
    f.close()
        




