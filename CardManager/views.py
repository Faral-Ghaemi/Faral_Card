from django.views import View
from django.http import JsonResponse
from .models import TimeCard
from django.utils import timezone
from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'index.html')

class StartWorkView(View):
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id')
        project_id = request.POST.get('project_id')

        # ایجاد یا به‌روزرسانی TimeCard
        time_card, created = TimeCard.objects.get_or_create(
            user_id=user_id,
            project_id=project_id,
            defaults={'start_time': timezone.now()}
        )

        if not created:
            # اگر TimeCard قبلاً ایجاد شده بود، تنها زمان شروع را به‌روزرسانی کن
            time_card.start_time = timezone.now()
            time_card.save()

        return JsonResponse({'status': 'success', 'message': 'Work started'})

class EndWorkView(View):
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id')
        project_id = request.POST.get('project_id')
        report = request.POST.get('report')

        time_card = TimeCard.objects.get(
            user_id=user_id,
            project_id=project_id,
            end_time__isnull=True  # فیلتر کردن بر اساس TimeCard‌هایی که هنوز پایان نیافته‌اند
        )

        time_card.end_time = timezone.now()
        time_card.report = report
        time_card.save()

        return JsonResponse({'status': 'success', 'message': 'Work ended and report saved'})
