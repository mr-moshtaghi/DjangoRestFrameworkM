from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def one(request):
	if request.method == 'POST':
		name = request.data['name']
		return Response({'name': f'my name is {name}'})
	else:
		return Response({'name':'my name is amir'})