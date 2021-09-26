import socket
import client
import threading
import time
import alarm
import http_server
import asyncio
from aiohttp import web
import msg
import json

class server:
    def __init__(self, address, port):
        self.clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((address, port))
        self.sock.listen()
        self.tasks = []
    def __del__(self):
        for c in self.clients:
            del c
    def run(self):
        t = threading.Thread(target=self.handle_connections, args=())
        t.start()


        he = http_server.http_endpoint(self)
        runner = web.AppRunner(he.app)
        het = threading.Thread(target=self.launch_http_server, args=(runner,))
        het.start()

        # self.tasks.append(alarm.alarm(time.time() + 30))

        while True:
            time.sleep(10)
            for task in self.tasks:
                if task.check():
                    for c in self.clients:
                        c.sock.sendall(msg.msg("task", json.dumps(task.__dict__)))
    def handle_connections(self):
        while True:
            (client_sock, address) = self.sock.accept()
            c = client.client(client_sock, address)

            self.clients.append(c)
            print("added client:", address)

            t = threading.Thread(target=c.run, args=())
            t.start()
    def launch_http_server(self, app_runner):
        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)
        event_loop.run_until_complete(app_runner.setup())
        endpoint = web.TCPSite(app_runner, "0.0.0.0", 8080)
        event_loop.run_until_complete(endpoint.start())
        event_loop.run_forever()
