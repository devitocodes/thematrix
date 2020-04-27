from examples.seismic.tti.tti_example import tti_setup

from thematrix.benchmarks.common import check_norms


class TTIAcoustic(object):

    params = ([(350, 350, 350)], [12], [{'rec': 66.417102, 'u': 30.707737, 'v': 30.707728}])
    param_names = ['shape', 'space_order', 'norms']

    nbl = 10
    tn = 50

    repeat = 1

    timeout = 600.0

    # Default shape for loop blocking
    x0_blk0_size = 16
    y0_blk0_size = 16

    def setup(self, shape, space_order, norms):
        self.solver = tti_setup(shape=shape, space_order=space_order,
                                opt=('advanced', {'openmp': True}))

    def time_forward(self, shape, space_order, norms):
        rec, u, v, summary = self.solver.forward(x0_blk0_size=self.x0_blk0_size,
                                                 y0_blk0_size=self.y0_blk0_size)

        # Compare output against reference norms
        check_norms(rec, u, v)
