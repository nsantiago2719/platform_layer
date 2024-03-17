from django.shortcuts import render

from .models import Cluster


def index(request):
    clusters = Cluster.objects.order_by("id")
    context = {
        "cluster_list": clusters,
    }
    return render(request, "clusters/index.html", context)
