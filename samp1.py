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
    result2 = result2 + str("Roll_Nos of the Top five students and their total marks are:\n") + str('\n') 
    for i,row in enumerate(reader):
        #print(row['ID'],row['absreason'])
        result2 = result2 + str(row['rollno']) + str('----') + str(row['total']) + "<br/>"
        if(i >= 4):
          break
result2 = str(result2).replace('\n','<br />\n')
items = []
items.append(platypus.Paragraph(result2,PS('body')))
doc = SimpleDocTemplate('samp1.pdf')
doc.multiBuild(items)
      
