from django.db import models
from django.contrib.auth.models import User,AbstractUser,AbstractBaseUser
# Create your models here.

class NetflixUser(AbstractUser):
    email = models.EmailField(("E-mail adresi"), max_length=254,unique=True)
    avatar = models.ImageField(("Profil Fotoğrafı"), upload_to="Users/Avatars/")