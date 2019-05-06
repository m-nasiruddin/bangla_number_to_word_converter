#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:44:23 2018
@author: Mohammad Nasiruddin

This Python program can convert any given Bangla (Bengali) number into word.
For example, if ৩০৫০৪১ is given, it should return তিন লক্ষ পাঁচ হাজার একচল্লিশ.
This program can convert upto 100 million.
"""

one_dict = {'০': 'শুন্য', '১': 'এক', '২': 'দুই', '৩': 'তিন', '৪': 'চার', '৫': 'পাঁচ', '৬': 'ছয়', \
                                                                                    '৭': 'সাত', '৮': 'আট', '৯': 'নয়'}
ten_dict = {'১০': 'দশ', '১১': 'এগার', '১২': 'বার', '১৩': 'তের', '১৪': 'চৌদ্দ', '১৫': 'পনের', \
            '১৬': 'ষোল', '১৭': 'সতের', '১৮': 'আঠার', '১৯': 'ঊনিশ', '২০': 'বিশ', '২১': 'একুশ', \
            '২২': 'বাইশ', '২৩': 'তেইশ', '২৪': 'চব্বিশ', '২৫': 'পঁচিশ', '২৬': 'ছাব্বিশ', '২৭': 'সাতাশ', \
            '২৮': 'আঠাশ', '২৯': 'ঊনত্রিশ', '৩০': 'ত্রিশ', '৩১': 'একত্রিশ', '৩২': 'বত্রিশ', '৩৩': 'তেত্রিশ', \
            '৩৪': 'চৌত্রিশ', '৩৫': 'পঁয়ত্রিশ', '৩৬': 'ছত্রিশ', '৩৭': 'সাইত্রিশ', '৩৮': 'আটত্রিশ', \
            '৩৯': 'ঊনচল্লিশ', '৪০': 'চল্লিশ', '৪১': 'একচল্লিশ', '৪২': 'বিয়াল্লিশ', '৪৩': 'তেতাল্লিশ', \
            '৪৪': 'চুয়াল্লিশ', '৪৫': 'পঁয়তাল্লিশ', '৪৬': 'ছেচল্লিশ', '৪৭': 'সাতচল্লিশ', '৪৮': 'আটচল্লিশ', \
            '৪৯': 'ঊনপঞ্চাশ', '৫০': 'পঞ্চাশ', '৫১': 'একান্ন', '৫২': 'বায়ান্ন', '৫৩': 'তিপ্পান্ন', '৫৪': 'চুয়ান্ন', \
            '৫৫': 'পঞ্চান্ন', '৫৬': 'ছাপ্পান্ন', '৫৭': 'সাতান্ন', '৫৮': 'আটান্ন', '৫৯': 'ঊনষাট', '৬০': 'ষাট', \
            '৬১': 'একষট্টি', '৬২': 'বাষট্টি', '৬৩': 'তেষট্টি', '৬৪': 'চৌষট্টি', '৬৫': 'পঁয়ষট্টি', '৬৬': 'ছেষট্টি', \
            '৬৭': 'সাতষট্টি', '৬৮': 'আটষট্টি', '৬৯': 'ঊনসত্তুর', '৭০': 'সত্তুর', '৭১': 'একাত্তুর', \
            '৭২': 'বাহাত্তুর', '৭৩': 'তিয়াত্তুর', '৭৪': 'চুয়াত্তুর', '৭৫': 'পঁচাত্তুর', '৭৬': 'ছিয়াত্তুর', \
            '৭৭': 'সাতাত্তুর', '৭৮': 'আটাত্তুর', '৭৯': 'ঊনআশি', '৮০': 'আশি', '৮১': 'একাশি', \
            '৮২': 'বিরাশি', '৮৩': 'তিরাশি', '৮৪': 'চুরাশি', '৮৫': 'পঁচাশি', '৮৬': 'ছিয়াশি', \
            '৮৭': 'সাতাশি', '৮৮': 'আটাশি', '৮৯': 'ঊননব্বই', '৯০': 'নব্বই', '৯১': 'একানব্বই', \
            '৯২': 'বিরানব্বই', '৯৩': 'তিরানব্বই', '৯৪': 'চুরানব্বই', '৯৫': 'পঁচানব্বই', '৯৬': 'ছিয়ানব্বই', \
            '৯৭': 'সাতানব্বই', '৯৮': 'আটানব্বই', '৯৯': 'নিরানব্বই'}
hundred_dict = {'১০০': 'একশ', '২০০': 'দুইশ', '৩০০': 'তিনশ', '৪০০': 'চারশ', '৫০০': 'পাঁচশ', \
                '৬০০': 'ছয়শ', '৭০০': 'সাতশ', '৮০০': 'আটশ', '৯০০': 'নয়শ'}


def one(given_number):
    for number, word in one_dict.items():
        if number == given_number:
            return word


def ten(given_number):
    for number, word in ten_dict.items():
        if number == given_number:
            return word


def hundred(given_number):
    for number, word in hundred_dict.items():
        if number == given_number:
            return word
    if given_number[1] == '০':
        return one(given_number[0]) + 'শ ' + one(given_number[2])
    return one(given_number[0]) + 'শ ' + ten(given_number[1:])


def thousand(given_number):
    if given_number[1] == '০' and given_number[2] == '০' \
                                                    and given_number[3] == '০':
        return one(given_number[0]) + ' হাজার '
    elif given_number[1] == '০' and given_number[2] == '০':
        return one(given_number[0]) + ' হাজার ' + one(given_number[3])
    elif given_number[1] == '০':
        return one(given_number[0]) + ' হাজার ' + ten(given_number[2:])
    else:
        return one(given_number[0]) + ' হাজার ' + hundred(given_number[1:])


def ten_thousand(given_number):
    if given_number[2] == '০' and given_number[3] == '০' \
                                                    and given_number[4] == '০':
        return ten(given_number[:2]) + ' হাজার '
    elif given_number[2] == '০' and given_number[3] == '০':
        return ten(given_number[:2]) + ' হাজার ' + one(given_number[4])
    elif given_number[2] == '০':
        return ten(given_number[:2]) + ' হাজার ' + ten(given_number[3:])
    else:
        return ten(given_number[:2]) + ' হাজার ' + hundred(given_number[2:])


def hundred_thousand(given_number):
    if given_number[1] == '০' and given_number[2] == '০' \
                        and given_number[3] == '০' and given_number[4] == '০' \
                                                    and  given_number[5] == '০':
        return one(given_number[0]) + ' লক্ষ '
    elif given_number[1] == '০' and given_number[2] == '০' \
                        and given_number[3] == '০' and given_number[4] == '০':
        return one(given_number[0]) + ' লক্ষ ' + one(given_number[5])
    elif given_number[1] == '০' and given_number[2] == '০' \
                                                    and given_number[3] == '০':
        return one(given_number[0]) + ' লক্ষ ' + ten(given_number[4:])
    elif given_number[1] == '০' and given_number[2] == '০':
        return one(given_number[0]) + ' লক্ষ ' + hundred(given_number[3:])
    elif given_number[1] == '০':
        return one(given_number[0]) + ' লক্ষ ' + thousand(given_number[2:])
    else:
        return one(given_number[0]) + ' লক্ষ ' + ten_thousand(given_number[1:])


def million(given_number):
    if given_number[2] == '০' and given_number[3] == '০' \
                        and given_number[4] == '০' and given_number[5] == '০' \
                                                    and  given_number[6] == '০':
        return ten(given_number[:2]) + ' লক্ষ '
    elif given_number[2] == '০' and given_number[3] == '০' \
                        and given_number[4] == '০' and given_number[5] == '০':
        return ten(given_number[:2]) + ' লক্ষ ' + one(given_number[6])
    elif given_number[2] == '০' and given_number[3] == '০' \
                                                    and given_number[4] == '০':
        return ten(given_number[:2]) + ' লক্ষ ' + ten(given_number[5:])
    elif given_number[2] == '০' and given_number[3] == '০':
        return ten(given_number[:2]) + ' লক্ষ ' + hundred(given_number[4:])
    elif given_number[2] == '০':
        return ten(given_number[:2]) + ' লক্ষ ' + thousand(given_number[3:])
    else:
        return ten(given_number[:2]) + ' লক্ষ ' + ten_thousand(given_number[2:])


search_number = '৪৬০৩৩১৯'
if search_number[0] == '০':
    print('দুঃখিত, নম্বরের শুরুতে শুন্য রাখা যাবেনা!')
elif len(search_number) == 1:
    print(one(search_number))
elif len(search_number) == 2:
    print(ten(search_number))
elif len(search_number) == 3:
    print(hundred(search_number))
elif len(search_number) == 4:
    print(thousand(search_number))
elif len(search_number) == 5:
    print(ten_thousand(search_number))
elif len(search_number) == 6:
    print(hundred_thousand(search_number))
elif len(search_number) == 7:
    print(million(search_number))
    