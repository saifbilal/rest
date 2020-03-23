import paramiko
import os
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
ssh.connect("192.168.2.219", port=22, username="root", password="nokia123",timeout=5000)
stdin, stdout, stderr = ssh.exec_command("ls")
opt = stdout.readlines()
opt = "".join(opt)
print(opt)
list_of_files = glob.glob('/home/stack/healthchecksbyomar/*')
latest_file = max(list_of_files, key=os.path.getctime)
print latest_file
#copy files from remote host to local host
ftp_client=ssh.open_sftp()
#ftp_client.get('/home/stack/healthchecksbyomar/hchkomar_20200322','/home/stack/hchkomar_20200322')
ftp_client.close()
