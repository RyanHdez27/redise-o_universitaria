from flask import request, redirect, render_template, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_connection

def register_user():
    if request.method == 'POST':
        email = request.form['email']
        contraseña = request.form['password']
        rol_id = int(request.form['role'])  
        
        ####solo un administrador puede registrar otros administradores
        if rol_id == 1:
            if 'user_role' not in session or session['user_role'] != 1:
                flash("Solo un administrador puede crear otro administrador.")
                return redirect(url_for('register'))

        hashed_password = generate_password_hash(contraseña)
        conn = get_connection()
        cursor = conn.cursor()

        ##verificamos si el usuario ya existe
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (email,))
        existing = cursor.fetchone()

        if existing:
            flash("El usuario ya existe.")
            cursor.close()
            conn.close()
            return redirect(url_for('register'))

        ##insertamos un nuevo usuario
        cursor.execute("INSERT INTO usuarios (correo, contraseña, rol_id) VALUES (%s, %s, %s)",
                       (email, hashed_password, rol_id))
        conn.commit()
        cursor.close()
        conn.close()

        flash("Registro exitoso. Inicia sesión.")
        return redirect(url_for('ingresar'))

    return render_template('register.html')

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user['contraseña'], password):
            session['user_id'] = user['id']
            session['user_role'] = user['rol_id']
            session['email'] = user['correo']
            flash("Inicio de sesión exitoso.")
            
            return redirect(url_for('portal'))
        
        else:
            flash("Correo o contraseña incorrectos.")

    return render_template('login_ll.html')


def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['new_password']

        hashed = generate_password_hash(new_password)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (email,))
        user = cursor.fetchone()

        if not user:
            flash("Correo no encontrado.")
            cursor.close()
            conn.close()
            return redirect(url_for('reset_password'))

        cursor.execute("UPDATE usuarios SET contraseña = %s WHERE correo = %s", (hashed, email))
        conn.commit()
        cursor.close()
        conn.close()

        flash("Contraseña actualizada. Inicia sesión.")
        return redirect(url_for('login'))

    return render_template('reset_password.html')
