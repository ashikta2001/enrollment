import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x0e\x8d\xf9\xc0\x18W1\x97$^\x14\xdd\xd0\xf4l\xe1'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment'}
     # 'host':'mongodb://localhost:27017/UTA_Enrollment' 
    