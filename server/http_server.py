from aiohttp import web
import asyncio
import time
import alarm
import json
class http_endpoint:
    def __init__(self, server):
        self.parent = server
        self.app = web.Application()
        self.app.add_routes([web.get("/r/tasks", self.rtasks),
        web.get("/w/task", self.wtasks)])
    async def rtasks(self, request):
        resp = []
        for task in self.parent.tasks:
            resp.append(task.__dict__)
        return web.Response(text=json.dumps(resp))
    async def wtasks(self, request):
        name = request.query.get("name")
        try:
            tim = float(request.query.get("time"))
        except:
            return web.Response(status=422, text="400 bad arg")
        if name == "": name = "unnamed"
        if tim == 0.0: tim = time.time()
        new = alarm.alarm(tim, name)
        self.parent.tasks.append(new)
        return web.Response(text=str(new.__dict__))
