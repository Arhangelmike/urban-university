import socket
from datetime import datetime
import sys
start = datetime.now()
# словарь из пар: порт и название порта
ports = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
    115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP",
    179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
    514: "SYSLOG", 515: "PRINTER", 993: "IMAPS",
    995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
    1433: "SQL Server", 1723: "PPTP", 3128: "HTTP",
    3268: "LDAP", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin" }
# ip адрес
host_name = '45.33.32.156'
ip = socket.gethostbyname(host_name)
# распечатаем имя сайта по его ip адресу
hostname1 = socket.gethostbyaddr(ip)[0]
print(hostname1)


# в цикле обойдем все порты из списка и проверим возможность подключения к ним.
# Если порт закрыт, будет вызываться исключение, которое мы перехватим, и программа не вылетит.
for port in ports:
    cont = socket.socket()
    cont.settimeout(1)
    try:
        cont.connect((ip, port))
        s1 = socket.create_connection((ip, port), timeout=5)
        print(s1)
    except socket.error as error1:
        print(error1)
    else:
        print(f"{socket.gethostbyname(ip)}:{str(port)} is open/{ports[port]}")
        cont.close()
ends = datetime.now()
print("<Time:{}>".format(ends - start))
input("Press Enter to the exit....")


