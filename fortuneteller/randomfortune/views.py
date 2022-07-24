from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here:
def homepage(request):
    return HttpResponse('Hello! Click <a href = "./fortune">here</a> to discover your future or <a href="./quote">here</a> to Discover a Stoic quote!')

def fortune(request):
    context = {"fortune_placeholder": random_fortune()}
    return render(request, 'fortune.html', context)

def quote(request):
    context = {"quote_placeholder": random_quote(stoic_quotes)}
    return render(request, 'quote.html', context)

def random_fortune():
    random_num = random.randint(0, 3)
    if random_num == 3:
        return 'You will become a millionaire selling Spanish cherries.'
    elif random_num == 2:
        return 'You will win a marathon for seniors at age 92.'
    elif random_num == 1:
        return 'You will visit the Amazon rainforset.'
    else:
        return 'You will adopt a bulldog'


stoic_quotes = [
"The best answer to anger is silence. - Marcus Aurelius",
"The more we value things outside our control, the less control we have. - Marcus Aurelius",
"Confine yourself to the present. - Marcus Aurelius",
"When you arise in the morning, think of what a precious privilege it is to be alive – to breathe, to think, to enjoy, to love. - Marcus Aurelius",
"Give yourself a gift, the present moment. - Marcus Aurelius",
"We suffer more often in imagination than in reality. - Seneca",
"Ignorance is the cause of fear. - Seneca",
"While we wait for life, life passes. - Seneca",
"He who is brave is free. - Seneca",
"It does not matter how many books you have, but how good are the books which you have. - Seneca",
"The greatest remedy for anger is delay. - Seneca"
]

def random_quote(quotes):
    return quotes[random.randint(0, len(quotes)-1)]
