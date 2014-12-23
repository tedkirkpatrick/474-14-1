# Tools for managing jekyll site served on an AWS S3 bucket

import glob
import os.path

from boto.s3.connection import S3Connection
from boto.s3.key import Key

def getKeys(file):
    with open(file,'r') as inf:
        hdr = inf.readline()
        keys = inf.readline().split(',')
    return keys[1], keys[2]

def fileKey(cb, fn):
    return Key(cb, fn)

#schedule = fileKey(cb, 'Schedule.html')
#challenges = fileKey(cb, 'Challenges.html')

def push(cb, fkey):
    fpath = os.path.join('_site', fkey.key)
    fkey.set_contents_from_filename(fpath)
    fkey.make_public()

def pushFilesMatching(cb, pat):
    for fpath in glob.iglob(pat):
        fn = os.path.split(fpath)[1]
        k = fileKey(cb, fn)
        push(cb, k)

def pushAllSiteFiles(cb):
    pushFilesMatching(cb, '_site/*.html')
    pushFilesMatching(cb, '_site/*.css')

def openS3Bucket(keyFile, bucketName):
    acc, priv = getKeys(keyFile)
    conn = S3Connection(acc, priv)
    for b in conn.get_all_buckets():
        if str(b) == '<Bucket: '+ bucketName + '>':
            break
    else:
        assert False
    return b

def pushSite(keyFile, bucketName):
    cb = openS3Bucket(keyFile, bucketName)
    pushAllSiteFiles(cb)
