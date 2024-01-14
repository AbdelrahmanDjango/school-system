# from . forms import Class_room_form


# def classroom_list(request):
#     classrooms = Class_room.objects.all()
#     return render(request, 'classroom_list.html', {'classrooms':classrooms})

# def add_classroom(request):
#     if request.method == 'POST':
#         form = Class_room_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('school:classroom_list')
#     else:
#         form = Class_room_form()
#     return render(request, 'add_classroom.html', {'form':form})