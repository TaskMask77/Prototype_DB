from source.database.db_mysql import get_connection


class modelo_usuario:

    @classmethod
    def get_usuario_list(cls):
        conexion = get_connection()
        with conexion.cursor() as cursor:
            SQLITO = "SELECT nombre_usuario, apellido_user, Telefono_usuario, fecha_nac, id_rol FROM usuario; "
            cursor.execute()
            listusers_ctrl = cursor.fetchall()
        conexion.close()
        return listusers_ctrl


