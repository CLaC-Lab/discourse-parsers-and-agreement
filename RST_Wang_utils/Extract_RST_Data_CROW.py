# import required module
import os
import json
import re
import csv
# assign directory
directory = '/home/blaise/Desktop/Wang-2017-RST/RST-Parser-GIT/src/Ind_Essays_PreProcess/output'
 
# iterate over files in
# that directory
csv_f = open(directory + '/output.csv', 'w')
writer = csv.writer(csv_f)
header = ['file','Essay Type','Country','Level']
discourse_list = ['Elaboration', 'Same-Unit', 'Attribution', 'Joint', 'Enablement', 'Background', 'Comparison', 'Contrast', 'Manner-Means', 'Temporal', 'Condition', 'Summary', 'Cause', 'Topic-Comment', 'Evaluation', 'Explanation', 'Textual-Organization', 'Topic-Change', 'Comparison']
for discourse in discourse_list:
    header.append(discourse + " N")
    header.append(discourse + " %")   
header.append("total lines")        
writer.writerow(header)
for subdir, dirs, files in os.walk(directory):
  for filename in os.listdir(subdir):
    print(filename)
    f = os.path.join(subdir, filename)
    print(f)
    # checking if it is a file

    if os.path.isfile(f):
    	if(f.endswith(".parse")):
                parsefile = open(f)
                data = parsefile.read()
                
                print(data)
                endfile = f.rsplit('/', 1)[-1]
                essaytype = "Argumentative"
                row = [endfile,essaytype,endfile[9:13].replace('_', ''),endfile[endfile.rindex('_')-5:endfile.rindex('_')]]
                total = 0
            
                
                for discourse in discourse_list:
                    count = data.count("-" + discourse)
                    total += count
                for discourse in discourse_list:
                    count = data.count("-" + discourse)
                    row.append(count)
                    if(total > 0):
                        row.append(round(count/total,2))
                    else:
                        row.append(str(0))
                print(f)
                
                
                row.append(total)
                
                
                
                
                writer.writerow(row)
                 
  
                parsefile.close()
csv_f.close()
        	

  

