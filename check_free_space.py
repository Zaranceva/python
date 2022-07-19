import shutil
from pathlib import Path
import time

# вычесляем свободное место на диске.
# вычесляем размер директории
# копируем если есть свободное место.

# start config
# дата и время
name_dst_dir = Path(time.strftime('%d.%m.%Y.%H'))
dst_path = Path('/usr/') # папка назначения
src_path = Path('/kx/')  # папка что копируем
dest_disk_free_size = 0 # сколько должно остатся места.
folder_size = 0
disk_buffer = 0 # сколько свободного места должно остаться на диске
# end config

def mk_dest_folder():
    '''проверяем есть ли папка места назначения
    если нет, то создаем
    '''
    p = dst_path / name_dst_dir
    if not p.exists() : 
        print('папка не существует, создать')
        p.mkdir()
        return p
    else: 
        print('папка существует, не создаем новую')
        return False


def c_s_d (src_path):
    """ 
    Принемает Path объект места назначения и считает сумму всех файлов в директории
    и поддиректории.
    Возвращает размер папки в байтах.
    """
    total_size = 0
    for i in src_path.iterdir(): 
        if i.is_dir() :  total_size += c_s_d (i)
        if i.is_file() : total_size += i.stat().st_size
    return total_size


def start_copy():
    '''старт копирования'''    
    # свободное место на диске назначения
    dest_disk_free_size = shutil.disk_usage(dst_path).free//1024//1024
    folder_size = c_s_d(src_path)//1024//1024
    if dest_disk_free_size - disk_buffer - folder_size <0 :
        print ('нет свободного места на диске')
    else:
        print('начинаем копирование папки', src_path, 'размером', folder_size,'mb' , 'в ', dst_path)
        shutil.copytree(src_path, mk_dest_folder(), dirs_exist_ok=True)
    print('копирование завершено')

start_copy()
