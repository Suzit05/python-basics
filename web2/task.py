import shutil
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#1.Parse system logs
def check_logs(file_path):
    errors=[]
    with open(file_path, "r") as f:
        for line in f:
            if "ERROR" in line:
                errors.append(line.strip())
    return errors    

#2.Create backup if error
def backup_data(source, backup_dir):
    timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file=os.path.join(backup_dir, f"backup-{timestamp}.zip")    
    shutil.make_archive(backup_file.replace(".zip", ""),"zip",source)   
    return backup_file

#3.notifies you via emai
def send_email(subject,body):
    msg=MIMEText(body)
    msg['To']="sujeet05kp@gmail.com" #receiver
    msg['From']="sujeet05kp@gmail.com" #sender
    msg['Subject']=subject

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login("sujeet05kp@gmail.com","your app password") #sever.login(sender,password)
        server.send_message(msg)

#run automation...
errors=check_logs("system.log")

if errors:
    backup_path=backup_data("C:/important","C:/backupss")
    send_email("ERROR detected-backup done!",f"ERROR:\n{chr(10).join(errors)}\n Backup: {backup_path}")
    print("Task done with error notifications")
else:
    print("NO error found")


 



 


