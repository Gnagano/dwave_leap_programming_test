import dwavebinarycsp
import dwavebinarycsp.factories.constraint.gates as gates

csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(gates.and_gate(['x1','x2','y1']))
bqm = dwavebinarycsp.stitch(csp)
print bqm
