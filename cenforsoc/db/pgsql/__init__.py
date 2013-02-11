import logging
from z3c.sqlalchemy import createSAWrapper
from zope.component import getUtility
from affinitic.pwmanager.interfaces import IPasswordManager

LOGGER = 'cenforsoc.db.pgsql'
logging.getLogger(LOGGER).info('cenforsoc.db.pgsql - Installing Product')


def initialize(context):
    pwManager = getUtility(IPasswordManager, 'pg')
    connString = 'postgresql://%s@localhost/cenforsoc' % pwManager.getLoginPassWithSeparator(':')
    createSAWrapper(connString,
                    forZope=True,
                    echo=False,
                    engine_options={'convert_unicode': True},
                    name='cenforsoc',
                    model='cenforsocMappings')
