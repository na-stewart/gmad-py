import os


def extract(parent_dir, delete=False):
    for f in os.listdir(parent_dir):
        if '.gma' in f:
            file_to_extract = parent_dir + '/' + f
            os.system('lib/gmad_linux extract -file {0}'.format(file_to_extract))
            if delete:
                os.remove(file_to_extract)


def create(parent_dir, delete=False):
    for d in os.listdir(parent_dir):
        if '.gma' not in d:
            folder_to_create = parent_dir + '/' + d
            os.system('lib/gmad_linux create -folder {0} -out {1}'.format(folder_to_create, folder_to_create + '.gma'))
            if delete:
                os.rmdir(folder_to_create)
   

def execute(parent_dir, delete, gmad_type):
    if gmad_type == 'extract':
        extract(parent_dir, delete == 'yes')
    elif gmad_type == 'create':
        create(parent_dir, delete == 'yes')
    else:
        raise TypeError('Gmad execution type must be extract or create.')
    print('Thanks for using GmadEEC. Have a great day and I hope to see you soon!')


if __name__ == '__main__':
    print('''                                         /$$
                                        | $$
  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$$
 /$$__  $$| $$_  $$_  $$ |____  $$ /$$__  $$
| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  | $$
| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$
|  $$$$$$$| $$ | $$ | $$|  $$$$$$$|  $$$$$$$
 \____  $$|__/ |__/ |__/ \_______/ \_______/
 /$$  \ $$                                  
|  $$$$$$/                                  
 \______/                                   
                                        ''')
    print('Gmad Easy Extractor and Creator')
    print('Developed by sunset-developer. https://github.com/sunset-developer')
    print('------------------------------------------------------------------')
    parent_dir = input("Please enter the directory that your addons are located (/home/user/projects/addons): ")
    delete = input("Would you like to delete on completion? (yes/no): ")
    gmad_type = input("Please enter gmad execution type (extract/create): ")
    execute(parent_dir, delete, gmad_type)
