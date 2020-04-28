from devito import switchconfig
from examples.seismic.acoustic.acoustic_example import acoustic_setup

from thematrix.benchmarks.common import check_norms


class IsotropicAcoustic(object):

    params = ([(492, 492, 492)], [12], [{'rec': 184.526400, 'u': 151.545837}])
    param_names = ['shape', 'space_order', 'norms']

    tn = 100

    repeat = 1

    timeout = 600.0

    # Default shape for loop blocking
    x0_blk0_size = 16
    y0_blk0_size = 16

    @switchconfig(profiling='advanced')
    def setup(self, shape, space_order, norms):
        solver = acoustic_setup(shape=shape, space_order=space_order, tn=self.tn,
                                opt=('advanced', {'openmp': True}))
        rec, u, self.summary = solver.forward(x0_blk0_size=self.x0_blk0_size,
                                              y0_blk0_size=self.y0_blk0_size)

        # Compare output against reference norms
        check_norms([rec, u], norms)

    def track_runtime(self, shape, space_order, norms):
        return self.summary.globals['fdlike'].time
    track_runtime.unit = "runtime"

    def track_gpointss(self, shape, space_order, norms):
        return self.summary.globals['fdlike'].gpointss
    track_gpointss.unit = "gpointss"
