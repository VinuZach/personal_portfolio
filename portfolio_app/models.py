from django.db import models


class ProjectDetails(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(blank=False)
    project_link = models.TextField(max_length=100, blank=True, null=True)


class Technology(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)



class TechInProject(models.Model):
    project_id = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE)
    tech_id = models.ForeignKey(Technology, on_delete=models.CASCADE, default="")


class Images(models.Model):
    image_origin = models.CharField(max_length=30, blank=False,default="")
    image_tag = models.CharField(max_length=30, blank=False)
    imageData = models.ImageField(upload_to='project_images/', default=None)

