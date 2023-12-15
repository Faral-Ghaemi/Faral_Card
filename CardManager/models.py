from django.db import models
import jdatetime
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

# Create models of Team.
#مشخصات تیم
class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField()




#مشخصات اضا
class Members(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.TextField()
    email = models.CharField(max_length=100)
    date_joined = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

#مشخصات پوروژه
class Projects(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

#گزارش کاربرا و زمان ورود و خوروج
class TimeCard(models.Model):
    user = models.ForeignKey(Members, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    report = models.TextField(null=True, blank=True)  # گزارش روزانه

    def start_work(self):
        self.start_time = timezone.now()
        self.save()

    def end_work(self, report):
        self.end_time = timezone.now()
        self.report = report
        self.save()

    @property
    def work_duration(self):
        if self.start_time and self.end_time:
            duration = self.end_time - self.start_time
            hours, remainder = divmod(duration.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours} ساعت, {minutes} دقیقه, {seconds} ثانیه"
        return None

    @property
    def start_time_jalali(self):
        if self.start_time:
            return jdatetime.datetime.fromgregorian(datetime=self.start_time)
        return None

    @property
    def end_time_jalali(self):
        if self.end_time:
            return jdatetime.datetime.fromgregorian(datetime=self.end_time)
        return None

    def __str__(self):
        return f"{self.user.full_name} - Activity"