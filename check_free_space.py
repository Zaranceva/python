import shutil
from pathlib import Path
# проверяем свободное место на диске.
# проверяем размер директории
# копируем

dst_path = Path('c:/usr/')
dir_path = Path('c:/kx/')

dest_disk_free_size = 0
folder_size = 0

# свободное место на диске назначения
dest_disk_free_size = shutil.disk_usage(dst_path).free//1024//1024


def c_s_d (dir_path):
    """ 
    Принемает Path объект места назначения и считает сумму всех файлов в директории
    и поддиректории.
    Возвращает размер папки в байтах.
    """
    total_size = 0
    for i in dir_path.iterdir(): 
        if i.is_dir() :  total_size += c_s_d (i)
        if i.is_file() : total_size += i.stat().st_size
    return total_size

folder_size = c_s_d(dir_path)//1024//1024

if dest_disk_free_size - 1000 - folder_size <0 :
    print ('нет свободного места на диске')
else:
    print('начинаем копирование папки', dir_path, 'размером', folder_size,'mb' , 'в ', dst_path)
    shutil.copytree(dir_path, dst_path, dirs_exist_ok=True)
print('копирование завершено')