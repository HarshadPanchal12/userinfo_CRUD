from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)
users=[
  {'name':'Alice','age':30,'email':'alice@example.com'},
  {'name':'Bob','age':25,'email':'bob@example.com'},
  {'name':'Charlie','age':35,'email':'charlie@example.com'}
]

@app.route('/',methods=['GET','POST'])
def home():
  if request.method=='POST':
    name=request.form['name']
    age=request.form['age']
    email=request.form['email']
    users.append({'name':name,'age':age,'email':email})
  return render_template('home.html',users=users)

@app.route('/users',methods=['GET'])
def user():
  return render_template('users.html')

@app.route('/update/<string:name>',methods=['GET','POST'])
def update(name):
  cnt=0
  user_to_update=None
  for user in users:
    
    if user['name']==name:
      user_to_update=user
      break
    cnt+=1
  if request.method=='POST' and user_to_update:
    new_name=request.form['name']
    new_age=request.form['age']
    new_email=request.form['email']
    users[cnt]['name']=new_name
    users[cnt]['age']=new_age
    users[cnt]['email']=new_email
    return redirect(url_for('home'))
  else:
    return render_template('update.html',user=user_to_update)

@app.route('/delete/<string:name>',methods=['GET','POST'])
def delete(name):
  cnt=0
  user_to_delete=None
  for user in users:
    
    if user['name']==name:
      user_to_delete=user
      break
    cnt+=1
  if request.method=='POST' and user_to_delete:
    users.pop(cnt)
    return redirect(url_for('home'))
  else:
    return render_template('delete.html',user=user_to_delete)

if __name__=="__main__":
  app.run(debug=True)