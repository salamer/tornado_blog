import tornado.ioloop
import pymongo
import tornado.web

port=3000
Mongo_url="localhost"
Mongo_port=27017
db_name="blog"
con_name="blog"

class BlogHandler(tornado.web.RequestHandler):
	def initialize(self):
		self.client=pymongo.MongoClient(Mongo_url,Mongo_port)
		self.db=self.client[db_name]
		self.con=self.db[con_name]

	def get(self):
		blogs=self.con.find()

		self.render("index.html",blogs=blogs)
	
	def post(self):
		editor=self.get_argument("editor")
		body=self.get_argument("body")
		self.con.insert_one({"editor":editor,"body":body}).inserted_id
		self.redirect("/")

def init_app():
	print "app is running on http://127.0.0.1:%s" % port
	return tornado.web.Application([
		tornado.web.url(r"/",BlogHandler)
	])

if __name__=="__main__":
	app=init_app()
	app.listen(port)
	tornado.ioloop.IOLoop.current().start()
