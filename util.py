import os
import imghdr


def checkFile(path):
    try:
        return os.path.isfile(path)
    except Exception:
        pass


def fileType(path):
    f = getFileName(path).split('.')[1]
    return f


def fileBaseName(path):
    f = getFileName(path).split('.')[0]
    return f


def getDirPath(path):
    f = getFileName(path)
    return path.replace(f, "")


def isImg(path):
    return imghdr.what(path)


def getFileName(path):
    return os.path.basename(path)
