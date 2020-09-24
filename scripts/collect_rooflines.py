from git import Repo
import json
from tempfile import gettempdir
import os
from shutil import move
import sys

import thematrix


def collect_rooflines(subdir=None):
    """
    Reads the file created from generate_rooflines.py and moves all generated
    artifacts to the results folder in the repository
    """

    # Set the roofline results directory
    thematrix_roof_res = os.path.join(os.path.dirname(thematrix.__path__[0]),
                                      'results')
    if subdir:
        thematrix_roof_res = os.path.join(thematrix_roof_res, subdir)

    if not os.path.isdir(thematrix_roof_res):
        # Create the roofline results directory if it does not exist
        os.makedirs(thematrix_roof_res)
    
    # Navigate to the file storing the paths of the generated rooflines
    generated_dir = os.path.join(gettempdir(), 'generate_rooflines_tmp')
    generated_file = os.path.join(generated_dir, 'generated.txt')

    if os.path.isfile(generated_file):
        # Prepare the filename for the collected data
        thematrix_repo = Repo(os.path.dirname(thematrix.__path__[0]))
        commit_hash = thematrix_repo.head.commit.hexsha
        json_f_name = os.path.join(thematrix_roof_res,
                                   '%s_rooflines_data.json' % commit_hash)

        # Setup the dictionary for all roofline data
        all_roofs_data = {}

        with open(generated_file, 'r') as f:
            # Remove newlines from directory names
            prob_dirs = [line.replace('\n', '') for line in f.readlines()]

            # Traverse each directory to extract roofline data
            for prob_dir in prob_dirs:
                prob_ident = os.path.basename(prob_dir)
                all_roofs_data[prob_ident] = _collect_all_roofline_data(prob_dir)

        # Remove file containing generated roofline data
        os.remove(generated_file)

        # Write to json file
        with open(os.path.join(thematrix_roof_res, json_f_name), 'w+') as json_f:
            json_f.write(json.dumps(all_roofs_data))
        print('Roofline data successfully collected into %s.' % json_f_name)

    else:
        print('%s file containing generated data could not be found. Make sure that '
              'the data has not already been collected.' % generated_file)


def _collect_all_roofline_files(filetype, prob_dir, dst_dir):
    """
    Moves all files of a specific filetype inside prob_dir into dst_dir
    """

    # Collect all files of the given type
    filetype_files = _get_files_by_type(filetype, prob_dir)

    # Collect the most recent commit hash to append to the start of the file name
    thematrix_repo = Repo(os.path.dirname(thematrix.__path__[0]))
    commit_hash = thematrix_repo.head.commit.hexsha

    # Obtain the problem identifier to append to the filename
    prob_ident = os.path.basename(prob_dir)

    if not filetype_files:
        print('Warning: no files of type %s present in %s.' % (filetype, prob_dir))
    
    for f_name in filetype_files:
        src_f_path = os.path.join(prob_dir, f_name)
        dst_f_name = '%s_%s_%s' % (commit_hash, prob_ident, f_name)
        dst_f_path = os.path.join(dst_dir, dst_f_name)

        if os.path.isfile(dst_f_path):
            # Remove pre-existing file at the destination
            os.remove(dst_f_path)

        move(src_f_path, dst_f_path)


def _collect_all_roofline_data(prob_dir):
    json_files = _get_files_by_type('json', prob_dir)
    if not json_files:
        print('Warning: no json files present in %s.' % prob_dir)

    rooflines = []
    for json_file in json_files:
        with open(json_file, 'r') as f:
            rooflines.append(json.load(f))

    return rooflines


def _get_files_by_type(filetype, src_dir):
    return [os.path.join(src_dir, f_name) for f_name in os.listdir(src_dir)
            if f_name.endswith('.%s' % filetype)]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        collect_rooflines(sys.argv[1])
    else:
        collect_rooflines()
