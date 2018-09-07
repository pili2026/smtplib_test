import email_smtplib_function

smtplib_fun = email_smtplib_function.smtplib_test()
smtplib_test = smtplib_fun.create_message_with_attchment("chiwei2026@gmail.com", 
    "pili3722", "This is mail test for smtplib.", 
    "I'm mail test,hello world.", 
    fileAtt=['/home/jeremy/PyProjects/smtplib_test/image.jpg'],
    To=["Chi-Wei.Shen@zyxel.com.tw"],
    CC=["b9813114@outlook.com"], 
    BCC=["chiwei2026@gmail.com"])
