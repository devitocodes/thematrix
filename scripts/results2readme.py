""" This script parses repo JSON files to generate summary of
the results in README.md
"""

from string import Template
import pandas as pd
import json
import json2html
from pygit2 import Repository

thematrix_json = "thematrix/thematrix.json"
benchmarks_json = "results/benchmarks.json"

azvm_url = "https://docs.microsoft.com/en-us/azure/virtual-machines/"
matrix_url = "https://www.devitoproject.org/thematrix/"
faq_url = "https://github.com/devitocodes/devito/wiki/FAQ#"

readme_template = Template(open("README-template.md", "r").read())
x_emoji = """
<figure>
<img src="https://github.githubassets.com/images/icons/emoji/unicode/274c.png"
alt="x" width=20ch</img>
</figure>""".replace('\n', "")


def wrap_html_path(filename):
    branch = Repository('.').head.shorthand+"/"
    github_preview = "https://htmlpreview.github.io/?"
    github_url = "https://raw.githubusercontent.com/devitocodes/thematrix/"

    return github_preview + github_url + branch + filename


def ahref(url, txt=""):
    return '<a href="%s">%s</a>' % (url, txt)


def unpack(df, column):
    new_columns = {}
    loc = 0
    for data in df[column]:
        for key in data:
            if key not in new_columns:
                new_columns[key] = [x_emoji for i in range(len(df))]
            new_columns[key][loc] = data[key]
        loc += 1

    for key in new_columns:
        df[key] = new_columns[key]

    del df[column]

    return new_columns.keys()


def convert_json2html(jsonfile):
    html_filename = jsonfile[:-4]+"html"

    data = json.load(open(jsonfile, 'r'))
    html = json2html.json2html.convert(json=data)

    htmlfile = open(html_filename[:-4]+"html", "w")
    htmlfile.write(html)
    htmlfile.close()

    return html_filename


def nest_table(content):
    df = pd.DataFrame(data=content).T
    df = df.reindex(sorted(df.columns), axis=1)

    def squash_mpi(data):
        if data[0] == "0":
            return ""
        else:
            return '%s, %s' % (data[0], data[1])

    def squash_openmp(data):
        if data[0] == "openmp":
            return '%s, %s, %s, %s' % (data[0], data[1], data[2], data[3])
        else:
            return ""

    mpi_key = "%s,<br>number of ranks" % \
              ahref(faq_url+'DEVITO_MPI', 'MPI mode')
    df[mpi_key] = df[['mpi', 'num_procs']].apply(squash_mpi, axis=1)

    openmp_key = ahref(faq_url+'devito_language', 'Execution model')
    df[openmp_key] = df['language']

    for key in ('mpi', 'num_procs', 'language', 'platform', 'num_cpu',
                'num_threads', 'omp_places', 'omp_proc_bind', 'ram'):
        if key in df:
            del df[key]

    column_lut = {'jit': 'Compiler'}

    df = df.rename(columns=column_lut)

    return df.to_html(index=False, escape=False).replace('\n', '')


def get_thematrix():
    df = pd.read_json(thematrix_json)

    unpack(df, 'runners')

    lut = {"Standard-NC": azvm_url + "nc-series",
           "Standard-H": azvm_url + "h-series",
           "Standard-F": azvm_url + "fsv2-series"}

    for label in df.index.values:
        for key in lut:
            if key in label:
                link = ahref(lut[key], label[6:])
                os = df["os"][label]
                arch = df["arch"][label]
                new_label = r"%s<br>%s<br>%s" % (link, os, arch)
                df = df.rename(index={label: new_label})
                break

    df = df.loc[~df.index.duplicated(keep='first')]

    df['Runtime specification'] = df['jobs'].apply(nest_table)
    df['Hardware'] = df['arch']

    for crud in ('name', 'tags', 'cpu', 'os', 'arch', 'jobs'):
        del df[crud]

    return df.to_html(escape=False).replace('\n', '')


def get_benchmarks():
    df = pd.read_json(benchmarks_json)
    del df['version']

    df = df.transpose()

    for crud in ('code', 'timeout', 'type', 'name', 'version',
                 'param_names', 'params', 'unit'):
        del df[crud]

    links = []
    for label in df.index.values:
        link = """
<a href="%s">
  <figure>
    <img src="https://www.devitoproject.org/thematrix/swallow.png"
    alt="Airspeed velocity"</img>
  </figure>
</a>""" % ("%s#%s" % (matrix_url, label))
        links.append(link.replace('\n', ""))
    df["Airspeed velocity"] = pd.Series(links, index=df.index.values)

    return df.to_html(escape=False)


subs = {"THEMATRIX_TABLE": get_thematrix(),
        "BENCHMARKS_TABLE": get_benchmarks(),
        "THEMATRIX_HTML": wrap_html_path(convert_json2html(thematrix_json)),
        "BENCHMARKS_HTML": wrap_html_path(convert_json2html(benchmarks_json))}

readme = open("README.md", "w")
readme.write(readme_template.substitute(**subs))
readme.close()
