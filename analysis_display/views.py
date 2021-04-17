from django.shortcuts import render
import os
import  xml.dom.minidom
from django.conf import settings
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import re
import networkx as nx
import json
from django.http import HttpResponse, FileResponse
import pandas as pd
from collections import Counter
plt.switch_backend('agg')



def index(request):
    return render(request, 'index.html')



def map(request):
    file_path = open(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), 'rb')
    data = pd.read_csv(file_path)
    Lat_Long = data['Lat/Long'].tolist()
    sightings = []
    for i in range(0, 99):
        each_dict = {}
        each_dict['latitude'] = float(Lat_Long[i].split(' (')[-1].replace(')','').split(' ')[1])
        each_dict['longitude'] = float(Lat_Long[i].split(' (')[-1].replace(')', '').split(' ')[0])
        # print(each_dict)
        sightings.append(each_dict)

    return render(request, 'function1.html', context={'sightings': sightings})

def sightings(request):
    file_path = open(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), 'rb')
    data = pd.read_csv(file_path)
    Unique_Squirrel_ID = data['Unique Squirrel ID'].tolist()
    Date = data['Date'].tolist()
    sightings = []
    for i in range(len(Unique_Squirrel_ID)):
        each_dict = {}
        each_dict['Unique_Squirrel_ID'] = Unique_Squirrel_ID[i]
        each_dict['Date'] = Date[i]
        print(each_dict)
        sightings.append(each_dict)

    return render(request, 'function2.html', context={'sightings': sightings})


def sightings_id(request, Unique_Squirrel_ID):
    file_path = open(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), 'rb')
    data = pd.read_csv(file_path)
    Latitude = data['Y'].tolist()
    Longitude = data['X'].tolist()
    result_Unique_Squirrel_ID = data['Unique Squirrel ID'].tolist()
    Shift = data['Shift'].tolist()
    Date = data['Date'].tolist()
    Age = data['Age'].tolist()
    for i in range(len(result_Unique_Squirrel_ID)):
        if result_Unique_Squirrel_ID[i] == Unique_Squirrel_ID:
            break
    result_dict = {}
    result_dict['Unique_Squirrel_ID'] = result_Unique_Squirrel_ID[i]
    result_dict['Latitude'] = Latitude[i]
    result_dict['Longitude'] = Longitude[i]
    result_dict['Shift'] = Shift[i]
    result_dict['Date'] = Date[i]
    result_dict['Age'] = Age[i]

    return render(request, 'function5.html', context={'result_dict': result_dict})


def sightings_add(request):
    return render(request, 'function3.html')

def sightings_stats(request):
    file_path = open(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), 'rb')
    data = pd.read_csv(file_path)
    new_data = data.dropna(subset=['Hectare Squirrel Number'])
    Hectare_Squirrel_Number = new_data['Hectare Squirrel Number'].tolist()
    item_value_dict = {'x<=3': 0, '3<x<=6':0, '6<x<=9':0, '9<x<=12':0, 'x>12': 0}
    for each in Hectare_Squirrel_Number:
        each_int = int(each)
        if int(each_int) <= 3:
            item_value_dict['x<=3'] = item_value_dict['x<=3'] + 1
        if 3 < int(each_int) <= 6:
            item_value_dict['3<x<=6'] = item_value_dict['3<x<=6'] + 1
        if 6 < int(each_int) <= 9:
            item_value_dict['6<x<=9'] = item_value_dict['6<x<=9'] + 1
        if 9 < int(each_int) <= 12:
            item_value_dict['9<x<=12'] = item_value_dict['9<x<=12'] + 1
        if 12 < int(each_int):
            item_value_dict['x>12'] = item_value_dict['x>12'] + 1
    item_list = list(item_value_dict.keys())
    value_list = list(item_value_dict.values())
    plt.figure(figsize=(4.5, 2.6), dpi=100)
    plt.bar(item_list, value_list, color='MediumPurple')
    plt.tight_layout()
    picture0_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/images/videos/picture0.png')
    plt.savefig(picture0_path)
    plt.close('all')

    data1 = data.dropna(subset=['Age'])
    Age = data1['Age'].tolist()
    item_value_dict = {}
    for each in Age:
        if each not in item_value_dict.keys():
            item_value_dict[each] = 1
        else:
            item_value_dict[each] = item_value_dict[each] + 1
    item_list = list(item_value_dict.keys())
    value_list = list(item_value_dict.values())
    plt.figure(figsize=(4.5, 2.6), dpi=100)
    plt.bar(item_list, value_list, color='MediumPurple')
    plt.tight_layout()
    picture1_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/images/videos/picture1.png')
    plt.savefig(picture1_path)
    plt.close('all')

    data2 = data.dropna(subset=['Eating'])
    Eating = data2['Eating'].tolist()
    item_value_dict = {}
    for each in Eating:
        if each not in item_value_dict.keys():
            item_value_dict[each] = 1
        else:
            item_value_dict[each] = item_value_dict[each] + 1
    item_list = list(item_value_dict.keys())
    value_list = list(item_value_dict.values())
    colors = ['yellowgreen', 'lightskyblue']  # 每块颜色定义
    plt.figure(figsize=(4.5, 2.6), dpi=100)
    plt.pie(value_list,
            labels=item_list,
            colors=colors)
    plt.tight_layout()
    picture2_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/images/videos/picture2.png')
    plt.savefig(picture2_path)
    plt.close('all')

    data3 = data.dropna(subset=['Location'])
    Location = data3['Location'].tolist()
    item_value_dict = {}
    for each in Location:
        if each not in item_value_dict.keys():
            item_value_dict[each] = 1
        else:
            item_value_dict[each] = item_value_dict[each] + 1
    item_list = list(item_value_dict.keys())
    value_list = list(item_value_dict.values())
    colors = ['yellowgreen', 'lightskyblue']  # 每块颜色定义
    plt.figure(figsize=(4.5, 2.6), dpi=100)
    plt.pie(value_list,
            labels=item_list,
            colors=colors)
    plt.tight_layout()
    picture3_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/images/videos/picture3.png')
    plt.savefig(picture3_path)
    plt.close('all')

    data4 = data.dropna(subset=['Running'])
    Running = data4['Running'].tolist()
    item_value_dict = {}
    for each in Running:
        if each not in item_value_dict.keys():
            item_value_dict[each] = 1
        else:
            item_value_dict[each] = item_value_dict[each] + 1
    item_list = list(item_value_dict.keys())
    value_list = list(item_value_dict.values())
    colors = ['yellowgreen', 'lightskyblue']  # 每块颜色定义
    plt.figure(figsize=(4.5, 2.6), dpi=100)
    plt.pie(value_list,
            labels=item_list,
            colors=colors)
    plt.tight_layout()
    picture4_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/images/videos/picture4.png')
    plt.savefig(picture4_path)
    plt.close('all')

    data5 = data.dropna(subset=['Chasing'])
    Chasing = data5['Chasing'].tolist()
    item_value_dict = {}
    for each in Chasing:
        if each not in item_value_dict.keys():
            item_value_dict[each] = 1
        else:
            item_value_dict[each] = item_value_dict[each] + 1
    item_list = list(item_value_dict.keys())
    value_list = list(item_value_dict.values())
    colors = ['yellowgreen', 'lightskyblue']  # 每块颜色定义
    plt.figure(figsize=(4.5, 2.6), dpi=100)
    plt.pie(value_list,
            labels=item_list,
            colors=colors)
    plt.tight_layout()
    picture5_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/images/videos/picture5.png')
    plt.savefig(picture5_path)
    plt.close('all')


    return render(request, 'function4.html', context={'img_url0': os.path.join('../static/assets/images/videos/', 'picture0.png'),
                                                      'img_url1': os.path.join('../static/assets/images/videos/', 'picture1.png'),
                                                      'img_url2': os.path.join('../static/assets/images/videos/', 'picture2.png'),
                                                      'img_url3': os.path.join('../static/assets/images/videos/', 'picture3.png'),
                                                      'img_url4': os.path.join('../static/assets/images/videos/', 'picture4.png'),
                                                      'img_url5': os.path.join('../static/assets/images/videos/', 'picture5.png')})


def sightings_add_upload_text(request):
    if request.method == 'POST':
        Latitude = request.POST.get('Latitude')
        Longitude = request.POST.get('Longitude')
        Unique_Squirrel_ID = request.POST.get('Unique Squirrel ID')
        Shift = request.POST.get('Shift')
        Date = request.POST.get('Date')
        Age = request.POST.get('Age')
        Primary_Fur_Color = request.POST.get('Primary Fur Color')
        Location = request.POST.get('Location')
        Specific_Location = request.POST.get('Specific Location')
        Running = request.POST.get('Running')
        Chasing = request.POST.get('Chasing')
        Climbing = request.POST.get('Climbing')
        Eating = request.POST.get('Eating')
        Foraging = request.POST.get('Foraging')
        Other_Activities = request.POST.get('Other Activities')
        Kuks = request.POST.get('Kuks')
        Quaas = request.POST.get('Quaas')
        Moans = request.POST.get('Moans')
        Tail_flags = request.POST.get('Tail flags')
        Tail_twitches = request.POST.get('Tail twitches')
        Approaches = request.POST.get('Approaches')
        Indifferent = request.POST.get('Indifferent')
        Runs_from = request.POST.get('Runs from')

        data1 = {'X': Longitude, 'Y': Latitude, 'Unique Squirrel ID': Unique_Squirrel_ID,
                 'Hectare': '', 'Shift': Shift, 'Date': Date, 'Hectare Squirrel Number': '',
                 'Age': Age, 'Primary Fur Color': Primary_Fur_Color, 'Highlight Fur Color': '',
                 'Combination of Primary and Highlight Color': '', 'Color notes': '', 'Location': Location,
                 'Above Ground Sighter Measurement': '', 'Specific Location': Specific_Location, 'Running':Running,
                 'Chasing': Chasing, 'Climbing': Climbing, 'Eating':Eating, 'Foraging': Foraging,
                 'Other Activities': Other_Activities, 'Kuks': Kuks, 'Quaas':Quaas, 'Moans': Moans,
                 'Tail flags': Tail_flags, 'Tail twitches': Tail_twitches, 'Approaches': Approaches,
                 'Indifferent': Indifferent, 'Runs from': Runs_from, 'Other Interactions': '',
                 'Lat/Long': 'POINT (' + str(Longitude) + ' ' + str(Latitude) + ')'}
        df1 = pd.DataFrame(data1,index = [0])

        df1.to_csv(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), index=None,header=None, mode='a')
        return render(request, 'function3.html')


def sightings_update_upload_text(request):
    if request.method == 'POST':
        Latitude = request.POST.get('Latitude')
        Longitude = request.POST.get('Longitude')
        Unique_Squirrel_ID = request.POST.get('Unique Squirrel ID')
        Shift = request.POST.get('Shift')
        Date = request.POST.get('Date')
        Age = request.POST.get('Age')

        file_path = open(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), 'rb')
        data = pd.read_csv(file_path)
        print(data)
        index = data[data['Unique Squirrel ID'] == Unique_Squirrel_ID].index.tolist()[0]
        data.loc[index:index, ('Latitude', 'Longitude', 'Unique Squirrel ID', 'Shift', 'Date', 'Age')] = [Latitude, Longitude, Unique_Squirrel_ID,
                                                                                    Shift, Date, Age]
        data.to_csv(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), index=None, mode='w')

        file_path = open(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), 'rb')
        data = pd.read_csv(file_path)
        Latitude = data['Y'].tolist()
        Longitude = data['X'].tolist()
        result_Unique_Squirrel_ID = data['Unique Squirrel ID'].tolist()
        Shift = data['Shift'].tolist()
        Date = data['Date'].tolist()
        Age = data['Age'].tolist()
        for i in range(len(result_Unique_Squirrel_ID)):
            if result_Unique_Squirrel_ID[i] == Unique_Squirrel_ID:
                break
        result_dict = {}
        result_dict['Unique_Squirrel_ID'] = result_Unique_Squirrel_ID[i]
        result_dict['Latitude'] = Latitude[i]
        result_dict['Longitude'] = Longitude[i]
        result_dict['Shift'] = Shift[i]
        result_dict['Date'] = Date[i]
        result_dict['Age'] = Age[i]

        return render(request, 'function5.html', context={'result_dict': result_dict})




def main_index(request):
    return render(request, 'index.html')





def main_upload_file_views(request):
    File = request.FILES.get("myfile", None)
    if File is None:
        a = '请选择待识别软件!'
        return render(request, 'index.html', locals())
    else:
        file_path = open(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), 'wb+')
        for chunk in File.chunks():  # 分块写入文件
            file_path.write(chunk)
            file_path.close()
            return render(request, 'index.html', locals())

def main_download_file_views(request):
    file_path = open(os.path.join(settings.UPLOADFILES_DIRS, 'upload_file.csv'), 'rb')
    response = FileResponse(file_path)
    response['content_type']='text/csv'
    response['Content-Disposition'] = 'attachment;filename=upload_file.csv'
    return response








