import os,sys
dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.normpath(os.path.join(dir,'../../'))
sys.path.append(root)

from config import account
from dwave.cloud import Client

client = Client.from_config(token=account.LEAP_API_TOKEN)
print client.get_solvers()
