from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Exam, ExamGroup,ExamStudent,ExamStudentResult, ExamGroupResult
from coursedata.models  import Groups, Student,StudentGroup
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request,'exams/home.html')

class HomeView(TemplateView):
    template_name='exams/home.html'

class ExamListView(ListView):
    model=Exam
    # queryset=Teacher.objects.all()
    queryset=Exam.objects.order_by('exam_name')
    context_object_list="exam_list"

class ExamCreateView(CreateView):
    model=Exam
    fields="__all__"
    success_url=reverse_lazy('exams:exam_list')

class ExamUpdateView(UpdateView):
    model=Exam
    fields=['exam_name']
    success_url=reverse_lazy('exams:exam_list')

class ExamDeleteView(DeleteView):
    model=Exam
    success_url=reverse_lazy('exams:exam_list')

def ExamGroupList(request):
    examgroup_obj=ExamGroup.objects.all()
    
    # print(studentparent_obj.student_id.id) 
    
    context={'examgroup_obj':examgroup_obj}
    return render(request,'exams/exam_group_list.html',context=context)

def ExamGroupAdd(request):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        group_kod=request.POST['group']
        group=Groups.objects.get(pk=group_kod)
        exam_group_date=request.POST['exam_group_date']
        
        # if 'student_parent_active' not in request.POST:
        #     student_parent_active_kod = False
        # else:
        #     if request.POST['student_parent_active']=="checked":
        #         student_parent_active_kod=True
        #     else:
        #         student_parent_active_kod=False

        # print(exam_group_date)
        ExamGroup.objects.create(exam_id=exam,group_id=group,exam_group_date=exam_group_date)
        return redirect(reverse('exams:exam_group_list'))
    else:
        exam_obj=Exam.objects.all() 
        group_obj=Groups.objects.all() 
        # context1={'student_obj':student_obj}
        # context2={'parent_obj':parent_obj}
        return render(request,'exams/exam_group_add.html',{"exam_obj":exam_obj,"group_obj":group_obj})

class ExamGroupDeleteView(DeleteView):
    model=ExamGroup
    success_url=reverse_lazy('exams:exam_group_list')

def ExamGroupUpdate(request, pk):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        group_kod=request.POST['group']
        group=Groups.objects.get(pk=group_kod)
        
        # if 'student_parent_active' not in request.POST:
        #     student_parent_active_kod = False
        # else:
        #     if request.POST['student_parent_active']=="checked":
        #         student_parent_active_kod=True
        #     else:
        #         student_parent_active_kod=False

        exam_group_date=request.POST['exam_group_date']
        exam_group_cur_obj=ExamGroup.objects.get(pk=pk)
       
        # student_parent_cur_obj.refresh_from_db()
        exam_group_cur_obj.exam_id=exam
        exam_group_cur_obj.group_id=group
        exam_group_cur_obj.exam_group_date=exam_group_date 
        exam_group_cur_obj.save()
        # StudentParent.objects.create(student_id=student,parent_id=parent,student_parent_active=student_parent_active_kod)
        return redirect(reverse('exams:exam_group_list'))
        # return HttpResponse("asa")
    else:
        exam_obj=Exam.objects.all() 
        group_obj=Groups.objects.all()
        exam_group_cur_obj=ExamGroup.objects.get(pk=pk)
        # print(exam_group_cur_obj.exam_group_date)
        # return HttpResponse('asd')
        
        return render(request,'exams/exam_group_update.html', {"exam_obj":exam_obj,"group_obj":group_obj,'exam_group_cur_obj':exam_group_cur_obj})


def ExamStudentList(request):
    examstudent_obj=ExamStudent.objects.all()
    
    # print(studentparent_obj.student_id.id) 
    
    context={'examstudent_obj':examstudent_obj}
    return render(request,'exams/exam_student_list.html',context=context)

def ExamStudentAdd(request):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        student_kod=request.POST['student']
        student=Student.objects.get(pk=student_kod)
        exam_student_date=request.POST['exam_student_date']
        
        # if 'student_parent_active' not in request.POST:
        #     student_parent_active_kod = False
        # else:
        #     if request.POST['student_parent_active']=="checked":
        #         student_parent_active_kod=True
        #     else:
        #         student_parent_active_kod=False

        # print(exam_group_date)
        ExamStudent.objects.create(exam_id=exam,student_id=student,exam_student_date=exam_student_date)
        return redirect(reverse('exams:exam_student_list'))
    else:
        exam_obj=Exam.objects.all() 
        student_obj=Student.objects.all() 
        # context1={'student_obj':student_obj}
        # context2={'parent_obj':parent_obj}
        return render(request,'exams/exam_student_add.html',{"exam_obj":exam_obj,"student_obj":student_obj})

class ExamStudentDeleteView(DeleteView):
    model=ExamStudent
    success_url=reverse_lazy('exams:exam_student_list')

def ExamStudentUpdate(request, pk):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        student_kod=request.POST['student']
        student=Student.objects.get(pk=student_kod)
        
        # if 'student_parent_active' not in request.POST:
        #     student_parent_active_kod = False
        # else:
        #     if request.POST['student_parent_active']=="checked":
        #         student_parent_active_kod=True
        #     else:
        #         student_parent_active_kod=False

        exam_student_date=request.POST['exam_student_date']
        exam_student_cur_obj=ExamStudent.objects.get(pk=pk)
       
        # student_parent_cur_obj.refresh_from_db()
        exam_student_cur_obj.exam_id=exam
        exam_student_cur_obj.student_id=student
        exam_student_cur_obj.exam_student_date=exam_student_date 
        exam_student_cur_obj.save()
        # StudentParent.objects.create(student_id=student,parent_id=parent,student_parent_active=student_parent_active_kod)
        return redirect(reverse('exams:exam_student_list'))
        # return HttpResponse("asa")
    else:
        exam_obj=Exam.objects.all() 
        student_obj=Student.objects.all()
        exam_student_cur_obj=ExamStudent.objects.get(pk=pk)
        # print(exam_group_cur_obj.exam_group_date)
        # return HttpResponse('asd')
        
        return render(request,'exams/exam_student_update.html', {"exam_obj":exam_obj,"student_obj":student_obj,'exam_student_cur_obj':exam_student_cur_obj})


def ExamStudentResultList(request):
    examstudentresult_obj=ExamStudentResult.objects.all()
    
    # print(studentparent_obj.student_id.id) 
    
    context={'examstudentresult_obj':examstudentresult_obj}
    return render(request,'exams/exam_student_result_list.html',context=context)


# def ExamStudentResultAdd(request):
#     if request.POST:
#         exam_kod=request.POST['exam']
#         exam=Exam.objects.get(pk=exam_kod)
#         student_kod=request.POST['student']
#         student=Student.objects.get(pk=student_kod)
#         group_kod=request.POST['group']
#         group=Groups.objects.get(pk=group_kod)
#         # exam_student_id=ExamStudent.objects.filter(exam_id=exam_kod,student_id=student_kod).values_list()
#         exam_student_id=ExamStudent.objects.filter(exam_id=exam_kod,student_id=student_kod).first()
#         student_group_id=StudentGroup.objects.filter(student_id=student_kod,group_id=group_kod).first()
        

#         exam_percent=request.POST['exam_percent']
#         exam_comment=request.POST['exam_student_result_comment']
        
        
#         # if 'student_parent_active' not in request.POST:
#         #     student_parent_active_kod = False
#         # else:
#         #     if request.POST['student_parent_active']=="checked":
#         #         student_parent_active_kod=True
#         #     else:
#         #         student_parent_active_kod=False

#         # print(exam_student_id.id)
#         ExamStudentResult.objects.create(exam_student_id=exam_student_id,student_group_id=student_group_id,exam_percent=exam_percent,exam_comment=exam_comment)
#         return redirect(reverse('exams:exam_student_result_list'))
#     else:
#         exam_obj=Exam.objects.all() 
#         group_obj=Groups.objects.all()
#         student_obj=Student.objects.all() 
#         # context1={'student_obj':student_obj}
#         # context2={'parent_obj':parent_obj}
#         return render(request,'exams/exam_student_result_add.html',{"exam_obj":exam_obj,"group_obj":group_obj,"student_obj":student_obj})

# class ExamStudentResultDeleteView(DeleteView):
#     model=ExamStudentResult
#     success_url=reverse_lazy('exams:exam_student_result_list')


# def ExamStudentResultUpdate(request, pk):
#     if request.POST:
#         exam_kod=request.POST['exam']
#         exam=Exam.objects.get(pk=exam_kod)
#         student_kod=request.POST['student']
#         student=Student.objects.get(pk=student_kod)
#         group_kod=request.POST['group']
#         group=Groups.objects.get(pk=group_kod)
#         # exam_student_id=ExamStudent.objects.filter(exam_id=exam_kod,student_id=student_kod).values_list()
#         exam_student_id=ExamStudent.objects.filter(exam_id=exam_kod,student_id=student_kod).first()
#         student_group_id=StudentGroup.objects.filter(student_id=student_kod,group_id=group_kod).first()
        

#         exam_percent=request.POST['exam_percent']
#         exam_comment=request.POST['exam_student_result_comment']
        
#         exam_student_result_cur_obj=ExamStudentResult.objects.get(pk=pk)
       
#         # student_parent_cur_obj.refresh_from_db()
#         exam_student_result_cur_obj.exam_student_id=exam_student_id
#         exam_student_result_cur_obj.student_group_id=student_group_id
#         exam_student_result_cur_obj.exam_percent=exam_percent
#         exam_student_result_cur_obj.exam_percentexam_comment=exam_comment
         
#         exam_student_result_cur_obj.save()
#         # StudentParent.objects.create(student_id=student,parent_id=parent,student_parent_active=student_parent_active_kod)
#         return redirect(reverse('exams:exam_student_result_list'))
#         # return HttpResponse("asa")
#     else:
#         exam_obj=Exam.objects.all()
#         group_obj=Groups.objects.all() 
#         student_obj=Student.objects.all()
#         exam_student_result_cur_obj=ExamStudentResult.objects.get(pk=pk)
#         # print(exam_group_cur_obj.exam_group_date)
#         # return HttpResponse('asd')
        
#         return render(request,'exams/exam_student_result_update.html', {"exam_obj":exam_obj,"group_obj":group_obj,"student_obj":student_obj,'exam_student_result_cur_obj':exam_student_result_cur_obj})


def ExamStudentResultInd(request, pk):
    ExamStudentResultInd_obj=ExamStudentResult.objects.filter(exam_student_id=pk).first()
    
    if not ExamStudentResultInd_obj:
        return redirect(reverse('exams:create_exam_student_result_ind',args=(pk,)))
        # return HttpResponse('ada')
    
    else:
        
        pk=ExamStudentResultInd_obj.id
        return redirect(reverse('exams:exam_student_result_ind_update',args=(pk,)))
    

def ExamStudentResultIndUpdate(request, pk):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        student_kod=request.POST['student']
        student=Student.objects.get(pk=student_kod)
        group_kod=request.POST['group']
        group=Groups.objects.get(pk=group_kod)
        exam_student_id=ExamStudent.objects.filter(exam_id=exam_kod,student_id=student_kod).first()
        student_group_id=StudentGroup.objects.filter(student_id=student_kod,group_id=group_kod).first()
        exam_percent=request.POST['exam_percent']
        exam_comment=request.POST['exam_student_result_comment']
        exam_student_result_cur_obj=ExamStudentResult.objects.get(pk=pk)
        exam_student_result_cur_obj.exam_student_id=exam_student_id
        exam_student_result_cur_obj.student_group_id=student_group_id
        exam_student_result_cur_obj.exam_percent=exam_percent
        exam_student_result_cur_obj.exam_percentexam_comment=exam_comment
         
        exam_student_result_cur_obj.save()
        return redirect(reverse('exams:exam_student_list'))
    else:
        exam_obj=Exam.objects.all()
        group_obj=Groups.objects.all() 
        student_obj=Student.objects.all()
        ExamStudentResultInd_obj=ExamStudentResult.objects.get(pk=pk)
        return render(request,'exams/exam_student_result_ind_update.html', {"exam_obj":exam_obj,"group_obj":group_obj,"student_obj":student_obj,'ExamStudentResultInd_obj':ExamStudentResultInd_obj})

def ExamStudentResultAddInd(request,pk):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        student_kod=request.POST['student']
        student=Student.objects.get(pk=student_kod)
        group_kod=request.POST['group']
        group=Groups.objects.get(pk=group_kod)
        exam_student_id=ExamStudent.objects.filter(exam_id=exam_kod,student_id=student_kod).first()
        student_group_id=StudentGroup.objects.filter(student_id=student_kod,group_id=group_kod).first()
        exam_percent=request.POST['exam_percent']
        exam_comment=request.POST['exam_student_result_comment']
        ExamStudentResult.objects.create(exam_student_id=exam_student_id,student_group_id=student_group_id,exam_percent=exam_percent,exam_comment=exam_comment)
        return redirect(reverse('exams:exam_student_result_list'))
        # return HttpResponse('asas')
    else:
        examstudent_cur_obj=ExamStudent.objects.get(pk=pk)
        print(examstudent_cur_obj.exam_id.id)
        print(examstudent_cur_obj.exam_id.exam_name)
        print(examstudent_cur_obj.student_id.id)
        print(examstudent_cur_obj.student_id.student_fio)
        studentgroup_cur_obj=StudentGroup.objects.filter(student_id=examstudent_cur_obj.student_id.id).first()
        print(studentgroup_cur_obj.group_id.id)
        print(studentgroup_cur_obj.group_id.group_name)

        exam_obj=Exam.objects.all() 
        group_obj=Groups.objects.all()
        student_obj=Student.objects.all()
        
        return render(request,'exams/exam_student_result_ind_add.html',{"exam_obj":exam_obj,"group_obj":group_obj,"student_obj":student_obj})
        
def ExamGroupResultList(request):
    examgroupresult_obj=ExamGroupResult.objects.all()
    
    # print(studentparent_obj.student_id.id) 
    
    context={'examgroupresult_obj':examgroupresult_obj}
    return render(request,'exams/exam_group_result_list.html',context=context)
