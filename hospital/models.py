from django.http import JsonResponse
from django.db import models

# the following lines added:
import datetime
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    # 1 : user , 2 : doctor , 3 : pharmacy
    user_type = models.IntegerField()


class Prescription(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(User, related_name='doctor', on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=2000)
    date = models.DateTimeField()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=15) <= self.date <= now


def auth(username, password):
    users = User.objects.filter(username=username, password=password)
    if len(users) > 0:
        return users[0].user_type
    else:
        return -1


def add_prescription(username, password, user, text):
    users = User.objects.filter(username=username, password=password)
    if len(users) > 0:
        if users[0].user_type == 2:
            patient = User.objects.filter(username=user)
            prescription = Prescription(user=patient[0], doctor=users[0], text=text, date=timezone.now())
            prescription.save()
            return 1
    return -1


def get_prescription(username, password, user):
    users = User.objects.filter(username=username, password=password)
    if len(users) > 0:
        if users[0].user_type == 1 or user == -1:
            prescriptions = Prescription.objects.filter(user=users[0])
            ps = []
            for p in prescriptions:
                ps.append(p.text)
            return JsonResponse({'status': 1, 'prescriptions': ps})
        elif users[0].user_type == 3:
            db_user = User.objects.filter(username=user)
            if len(db_user) > 0:
                prescriptions = Prescription.objects.filter(user=db_user[0])
                ps = []
                for p in prescriptions:
                    ps.append(p.text)
                return JsonResponse({'status': 1, 'prescriptions': ps})
    return JsonResponse({'status': -1})
