import shutil

source = "logs/aap.log"          # correct filename
destination = "logs/aap_backup.log"

shutil.copy(source, destination)
print("Backup done!")


