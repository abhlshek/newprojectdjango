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
        db_table="admission"
        
        



class PhoneBook(models.Model):
    name=models.CharField(max_length=100)
    
    
    
    
    class Meta:
        db_table="phonebook"


