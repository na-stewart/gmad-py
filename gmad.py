from gmad.core.creator import create
from gmad.core.extractor import extract


def user_input():
    parent_dir = input("Please enter the directory that your addons are located (/home/user/projects/addons): ")
    delete = input("Would you like to delete on completion? (yes/no): ")
    gmad_type = input("Please enter gmad execution type (extract/create): ")
    execute(parent_dir, delete, gmad_type)


def execute(parent_dir, delete, gmad_type):
    if gmad_type == 'extract':
        extract(parent_dir, delete == 'yes')
    elif gmad_type == 'create':
        create(parent_dir, delete == 'yes')
    else:
        raise TypeError('Gmad execution type must be extract or create.')
    print ('Thanks for using GmadEAEC. Have a great day and I hope to see you soon!')



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
    user_input()
