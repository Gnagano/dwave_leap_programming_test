import networkx       as nx
import dwave_networkx as dnx
from dimod.reference.samplers import ExactSolver
import datetime

start = datetime.datetime.now()
print "start time is " + str(start)

sampler = ExactSolver()

# w5 = nx.wheel_graph(5)
# print(dnx.min_vertex_cover(w5,sampler))

w25 = nx.wheel_graph(23)
print(dnx.min_vertex_cover(w25,sampler))

end = datetime.datetime.now()
print "the end time is " + str(end)
print "the calculate time is " + str(end - start)
