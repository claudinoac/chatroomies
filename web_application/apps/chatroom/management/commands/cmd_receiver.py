from django.core.management.base import BaseCommand, CommandError
from apps.chatroom.workers import start_worker

class Command(BaseCommand):
    help = 'Run command result consumer from bot'

    def handle(self, *args, **kwargs):
        start_worker()

    def add_arguments(self, parser):
        pass


