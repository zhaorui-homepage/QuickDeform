from django.http import JsonResponse
from django.shortcuts import render

from okada.models import parameters
from spider import ajax


def earthquakeV(request):
	# db = dataIN.connectdb()
	latestRecord = parameters.objects.order_by('-id')[0]
	record1 = parameters.objects.order_by('-id')[1]
	record2 = parameters.objects.order_by('-id')[2]
	record3 = parameters.objects.order_by('-id')[3]
	record4 = parameters.objects.order_by('-id')[4]
	record5 = parameters.objects.order_by('-id')[5]
	date1 = record1.Edatetime.split()
	date1 = date1[0]
	date2 = record2.Edatetime.split()
	date2 = date2[0]
	date3 = record3.Edatetime.split()
	date3 = date3[0]
	date4 = record4.Edatetime.split()
	date4 = date4[0]
	date5 = record5.Edatetime.split()
	date5 = date5[0]

	content = {'Etitle': latestRecord.Etitle, 'Edatetime': latestRecord.Edatetime,
			   'Lat': latestRecord.Latitude, 'Lon': latestRecord.Longitude,
			   'Mag': latestRecord.Magnitude, 'Depth': latestRecord.Depth,
			   'Strike': latestRecord.Strike1, 'Dip': latestRecord.Dip1, 'Rake': latestRecord.Rake1,
			   'Strike2': latestRecord.Strike2, 'Dip2': latestRecord.Dip2, 'Rake2': latestRecord.Rake2,
			   'title1': record1.Etitle, 'date1': date1,
			   'title2': record2.Etitle, 'date2': date2,
			   'title3': record3.Etitle, 'date3': date3,
			   'title4': record4.Etitle, 'date4': date4,
			   'title5': record5.Etitle, 'date5': date5}
	# dataIN.closedb(db)
	return render(request, 'index.html', content)


def custom(request):
	lat = float(request.GET['lat'])
	lng = float(request.GET['lng'])
	Mw = float(request.GET['Mw'])
	depth = float(request.GET['depth'])
	strike = float(request.GET['strike'])
	dip = float(request.GET['dip'])
	rake = float(request.GET['rake'])
	layer = request.GET['layer']

	result = ajax.quickquake(lat, lng, Mw, depth, [strike, dip, rake], layer)

	return JsonResponse(result, safe=False)

def history(request):
	key = request.GET['key']
	layer = request.GET['layer']
	record = parameters.objects.order_by("-id")[int(key)]
	lat = record.Latitude
	lng = record.Longitude
	Mw = record.Magnitude
	depth = record.Depth
	strike = record.Strike1
	dip = record.Dip1
	rake = record.Rake1

	map = ajax.quickquake(lat, lng, Mw, depth, [strike, dip, rake], layer)

	result = {'map': map, 'lat': lat,'lng': lng,
			  'Mw': Mw, 'depth': depth,
			  'strike': strike, 'dip': dip, 'rake': rake}

	return JsonResponse(result, safe=False)




# def ajax_dict(request):
# 	lat = float(request.GET['lat'])
# 	lng = float(request.GET['lng'])
# 	name_dict = {'twz': 'Love python and Django', 'age': lat + lng}
# 	return JsonResponse(name_dict)
