from dwave.cloud import Client
client = Client.from_config(token='DEV-c7a62b6fb390e91e63c6ac2a7f8450fa50a6d09d')
print client.get_solvers()
