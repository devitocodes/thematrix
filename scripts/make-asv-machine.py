import json
import sys

if len(sys.argv) != 3:
    print("Usage: python make-asv-machine.py RUNNER JOBNAME")
    sys.exit(1)

runner = sys.argv[1]
jobname = sys.argv[2]

with open('thematrix.json', 'r') as f:
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

with open('.asv-machine.json', 'w') as f:
    json.dump(output, f, indent=4)
