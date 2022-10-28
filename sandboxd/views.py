from django.shortcuts import render
import pyrebase
config={
	"apiKey": "AIzaSyBcGJ9d3QOHuH_K2G3Gqwu7zgcr1I6a2MM",
	"authDomain": "sandbox-ec83f.firebaseapp.com",
	"databaseURL": "https://sandbox-ec83f-default-rtdb.firebaseio.com/",
	"projectId": "sandbox-ec83f",
	"storageBucket": "sandbox-ec83f.appspot.com",
	"messagingSenderId": "342827697815",
	"appId": "1:342827697815:web:a6ff5093e839f1ff070bd2"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
def home(request):
	day = database.child('Data').child('Day').get().val()
	id = database.child('Data').child('Id').get().val()
	projectname = database.child('Data').child('ProjectName').get().val()
	return render(request,"Home.html",{"day":day,"id":id,"projectname":projectname })


