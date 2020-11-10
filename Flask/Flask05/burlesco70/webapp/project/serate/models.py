from project import db

# Tabella di relazione 1 Corso : N Serate
class Serata(db.Model):

    __tablename__ = "serata"

    __table_args__ = (db.UniqueConstraint("id", "data", name="constraint_serata"),)

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descrizione = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime(), nullable=False)
    link_partecipazione = db.Column(db.String(255), nullable=True)
    link_registrazione = db.Column(db.String(255), nullable=True)

    corso_id = db.Column(db.Integer(), db.ForeignKey("corso.id"))

    def __init__(self, nome, descrizione, data, link_partecipazione='', link_registrazione=''):
        self.nome = nome
        self.descrizione = descrizione
        self.data = data
        self.link_partecipazione = link_partecipazione
        self.link_registrazione = link_registrazione

    def __repr__(self):
        return "<Descrizione '{}'. Link registrazione>".format(self.descrizione, self.link_registrazione)