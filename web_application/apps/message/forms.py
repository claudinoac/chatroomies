from django import forms
from django.core.exceptions import ValidationError


class MessageForm(forms.Form):
    content = forms.CharField(max_length=300)
    user_id = forms.IntegerField()
    chatroom_id = forms.IntegerField()

    def clean_content(self):
        content = self.cleaned_data.get("content")

        if content.startswith("/"):
            cleaned_message = content.split("/")[-1]
            try:
                bot_command, bot_argument = cleaned_message.split("=")
            except ValueError:
                raise ValidationError("Invalid command. The command must be in the format \"/command=argument\"")
        return content

