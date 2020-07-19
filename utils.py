# import json

def resp(status, data, msg = None):
    return json.dumps({'status': status, 'data': data, 'msg': msg})