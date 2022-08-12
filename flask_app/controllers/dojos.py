from flask_app import app, render_template, request, redirect
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def show_dojos():
    dojos = Dojo.get_all()
    ninjas_per_dojo = []
    for dojo in dojos:
        ninjas_per_dojo.append(
            Dojo.get_dojo_with_ninjas({'id': dojo.id}))
    return render_template('index.html', dojos=dojos, page_title='Dojos', ninjas_per_dojo=ninjas_per_dojo)


@app.route('/post/dojo', methods=['POST'])
def post_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojo/<int:id>')
def show_dojo(id):
    dojo = Dojo.get_dojo_with_ninjas({'id': id})
    return render_template('ninjas.html', dojo=dojo)


@app.route('/update/dojo', methods=['POST'])
def post_update():
    Dojo.update(request.form)
    return redirect(f"/dojo/{request.form['id']}")


@app.route('/delete/<int:id>')
def delete(id):
    Dojo.delete({'id': id})
    return redirect('/')
