#!/usr/bin/python

import cgi,cgitb
import sendmail

print "Content-typ:tex/html"
print  


config={"server":"smtp.adsame.com",
	"fr":"kurt_sun@adsame.com",
   	"user":"kurt_sun",
	"password":"adsame123",
}

form=cgi.FieldStorage()

content=form.getvalue('content')
to=form.getvalue('tos')
config['subject']=form.getvalue('subject')


#print "<br><b>%s<b></br>" % to
config['to']=to.split(";")


sendmail.Mail(content,config).send_mail()

