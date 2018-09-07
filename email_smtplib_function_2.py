# -*- coding: utf-8 -*-
import sys
import base64
import smtplib
import mimetypes
import datetime
import time
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email import charset
from email import utils, errors
 
class smtplib_test:
    def __init__(self):
        pass 

    def create_message_with_attchment(self, userName, userPawd, subject, message_text,
        fileAtt=[None], To=[], CC=[], BCC=[None]):
        
        html = """\
        <html>
          <head></head>
          <body>
            <p>Hi!<br>
               How are you?<br>
               Here is the <a href="https://www.python.org">link</a> you wanted.
            </p>
          </body>
        </html>
        """

        msg = MIMEMultipart()
        charset.add_charset('utf-8', charset.SHORTEST, charset.QP, 'utf-8')

        msg['Subject'] = subject + ': [%s]' % str(datetime.date.today())
        msg['Message'] = message_text
        msg['From'] = userName
        msg["To"] = ", ".join(To)
        msg["CC"] = ", ".join(CC)
        msg["BCC"] = ", ".join(BCC)
        msg['Date'] = utils.formatdate(localtime = 1)
        msg['Message-ID'] = utils.make_msgid()
        msg['Content-Type'] = "text/calendar; charset=utf-8"
        body = MIMEText(html, 'html', "utf-8")
        # body = MIMEText(message_text, 'plain', "utf-8")
        body.set_charset("utf-8")
        msg.attach(body)
        print('msg_1 =>', msg) 
        print('fileName =>', fileAtt) 

        fileData = open(fileAtt, 'rb')
        mimeType, mimmeEncoding = mimetypes.guess_type(fileAtt)
        print("mimetype =>", mimeType)
        print('mimmeEncoding =>', mimmeEncoding)

        try:
            # '''
            # Use the SMTP connection on SSL (Secure Sockets Layer) mode.
            # '''
            # smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            # smtp.ehlo()
            # smtp.login(userName, userPawd)

            '''
            Put the SMTP connection in TLS (Transport Layer Security) mode.
            '''
            print(msg["To"])
            # smtp = smtplib.SMTP('smtp.gmail.com', 587)
            # # smtp.set_debuglevel(2)
            # smtp.ehlo() # or smtp.helo()
            # smtp.starttls() 
            # smtp.login(userName, userPawd)
            # smtp.sendmail(msg['From'], To + CC + BCC, msg.as_string())
            # smtp.quit()
        except errors.MessageError as error:
            print("Something error at", error)
            print('An error occurred: %s' % error)