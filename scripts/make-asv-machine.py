"""Create ``~/.asv-machine.json`` for a given ``<runner, job>``."""

# Example usage
#
#    python make-asv-machine.py matrix-runner-cpu-00 nonHPC-IntelXeon8168-1x1-omp

import json
import sys

if len(sys.argv) != 3:
    print("Usage: python make-asv-machine.py RUNNER JOBNAME")
    sys.exit(1)


# Generate .asv-machine.json

runner = sys.argv[1]
jobname = sys.argv[2]

root_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

with open(os.path.join(root_path, 'thematrix', 'thematrix.json'), 'r') as f:
    data = json.load(f)

arch = data['runners'][runner]['arch']
cpu = data['runners'][runner]['cpu']
machine = jobname
num_cpu = data['runners'][runner]['jobs'][jobname]['num_cpu']
os = data['runners'][runner]['os']
ram = data['runners'][runner]['jobs'][jobname]['ram']

output = {
    machine : {
        'arch': arch,
        'cpu': cpu,
        'machine': machine,
        'num_cpu': num_cpu,
        'os': os,
        'ram': ram
    }
}

# Store in HOME because that's where ASV looks for this file
with open('~/.asv-machine.json', 'w') as f:
    json.dump(output, f, indent=4)
