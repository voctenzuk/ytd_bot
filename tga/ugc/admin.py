from django.contrib import admin

from .forms import ProfileForm
from .models import Message
from .models import Profile
from .models import Video
from .models import AppConfig


@admin.register(AppConfig)
class AppConfigAdmin(admin.ModelAdmin):
    # list_display = ('session_name', 'api_id', 'api_hash', 'is_active', 'is_bot',
    #                 'bot_token', 'posting_channel', 'temp_chat', 'timestamp')
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "external_id", "name")
    form = ProfileForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "profile", "text", "created_at")
    # pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "yt_id",
        "show_url",
        "title",
        "uploader",
        "view_count",
        "rating",
        "status",
    )
