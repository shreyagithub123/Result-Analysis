import csv
import pandas as pd
from reportlab import platypus
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate

df = pd.read_csv('results1.csv', delimiter=',')
df = df.sort_values(['total'], ascending=[False]) # parameter ascending is applied to 'col1' and 'col2' respectively.

df.to_csv('sorted.csv')
result2 = str(" ")
with open('sorted.csv') as file1:
    reader = csv.DictReader(file1)
    #print 'IDs of the Top five absentees and the absent categories are:'
    result2 = result2 + str("Roll_Nos of students failed in subject1 and their subject marks are:\n")
    j = 0
    for i,row in enumerate(reader):
        #print(row['ID'],row['absreason'])
        if(int(row['subject1']) < 40):       
          result2 = result2 + str(row['rollno']) + str('----') + str(row['subject1']) + "<br/>"
          j = j + 1
    if(j == 0):
      result2 = result2 + str('NONE') + "<br/>"
    
        
result2 = str(result2).replace('\n','<br />\n')
items = []
items.append(platypus.Paragraph(result2,PS('body')))
doc = SimpleDocTemplate('samp3.pdf')
doc.multiBuild(items)
      
