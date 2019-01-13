def email_send_funct():
	import smtplib
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	from email.mime.base import MIMEBase
	from email import encoders
	
	email_user = 'alexis.assisstant@gmail.com'
	email_password = 'PASSWORD_OF_ABOVE_EMAIL'
	email_send = 'EMAILID_OF_RECEIVER'
	
	subject = 'Minutes of meeting document'
	
	msg = MIMEMultipart()
	msg['From'] = email_user
	msg['To'] = email_send
	msg['Subject'] = subject
	
	body = 'Hello, sending minutes of meeting. You also get the main action points from the meeting, the future tasks ans AI insights'
	msg.attach(MIMEText(body,'plain'))
	
	filename='hello.txt'
	attachment  = open(filename,'rb')
	
	part = MIMEBase('application','octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment; filename= "+filename)
	
	msg.attach(part)
	text = msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(email_user,email_password)
	
	
	server.sendmail(email_user,email_send,text)
	server.quit()
	
	
email_send_funct()
