#!/usr/bin/python3
# coding: utf-8
import tornado.web
from tornado.ioloop import IOLoop
import tornado.options as options

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 请求参数读取
        self.write('<h3>我是主页</h3>')

def make_app():
    return tornado.web.Application([
        ('/', IndexHandler),
    ], default_host=tornado.options.options.host)


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