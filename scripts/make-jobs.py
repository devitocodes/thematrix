import json

with open('../thematrix/thematrix.json', 'r') as f:
    data = json.load(f)

# Gather the required data
runners = data['runners'].keys()
rdata = data['runners']

# TODO: Tidy up the below mess

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
        jobs_list.append(job_dict)

output = {"include": jobs_list}

with open('jobs.json', 'w') as f:
    json.dump(output, f, indent=4)
