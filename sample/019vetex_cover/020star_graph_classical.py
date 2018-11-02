import networkx       as nx
import dwave_networkx as dnx
from dimod.reference.samplers import ExactSolver

sampler = ExactSolver()
s5 = nx.star_graph(4)
print(dnx.min_vertex_cover(s5,sampler))
