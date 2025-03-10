from django.forms import ModelForm
from .models import Room, Profile
from django.contrib.auth.models import User
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Tell something about yourself...',
            'rows': 4
        }), 
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance')
        super(UserForm, self).__init__(*args, **kwargs)
        if user:
            try:
                self.fields['avatar'].initial = user.profile.avatar
                self.fields['bio'].initial = user.profile.bio
            except Profile.DoesNotExist:
                pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']