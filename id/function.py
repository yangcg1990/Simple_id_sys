import datetime, time

from .models import Provinces, Cities, Areas

#身份证前17位的有效输入
max_nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#身份证第18位的有效输入
max_ten = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
#身份证计算第十八位所需的权值
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
#身份证最后一位对应的检验码
test_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

def check_id_numbers_wrong(id_numbers):
    '''检查输入的身份证号是否有误'''
    if len(id_numbers) != 18:
        print('不足18位！')
        return True
    if id_numbers[17] not in max_ten:
        print('请输入数字！')
        return True
    for num in id_numbers[:16]:
        if int(num) not in max_nine:
            print('请输入数字！')
            return True
    return False

def check_test_code_wrong(id_numbers):
    '''检查身份证最后一位验证码'''

    #计算的检验码
    calculation_test_code = 0
    for num in range(0, 17):
        calculation_test_code += int(id_numbers[num]) * weight[num]
    calculation_test_code = calculation_test_code % 11
    if id_numbers[17] != test_code[calculation_test_code]:
        print('校验码错误!')
        return True
    else:
        return False

def get_id_adress(id_numbers):
    '''获取身份证地址信息'''

    #身份证前6位
    id_numbers_six = id_numbers[:6]
    area_all = Areas.objects.all().values('areaid')
    area_list = []
    for are in area_all:
        area_list.append(are['areaid'])

    #判断身份证地址
    if id_numbers_six in area_list:
        area = Areas.objects.get(areaid=id_numbers_six)
        city = Cities.objects.get(cityid=area.cityid)
        province = Provinces.objects.get(provinceid=city.provinceid)
    else:
        area = ''
        city = Cities.objects.get(cityid=id_numbers_six)
        province = Provinces.objects.get(provinceid=city.provinceid)

    #身份证上的地址信息
    id_adress = [province, city, area]
    return id_adress

def get_id_age(id_numbers):
    '''获取身份证年龄信息'''

    #获取身份证第7至14位
    id_age_message = id_numbers[6:14]
    #年
    id_year = id_age_message[:4]
    #月
    id_month = id_age_message[4:6]
    #日
    id_day = id_age_message[6:]

    #计算年龄
    current_date = datetime.date.today()
    current_year = current_date.year
    id_age = current_year - int(id_year)

    #身份证上的年龄信息
    id_message = [id_year, id_month, id_day, id_age]
    return id_message

def get_id_sex(id_numbers):
    '''获取性别'''
    #身份证第17位
    id_sex = id_numbers[16]
    if (int(id_sex) % 2):
        sex = '男'
    else:
        sex = '女'

    return sex