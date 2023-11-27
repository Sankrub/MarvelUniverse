# profile.py
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from MarvelUniverse.models import UserData


class ProfileView(View):
    template_name = 'MarvelUniverse/profile.html'

    def get(self, request):
        this_user = request.user
        user_data, created = UserData.objects.get_or_create(user=this_user)

        formatted_date_joined = naturaltime(this_user.date_joined)

        context = {
            'username': this_user.username,
            'email': this_user.email,  # Added email to the context
            'profile_img_url': user_data.profile_img_url,
            'medal_img': user_data.medal_img,
            'scores': user_data.scores,
            'date_joined': formatted_date_joined,
        }

        return render(request, self.template_name, context=context)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateProfileImageView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        avatar_url = data.get('avatarUrl', '')

        user_data = UserData.objects.get(user=request.user)
        user_data.profile_img_url = avatar_url
        user_data.save()

        return JsonResponse({'success': True})
