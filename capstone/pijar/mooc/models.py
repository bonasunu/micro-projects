from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

class Cards(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="card_category")
    card_question = models.CharField(max_length=100000)
    card_answer = models.CharField(max_length=100000)


"""
TODO
Pijar - minimalistic flashcards to help your learning process
no distractions

Create user model
- Full name
- username
- email
- password

Create cards model
- category
- add or delete category
- add or remove cards inside category
- viewing all categories
- viewing all cards inside category

Create learn model
- select category
- start/stop learning
- random cards
- load card

UX on learn page
- select category using dropdown
- load card  to start learning (show a card)
- stop to stop learning (clear view and show meaage info)
- message info (how to start/stop learning)

additional feature
- save last open cards, category, or close card


"""