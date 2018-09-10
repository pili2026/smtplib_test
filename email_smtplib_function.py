# -*- coding: utf-8 -*-
import smtplib
import mimetypes
import datetime
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email import charset
from email import utils, errors
 
class SmtplibFun:
    def __init__(self, user_name, user_pawd, subject, message_text):
        self.user_name = user_name
        self.user_pawd = user_pawd
        self.subject = subject
        self.message_text = message_text

    def create_message_with_attchment(self, attachment_file=None, To=[], CC=[], BCC=[]):
        
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

        msg['Subject'] = self.subject + ': [%s]' % str(datetime.date.today())
        msg['Message'] = self.message_text
        msg['From'] = self.user_name
        msg["To"] = ", ".join(To)
        msg["CC"] = ", ".join(CC)
        msg["BCC"] = ", ".join(BCC)
        msg['Date'] = utils.formatdate(localtime=1)
        msg['Message-ID'] = utils.make_msgid()
        msg['Content-Type'] = "text/calendar; charset=utf-8"
        body = MIMEText(html, 'html', "utf-8")
        
        # body = MIMEText(message_text, 'plain', "utf-8")
        body.set_charset("utf-8")
        msg.attach(body)
        print('msg =>', msg) 
         
        if attachment_file is not None:
            for file_list in attachment_file:
                print(file_list)     
                msg.attach(self.attachment(file_list))
                print('File Name =>', attachment_file)
        
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
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            # smtp.set_debuglevel(2)
            smtp.ehlo() # or smtp.helo()
            smtp.starttls() 
            smtp.login(self.user_name, self.user_pawd)
            smtp.sendmail(msg['From'], To + CC + BCC, msg.as_string())
            smtp.quit()
        except errors.MessageError as error:
            print("Something error at", error)
            print('An error occurred: %s' % error)

    def attachment(self, files):
        logging.basicConfig(level=logging.INFO)
        file_data = open(files, 'rb')
        mimeType, mimmeEncoding = mimetypes.guess_type(files)
        print("mimetype =>", mimeType)
        print('mimmeEncoding =>', mimmeEncoding)
        
        if mimmeEncoding or (mimeType is None):
            mimeType = 'application/octet-stream'
            logging.info(mimeType)
        mainType, subType = mimeType.split('/')
        
        if mainType == 'text':
            ret_val = MIMEText(file_data.read(), _subtype=subType, _charset='utf-8')
        else:
            ret_val = MIMEBase(mainType, subType)
            ret_val.set_payload(file_data.read())
            encoders.encode_base64(ret_val)
        file_name = self.getFileName(files)
        ret_val.add_header('Content-Disposition', 'attachment', filename=file_name)
        file_data.close()
        return ret_val

    def getFileName(self, sFileName):
        File = sFileName.split('/')
        return File[-1]    
