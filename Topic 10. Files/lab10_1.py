import io

with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = 'Це JPEG файл (%d байт)\n'
else:
    text = 'Це інший файл (%d байт)\n'

with io.open('photo.jpg', 'rb') as outf:
    # outf.write(text % len(jpgdata))
    f = outf.read()
    print(f)
