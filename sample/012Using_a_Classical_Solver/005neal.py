import neal
solver = neal.SimulatedAnnealingSampler()
response = solver.sample_ising(
    {'a': -0.5, 'b': 1.0},
    {('a','b') : -1 },
    num_reads=2
)
print response.data_vectors['energy']
