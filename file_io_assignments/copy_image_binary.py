def copy_binary(src='photo.jpg', dst='photo_copy.jpg'):
    try:
        with open(src, 'rb') as s:
            data = s.read()
        with open(dst, 'wb') as d:
            d.write(data)
        print('Binary copied')
    except FileNotFoundError:
        print('Source not found')

if __name__ == '__main__':
    copy_binary()
