from django.test import TestCase
from apps.message.forms import MessageForm


class TestMessageForm(TestCase):

    def setUp(self):
        pass

    def test_send_command(self):
        form = MessageForm({
            "user_id": 1,
            "chatroom_id": 1,
            "content": "/stock=appl.us"
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["content"], "/stock=appl.us")

    def test_send_invalid_command(self):
        form = MessageForm({
            "user_id": 1,
            "chatroom_id": 1,
            "content": "/stock==appl.us"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            "content": ['Invalid command. The command must be in the format "/command=argument"']
        })
