import paramiko
import time
from datafile import *
import re

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(c_host, c_port, c_username, c_password)
time.sleep(5)
print('Connected to Machine\n')

stdin, stdout, stderr = ssh.exec_command(getnodes, get_pty=True)
nodes=stdout.readlines()

finallist=[]
finalhost=[]
for i in range(0,16):
	cnode=nodes[i].split(':')
	node=cnode[0].split()
	nnode=node[0]

	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sshpass -p 'root' ssh "+nnode, get_pty=True)
	ssh_stdin.write(getips)
	ssh_stdin.write('exit\n')
	ssh_stdin.flush()
	output=ssh_stdout.readlines()
	iplist=[]
	for i in range(5,len(output)-3):
		out=output[i]
		ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
		ip=ansi_escape.sub('', out).strip()
		iplist.append(ip)
		hostip=[x for x in iplist if x.startswith('10')]
	finalhost.append(hostip)
	finallist.append(iplist)

scanip=[]
for x in range(0,16):
	flist=finallist[x]
	scanip=scanip+flist
scanip=list(dict.fromkeys(scanip))
loginip=finalhost[0]

def eIPScan():
	for ips in scanip:
		print("\nRunning IP Scan- "+ips)
		host=loginip[0]
		ssh.connect(host,c_port,c_username,c_password)
		stdin, stdout, stderr = ssh.exec_command("mkdir "+csd_ip_folder, get_pty=True)
		stdin, stdout, stderr = ssh.exec_command("cd "+csd_ip_folder+" && nmap -sO -p- -Pn -vvv --reason --webxml -oA CSD_IP_SCAN_"+ips+" "+ips)
		conn=stdout.readlines()
		print(conn)
		print("\nip-"+ips+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+csd_ip_folder+'/CSD_IP_SCAN_'+ips+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_ip_folder+'/CSD_IP_SCAN_'+ips+'.xml')
		ftp_client.get('/root/'+csd_ip_folder+'/CSD_IP_SCAN_'+ips+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_ip_folder+'/CSD_IP_SCAN_'+ips+'.nmap')
		ftp_client.get('/root/'+csd_ip_folder+'/CSD_IP_SCAN_'+ips+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_ip_folder+'/CSD_IP_SCAN_'+ips+'.gnmap')

def eTCPScan():
	for ips in scanip:
		print("\nRunning TCP Scan- "+ips)
		host=loginip[0]
		ssh.connect(host,c_port,c_username,c_password)
		stdin, stdout, stderr = ssh.exec_command("mkdir "+csd_tcp_folder, get_pty=True)
		stdin, stdout, stderr = ssh.exec_command("cd "+csd_tcp_folder+" && nmap -sS -sV -p- -Pn -vvv --reason --webxml -oA CSD_TCP_SCAN_"+ips+" "+ips)
		conn=stdout.readlines()
		print(conn)
		print("\nip-"+ips+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+csd_tcp_folder+'/CSD_TCP_SCAN_'+ips+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_tcp_folder+'/CSD_TCP_SCAN_'+ips+'.xml')
		ftp_client.get('/root/'+csd_tcp_folder+'/CSD_TCP_SCAN_'+ips+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_tcp_folder+'/CSD_TCP_SCAN_'+ips+'.nmap')
		ftp_client.get('/root/'+csd_tcp_folder+'/CSD_TCP_SCAN_'+ips+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_tcp_folder+'/CSD_TCP_SCAN_'+ips+'.gnmap')

def eSCTPScan():
	for ips in scanip:
		print("\nRunning SCTP Scan- "+ips)
		host=loginip[0]
		ssh.connect(host,c_port,c_username,c_password)
		stdin, stdout, stderr = ssh.exec_command("mkdir "+csd_sctp_folder, get_pty=True)
		stdin, stdout, stderr = ssh.exec_command("cd "+csd_sctp_folder+" && nmap -sY -sV -p- -Pn -vvv --reason --webxml -oA CSD_SCTP_SCAN_"+ips+" "+ips)
		conn=stdout.readlines()
		print(conn)
		print("\nip-"+ips+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+csd_sctp_folder+'/CSD_SCTP_SCAN_'+ips+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_sctp_folder+'/CSD_SCTP_SCAN_'+ips+'.xml')
		ftp_client.get('/root/'+csd_sctp_folder+'/CSD_SCTP_SCAN_'+ips+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_sctp_folder+'/CSD_SCTP_SCAN_'+ips+'.nmap')
		ftp_client.get('/root/'+csd_sctp_folder+'/CSD_SCTP_SCAN_'+ips+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_sctp_folder+'/CSD_SCTP_SCAN_'+ips+'.gnmap')

def eUDPScan():
	for ips in scanip:
		print("\nRunning UDP Scan- "+ips)
		host=loginip[0]
		ssh.connect(host,c_port,c_username,c_password)
		stdin, stdout, stderr = ssh.exec_command("mkdir "+csd_udp_folder, get_pty=True)
		stdin, stdout, stderr = ssh.exec_command("cd "+csd_udp_folder+" && nmap -sU -sV -p- -Pn --max-retries 1 --version-intensity 0 --min-hostgroup 32 --max-scan-delay 10ms -vvv --reason --webxml -oA CSD_UDP_SCAN_"+ips+" "+ips)
		conn=stdout.readlines()
		print(conn)
		print("\nip-"+ips+" Completed\n")
		print("Extracting Results\n")
		ftp_client=ssh.open_sftp()
		ftp_client.get('/root/'+csd_udp_folder+'/CSD_UDP_SCAN_'+ips+'.xml', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_udp_folder+'/CSD_UDP_SCAN_'+ips+'.xml')
		ftp_client.get('/root/'+csd_udp_folder+'/CSD_UDP_SCAN_'+ips+'.nmap', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_udp_folder+'/CSD_UDP_SCAN_'+ips+'.nmap')
		ftp_client.get('/root/'+csd_udp_folder+'/CSD_UDP_SCAN_'+ips+'.gnmap', 'C:/Users/yogeshku/Desktop/Scan Results/CSD/'+csd_udp_folder+'/CSD_UDP_SCAN_'+ips+'.gnmap')

eIPScan()
eTCPScan()
eSCTPScan()
eUDPScan()