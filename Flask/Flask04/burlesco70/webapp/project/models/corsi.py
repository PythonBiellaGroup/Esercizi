from project import db
from project.tags.models import Tag

'''
Oggetti Tabella relativi al modulo "corsi"
'''


# corso_tags - tabella di relazione N:N tra Corso e Tag
tags = db.Table(
    "corso_tags",
    db.Column("corso_id", db.Integer, db.ForeignKey("corso.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)

# corso - tabella con i corsi
class Corso(db.Model):
    # Nome della tabella
    __tablename__ = "corso"

    # Struttura/Attributi
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    insegnante = db.Column(db.String(100))
    # Il numero delle lezioni è un attributo calcolabile
    # lezioni = db.Column(db.Integer())
    livello = db.Column(db.String(100))
    descrizione = db.Column(db.String(255))

    # Relazione 1:n; ordinamento serate per data
    serate = db.relationship(
        "Serata", order_by="asc(Serata.data)", backref="corso", lazy="subquery"
    )

    # Relazione n:n
    tags = db.relationship(
        "Tag", secondary=tags, lazy="subquery", backref=db.backref("corso", lazy=True),
    )

    # Costruttore

    # NOTA: Lasciare il costruttore crea problemi nella gestione della form di creazione
    def __init__(self, nome, insegnante, livello, descrizione):
        self.nome = nome
        self.insegnante = insegnante
        # self.lezioni = lezioni
        self.livello = livello
        self.descrizione = descrizione
        # self.serate = serate
        # self.tags = tags

    # Visualize object corso informations
    def __repr__(self):
        return "\n{}: {} è tenuto da {}. Livello {}. Id {}. Tags {}".format(
            self.nome,
            self.descrizione,
            self.insegnante,
            self.livello,
            self.id,
            self.tags,
        )



# Tabella di relazione 1 Corso : N Serate
class Serata(db.Model):

    __tablename__ = "serata"

    __table_args__ = (db.UniqueConstraint("id", "data", name="contraint_serata"),)

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
