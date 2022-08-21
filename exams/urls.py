from django.urls import path
from .views import (HomeView, ExamListView, ExamCreateView, ExamUpdateView, ExamDeleteView,
                    ExamGroupList ,ExamGroupAdd,ExamGroupDeleteView,ExamGroupUpdate,
                    ExamStudentList ,ExamStudentAdd,ExamStudentDeleteView,ExamStudentUpdate,
                    ExamStudentResultList,ExamStudentResultInd,
                    # ExamStudentResultAddInd,
                    ExamStudentResultIndUpdate,ExamStudentResultAddInd,
                    # ExamStudentResultList, ExamStudentResultAdd,ExamStudentResultDeleteView,ExamStudentResultUpdate,
                    ExamGroupResultList)

app_name='exams'

urlpatterns = [
    path('', HomeView.as_view(), name='home_exams'),
    path('exam_list/', ExamListView.as_view(), name='exam_list'),
    path('create_exam/',ExamCreateView.as_view(),name='create_exam'),
    path('exam_update/<int:pk>',ExamUpdateView.as_view(),name='exam_update'),
    path('exam_delete/<int:pk>',ExamDeleteView.as_view(),name='exam_delete'),
    path('exam_group_list/', ExamGroupList, name='exam_group_list'),
    path('creare_exam_group/', ExamGroupAdd, name='create_exam_group'),
    path('exam_group_delete/<int:pk>',ExamGroupDeleteView.as_view(),name='exam_group_delete'),
    path('exam_group_update/<int:pk>',ExamGroupUpdate,name='exam_group_update'),
    path('exam_student_list/', ExamStudentList, name='exam_student_list'),
    path('creare_exam_student/', ExamStudentAdd, name='create_exam_student'),
    path('exam_student_delete/<int:pk>',ExamStudentDeleteView.as_view(),name='exam_student_delete'),
    path('exam_student_update/<int:pk>',ExamStudentUpdate,name='exam_student_update'),
    # path('exam_student_result_list/', ExamStudentResultList, name='exam_student_result_list'),
    path('exam_student_result_list_ind/<int:pk>', ExamStudentResultInd, name='exam_student_result_list_ind'),
    # path('creare_exam_student_result/', ExamStudentResultAdd, name='create_exam_student_result'),
    path('creare_exam_student_result_ind/<int:pk>', ExamStudentResultAddInd, name='create_exam_student_result_ind'),
    path('exam_student_result_ind_update/<int:pk>',ExamStudentResultIndUpdate,name='exam_student_result_ind_update'),
    # path('exam_student_result_delete/<int:pk>',ExamStudentResultDeleteView.as_view(),name='exam_student_result_delete'),
    # path('exam_student_result_update/<int:pk>',ExamStudentResultUpdate,name='exam_student_result_update'),
    path('exam_group_result_list/', ExamGroupResultList, name='exam_group_result_list'),
    # path('creare_exam_group_result/', ExamStudentResultAdd, name='create_exam_group_result'),
    

]