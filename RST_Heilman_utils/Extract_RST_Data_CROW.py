# import required module
import os
import json
import re
import csv
# assign directory
directory = 'CROW'
 
# iterate over files in
# that directory
csv_f = open(directory + '/output.csv', 'w')
writer = csv.writer(csv_f)
header = ['file','Essay Type','Country','ID']
discourse_list = ['Elaboration', 'Same-Unit', 'Attribution', 'Joint', 'Enablement', 'Background', 'Comparison', 'Contrast', 'Manner-Means', 'Temporal', 'Condition', 'Summary', 'Cause', 'Topic-Comment', 'Evaluation', 'Explanation', 'Textual-Organization', 'Topic-Change']
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
    	if(f.endswith(".json") and not os.path.getsize(f) == 0):
            jsonFile = open(f)
            data = json.load(jsonFile)
            
            for i in data['scored_rst_trees']:
                endfile = f.rsplit('/', 1)[-1]
                essaytype = "Argumentative"
                row = [endfile,essaytype,endfile[9:13].replace('_', ''),endfile[endfile.rindex('_')-5:endfile.rindex('_')]]
                total = 0
                for discourse in discourse_list:
                    count = i.get('tree').count(":" + discourse.lower())
                    total += count
                for discourse in discourse_list:
                    count = i.get('tree').count(":" + discourse.lower())
                    row.append(count)
                    if(total > 0):
                        row.append(round(count/total,2))
                    else:
                        row.append(str(0))
                print(f)
                row.append(total)
                writer.writerow(row)
                
            jsonFile.close()
csv_f.close()
