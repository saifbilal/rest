import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
ssh.connect("192.168.2.219", port=22, username="root", password="nokia123",timeout=5000)
stdin, stdout, stderr = ssh.exec_command("ls")
opt = stdout.readlines()
opt = "".join(opt)
print(opt)