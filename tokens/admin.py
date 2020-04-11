from django.contrib import admin

from .models import Election, Voter, Token

admin.site.register(Election)
admin.site.register(Voter)
admin.site.register(Token)