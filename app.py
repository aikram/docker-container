from flask import Flask, render_template, request, flash, redirect, url_for, session
from dao.DAOUsuario import DAOUsuario
from dao.DAOCurso import DAOCurso
from dao.DAOEmpleado import DAOEmpleado
from dao.DAOExtra import DAOExtra

app = Flask(__name__)
app.secret_key = "Utec123456"
db = DAOUsuario()
db1 = DAOCurso()
db2 = DAOEmpleado()
db3 = DAOExtra()


@app.route('/') # root route
def inicio():
    return render_template('index.html')

@app.route('/usuario') # user route
def index():
    datos = db.read(None)
    return render_template('usuario/index.html', data=datos)

@app.route('/usuario/add/')
def add():
    return render_template('usuario/add.html')

@app.route('/usuario/addusuario', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/usuario/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('usuario/update.html', data = data)

@app.route('/usuario/updateusuario', methods = ['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/usuario/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('usuario/delete.html', data = data)

@app.route('/usuario/deleteusuario', methods = ['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/curso') # curso route
def curso():
    datos = db3.read(None)
    return render_template('curso/index.html', data=datos)

@app.route('/login') # login route
def loginPage():
    return render_template('login.html')

@app.route('/about') # about route
def aboutPage():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

@app.route('/empleado') # empleado route
def index_empleado():
    datos = db2.read(None)
    return render_template('empleado/index_e.html', data=datos)

@app.route('/empleado/add/')
def add_empleado():
    return render_template('empleado/add.html')

@app.route('/empleado/addempleado', methods = ['POST', 'GET'])
def addempleado():
    if request.method == 'POST' and request.form['save']:
        if db2.insert(request.form):
            flash("Nuevo empleado creado")
        else:
            flash("ERROR, al crear empleado")

        return redirect(url_for('index_empleado'))
    else:
        return redirect(url_for('index_empleado'))

@app.route('/empleado/update/<int:id>/')
def update_empleado(id):
    data = db2.read(id);

    if len(data) == 0:
        return redirect(url_for('index_empleado'))
    else:
        session['update'] = id
        return render_template('empleado/update.html', data = data)

@app.route('/empleado/updateempleado', methods = ['POST'])
def updateempleado():
    if request.method == 'POST' and request.form['update']:

        if db2.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index_empleado'))
    else:
        return redirect(url_for('index_empleado'))

@app.route('/empleado/delete/<int:id>/')
def delete_empleado(id):
    data = db2.read(id);

    if len(data) == 0:
        return redirect(url_for('index_empleado'))
    else:
        session['delete'] = id
        return render_template('empleado/delete.html', data = data)

@app.route('/empleado/deleteempleado', methods = ['POST'])
def deleteempleado():
    if request.method == 'POST' and request.form['delete']:

        if db2.delete(session['delete']):
            flash('Empleado eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index_empleado'))
    else:
        return redirect(url_for('index_empleado'))


if __name__ == '__main__':
    app.run(debug=True, port=3002)
