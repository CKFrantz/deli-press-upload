import buttoncode

def request_page(request):
  if(request.GET.get('mybtn')):
    #buttoncode.subfun( int(request.GET.get('fname')) )
    fname = buttoncode.subfun(request.GET.get('fname') )
	#fname = request.GET.get('fname')
	print('testing')
	print(fname)
return render(request,'templates/home.html')

