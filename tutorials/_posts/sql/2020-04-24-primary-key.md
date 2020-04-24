---
permalink: /sql/primary-key
layout: post
date: 2020-04-24
title: سلسلة دروس SQL| Primary Key
type: tutorial
lesson: 45
hidden: true
comments: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

# قيد PRIMARY KEY في SQL

القيد PRIMARY KEY يعرّف بشكل فريد كل سجل في جدول.

يجب أن يحتوي PRIMARY KEY على قيم UNIQUE ، ولا يمكن أن تحتوي على قيم NULL.

يمكن أن يحتوي الجدول على مفتاح PRIMARY KEY واحد فقط ؛ وفي الجدول يمكن أن يتكون PRIMARY KEY هذا من أعمدة (حقول) مفردة أو متعددة.

# أستخدام PRIMARY KEY في CREATE TABLE في SQL

يقوم SQL التالي بإنشاء PRIMARY KEY على عمود "المعرف" عند إنشاء جدول "الأشخاص":

**MySQL:**

{% highlight sql %}

CREATE TABLE Persons (

    ID int NOT NULL,

    LastName varchar(255) NOT NULL,

    FirstName varchar(255),

    Age int,

    PRIMARY KEY (ID)

); 

{% endhighlight %}

**SQL Server / Oracle / MS Access:**

{% highlight sql %}

CREATE TABLE Persons (

    ID int NOT NULL PRIMARY KEY,

    LastName varchar(255) NOT NULL,

    FirstName varchar(255),

    Age int

); 

{% endhighlight %}

للسماح بتسمية قيد PRIMARY KEY ، ولتحديد قيد PRIMARY KEY على أعمدة متعددة ، استخدم بناء جملة SQL التالي:

**MySQL / SQL Server / Oracle / MS Access:**

{% highlight sql %}

CREATE TABLE Persons (

    ID int NOT NULL,

    LastName varchar(255) NOT NULL,

    FirstName varchar(255),

    Age int,

    CONSTRAINT PK_Person PRIMARY KEY (ID,LastName)

); 

{% endhighlight %}

**ملاحظة:** في المثال أعلاه ، يوجد PRIMARY KEY واحد فقط (PK_Person) ومع ذلك نلاحظ أنه تتكون قيمة PRIMARY KEY من اثنين من الأعمدة (ID + LastName).

# أستخدام PRIMARY KEY في ALTER TABLE في SQL

لإنشاء قيد PRIMARY KEY على عمود "المعرف" عند إنشاء الجدول  ، استخدم SQL التالية:

**MySQL / SQL Server / Oracle / MS Access:**

{% highlight sql %}

		ALTER TABLE Persons

		ADD PRIMARY KEY (ID); 

{% endhighlight %}

للسماح بتسمية قيد PRIMARY KEY ، ولتحديد قيد PRIMARY KEY على أعمدة متعددة ، استخدم بناء جملة SQL التالي:

**MySQL / SQL Server / Oracle / MS Access:**

{% highlight sql %}

		ALTER TABLE Persons

		ADD CONSTRAINT PK_Person PRIMARY KEY (ID,LastName); 

{% endhighlight %}

**ملاحظة:** إذا كنت تستخدم عبارة ALTER TABLE لإضافة PRIMARY KEY ، فيجب أن يكون عمود (أعمدة) PRIMARY KEY قد تم تعريفه بالفعل على أنه لا يحتوي على قيم NULL (عندما تم إنشاء الجدول لأول مرة).

# حذف القيد PRIMARY KEY

لحذف قيد PRIMARY KEY، استخدم عبارة SQL التالية:

**MySQL:**

{% highlight sql %}

		ALTER TABLE Persons

		DROP PRIMARY KEY; 

{% endhighlight %}

**SQL Server / Oracle / MS Access:**

{% highlight sql %}

		ALTER TABLE Persons
	
		DROP CONSTRAINT PK_Person; 

{% endhighlight %}



