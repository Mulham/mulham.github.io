---
permalink: /sql/إنشاء-جدول
layout: post
date: 2020-04-17
title: سلسلة دروس SQL| إنشاء جدول
type: tutorial
lesson: 39
hidden: true
comments: true
author: husam
---

{% include sql-content.html %}

* Toc
{:toc}

# عبارة CREATE TABLE في SQL

يتم استخدام عبارة CREATE TABLE لإنشاء جدول جديد في قاعدة البيانات.

# بناء الجملة

{% highlight sql %}

		CREATE TABLE table_name (
    		column1 datatype,
    		column2 datatype,
    		column3 datatype,
   		....
		); 

{% endhighlight %}

تُحدِّد مُعامِلات العمود (parameters) أسماء أعمدة الجدول.

يُحدِّد مُعامِل نوع البيانات نوع البيانات التي يمكن للعمود الاحتفاظ بها (مثل varchar، عدد صحيح، تاريخ، إلخ).

# مثال عن CREATE TABLE في SQL

يُنشئ المثال التالي جدولًا يسمى "الأشخاص" يحتوي على خمسة أعمدة: معرف الشخص والاسم الأخير والاسم الأول والعنوان والمدينة:


{% highlight sql %}

		CREATE TABLE Persons (

    		PersonID int,

    		LastName varchar(255),

    		FirstName varchar(255),

    		Address varchar(255),

    		City varchar(255)

		);

{% endhighlight %}

عمود مُعرِّف الشخص من نوع int وسيحتوي على عدد صحيح.

أعمدة "الاسم الأخير" و "الاسم الأول" و "العنوان" و "المدينة" هي من نوع varchar وستحتوي على أحرف ، والحد الأقصى لطول هذه الحقول هو 255 حرفًا.

جدول "الأشخاص" الفارغ سيبدو الآن كما يلي:

| PersonID |	LastName |	FirstName |	Address |	City |
|---------- | ----------- | ------------ | ---------- | ------------- |
|           |             |              |            |               |

# إنشاء جدول باستخدام جدول آخر

يمكن أيضًا إنشاء نسخة من جدول موجود باستخدام CREATE TABLE.

يحصل الجدول الجديد على نفس تعريفات الأعمدة. يمكن تحديد جميع الأعمدة أو الأعمدة المحددة.

إذا قمت بإنشاء جدول جديد باستخدام جدول موجود، فسيتم تعبئة الجدول الجديد بالقيم الموجودة من الجدول القديم.


{% highlight sql %}
		
		CREATE TABLE new_table_name AS

    		SELECT column1, column2,...

    		FROM existing_table_name

    		WHERE ....; 

{% endhighlight %}

يقوم SQL التالي بإنشاء جدول جديد يسمى "جداول الاختبار" (وهي نسخة من جدول "العملاء"):

{% highlight sql %}

		CREATE TABLE TestTable AS

		SELECT customername, contactname

		FROM customers; 

{% endhighlight %}


