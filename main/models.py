from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=300)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_data = models.DateField()


class Teacher(models.Model):
    name = models.CharField(max_length=70)
    empnum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()



# class Comment(models.Model):
#     answer= models.ForeignKey(Answer, on_delete=models.CASCADE)
#     user= models.ForeignKey(User, on_delete=models.CASCADE,related_name='comment_user')
#     add_time=models.DateTimeField(auto_now_add=True)


# class UpVote(models.Model):
#     answer= models.ForeignKey(Answer, on_delete=models.CASCADE)
#     user= models.ForeignKey(User, on_delete=models.CASCADE,related_name='Upvote_user')
  

# class DownVote(models.Model):
#     answer= models.ForeignKey(Answer, on_delete=models.CASCADE)
#     user= models.ForeignKey(User, on_delete=models.CASCADE,related_name='DownVote_user')
    