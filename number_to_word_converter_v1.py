#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:44:23 2018

@author: Mohammad Nasiruddin
"""

number_word_dict = {'০': 'শুন্য',
                    '১': 'এক',
                    '২': 'দুই',
                    '৩': 'তিন',
                    '৪': 'চার',
                    '৫': 'পাঁচ',
                    '৬': 'ছয়',
                    '৭': 'সাত',
                    '৮': 'আট',
                    '৯': 'নয়',
                    '১০': 'দশ',
                    '১১': 'এগার',
                    '১২': 'বার',
                    '১৩': 'তের',
                    '১৪': 'চৌদ্দ',
                    '১৫': 'পনের',
                    '১৬': 'ষোল',
                    '১৭': 'সতের',
                    '১৮': 'আঠার',
                    '১৯': 'ঊনিশ',
                    '২০': 'বিশ',
                    '২১': 'একুশ',
                    '২২': 'বাইশ',
                    '২৩': 'তেইশ',
                    '২৪': 'চব্বিশ',
                    '২৫': 'পঁচিশ',
                    '২৬': 'ছাব্বিশ',
                    '২৭': 'সাতাশ',
                    '২৮': 'আঠাশ',
                    '২৯': 'ঊনত্রিশ',
                    '৩০': 'ত্রিশ',
                    '৩১': 'একত্রিশ',
                    '৩২': 'বত্রিশ',
                    '৩৩': 'তেত্রিশ',
                    '৩৪': 'চৌত্রিশ',
                    '৩৫': 'পঁয়ত্রিশ',
                    '৩৬': 'ছত্রিশ',
                    '৩৭': 'সাইত্রিশ',
                    '৩৮': 'আটত্রিশ',
                    '৩৯': 'ঊনচল্লিশ',
                    '৪০': 'চল্লিশ',
                    '৪১': 'একচল্লিশ',
                    '৪২': 'বিয়াল্লিশ',
                    '৪৩': 'তেতাল্লিশ',
                    '৪৪': 'চুয়াল্লিশ',
                    '৪৫': 'পঁয়তাল্লিশ',
                    '৪৬': 'ছেচল্লিশ',
                    '৪৭': 'সাতচল্লিশ',
                    '৪৮': 'আটচল্লিশ',
                    '৪৯': 'ঊনপঞ্চাশ',
                    '৫০': 'পঞ্চাশ',
                    '৫১': 'একান্ন',
                    '৫২': 'বায়ান্ন',
                    '৫৩': 'তিপ্পান্ন',
                    '৫৪': 'চুয়ান্ন',
                    '৫৫': 'পঞ্চান্ন',
                    '৫৬': 'ছাপ্পান্ন',
                    '৫৭': 'সাতান্ন',
                    '৫৮': 'আটান্ন',
                    '৫৯': 'ঊনষাট',
                    '৬০': 'ষাট',
                    '৬১': 'একষট্টি',
                    '৬২': 'বাষট্টি',
                    '৬৩': 'তেষট্টি',
                    '৬৪': 'চৌষট্টি',
                    '৬৫': 'পঁয়ষট্টি',
                    '৬৬': 'ছেষট্টি',
                    '৬৭': 'সাতষট্টি',
                    '৬৮': 'আটষট্টি',
                    '৬৯': 'ঊনসত্তুর',
                    '৭০': 'সত্তুর',
                    '৭১': 'একাত্তুর',
                    '৭২': 'বাহাত্তুর',
                    '৭৩': 'তিয়াত্তুর',
                    '৭৪': 'চুয়াত্তুর',
                    '৭৫': 'পঁচাত্তুর',
                    '৭৬': 'ছিয়াত্তুর',
                    '৭৭': 'সাতাত্তুর',
                    '৭৮': 'আটাত্তুর',
                    '৭৯': 'ঊনআশি',
                    '৮০': 'আশি',
                    '৮১': 'একাশি',
                    '৮২': 'বিরাশি',
                    '৮৩': 'তিরাশি',
                    '৮৪': 'চুরাশি',
                    '৮৫': 'পঁচাশি',
                    '৮৬': 'ছিয়াশি',
                    '৮৭': 'সাতাশি',
                    '৮৮': 'আটাশি',
                    '৮৯': 'ঊননব্বই',
                    '৯০': 'নব্বই',
                    '৯১': 'একানব্বই',
                    '৯২': 'বিরানব্বই',
                    '৯৩': 'তিরানব্বই',
                    '৯৪': 'চুরানব্বই',
                    '৯৫': 'পঁচানব্বই',
                    '৯৬': 'ছিয়ানব্বই',
                    '৯৭': 'সাতানব্বই',
                    '৯৮': 'আটানব্বই',
                    '৯৯': 'নিরানব্বই',
                    '১০০': 'একশ',
                    '২০০': 'দুইশ',
                    '৩০০': 'তিনশ',
                    '৪০০': 'চারশ',
                    '৫০০': 'পাঁচশ',
                    '৬০০': 'ছয়শ',
                    '৭০০': 'সাতশ',
                    '৮০০': 'আটশ',
                    '৯০০': 'নয়শ'}
# print(number_word_dict)
# for key in number_word_dict:
#     print(key)
# print(int('২') + int('২'))
# print(2)
search_number = '৩৯১৯'


def one_ten(given_number):
    for number, word in number_word_dict.items():
        if number == given_number:
            return word


def hundred(given_number):
    hazar = ekok_dosok = ''
    for number, word in number_word_dict.items():
        if number == given_number[0]:
            hazar = word
        elif number == given_number[1:]:
            ekok_dosok = word
    return hazar + 'শ ' + ekok_dosok


def thousand(given_number):
    hazar = ''
    for number, word in number_word_dict.items():
        if number == given_number[0]:
            hazar = word
    return hazar + ' হাজার ' + hundred(given_number[1:])


if len(search_number) is 1 or len(search_number) is 2:
    one_ten(search_number)
elif len(search_number) is 3:
    print(hundred(search_number))
elif len(search_number) is 4:
    print(thousand(search_number))