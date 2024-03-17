from django.db import models


class Cluster(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    version = models.CharField(max_length=5)
    kubeconfig = models.TextField()
