---
permalink: /sql/foreign-key
layout: post
date: 2020-04-24
title: سلسلة دروس SQL| FOREIGN KEY
type: tutorial
lesson: 46
hidden: true
comments: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

# قيد FOREIGN KEY في SQL

FOREIGN KEY هو مفتاح يستخدم لربط جدولين معًا.

FOREIGN KEY هو حقل (أو مجموعة من الحقول) في أحد الجداول التي تشير إلى PRIMARY KEY في جدول آخر.

يسمى الجدول الذي يحتوي على FOREIGN KEY الجدول الفرعي ، ويسمى الجدول الذي يحتوي على candidate key الجدول المرجعي أو الجدول الأصل.

انظر إلى الجدولين التاليين:

جدول "الأشخاص":

| PersonID |	LastName |	FirstName 	| Age |
| ---------- | -------- | ------------------ | -------- |
| 1 |	Hansen |	Ola |	30 |
| 2 |	Svendson |	Tove |	23 |
| 3 |	Pettersen |	Kari |	20 |

جدول "الطلبات":

| OrderID |	OrderNumber |	PersonID |
| 1 |	77895 |	3 |
| 2 |	44678 |	3 ا
| 3 |	22456 |	2 |
| 4 |	24562 |	1 |

لاحظ أن عمود "PersonID" في جدول "الطلبات" يشير إلى عمود "Person ID" في جدول "الأشخاص".

عمود "PersonID" في جدول "الأشخاص" هو PRIMARY KEY في جدول "الأشخاص".

عمود "PersonID" في جدول "الطلبات" هو FOREIGN KEY في جدول "الطلبات".

يستخدم قيد FOREIGN KEY لمنع الإجراءات التي من شأنها تدمير الروابط بين الجداول.

يمنع القيد FOREIGN KEY أيضًا إدخال البيانات غير الصالحة في عمود FOREIGN KEY، لأنه يجب أن تكون البيانات المدخلة من أحد القيم الموجودة في الجدول الذي يشير إليه.

# استخدام FOREIGN KEY في CREATE TABLE في SQL

يقوم SQL التالي بإنشاء FOREIGN KEY في عمود "PersonID" عند إنشاء جدول "الطلبات":

**MySQL:**

{% highlight sql %}

		CREATE TABLE Orders (

    		OrderID int NOT NULL,

    		OrderNumber int NOT NULL,

   		 PersonID int,

   		 PRIMARY KEY (OrderID),

   		 FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)

		); 

{% endhighlight %}

**SQL Server / Oracle / MS Access:**

{% highlight sql %}

		CREATE TABLE Orders (

   		 OrderID int NOT NULL PRIMARY KEY,

   		 OrderNumber int NOT NULL,

    		PersonID int FOREIGN KEY REFERENCES Persons(PersonID)

		); 

{% endhighlight %}

للسماح بتسمية قيد FOREIGN KEY، ولتحديد قيد FOREIGN KEY على أعمدة متعددة، استخدم بناء جملة SQL التالي:

**MySQL / SQL Server / Oracle / MS Access:**

{% highlight sql %}

		CREATE TABLE Orders (

    		OrderID int NOT NULL,

    		OrderNumber int NOT NULL,

   		 PersonID int,

   		 PRIMARY KEY (OrderID),

   		 CONSTRAINT FK_PersonOrder FOREIGN KEY (PersonID)

  		  REFERENCES Persons(PersonID)

		); 

{% endhighlight %}

# استخدام FOREIGN KEY في ALTER TABLE في SQL

لإنشاء قيد FOREIGN KEY على عمود "PersonID" عند إنشاء جدول "الطلبات"، استخدم SQL التالية:

**MySQL / SQL Server / Oracle / MS Access:**

{% highlight sql %}

		ALTER TABLE Orders

		ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);

{% endhighlight %}

للسماح بتسمية قيد FOREIGN KEY، ولتحديد قيد FOREIGN KEY على أعمدة متعددة، استخدم بناء جملة SQL التالي:

**MySQL / SQL Server / Oracle / MS Access:** 

{% highlight sql %}

		ALTER TABLE Orders

		ADD CONSTRAINT FK_PersonOrder

		FOREIGN KEY (PersonID) REFERENCES Persons(PersonID); 

{% endhighlight %}

# حذف القيد FOREIGN KEY

لحذف قيد FOREIGN KEY، استخدم عبارة SQL التالية:

**MySQL:**

{% highlight sql %}

		ALTER TABLE Orders

		DROP FOREIGN KEY FK_PersonOrder;

{% endhighlight %} 

**SQL Server / Oracle / MS Access:**


{% highlight sql %}

		ALTER TABLE Orders

		DROP CONSTRAINT FK_PersonOrder; 

{% endhighlight %}


