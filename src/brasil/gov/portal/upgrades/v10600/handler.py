# -*- coding: utf-8 -*-
from brasil.gov.portal.config import PROJECTNAME
from brasil.gov.portal.setuphandlers import set_tinymce_formats
from plone import api
from plone.app.upgrade.utils import loadMigrationProfile

import logging


logger = logging.getLogger(PROJECTNAME)


def install_product(context):
    """Instala brasil.gov.portlets"""
    qi = api.portal.get_tool('portal_quickinstaller')
    if not qi.isProductInstalled('brasil.gov.portlets'):
        logger.info('Instalando produto brasil.gov.portlets')
        qi.installProduct('brasil.gov.portlets')
    logger.info('brasil.gov.portlets instalado')


def set_some_tiny_formats(context):
    set_tinymce_formats(context)

    # Novas regras foram adicionadas nos arquivos css.
    api.portal.get_tool('portal_css').cookResources()


def apply_profile(context):
    """Atualiza perfil para versao 10600, para registrar novas viewlets."""
    profile = 'profile-brasil.gov.portal.upgrades.v10600:default'
    loadMigrationProfile(context, profile)
    logger.info('Atualizado para versao 10600')
