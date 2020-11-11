from flask import render_template, url_for, request, redirect
from solarblog import app, db
from solarblog.models import Posts

@app.route("/", methods = ["POST", "GET"])
def home ():
	if request.method == "POST" :
		content_name = request.form['content']
		new_content = Posts(content=content_name)
		
		try:
			db.session.add(new_content)
			db.session.commit()
			return redirect (url_for("home"))
		except :
			return "THERE WAS AN ERROR"

	
	else :
		posts = Posts.query.order_by(Posts.date_created)
		return render_template('home.html', posts = posts)