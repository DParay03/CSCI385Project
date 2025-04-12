from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Corey',
        'title': 'Blog Post 1',
        'content': 'Sfshdfldksjahnfkljaswdh;flkahswjkhflsjaikhfljikdsahljikfhdsaljikhflikjdswhljikfashjkdsafhijkaw'
    },
    {
        'author': 'Corey',
        'title': 'Blog Post 1',
        'content': 'Sfshdfldksjahnfkljaswdh;flkahswjkhflsjaikhfljikdsahljikfhdsaljikhflikjdswhljikfashjkdsafhijkaw'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'communityPost.html', context)
