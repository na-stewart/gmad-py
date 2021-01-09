import os


def extract(parent_dir, delete=False):
    for f in os.listdir(parent_dir):
        if '.gma' in f:
            file_to_extract = parent_dir + '/' + f
            os.system('lib/gmad_linux extract -file {0}'.format(file_to_extract))
            print('-------------------------------------------------------------------------------------------------\n')
            if delete:
                os.remove(file_to_extract)

