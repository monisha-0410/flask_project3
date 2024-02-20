from flask import Flask,request,render_template
from flask_wtf import Form
from wtforms import StringField,SubmitField
FAI=Flask(__name__)



@FAI.route('/htmlform',methods=['GET','POST'])
def htmlform():
    if request.method=='POST':
        fd=request.form
        return fd['un']
    return render_template('htmlform.html')

class NameForm(Form):
    name=StringField()
    submit=SubmitField()

@FAI.route('/webform',methods=['GET','POST'])
def webform():
    form=NameForm()
    if request.method=='POST':
        fd=NameForm(request.form)
        if fd.validate():
            return fd.name.data
    return render_template('webform.html',form=form)

if __name__=='__main__':
    FAI.run(debug=True)