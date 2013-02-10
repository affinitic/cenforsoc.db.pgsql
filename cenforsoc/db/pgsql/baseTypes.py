# -*- coding: utf-8 -*-
"""
cenforsoc.db.pgsql

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: baseTypes.py 5772 2011-11-06 15:59:55Z amulux $
"""
from z3c.sqlalchemy.mapper import MappedClassBase


class Periodique(MappedClassBase):
    c = None


class Auteur(MappedClassBase):
    c = None


class Livre(MappedClassBase):
    c = None


class LinkLivreAuteur(MappedClassBase):
    c = None


class Affiche(MappedClassBase):
    c = None


class Formation(MappedClassBase):
    c = None


class FormationInscription(MappedClassBase):
    c = None


class LinkFormationInscription(MappedClassBase):
    c = None
