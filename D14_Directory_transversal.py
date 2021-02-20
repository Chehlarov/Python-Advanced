import os
import pathlib

directory = input()

directory_dict = {}

for root, dirs, files in os.walk(directory):
    # print(root)
    # print(dirs)
    # print(files)
    # print('-------Moving to next iteration')
    for file in files:
        extension = '.' + file.split('.')[-1]
        if extension not in directory_dict:
            directory_dict[extension] = []
        directory_dict[extension].append(file)
# print(directory_dict)

file_output = ''

for extension in sorted(directory_dict.keys()):
    file_output += extension + '\n'
    for file in sorted(directory_dict[extension]):
        file_output += f"- - - {file}\n"

print(file_output)

report_path = str(pathlib.Path.home()) + os.path.sep + "Desktop" + os.path.sep + "report.txt"

with open(report_path, "w") as file:
    file.write(file_output)
