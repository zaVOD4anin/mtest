import os
import time
import zipfile

source = 'C:\\Code'
target_dir = 'C:\\Backupp'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан!')
comment = input('Введите комментарий: ')
if comment:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
else:
    target = today + os.sep + now + '.zip'
try:
    with zipfile.ZipFile(target, 'w') as zipchik:
        for folder, subfolders, files in os.walk(source):
            print(folder, subfolders, files)
            for file in files:
                zipchik.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), source),
                              compress_type=zipfile.ZIP_DEFLATED)
                print(os.path.join(folder, file))
                print('333333333333333')
                print(os.path.relpath(os.path.join(folder, file), source))
except:
    print('Error')
else:
    print('Zip created')

