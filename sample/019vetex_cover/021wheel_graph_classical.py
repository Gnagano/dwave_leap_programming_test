import networkx       as nx
import dwave_networkx as dnx
from dimod.reference.samplers import ExactSolver

sampler = ExactSolver()
w5 = nx.wheel_graph(5)
print(dnx.min_vertex_cover(w5,sampler))
