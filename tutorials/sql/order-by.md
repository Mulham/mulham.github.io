---
layout: post
date: 2016-06-18
title: سلسلة دروس SQL|دالة ORDER BY
---

الفهرس :


[الدرس الأول : التعريف بـ SQL](intro)

[الدرس الثاني : بناء SQL](build)

[الدرس الثالث : تصريح SELECT](select)

[الدرس الرابع : تصريح تحديد الاختلاف في SQL](select-distinct)

[الدرس الخامس : عبارة WHERE في SQL](where)

[الدرس السادس : عمليات AND & OR في SQL](and-or)

الدرس السابع : دالة ORDER BY فيSQL

[الدرس الثامن: تصريح INSERT INTO في SQL](insert-into)

[الدرس التاسع: تصريح UPDATE في SQL](update)

[الدرس العاشر: تصريح DELETE في SQL](delete)

*****************

* Toc
{:toc}

تستخدم دالة ORDER BY لفرز مجموعة النتائج


# دالة ORDER BY في SQL


تستخدم دالة ORDER BY لفرز مجموعة النتائج بعمود واحد أو أكثر

تقوم دالة ORDER BY بفرز التسجيلات افتراضياً بحسب الترتيب الأبجدي (ascending) ، لفرز التسجيلات بعكس الترتيب الأبجدي (descending) ، استعمل دالة DESC .


# بناء ORDER BY


        SELECT column_name,column_name

        FROM table_name

        ORDER BY column_name,column_name ASC|DESC;


# استعراض قاعدة بيانات


سنستخدم في هذا الشرح قاعدة البيانات المعروفة جيداً Northwind 


في الأسفل تحديد من جدول الزبائن Customers

![customers](/assets/customers.png)



# مثال على ORDER BY


تصريح SQL التالي يحدد جميع الزبائن من جدول الزبائن ، مرتبين بحسب عمود الدولة Country


		SELECT * FROM Customers

		ORDER BY Country; 


## مثال على ORDER BY DESC


تصريح SQL التالي يحدد جميع الزبائن من جدول الزبائن ، مرتبين عكس الترتيب الأبجدي  بحسب عمود الدولة Country

		SELECT * FROM Customers

		ORDER BY Country DESC;


## مثال على ORDER BY لعدة أعمدة



 تصريح SQL التالي يحدد جميع الزبائن من جدول الزبائن ، مرتبين بحسب أعمدة الدولة Country واسم الزبون CustomerName


		SELECT * FROM Customers

		ORDER BY Country,CustomerName;

التالي: [تصريح INSERT INTO](insert-into)