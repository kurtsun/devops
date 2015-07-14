#!/usr/bin/python

import cgi,cgitb
import urllib
import urllib2

print "Content-typ:tex/html"
print  



form=cgi.FieldStorage()

content=form.getvalue('content')
to=form.getvalue('tos')


#print "<br><b>%s<b></br>" % to
telphones=to.split(",")

requrl='http://msg.adsame.com/send.php'
for tel in telphones:
    sms_data={'telephone':str(tel),
           'system':'monitor',
	   'message':str(content),}
    data_encode = urllib.urlencode(sms_data)
    req = urllib2.Request(url=requrl,data=data_encode)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res
