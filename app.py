from flask import Flask,render_template,redirect,request



app=Flask(__name__)

list=[]
avail_location=[{'from':'coimbatore','to':'chennai'}]


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        list.append({'username':username,'password':password})
        return render_template('flight_booking.html',name=username)

    return render_template('login.html')

@app.route('/flight',methods=["GET","POST"])
def flight():
    if request.method=='POST':
        depart_from=request.form.get('from')
        going_to=request.form.get('to')
        depature_date=request.form.get('depature_date') 
        avail_location=[{'from':'coiambatore','to':'chennai'}]
        if avail_location[0]['from']==depart_from and avail_location[0]['to']==going_to:
           return render_template('flight_booking.html',depart_from=depart_from,going_to=going_to,avail_location1=avail_location)
        else:
            return "there is no bus is available in this via"
    return render_template('flight_booking.html')

@app.route('/search',methods=["GET"])
def search():
    context=avail_location
    return render_template('flight_booking.html',context=context)

if __name__=='__main__':
    app.run(debug=True)
