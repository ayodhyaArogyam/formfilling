from django.db import models

# Create your models here.


class FormfillingUser(models.Model):
    first_name = models.CharField(max_length=224)
    last_name = models.CharField(max_length=224)
    who_invited = models.CharField(max_length=244 )
    date_visit = models.DateField( auto_now=False, auto_now_add=False)
    hear_about = models.CharField(max_length=224)
    company_name = models.CharField(max_length=224)
    Your_industry = models.CharField(max_length= 255)
    professional_classifiction = models.CharField(max_length=255)
    Address1 = models.CharField(max_length=255)
    Address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal = models.IntegerField()
    email = models.EmailField(max_length=254)
    website = models.CharField(max_length=254)
    number1 = models.IntegerField()
    number2 = models.IntegerField(null=True , blank=True , default=0)
    gst = models.CharField(null=True,blank=True,default='no data',max_length=224)
    experience = models.CharField(max_length=254)
    time_spend = models.CharField(max_length=254)
    edu_background = models.CharField(max_length=254)
    revoke_license = models.BooleanField(default=False)
    primary_occupation = models.BooleanField(default=False)
    commitment = models.BooleanField(default=False)
    qualified_substitue = models.BooleanField(default=False)
    bring_referral = models.BooleanField(default=True)
    quantity_referral = models.IntegerField(default=0)
    bkmember = models.BooleanField(default=False)
    otherOrg = models.BooleanField(default=False)


class Referralform(models.Model):
    ref_firs_name = models.CharField(max_length=254)
    ref_last_name = models.CharField(max_length=254)
    ref_bussiness_name = models.CharField(max_length=254, null=True ,blank=True)
    ref_phone = models.IntegerField()
    ref_email = models.EmailField()
    ref_business_rel1 = models.CharField(max_length=254)
    formuser = models.ForeignKey(to='FormfillingUser',on_delete=models.CASCADE)
    
    




