# -*- coding:UTF-8 -*-

from flask import Flask, jsonify


class FlaskServer(object):

    def __init__(self, ip="127.0.0.1", port=58888):
        self.app = Flask(__name__)
        self._route_func_init()
        self.ip = ip
        self.port = port
        self.role = 'slave'
    
    def _route_func_init(self):
        @self.app.route('/role', methods=['GET'])
        def get_role():
            code = 200
            return jsonify({'role':self.role}), code

    def run(self):
        self.app.run(self.ip, self.port)
    
    def stop(self):
        self.app.stop()
    

if __name__ == '__main__':
    server = FlaskServer()
    server.run()