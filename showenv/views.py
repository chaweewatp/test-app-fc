from django.shortcuts import render
import os 
# Create your views here.
def showall(request):
    context={'secret_key':os.environ.get('SECRET_KEY'),'database_url':os.environ.get('DATABASE_URL')}
    return render(request, 'showenv/showall.html', context)


    