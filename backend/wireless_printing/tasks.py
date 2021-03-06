from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .util import remove_credits


@shared_task
def print_file(path, from_page, to_page, color, credits, user):
    # SEND FILE TO PRINTER FOR PRINTING

    # ON SUCCESSFUL PRINT REMOVE CREDITS
    remove_credits(user, credits, True)
    pass
