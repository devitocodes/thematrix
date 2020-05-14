from devito.operator.profiling import PerfEntry
from examples.seismic.acoustic.acoustic_example import acoustic_setup

from thematrix.common import check_norms, run_prepare, run_benchmark


class IsotropicAcoustic(object):

    # Problem setup
    params = ([(492, 492, 492)], [12], [{'rec': 184.526400, 'u': 151.545837}])
    param_names = ['shape', 'space_order', 'norms']
    tn = 100

    # ASV parameters
    repeat = 1
    timeout = 900.0
    processes = 1

    def setup(self, shape, space_order, norms):
        fn_perf, fn_norms = run_prepare('acoustic-iso', shape, space_order)
        try:
            with open(fn_perf, 'r') as f:
                self.summary = eval(f.read())
        except FileNotFoundError:
            run_benchmark('acoustic', shape, space_order, self.tn, fn_perf, fn_norms)
            check_norms(fn_norms, norms)
            with open(fn_perf, 'r') as f:
                self.summary = eval(f.read())

    def track_runtime(self, shape, space_order, norms):
        return self.summary.time
    track_runtime.unit = "runtime"

    def track_gflopss(self, shape, space_order, norms):
        return self.summary.gflopss
    track_gflopss.unit = "gflopss"

    def track_gpointss(self, shape, space_order, norms):
        return self.summary.gpointss
    track_gpointss.unit = "gpointss"
