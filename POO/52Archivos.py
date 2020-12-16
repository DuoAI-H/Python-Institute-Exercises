#Modos de apertura:

    #r: lectura.
        #El stream se abrira en moodo lectura.
        #Tiene que existir y ser legible.
    
    #w: escritura.
        #El stream se abrira en modo escritura.
        #Si no existe, se creara. Si existe, se borrara.

    #a: adjuntar.
        #El stream se abrira en modo adjuntar.
        #Si no existe, se creara. Si existe, se grabara desde el final del archivo.
    
    #r+ (b o t): leer y actualizar.
        #El stream se abrira en modo leer y actualizar.
        #Debe existir y ser legible.
        #Se permiten operaciones de lectura y escritura en el stream.

    #w+ (b o t): escribir y actualizar.
        #El stream se abrira en modo escribir y actualizar.
        #Si no existe, se creara. El contenido interior permanece intacto.
        #Se permiten operaciones de lectura y escritura en el stream.

    #x: creacion exclusiva.
        #Crea el archivo

#Modos de texto

    #b: modo binario

    #t: modo texto
        #Predeterminado.