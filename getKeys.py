def getKeys(file):
    with open(file,'r') as inf:
        hdr = inf.readline()
        keys = inf.readline().split(',')
    return {'aws_access_key' : keys[1], 'aws_secret_access_key' : keys[2]}
