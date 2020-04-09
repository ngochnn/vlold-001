import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! HA NGUYEN NHU NGOC 2175162!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
