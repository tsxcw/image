# image
# 安装
pip3 install -r requirements.txt

修改config.json设置好裁剪后图片的缓存路径即可，
rootDir程序处理的图片源文件的文件夹
cache处理后缓存的文件夹，第二次同样的参数则直接从缓存读取
width数组可以限制只能裁剪那些宽度尺寸
originalImage为true可以保护原图不被访问

# 启动
python main.py
