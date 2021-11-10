import json
import logging
import random
import string
from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    # noinspection PyPep8Naming
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        res = dict()
        for i in range(10):
            res[i] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))

        self.wfile.write(json.dumps(res).encode("utf-8"))


def run(server_class=HTTPServer):
    server_address = ('', 8000)
    httpd = server_class(server_address, Server)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
