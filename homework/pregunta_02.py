"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel




def pregunta_02():
    """
    Retorne el string "Hello cruel world!".

    Rta/
    Hello cruel world!

    """

    #funcion para concatenar dos palabras
    def saludo2(palabra1, palabra2):
        return f"{palabra1} {palabra2}!"

    mensaje2 = saludo2("Hello", "cruel world")

    return mensaje2


if __name__ == "__main__":
    print(pregunta_02())
