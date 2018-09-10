import email_smtplib_function
import email_smtplib_function_2

smtplib_fun = email_smtplib_function.SmtplibFun(user_name="chiwei2026@gmail.com", 
    user_pawd="XX",
    subject="This is mail test for smtplib.",
    message_text="I'm mail test,hello world.")

smtplib_test = smtplib_fun.create_message_with_attchment(
    attachment_file=['/home/jeremy/PyProjects/smtplib_test/log.txt'],
    To=["Chi-Wei.Shen@zyxel.com.tw"],
    CC=["shenchiwei2026@gmail.com", "b9813114@outlook.com"], 
    BCC=["chiwei2026@gmail.com", "b9813114@gmail.com"])


# smtplib_fun = email_smtplib_function_2.SmtplibFun()
# smtplib_test = SmtplibFun.create_message_with_attchment(
#     userName="chiwei2026@gmail.com", 
#     userPawd="pili3722", 
#     subject="This is mail test for smtplib.", 
#     message_text="I'm mail test,hello world.", 
#     attachment_file=['/home/jeremy/PyProjects/smtplib_test/image.jpg',
#     '/home/jeremy/PyProjects/smtplib_test/ppt.pptx'],
#     To=["shenchiwei2026@gmail.com", "Chi-Wei.Shen@zyxel.com.tw"],
#     CC=["b9813114@outlook.com"], 
#     BCC=["chiwei2026@gmail.com"])