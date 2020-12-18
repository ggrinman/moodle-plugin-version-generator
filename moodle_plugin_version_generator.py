#!/usr/bin/env python3

import datetime

def get_version_line():
    print("Find the version variable line")
    a_file = open("version.php", "r")
    list_of_lines = a_file.readlines()
    for i, line in enumerate(list_of_lines):
        if line.find("$plugin->version") != -1:
            print("Version line " + str(i))
            return i
    return -1

def get_current_version(line):
    print("Retrieve the current version")
    a_file = open("version.php", "r")
    list_of_lines = a_file.readlines()
    current_version = list_of_lines[line][(list_of_lines[line].find("=") + 1):-2].strip();
    print("Current version " + current_version)
    return current_version

def increase_version(current_version):
    print("Increase the current version")
    version_date = current_version[0:8]
    version_number = current_version[8:len(current_version)]
    version_number_len = len(version_number)
    print("Current version date " + version_date)
    print("Current version number " + version_number)
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    print("Current date " + current_date)
    if current_date > version_date:
        print("Increase the current version date and reset version number to 00")
        version_date = current_date
        version_number = "0"
    else:        
        version_number = int(version_number) + 1
    version_number = str(version_number).zfill(version_number_len)
    print("New version date " + version_date)
    print("New version number " + version_number)
    new_version = version_date + version_number
    print("New version " + new_version)
    return new_version

def overwrite_version(line, new_version):
    print("Overwrite the current version in the file")
    a_file = open("version.php", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[line] = "$plugin->version = " + new_version + ";\n"
    a_file = open("version.php", "w")
    a_file.writelines(list_of_lines)
    a_file.close()
    return

def main():
    line = get_version_line()
    if line > -1:
        current_version = get_current_version(line)
        new_version = increase_version(current_version)
        overwrite_version(line, new_version)

main()