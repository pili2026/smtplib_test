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
 
 
def attachment(filename):
    fd = open(filename, 'rb')
    mimetype, mimeencoding = mimetypes.guess_type(filename)
    print ("mimetype =>", mimetype)
    if mimeencoding or (mimetype is None):
        mimetype = 'application/octet-stream'
    maintype, subtype = mimetype.split('/')
    if maintype == 'text':
        retval = MIMEText(fd.read(), _subtype = subtype)
    else:
        retval = MIMEBase(maintype, subtype)
        retval.set_payload(fd.read())
        encoders.encode_base64(retval)
    filename = getFileName(filename)
    retval.add_header('Content-Disposition', 'attachment', filename = filename)
    fd.close()
    return retval
 
 
def Group_People_To_CC_BCC():
    To = []
    CC = []
    BCC = []
    #==to
    To.append("b9813114@gmail.com")
    To.append("Chi-Wei.Shen@zyxel.com.tw")
    #==cc
    CC.append("shenchiwei2026@gmail.com")
    CC.append("chiwei2026@gmail.com")
    #==Bcc
    BCC.append("b9813114@outlook.com")
    BCC.append("chiwei2026@gmail.com")
    return To, CC, BCC
 
def mail_main():
    msg = MIMEMultipart()
    charset.add_charset('utf-8', charset.SHORTEST, charset.QP, 'utf-8')
    sFile = r"/home/jeremy/PyProjects/smtplib_test/word.docx" #夾檔案
    sFile_2 = r"/home/jeremy/PyProjects/smtplib_test/0120.pdf"
    files = []
    files.append(sFile)
    files.append(sFile_2)
    To, CC, BCC = Group_People_To_CC_BCC()
    # message_text = """This is message test!! """
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
 
    subject = 'This is a mail test: [%s]' % str(datetime.date.today())
    msg['Subject'] = subject
    msg['From'] = 'chiwei2026@gmail.com'
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
    for filename in files:
        print(filename)     
        msg.attach(attachment(filename))
    
    userName = "chiwei2026@gmail.com"
    userPawd = "pili3722"    
 
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
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        # smtp.set_debuglevel(2)
        smtp.ehlo() # or smtp.helo()
        smtp.starttls() 
        smtp.login(userName, userPawd)
        smtp.sendmail(msg['From'], To + CC + BCC, msg.as_string())
        smtp.quit()
    except errors.MessageError as error:
        print("Something error at", error)
        print('An error occurred: %s' % error)
 
def getFileName(sFileName):
    File = sFileName.split("//")
    return File[-1]
 
if __name__ == '__main__':
    mail_main()