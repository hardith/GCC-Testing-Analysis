import os
import pathlib
import csv
  
all_files = list()
dir_path = "../gcc-11.2.0"
language_list = [".c",".cc",".f90",".go",".m",".mm"]
language_dict = {
    ".c":0,
    ".cc":0,
    ".f90":0,
    ".go":0,
    ".m":0,
    ".mm":0
}

extension_map = {
    ".c":"C",
    ".cc":"CPP",
    ".f90":"Fortran",
    ".go":"Go",
    ".m":"Objective C",
    ".mm":"Objective CPP"
}

output_dict = {}
# Iterate for each dict object in os.walk()
for root, dirs, files in os.walk(dir_path):
    # Add the files list to the the all_files list
    all_files.extend(files)


def getExtension(files):
    for file in files:
        extension = pathlib.Path(file.lower()).suffix
        if extension in language_list:
            language_dict[extension] = language_dict[extension] + 1

def createOutputDict():
    for key in language_dict:
        output_dict[extension_map[key]] = language_dict[key]

def output_to_csv():
    with open('../csv-data/ExtensionsData.csv', 'w') as f:
        f.write("%s,%s\n" % ("Language","Count"))
        for key in output_dict.keys():
            f.write("%s, %s\n" % (key, output_dict[key]))

    print("------------done-------------")


getExtension(all_files)
createOutputDict()
output_to_csv()
