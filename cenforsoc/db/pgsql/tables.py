# -*- coding: utf-8 -*-

from sqlalchemy import (Table, Column, ForeignKey, Integer, Text, Sequence, func, DateTime)


def getAllPeriodique(metadata):
    autoload = False
    if metadata.bind.has_table('periodique'):
        autoload = True
    periodique = Table('periodique', metadata,
                        Column('per_pk', Integer(),
                               Sequence('periodique_per_pk_seq'),
                               primary_key=True),
                        Column('per_titre', Text()),
                        Column('per_description', Text()),
                        autoload=autoload,
                        extend_existing=True)
    return periodique


def getAllAuteur(metadata):
    autoload = False
    if metadata.bind.has_table('auteur'):
        autoload = True
    auteur = Table('auteur', metadata,
                        Column('auteur_pk', Integer(),
                               Sequence('auteur_auteur_pk_seq'),
                               primary_key=True),
                        Column('auteur_nom', Text()),
                        Column('auteur_prenom', Text()),
                        Column('auteur_prenom', Text()),
                        autoload=autoload,
                        extend_existing=True)
    return auteur


def getLinkLivreAuteur(metadata):
    autoload = False
    if metadata.bind.has_table('link_livre_auteur'):
        autoload = True
    linkLivreAuteur = Table('link_livre_auteur', metadata,
                             Column('livre_fk', Integer(),
                                     ForeignKey('livre.liv_pk'),
                                     primary_key=True),
                             Column('auteur_fk', Integer(),
                                     ForeignKey('auteur.auteur_pk'),
                                     primary_key=True),
                             autoload=autoload,
                             extend_existing=True)
    return linkLivreAuteur


def getAllLivre(metadata):
    autoload = False
    if metadata.bind.has_table('livre'):
        autoload = True
    livre = Table('livre', metadata,
                  Column('liv_pk', Integer(),
                         Sequence('livre_liv_pk_seq'),
                         primary_key=True),
                  Column('liv_titre', Text()),
                  Column('liv_inventaire', Text()),
                  Column('liv_cote_rang', Text()),
                  Column('liv_titre', Text()),
                  Column('liv_auteur_1', Text()),
                  Column('liv_auteur_2', Text()),
                  Column('liv_auteur_3', Text()),
                  Column('liv_edition', Text()),
                  Column('liv_lieu', Text()),
                  Column('liv_editeur', Text()),
                  Column('liv_date', Text()),
                  Column('liv_pages', Text()),
                  Column('liv_collection', Text()),
                  Column('liv_notes', Text()),
                  Column('liv_isbn', Text()),
                  Column('liv_mots_cles', Text()),
                  Column('liv_pret', Text()),
                  autoload=autoload,
                  extend_existing=True)
    return livre


def getAllFormation(metadata):
    autoload = False
    if metadata.bind.has_table('formation'):
        autoload = True
    formation = Table('formation', metadata,
                      Column('form_pk', Integer(),
                             Sequence('formation_for_pk_seq'),
                             primary_key=True),
                      Column('form_titre', Text()),
                      Column('form_duree', Text()),
                      Column('form_date_deb', DateTime(), default=func.now()),
                      Column('form_description', Text()),
                      Column('form_niveau_requis', Text()),
                      Column('form_etat', Text()),
                      autoload=autoload,
                      extend_existing=True)
    return formation


def getAllFormationInscription(metadata):
    autoload = False
    if metadata.bind.has_table('formation_inscription'):
        autoload = True
    formationInscription = Table('formation_inscription', metadata,
                                 Column('form_ins_pk', Integer(),
                                        Sequence('formation_inscription_form_ins_pk_seq'),
                                        primary_key=True),
                                 Column('form_ins_date', DateTime(), default=func.now()),
                                 Column('form_ins_nom', Text()),
                                 Column('form_ins_prenom', Text()),
                                 Column('form_ins_date_naissance', DateTime()),
                                 Column('form_ins_adresse', Text()),
                                 Column('form_ins_cp', Text()),
                                 Column('form_ins_localite', Text()),
                                 Column('form_ins_email', Text()),
                                 Column('form_ins_tel', Text()),
                                 Column('form_ins_gsm', Text()),
                                 Column('form_ins_central_pro_fgtb', Text()),
                                 Column('form_ins_regional', Text()),
                                 Column('form_ins_profession', Text()),
                                 Column('form_ins_entreprise', Text()),
                                 Column('form_ins_tel_entreprise', Text()),
                                 Column('form_ins_horaire_travail', Text()),
                                 Column('form_ins_conge_educ', Text()),
                                 Column('form_ins_conge_synd', Text()),
                                 Column('form_ins_del_synd', Text()),
                                 Column('form_ins_del_ce', Text()),
                                 Column('form_ins_del_cppt', Text()),
                                 Column('form_ins_formation_suivie', Text()),
                                 autoload=autoload,
                                 extend_existing=True)
    return formationInscription


def getLinkFormationInscription(metadata):
    autoload = False
    if metadata.bind.has_table('link_formation_inscription'):
        autoload = True
    linkFormationInscription = Table('link_formation_inscription', metadata,
                                     Column('lnk_formation_pk', Integer(),
                                            ForeignKey('formation.form_pk'),
                                            primary_key=True),
                                     Column('lnk_inscription_pk', Integer(),
                                            ForeignKey('formation_inscription.form_ins_pk'),
                                            primary_key=True),
                                     autoload=autoload,
                                     extend_existing=True)
    return linkFormationInscription


def getAllAffiche(metadata):
    autoload = False
    if metadata.bind.has_table('affiche'):
        autoload = True
    affiche = Table('affiche', metadata,
                    Column('affiche_pk', Integer(),
                           Sequence('affiche_affiche_pk_seq'),
                           primary_key=True),
                    Column('affiche_inventaire', Text()),
                    Column('affiche_titre', Text()),
                    Column('affiche_auteur', Text()),
                    Column('affiche_illustrateur', Text()),
                    Column('affiche_lieu_edition', Text()),
                    Column('affiche_editeur', Text()),
                    Column('affiche_date_edition', Text()),
                    Column('affiche_coloration', Text()),
                    Column('affiche_format', Text()),
                    Column('affiche_nbre_exemplaire', Text()),
                    Column('affiche_mot_cle', Text()),
                    Column('affiche_descriptif', Text()),
                    Column('affiche_historique', Text()),
                    Column('affiche_commanditaire', Text()),
                    Column('affiche_serie', Text()),
                    autoload=autoload,
                    extend_existing=True)
    return affiche
