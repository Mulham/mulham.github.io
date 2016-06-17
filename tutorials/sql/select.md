---
layout: post
date: 2016-06-18
title: سلسلة دروس SQL|تصريح SELECT
---

الفهرس :


الدرس الأول : التعريف بـ SQL

الدرس الثاني : بناء SQL

الدرس الثالث : تصريح SELECT

الدرس الرابع : تصريح تحديد الاختلاف في SQL

الدرس الخامس : عبارة WHERE في SQL

الدرس السادس : عمليات AND & OR في SQL

الدرس السابع : دالة ORDER BY في SQL

الدرس الثامن: تصريح INSERT INTO في SQL

الدرس التاسع: تصريح UPDATE في SQL

الدرس العاشر: تصريح DELETE في SQL

*****************


يستخدم تصريح SELECT لتحديد بيانات في قاعدة البيانات .


تُخزن النتائج في جدول للنتائج يدعى مجموعة النتائج result-set


* Toc
{:toc}

# بناء تصريح SELECT 


        SELECT column_name,column_name

        FROM table_name; 

و


        SELECT * FROM table_name;

# استعراض قاعدة بيانات :



سنستخدم قاعدة البيانات المعروفة جيداً : `Northwind`


في الأسفل تحديد من جدول الزبائن Customers

![](http://1.bp.blogspot.com/-txe3CmsAcew/VODvNYC9AII/AAAAAAAABpc/-n-9ly6Kz74/s1600/Screenshot%2Bfrom%2B2015-02-15%2B21%3A09%3A44.png)

## مثال على تحديد عمود


تصريح SQL التالي يحدد اسم الزبون CustomerName و المدينة City من جدول الزبائن


        SELECT CustomerName,City FROM Customers;

## مثال على تحديد الكل


 تصريح SQL التالي يحدد كافة الأعمدة من جدول الزبائن


        SELECT * FROM Customers;

## التنقل في مجموعة النتائج


معظم برامج أنظمة قواعد البيانات تسمح بالتنقل في مجموعة النتائج باستعمل وظائف برمجية مثل :

* `Move-To-First-Record`: الانتقال للتسجيل الأول

* `Get-Record-Content`: الحصول على محتوى التسجيل

* `Move-To-Next-Record`: الانتقال للتسجيل التالي

إلخ ..


وظائف برمجية مثل هذه ليست جزء من سلسلة الشروحات هذه ، لتعلم الوصول للبيانات من خلال وظائف برمجية function calls ، يرجى الاطلاع على شروحات خارجية حول لغة البرمجة PHP أو ASP حيث يوجد الكثير من الشروحات العربية حول هذا الموضوع .


التالي: [تصريح تحديد الإختلاف في sql](select-distinct)


