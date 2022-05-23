from mimetypes import types_map, common_types

filename = input('Filename: ').strip()

filename = filename.split('.')

mimetype = 'application/octet-stream'
for extension in filename[len(filename)-1:0:-1]:

    try:
        mimetype = types_map[f'.{extension.lower()}']
        break

    except KeyError:
        try:
            mimetype = common_types[f'.{extension.lower()}']
        except KeyError:
            mimetype = 'application/octet-stream'
            break


print(mimetype)
