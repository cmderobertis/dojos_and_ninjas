from flask_app import app, render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/dojo/ninjas')
def show_ninjas():
    ninjas = Ninja.get_all()
    return render_template('index.html', ninjas=ninjas, page_title='Ninjas')


@app.route('/create_ninja')
def create_ninja():
    return render_template('createninja.html', page_title='Create Ninja', dojos=Dojo.get_all())


@app.route('/post_ninja', methods=['POST'])
def post_ninja():
    Ninja.save(request.form)
    return redirect(f"/dojo/{request.form['dojo_id']}")


@app.route('/profile/<int:id>')
def show_ninja(id):
    ninja = Ninja.get_one({'id': id})
    return render_template('profile.html', ninja=ninja)
