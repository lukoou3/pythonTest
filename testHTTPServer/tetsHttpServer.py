# -*- coding: utf-8 -*-
import http.server as hs
import urllib
import sys, os,time

try:
    basepath = sys._MEIPASS
except:
    basepath = "."

class ServerException(Exception):
    '''服务器内部错误'''
    pass


class RequestHandler(hs.BaseHTTPRequestHandler):
    num = 1
    access_urls = ["/handle"]
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """
    def __init__(self, *params):
        super().__init__(*params)
        """
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()
        """

    def send_content(self, page, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html;charset=utf-8")#application/javascript
        #self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(bytes(page, encoding='utf-8'))

    def do_GET(self):
        mpath, margs = urllib.parse.splitquery(self.path)  # ?分割
        margs = margs if margs else ""
        params = urllib.parse.parse_qs(urllib.parse.unquote(margs))
        self.do_action(mpath, params)

    def do_POST(self):
        path, margs = urllib.parse.splitquery(self.path)
        margs = margs if margs else ""
        params = urllib.parse.parse_qs(urllib.parse.unquote(margs))
        s = str(self.rfile.read(int(self.headers['content-length'])), 'UTF-8')  # 先解码     #datas = self.rfile.read(int(self.headers['content-length']))
        params.update( urllib.parse.parse_qs(urllib.parse.unquote(s)) )  # 解释参数
        self.do_action(path,params)

    def do_action(self, path, params):
        RequestHandler.num = RequestHandler.num + 1
        print(RequestHandler.num)
        #print(self.client_address)
        if path.endswith(".js"):
            self.handle_file(path)
        elif path in self.access_urls:
            self.send_content(str(params), 200)
        else:
            full_path = "/page/index.html"
            self.handle_file(full_path)

    def handle_file(self, full_path):
        try:
            with open(basepath+full_path, 'r', encoding='utf-8') as file:
                content = file.read()
            self.send_content(content, 200)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)


if __name__ == '__main__':
    print("#"*30)
    httpAddress = ('', 8081)
    httpd = hs.HTTPServer(httpAddress, RequestHandler)
    httpd.serve_forever()
