from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=
                            forms.TextInput(
                                attrs= {
                                    "class":"form-control",
                                    "placeholder":"write your title"
                                }
                            )
                        )

    class Meta:
        model= Post
        fields= [
            'title',
            'content',
        ]



