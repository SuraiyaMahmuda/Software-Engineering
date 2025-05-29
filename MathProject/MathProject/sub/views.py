from django.shortcuts import render
from .models import Subtraction

def subtract_numbers(request):
    """
    View to subtract two numbers provided by the user via POST request.

    Retrieves `num_first` and `num_second` from POST data, creates a
    `Subtraction` instance with these numbers, and calculates the result.

    Args:
        request (HttpRequest): The request object containing HTTP metadata.

    Returns:
        HttpResponse: The rendered template with the subtraction result.

    Template:
        result.html

    Context:
        result (float or None): The result of the subtraction if POST data is provided, otherwise None.
    """
    result = None
    if request.method == 'POST':
        num_first = request.POST.get('num_first')
        num_second = request.POST.get('num_second')
        num_first = int(num_first)
        num_second = int(num_second)
        subtraction = Subtraction(num_first=num_first, num_second=num_second)
        result = subtraction.result()
    
    return render(request, 'result.html', {'result': result})
