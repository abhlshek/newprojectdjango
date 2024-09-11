from django.db import models
class QuizModel(models.Model):
    
    question = models.CharField(max_length = 300)
    opta = models.CharField(max_length = 50)
    optb = models.CharField(max_length = 50)
    optc = models.CharField(max_length = 50)
    optd = models.CharField(max_length = 50)
    correctanswer = models.IntegerField()
    
    class Meta:
        db_table="questions"
        
        
class cock(models.Model):
    coname=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    
    
    class Meta:
        db_table="cock"
        
        
        
class Entry(models.Model):
    booktitle=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)
    tel=models.CharField(max_length=50)
    
    class Meta:
        db_table="entry"
        
        
        
class Admission(models.Model):
    name=models.CharField(max_length=100)
    father=models.CharField(max_length=100)
    mother=models.CharField(max_length=100)
    dateofbirth=models.CharField(max_length=100)
    male=models.CharField(max_length=20)
    female=models.CharField(max_length=20)
    single=models.CharField(max_length=20)
    married=models.CharField(max_length=20)
    presentaddress=models.CharField(max_length=100)
    permanentaddress=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    sql=models.CharField(max_length=100)
    java=models.CharField(max_length=100)
    html=models.CharField(max_length=100)
    python=models.CharField(max_length=100)
    css=models.CharField(max_length=100)
    bootstrap=models.CharField(max_length=100)


    class Meta:
        db_table="admissions"




class PhoneBook(models.Model):
    name=models.CharField(max_length=100)




    class Meta:
        db_table="phonebook"










class collage(models.Model):
    name=models.CharField(max_length=150)
    cla = models.CharField(max_length=100)
    
    
    class Meta:
        db_table="collage"



class Form(models.Model):
    name=models.CharField(max_length=100)
    middlename=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    
    class Meta:
        db_table="froms"




class Marksheet(models.Model):
    roll= models.CharField(max_length=100)
    name=models.CharField(max_length=80)
    java=models.CharField(max_length=100)
    python=models.CharField(max_length=50)
    c=models.CharField(max_length=100)
    
    class Meta:
        db_table="results"
        
        
class company(models.Model):
    name=models.CharField(max_length=100)
    comapnyname=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    
    class Meta:
        db_table="company"



class customer(models.Model):
    customername=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    age=models.IntegerField(default=100)
    phone=models.IntegerField(default=100)
    
    
    class Meta:
        db_table="customer"



class Hotal(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    
    class Meta:
        db_table="hotal"




class item(models.Model):
    shopname=models.CharField(max_length=100)
    itemno=models.IntegerField(max_length=100)
    itemname=models.CharField(max_length=100)
    price=models.IntegerField(max_length=100)
    place=models.CharField(max_length=100)
    dist=models.CharField(max_length=100)
    
    class Meta:
        db_table="items"




class  showroom(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    model=models.IntegerField(max_length=100)
    price=models.IntegerField(max_length=100)
    email=models.CharField(max_length=300)
    
    class Meta:
        db_table="showrooms"

class bank(models.Model):
    account=models.IntegerField(max_length=100)
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    balance=models.IntegerField(max_length=255)
    
    class Meta:
        db_table="banks"



