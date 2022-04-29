from mimetypes import types_map, common_types

filename = input('Filename: ').strip()

print(filename.split('.'))
try:
    index = filename.index('.')
    
except ValueError:
    index = 0

try:
    mimetype = types_map[filename[index:].lower()]
    
except KeyError:
    try:
        
        mimetype = common_types[filename[index:].lower()]

    except KeyError:
        mimetype = 'application/octet-stream'


print(mimetype)