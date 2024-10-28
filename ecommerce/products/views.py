from django.http import JsonResponse


def all_products(request):
    products = [
        {
            "name": "Camiseta",
            "qty": 10,
            "price": 100,
        },
        {
            "name": "Pantalón",
            "qty": 3,
            "price": 200,
        },
        {
            "name": "Zapatillas",
            "qty": 30,
            "price": 500,
        },
    ]
    return JsonResponse(products, safe=False)