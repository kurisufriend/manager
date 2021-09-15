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
            resp.append({"name":task.name, "time":task.time})
        return web.Response(text=json.dumps(resp))
    async def wtasks(self, request):
        name = request.query.get("name")
        try:
            tim = float(request.query.get("time"))
        except:
            return web.Response(status=422, text="400 bad arg")
        if name == "": name = "unnamed"
        if tim == 0.0: tim = time.time()
        self.parent.tasks.append(alarm.alarm(tim, name))
        self.rtasks(request)
        return web.Response(text="done")
