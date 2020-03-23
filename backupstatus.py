import paramiko
import os
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("IP", port=22, username="username",timeout=5000, key_filename='/root/.ssh/kename.rsa')



def controller_check():
  zones = ["mgmt", "exp"]
  for zone in zones:
    i=0
    while (i < 3):
      stdin, stdout, stderr = ssh.exec_command("ls -ltr /path/" + zone + "/is/here-" + str(i) + "/* | tail -3")
      opt = stdout.readlines()
      opt = "".join(opt)
      if 'db_backup.enc' in opt:
        print('Latest Backup of '+ zone + ' Controller '+ str(i)+ ' Found' )
        print(opt)
      else:
        print('WARNING Latest Backup of '+ zone + ' Controller '+ str(i)+ ' NOT PRESENT' )
        #print(opt)
      i=i+1



controller_check()
ssh.close()
