import subprocess
'''

Created by Basu Khadka Tue Nov 28 4:52 PM
Basic Automation file for ubuntu 
 
This Program will do the follwoing

 [1] Updates
 [2] UFW config
 [3] Delete unwanted media files
 [4] NGINX server is closed
 [5] SSH is started and running
 [6] Auditd is installed and running
 [7] delete some common hacking tools
 [8] sudo authentication
 [9] Disbale root acess through SSHD
 [10] Insecure Permissions on shadow file
 [10] PAM files

'''

#===============  Variables You Set Up ==============#
AllUsers = [
    ""
]
#====================================================#



#=============  Functions ============#

def returnCode(command,Passed,Failed):
    if(command.returncode==0):
        print("-"*20)
        print(Passed)
        print("-"*20)
    else:
        print("!"*20)
        print(Failed)
        print("!"*20)
    
def GetProhibitedFiles(rmv:bool):
    files = subprocess.run("sudo find home \( -iname '*.mp3' -o -iname '*.mp4' -o -iname '*.mov' -o -iname '*.wav' \)",shell=True,capture_output=True,text=True)
    if(not rmv):
        return files.stdout
    if(rmv):
        deletedFiles=subprocess.run("sudo find home \( -iname '*.mp3' -o -iname '*.mp4' -o -iname '*.mov' -o -iname '*.wav' \) -exec rm {} + >/dev/null",shell=True)
        returnCode(deletedFiles,"Succesfully Deleted Files","FAILED to delete files")

#=====================================#


# Updates
subprocess.run("sudo apt upgrade",shell=True)
subprocess.run("sudo apt update",shell=True)

# UFW Config
subprocess.run("sudo apt install ufw",shell=True)
deny = subprocess.run("sudo ufw default deny incoming >/dev/null",shell=True)

returnCode(deny,"UFW Incoming is set to deny","UFW Incoming FAILED to set to deny")
allow = subprocess.run("sudo ufw default allow outgoing >/dev/null",shell=True)
returnCode(allow,"UFW outgoing is set to allow","UFW outgoing FAILED to set to allow")

enable = subprocess.run("sudo ufw enable >/dev/null",shell=True)
returnCode(enable,"UFW enabled","UFW FAILED TO ENABLE")

# Media Files
files = GetProhibitedFiles(False)
print("==================== Prohibited Files ====================\n")
print(files)
print("==========================================================")
delete = input("Would You Like To Delete These Prohibited Files? (y/n)")
if(delete == "y"):
    GetProhibitedFiles(True)
else:
    print("="*20 + "\nDid not delete FIles\n" + "="*20)

# NGINX Service
subprocess.run("sudo systemctl stop nginx",shell=True)
subprocess.run("sudo systemctl disable nginx",shell=True)

# SSH
