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
        for i in range(s * n, len(l), n):
            chnk = []
            for _ in range(n):
                chnk.append(next(l))

            yield chnk
    else:
        for i in range(s * n, len(l), n):
            yield l[i : i + n]


def extract_archive(archive_fp, outdir="."):
    with tarfile.open(archive_fp, "r") as tar:
        tar.extractall(outdir)
    return outdir


def mkdir(fp):
    try:
        os.makedirs(fp)
    except FileExistsError:
        pass
    return fp
