from usos_api.api_secrets import secret, key
from usos_api.usosapi import USOSAPIConnection

connection = USOSAPIConnection(api_base_address='https://apps.usos.pwr.edu.pl/',
                               consumer_key=key,
                               consumer_secret=secret)
connection_url = connection.get_authorization_url()
open(connection_url)
pin = input()
