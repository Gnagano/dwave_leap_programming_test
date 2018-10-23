import os,sys
sys.path.append(os.path.dirname(os.pardir))

from config import account
from dwave.cloud import Client

client = Client.from_config(token=account.LEAP_API_TOKEN)
print client.get_solvers()
