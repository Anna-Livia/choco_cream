from django.db import models

# Create your models here.
class Transaction(models.Model):
    amount = models.FloatField(default=0)
    # TODO date ou une ref unique
    # TODO Narration (tier)
    # TODO compte d'entree / compte de sortie
    # TODO flag / status

# TODO Transaction
    # TODO recurrence

# TODO comptes
    # TODO fournisseur
    # TODO comptes internes


# TODO Budget mensuel
 # TODO ensemble de transaction


