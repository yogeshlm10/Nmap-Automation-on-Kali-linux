import paramiko
import time
import re
from datafile import *

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(v_host, v_port, v_username, v_password)
time.sleep(5)
print('Connected to Machine\n')

stdin, stdout, stderr = ssh.exec_command("mkdir "+vi_storage_folder)

stdin, stdout, stderr = ssh.exec_command(v_get_nodes)
node2=stdout.readlines()
node2 = list(dict.fromkeys(node2))
for i in range(len(node2)):
		cnode=node2[i].split(':')
		bmnode2=cnode[1].strip()
		print(bmnode2)

def IPScan():
	for i in range(len(node2)):
		cnode=node2[i].split(':')
		bmnode2=cnode[1].strip()
		print(bmnode2)
		print("Running IP Scan-"+bmnode2)
		stdin, stdout, stderr = ssh.exec_command("cd "+vi_storage_folder+" && nmap -sO -p- -Pn -vvv --reason --webxml -oA VI_IP_SCAN_"+bmnode2+" "+bmnode2)
		version=stdout.readlines()
		print(version)
		print("\nip-"+bmnode2+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+vi_storage_folder+'/VI_IP_SCAN_'+bmnode2+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_IP_SCAN_'+bmnode2+'.xml')
		ftp_client.get('/root/'+vi_storage_folder+'/VI_IP_SCAN_'+bmnode2+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_IP_SCAN_'+bmnode2+'.nmap')
		ftp_client.get('/root/'+vi_storage_folder+'/VI_IP_SCAN_'+bmnode2+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_IP_SCAN_'+bmnode2+'.gnmap')

def TCPScan():
	for i in range(len(node2)):
		cnode=node2[i].split(':')
		bmnode2=cnode[1].strip()
		print(bmnode2)
		print("Running TCP Scan-"+bmnode2)
		stdin, stdout, stderr = ssh.exec_command("cd "+vi_storage_folder+" && nmap -sS -sV -p- -Pn -vvv --reason --webxml -oA VI_TCP_SCAN_"+bmnode2+" "+bmnode2)
		version=stdout.readlines()
		print(version)
		print("\nip-"+bmnode2+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+vi_storage_folder+'/VI_TCP_SCAN_'+bmnode2+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_TCP_SCAN_'+bmnode2+'.xml')
		ftp_client.get('/root/'+vi_storage_folder+'/VI_TCP_SCAN_'+bmnode2+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_TCP_SCAN_'+bmnode2+'.nmap')
		ftp_client.get('/root/'+vi_storage_folder+'/VI_TCP_SCAN_'+bmnode2+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_TCP_SCAN_'+bmnode2+'.gnmap')

def SCTPScan():
	for i in range(len(node2)):
		cnode=node2[i].split(':')
		bmnode2=cnode[1].strip()
		print(bmnode2)
		print("Running SCTP Scan-"+bmnode2)
		stdin, stdout, stderr = ssh.exec_command("cd "+vi_storage_folder+" && nmap -sY -sV -p- -Pn -vvv --reason --webxml -oA VI_SCTP_SCAN_"+bmnode2+" "+bmnode2)
		version=stdout.readlines()
		print(version)
		print("\nip-"+bmnode2+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+vi_storage_folder+'/VI_SCTP_SCAN_'+bmnode2+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_SCTP_SCAN_'+bmnode2+'.xml')
		ftp_client.get('/root/'+vi_storage_folder+'/VI_SCTP_SCAN_'+bmnode2+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_SCTP_SCAN_'+bmnode2+'.nmap')
		ftp_client.get('/root/'+vi_storage_folder+'/VI_SCTP_SCAN_'+bmnode2+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_SCTP_SCAN_'+bmnode2+'.gnmap')

def UDPScan():
	for i in range(len(node2)):
		cnode=node2[i].split(':')
		bmnode2=cnode[1].strip()
		print(bmnode2)
		print("Running UDP Scan-"+bmnode2)
		stdin, stdout, stderr = ssh.exec_command("cd "+vi_storage_folder+" && nmap -sU -sV -p- -Pn --max-retries 1 --version-intensity 0 --min-hostgroup 32 --max-scan-delay 10ms -vvv --reason --webxml -oA VI_UDP_SCAN_"+bmnode2+" "+bmnode2)
		version=stdout.readlines()
		print(version)
		print("\nip-"+bmnode2+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+vi_storage_folder+'/VI_UDP_SCAN_'+bmnode2+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_UDP_SCAN_'+bmnode2+'.xml')
		ftp_client.get('/root/'+vi_storage_folder+'/VI_UDP_SCAN_'+bmnode2+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_UDP_SCAN_'+bmnode2+'.nmap')
		ftp_client.get('/root/'+vi_storage_folder+'/VI_UDP_SCAN_'+bmnode2+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+vi_storage_folder+'/VI_UDP_SCAN_'+bmnode2+'.gnmap')

IPScan()
TCPScan()
SCTPScan()
UDPScan()