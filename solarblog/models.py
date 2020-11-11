from datetime import datetime
from solarblog import db

class Posts(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	content = db.Column(db.Text, nullable =True)
	date_created=db.Column(db.DateTime, default = datetime.utcnow)

	
	def __repr__ (self) :
		return f"Posts('{self.content}', '{self.date_created}')"