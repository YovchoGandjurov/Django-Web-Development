from django.shortcuts import render
from django.http import HttpResponse
import re


def index(request):
    return HttpResponse('</br></br></br><h1>Hello Django!</h1>')


def num_recognition(arg):
    result = None
    re_pattern = r"^\d+?\.\d+?$"

    if re.match(re_pattern, arg):
        result = float(arg)
    elif arg.isdigit():
        result = int(arg)
    return result


def calculate(request, operator, arg1, arg2):
    result = None
    if num_recognition(arg1) is not None and \
            num_recognition(arg2) is not None:

        if operator == 'add':
            result = num_recognition(arg1) + num_recognition(arg2)
            return HttpResponse(f'<h1>{result}</h1>')
        elif operator == 'subtract':
            result = num_recognition(arg1) - num_recognition(arg2)
            return HttpResponse(f'<h1>{result}</h1>')
        elif operator == 'multiply':
            result = num_recognition(arg1) * num_recognition(arg2)
            return HttpResponse(f'<h1>{result}</h1>')
        elif operator == 'divide':
            if num_recognition(arg1) == 0 or num_recognition(arg2) == 0:
                return HttpResponse(
                        '<h1>ERROR: You can not use 0 for a devision</h1>')
            result = num_recognition(arg1) / num_recognition(arg2)
            return HttpResponse(f'<h1>{result}</h1>')

    else:
        return HttpResponse(
            '<h1>ERROR: Ops! Something went wrong!</h1></br> \
             <h2>The correct format - /operator/number/number/</h2> \
             <h2>The correct operators - \
             add or subtract or multiply or divide</h2>')
