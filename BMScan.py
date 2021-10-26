import paramiko
import time
import re
from datafile import *

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(b_host, b_port, b_username, b_password)
time.sleep(5)
print('Connected to Machine\n')

stdin, stdout, stderr = ssh.exec_command("mkdir "+bm_storage_folder)

stdin, stdout, stderr = ssh.exec_command(b_get_nodes)
node1=stdout.readlines()

def bIPScan():
	for i in range(len(node1)):
		cnode=node1[i].split(':')
		bmnode1=cnode[1].strip()
		print(bmnode1)
		print("Running IP Scan-"+bmnode1)
		stdin, stdout, stderr = ssh.exec_command("cd "+bm_storage_folder+" && nmap -sO -p- -Pn -vvv --reason --webxml -oA BM_IP_SCAN_"+bmnode1+" "+bmnode1)
		version=stdout.readlines()
		print(version)
		print("\nip-"+bmnode1+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+bm_storage_folder+'/BM_IP_SCAN_'+bmnode1+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_IP_SCAN_'+bmnode1+'.xml')
		ftp_client.get('/root/'+bm_storage_folder+'/BM_IP_SCAN_'+bmnode1+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_IP_SCAN_'+bmnode1+'.nmap')
		ftp_client.get('/root/'+bm_storage_folder+'/BM_IP_SCAN_'+bmnode1+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_IP_SCAN_'+bmnode1+'.gnmap')

def bTCPScan():
	for i in range(len(node1)):
		cnode=node1[i].split(':')
		bmnode1=cnode[1].strip()
		print(bmnode1)
		print("Running TCP Scan-"+bmnode1)
		stdin, stdout, stderr = ssh.exec_command("cd "+bm_storage_folder+" && nmap -sS -sV -p- -Pn -vvv --reason --webxml -oA BM_TCP_SCAN_"+bmnode1+" "+bmnode1)
		version=stdout.readlines()
		print(version)
		print("\nip-"+bmnode1+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+bm_storage_folder+'/BM_TCP_SCAN_'+bmnode1+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_TCP_SCAN_'+bmnode1+'.xml')
		ftp_client.get('/root/'+bm_storage_folder+'/BM_TCP_SCAN_'+bmnode1+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_TCP_SCAN_'+bmnode1+'.nmap')
		ftp_client.get('/root/'+bm_storage_folder+'/BM_TCP_SCAN_'+bmnode1+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_TCP_SCAN_'+bmnode1+'.gnmap')

def bSCTPScan():
	for i in range(len(node1)):
		cnode=node1[i].split(':')
		bmnode1=cnode[1].strip()
		print(bmnode1)
		print("Running SCTP Scan-"+bmnode1)
		stdin, stdout, stderr = ssh.exec_command("cd "+bm_storage_folder+" && nmap -sY -sV -p- -Pn -vvv --reason --webxml -oA BM_SCTP_SCAN_"+bmnode1+" "+bmnode1)
		version=stdout.readlines()
		print(version)
		print("\nip-"+bmnode1+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+bm_storage_folder+'/BM_SCTP_SCAN_'+bmnode1+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_SCTP_SCAN_'+bmnode1+'.xml')
		ftp_client.get('/root/'+bm_storage_folder+'/BM_SCTP_SCAN_'+bmnode1+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_SCTP_SCAN_'+bmnode1+'.nmap')
		ftp_client.get('/root/'+bm_storage_folder+'/BM_SCTP_SCAN_'+bmnode1+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_SCTP_SCAN_'+bmnode1+'.gnmap')

def bUDPScan():
	for i in range(len(node1)):
		cnode=node1[i].split(':')
		bmnode1=cnode[1].strip()
		print(bmnode1)
		print("Running UDP Scan-"+bmnode1)
		stdin, stdout, stderr = ssh.exec_command("cd "+bm_storage_folder+" && nmap -sU -sV -p- -Pn --max-retries 1 --version-intensity 0 --min-hostgroup 32 --max-scan-delay 10ms -vvv --reason --webxml -oA BM_UDP_SCAN_"+bmnode1+" "+bmnode1)
		version=stdout.readlines()
		print(version)
		print("\nip-"+bmnode1+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+bm_storage_folder+'/BM_UDP_SCAN_'+bmnode1+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_UDP_SCAN_'+bmnode1+'.xml')
		ftp_client.get('/root/'+bm_storage_folder+'/BM_UDP_SCAN_'+bmnode1+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_UDP_SCAN_'+bmnode1+'.nmap')
		ftp_client.get('/root/'+bm_storage_folder+'/BM_UDP_SCAN_'+bmnode1+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CFX/'+bm_storage_folder+'/BM_UDP_SCAN_'+bmnode1+'.gnmap')

bIPScan()
bTCPScan()
bSCTPScan()
bUDPScan()



