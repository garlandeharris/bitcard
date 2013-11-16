# -*- coding: utf-8 -*-

import web
from view import index

urls = (
#    r"/login",      view.login.app,
#    r"/account",    view.account.app,
    r"/",           index.app,
)

app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()
