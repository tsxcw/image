import os

from PIL import Image

import config
import util

cachePath = config.env('cache', "./tmp/")
if not (os.path.isdir(cachePath)):
    os.mkdir(cachePath)


# 文件根目录合成
def realRootPath(path):
    return config.env("rootDir") + path


# 缓存路径合成
def cacheExis(path):
    return cachePath + path


def getCachePath(path, width):
    f = f"{util.getDirPath(path)}{util.fileBaseName(path)}_{width}.{util.fileType(path)}"
    return f


def createDir(path):
    global cachePath
    p = f"{cachePath}{util.getDirPath(path)}"
    if not (os.path.isdir(p)):
        os.makedirs(p)


# 设置尺寸
def resize(path, width=0):
    global cachePath

    try:
        cache = cacheExis(getCachePath(path, width))
        if util.checkFile(cache):  # 如果有缓存走缓存
            return cache
    except Exception:
        pass

    if not (util.checkFile(realRootPath(path))):
        return False

    if width == 0:
        return realRootPath(path)

    if not (util.checkFile(realRootPath(path))):  # 检查源文件是否存在
        return False

    try:
        img = Image.open(realRootPath(path))  # 处理图片
    except FileNotFoundError as error:
        return False

    img.thumbnail((width, width))
    createDir(path)
    file = f"{cacheExis(getCachePath(path, width))}"
    img.save(file)
    return file
