from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)
        descuento_total = total_sin_descuento * descuento

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,descuento_total=descuento_total,
                               total_con_descuento=total_con_descuento)
    return render_template('/ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    lista_usuarios = {
        "juan": "admin",
        "pepe": "user"
    }
    if request.method == 'POST':
        usuario = request.form['nombre']
        contraseña = request.form['contraseña']
        if usuario in lista_usuarios and lista_usuarios[usuario] == contraseña:
            if usuario == 'juan':
                    mensaje = f"Bienvenido Administrador {usuario}"
            elif usuario == 'pepe':
                    mensaje = f"Bienvenido Usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

        return render_template('/ejercicio2.html', mensaje=mensaje)
    return render_template('/ejercicio2.html')

if __name__ == '__main__':
    app.run()





'''precio_tarro = 9000

    total_sin_descuento = cantidad * precio_tarro

    if 18 <= edad <=30:
        descuento = 0.15
        total_con_descuento = (cantidad * precio_tarro) * (1-descuento)
    elif edad > 30:
        descuento = 0.25
        total_con_descuento = (cantidad * precio_tarro) * (1-descuento)
    else:
        total_sin_descuento = cantidad * precio_tarro'''

'''if usuario == "juan" and contraseña == "admin":
    mensaje = f"Bienvenido Administrador {usuario}"
elif usuario == "pepe" and contraseña == "user":
    mensaje = f"Bienvenido Usuario {usuario}"
else:
    mensaje = "Usuario o contraseña incorrectos."'''



