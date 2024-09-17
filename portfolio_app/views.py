from django.shortcuts import render
from .models import *
import json
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.serializers import serialize
from .serializers import *

# Create your views here.
no_of_projects = "30+"
years_of_experience = "8"


def home_page(request):
    project_details = ProjectDetails.objects.all()
    result_value = []
    for project_item in project_details.values():
        modified_item = {"project": project_item}
        tech_in_projects = list(TechInProject.objects.select_related('tech_id', 'project_id').filter(
            project_id__id=project_item['id']).values(
            'project_id__id', 'tech_id__name'
        ))
        print(tech_in_projects)

        modified_item["tech"] = tech_in_projects
        modified_item["images"] = list(
            Images.objects.filter(image_origin="Project", image_tag=project_item['id']).values())
        result_value.append(modified_item)
    return render(request, "home.html", {"result": result_value, "no_of_projects": no_of_projects,
                                         "years_of_experience": years_of_experience})


@api_view(['GET'])
def retrieve_project_details(request):
    project_details = ProjectDetails.objects.all()
    result_value = []
    for project_item in project_details.values():
        modified_item = {"project": project_item}
        tech_in_projects = list(TechInProject.objects.select_related('tech_id', 'project_id').filter(
            project_id__id=project_item['id']).values(
            'project_id__id', 'tech_id__name'
        ))
        print(tech_in_projects)

        modified_item["tech"] = tech_in_projects
        modified_item["images"] = list(
            Images.objects.filter(image_origin="Project", image_tag=project_item['id']).values())
        result_value.append(modified_item)
    return JsonResponse({"result": result_value})
