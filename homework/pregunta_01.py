"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel



#funcion que retorna las dos palabras concatenadas
def pregunta_01():
    """
    Retorne el string "Hola mundo cruel!".

    Rta/
    Hola mundo cruel!

    """
    #funcion para concatenar dos palabras
    def saludo(palabra1, palabra2):
        return f"{palabra1} {palabra2}!"

    mensaje = saludo("Hola", "mundo cruel")

    return mensaje


if __name__ == "__main__":
    print(pregunta_01())
