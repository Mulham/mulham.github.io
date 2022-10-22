---
permalink: /sql/تعديل-جدول
layout: post
date: 2020-04-24
title: سلسلة دروس SQL| تعديل جدول
type: tutorial
lesson: 41
hidden: true
comments: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

# عبارة ALTER TABLE في SQL

يتم استخدام عبارة ALTER TABLE لإضافة أعمدة أو حذفها أو تعديلها في جدول موجود.

يتم استخدام عبارة ALTER TABLE أيضا لإضافة وإفلات قيود مختلفة على جدول موجود.

# جدول بديل - إضافة عمود

لإضافة عمود في جدول ، استخدم بناء الجملة التالي:

{% highlight sql %}

		ALTER TABLE table_name

		ADD column_name datatype;

{% endhighlight %}

يضيف SQL التالي عمود "البريد الإلكتروني" إلى جدول "العملاء":

**مثال**

{% highlight sql %}

		ALTER TABLE Customers

		ADD Email varchar(255);

{% endhighlight %}

# جدول بديل - حذف عمود


لحذف عمود في جدول ، استخدم بناء الجملة التالي (لاحظ أن بعض أنظمة قواعد البيانات لا تسمح بحذف عمود):

{% highlight sql %}

		ALTER TABLE table_name

		DROP COLUMN column_name; 

{% endhighlight %}

يحذف SQL التالي عمود "البريد الإلكتروني" من جدول "العملاء":

**مثال**

{% highlight sql %}

		ALTER TABLE Customers
		DROP COLUMN Email;

{% endhighlight %}

# جدول بديل - تعديل العمود

لتغيير نوع بيانات عمود في جدول ، استخدم بناء الجملة التالي:

**SQL Server / MS Access:**

{% highlight sql %}

		ALTER TABLE table_name

		ALTER COLUMN column_name datatype; 

{% endhighlight %}

My SQL / Oracle ( G الإصدار السابق 10):

{% highlight sql %}

		ALTER TABLE table_name

		MODIFY COLUMN column_name datatype;
 
{% endhighlight %}

Oracle 10G والإصدارات الأحدث:

{% highlight sql %}

		ALTER TABLE table_name

		MODIFY column_name datatype;

{% endhighlight %} 

# مثال عن ALTER TABLE في SQL

انظر إلى جدول "الأشخاص":

| ID 	| LastName |	FirstName |	Address |	City |
| ----- | -------- | ------------ | ----------- |------------ |
| 1 |	Hansen |	Ola |	Timoteivn 10 |	Sandnes |
| 2 |	Svendson |	Tove |	Borgvn 23 |	Sandnes |
| 3 |	Pettersen |	Kari |	Storgt 20 |	Stavanger |


نريد الآن إضافة عمود باسم "تاريخ الميلاد" في جدول "الأشخاص".

نستخدم عبارة SQL التالية:

{% highlight sql %}

		ALTER TABLE Persons

		ADD DateOfBirth date; 

{% endhighlight %} 

لاحظ أن العمود الجديد "تاريخ الميلاد" هو من نوع التاريخ وسيحتفظ بتاريخ يحدد نوع البيانات التي يمكن للعمود الاحتفاظ بها.

سيبدو جدول "الأشخاص" الآن كما يلي:

| ID |	LastName |	FirstName |	Address |	City |	DateOfBirth |
| --- | --------- | ------------- | ----------- | ---------- | ------------- |
| 1 |	Hansen |	Ola |	Timoteivn 10 |	Sandnes |                   |	
| 2 |	Svendson |	Tove |	Borgvn 23 |	Sandnes |                   |	
| 3 |	Pettersen |	Kari |	Storgt 20 |	Stavanger |                 |	

# مثال على تغيير نوع البيانات

 
نريد الآن تغيير نوع بيانات العمود المسمى "تاريخ الميلاد" في جدول "الأشخاص".

نستخدم عبارة SQL التالية:

{% highlight sql %}

		ALTER TABLE Persons

		ALTER COLUMN DateOfBirth year; 

{% endhighlight %}

لاحظ أن عمود "تاريخ الميلاد" هو الآن من نوع السنة وسيحتفظ بقيمة الأعوام بتنسيق مكون من رقمين أو أربعة أرقام.

# مثال عن DROP COLUMN

بعد ذلك ، نريد حذف العمود المسمى "تاريخ الميلاد" في جدول "الأشخاص".

نستخدم عبارة SQL التالية:

{% highlight sql %}

		ALTER TABLE Persons

		DROP COLUMN DateOfBirth; 

{% endhighlight %}

سيبدو جدول "الأشخاص" الآن كما يلي:

| ID |	LastName |	FirstName |	Address |	City |
| --- | ------- | ---------------- | ---------- | ---------- |
| 1 |	Hansen |	Ola |	Timoteivn 10 |	Sandnes |
| 2 |	Svendson |	Tove |	Borgvn 23 |	Sandnes |
| 3 | 	Pettersen |	Kari |	Storgt 20 |	Stavanger |

التالي: [القيود](القيود)
