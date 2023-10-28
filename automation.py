import subprocess

print("Running Cyberpatriots Ubuntu Hardening")
print("This program will notify you when deleting files or making any other significant changes")
print("The program will do the following")
print("")

allow = input('Run Program (y/n)')


subprocess.run('sudo apt upgrade',shell=True)

# firewall policies 
subprocess.run('sudo ufw default deny incoming',shell=True)
subprocess.run('sudo ufw default allow outgoing',shell=True)
subprocess.run('sudo ufw enable',shell=True)

# finds and deletes mp3 files, 
# the + terminates the exec command and is more efficent as it allows the command to ground files together
# NOTE: you can also use (\;) but this will run rm command for every file found instead of just grouping 
# files together
#t he exec atribute just says to do the following with the files found 
# and the {} is used to symbolize the files found
# the -o stands for the OR operand
print("Following files found in home directory:")
subprocess.run('sudo find /home/ \( -iname "*.mp3" -o -iname "*.mp4" -o -iname "*.mov" -o -iname "*.wav" \)',shell=True)

delMedia = input("Delete All Media Files (y/n)")

if(delMedia == 'y'):
    subprocess.run(['sudo find /home/ \( -iname "*.mp3" -o -iname "*.mp4" -o -iname "*.mov" -o -iname "*.wav" \) -exec rm {} +'],shell=True)
else:
    print("Files Were Not Deleted")

