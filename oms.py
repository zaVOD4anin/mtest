import os
import time
import zipfile
source = ['C:\\Code']
target_dir = 'C:\\Backupp'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан!')
comment = input('Введите комментарий: ')
if comment:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.txt'
else:
    target = today + os.sep + now + '.txt'
zip_command = "copy {0}{1}".format(target, str(source))
if os.system(zip_command) == 0:
    print('OK', target + os.sep)
else:
    print('Error')