# import required module
import os
import json
import re
import csv
# assign directory
directory = 'ICNALE'
 
# iterate over files in
# that directory

discourse_list = ["Temporal", "Contingency", "Comparison", "Expansion", "EntRel", "Implicit", "Explicit"]

csv_f = open(directory + '/output.csv', 'w')
writer = csv.writer(csv_f)
header = ['file','Essay Type','Country','Level']
header_added = 0

             
#print(discourse_list)
for discourse in discourse_list:
    header.append(discourse + " N")
    header.append(discourse + " Mean")   
header.append("total lines")             
writer.writerow(header)
#print(header)

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file

    if os.path.isfile(f):
    	if(f.endswith(".pipe")):
                txtFile = open(f, "r",encoding="utf-8")
                data = txtFile.read()
                
                endfile = f.rsplit('/', 1)[-1]
                essaytype = "Smoking" if 'SMK' in endfile else "Jobs"
                row = [endfile,essaytype,endfile[2:5],endfile[10:14]]
                
                total = len(data.split("\n")) - 1
                
                for discourse in discourse_list:
                    count = data.count(discourse + "|")
                    row.append(count)
                    row.append(round(count/total,2))
                    
                row.append(total)    
                writer.writerow(row)
                
                txtFile.close()

"""
                background = data.count('background')
                explanation = data.count('explanation')
                elaboration = data.count('elaboration')
                joint = data.count('joint')
                attribution = data.count('attribution')
                condition = data.count('condition')
                span = data.count('span')
                total = int(re.findall(r'\d+', data)[-1])
                print(f)
                print("Background:" + str(background) + "/" + str(total) + " " + str(background/total*100))
                print("Explanation:" + str(explanation) + "/" + str(total) + " " + str(explanation/total*100))
                print("Elaboration:" + str(elaboration) + "/" + str(total) + " " + str(elaboration/total*100))
                print("Joint:" + str(joint) + "/" + str(total) + " " + str(joint/total*100))
                print("Attribution:" + str(attribution) + "/" + str(total) + " " + str(attribution/total*100))
                print("Condition:" + str(condition) + "/" + str(total) + " " + str(condition/total*100))
                print("Span:" + str(span) + "/" + str(total) + " " + str(span/total*100))
"""
                
                
                
                
#writer.writerow([endfile,essaytype,endfile[2:5],endfile[10:14],background,str(background/total*100),explanation,str(explanation/total*100),elaboration,str(elaboration/total*100),joint,str(joint/total*100), attribution, str(attribution/total*100), condition, str(condition/total*100), span, str(span/total*100), total])
                
"""
                
                endfile = f.rsplit('/', 1)[-1]
                essaytype = "Smoking" if 'SMK' in endfile else "Jobs"
                row = [endfile,essaytype,endfile[2:5],endfile[10:14]]
"""                                
  
                
csv_f.close()
        	

  

