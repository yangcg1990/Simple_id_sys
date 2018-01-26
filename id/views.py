from django.shortcuts import render

from .forms import IdForm
from .function import *

# Create your views here.
def index(request):
    '''首页'''
    if request.method != 'POST':
        form = IdForm()
        id_check = 'message'
    else:
        form = IdForm(data=request.POST)
        if form.is_valid():
            form.save()
            #获取身份证信息
            id_numbers = request.POST['id_numbers']
            #检查输入是否有误
            if check_id_numbers_wrong(id_numbers) \
                    or check_test_code_wrong(id_numbers):
                id_check = 'wrong'
            else:
                #获取身份证信息
                #地址
                id_adress = get_id_adress(id_numbers)
                #出生日期
                id_age = get_id_age(id_numbers)
                #性别
                id_sex = get_id_sex(id_numbers)

                id_check = {'adress':id_adress, 'age':id_age, 'sex':id_sex}
        else:
            id_check = 'wrong'

    context = {'form':form, 'id_check':id_check}
    return render(request, 'id/index.html', context)