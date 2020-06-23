from flask import Flask, render_template, url_for, flash, redirect, request, send_file
from forms import FupForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "123456789"


#main page
@app.route('/home', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def home():
    form = FupForm()
    #if form.validate_on_submit():
    if request.method == "POST":
        #get the inserted data
        ibanorder = form.ibanorder.data
        bicorder = form.bicorder.data
        banknameorder= form.banknameorder.data

        flash(" Templates successfully created", "success")
        return redirect(url_for("download"))
    return render_template("home.html", title="FUP", form=form)

#page where the download button is
@app.route('/download')
def download():
    return render_template("download.html", title="FUP")

#link for the download button
@app.route('/returnfile')
def returnfile():
    return send_file(r"C:\Users\Kevin\Desktop\Python\Flask_test\static\deutsche_bank.png")

#howto page
@app.route('/howto')
def howto():
    return render_template("howto.html", title="FUP")

#contact page
@app.route('/contact')
def contact():
    return render_template("contact.html", title="FUP")


if __name__ == '__main__':
    app.run()
