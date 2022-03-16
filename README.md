This is an AbuseIPDB & Shodan API's based scripts to get organization users not from corporate OpenVPN server country.
Prerequisites:

1.pip3 install shodan;

2.get Shodan [free] API key;

3.get AbuseIPDB [free] API key.

One should substitute "/PATH_TO_OPENVPN_LOG_FILE" in lines 9 and 44, "YOUR_ABUSEIPDB_API_KEY" in line 29 for actual ones in get_targetted_users.py.
One should substitute "/PATH_TO_OPENVPN_LOG_FILE" in lines 9 and 44, "YOUR_ABUSEIPDB_API_KEY" in line 29, YOUR_SHODAN_API_KEY in line 8 for actual ones in get_targetted_users_enhanced.py.
One should substitute "US" in line 35 for desired value.
Besides one should keep in mind that it's important to know how many lines and what lines one should remove from openvpn log file output. In line 9 "standard" output is formatted.
