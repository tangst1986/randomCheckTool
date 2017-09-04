# -*- coding: utf-8 -*-

'''
@author: m1tang
'''

import os
import xlrd
import xlwt
import random
import math
import codecs

w_file = r'result.xls'

global im_lots_dict, im_few_dict, co_lots_dict, co_few_dict, type_select
im_lots_dict = {'total':[], 'remain':[], '1':[], '2':[], '3':[], '4':[]}
im_few_dict = {'total':[], 'remain':[], '1':[], '2':[], '3':[], '4':[]}
co_lots_dict = {'total':[], 'remain':[], '1':[], '2':[], '3':[], '4':[]}
co_few_dict = {'total':[], 'remain':[], '1':[], '2':[], '3':[], '4':[]}

def find_lots_department(lots_col, im_sheet,  co_sheet):
    global im_lots_dict, im_few_dict, co_lots_dict, co_few_dict, type_select
    
    im_count = im_sheet.nrows
    co_count = co_sheet.nrows    
    
    for i in range(1, im_count):
        if type_select.decode('utf-8').encode('gb2312') in im_sheet.row_values(i)[lots_col].encode('gb2312'):
            im_lots_dict['total'].append(i)
        else:
            im_few_dict['total'].append(i)
    
    for i in range(1, co_count):
        if type_select.decode('utf-8').encode('gb2312') in co_sheet.row_values(i)[lots_col].encode('gb2312'):
            co_lots_dict['total'].append(i)
        else:
            co_few_dict['total'].append(i)
    
    
    im_lots_dict['remain'] = im_lots_dict['total']
    im_few_dict['remain'] = im_few_dict['total']
    co_lots_dict['remain'] = co_lots_dict['total']
    co_few_dict['remain'] = co_few_dict['total']
#     print im_lots_dict, im_few_dict, co_lots_dict, co_few_dict
    return

def findImDepartmetn(im_count, lots_percent, quarter_index):
    global im_lots_dict, im_few_dict
        
    im_lots_count = math.ceil(im_count * lots_percent / 100.)
    im_few_count = im_count - im_lots_count
    while im_lots_count > 0 and len(im_lots_dict['remain']) > 0:
        im_lots_dict['%s' % quarter_index].append(random.choice(im_lots_dict['remain']))
        im_lots_dict['remain'] = list(set(im_lots_dict['remain']).difference(set(im_lots_dict['%s' % quarter_index])))
        im_lots_count -= 1
    
    if im_lots_count > 0:
        im_few_count += im_lots_count
    
    while im_few_count > 0 and len(im_few_dict['remain']) > 0:
        im_few_dict['%s' % quarter_index].append(random.choice(im_few_dict['remain']))
        im_few_dict['remain'] = list(set(im_few_dict['remain']).difference(set(im_few_dict['%s' % quarter_index])))
        im_few_count -= 1
    
    if im_few_count > 0:
            im_few_dict['remain'] = list(set(im_few_dict['total']).difference(set(im_few_dict['%s' % quarter_index])))
            while im_few_count > 0 and len(im_few_dict['remain']) > 0:
                im_few_dict['%s' % quarter_index].append(random.choice(im_few_dict['remain']))
                im_few_dict['remain'] = list(set(im_few_dict['remain']).difference(set(im_few_dict['%s' % quarter_index])))
                im_few_count -= 1
                
            im_lots_count = im_few_count
            im_lots_dict['remain'] = list(set(im_lots_dict['total']).difference(set(im_lots_dict['%s' % quarter_index])))
            while im_lots_count > 0 and len(im_lots_dict['remain']) > 0:
                im_lots_dict['%s' % quarter_index].append(random.choice(im_lots_dict['remain']))
                im_lots_dict['remain'] = list(set(im_lots_dict['remain']).difference(set(im_lots_dict['%s' % quarter_index])))
                im_lots_count -= 1  
             
                 
def findCoDepartmetn(co_count, lots_percent, quarter_index):
    global co_lots_dict, co_few_dict
        
    co_lots_count = math.ceil(co_count * lots_percent / 100.)
    co_few_count = co_count - co_lots_count
    while co_lots_count > 0 and len(co_lots_dict['remain']) > 0:
        co_lots_dict['%s' % quarter_index].append(random.choice(co_lots_dict['remain']))
        co_lots_dict['remain'] = list(set(co_lots_dict['remain']).difference(set(co_lots_dict['%s' % quarter_index])))
        co_lots_count -= 1
    
    if co_lots_count > 0:
        co_few_count += co_lots_count
    
    while co_few_count > 0 and len(co_few_dict['remain']) > 0:
        co_few_dict['%s' % quarter_index].append(random.choice(co_few_dict['remain']))
        co_few_dict['remain'] = list(set(co_few_dict['remain']).difference(set(co_few_dict['%s' % quarter_index])))
        co_few_count -= 1
    
    if co_few_count > 0:
            co_few_dict['remain'] = list(set(co_few_dict['total']).difference(set(co_few_dict['%s' % quarter_index])))
            while co_few_count > 0 and len(co_few_dict['remain']) > 0:
                co_few_dict['%s' % quarter_index].append(random.choice(co_few_dict['remain']))
                co_few_dict['remain'] = list(set(co_few_dict['remain']).difference(set(co_few_dict['%s' % quarter_index])))
                co_few_count -= 1
                
            co_lots_count = co_few_count
            co_lots_dict['remain'] = list(set(co_lots_dict['total']).difference(set(co_lots_dict['%s' % quarter_index])))
            while co_lots_count > 0 and len(co_lots_dict['remain']) > 0:
                co_lots_dict['%s' % quarter_index].append(random.choice(co_lots_dict['remain']))
                co_lots_dict['remain'] = list(set(co_lots_dict['remain']).difference(set(co_lots_dict['%s' % quarter_index])))
                co_lots_count -= 1
                          
def findDepartment(im_count, co_count, lots_percent, quarter_index):
    
    findImDepartmetn(im_count, lots_percent, quarter_index)
    findCoDepartmetn(co_count, lots_percent, quarter_index)


def write_quater_result(w_excel, im_sheet, co_sheet, title, quarter_index):
    global im_lots_dict, im_few_dict, co_lots_dict, co_few_dict, file_dir
    
    im_quarter_record = im_lots_dict['%s' % quarter_index] + im_few_dict['%s' % quarter_index]
    im_quarter_record = sorted(im_quarter_record)
    
    co_quarter_record = co_lots_dict['%s' % quarter_index] + co_few_dict['%s' % quarter_index]
    co_quarter_record = sorted(co_quarter_record)
    
    if quarter_index == 1:
        w_sheet = w_excel.add_sheet('第一季度')
    elif quarter_index == 2:
        w_sheet = w_excel.add_sheet('第二季度')
    elif quarter_index == 3:
        w_sheet = w_excel.add_sheet('第三季度')
    elif quarter_index == 4:
        w_sheet = w_excel.add_sheet('第四季度')
    else:
        print 'err: quarter index overranging'
        return
    for i in range(len(title)):
        w_sheet.write(0, i, title[i])

    row_no = 1

    csv_file = os.path.join(file_dir, '%d.csv' % quarter_index)
    write_csv_file = open(csv_file, 'w+')
    write_csv_file.write(codecs.BOM_UTF8)
    data_str = ",".join("%s" % ele for ele in title)
    write_csv_file.write(data_str.encode('utf-8'))
    write_csv_file.write('\n')
    
    for ele in im_quarter_record:
        r_line = im_sheet.row_values(int(ele))
        data_str = ",".join("%s" % ele for ele in r_line)
        write_csv_file.write(data_str.encode('utf-8'))
        write_csv_file.write('\n')
        for i in range(len(r_line)):
            w_sheet.write(row_no, i, r_line[i])
        row_no += 1
    
    for ele in co_quarter_record:
        r_line = co_sheet.row_values(int(ele))
        data_str = ",".join("%s" % ele for ele in r_line)
        write_csv_file.write(data_str.encode('utf-8'))
        write_csv_file.write('\n')
        for i in range(len(r_line)):
            w_sheet.write(row_no, i, r_line[i])
        row_no += 1

    write_csv_file.close()
    
def write_result_file(im_sheet, co_sheet, w_file_path):
    title = im_sheet.row_values(0)
    w_excel = xlwt.Workbook(encoding='utf-8', style_compression=1)
        
    for i in range(4):
        write_quater_result(w_excel, im_sheet, co_sheet, title, i + 1)
    
    
    w_excel.save(w_file_path)
    
    
def clickExportFile(excel_file, i1, i2, i3, i4, co1, co2, co3, co4, lot1, lot2, lot3, lot4, select_type):
    global im_lots_dict, im_few_dict, co_lots_dict, co_few_dict, file_dir, type_select
    im_lots_dict = {'total':[], 'remain':[], '1':[], '2':[], '3':[], '4':[]}
    im_few_dict = {'total':[], 'remain':[], '1':[], '2':[], '3':[], '4':[]}
    co_lots_dict = {'total':[], 'remain':[], '1':[], '2':[], '3':[], '4':[]}
    co_few_dict = {'total':[], 'remain':[], '1':[], '2':[], '3':[], '4':[]}
    
    type_select = select_type
    
    file_dir = os.path.dirname(excel_file)
    w_file_path = os.path.join(file_dir, w_file)
    
    if os.path.exists(w_file_path):
        os.remove(w_file_path)
    
    r_excel = xlrd.open_workbook(excel_file)
    
    im_sheet = r_excel.sheet_by_index(0)
    co_sheet = r_excel.sheet_by_index(1)
    
    lots_col = 3
    
    find_lots_department(lots_col, im_sheet, co_sheet)
    
    
    im_total_count = im_sheet.nrows - 1
    co_total_count = co_sheet.nrows - 1
    
    im_percent = []
    im_percent.append(i1)
    im_percent.append(i2)
    im_percent.append(i3)
    im_percent.append(i4)
    
    co_percent = []
    co_percent.append(co1)
    co_percent.append(co2)
    co_percent.append(co3)
    co_percent.append(co4)
    
    lots_percent = []
    lots_percent.append(lot1)
    lots_percent.append(lot2)
    lots_percent.append(lot3)
    lots_percent.append(lot4)
    
    for i in range(4):
        quarter_im_count = math.ceil(im_total_count * im_percent[i] / 100.)
        quarter_co_count = math.ceil(co_total_count * co_percent[i] / 100.)
        findDepartment(quarter_im_count, quarter_co_count, lots_percent[i], i+1)
        
    write_result_file(im_sheet, co_sheet, w_file_path)
    return

def cleanup(file_dir):
    if not file_dir:
        return

    for ele in os.listdir(file_dir):
        if ele == '1.csv':
            os.remove(os.path.join(file_dir, ele))
        elif ele == '2.csv':
            os.remove(os.path.join(file_dir, ele))
        elif ele == '3.csv':
            os.remove(os.path.join(file_dir, ele))
        elif ele == '4.csv':
            os.remove(os.path.join(file_dir, ele))
        elif ele == 'result.xls':
            os.remove(os.path.join(file_dir, ele))