from django.http import HttpResponse
from django.shortcuts import render
import pathlib

this_file_path = pathlib.Path(__file__).resolve().parent # get the path of this file
print(this_file_path) 

def home_page_view(request):
    title = "This Page And is the Home Page"
    my_Content = {
        "myPage": title,
    }

    html_template = "demo.html"
    return render(request, html_template, my_Content) 

def old_home_page_view(request):
    # html_file = this_file_path / "demo.html"
    # html_ = html_file.read_text()
    title = "This Page And is the Home Page"

    my_Content = {
        "myPage": title,
    }

    html_ = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Escapade SaaS</title>
        </head>
        <body>
            <h1>Escapade SaaS</h1>
            <h3>Welcome to {myPage}</h3>
        </body>
        </html>
    """.format(**my_Content)

    return HttpResponse(html_)