from django import models


class Store ():
    Tienda= models.Charfield(Max_length=40)
    Categoria= models.Charfield(Max_lenght=30)

class User(models.Model):
    Nombre= models.Charfield(Max_length=30)
    Apellido= models.Charfield(Max_length=30)
    Email= models.EmailField()

class Item()
    producto= models.Charfield(Max_length=30)
    product_id= models.IntegerField()
    precio= models.IntegerField()
    prod_detail= models.Charfield(Max_lenght=50)

