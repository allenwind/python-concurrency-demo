import os
import multiprocessing
import hashlib

BUFSIZE = 81920
POOLSIZE = 4

def compute_digest(filename):
    try:
        f = open(filename, 'rb')
    except IOError:
        return None
    digest = hashlib.sha512()
    while True:
        chunk = f.read(BUFSIZE)
        #chunk = os.urandom(1000) #测试CPU
        if not chunk:
            break
        digest.update(chunk)
    f.close()
    return filename, digest.hexdigest()

def build_digest_map(topdir):
    digest_pool = multiprocessing.Pool(POOLSIZE)
    allfiles = (os.path.join(path, name)
        for path, dirs, files in os.walk(topdir)
        for name in files)

    digest_map = dict(digest_pool.imap_unordered(compute_digest, allfiles, 20))
    digest_pool.close()
    return digest_map

if __name__ == '__main__':
    digest_map = build_digest_map(r"F:\music\phone music")
    print(digest_map)