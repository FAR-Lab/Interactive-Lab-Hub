import re
import datetime


tf =  open('/home/gilbertoe.ruiz/Interactive-Lab-Hub/Lab 3/speech-scripts/lab3pt1B.txt', 'r')
mystr = tf.read()
tf.close()
last_partial = mystr.split('{')
tmp = '' 
for x in reversed(last_partial): #find last non-empty string in the file
    x = x.split(':')[-1].strip()
    x = re.sub(r'[^A-Za-z0-9 ]+', '', x).strip()
    if x == '':
        continue
    else:
        tmp = x
        break

    
tf =  open(f'/home/gilbertoe.ruiz/Interactive-Lab-Hub/Lab 3/output_{datetime.datetime.now().strftime("%m_%d_%Y__%H_%M_%S")}.txt', 'w+')
tf.write(tmp)
tf.close()
    
