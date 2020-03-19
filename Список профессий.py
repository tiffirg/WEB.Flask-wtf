from flask import Flask, render_template
app = Flask(__name__)


@app.route('/list_prof/<value>')
def list_prof(value):
    array_prof = ["Строитель", "Врач"]
    return render_template('list_prof.html', array_prof=array_prof, value=value)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')