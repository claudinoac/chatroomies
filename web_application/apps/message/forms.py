from django import forms


class MessageForm(forms.Form):
    content = forms.CharField(max_length=300)
    user_id = forms.IntegerField()
    chatroom_id = forms.IntegerField()
