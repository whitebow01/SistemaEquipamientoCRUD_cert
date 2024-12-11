#Instalar en terminal 
# pip install mysql.connector
# pip install requests
# pip install pymysql
# pip install tabulate
# pip install pwinput 

from hashlib import md5
from pwinput import pwinput 
import pymysql #Necesario para no mostrar el codigo de acceso en pantalla

class DataBaseMD5:
    def __init__(self):
        self.conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='Inacap22.', 
            database='certamen3'
        )
        self.cursor = self.conexion.cursor()

    def insertar_registro(self):
        
        num_equipo = input("Ingrese número de equipamiento: ")
        codigo_acceso = pwinput("Ingrese codigo de acceso: ")
        fecha_fabricacion = input("Ingrese fecha de fabricacion (DD-MM-YYYY): ")
        precio_equipo = int(input("Ingrese precio equipo: "))

        # codigo encriptada
        codigo_enc = md5(codigo_acceso.encode('utf-8')).hexdigest()

        # Validamos numero de equipo
        sql_validar = 'select NumEquip from Equipamientos where NumEquip ='+repr(num_equipo)
        # Insertamos
        try:
            self.cursor.execute(sql_validar)
            if self.cursor.fetchone() is None:  # Si no existe, insertamos
                
                sql_insertar = "insert into Equipamientos values ("+repr(num_equipo)+","+repr(codigo_enc)+","+repr(fecha_fabricacion)+","+repr(precio_equipo)+")"
                    
                try:
                    self.cursor.execute(sql_insertar)
                    self.conexion.commit()
                    print("Registro insertado correctamente.")
                except Exception as err:
                    self.conexion.rollback()
                    print(f"Error al insertar el registro:{err}")
            else:
                print("El número de equipo ya existe. Intente con otro número.")
        except Exception as err:
            print(f"Error al validar el número de equipo:{err}")


    def login(self):
        try:
            num_equipo = input("Ingrese número de equipo: ")
            codigo_acceso = pwinput("Ingrese codigo acceso: ")

            # Encriptamos codigo con md5
            codigo_enc = md5(codigo_acceso.encode('utf-8')).hexdigest()

            # Verificamos
            self.cursor.execute("select count(*) from Equipamientos where NumEquip = %s and codAcceso = %s",(num_equipo, codigo_enc),)
            cuenta_existente = self.cursor.fetchone()[0]

            if cuenta_existente:
                #Busca el registro y lo muestra 
                print("------------------------------------------------------------")
                print("Numero de equipo y codigo correctos!")


                self.cursor.execute("select * from Equipamientos where NumEquip = %s", (num_equipo,))               
                registro = self.cursor.fetchone()

                if registro:
                    print("------------------------------------------------------------")
                    print(f"{'Numero Equip.':15}{'Fecha Equip.':15}{'Precio Equip.':15}")

                    print(f"{registro[0]:5}         {registro[2]:15}{registro[3]:10}")
                    print("------------------------------------------------------------")
                else:
                    print("El número de Equipamiento no existe")

            else:
                print("Número de equipo o codigo de acceso incorrectos.")
        except Exception as err:
            print(f"Error al intentar iniciar sesión: {err}")


    def mostrar_todos(self):
        sql = 'select * from Equipamientos'
        try: 
            self.cursor.execute(sql)
            repu = self.cursor.fetchall()
            print("------------------------------------------------------------")    
            print(f"{'Numero Equip.':15}{'Fecha Equip.':15}{'Precio Equip.':10}")
            print("------------------------------------------------------------")

            for rep in repu:
                print(f"{rep[0]:5}          {rep[2]:15}{rep[3]:15}")
                
        except Exception as err:
            print(f"No se encuentran registros en la base de datos:{err}")


    def mostrar_rango_precios(self):
        try:
            self.cursor.execute("select * from Equipamientos where precioEq BETWEEN 100000 AND 500000")
            registros = self.cursor.fetchall()
            
            if registros:
                print("----------------------------------------")
                print("Hay registros en ese rango de precios:")
                print("----------------------------------------")

                for registro in registros:
                    print("------------------------------------------------------------")
                    print(f"{'Numero Equip.':15}{'Fecha Equip.':15}{'Precio Equip.':15}")

                    print(f"{registro[0]:5}         {registro[2]:15}{registro[3]:10}")
                    print("------------------------------------------------------------")
            else:
                print("No hay registros con precio entre 100.000 y 500.000 ")
        except Exception as err:
            print(f"Error al obtener los registros: {err}")

    def modificar_registro(self):
        num_equipo = input("Ingrese el número de equipamiento que desea modificar su PRECIO: ")
        #validacion
        try:
            self.cursor.execute("select * from Equipamientos where NumEquip = %s", (num_equipo,))
            registro = self.cursor.fetchone()

            if registro:
                #print(f"Registro actual: {registro}") 
                print("----------------------------------")
                print("PRECIO actual del Equipamiento:")
                print("----------------------------------")

                print(f"{'Numero Equip.':15}{'Fecha Equip.':15}{'Precio Equip.':15}")

                print(f"{registro[0]:5}         {registro[2]:15}{registro[3]:10}")
                print("-----------------------------------------------------------")
                
                
                nuevo_precio = int(input("Ingrese el nuevo PRECIO: "))
                self.cursor.execute("update Equipamientos set precioEq = %s where NumEquip = %s", (nuevo_precio, num_equipo))
                self.conexion.commit()

                print("-------------------------------------")
                print("PRECIO modificado del Equipamiento:")
                print("-------------------------------------")

                
            else:
                print("El número de Equipamiento no existe")
        except Exception as err:
            print(f"Error al modificar el PRECIO del registro: {err}")
            self.conexion.rollback()


    def eliminar_registro(self):
        try:
            num_equipo = input("Ingrese el número Equipamiento que desea eliminar su registro: ")

            self.cursor.execute("select * from Equipamientos where NumEquip = %s", (num_equipo,))
            registro = self.cursor.fetchone()

            if registro:
                self.cursor.execute("delete from Equipamientos where NumEquip = %s", (num_equipo,))
                self.conexion.commit()
                print("Equipamiento eliminado correctamente.")
            else:
                print("El número de Equipamiento no existe.")
        except Exception as err:
            print(f"Error al eliminar el Equipamiento: {err}")