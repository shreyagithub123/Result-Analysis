import csv
import pandas as pd
from reportlab import platypus
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate

df = pd.read_csv('results1.csv', delimiter=',')
df = df.groupby('division').sum()

df.to_csv('groupbyedu.csv')
result2 = str(" ")
with open('groupbyedu.csv') as file1:
    reader = csv.DictReader(file1)
    #print 'Education wise, Absenteeism is as follows:' 
    result2 = result2 + str("Division wise, Total marks are as follows:\n") + str('\n') 
    for i,row in enumerate(reader):
       #print(row['Education'],row['noofhrsabsent'])
       result2 = result2 + str(row['division']) + str('----') + str(row['total']) + "<br/>"
       if(i >= 3):
         break
result2 = str(result2).replace('\n','<br />\n')
items = []
items.append(platypus.Paragraph(result2,PS('body')))
doc = SimpleDocTemplate('samp2.pdf')
doc.multiBuild(items)     
