import os
from tempfile import gettempdir

from devito import switchconfig, __version__ as devito_version
from devito.operator.profiling import PerfEntry
from examples.seismic.acoustic.acoustic_example import acoustic_setup

from thematrix.benchmarks.common import check_norms


class IsotropicAcoustic(object):

    # Problem setup
    params = ([(492, 492, 492)], [12], [{'rec': 184.526400, 'u': 151.545837}])
    param_names = ['shape', 'space_order', 'norms']
    tn = 100

    # ASV parameters
    repeat = 1
    timeout = 600.0
    processes = 1

    # Default shape for loop blocking
    x0_blk0_size = 16
    y0_blk0_size = 16

    @switchconfig(profiling='advanced')
    def setup(self, shape, space_order, norms):
        filename = 'acoustic_iso_shape%s_so%d_devito%s.asv' % (str(shape).replace(" ", ""),
                                                               space_order,
                                                               devito_version.split('.')[1])
        filename = os.path.join(gettempdir(), filename)

        try:
            with open(filename, 'r') as f:
                self.summary = eval(f.read())
        except FileNotFoundError:
            solver = acoustic_setup(shape=shape, space_order=space_order, tn=self.tn,
                                    opt=('advanced', {'openmp': True}))
            rec, u, summary = solver.forward(x0_blk0_size=self.x0_blk0_size,
                                             y0_blk0_size=self.y0_blk0_size)
            self.summary = summary.globals['fdlike']

            # Compare output against reference norms
            check_norms([rec, u], norms)

            # Custom caching -- ASV's setup_cache won't work
            with open(filename, 'w') as f:
                f.write(str(self.summary))

    def track_runtime(self, shape, space_order, norms):
        return self.summary.time
    track_runtime.unit = "runtime"

    def track_gflopss(self, shape, space_order, norms):
        return self.summary.gflopss
    track_gflopss.unit = "gflopss"

    def track_gpointss(self, shape, space_order, norms):
        return self.summary.gpointss
    track_gpointss.unit = "gpointss"
