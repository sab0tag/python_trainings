import base64
usr = base64.b64decode(b'YWRtaW4=').decode('utf-8')
pwd = base64.b64decode(b'c2VjcmV0').decode('utf-8')
print(pwd)
"""
import yaml
conf = open('application.yml')
parse_conf = yaml.load(conf, Loader=yaml.FullLoader)
username_cred = parse_conf['user']['username']
password_cred = parse_conf['user']['password']

"""

