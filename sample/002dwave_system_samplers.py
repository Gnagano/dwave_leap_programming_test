import sys
sys.path.append('..')
from config import account
from dwave.system.samplers import DWaveSampler

sampler = DWaveSampler()
print sampler.parameters
