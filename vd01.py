import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! NGOC NGOC!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
