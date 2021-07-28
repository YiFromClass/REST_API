from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Mood(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	day = db.Column(db.String(80), unique=True, nullable=False)
	mood_value = db.Column(db.Integer)
	username = db.Column(db.String(80), nullable=False)
	password = db.Column(db.String(80), nullable=False)
	streak = db.Column(db.Integer)

	def __repr__(self):
		return f"{self.day} - {self.mood_value}"

@app.route('/')
def index():
	return 'Hello!'

@app.route('/mood')
def get_moods():
	moodlist = Mood.query.all()
	temp = date.today()
	temp2 = temp.strftime("%Y-%m-%d")
	output = []
	check = False
	for moods in moodlist:
		if moods.day == temp2:
			check = True
	if check:
		for moods in moodlist:
			mood_data = {'id': moods.id, 'username': moods.username, 'day': moods.day, 'mood_value': moods.mood_value, "streak": moods.streak}
			output.append(mood_data)
		return {"moods": output}
	return {"error": "please post your mood today first"}

@app.route('/mood/<id>')
def get_mood(id):
	mood = Mood.query.get_or_404(id)
	return ({"day": mood.day, "mood_value": mood.mood_value, "streak": mood.streak})

@app.route('/mood', methods=['POST'])
def add_mood():
	temp_mood = Mood.query.all()
	temp = date.today()
	temp2 = temp.strftime("%Y-%m-%d")
	temp3 = date.today() - timedelta(days = 1)
	temp4 = temp3.strftime("%Y-%m-%d")
	if len(temp_mood) == 0:
		mood = Mood(day=temp2, mood_value=request.json['mood_value'], username=request.json['username'], password=request.json['password'], streak = 1)
		db.session.add(mood)
		db.session.commit()
		return {'id': mood.id, 'streak': mood.streak}
	else:
		mood = Mood(day=temp2, mood_value=request.json['mood_value'], username=request.json['username'], password=request.json['password'])
		listmood = temp_mood[-1]
		if listmood.day == mood.day:
			return {"error": "you have already signed in today"}
		if listmood.username == mood.username:
			if listmood.password == mood.password:
				if listmood.day == temp4:
					mood.streak = listmood.streak + 1
				else:
					mood.streak = 1
				db.session.add(mood)
				db.session.commit()
				return {'id': mood.id, 'streak': mood.streak}
	return {'error': 'bad username or password'}

@app.route('/mood/<id>', methods=['DELETE'])
def delete_mood(id):
	mood = Mood.query.get(id)
	if mood is None:
		return {"error": "not found"}
	db.session.delete(mood)
	db.session.commit()
	return {"success": "done"} 