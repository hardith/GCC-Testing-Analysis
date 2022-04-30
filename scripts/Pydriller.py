from pydriller import Repository
from datetime import datetime
import csv

file_dict = {}
contributers = {}
c = 0
for commit in Repository('https://github.com/gcc-mirror/gcc',
                         filepath='gcc/testsuite', num_workers=8, since=datetime(2018, 8, 1),
                         to=datetime(2022, 4, 25)).traverse_commits():
    if commit.author.name not in contributers:
        contributers[commit.author.name] = 0
    contributers[commit.author.name] += 1
    for file in commit.modified_files:
        filepath = file.new_path
        if filepath is None:
            filepath = file.old_path
        if filepath.startswith('gcc/testsuite'):
            if filepath not in file_dict:
                file_dict[filepath] = [[], [], 0]
            file_dict[filepath][2] += 1
            if commit.author_date.date().isoformat() not in file_dict[filepath][1]:
                file_dict[filepath][1].append(commit.author_date.date().isoformat())
            if commit.author.name not in file_dict[filepath][0]:
                file_dict[filepath][0].append(commit.author.name)


csv_list = []
csv_list.append(["filename", "added_date", "authors", "modified"])
for a in file_dict.keys():
    csv_list.append([a, min(file_dict[a][1]), file_dict[a][0], file_dict[a][2]])


with open("pydrillerData.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv_list)


authors_list = []
authors_list.append(["author", "No of commits"])
for author in contributers.keys():
    authors_list.append([author, contributers[author]])


with open("authordata.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(authors_list)
