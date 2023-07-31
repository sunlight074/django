from django.db import models
from django.contrib.auth.models import User

class jobAlert(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    search_name = models.CharField(max_length=200, null=True)
    result_link = models.CharField(max_length=200, null=True)
    results = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class jobAlertDetail(models.Model):
    id = models.AutoField(primary_key=True)
    alert_detail_assign = models.ForeignKey(jobAlert, on_delete=models.CASCADE, related_name='alert_detail_assign')
    status_choices = (
            ('Escalation','Escalation'), 
            ('In progress','In progress'), 
            ('Close','Close'))
    severity_choices = (
                ('Low','Low'), 
                ('Medium','Medium'), 
                ('High','High'), 
                ('Critical','Critical'))
    severity = models.CharField(max_length=200, choices=severity_choices)
    status = models.CharField(max_length=200, choices=status_choices)
    assign = models.ForeignKey(User, null=True, on_delete=models.CASCADE , related_name='assign')
    report = models.ForeignKey(User, null=True, on_delete=models.CASCADE , related_name='report')
    app = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    job_detail_id = models.ForeignKey('jobAlertDetail', on_delete=models.CASCADE, related_name='job_detail_id')
    comment_person = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='comment_person')
    comment_text = models.CharField(max_length=200, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment_id)


# python manage.py makemigrations
# python manage.py migrate