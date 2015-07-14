from mailer import Mailer
from mailer import Message
import subprocess
import sys
import argparse

class Mail(object):
    #def __init__(self,body,args):
    #    self.server = args.server
    #    self.to = args.to
    #    self.fr = args.fr
    #    self.sub = args.subject
    #    self.body = args.body
    #    self.usr = args.user
    #    self.pwd = args.password
    
    def __init__(self,body,dict):
        self.server = dict['server']
        self.to = dict['to']
        self.fr = dict['fr']
        self.sub = dict['subject']
        self.body = body
        self.usr = dict['user']
        self.pwd = dict['password']
    

           

    def send_mail(self):
    
        message =  Message(From=self.fr,
                    To=self.to,
                    Subject=self.sub)
	message.Body = self.body

        sender = Mailer(host=self.server,usr=self.usr,pwd=self.pwd)
        sender.send(message)

        
if __name__ == '__main__':

    body = sys.stdin.read()

    parser = argparse.ArgumentParser(description='mail sender')
    parser.add_argument('--server', default="smtp.adsame.com", help='mail server')
    parser.add_argument('--to',nargs='+',default=["79512000@qq.com"],help='mail to')
    parser.add_argument('--fr',default="kurt_sun@adsame.com",help='mail from')
    parser.add_argument('--subject',required=True,help='subject')
    parser.add_argument('--user',default="kurt_sun",help='user')
    parser.add_argument('--password',default="adsame123",help='password')
    parser.add_argument('--body',default=body,help='message body')
    args = parser.parse_args()

    argsdict = args.__dict__;

    Mail(body,argsdict).send_mail()


