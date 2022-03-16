import os
import requests
import json

conns_list = []
IPs_list = []

os.system("shodan init YOUR_SHODAN_API_KEY")
os.system(
    "cat /PATH_TO_OPENVPN_LOG_FILE | awk '{print $1}' | head -n -3 | tail -n +4 | sed 's/ROUTING//;s/Virtual//' | sed '/^$/d' > /tmp/not_ru_users.txt"
)

print("\033[1;90mSearching...\033[1;00m")
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
    headers = {'Accept': 'application/json', 'Key': 'YOUR_ABUSEIPDB_API_KEY'}
    response = requests.request(method='GET',
                                url=url,
                                headers=headers,
                                params=querystring)

    decodedResponse = json.loads(response.text)
    if decodedResponse['data']['countryCode'] != 'RU':
        print("\033[1;91m")
        print(
            json.dumps(decodedResponse['data']['ipAddress'],
                       sort_keys=True,
                       indent=4), "\033[1;00m")
        target_IP = decodedResponse['data']['ipAddress']
        os.system(
            "grep {} /PATH_TO_OPENVPN_LOG_FILE | head -n 1".format(target_IP))
        print("\033[1;95mAbuseIPDB \033[1;94mIP info: \033[1;00m")
        print(json.dumps(decodedResponse['data'], sort_keys=True, indent=4))
        print("\033[1;93mShodan \033[1;94mIP info: \033[1;00m")
        os.system("shodan host {}".format(target_IP))


for line in IPs_list:
    get_IP_info(line)

os.system('rm /tmp/not_ru_users.txt')

