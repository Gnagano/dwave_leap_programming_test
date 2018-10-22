import os,sys
sys.path.append(os.path.dirname(os.pardir))

from config import account
from config import config
import networkx       as nx
import dwave_networkx as dnx

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler(
    endpoint = config.API_ENDPOINT,
    token    = account.LEAP_API_TOKEN,
    solver   = config.SOLVER_NAME))

w5 = nx.wheel_graph(5)
w25 = nx.wheel_graph(25)

print(dnx.min_vertex_cover(w5,sampler))
print(dnx.min_vertex_cover(w25,sampler))
