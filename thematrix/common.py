from devito import info, norm
from devito.types.dense import DiscreteFunction

def check_norms(functions, reference):
    assert len(functions) == len(reference)

    for i in functions:
        if isinstance(i, DiscreteFunction):
            v = norm(i)
            info("norm(%s) = %f (expected = %f, delta = %f)"
                 % (i.name, v, reference[i.name], abs(v - reference[i.name])))
