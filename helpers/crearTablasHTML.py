def crearTablas(dataframe, nombreTabla):
    archivoHTML = dataframe.to_html()  # Aqui tengo el dataframe
    archivo = open(f"./tablas/{nombreTabla}.html", "w",encoding="UTF-8")  # tengo un archivo html vacio
    archivo.write(
        """
        <!DOCTYPE html>
        <html>
        <head>
        <title>tablas</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        </head>
        <body>
    """
    )
    archivo.write(archivoHTML)
    archivo.write(
        """
        </body>
        </html>
    """
    )
    archivo.close()
