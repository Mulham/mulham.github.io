# عبارة DROP TABLE في SQL

يتم استخدام عبارة DROP TABLE لإسقاط جدول موجود في قاعدة بيانات.

# بناء الجملة

{% highlight sql %}

DROP TABLE table_name; 

{% endhighlight %}

**ملاحظة:** كن حذرا قبل إسقاط جدول. سيؤدي حذف جدول إلى فقدان المعلومات الكاملة المخزنة في الجدول!

مثال عن DROP TABLE في SQL

تسقط عبارة SQL التالية الجدول الحالي "Shippers":

**مثال**

{% highlight sql %}

		DROP TABLE Shippers;

{% endhighlight %}

# اقتطاع الجدول في SQL

يتم استخدام العبارة TRUNCATE TABLE لحذف البيانات داخل جدول ، ولكن ليس الجدول نفسه.


# بناء الجملة

{% highlight sql %}

		TRUNCATE TABLE table_name; 

{% endhighlight %}

***
