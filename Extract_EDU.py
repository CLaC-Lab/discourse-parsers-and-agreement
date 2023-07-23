# import required module
import os
import json
import re
import csv
# assign directory
directory = '/home/blaise/Desktop/RST-Finder-Trained/trained-RST-finder/Ind_Essays'
 
# iterate over files in
# that directory
csv_f = open(directory + '/comb_edus_joint_redo.csv', 'w')
#⛄ because comma was giving issues in libreoffice calc, and because he just a lil snowman :)
writer = csv.writer(csv_f, delimiter='⛄')
header = ['file','Essay Type','Country','Level','EDU','RST 2015']
writer.writerow(header)

#rows to write to excel spreadsheet. created in first loop, appended to with second parser data and added to csv file in second loop. see "FIRST LOOP" and "SECOND LOOP"
rows = []

def find_parens(s):
    toret = {}
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret
    
def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

#---------------------------FIRST LOOP---------------------------
#loop through TRAINED RST FINDER (2015)
for subdir, dirs, files in os.walk(directory):
  for filename in os.listdir(subdir):
    print(filename)
    f = os.path.join(subdir, filename)
    print(f)
    # checking if it is a file

    if os.path.isfile(f):
    	if(f.endswith(".json")):
            jsonFile = open(f)
            data = json.load(jsonFile)
           
            
            for i in data['scored_rst_trees']:
                endfile = f.rsplit('/', 1)[-1]
                essaytype = "Smoking" if 'SMK' in endfile else "Jobs"
                row = [endfile,essaytype,endfile[2:5],endfile[15:19]]
                
                tree_tok = i.get('tree').split(' ')
                
                last_lab = "None"
                curr_edu_label = []
                for line in tree_tok:
                    if ':' in line:
                        curr_edu_label.append(line[line.find(':')+1:])
                    line = line.replace(')','')
                    if(line.isdigit()):
                        edu = data['edu_tokens'][int(line)]
                        edu_unravel = ' '.join(edu)
                        row.append(edu_unravel)
                        
                        for c in curr_edu_label:
                            if "span" not in c:
                                last_lab = c
                            else:
                                last_lab = "Nucleus"
                        row.append(last_lab)
                        rows.append(row)
                        curr_edu_label = []
                
                        row = [endfile,essaytype,endfile[2:5],endfile[15:19]]    
                
            jsonFile.close()
        	
        	
# assign directory
directory = '/home/blaise/Desktop/Wang-2017-RST/RST-Parser-GIT/src/Ind_Essays_PreProcess/output'
EDUS_dire = '/home/blaise/Desktop/Wang-2017-RST/RST-Parser-GIT/src/Ind_Essays_PreProcess'

#https://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string        	
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def find_parens(s):
    toret = {}
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret
    
def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]




#---------------------------SECOND LOOP---------------------------
#loop through RST PARSER (2017)
for subdir, dirs, files in os.walk(directory):
  for filename in os.listdir(subdir):
    print(filename)
    f = os.path.join(subdir, filename)
    print(f)
    # checking if it is a file

    if os.path.isfile(f):
    	if(f.endswith(".parse")):
                parsefile = open(f)
                data = parsefile.readlines()
               
                endfile = f.rsplit('/', 1)[-1]
                essaytype = "Smoking" if 'SMK' in endfile else "Jobs"
                row = [endfile,essaytype,endfile[2:5],endfile[15:19]]
                
                curr_edu_label = "none"
                label_dic = []
                for line in data:
                    leadsp = len(line) - len(line.lstrip(' '))
                    if 'NS-' in line or 'SN-' in line or 'NN-' in line:
                        curr_edu_label = line[line.find('-')-2:line.find(' ',line.find('-'))]
                    label_dic.append((leadsp,curr_edu_label))
                    
                    ed_idx = line.count('EDU')
                    edu_since_last = 0
                    for i in range(ed_idx):
                        edu = line[find_nth(line,'EDU',i+1)+6:line.find(')',find_nth(line,'EDU',i+1)+6)-2]
                        edu = edu.replace('_',' ')
                        row.append(edu)
                        print(curr_edu_label)
                        if curr_edu_label is not "none" and "NS-" in curr_edu_label:
                            if i > 0:
                                row.append("leaf level")
                                row.append(curr_edu_label[3:])
                            else:
                                row.append("leaf level")
                                row.append("nucleus")
                        elif curr_edu_label is not "none" and "SN-" in curr_edu_label:
                            if i is 0:
                                row.append("leaf level")
                                row.append(curr_edu_label[3:])
                            else:
                                row.append("leaf level")
                                row.append("nucleus")
                        elif curr_edu_label is not "none" and "NN-" in curr_edu_label:
                            if i > 0:
                                row.append("leaf level - multinucleic")
                                row.append(curr_edu_label[3:])
                            else:
                                row.append("leaf level - multinucleic")
                                row.append("nucleus")
                        else:
                            labelUpOne = ""
                            for lab in label_dic:
                                if lab[0] == leadsp-2:
                                    labelUpOne = lab[1]
                            row.append("second level")
                            row.append(labelUpOne[3:])
                        for r in rows:
                            if r[0] in row[0] and ''.join(e for e in row[4] if e.isalnum()).lower() == ''.join(e for e in r[4] if e.isalnum()).lower():
                                for element in row:
                                    r.append(element)
                                writer.writerow(r)
                                rows.remove(r)
                                print(r)
                                break 
                
                        row = [endfile,essaytype,endfile[2:5],endfile[15:19]]           
                parsefile.close()
csv_f.close()        	

  

