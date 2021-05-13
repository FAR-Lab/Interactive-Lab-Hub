# importing library
import requests
from bs4 import BeautifulSoup
from subprocess import call

# enter city name
city = "Boston"

# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# formatting data
data = str.split('\n')
time = data[0]
sky = data[1]

# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text

# getting other required data
pos = strd.find('Wind')
other_data = strd[pos:]

text = "In " + city + "Temperature is" + temp + sky
#call out weather

cmd_beg= 'espeak '
cmd_end= ' | aplay ./weather.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
cmd_out= '--stdout > ./weather.wav ' # To store the voice file


#Replacing ' ' with '_' to identify words in the text entered
text = text.replace(' ', '_')

#Calls the Espeak TTS Engine to read aloud a Text
call([cmd_beg+cmd_out+text+cmd_end], shell=True)

# printing all data
print("In ", city)
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)
