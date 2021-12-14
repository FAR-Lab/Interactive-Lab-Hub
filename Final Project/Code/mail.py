import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
import os
import ffmpeg
# reference: msg.add_header('Content-Disposition', 'attachment', filename=path.split('/')[-1])

# Email you want to send the update from (only works with gmail)
fromEmail = 'zl.tonyzhong@gmail.com'
# You can generate an app password here to avoid storing your password in plain text
# https://support.google.com/accounts/answer/185833?hl=en
fromEmailPassword = 'Lzzhfhd18.!?'

# Email you want to send the update to
toEmail = 'lz555@cornell.edu'




def sendEmail():
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'Fall Detected!'
	msgRoot['From'] = fromEmail
	msgRoot['To'] = toEmail
	msgRoot.preamble = 'Fall detected!'

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	msgText = MIMEText('Fall detected!')
	msgAlternative.attach(msgText)

	# os.system('rm recording.mp4')
	# os.system('ffmpeg -f v4l2  -s 1280x720 -t 15 -i /dev/video0 recording.mp4')
	path = "/home/pi/lingz/Interactive-Lab-Hub/Final/recording.mp4"

	fp = open(path, "rb")
	mkv = MIMEApplication(fp.read())
	mkv.add_header('Content-Disposition', 'attachment', filename=path.split('/')[-1])
	msgRoot.attach(mkv)

	
	
	# msgText = MIMEText('<img src="/home/pi/test.jpg">', 'html')
	# msgAlternative.attach(msgText)
# 
	# attachment = "test.jpg"
	# fp = open(attachment, 'rb')
	# msgImage = MIMEImage(fp.read())
	# fp.close()

	# msgImage.add_header('Content-ID', '<image1>')
	# msgRoot.attach(msgImage)

	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.starttls()
	smtp.login(fromEmail, fromEmailPassword)
	smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
	smtp.quit()

# sendEmail()