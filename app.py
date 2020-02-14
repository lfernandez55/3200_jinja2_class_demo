from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template():
    my_fruit_list = ['oranges','limes','lemons','pumpkins']
    my_person_list = [
        {'name':'bob', 'age':'22'},
        {'name': 'joe', 'age': '33'}
    ]
    print(my_person_list[1]['name'])
    return render_template('template.html', my_fruit_list=my_fruit_list, my_person_list=my_person_list)

@app.route("/contact_me")
def contact_me():

    return render_template('contact_me.html')

if __name__ == '__main__':
    app.run(debug=True)
