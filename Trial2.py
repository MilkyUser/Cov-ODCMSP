import pandas

data = pandas.read_csv('OD_2017.csv')


class Visitante:

	def __init__(self, visitante_id: int):
		self.visitante_id = visitante_id


class Local:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visitantes = []

    def add_visitante(self, visitante: Visitante):
        self.visitantes.append(visitante)


locais = {}
for row in data.itertuples():
    x, y = row.CO_DOM_X, row.CO_DOM_Y

    if (x, y) not in locais:
        locais[(x, y)] = Local(row.CO_DOM_X, row.CO_DOM_Y)
        

visitantes = {}
for row in data.itertuples():
    visitante_id = row.ID_PESS
    if visitante_id not in visitantes:
        visitantes[visitante_id] = Visitante(visitante_id)

    x, y = row.CO_DOM_X, row.CO_DOM_Y
    visitante = visitantes[visitante_id]
    locais[(x, y)].add_visitante(visitante)
    