from z3c.sqlalchemy import Model
from z3c.sqlalchemy.interfaces import IModelProvider
from zope.interface import implements

from sqlalchemy.orm import mapper
from cenforsoc.db.pgsql.baseTypes import (Periodique,
                                          Livre,
                                          Formation,
                                          FormationInscription,
                                          LinkFormationInscription)
from cenforsoc.db.pgsql.tables import (getAllPeriodique,
                                       getAllLivre,
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

## table livre ##
        livreTable = getAllLivre(metadata)
        livreTable.create(checkfirst=True)
        mapper(Livre, livreTable)
        model.add('livre', table=livreTable, mapper_class=Livre)

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

## table jointure likn_formation_inscription
        linkFormationInscriptionTable = getLinkFormationInscription(metadata)
        linkFormationInscriptionTable.create(checkfirst=True)
        mapper(LinkFormationInscription, linkFormationInscriptionTable,
                primary_key=[linkFormationInscriptionTable.c.lnk_formation_pk, linkFormationInscriptionTable.c.lnk_inscription_pk])
        model.add('link_formation_inscription',
                   table=linkFormationInscriptionTable,
                   mapper_class=LinkFormationInscription)

        metadata.create_all()
        return model
