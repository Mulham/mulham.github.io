# عبارة SQL  CREATE INDEX

يتم استخدام عبارة CREATE INDEX لإنشاء فهارس في الجداول.

يتم استخدام الفهارس لاسترداد البيانات من قاعدة البيانات بشكل أسرع من غير ذلك. لا يمكن للمستخدمين رؤية الفهارس ،يتم استخدامها فقط لتسريع عمليات البحث / الاستعلامات.

**ملاحظة:** تحديث الجدول باستخدام الفهارس يستغرق وقتًا أطول من تحديث الجدول بدون (لأن الفهارس تحتاج أيضًا إلى تحديث). لذا، قم فقط بإنشاء فهارس على الأعمدة التي سيتم البحث عنها بشكل متكرر.

# يناء جملةCREATE INDEX

إنشاء فهرس على جدول يسمح بقيم مكررة:

{% highlight sql %}

		CREATE INDEX index_name

		ON table_name (column1, column2, ...); 

{% endhighlight %}

# بناء جملةCREATE UNIQUE INDEX

إنشاء فهرس فريد على جدول. القيم المكررة غير مسموح بها:

{% highlight sql %}

		CREATE UNIQUE INDEX index_name

		ON table_name (column1, column2, ...); 

{% endhighlight %}

**ملاحظة:** تختلف بنية إنشاء الفهارس بين قواعد البيانات المختلفة. لذلك: تحقق من بناء الجملة لإنشاء فهارس في قاعدة البيانات الخاصة بك.

# مثال عن CREATE INDEX

تقوم جملة SQL أدناه بإنشاء فهرس باسم "idx_lastname" في عمود "اسم العائلة" في جدول "الأشخاص":

{% highlight sql %}

		CREATE INDEX idx_lastname

		ON Persons (LastName); 

{% endhighlight %}

إذا كنت تريد إنشاء فهرس على مجموعة من الأعمدة، يمكنك إدراج أسماء الأعمدة داخل الأقواس، مفصولة بفواصل:

{% highlight sql %}

		CREATE INDEX idx_pname

		ON Persons (LastName, FirstName); 

{% endhighlight %}

# حذف عبارةINDEX

يتم استخدام عبارة DROP INDEX لحذف فهرس في جدول.

**MS Access:**

{% highlight sql %}

DROP INDEX index_name ON table_name; 

{% endhighlight %}

**SQL Server:**

{% highlight sql %}

DROP INDEX table_name.index_name; 

{% endhighlight %}

**DB2/Oracle:**

{% highlight sql %}

DROP INDEX index_name; 

{% endhighlight %}

**MySQL:**

{% highlight sql %}

		ALTER TABLE table_name

		DROP INDEX index_name; 

{% endhighlight %}
***





