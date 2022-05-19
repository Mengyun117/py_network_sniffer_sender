# �������Ȩ��Mengyun199���У�All Rights Reserved (C) 2022-
#####################################################################################################
# ������hanasaki-workstation
# ��¼�û���Mengyun Jia
# �������ƣ�hanasaki-workstation
# ��ϵ�����䣺jiamengyun1024@outlook.com
#####################################################################################################
# ������ݣ�2022
# �����ˣ�Mengyun Jia
#####################################################################################################

from scapy.all import *

class MyEth(Packet):
    name="MyEther"
    fields_desc=[DestMACField("dst"),
                 SourceMACField("src"),
                 XShortEnumField("type",0x0800,ETHER_TYPES),
                 IntEnumField("donald" , 1 ,{ 1: "ETH1", 2: "ETH2" , 3: "ETH3" } )]

class MyUDP(Packet):
    name = "MyUDP"
    fields_desc = [ShortEnumField("sport", 53, UDP_SERVICES),
                   ShortEnumField("dport", 53, UDP_SERVICES),
                   ShortField("len", None),
                   XShortField("chksum", None),
                   IntEnumField("donald" , 1 ,{ 1: "UDP1", 2: "UDP2" , 3: "UDP3" } )]

class MyTCP(Packet):
    name = "MyTCP"
    fields_desc = [ShortEnumField("sport", 20, TCP_SERVICES),
                   ShortEnumField("dport", 80, TCP_SERVICES),
                   IntField("seq", 0),
                   IntField("ack", 0),
                   BitField("dataofs", None, 4),
                   BitField("reserved", 0, 3),
                   FlagsField("flags", 0x2, 9, "FSRPAUECN"),
                   ShortField("window", 8192),
                   XShortField("chksum", None),
                   ShortField("urgptr", 0),
                   TCPOptionsField("options", ""),
                   IntEnumField("donald" , 1 ,{ 1: "TCP1", 2: "TCP2" , 3: "TCP3" })]

def eth_editor():		#Ether��̫��MAC֡���ݰ��༭����
	eth_macsrc = input("source mac address: ")
	eth_macdst = input("destination mac address: ")
	type = input("type: ")
	try:		#�쳣�����ֹ�û�����������������
		eth_type = int(type,16)
	except :		#���û�������Ч����ʾ��Ч���ݲ��˳�����
		print("invalid mac address detected\nscript exiting...")
		exit()
	eth_packet = Ether(dst = eth_macdst, src = eth_macsrc, type = eth_type)
	eth_packet.show()
	return eth_packet

def ip_editor():		#IPЭ�����ݰ��༭����
	ip_version = input("ip protocol version: ")
	ip_ihl = input("header length: ")
	ip_tos = input("type od service: ")
	ip_len = input("total length: ")
	ip_id = input("identifier: ")
	ip_flags = input("flags(DF/MF): ")
	ip_frag  = input("fragment offset: ")
	ip_ttl = input("ttl: ")
	ip_src = input("source ip address: ")
	ip_dst = input("destination ip address: ")
	ip_packet = IP(version = ip_version,ihl = ip_ihl,tos = ip_tos,len = ip_len,id = ip_id,flags = ip_flags,frag = ip_frag,ttl = ip_ttl,proto = 6,src = ip_src,dst = ip_dst)
	return ip_packet

def tcp_editor():		#TCPЭ�����ݰ��༭����
	tcp_sport = input("source port: ")
	tcp_dport = input("destination port: ")
	tcp_seq = input("sequence: ")
	tcp_ack = input("acknowledge: ")
	tcp_dataofs = input("data offset: ")
	tcp_reserved = input("reserved: ")
	tcp_flags = input("flags: ")
	tcp_window = input("window: ")
	tcp_urgptr = input("urgent pointer: ")
	tcp_packet = TCP(sport = tcp_sport,dport = tcp_dport,seq = tcp_seq,ack = tcp_ack,dataofs = tcp_dataofs,reserved = tcp_reserved,flags = tcp_flags,window = tcp_window,urgptr = tcp_urgptr)
	return tcp_packet

def udp_editor():		#UDPЭ�����ݰ��༭����
	udp_sport = input("source port: ")
	udp_dport = input("destination port: ")
	udp_len = input("total length: ")
	udp_packet = UDP(sport = udp_sport,dport = udp_dport,len = udp_len)
	return udp_packet


# PROGRAM START HERE
# �û�ѡ��ģʽ�������û����������Э��༭����Э�������
mode = input("select a mode\n1. packet editor\n2. packet sniffer\n\nselection: ")
print("\n")

if mode == '1':		#���ݰ����ͣ�Э��༭����
	type = input("select a protocol\n1. Ether\n2. IP\n3. TCP\n4. UDP\nselection: ")
	print("\n")

	#�����Ѷ���ĺ�������Э��༭�����ݰ�����װ
	if type == '1' :
		packs = eth_editor()

	elif type == '2' :
		packs = (eth_editor()/ip_editor())

	elif type == '3' :
		packs = (eth_editor()/ip_editor()/tcp_editor())

	elif type == '4' :
	    packs = (eth_editor()/ip_editor()/udp_editor())

	else:
		#��Ч����ֱ���˳�����
		print("invalid selection detected\nscript exiting...")
		exit()
	
	#������װ�õ����ݰ�
	sendp(packs)

elif mode == '2':		#���ݰ����񼰷�����Э���������

	#�û�ѡ�񲶻����ݰ�������
	sniff_count = int(input("input number of packets to sniff: "))
	print("\n")

	#�û�ѡ�������
	filter_num = input("select a protocol:\n1. Ether\n2. ARP\n3. IP\n4. TCP\n5. ICMP\n6. UDP\n7. DNS\n\nselection: ")
	print("\n")

	#�����û���ѡ�����ù�����������
	if filter_num == '1':
		sniff_filter = ""

	elif filter_num == '2':
		sniff_filter = "arp"

	elif filter_num == '3':
		sniff_filter = "ip"

	elif filter_num == '4':
		sniff_filter = "tcp"

	elif filter_num == '5':
		sniff_filter = "icmp"

	elif filter_num == '6':
		sniff_filter = "udp"

	elif filter_num == '7':
		sniff_filter = "port 53"

	else:
		#��Ч����ֱ���˳�����
		print("invalid selection detected\nscript exiting...")
		exit()

	#�����ʽ"lambda x:x.summary()"Ϊ������˴��룬Ŀǰ������ԭ��
	packets = sniff(prn = lambda x:x.summary(), count = sniff_count, filter = sniff_filter)

	#���´������������Ѳ�������ݰ�
	while (1):
		#�û�ѡ����Ҫ���������ݰ���ź��¼�ڱ���i�У����û�����0���˳�
		i=int(input("select a packet to analyze(input a number, 0 to cancel): "))

		if i == 0:
			#�û�����0��ʾ�û����˳��ű�ִ��
			print("user exit operation detected\nscript exiting...")
			exit()

		#��ʾ������Ӧ��ŵ����ݰ�����
		packets[i-1].show()

else:
	#��Ч����ֱ���˳�����
	print("invalid selection detected\nscript exiting...")
	exit()

