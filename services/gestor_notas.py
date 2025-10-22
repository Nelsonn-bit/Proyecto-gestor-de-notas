import os
import shutil
from models . nota import Nota
class GestorNotas :
    """
    Administra las operaciones de creaci ón, lectura , edici ón,
    búsqueda y eliminaci ón de notas .
    """
    def __init__ ( self , carpeta =" notas ") :
        """Inicializa el gestor con la carpeta designada para almacenar las notas."""
        self . carpeta = carpeta
        if not os . path . exists ( carpeta ):
                os . makedirs ( carpeta )


    def guardar ( self , nota : Nota ) :
        """Guarda una nueva nota en la carpeta designada."""
        ruta = os . path . join ( self . carpeta , f"{ nota . nombre }. txt ")
        with open ( ruta , "w", encoding ="utf -8") as archivo :
            archivo . write ( str ( nota ))


    def leer ( self , nombre ):
        """Lee y devuelve el contenido de una nota por su nombre."""
        ruta = os . path . join ( self . carpeta , f"{ nombre }. txt ")
        if os . path . exists ( ruta ) :
            with open ( ruta , "r", encoding ="utf -8") as archivo :
                return archivo . read ()
            return " Nota no encontrada ."
        

    def listar ( self ):
        """Devuelve una lista con los nombres de todas las notas almacenadas."""
        return [a [: -4] for a in os . listdir ( self . carpeta ) if a. endswith
        (".txt ")]
    

    def buscar ( self , palabra ) :
        """Busca una palabra en todas las notas y devuelve los nombres de las notas que la contienen."""

        resultados = []
        for archivo in os . listdir ( self . carpeta ):
            ruta = os . path . join ( self . carpeta , archivo )
            with open ( ruta , "r", encoding ="utf -8") as f :
                if palabra . lower () in f. read () . lower () :
                    resultados . append ( archivo [: -4])
        return resultados
    

    def editar ( self , nombre , nuevo_contenido ) :
        """Edita una nota existente y crea un respaldo antes de modificarla."""

        # Validación de entradas
        if not nombre.strip():
            print("El nombre de la nota no puede estar vacío.")
            return False
        if len(nuevo_contenido.strip()) < 5:
            print("El contenido es muy corto (mínimo 5 caracteres).")
            return False
        
        ruta = os . path . join ( self . carpeta , f"{ nombre }. txt ")
        if os . path . exists ( ruta ) :
            respaldo = os . path . join ( self . carpeta , f"{ nombre } _bak . txt ")
            shutil . copy ( ruta , respaldo )
            with open ( ruta , "w", encoding ="utf -8") as archivo :
                archivo . write ( nuevo_contenido )
            return True
        return False
    

    def eliminar ( self , nombre ):
        """Elimina una nota por nombre y responde con mensajes seguros."""
        ruta = os . path . join ( self . carpeta , f"{ nombre }. txt ")
        if os . path . exists ( ruta ) :
            os . remove ( ruta )
            return True
        return False
