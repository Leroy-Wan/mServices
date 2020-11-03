#!/usr/bin/python3
# coding: utf-8
import json
from app import make_app
import tornado.web

from tornado.ioloop import IOLoop
import tornado.options as options

# http://localhost:9000/?wd=python&title=%E7%9C%8B&title=lk&title=%E5%8A%A0



if __name__ == '__main__':
    # 定义命令行参数
    options.define('port',
                           default=8000,
                           type=int,
                           help='bind socket port')
    options.define('host',
                           default='localhost',
                           type=str,
                           help='设置host name')

    # 解析命令行参数的
    options.parse_command_line()

    app = make_app()
    app.listen(tornado.options.options.port)  # 使用命令行参数

    print('starting Web Server http://%s:%s' % (
        options.options.host,
        options.options.port
    ))
    # 启动服务
    IOLoop.current().start()