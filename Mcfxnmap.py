import paramiko
import time
import re
from datafile import *

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(m_host, m_port, m_username, m_password)
time.sleep(5)
print('Connected to Machine\n')

stdin, stdout, stderr = ssh.exec_command(m_get_nodes)
node=stdout.readlines()

def McfxScan():
	#for i in range(1,len(node)):
	nodes=node[1].split()
	ips=nodes[5]

	print("\nRunning IP Scan- "+ips)
	stdin, stdout, stderr = ssh.exec_command("mkdir "+mcfx_ip_folder, get_pty=True)
	stdin, stdout, stderr = ssh.exec_command("cd "+mcfx_ip_folder+" && nmap -sO -p- -Pn -vvv --reason --webxml -oA MCFX_IP_SCAN_"+ips+" "+ips)
	conn=stdout.readlines()
	print(conn)
	print("\nip-"+ips+" Completed\n")
	print("Extracting Results\n")
	ftp_client=ssh.open_sftp()
	ftp_client.get('/root/'+mcfx_ip_folder+'/MCFX_IP_SCAN_'+ips+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_ip_folder+'/MCFX_IP_SCAN_'+ips+'.xml')
	ftp_client.get('/root/'+mcfx_ip_folder+'/MCFX_IP_SCAN_'+ips+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_ip_folder+'/MCFX_IP_SCAN_'+ips+'.nmap')
	ftp_client.get('/root/'+mcfx_ip_folder+'/MCFX_IP_SCAN_'+ips+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_ip_folder+'/MCFX_IP_SCAN_'+ips+'.gnmap')

	print("\nRunning TCP Scan- "+ips)
	stdin, stdout, stderr = ssh.exec_command("mkdir "+mcfx_tcp_folder, get_pty=True)
	stdin, stdout, stderr = ssh.exec_command("cd "+mcfx_tcp_folder+" && nmap -sS -sV -p- -Pn -vvv --reason --webxml -oA MCFX_TCP_SCAN_"+ips+" "+ips)
	conn=stdout.readlines()
	print(conn)
	print("\nip-"+ips+" Completed\n")
	print("Extracting Results\n")
	ftp_client=ssh.open_sftp()
	ftp_client.get('/root/'+mcfx_tcp_folder+'/MCFX_TCP_SCAN_'+ips+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_tcp_folder+'/MCFX_TCP_SCAN_'+ips+'.xml')
	ftp_client.get('/root/'+mcfx_tcp_folder+'/MCFX_TCP_SCAN_'+ips+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_tcp_folder+'/MCFX_TCP_SCAN_'+ips+'.nmap')
	ftp_client.get('/root/'+mcfx_tcp_folder+'/MCFX_TCP_SCAN_'+ips+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_tcp_folder+'/MCFX_TCP_SCAN_'+ips+'.gnmap')

	print("\nRunning SCTP Scan- "+ips)
	stdin, stdout, stderr = ssh.exec_command("mkdir "+mcfx_sctp_folder, get_pty=True)
	stdin, stdout, stderr = ssh.exec_command("cd "+mcfx_sctp_folder+" && nmap -sY -sV -p- -Pn -vvv --reason --webxml -oA MCFX_SCTP_SCAN_"+ips+" "+ips)
	conn=stdout.readlines()
	print(conn)
	print("\nip-"+ips+" Completed\n")
	print("Extracting Results\n")
	ftp_client=ssh.open_sftp()
	ftp_client.get('/root/'+mcfx_sctp_folder+'/MCFX_SCTP_SCAN_'+ips+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_sctp_folder+'/MCFX_SCTP_SCAN_'+ips+'.xml')
	ftp_client.get('/root/'+mcfx_sctp_folder+'/MCFX_SCTP_SCAN_'+ips+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_sctp_folder+'/MCFX_SCTP_SCAN_'+ips+'.nmap')
	ftp_client.get('/root/'+mcfx_sctp_folder+'/MCFX_SCTP_SCAN_'+ips+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_sctp_folder+'/MCFX_SCTP_SCAN_'+ips+'.gnmap')

	print("\nRunning UDP Scan- "+ips)
	stdin, stdout, stderr = ssh.exec_command("mkdir "+mcfx_udp_folder, get_pty=True)
	stdin, stdout, stderr = ssh.exec_command("cd "+mcfx_udp_folder+" && nmap -sU -sV -p- -Pn --max-retries 1 --version-intensity 0 --min-hostgroup 32 --max-scan-delay 10ms -vvv --reason --webxml -oA MCFX_UDP_SCAN_"+ips+" "+ips)
	conn=stdout.readlines()
	print(conn)
	print("\nip-"+ips+" Completed\n")
	print("Extracting Results\n")
	ftp_client=ssh.open_sftp()
	ftp_client.get('/root/'+mcfx_udp_folder+'/MCFX_UDP_SCAN_'+ips+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_udp_folder+'/MCFX_UDP_SCAN_'+ips+'.xml')
	ftp_client.get('/root/'+mcfx_udp_folder+'/MCFX_UDP_SCAN_'+ips+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_udp_folder+'/MCFX_UDP_SCAN_'+ips+'.nmap')
	ftp_client.get('/root/'+mcfx_udp_folder+'/MCFX_UDP_SCAN_'+ips+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/MCFX/'+mcfx_udp_folder+'/MCFX_UDP_SCAN_'+ips+'.gnmap')

McfxScan()