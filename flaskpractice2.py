from flask import Flask, render_template, request
app = Flask("MyFlaskApp", static_folder="static")


@app.route('/sample')
def getSampleHtml():
    return render_template('sample.html')


@app.route('/user/<username>', methods=['GET'])
def greetUser(username):
    return render_template("result.html", username=username)



@app.route('/user', methods=['GET'])
def greetUserBasedOnReg():
    username = request.args.get("username")
    return render_template("result.html", username=username)

@app.route('/')
def hello():
    return 'Hello Michael'

if __name__ == '__main__':
    app.run(debug=True)