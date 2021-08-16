import os
import requests
import json

conns_list = []
IPs_list = []

os.system(
    "cat /PATH_TO_OPENVPN_LOG_FILE | awk '{print $1}' | head -n -3 | tail -n +4 | sed 's/ROUTING//;s/Virtual//' | sed '/^$/d' > /tmp/not_ru_users.txt"
)   

with open('/tmp/not_ru_users.txt') as conns:
    for line in conns.readlines():
        conns_list.append(line.split(','))

try:
    for line in conns_list:
        IP = line[1]
        IPs_list.append(IP[0:IP.index(":")])

except (ValueError, IndexError):
    pass


def get_IP_info(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {'ipAddress': ip, 'maxAgeInDays': '90'}

    headers = {
        'Accept':
        'application/json',
        'Key':
        'YOUR_ABUSEIPDB_API_KEY'
    }

    response = requests.request(method='GET',
                                url=url,
                                headers=headers,
                                params=querystring)

    decodedResponse = json.loads(response.text)
    if decodedResponse['data']['countryCode'] != 'RU':
        print("\033[1;91m")
        print(json.dumps(decodedResponse['data']['ipAddress'], sort_keys=True, indent=4),"\033[1;00m")
        not_ru_IP = decodedResponse['data']['ipAddress']
        os.system("grep {} /PATH_TO_OPENVPN_LOG_FILE | head -n 1".format(not_ru_IP))
        print("\033[1;94mIP info: \033[1;00m")
        print(json.dumps(decodedResponse['data'], sort_keys=True, indent=4))
        print("")


for line in IPs_list:
    get_IP_info(line)

os.system('rm /tmp/not_ru_users.txt')

