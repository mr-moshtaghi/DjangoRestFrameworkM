from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer
from .models import Person


@api_view(['GET', 'POST'])
def one(request):
	if request.method == 'POST':
		name = request.data['name']
		return Response({'name': f'my name is {name}'})
	else:
		return Response({'name':'my name is amir'})

@api_view()
def persons(request):
	persons = Person.objects.all()
	ser_data = PersonSerializer(persons, many=True)
	return Response(ser_data.data)