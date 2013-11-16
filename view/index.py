# -*- coding: utf-8 -*-

import web

urls = (
    "", "index",
)

app = web.application(urls, locals())

class index:
    def GET(self):
        return "Yeah!"
