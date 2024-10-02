# import os
# '''работает но не пишет'''
# ip = '192.168.0.1' # нужный айпи
# ping_file = 'main2.txt'
# response = os.popen(f'ping {ip} > "{ping_file}"').read()
# with open(ping_file, 'r', encoding='cp866') as file:
#     ping = file.read()
#
# print(ping)


import os
result_file = open("result.txt", "a+")
ip_list = []
for ip in range(1, 256):
    ip_list.append("192.168.1." + str(ip))
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 1" and "Approximate" in response:
        result_file.write(f"UP {ip} Ping Successful" + "\n")
        print(f'{response}')
    else:
        result_file.write(f"DOWN {ip} Ping UnSuccessful" + "\n")
        print(f'{response}')
result_file.close()
# with open("result.txt", "r") as file:
#     for ip in park:
#     lineread = file.read()
#     print(" {park}  \n")


#     park = file.read()
#     park = park.splitlines()
#     print(" {park}  \n")
#
#
#
# with open("ip_list.txt") as file:
#     park = file.read()
#     park = park.splitlines()
#     print(" {park}  \n")
#     # ping for each ip in the file
# for ip in park:
#     response = os.popen(f"ping -c 4 {ip} ").read()
#     # Pinging each IP address 4 times
#
#     # saving some ping output details to output file
#     if ("Request timed out." or "unreachable") in response:
#         print(response)
#         f = open("main2.txt", "a")
#         f.write(str(ip) + ' link is down' + '\n')
#         f.close()
#     else:
#         print(response)
#         f = open("main2.txt", "a")
#         f.write(str(ip) + ' is up ' + '\n')
#         f.close()
#         # print output file to screen
# with open("main2.txt") as file:
#     output = file.read()
#     f.close()
#     print(output)
# with open("main2.txt", "w") as file:
#     pass