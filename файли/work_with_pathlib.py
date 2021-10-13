from pathlib import *

# take current_dir = C:\Users\nboichuk\PycharmProjects\python_lessons\файли
current_dir = Path.cwd()
# take home dir = C:\Users\nboichuk
home_dir = Path.home()
# make dir with name new_dir
Path("new_dir/").mkdir(parents=True, exist_ok=True)
fn = 'test.txt'
filepath = current_dir/fn
with filepath.open('w', encoding='utf-8') as f:
    f.write('this string will be write to test.txt')

try:
    filepath.unlink()
    Path("new_dir/").rmdir()
except FileNotFoundError as e:
    print(f"Error: {filepath} : {e.strerror}")
except OSError as e:
    print(f"Error : {e.strerror}")
