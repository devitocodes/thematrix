from examples.seismic.acoustic.acoustic_example import acoustic_setup

from thematrix.benchmarks.common import check_norms


class IsotropicAcoustic(object):

    params = ([(492, 492, 492)], [12], [{'rec': 184.526400, 'u': 151.545837}])
    param_names = ['shape', 'space_order', 'norms']

    nbl = 10
    tn = 100

    repeat = 3

    timeout = 600.0

    # Default shape for loop blocking
    x0_blk0_size = 16
    y0_blk0_size = 16

    def setup(self, shape, space_order):
        self.solver = acoustic_setup(shape=shape, space_order=space_order,
                                     opt=('advanced', {'openmp': True}))

    def time_forward(self, shape, space_order):
        rec, u, summary = self.solver.forward(x0_blk0_size=self.x0_blk0_size,
                                              y0_blk0_size=self.y0_blk0_size)

        # Compare output against reference norms
        check_norms(rec, u)
