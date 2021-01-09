from gmad.core.creator import create
from gmad.core.extractor import extract


def user_input():
    parent_dir = input("Please enter the directory that your addons are located (/home/user/projects/addons): ")
    delete = input("Would you like to delete on completion? (yes/no): ")
    gmad_type = input("Please enter if you would like too extract or create an addon (extract/create): ")
    execute(parent_dir, delete, gmad_type)


def execute(parent_dir, delete, gmad_type):
    if gmad_type == 'extract':
        extract(parent_dir, delete == 'yes')
    elif gmad_type == 'create':
        create(parent_dir, delete == 'yes')


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
