from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
  def create_user(self, email, username, password=None):
    if not email:
      raise ValueError("Users must have an email address")
    if not username:
      raise ValueError("Users must have a username")

    if not full_name:
      raise ValueError("This field cannot be blank")
    if not artist_type:
      raise ValueError("This field cannot be blank")

    if not bio:
      raise ValueError("This field cannot be blank")

    user = self.model(
         email = self.normalize_email(email),
         username = username,
         full_name = full_name,
         artist_type = artist_type,
         bio = bio,
         website = website,
         facebook = facebook,
         instagram = instagram
    )

    user.set_password(password)
    user.save(using = self._db)
    return user

  def create_superuser(self, email, username ,password):
    user = self.create_user(
      email = self.normalize_email(email),
      username = username,
      password = password
    )

    user.is_admin = True
    user.is_staff = True
    user.is_superuser =True
    user.save(using = self._db)
    return user



class Account(AbstractBaseUser):
    """docstring for Account"""
    email 		= models.EmailField(verbose_name = "email", max_length= 60, unique = True)
    username 	= models.CharField(max_length = 40, unique = True)
    full_name = models.CharField(max_length=50)
    instagram   = models.URLField()
    facebook    = models.URLField()
    artist_type = models.CharField(max_length=50)
    bio         = models.CharField(max_length=150)
    profile_image = models.ImageField() 
    website     = models.URLField()
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add = True) 
    last_login  = models.DateTimeField(verbose_name= 'last login', auto_now= True)
    is_admin    = models.BooleanField(default= False)
    is_active   = models.BooleanField(default= True)
    is_staff    = models.BooleanField(default = False)
    is_superuser= models.BooleanField(default= False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()

    def __str__(self):
      return self.email + "," + self.username

    def has_perm(self,perm, obj=None):
      return self.is_admin
    def has_module_perms(self, app_label):
      return True


class Profile(models.Model):
  full_name       = models.CharField(max_length=50)
  profile_image   = models.ImageField()
  artist_category = models.CharField(max_length= 50)
  bio             = models.CharField(max_length= 100)
  date_created	    = models.DateTimeField(verbose_name='date  created', auto_now_add = True) 
  

  def __str__(self):
    return self.full_name
  

  # full_name 		= models.CharField(max_length = 50)
	# profile_image	= models.ImageField(upload_to=upload_location, null=True, blank=True)
	# artist_category = models.CharField(max_length= 50)
	# bio = models.CharField(max_length= 100)
	# achievements  = models.CharField(max_length=100)
	# slug 					= models.SlugField(blank=True, unique=True)

  # def __str__(self):
	# 	return self.full_name + ","+ self.artist_category + "," +self.bio


