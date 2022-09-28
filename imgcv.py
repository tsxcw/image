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


# 获取缓存路径
def getCachePath(path, width):
    f = f"{util.getDirPath(path)}{util.fileBaseName(path)}_{width}.{util.fileType(path)}"
    return f


# 深曾从创建文件夹
def createDir(path):
    global cachePath
    p = f"{cachePath}{util.getDirPath(path)}"
    if not (os.path.isdir(p)):
        os.makedirs(p)


# 检查图片宽度是否符合标准
def checkWidth(w):
    width = config.env('width', [])
    originalImage = config.env('originalImage', True)
    if w == 0:
        if originalImage:  # 允许原图查看
            return True
        return False
    if len(width) == 0:  # 如果限制数组长度为0,通过
        return True  # 不允许查看原图
    if w in width:  # 如果再配置的数组中包含传递的参数，通过
        return True


# 设置尺寸
def resize(path, width=0):
    global cachePath
    if not (checkWidth(width)):  # 检查图片尺寸是否被允许
        return False
    try:
        cache = cacheExis(getCachePath(path, width))
        if util.checkFile(cache):  # 如果有缓存走缓存
            return cache
    except Exception:
        pass

    if not (util.checkFile(realRootPath(path))):  # 检查文件是否存在
        return False

    if width == 0:
        return realRootPath(path)

    if not (util.checkFile(realRootPath(path))):  # 检查源文件是否存在
        return False

    try:
        img = Image.open(realRootPath(path))  # 处理图片
    except FileNotFoundError as error:
        return False

    h = int(img.height / (img.width / width))
    # img.thumbnail((width, width))#宽度和高度某一条维度达到数值优先按照那个维度算
    img = img.resize((width, h))  # 更具宽度计算，等比例裁剪高度
    createDir(path)  # 创建缓存写入文件夹

    file = f"{cacheExis(getCachePath(path, width))}"  # 组装缓存地址文件路径
    img.save(file)  # 写入图片
    return file  # 返回文件地址
