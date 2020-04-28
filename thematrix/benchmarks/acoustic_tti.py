from devito import switchconfig
from examples.seismic.tti.tti_example import tti_setup

from thematrix.benchmarks.common import check_norms


class TTIAcoustic(object):

    params = ([(350, 350, 350)], [12], [{'rec': 66.417102, 'u': 30.707737, 'v': 30.707728}])
    param_names = ['shape', 'space_order', 'norms']

    tn = 50

    repeat = 1

    timeout = 600.0

    # Default shape for loop blocking
    x0_blk0_size = 16
    y0_blk0_size = 16

    @switchconfig(profiling='advanced')
    def setup(self, shape, space_order, norms):
        solver = tti_setup(shape=shape, space_order=space_order, tn=self.tn,
                           opt=('advanced', {'openmp': True}))
        rec, u, v, self.summary = solver.forward(x0_blk0_size=self.x0_blk0_size,
                                                 y0_blk0_size=self.y0_blk0_size)

        # Compare output against reference norms
        check_norms([rec, u, v], norms)

    def track_runtime(self, shape, space_order, norms):
        return self.summary.globals['fdlike'].time
    track_runtime.unit = "runtime"

    def track_gflopss(self, shape, space_order, norms):
        return self.summary.globals['fdlike'].gflopss
    track_gflopss.unit = "gflopss"

    def track_gpointss(self, shape, space_order, norms):
        return self.summary.globals['fdlike'].gpointss
    track_gpointss.unit = "gpointss"
