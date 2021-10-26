#nmap Checking
nmap_local_folder='C:/Users/yogeshku/Downloads/'
nmap_root_folder='/root/'
nmap_install_code='rpm -ivh '
check_nmap='nmap -version'
uninstall_nmap='rpm -e nmap'

##Connecting to BM Test Bed
b_host='10.53.204.75'
b_port='22'
b_username='root'
b_password='yt_xk39b'
b_get_nodes="cmcli info | grep 'CoreLAN IP'"

##Connecting to VI Test Bed 
v_host='100.70.15.8'
v_port='22'
v_username='root'
v_password='yt_xk39b'
v_get_nodes="cmcli info | grep '100.'"

##Connecting to CSD Test Bed 
c_host='10.43.0.2'
c_port='22'
c_username='root'
c_password='root'
getnodes="kubectl get nodes -n csdci | grep 'ncs'"
getips="ip -4 addr | grep -oP '(?<=inet\s)\d+(\.\d+){3}'\n"

##Connecting to Micro CFX Test Bed
m_host='10.103.111.38'
m_port='22'
m_username='root'
m_password='root'
m_get_nodes="kubectl get pods -n mtb18 -o wide"

##Reports Storage Folder
bm_storage_folder= "BMScans"
vi_storage_folder= "VIScans"

csd_ip_folder= "CSDIP"
csd_tcp_folder= "CSDTCP"
csd_sctp_folder= "CSDSCTP"
csd_udp_folder= "CSDUDP"

mcfx_ip_folder= "MCFX_IP"
mcfx_tcp_folder= "MCFX_TCP"
mcfx_sctp_folder= "MCFX_SCTP"
mcfx_udp_folder= "MCFX_UDP"