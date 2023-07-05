#encoding utf8

from glob import glob
import os

def get_input_files(input_folder_path):
    '''
    get all NER result files within the given input folder in a sorted list
    '''
    return sorted(glob(f'{input_folder_path}*.json'), key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split("-")[-1]))

def get_file_idx(filename):
    return int(os.path.splitext(os.path.basename(filename))[0].split("-")[-1])
	
    
if __name__== "__main__":
    
    path_ = "../res/ner_chemical/"
    
    start = 0
    end = 120
    
    input_files_list = get_input_files(path_)
    #print(input_files_list)

    idx_list = [get_file_idx(x) for x in input_files_list]
    #print(idx_list)

    for i in range(start, end):
        if i not in idx_list:
            print(i)
    	