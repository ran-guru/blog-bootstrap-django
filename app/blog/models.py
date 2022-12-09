from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name of the category",max_length=100,null=False)
    state = models.BooleanField("State of the category",default=True)
    creation_date = models.DateField("Creation date",auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Autor's mame",max_length=100,null=False)
    last_name = models.CharField("Autor's last name",max_length=100,null=False)

    facebook = models.URLField('Facebook',null=True)
    twitter = models.URLField('Twitter',null=True)
    instagram = models.URLField('Instagram',null=True)
    web = models.URLField('Web',null=True)

    email = models.EmailField('Email',max_length=100,null=False)
    state = models.BooleanField('State of the autor',default=True)
    creation_date = models.DateField('Create Date',auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autors'

    def __str__(self):
        return "{0} {1}".format(self.last_name, self.name)



class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title',max_length=90,null=False)
    slug = models.CharField('Slug',max_length=100,null=False)
    description = models.CharField('Description',max_length=100,null=False)
    image = models.URLField(max_length=255,null=False)

    content = RichTextField('content')

    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    state = models.BooleanField("Post/No Post",default=True)
    creation_date = models.DateField('Creation date',auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
