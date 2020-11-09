from project import db
from project.tags.models import Tag
from project.serate.models import Serata

'''
Oggetti Tabella relativi al modulo "corsi"
'''
# corso_tags - tabella di relazione N:N tra Corso e Tag
tags = db.Table(
    "corso_tags",
    #__table_args__ = {'extend_existing': True},
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
    def __init__(self, nome, insegnante, livello, descrizione):
        self.nome = nome
        self.insegnante = insegnante
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


