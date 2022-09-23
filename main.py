import io
import os

from flask import Flask, request, send_file, Response

import config
import imgcv

app = Flask(__name__)


@app.get("/<path:path>")
def print_hi(path):
    w = int(request.args.get('width', 0))
    p = imgcv.resize(path, w)
    if p:
        return send_file(p)
    return Response(status=404)

    # 在下面的代码行中使用断点来调试脚本。


@app.get('/<int:width>/<path:path>')
def main2(width, path):
    w = int(width)
    p = imgcv.resize(path, w)
    if p:
        return send_file(p)
    return Response(status=404)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app.run(port=9999, host='0.0.0.0', debug=True)
