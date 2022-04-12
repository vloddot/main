filename = input('Filename: ').strip()

mimetype_map = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip',
}

try:
    index = filename.index('.')

    mimetype = mimetype_map[filename[index+1:]]

except (KeyError, ValueError):
    mimetype = 'application/octet-stream'

print(mimetype)
