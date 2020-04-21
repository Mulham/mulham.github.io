# حقن SQL

حقن SQL هو تقنية إدخال التعليمات البرمجية التي قد تدمر قاعدة البيانات الخاصة بك.

يعد حقن SQL أحد أكثر تقنيات اختراق الويب شيوعًا.

حقن SQL هو وضع التعليمات البرمجية الضارة في عبارات SQL، عبر إدخال صفحة الويب.

# SQL في صفحات الويب

عادة ما يحدث حقن  SQL عندما تطلب من المستخدم إدخال مثل اسم المستخدم / معرف المستخدم الخاص به، وبدلاً من الاسم / المعرف، يمنحك المستخدم عبارة SQL التي ستقوم بتشغيلها دون علم على قاعدة البيانات الخاصة بك.

انظر إلى المثال التالي الذي ينشئ عبارة SELECT عن طريق إضافة متغير (txtUserId) إلى سلسلة تحديد. يتم جلب المتغير من إدخال المستخدم (getRequestString):

**مثال**

{% highlight sql %}

		txtUserId = getRequestString("UserId");

		txtSQL = "SELECT * FROM Users WHERE UserId = " + txtUserId;

{% endhighlight %}

يصف الجزء المتبقي من هذا الفصل المخاطر المحتملة لاستخدام إدخال المستخدم في عبارات SQL.

# حقن SQL على أساس 1 = 1 صحيح دائمًا

انظر إلى المثال أعلاه مرة أخرى. كان الغرض الأصلي من التعليمات البرمجية إنشاء عبارة SQL لتحديد مستخدم بمعرف مستخدم معين.

إذا لم يكن هناك شيء يمنع المستخدم من إدخال الإدخال "الخاطئ" ، فيمكن للمستخدم إدخال الإدخال "الذكي" مثل هذا:

UserId: | 105 OR 1=1 |

بعد ذلك ، ستبدو عبارة SQL كما يلي:

{% highlight sql %}

		SELECT * FROM Users WHERE UserId = 105 OR 1=1;

{% endhighlight %}

SQL أعلاه صالحة وستُرجع جميع الصفوف من جدول "المستخدمون" ، حيث أن OR 1 = 1 دائمًا TRUE.

هل يبدو المثال أعلاه خطيرًا؟ ماذا لو احتوى جدول "المستخدمون" على أسماء وكلمات مرور؟

عبارة SQL أعلاه هي نفسها تقريبًا:

{% highlight sql %}

		SELECT UserId, Name, Password FROM Users WHERE UserId = 105 or 1=1; 

{% endhighlight %}

قد يتمكن المخترق من الوصول إلى جميع أسماء المستخدمين وكلمات المرور في قاعدة البيانات ، بمجرد إدخال 105 OR 1 = 1 في حقل الإدخال.

# حقن SQL على أساس "" = "" صحيح دائمًا

فيما يلي مثال لتسجيل دخول المستخدم على موقع ويب:

اسم المستخدم:

| فلان الفلاني "John Doe" |

كلمه السر:


| كلمة المرور الخاصة بي "myPass" |

**مثال**

{% highlight sql %}

		uName = getRequestString("username");

		uPass = getRequestString("userpassword");

		sql = 'SELECT * FROM Users WHERE Name ="' + uName + '" AND Pass ="' + uPass + '"'

{% endhighlight %}

**النتيجة**

{% highlight sql %}

 SELECT * FROM Users WHERE Name ="John Doe" AND Pass ="myPass" 

{% endhighlight %}

قد يتمكن المخترق من الوصول إلى أسماء المستخدمين وكلمات المرور في قاعدة بيانات بمجرد إدخال "OR" "=" في مربع نص اسم المستخدم أو كلمة المرور:

اسم المستخدم:

 | " or ""=" |

كلمه السر:

| " or ""=" |

سيقوم الكود الموجود على الخادم بإنشاء جملة SQL صالحة مثل هذا:

**النتيجة**

{% highlight sql %}

		 SELECT * FROM Users WHERE Name ="" or ""="" AND Pass ="" or ""="" 

{% endhighlight %}

إن SQL أعلاه صالحة وستُرجع جميع الصفوف من جدول "Users" ، نظرًا لأن OR "" = "" هي دائمًا TRUE.

# حقن SQL استناداً إلى عدة عبارات SQL مجتمعة

تدعم معظم قواعد البيانات جملة SQL المجمعة.

مجموعة عبارات SQL هي مجموعة من عبارات SQL أو أكثر، مفصولة بفواصل منقوطة.

ستقوم عبارة SQL أدناه بإرجاع كافة الصفوف من جدول "المستخدمون"، ثم حذف جدول "الموردين".

**مثال**

{% highlight sql %}


		SELECT * FROM Users; DROP TABLE Suppliers 

{% endhighlight %}

فلننظر إلى المثال التالي:

**مثال**

{% highlight sql %}

		txtUserId = getRequestString("UserId");

		txtSQL = "SELECT * FROM Users WHERE UserId = " + txtUserId;

{% endhighlight %}

والمدخلات التالية:

معرف المستخدم : | 105; DROP TABLE Suppliers "حذف جدول الموردين" |

ستبدو عبارة SQL الصالحة كما يلي:

**النتيجة**


{% highlight sql %}

		SELECT * FROM Users WHERE UserId = 105; DROP TABLE Suppliers

{% endhighlight %}

# استخدم معلمات SQL للحماية

لحماية موقع ويب من حقن SQL ، يمكنك استخدام معلمات SQL.

معلمات SQL هي القيم التي تتم إضافتها إلى استعلام SQL في وقت التنفيذ، بطريقة يتم التحكم فيها.

**مثال ASP.NET Razor**

{% highlight sql %}

		txtUserId = getRequestString("UserId");

		txtSQL = "SELECT * FROM Users WHERE UserId = @0";

		db.Execute(txtSQL,txtUserId);

{% endhighlight %}

لاحظ أن المعلمات ممثلة في جملة SQL بعلامة @.

يتحقق مشغل SQL من كل معلمة للتأكد من أنها صحيحة لعمودها ويتم التعامل معها بشكل حرفي ، وليس كجزء من SQL ليتم تنفيذها.

**مثال آخر**

{% highlight sql %}

		txtNam = getRequestString("CustomerName");

		txtAdd = getRequestString("Address");

		txtCit = getRequestString("City");

		txtSQL = "INSERT INTO Customers (CustomerName,Address,City) Values(@0,@1,@2)";

		db.Execute(txtSQL,txtNam,txtAdd,txtCit);

{% endhighlight %}

**أمثلة**

توضح الأمثلة التالية كيفية إنشاء استعلامات ذات معلمات في بعض لغات الويب الشائعة.

عبارة SELECT في ASP.NET:

{% highlight sql %}

		 txtUserId = getRequestString("UserId");

		sql = "SELECT * FROM Customers WHERE CustomerId = @0";

		command = new SqlCommand(sql);

		command.Parameters.AddWithValue("@0",txtUserID);

		command.ExecuteReader();

{% endhighlight %}

عبارة INSERT INTO في IN ASP.NET:

{% highlight sql %}

		txtNam = getRequestString("CustomerName");

		txtAdd = getRequestString("Address");

		txtCit = getRequestString("City");

		txtSQL = "INSERT INTO Customers (CustomerName,Address,City) Values(@0,@1,@2)";

		command = new SqlCommand(txtSQL);

		command.Parameters.AddWithValue("@0",txtNam);

		command.Parameters.AddWithValue("@1",txtAdd);

		command.Parameters.AddWithValue("@2",txtCit);

		command.ExecuteNonQuery();

{% endhighlight %}


عبارة INSERT INTO في PHP:

{% highlight sql %}

		$stmt = $dbh->prepare("INSERT INTO Customers (CustomerName,Address,City)

		VALUES (:nam, :add, :cit)");

		$stmt->bindParam(':nam', $txtNam);

		$stmt->bindParam(':add', $txtAdd);

		$stmt->bindParam(':cit', $txtCit);

		$stmt->execute();

{% endhighlight %}

***





 















