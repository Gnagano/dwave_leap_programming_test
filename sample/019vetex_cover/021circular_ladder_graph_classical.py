import networkx       as nx
import dwave_networkx as dnx
from dimod.reference.samplers import ExactSolver

sampler = ExactSolver()
c5 = nx.circular_ladder_graph(5)
print(dnx.min_vertex_cover(c5,sampler))
