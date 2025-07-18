import shutil
import os
from datetime import datetime
source="C:/important"
backup_dir="C:/backupss"
timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")

print(os.path.exists(source)) #check if the file exist or not
print(os.path.exists(backup_dir))

#path for backup file, including its name
backup_file=os.path.join(backup_dir,f"backups_{timestamp}.zip") 

shutil.make_archive(backup_file.replace(".zip",""),"zip",source)

print(f"Backup created at:{backup_file}")

