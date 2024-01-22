#Last updated:  1-22-2024
#this script does allow use on compound objects (8-21-2022)

#instructions: place this file and the csv file into the same directory as the .desc files: 
#C:\Users\yourprofilename\AppData\Roaming\OCLC\CONTENTdm Project Client\collectioname\Project # 

#PYTHON3 required plus the libraries listed on line 28.

"""be careful of the following characters (especially from MS Word or Excel)
Scene’s
“this is the end” 
Unique – and 
look out for ampersands: should replace with &amp; 
me‘am
... microsoft has a wierd elipsis character
watch for this: aśar ....change to this: aśar

also be sure the windows command prompt window is set to run utf-8 (stack overflow tells you how)

Required csv format:
record number,fieldnickname,value  [do not include these fieldnames at the top of the list]
1517,dateed,1921/1933
2911,dateed,1958

if any of your replacement strings contain commas, create csv with different delimiter such as "~" and tell the script at runtime what your delimiter is 
"""

import csv
import os
import glob
import codecs
import re
import time
import fnmatch
import datetime
import pandas
from os import listdir
from os.path import isfile, join

def replaceTextBetween(originalText, delimeterA, delimterB, replacementText):
    leadingText = originalText.split(delimeterA)[0]
    trailingText = originalText.split(delimterB)[1]
    return leadingText + delimeterA + replacementText + delimterB + trailingText

def does_file_exist_in_dir(path):
    return any(isfile(join(path, i)) for i in listdir(path))

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            s = open(filepath, encoding='utf-8').read()
            s = s.replace(find, replace)
            with open(filepath, "w", encoding='utf-8') as f:
                f.write(s)
                
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

startfile = input("Please enter the name of the csv file: ")

delim = input("please enter the delimiter you want to use: ")
counter=0
cntr = 0
cwd = os.getcwd()
flag = "on"
datetime=datetime.datetime.now()
fileflag = "on"



with open(startfile, 'rt') as f:
    readed = csv.reader(f, delimiter = delim)
    #readed = csv.reader(f, delimiter=delim,encoding='utf-8')
    changelist = list(readed)
    #print("changelist",changelist)
       

for x in changelist:
    linnum = 0
    counter = counter+1
    fname=x[0]+".desc"
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file == fname:
                fullpathname = find(fname, subdir)
                fieldlookup = x[1]
                #print(fieldlookup)
                if fieldlookup == "dater":
                    fieldlookup = "date"
                #print(fullpathname)
                ##time.sleep(3)
                contents = open(fullpathname, encoding='utf-8').read()
                findfield1 = "<"+fieldlookup+">"
                findfield2 = "</"+fieldlookup+">"
                match = re.search(rf"{findfield1}([\s\S]*?){findfield2}", contents, re.S | re.I | re.U)
                if match is None:
                    oldtext = ""
                    print("NOT FOUND: fname and fieldname: ",fname," ",fieldlookup)
                else:
                    oldtext = re.search(rf"{findfield1}([\s\S]*?){findfield2}", contents, re.S | re.I | re.U).group(1)
                if flag == "on":
                    #print(fullpathname)
                    flag = "off"
                    with open(startfile, 'r') as fp:
                        totallines = len(fp.readlines())
                        fp.close()
                print(fname,"~",fieldlookup,"~",x[2]," == ",cntr," of ",totallines)
                print("filename: ",fname)
                cntr = cntr + 1 
                findReplace(subdir, findfield1+oldtext+findfield2, findfield1+str(x[2])+findfield2, fname)
           
