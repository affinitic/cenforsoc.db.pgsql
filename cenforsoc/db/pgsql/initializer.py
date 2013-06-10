from z3c.sqlalchemy import Model
from z3c.sqlalchemy.interfaces import IModelProvider
from zope.interface import implements

from sqlalchemy.orm import mapper, relationship
from cenforsoc.db.pgsql.baseTypes import (Periodique,
                                          Auteur,
                                          Livre,
                                          Affiche,
                                          LinkLivreAuteur,
                                          Formation,
                                          FormationInscription,
                                          LinkFormationInscription)
from cenforsoc.db.pgsql.tables import (getAllPeriodique,
                                       getAllAuteur,
                                       getAllLivre,
                                       getLinkLivreAuteur,
                                       getAllAffiche,
                                       getAllFormation,
                                       getAllFormationInscription,
                                       getLinkFormationInscription
                                       )


class CenforsocModel(object):
    """
    A model providers provides information about the tables to be used
    and the mapper classes.
    """
    implements(IModelProvider)

    def getModel(self, metadata=None):
        """
            table de demo employe
        """
        model = Model()
        model.metadata = metadata

## table periodique ##
        periodiqueTable = getAllPeriodique(metadata)
        periodiqueTable.create(checkfirst=True)
        mapper(Periodique, periodiqueTable)
        model.add('periodique', table=periodiqueTable, mapper_class=Periodique)

## table auteur ##
        auteurTable = getAllAuteur(metadata)
        auteurTable.create(checkfirst=True)
        mapper(Auteur, auteurTable)
        model.add('auteur', table=auteurTable, mapper_class=Auteur)

## table livre ##
        livreTable = getAllLivre(metadata)
        livreTable.create(checkfirst=True)
        mapper(Livre, livreTable)
        model.add('livre', table=livreTable, mapper_class=Livre)

## table jointure likn_livre_auteur ##
        linkLivreAuteurTable = getLinkLivreAuteur(metadata)
        linkLivreAuteurTable.create(checkfirst=True)
        mapper(LinkLivreAuteur, linkLivreAuteurTable,
                primary_key=[linkLivreAuteurTable.c.livre_fk, linkLivreAuteurTable.c.auteur_fk],
                properties={'livres': relationship(Livre,
                                                   order_by=[livreTable.c.liv_titre]),
                            'auteurs': relationship(Auteur,
                                                    order_by=[auteurTable.c.auteur_nom])})
        model.add('link_livre_auteur',
                   table=linkLivreAuteurTable,
                   mapper_class=LinkLivreAuteur)

## table affiche ##
        afficheTable = getAllAffiche(metadata)
        afficheTable.create(checkfirst=True)
        mapper(Affiche, afficheTable)
        model.add('affiche', table=afficheTable, mapper_class=Affiche)

## table formation ##
        formationTable = getAllFormation(metadata)
        formationTable.create(checkfirst=True)
        mapper(Formation, formationTable)
        model.add('formation', table=formationTable, mapper_class=Formation)

## table formation_inscription ##
        formationInscriptionTable = getAllFormationInscription(metadata)
        formationInscriptionTable.create(checkfirst=True)
        mapper(FormationInscription, formationInscriptionTable)
        model.add('formation_inscription', table=formationInscriptionTable, mapper_class=FormationInscription)

## table jointure link_formation_inscription
        linkFormationInscriptionTable = getLinkFormationInscription(metadata)
        linkFormationInscriptionTable.create(checkfirst=True)
        mapper(LinkFormationInscription, linkFormationInscriptionTable,
                primary_key=[linkFormationInscriptionTable.c.lnk_formation_pk, linkFormationInscriptionTable.c.lnk_inscription_pk],
                properties={'formations' : relationship(Formation, order_by=[formationTable.c.form_titre]),
                            'inscrits' : relationship(FormationInscription, order_by=[formationInscriptionTable.c.form_ins_nom])})
        model.add('link_formation_inscription',
                   table=linkFormationInscriptionTable,
                   mapper_class=LinkFormationInscription)

        metadata.create_all()
        return model
