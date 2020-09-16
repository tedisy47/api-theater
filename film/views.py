from rest_framework import generics

from .models import Geenre, Film, Teather, Schedule
from .serializers import GeenreSerializer, FilmSerializer, TeatherSerializer, ScheduleSerializer


class GeenreList(generics.ListCreateAPIView):
    queryset = Geenre.objects.all()
    serializer_class = GeenreSerializer


class GeenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Geenre.objects.all()
    serializer_class = GeenreSerializer

class TeatherList(generics.ListCreateAPIView):
    queryset = Teather.objects.all()
    serializer_class = TeatherSerializer

class TeatherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teather.objects.all()
    serializer_class = TeatherSerializer

class FilmList(generics.ListCreateAPIView):
	serializer_class = FilmSerializer
	def get_queryset(self):
		queryset = Film.objects.all()
		status = self.request.query_params.get('status', None)
		geenre = self.request.query_params.get('geenre', None)
		if status is not None:
			queryset = queryset.filter(status=status)
		if geenre is not None:
			queryset = queryset.filter(geenre_id=geenre)
		return queryset
	# print(queryset)

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ScheduleList(generics.ListCreateAPIView):
	serializer_class = ScheduleSerializer
	def get_queryset(self):
		queryset = Schedule.objects.all()
		film = self.request.query_params.get('film', None)
		if film is not None:
			queryset = queryset.filter(film=film)
		return queryset
	# print(queryset)


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer