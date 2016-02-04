"""
    Process the twenty news groups dataset and return a tsv file of the form 
    ||doc_id | doc_contents | label||
    Srivatsan Ramanujam <vatsan.cs@utexas.edu>, Nov-2015
"""

import os
import csv
def main(data_folder, output_file):
    """
        Data folder for twenty news groups dataset
    """
    doc_num = 0
    outf = csv.writer(open(output_file, 'w'), delimiter='\t', quoting=csv.QUOTE_MINIMAL)
    for root, dir, files in os.walk(data_folder):
        #we only want those files under a given topic (folder name)
        #disregard root level folders (like "train" and "test")
        if root and not dir and files:
            for f in files:
                fname = os.path.join(root, f)
                contents = open(fname,'r').read()
                output =  [doc_num, contents, root.split(os.sep)[-1]]
                outf.writerow(output)
                doc_num+=1
    print doc_num, 'documents written to', output_file
if __name__ == '__main__':
    from sys import argv
    if(len(argv) !=3):
        print 'Usage: python process_twenty_newsgroups.py <data folder> <output_file>'
    else:
        main(argv[1], argv[2])