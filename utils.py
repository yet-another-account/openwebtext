# Code taken in large part from https://github.com/jcpeterson/openwebtext


import os
import os.path as op
import tarfile
import re
import collections


def extract_month(url_file_name):
    month_re = r"(RS_.*2\d{3}-\d{2})"
    month = op.split(url_file_name)[-1]
    month = re.match(month_re, month).group()
    return month


def chunks(l, n, s=0):
    """Yield successive n-sized chunks from l, skipping the first s chunks."""
    if isinstance(l, collections.Iterable):
        chnk = []
        for i, elem in enumerate(l):
            if i < s:
                continue

            chnk.append(elem)
            if len(chnk) == n:
                yield chnk
                chnk = []
        if len(chnk) != 0:
            yield chnk

    else:
        for i in range(s, len(l), n):
            yield l[i : i + n]


def extract_archive(archive_fp, outdir="."):
    with tarfile.open(archive_fp, "r") as tar:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, outdir)
    return outdir


def mkdir(fp):
    try:
        os.makedirs(fp)
    except FileExistsError:
        pass
    return fp


def linecount(filename):
    f = open(filename, 'rb')
    lines = 0
    buf_size = 1024 * 1024
    read_f = f.raw.read

    buf = read_f(buf_size)
    while buf:
        lines += buf.count(b'\n')
        buf = read_f(buf_size)

    return lines
