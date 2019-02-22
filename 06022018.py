from flask import Flask, render_template, flash, request , url_for, redirect

app=Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return 'Welcome on dashboard'

@app.route('/login/', methods=["GET", "POST"])
def login_page():
    error=''
    try:
        print(request.method)
        if request.method == "POST":
            attempted_username = request.form['username']
            print(attempted_username)
            attempted_password = request.form['password']
            print(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                print(url_for('dashboard'))
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid credentials. Try Again."

        return render_template('login.html', error=error)

    except Exception as e:
        return render_template('login.html', error=error)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)







