import functions_framework

@functions_framework.http
def hello_linkedin(request):
    """ 
    Simple HTTP Cloud Function 
    for this tutorial !
    """
    return "This is working!"

