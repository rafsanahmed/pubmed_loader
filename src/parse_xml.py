# coding=utf-8

import pubmed_parser as pp
import os
import json
from glob import glob
from tqdm import tqdm, trange

class PubMedLoader:
    
    def __init__(self, input_path,  output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.counter = {}
        
    def get_input_files(self, input_path):
        return glob(input_path + "*.xml.gz")
    
    def get_counter(self):
        return self.counter
    
    def load_xml_and_convert(self, input_file):
        data = pp.parse_medline_xml(input_file, year_info_only=False)
        
        count=0
        d_main = {}
        for art in data:
            if "abstract" in art:
                if len(art["abstract"])>0:
                    count+=1
                    pmid = art["pmid"] if "pmid" in art else count_tot
                    d_main[pmid] = {"title": art["title"],
                                   "abstract":art["abstract"],
                                   "mesh_terms":art["mesh_terms"],
                                   "pubdate":art["pubdate"],
                                   "chemical_list":art["chemical_list"]}
        
        self.counter[input_file] = count
        return d_main

    def write_to_json(self, data, input_file):
        outfile = os.path.join(self.output_path, os.path.basename(input_file.split(".xml")[0])+".json")
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(json.dumps(d_main, indent=2, ensure_ascii=False))
            
    def run_loader(self):
        input_files_list = self.get_input_files(self.input_path)
        
        for i, input_file in tqdm(enumerate(input_files_list)):
            
            data = self.load_xml_and_convert(input_file)
            self.write_to_json(data, input_file)


if __name__ == "__main__":

    input_path = "../data/tmp/"
    output_path = "../res/abstracts/"
    os.makedirs(output_path, exist_ok=True)

    loader = PubMedLoader(input_path,output_path)

    loader.run_loader()
    
    with open(f"{output_path}counts.txt", "w", encoding="utf-8"):
        for k, v in loader.get_counter().items():
            f.write(f"{k}\t{v}\n")




