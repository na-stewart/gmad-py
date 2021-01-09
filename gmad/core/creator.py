import os


def create(parent_dir, delete=False):
    for d in os.listdir(parent_dir):
        if '.gma' not in d:
            folder_to_create = parent_dir + '/' + d
            os.system('lib/gmad_linux create -folder {0} -out {1}'.format(folder_to_create, folder_to_create + '.gma'))
            print('-------------------------------------------------------------------------------------------------\n')
            if delete:
                os.rmdir(folder_to_create)


