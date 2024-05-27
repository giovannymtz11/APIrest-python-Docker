from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
<<<<<<< HEAD

conexion=MySQL(app)

#METODOS PARA TABLE CARRERA
@app.route('/carreras', methods=['GET'])
def listar_carreras():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT CarreraID, NombreCarrera, Semestres, EspecialidadID FROM carrera"
        cursor.execute(sql)
        datos = cursor.fetchall()
        carreras = []
        for fila in datos:
            carrera={'CarreraID':fila[0], 'NombreCarrera':fila[1], 'Semestres':fila[2], 'EspecialidadID':fila[3]}
            carreras.append(carrera)
        return jsonify({'carreras':carreras, 'mensaje': "Carreras listadas."})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})

@app.route('/carreras/<CarreraID>', methods=['GET'])
def leerCarreras(CarreraID):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT CarreraID, NombreCarrera FROM carrera WHERE CarreraID = '{0}'".format(CarreraID)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            carrera={'CarreraID':datos[0], 'NombreCarrera':datos[1]}
            return jsonify({'carreras':carrera, 'mensaje': "Carrera encontrada."})
        else:
            return jsonify({'mensaje': "Curso no encontrado"})      
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})  
    
@app.route('/carreras', methods=['POST'])
def registrarCarrera():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO carrera (CarreraID, NombreCarrera, Semestres, EspecialidadID) 
                VALUES ('{0}','{1}',{2},'{3}')""".format(request.json['CarreraID'],request.json['NombreCarrera'],
                                                           request.json['Semestres'],request.json['EspecialidadID'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la insercion de los datos.
        return jsonify({'mensaje': "Curso registrado"})      
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})  


@app.route('/carreras/<CarreraID>', methods=['DELETE'])
def eliminarCarrera(CarreraID):
    try:
        cursor = conexion.connection.cursor()
        sql = """DELETE FROM carrera WHERE CarreraID = '{0}'""".format(CarreraID)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la eliminacion de los datos.
        return jsonify({'mensaje': "Curso eliminado"})      
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})  
    
@app.route('/carreras/<CarreraID>', methods=['PUT'])
def actualizarCarrera(CarreraID):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE carrera SET NombreCarrera = '{0}', Semestres = {1}, 
                    EspecialidadID = '{2}' WHERE CarreraID = '{3}'""".format(request.json['NombreCarrera'], request.json['Semestres'],
                                                                             request.json['EspecialidadID'], CarreraID)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la actualizacion de los datos.
        return jsonify({'mensaje': "Curso actualizado"})      
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})  

#METODOS PARA TABLA ESPECIALIDAD
@app.route('/especialidades', methods=['GET'])
def listar_especialidades():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT EspecialidadID, NombreEspecialidad, CarreraID FROM especialidad"
        cursor.execute(sql)
        datos = cursor.fetchall()
        especialidades = []
        for fila in datos:
            especialidad={'EspecialidadID':fila[0], 'NombreEspecialidad':fila[1], 'CarreraID':fila[2]}
            especialidades.append(especialidad)
        return jsonify({'especialidades':especialidades, 'mensaje': "Especialidades listadas."})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"}) #LISTO

@app.route('/especialidades/<EspecialidadID>', methods=['GET'])
def leerEspecialidades(EspecialidadID):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT NombreEspecialidad, CarreraID FROM especialidad WHERE EspecialidadID = '{0}'".format(EspecialidadID)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            especialidad={'NombreEspecialidad':datos[0], 'CarreraID':datos[1]}
            return jsonify({'especialidades':especialidad, 'mensaje': "Especialidad encontrada."})
        else:
            return jsonify({'mensaje': "Curso no encontrado"})      
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})  
    
@app.route('/especialidades', methods=['POST'])
def registrarEspecialidad():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO especialidad (EspecialidadID, NombreEspecialidad, CarreraID) 
                VALUES ('{0}','{1}','{2}')""".format(request.json['EspecialidadID'],request.json['NombreEspecialidad'],
                                                           request.json['CarreraID'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la insercion de los datos.
        return jsonify({'mensaje': "Especialidad registrada"})      
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})  


@app.route('/especialidades/<EspecialidadID>', methods=['DELETE'])
def eliminarEspecialidad(EspecialidadID):
    try:
        cursor = conexion.connection.cursor()
        sql = """DELETE FROM especialidad WHERE EspecialidadID = '{0}'""".format(EspecialidadID)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la eliminacion de los datos.
        return jsonify({'mensaje': "Especialidad eliminada"})      
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})  
    
@app.route('/especialidades/<EspecialidadID>', methods=['PUT'])
def actualizarEspecialidad(EspecialidadID):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE especialidad SET NombreEspecialidad = '{0}', CarreraID = '{1}' 
                    WHERE EspecialidadID = '{2}'""".format(request.json['NombreEspecialidad'], request.json['CarreraID'],
                                                            EspecialidadID)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la actualizacion de los datos.
        return jsonify({'mensaje': "Especialidad actualizada"})      
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})  
    
# METODOS PARA TABLA MATERIA
@app.route('/materias', methods=['GET'])
def listar_materias():
    try:
        print("Conexión a la base de datos:", conexion.connection)
        cursor = conexion.connection.cursor()
        sql = "SELECT MateriaID, NombreMateria, Creditos, CarreraID, Semestre, Seguimiento, EspecialidadID FROM materia"
        cursor.execute(sql)
        datos = cursor.fetchall()
        print("Datos obtenidos de la consulta:", datos)
        materias = []
        for fila in datos:
            materia = {
                'MateriaID': fila[0],
                'NombreMateria': fila[1],
                'Creditos': fila[2],
                'CarreraID': fila[3],
                'Semestre': fila[4],
                'Seguimiento': fila[5],
                'EspecialidadID': fila[6]
            }
            materias.append(materia)
        return jsonify({'materias': materias, 'mensaje': "Materias listadas."})
    except Exception as ex:
            return jsonify({'mensaje': "ERROR!"})

@app.route('/materias/<MateriaID>', methods=['GET'])
def leerMateria(MateriaID):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT MateriaID, NombreMateria, Creditos, CarreraID, Semestre, Seguimiento, EspecialidadID FROM materia WHERE MateriaID = '{0}'".format(MateriaID)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            materia = {
                'MateriaID': datos[0],
                'NombreMateria': datos[1],
                'Creditos': datos[2],
                'CarreraID': datos[3],
                'Semestre': datos[4],
                'Seguimiento': datos[5],
                'EspecialidadID': datos[6]
            }
            return jsonify({'materias': materia, 'mensaje': "Materia encontrada."})
        else:
            return jsonify({'mensaje': "Materia no encontrada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})

@app.route('/materias', methods=['POST'])
def registrarMateria():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO materia (MateriaID, NombreMateria, Creditos, CarreraID, Semestre, Seguimiento, EspecialidadID) 
                    VALUES ('{0}', '{1}', {2}, '{3}', {4}, '{5}', '{6}')""".format(
            request.json['MateriaID'],
            request.json['NombreMateria'],
            request.json['Creditos'],
            request.json['CarreraID'],
            request.json['Semestre'],
            request.json['Seguimiento'],
            request.json['EspecialidadID']
        )
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': "Materia registrada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})

@app.route('/materias/<MateriaID>', methods=['DELETE'])
def eliminarMateria(MateriaID):
    try:
        cursor = conexion.connection.cursor()
        sql = """DELETE FROM materia WHERE MateriaID = '{0}'""".format(MateriaID)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': "Materia eliminada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})

@app.route('/materias/<MateriaID>', methods=['PUT'])
def actualizarMateria(MateriaID):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE materia SET NombreMateria = '{0}', Creditos = {1}, CarreraID = '{2}', Semestre = {3}, 
                    Seguimiento = '{4}', EspecialidadID = '{5}' WHERE MateriaID = '{6}'""".format(
            request.json['NombreMateria'],
            request.json['Creditos'],
            request.json['CarreraID'],
            request.json['Semestre'],
            request.json['Seguimiento'],
            request.json['EspecialidadID'],
            MateriaID
        )
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': "Materia actualizada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!"})
=======
app.config.from_object(config['default'])

mysql = MySQL(app)

@app.route('/carreras', methods=['GET'])
def listar_carreras():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT CarreraID, NombreCarrera, Semestres, EspecialidadID FROM carrera")
        datos = cursor.fetchall()
        carreras = [{'CarreraID': fila[0], 'NombreCarrera': fila[1], 'Semestres': fila[2], 'EspecialidadID': fila[3]} for fila in datos]
        return jsonify({'carreras': carreras, 'mensaje': "Carreras listadas."})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/carreras/<CarreraID>', methods=['GET'])
def leer_carrera(CarreraID):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT CarreraID, NombreCarrera, Semestres, EspecialidadID FROM carrera WHERE CarreraID = %s", (CarreraID,))
        datos = cursor.fetchone()
        if datos:
            carrera = {'CarreraID': datos[0], 'NombreCarrera': datos[1], 'Semestres': datos[2], 'EspecialidadID': datos[3]}
            return jsonify({'carrera': carrera, 'mensaje': "Carrera encontrada."})
        else:
            return jsonify({'mensaje': "Carrera no encontrada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/carreras', methods=['POST'])
def registrar_carrera():
    try:
        cursor = mysql.connection.cursor()
        sql = """INSERT INTO carrera (CarreraID, NombreCarrera, Semestres, EspecialidadID) 
                VALUES (%s, %s, %s, %s)"""
        values = (request.json['CarreraID'], request.json['NombreCarrera'], request.json['Semestres'], request.json['EspecialidadID'])
        cursor.execute(sql, values)
        mysql.connection.commit()
        return jsonify({'mensaje': "Carrera registrada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/carreras/<CarreraID>', methods=['DELETE'])
def eliminar_carrera(CarreraID):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM carrera WHERE CarreraID = %s", (CarreraID,))
        mysql.connection.commit()
        return jsonify({'mensaje': "Carrera eliminada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/carreras/<CarreraID>', methods=['PUT'])
def actualizar_carrera(CarreraID):
    try:
        cursor = mysql.connection.cursor()
        sql = """UPDATE carrera SET NombreCarrera = %s, Semestres = %s, EspecialidadID = %s WHERE CarreraID = %s"""
        values = (request.json['NombreCarrera'], request.json['Semestres'], request.json['EspecialidadID'], CarreraID)
        cursor.execute(sql, values)
        mysql.connection.commit()
        return jsonify({'mensaje': "Carrera actualizada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/especialidades', methods=['GET'])
def listar_especialidades():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT EspecialidadID, NombreEspecialidad, CarreraID FROM especialidad")
        datos = cursor.fetchall()
        especialidades = [{'EspecialidadID': fila[0], 'NombreEspecialidad': fila[1], 'CarreraID': fila[2]} for fila in datos]
        return jsonify({'especialidades': especialidades, 'mensaje': "Especialidades listadas."})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/especialidades/<EspecialidadID>', methods=['GET'])
def leer_especialidad(EspecialidadID):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT EspecialidadID, NombreEspecialidad, CarreraID FROM especialidad WHERE EspecialidadID = %s", (EspecialidadID,))
        datos = cursor.fetchone()
        if datos:
            especialidad = {'EspecialidadID': datos[0], 'NombreEspecialidad': datos[1], 'CarreraID': datos[2]}
            return jsonify({'especialidad': especialidad, 'mensaje': "Especialidad encontrada."})
        else:
            return jsonify({'mensaje': "Especialidad no encontrada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/especialidades', methods=['POST'])
def registrar_especialidad():
    try:
        cursor = mysql.connection.cursor()
        sql = """INSERT INTO especialidad (EspecialidadID, NombreEspecialidad, CarreraID) 
                VALUES (%s, %s, %s)"""
        values = (request.json['EspecialidadID'], request.json['NombreEspecialidad'], request.json['CarreraID'])
        cursor.execute(sql, values)
        mysql.connection.commit()
        return jsonify({'mensaje': "Especialidad registrada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/especialidades/<EspecialidadID>', methods=['DELETE'])
def eliminar_especialidad(EspecialidadID):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM especialidad WHERE EspecialidadID = %s", (EspecialidadID,))
        mysql.connection.commit()
        return jsonify({'mensaje': "Especialidad eliminada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/especialidades/<EspecialidadID>', methods=['PUT'])
def actualizar_especialidad(EspecialidadID):
    try:
        cursor = mysql.connection.cursor()
        sql = """UPDATE especialidad SET NombreEspecialidad = %s, CarreraID = %s WHERE EspecialidadID = %s"""
        values = (request.json['NombreEspecialidad'], request.json['CarreraID'], EspecialidadID)
        cursor.execute(sql, values)
        mysql.connection.commit()
        return jsonify({'mensaje': "Especialidad actualizada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/materias', methods=['GET'])
def listar_materias():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT MateriaID, NombreMateria, Creditos, CarreraID, Semestre, Seguimiento, EspecialidadID FROM materia")
        datos = cursor.fetchall()
        materias = [{'MateriaID': fila[0], 'NombreMateria': fila[1], 'Creditos': fila[2], 'CarreraID': fila[3], 'Semestre': fila[4], 'Seguimiento': fila[5], 'EspecialidadID': fila[6]} for fila in datos]
        return jsonify({'materias': materias, 'mensaje': "Materias listadas."})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/materias/<MateriaID>', methods=['GET'])
def leer_materia(MateriaID):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT MateriaID, NombreMateria, Creditos, CarreraID, Semestre, Seguimiento, EspecialidadID FROM materia WHERE MateriaID = %s", (MateriaID,))
        datos = cursor.fetchone()
        if datos:
            materia = {'MateriaID': datos[0], 'NombreMateria': datos[1], 'Creditos': datos[2], 'CarreraID': datos[3], 'Semestre': datos[4], 'Seguimiento': datos[5], 'EspecialidadID': datos[6]}
            return jsonify({'materia': materia, 'mensaje': "Materia encontrada."})
        else:
            return jsonify({'mensaje': "Materia no encontrada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/materias', methods=['POST'])
def registrar_materia():
    try:
        cursor = mysql.connection.cursor()
        sql = """INSERT INTO materia (MateriaID, NombreMateria, Creditos, CarreraID, Semestre, Seguimiento, EspecialidadID) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (request.json['MateriaID'], request.json['NombreMateria'], request.json['Creditos'], request.json['CarreraID'], request.json['Semestre'], request.json['Seguimiento'], request.json['EspecialidadID'])
        cursor.execute(sql, values)
        mysql.connection.commit()
        return jsonify({'mensaje': "Materia registrada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})

@app.route('/materias/<MateriaID>', methods=['DELETE'])
def eliminar_materia(MateriaID):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM materia WHERE MateriaID = %s", (MateriaID,))
        mysql.connection.commit()
        return jsonify({'mensaje': "Materia eliminada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})


@app.route('/materias/<MateriaID>', methods=['PUT'])
def actualizar_materia(MateriaID):
    try:
        cursor = mysql.connection.cursor()
        sql = """UPDATE materia SET NombreMateria = %s, Creditos = %s, CarreraID = %s, Semestre = %s, 
          Seguimiento = %s, EspecialidadID = %s WHERE MateriaID = %s"""
        values = (request.json['NombreMateria'], request.json['Creditos'], request.json['CarreraID'], request.json['Semestre'],
                  request.json['Seguimiento'], request.json['EspecialidadID'], MateriaID)
        cursor.execute(sql, values)
        mysql.connection.commit()
        return jsonify({'mensaje': "Materia actualizada"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR!", 'error': str(ex)})
>>>>>>> bba1099 (Dockerizacion exitosa)

def pagina_no_encontrada(error):
    return "<h1> La pagina que intentas buscar no existe... </h1>", 404

<<<<<<< HEAD
if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
=======
@app.route('/test_db')
def test_db():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SHOW TABLES;")
        tablas = cursor.fetchall()
        return jsonify({'tablas': tablas, 'mensaje': "Conexión exitosa a la base de datos."})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR al conectar a la base de datos.", 'error': str(ex)})


if __name__ == "__main__":
    # Configuración de la aplicación Flask
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)

    app.run(host="0.0.0.0", port=5000)
>>>>>>> bba1099 (Dockerizacion exitosa)
