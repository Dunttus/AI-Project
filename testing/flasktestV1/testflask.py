from flask import Flask, request, render_template
from form import SendLogForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'InsertSecretKey'

@app.route('/', methods=['GET', 'POST'])
def predict():
    form = SendLogForm()
    if form.is_submitted():
        result = request.form
        return render_template('pred.html', result=result)
    return render_template('predict.html', form=form)