numberDay = int(input('عددي بنويسيد که به سال و هفته تبديل کنيم'))
sal = numberDay//365
baghimandeRooz = numberDay%365
hafte = baghimandeRooz//7
rooz = baghimandeRooz%7
print('تعداد سال :', sal ,'تعداد هفته', hafte, 'تعداد روز ', rooz)



