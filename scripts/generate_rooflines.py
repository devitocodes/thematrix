import inspect
from pathlib import Path
import thematrix
import thematrix.acoustic_iso
import thematrix.acoustic_iso_adj
import thematrix.acoustic_iso_jac
import thematrix.acoustic_iso_jacadj
import thematrix.acoustic_iso_ssa
import thematrix.acoustic_iso_ssa_adj
import thematrix.acoustic_iso_ssa_jacadj
import thematrix.acoustic_tti
import thematrix.acoustic_tti_adj
import thematrix.elastic
import thematrix.viscoelastic


def find_all_roofline_methods():
    for name, data in inspect.getmembers(thematrix):
      if name.startswith('__'):
        continue
      print('Looking at: %s' % name)
      for subname, subdata in inspect.getmembers(data, predicate=inspect.isclass):
        if not subname == 'PerfEntry':
          for function_name, _ in inspect.getmembers(subdata, predicate=inspect.isfunction):
            print(function_name)
    

if __name__ == '__main__':
    find_all_roofline_methods()
