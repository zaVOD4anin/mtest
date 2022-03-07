import os
import time
source = ['C:\\Code']
target_dir = 'C:\\Backupp'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr {0}{1}".format(target, str(source))
if os.system(zip_command) == 0:
    print('OK', target + os.sep)
else:
    print('Error')