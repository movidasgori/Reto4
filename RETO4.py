class Entregable():

    def entregar(self):
        print(self.titulo, "-> ENTREGADO")
        self._entregado = True

    def devolver(self):
        print(self.titulo, "-> DEVUELTO")
        self._entregado = False

    def isEntregado(self):
        return self._entregado

    def compareTo(self, a):

        if (isinstance(a, Serie)):

            if (self.num_temporadas > a.num_temporadas):
                return True

            if (self.num_temporadas < a.num_temporadas):
                return False

        if (isinstance(a, Videojuego)):

            if (self.horas_estimadas > a.horas_estimadas):
                return True

            if (self.horas_estimadas < a.horas_estimadas):
                return False


class Serie(Entregable):
    # Propiedades
    _titulo = ''
    _num_temporadas = ''
    _genero = ''
    _creador = ''
    _entregado = False

    # Constructor
    def __init__(self):
        self._titulo = ''
        self._num_temporadas = 3
        self._genero = ''
        self._creador = ''

    # Get / Set

    # ---TITULO
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    # ---TEMPORADAS
    @property
    def num_temporadas(self):
        return self._num_temporadas

    @num_temporadas.setter
    def num_temporadas(self, num_temporadas):
        self._num_temporadas = num_temporadas

    # ---GENERO
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    # ---CREADOR
    @property
    def creador(self):
        return self._creador

    @creador.setter
    def creador(self, creador):
        self._creador = creador

    # VISTA ATRIBUTOS "__str__"
    def __str__(self):
        return 'Titulo: ' + self.titulo \
               + '\n Genero: ' + self.genero \
               + '\n Temporadas: ' + str(self.num_temporadas) \
               + '\n Creador: ' + self.creador


class Videojuego(Entregable):
    # Propiedades
    _titulo = ''
    _horas_estimadas = ''
    _genero = ''
    _compania = ''
    _entregado = False

    # Constructor
    def __init__(self):
        self._titulo = ''
        self._horas_estimadas = 10
        self._genero = ''
        self._compania = ''

    # Get / Set

    # ---TITULO
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    # ---HORAS ESTIMADAS
    @property
    def horas_estimadas(self):
        return self._horas_estimadas

    @horas_estimadas.setter
    def horas_estimadas(self, horas_estimadas):
        self._horas_estimadas = horas_estimadas

    # ---GENERO
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    # ---COMPAÑIA
    @property
    def compania(self):
        return self._compania

    @compania.setter
    def compania(self, compania):
        self._compania = compania

    # Get
    def __str__(self):
        return "Titulo: " + self.titulo + \
               "\n Horas estimadas: " + str(self.horas_estimadas) + \
               "\n Genero : " + self.genero + \
               "\n Compañia : " + self.compania

    def titulo(self):
        print(f'Titulo : {self.titulo}')
        return self.titulo


########################################################################

def videoclub():
    ###(1)

    # Array SERIES y JUEGOS
    series = []
    juegos = []

    ###(2)

    # Creamos objetos SERIE y JUEGO y los añadimos al array

    # SERIES
    s1 = Serie()
    s1.titulo = 'The Wire'
    s1.genero = 'Thriller'
    s1.num_temporadas = 6
    s1.creador = 'David Simon'
    series.append(s1)

    s2 = Serie()
    s2.titulo = 'Breaking Bad'
    s2.genero = 'Thriller'
    s2.num_temporadas = 5
    s2.creador = 'Vince Gilligan'
    series.append(s2)

    s3 = Serie()
    s3.titulo = 'Los Simpson'
    s3.genero = 'Animacion'
    s3.num_temporadas = 32
    s3.creador = 'Matt Groening'
    series.append(s3)

    s4 = Serie()
    s4.titulo = 'Juego de tronos'
    s4.genero = 'Aventuras'
    s4.num_temporadas = 32
    s4.creador = 'David Benioff'
    series.append(s4)

    s5 = Serie()
    s5.titulo = 'Los Soprano'
    s5.genero = 'Thriller'
    s5.num_temporadas = 6
    s5.creador = 'David Chase'
    series.append(s5)

    # JUEGOS
    j1 = Videojuego()
    j1.titulo = 'Final Fantasy'
    j1.genero = 'RPG'
    j1.horas_estimadas = 100
    j1.compania = 'Square Enix'
    juegos.append(j1)

    j2 = Videojuego()
    j2.titulo = 'Diablo'
    j2.genero = 'RPG'
    j2.horas_estimadas = 40
    j2.compania = 'Blizzard Entertainment'
    juegos.append(j2)

    j3 = Videojuego()
    j3.titulo = 'Half-Life'
    j3.genero = 'Shotter'
    j3.horas_estimadas = 50
    j3.compania = 'Valve'
    juegos.append(j3)

    j4 = Videojuego()
    j4.titulo = 'Age of Empiries'
    j4.genero = 'Estrategia'
    j4.horas_estimadas = 70
    j4.compania = 'Microsoft Studios'
    juegos.append(j4)

    j5 = Videojuego()
    j5.titulo = 'Age of Empiries II'
    j5.genero = 'Estrategia'
    j5.horas_estimadas = 80
    j5.compania = 'Microsoft Studios'
    juegos.append(j5)

    # Mostramos series
    print('\nSERIES REGISTRADAS\n****************************')
    for serie in series:
        print('\n->', serie)

    # Mostramos juegos
    print('\nJUEGOS REGISTRADOS\n********************************')
    for juego in juegos:
        print('\n->', juego)

    ###(3)

    # Entregamos series y juegos
    print('\nENTREGAMOS SERIES\n****************************')
    s1.entregar()
    s2.entregar()
    s3.entregar()

    print('\nENTREGAMOS JUEGOS\n****************************')
    j1.entregar()
    j2.entregar()
    j4.entregar()
    j5.entregar()

    ###(4)

    # Contamos los objetos entregadas y los devolvemos usando "is.Entregado()"
    def recuento_devolver(AR):

        CONT = 0

        for VAR in AR:
            if (VAR.isEntregado()):
                CONT += 1

        print('ARTICULOS entregadas:', CONT, '\n')

        for VAR in AR:
            if VAR.isEntregado():
                VAR.devolver()

    # Ejecutamos funcion "recuento_devolver"
    print('\n\nRECUENTO SERIES')
    print('-----------------------------')
    recuento_devolver(series)

    print('\n\nRECUENTO JUEGOS')
    print('-----------------------------')
    recuento_devolver(juegos)

    # Comparamos los articulos con "compareTo()"
    def mayor(lista):

        VAR = lista[0]

        for i in lista:
            if (VAR.compareTo(i) != True):
                VAR = i

        print('\nArticulo mayor: \n', VAR)

    # Ejecutamos funcion "mayor"
    mayor(series)
    mayor(juegos)


videoclub()
