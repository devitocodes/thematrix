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

with open('../thematrix/thematrix.json', 'r') as f:
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

with open('~/.asv-machine.json', 'w') as f:
    json.dump(output, f, indent=4)


# Generate jobs.json

runners = data['runners'].keys()
rdata = data['runners']

jobs_list = []
for i in runners:
    os = rdata[i]['os']
    tags = rdata[i]['tags']
    arch = rdata[i]['arch']
    cpu = rdata[i]['cpu']
    jobs = rdata[i]['jobs'].keys()
    jdat = rdata[i]['jobs']
    for j in jobs:
        name = j
        num_cpu = jdat[j]['num_cpu']
        ram = jdat[j]['ram']
        num_procs = jdat[j]['num_procs']
        num_threads = jdat[j]['num_threads']
        jit = jdat[j]['jit']
        language = jdat[j]['language']
        omp_places = jdat[j]['omp_places']
        omp_proc_bind = jdat[j]['omp_proc_bind']
        # Build dict
        job_dict = {}
        job_dict['name'] = name
        job_dict['tags'] = tags
        job_dict['os'] = os
        job_dict['arch'] = arch
        job_dict['cpu'] = cpu
        job_dict['num_cpu'] = num_cpu
        job_dict['ram'] = ram
        job_dict['num_procs'] = num_procs
        job_dict['num_threads'] = num_threads
        job_dict['jit'] = jit
        job_dict['language'] = language
        job_dict['omp_places'] = omp_places
        job_dict['omp_proc_bind'] = omp_proc_bind
        jobs_list.append(job_dict)

output = {"include": jobs_list}

with open('jobs.json', 'w') as f:
    json.dump(output, f, indent=4)


# Generate runners.json

output = {"include": [{"runner": i} for i in runners]}

with open('runners.json', 'w') as f:
    json.dump(output, f, indent=4)
