#import tornado.httpserver
import tornado.ioloop
#import tornado.options
import tornado.web

#import os.path

import tornado.options

#from tornado.options import define,options
#tornado.options.define("port",default=3000,help="app run on 127.0.0.1:3000",type=int)

port=3000

class PageHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

class ListHandler(tornado.web.RequestHandler):
	def get(self):
		book_list=['R in action','learning python','django book','guide to tornado','Introduction to Algorithms']
		self.render("list.html",items=book_list)

class GetDataHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("get_form.html")

class PostDataHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("post_form.html")

class ResultShowHandler(tornado.web.RequestHandler):

	def get(self):
		name=self.get_argument("name")
		age=self.get_argument("age")
		subject=self.get_argument("subject")
		flag=True
		self.render("show.html",name=name,age=age,subject=subject,flag=flag)
	def post(self):
		stanford_score=1800
		score=int(self.get_argument("score"))
		if score>stanford_score:
			result="you can go to stanford!"
		else:
			result="please choose other college!"
		flag=False
		self.render("show.html",result=result,flag=flag)


def init_app():
	print "app is running on http://127.0.0.1:%s" % port
	return tornado.web.Application([
		tornado.web.url(r"/",PageHandler),
		tornado.web.url("/list",ListHandler),
		tornado.web.url("/get",GetDataHandler),
		tornado.web.url("/post",PostDataHandler),
		tornado.web.url("/show",ResultShowHandler),
	])

if __name__=="__main__":
	app=init_app()
	app.listen(3000)
	tornado.ioloop.IOLoop.current().start()