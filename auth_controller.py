from flask import request, redirect, render_template, session, url_for, flash
from werkzeug.security import generate_password_hash
from db import get_connection

def register_user():
    if request.method == 'POST':
        email = request.form['email']
        contraseña = request.form['password']
        rol_id = int(request.form['role'])  
        
                        ##### solo un administradores pueden registrar otros administradores
        if rol_id == 1: ##### administrador
            if 'user_role' not in session or session['user_role'] != 1:
                flash("Solo un administrador puede crear otro administrador.")
                return redirect(url_for('register'))

        hashed_password = generate_password_hash(contraseña)
        conn = get_connection()
        cursor = conn.cursor()

        ##### verificamos si el usuarioexiste
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (email,))
        existing = cursor.fetchone()

        if existing:
            flash("El usuario ya existe.")
            cursor.close()
            conn.close()
            return redirect(url_for('register'))

        # Insertar el nuevo usuario
        cursor.execute("INSERT INTO usuarios (correo, contraseña, rol_id) VALUES (%s, %s, %s)",
                       (email, hashed_password, rol_id))
        conn.commit()
        cursor.close()
        conn.close()

        flash("Registro exitoso. Inicia sesión.")
        return redirect(url_for('login'))

    return render_template('register.html')
