from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'textUtils_app/index.html')

def analyze(request):
    text_var = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    new_line = request.POST.get('new_line', 'off')
    remove_extra_space = request.POST.get('remove_extra_space', 'off')
    count_char = request.POST.get('count_char', 'off')

    if removepunc == "on" and fullcaps == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[]\^_`{|}~'''

        analyzed = ""
        for char in text_var:
            if char not in punctuations:
                analyzed += char

        analyzed = analyzed.upper()

        my_dict = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'textUtils_app/analyze.html', context=my_dict)

    elif removepunc == "on" and fullcaps == "on" and new_line == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[]\^_`{|}~'''

        analyzed = ""
        for char in text_var:
            if char not in punctuations:
                analyzed += char

        analyzed = analyzed.upper()

        my_dict = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'textUtils_app/analyze.html', context=my_dict)

    elif removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[]\^_`{|}~'''

        analyzed = ""
        for char in text_var:
            if char not in punctuations:
                analyzed += char

        my_dict = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'textUtils_app/analyze.html', context=my_dict)

    elif fullcaps == "on":
        analyzed = text_var.upper()

        my_dict = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'textUtils_app/analyze.html', context=my_dict)

    elif new_line == "on":
        analyzed = ''
        for char in text_var:
            if char != '\n' and char != '\r':
                analyzed += char

        my_dict = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'textUtils_app/analyze.html', context=my_dict)

    elif remove_extra_space == "on":
        analyzed = ''
        for index, char in enumerate(text_var):
            if text_var[index] == ' ' and text_var[index+1] == ' ':
                pass
            else:
                analyzed += char

        my_dict = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        return render(request, 'textUtils_app/analyze.html', context=my_dict)

    elif count_char == "on":
        analyzed = 0
        for char in text_var:
            if char != " ":
                analyzed += 1

        analyzed = "No. of characters in a string: " + str(analyzed)

        my_dict = {'purpose': 'Counting Charaters', 'analyzed_text': analyzed}
        return render(request, 'textUtils_app/analyze.html', context=my_dict)

    else:
        return HttpResponse("Error")
