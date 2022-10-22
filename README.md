# image
# 安装
pip3 install -r requirements.txt

## 修改config.json设置好裁剪后图片的缓存路径即可，

```json
{
  "rootDir": "rootDir程序处理的图片源文件的文件夹",
  "cache": "处理后缓存的文件夹，第二次同样的参数则直接从缓存读取",
  "openCache": false,
  "openResize": true,
  "debug": false,
  "width": [ //数组可以限制只能裁剪那些宽度尺寸
    350,
    400,
    600,
    900
  ],
  "originalImage": true //true可以保护原图不被访问
}

```

# 启动
python main.py


#访问
* 程序占用9999端口，需要占用其他请求该main.py
* 第一种访问方式 http://127.0.0.1:9999/filePath?width=350
* 第二种访问方式 http://127.0.0.1:9999/350/filePath


