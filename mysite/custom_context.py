from blog.views import Post, Category

def mycontext(request):
    cat = Category.objects.all()
    brand_name = "PYTHONISTA"
    context = {'cat': cat, 'brand_name': brand_name,}
    return context
