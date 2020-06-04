from devito.operator.profiling import PerfEntry
from examples.seismic.tti.tti_example import tti_setup

from thematrix.common import check_norms, run_prepare, run_benchmark


class TTIAcousticForward(object):

    # Problem setup
    params = ([(350, 350, 350)], [12], [{'rec': 17.805016, 'u': 29.331156, 'v': 29.331171}])
    param_names = ['shape', 'space_order', 'norms']
    tn = 50

    # ASV parameters
    repeat = 1
    timeout = 900.0
    processes = 1

    def setup(self, shape, space_order, norms):
        fn_perf, fn_norms = run_prepare('acoustic-tti', shape, space_order)
        try:
            with open(fn_perf, 'r') as f:
                self.summary = eval(f.read())
        except FileNotFoundError:
            run_benchmark('tti', shape, space_order, self.tn, fn_perf, fn_norms)
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


class TTIAcousticAdjoint(object):

    # Problem setup
    params = ([(350, 350, 350)], [12], [{'srca': 1588.117065, 'p': 568135.687500, 'r': 620591.500000}])
    param_names = ['shape', 'space_order', 'norms']
    tn = 100

    # ASV parameters
    repeat = 1
    timeout = 900.0
    processes = 1

    def setup(self, shape, space_order, norms):
        fn_perf, fn_norms = run_prepare('acoustic-ttia', shape, space_order)
        try:
            with open(fn_perf, 'r') as f:
                self.summary = eval(f.read())
        except FileNotFoundError:
            run_benchmark('tti', shape, space_order, self.tn, fn_perf, fn_norms, op="adjoint")
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

