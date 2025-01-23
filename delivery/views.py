from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Customer,Restaurant,MenuItem


# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'signin.html')
def signup(request):
    return render(request,'signup.html')

def handle_login(request):

    if request.method=='POST':
        username=  request.POST.get('username')
        password = request.POST.get('password')
        try:
            cust = Customer.objects.get(username=username, password=password)
            return render(request, 'success.html')
        except:
            return render(request, 'fail.html')
    else:
        return HttpResponse("Invalid request")
def handle_signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')

        try:
            cust = Customer.objects.get(username=username)
        except:
            # username does not exist
            c = Customer(username=username, password=password, email=email, mobile=mobile, address=address)
            c.save()

        return render(request, 'signin.html')

    else:
        return HttpResponse("Invalid request")

def restaurant_page(request):
    return render(request,'add_restaurant.html')


def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        rest = Restaurant(name=name, picture=picture, cuisine=cuisine, rating=rating)
        rest.save()

        restaurants = Restaurant.objects.all()

        return render(request, 'show_restaurants.html', {"restaurants": restaurants})

    else:
        return HttpResponse("Invalid request")

def show_restaurant_page(request):
    restaurants = Restaurant.objects.all()
    return render(request,'show_restaurants.html', {"restaurants":restaurants})

def restaurant_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        # Handle adding new menu item
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        is_veg = request.POST.get('is_veg') == 'on'
        picture = request.POST.get('picture')

        MenuItem.objects.create(
            restaurant=restaurant,
            name=name,
            description=description,
            price=price,
            is_veg=is_veg,
            picture=picture
        )

        return redirect('restaurant_menu', restaurant_id=restaurant.id)

    # Fetch all menu items for this restaurant
    menu_items = restaurant.menu_items.all()

    return render(request, 'menu.html', {
        'restaurant': restaurant,
        'menu_items': menu_items,
    })