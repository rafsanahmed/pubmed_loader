# coding=utf-8

import pubmed_parser as pp
import os
import json
from glob import glob
from tqdm import tqdm, trange


def count_articles(input_path, count_file, k="23n"):
    count=0
    # k is used for keyword to split the filename obtained from pubmed. It's different for each annual baseline
    input_files = sorted(glob(f'{input_path}*.json'), key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split(k)[-1]))
    # print(input_files)
    count_writer = open(count_file, "w", encoding="utf-8")
    
    for infile in tqdm(input_files):
        with open(infile, "r",encoding="utf-8") as f:
                full_articles = json.loads(f.read())
        
        count_writer.write(f"{os.path.splitext(os.path.basename(infile))[0].split(k)[-1]}\t{len(full_articles)}\n")
        count+=len(full_articles)
    
    count_writer.write(f"total\t{count}")



if __name__ == "__main__":

    input_path = "../res/abstracts/"
    output_file = f"{input_path}counts.txt"

    count_articles(input_path, count_file=output_file)




