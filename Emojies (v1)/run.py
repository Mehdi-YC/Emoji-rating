from flask import Flask,render_template
from tinydb import TinyDB,Query
import sys
from datetime import datetime
from flask_table import Table, Col
app = Flask(__name__,template_folder='templates')
db = TinyDB('emojies.json')




class ItemTable(Table):
    VOTE = Col('VOTE')
    TIME = Col('TIME')
    DATE = Col('DATE')

class Item(object):
    def __init__(self, VOTE, TIME,DATE):
        self.VOTE = VOTE
        self.TIME = TIME
        self.DATE = DATE

@app.route("/")
def index():
    return render_template("test.html")



@app.route("/c1", methods=['POST'])
def c1():
    db.insert({"value":1,
                'date':str(datetime.now()).split(' ')[0],
                "time":str(datetime.now()).split(' ')[1].split('.')[0]})
    return render_template("test.html",mycolor='red')


@app.route("/c2", methods=['POST'])
def c2():
    db.insert({"value":2,
                'date':str(datetime.now()).split(' ')[0],
                "time":str(datetime.now()).split(' ')[1].split('.')[0]})
    return render_template("test.html",mycolor='#F08080')


@app.route("/c3", methods=['POST'])
def c3():
    db.insert({"value":3,
                'date':str(datetime.now()).split(' ')[0],
                "time":str(datetime.now()).split(' ')[1].split('.')[0]})
    return render_template("test.html",mycolor='#FFA500')


@app.route("/c4", methods=['POST'])
def c4():
    db.insert({"value":4,
                'date':str(datetime.now()).split(' ')[0],
                "time":str(datetime.now()).split(' ')[1].split('.')[0]})
    return render_template("test.html",mycolor='#f7dc15')



@app.route("/c5", methods=['POST'])
def c5():
    db.insert({"value":5,
                'date':str(datetime.now()).split(' ')[0],
                "time":str(datetime.now()).split(' ')[1].split('.')[0]})
    return render_template("test.html",mycolor='#00FF00')

@app.route("/admin/")
def admin():
    stat = Query()
    n1 = len(db.search(stat.value ==1))
    n2 = len(db.search(stat.value ==2))
    n3 = len(db.search(stat.value ==3))
    n4 = len(db.search(stat.value ==4))
    n5 = len(db.search(stat.value ==5))
    
    scores = n1+n2+n3+n4+n5
    if scores != 0:
        t1 = int((n1/scores)*100)
        t2 = int((n2/scores)*100)
        t3 = int((n3/scores)*100)
        t4 = int((n4/scores)*100)
        t5 = int((n5/scores)*100)
    else:
        t1=t2=t3=t4=t5=0
    
    items=[]
    for vote in db:
        items.append(dict(VOTE=vote['value'],DATE=vote['date'],TIME=vote['time']))
    
    table = ItemTable(items)

    return render_template("stats.html",t1=(t1),t2=(t2),t3=(t3),t4=(t4),t5=(t5),n1=int(n1),n2=int(n2),n3=int(n3),n4=int(n4),n5=int(n5),table=table.__html__())


@app.route("/admin/restored/")
def restore():
    db.drop_table('_default')
    db.table('_default')
    return render_template("stats.html",t1=(0),t2=(0),t3=(0),t4=(0),t5=(0),n1=int(0),n2=int(0),n3=int(0),n4=int(0),n5=int(0))

# run the application
if __name__ == "__main__":
    app.run(debug=True)

