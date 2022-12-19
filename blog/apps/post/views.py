from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def quienes_somos(request):
	return render(request, "quienes-somos.html", {})

def proyectos(request):
	return render(request, "proyectos.html", {})

def servicios(request):
	return render(request, "servicios.html", {})

def publicaciones(request):
	return render(request, "publicaciones.html", {})

def areas_de_estudio(request):
	return render(request, "areas-de-estudio.html", {})

def crear_post(request):
	return render(request, "crear-post.html", {})
