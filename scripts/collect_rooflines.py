from tempfile import gettempdir
import os
from shutil import move

import thematrix


def collect_rooflines():
    """
    Reads the file created from generate_rooflines.py and moves all generated
    artifacts to the results-roofline folder in the repository
    """

    thematrix_roof_res = os.path.join(os.path.dirname(thematrix.__path__[0]),
                                      'results-roofline')
    
    generated_dir = os.path.join(gettempdir(), 'generate_rooflines_tmp')
    generated_file = os.path.join(generated_dir, 'generated.txt')

    if os.path.isfile(generated_file):
        with open(generated_file, 'r') as f:
            for prob_dir in f.readlines():
                prob_ident = os.path.basename(prob_dir)

                dst_dir = os.path.join(thematrix_roof_res, prob_ident)
                if not os.path.isdir(dst_dir):
                    os.mkdir(dst_dir)

                _move_all_files('png', prob_dir, dst_dir)
                _move_all_files('json', prob_dir, dst_dir)

    print('Rooflines and data successfully moved to %s.' % thematrix_roof_res)


def _move_all_files(filetype, src_dir, dst_dir):
    """
    Moves all files of a specific filetype inside src_dir into dst_dir
    """

    for f_name in os.listdir(src_dir):
        if f_name.endswith('.%s' % filetype):
            try:
                move(os.path.join(src_dir, f_name), dst_dir)
            except OSError:
                os.remove(os.path.join(dst_dir, f_name))


if __name__ == '__main__':
    collect_rooflines()
