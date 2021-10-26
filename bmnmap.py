import paramiko
import time
import os
from datafile import *

def check():
	path = 'C:/Users/yogeshku/Downloads'
	os.chdir(path)
	files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
	newest = files[-1]
	print (newest)

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(b_host, b_port, b_username, b_password)
	time.sleep(5)
	print('Connected to Machine\n')

	def checknmap():
		stdin, stdout, stderr = ssh.exec_command(check_nmap)
		nmap_check=stdout.readlines()
		line=['Nmap']

		if line in nmap_check:
			print('Found')
		else:
			ftp_client=ssh.open_sftp()
			ftp_client.put(nmap_local_folder+newest, nmap_root_folder+newest)
			stdin, stdout, stderr = ssh.exec_command(uninstall_nmap)
			stdin, stdout, stderr = ssh.exec_command(nmap_install_code+newest)
			version=stdout.readlines()
			print(version)
	checknmap()

check()