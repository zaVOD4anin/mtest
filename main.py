def hello():
    print('hello world')
source = ['C:\\Code', 'aboba']
print(type(' '.join(source)))
hello()
num1 = num2 = [5]
print(num1 + num2, 'абоба')
for folder, subfolders, files in os.walk('C:\\Code'):
    for file in files:
        fantasy_zip.write(os.path.join(folder, file),
                          os.path.relpath(os.path.join(folder, file), 'C:\\Stories\\Fantasy'),
                          compress_type=zipfile.ZIP_DEFLATED)

print(os.path.relpath(os.path.join(folder,file), 'C:\\Stories\\Fantasy'))