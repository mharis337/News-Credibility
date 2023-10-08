from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import tensorflow as tf


def index(request):
    form = forms.ArticleForm()

    if request.method == 'POST':
        form = forms.ArticleForm(request.POST)

        if form.is_valid():
            new_model = tf.keras.models.load_model('Fake_News_Detector/model/Fake_News.tf')
            
            input_data = form.cleaned_data['content']
            i = new_model.predict([input_data])
            if(tf.squeeze(tf.round(i)).numpy().tolist() == 0):
                a = "This article is likely fake news. There is a {:.2f} % probability it is real news.".format(i[0][0]*100)
            else:
                a = "This article is likely real. There is a {:.2f} % probability it is real news.".format(i[0][0]*100)
            
            context = {
                'prediction_result': a,
            }
            return render(request, 'Fake_News_Detector/result_template.html', context)

    return render(request, 'Fake_News_Detector/index.html', {'form':form})