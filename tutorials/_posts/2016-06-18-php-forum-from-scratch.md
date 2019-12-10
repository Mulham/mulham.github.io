---
layout: post
date: 2016-06-20
title: إنشاء منتدى PHP من الصفر
description: شرح شامل ومُيسَّر لطريقة إنشاء منتدى متكامل باستخدام php و MySQL من البداية
type: tutorial
comments: true
tags: [PHP, برمجة]
---
هذا الدرس من تأليف Evert padje وترجمتي (ملهم) مع إضافتي للتحديثات اللازمة، يركّز الدرس على إنشاء منتدى باستخدام php و Mysql من أجل قاعدة بيانات المنتدى ..

سنقوم في هذا الشرح ببناء منتدى PHP/MySQL من الصفر. هذا الشرح أيضاً ممتاز للاعتياد على أساسيات لغة البرمجة php وقواعد بيانات MySQL . لنبدأ سويةً !



* Toc
{:toc}

# أولاً : إنشاء جداول قاعدة البيانات :

 

دائماً ، وقبل البدء بإنشاء أي تطبيق وب،  من الجيد القيام بإنشاء قاعدة بيانات جيدة لإدخال البيانات بشكل جيد . لنصف تطبيقنا الذي نريد إنشاؤه بجملة واحدة : سنقوم بإنشاء منتدى يحوي على مستخدمين يقوموا بإنشاء مواضيع بـ تصنيفات مختلفة ، المستخدمين الآخرين يمكنهم إضافة تعليق .

وكما ترى ، لقد قمت بالتركيز على كلمات معينة لتمثل أسماء الجداول في قاعدة البيانات التي نريدها .

 

* المستخدمون users

* التصنيفات categories

* المواضيع topics

* التعليقات replies

 

العناصر الثلاثة الأخيرة مرتبطة ببعضها البعض ، لذا سنقوم بعمل ذلك في تصميم الجدول .

> يمكن إنشاء قاعدة بيانات MySQL باستخدام أوامر Sql ، ولكننا هنا سنستخدم برنامج بواجهة رسومية ليسهل العملية ويجعلها مفهومة أكثر ، وممتعة أكثر . البرنامج هو [Workbench](http://dev.mysql.com/downloads/workbench/)  ، يمكنك التعرف عليه أكثر من خلال هذه المشاركة ، ولكن ذلك غير مطلوب لفهم تكملة هذا الشرح .

ألقِ نظرة على المخطط أدناه

![كيفية عمل منتدى باستخدام php و MySQL من الصفر](/assets/php.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر")

يبدو مرتباً أليس كذلك ؟ كل مربع هو عبارة عن جدول في قاعدة البيانات . جميع الأعمدة مدونة داخل كل جدول .. والخطوط بين الجداول تمثل العلاقة بينهم . سوف نشرح ذلك لاحقاً ، لا بأس إن لم تفهم الكثير الآن ..

سوف نناقش كل جدول بشرح أوامر Sql . والتي تم إنشاءها تلقائياً مع إنشاء المخطط في الأعلى . لصنع كودك الخاص يمكنك إنشاء مخطط مشابه وستحصل على أوامر الـ Sql التي قامت بإنشاء المخطط أيضاً . بعض محررات قواعد البيانات مثل MySQL Workbench الذي قمنا بإستخدامه لإنتاج ذلك المخطط ينتج ملفات بلاحقة Sql أيضاً . ولكننا ننصح تعلم أوامر Sql حيث ستجد الأمر ممتعاً . لمقدمة حول Sql يمكنك قراءة المشاركة [هنا](/sql/intro) .

## جدول المستخدمين

{% highlight sql %}

CREATE TABLE users (
user_id
INT(8) NOT NULL AUTO_INCREMENT,
user_name
VARCHAR (30) NOT NULL,
user_pass
VARCHAR (255) NOT NULL,
user_email VARCHAR (255) NOT NULL,
user_date
DATETIME NOT NULL,
user_level INT(8) NOT NULL,
UNIQUE INDEX user_name_unique (user_name),
PRIMARY KEY (user_id)
) TYPE=INNODB;

{% endhighlight %} 

> **تحديث**: في بعض إصدارات mysql قد يحدث خطأ عند كتابة الأمر أعلاه وكذلك أوامر sql في الأسفل، إذا حصلت على رسالة خطأ فقم دائماً باستبدال السطر الأخير TYPE=INNODB بـ Engine=InnoDB


تستخدم عبار `CREATE TABLE` لإنشاء جدول جديد. يتبع هذه العبارة اسم الجدول المراد إنشاؤه، ويتم وضع جميع أعمدة الجدول بين قوسين. بالنسبة لأسماء الحقول فهي تشرح نفسها بنفسها، لذا سنناقش الآن أنواع البيانات فقط.

### user_id

مفتاح أولي يستخدم لتعريف كل عمود في الجدول بشكل فريد (غير قابل للتكرار).
نوع هذا الحقل هو `INT`، وهذا يعني أن الحقل يجب أن يحوي على عدد صحيح (غير عشري). ولا يمكن لهذا الحقل أن يكون فارغاً بما أننا استخدمنا عبارة (NOT NULL). يمكن أن ترى في أسفل الجدول أن حقل user_id تم تحديده على أنه مفتاح أولي (primary key). يستخدم المفتاح الأولي كما ذكرنا لتعريف كل عمود في الجدول بشكل فريد،أي لا يمكن لأي عمودين في الجدول أن يكون لهم نفس القيمة لهذا الحقل. الكلام غير واضح؟ بالمثال يزول الإشكال :

لدينا مستخدم على سبيل المثال يدعى أحمد، إذا قام مستخدم آخر بالتسجيل وبنفس الاسم، فسيكون هناك مشكلة. ﻷنه لا يمكن التفريق بين أحمد هذا وأحمد ذاك. لا يمكنك التفريق ولا يمكن حتى لقاعدة البيانات حينها التفريق بينهم. يتم حل هذه المشكلة باستخدام المتاح الأولي (primary key) ، حيث سيعطى للاسمين رقم مختلف.

جميع الجداول الأخرى تحوي على مفاتيح أولية وتعمل بنفس الطريقة.

### user_name

هذا حقل نصي (وليس رقمي كالحقل السابق). يدعي الحقل بلغة SQL حقل VARCHAR وهو أحد أنواع الحقول النصية. الرقم بين الأقواس هو أقصى طول لعدد الأحرف التي يمكن أن يتم إدخالها في الحقل. في حالتنا هذه يمكن للمستخدم اختيار اسم يبلغ طوله كحد أقصى 30 حرف. ولا يمكن لهذا الحقل أن يكون فارغاً (NOT NULL)، سترى أسفل الجدول أن هذا الحقل تم تحديده على أنه فريد (UNIQUE)، وهذا يعني أنه لا يمكن لشخصين التسجيل بنفس الاسم.

الجزء الذي يحوي على عبارة `UNIQUE INDEX` يُخبر قاعدة البيانات أننا نريد إضافة مفتاح فريد (UNIQUE KEY)، بعدها قمنا بتحديد اسم المفتاح الفريد وهو هنا `user_name_unique` ، وبين الأقواس اسم الحقل الذي سينطبق المفتاح الفريد عليه (ليصبح غير قابل لتكرار قيمته مرتين في الجدول).

### user_pass

هذا الحقل نفس الحقل السابق، باستثناء الطول الأقصى له ، فبما أن كلمة سر المستخدم ومهما كان طولها سيتم تشفيرها لنوع تشفير sha1 ، فكلمة السر ستكون دائماً مع نوع التشفير هذا بطول 40 حرف.

توضيح: حين تدخل أي كملة سر ولنفترض 123 أو لتكن mulham أو أي شيئ آخر ومهما يكن طول كلمة السر التي ستدخلها، يتم تطبيق تشفير لكلمة السر هذه قبل حفظها في قاعدة البيانات وذلك للأمان، بحيث اذا استطاع أحد ما بالوصول لقاعدة البيانات بالخطأ، فلن يتمكن من معرفة كلمات سر المستخدمين، وهناك أنواع كثير للتشفير منها هذا النوع `sha1` والذي يحول أي كلمة سر ل 40 حرف (أحرف وأرقام)، وعند نموذج دخول المستخدم (بعد اشتراكه)، نطبق نفس نوع التشفير على كلمة السر المدخلة لنقارن قيمة تشفير الكلمة المدخلة مع قيمة التشفير المحفوظة في قاعدة البيانات، فإذا طابقها، ولج المستخدم للموقع بشكل صحيح.

### user_email

هذا الحقل هو تماماً نفس الحقل السابق (بالنسبة لقاعدة البيانات، أما لاحقاً عند عمل نموذج دخول بلغة HTML فيختلف الموضوع قليلاً )

### user_date

في هذا الحقل يتم تخزين التاريخ الذي قام به المستخدم بالتسجيل. نوع هذا الحقل هو `DATETIME` ولا يمكن أن يكون فارغ. (يتم تعبئة الحقل تلقائياً بحسب توقيت السيرفر).

### user_level

يحوي هذا الحقل مستوى المستخدم، على سبيل المثال: 0 للمستخدم العادي و 1 للمدير. ستتعرف على المزيد لاحقاً.

## جدول التصنيفات

{% highlight sql %}

CREATE TABLE categories (
cat_id
INT(8) NOT NULL AUTO_INCREMENT,
cat_name
VARCHAR (255) NOT NULL,
cat_description
VARCHAR(255) NOT NULL,
UNIQUE INDEX cat_name_unique (cat_name),
PRIMARY KEY (cat_id)
) TYPE=INNODB

{% endhighlight %} 

أنواع البيانات هنا تعمل بشكل أساسي بنفس الطريقة التي تعمل بها أنواع البيانات في جدول المستخدمين. يحوي هذا الجدول أيضاً مفتاح أولي ، واسم التصنيف يجب أن يكون فريد .

## جدول المواضيع

{% highlight sql %}

CREATE TABLE topics (
topic_id
INT(8) NOT NULL AUTO_INCREMENT,
topic_subject
VARCHAR(255) NOT NULL,
topic_date
DATETIME NOT NULL,
topic_cat
INT(8) NOT NULL,
topic_by
INT(8) NOT NULL,
PRIMARY KEY (topic_id)
) TYPE=INNODB;

{% endhighlight %} 

هذا الجدول تقريباً نفس الجداول السابقة، باستثناء حقل `topic_by` والذي يشير للمستخدم المنشئ للموضوع. وحقل `topic_cat` الذي يشير للتصنيف الذي يتبع الموضوع له. لا يمكن تحديد العلاقات بين هذه الحقول بذكر أسماء الحقول فقط. فيجب أن نُعلم قاعدة البيانات أن هذا الحقل (`topic_by`) يجب أن يحتوي على الرقم التسلسلي `user_id` لمستخدم موجود في جدول المستخدمين، والحقل الآخر (`topic_cat`) يجب أن يحتوي على الرقم التسلسلي cat_id لتصنيف موجود في جدول التصنيفات. سنضيف هذه العلاقات بين الحقول والجداول بعد مناقشة جدول التعليقات.

## جدول التعليقات

{% highlight sql %}

CREATE TABLE posts (
post_id
INT(8) NOT NULL AUTO_INCREMENT,
post_content
TEXT NOT NULL,
post_date
DATETIME NOT NULL,
post_topic
INT(8) NOT NULL,
post_by
INT(8) NOT NULL,
PRIMARY KEY (post_id)
) TYPE=INNODB;

{% endhighlight %} 

هذا الجدول هو نفس بقية الجداول، ويوجد هنا أيضاً حقل يشير لرقم مستخدم user_id في جدول المستخدمين : حقل `post_by` ، حقل `post_topic` يشير للموضوع الذي يتبع التعليق له .

المفتاح الخارجي `foreign key` هو قيد مرجعي بين جدولين. يُعرِّف المفتاح الخارجي عمود أو مجموعة أعمدة في جدول (مرجعي) والذي يشير لعمود أو مجموعة أعمدة في جدول (مرجعي) آخر .

الآن وبعد تنفيذ هذه التعليمات وإنشاء الجداول. أصبح لدينا ترتيب بيانات جيد، ولكن العلاقات بين هذه البيانات مازالت مفقودة. لنبدأ بتعريف أحد هذه العلاقات. سوف نستخدم شيئ يدعي المفتاح الخارجي. بعض الشروط لهذا الاستخدام:

* العمود في الجدول المرجعي والذي يشير له المفتاح الخارجي يجب أن يكون مفتاح أولي.

* القيم المشار لها يجب أن تكون موجودة في الجدول المرجعي.

أعرف أن كل هذه المصطلحات جديدة عليك، ولكنك ستكتشف أنها بسيطة جداً، هي فقط علاقة بين جدول وآخر ، ستتضح لك الأمور في السطور القادمة.

بإضافة مفاتيح خارجية تصبح المعلومات مرتبطة ببعضها، وهذا مهم جداً في ترتيب قاعدة البيانات.

الآن أصبحت تعرف نوعاً ما ما هو المفتاح الخارجي ولماذا نستخدمه. حان الوقت لإضافة مفاتيح خارجية للجداول التي أنشأناها باستخدام عبارة `ALTER`، والتي تستخدم لتعديل جدول موجود مسبقاً.

سنقوم في البداية بربط المواضيع بالتصنيفات:

{% highlight sql %}

ALTER TABLE topics ADD FOREIGN KEY(topic_cat) REFERENCES categories(cat_id) ON DELETE CASCADE ON UPDATE CASCADE;

{% endhighlight %} 

الجزء الأخير من التعليمة يوضح ما يجري. فعندما يتم حذف التصنيف من قاعدة البيانات، جميع المواضيع المرتبطة بهذا التصنيف سيتم حذفها أيضاً. إذا تم تغيير قيمة cat_id لتصنيف ما، جميع المواضيع المرتبطة بهذا التصنيف سيتم تحديثها أيضاً. وهذا ما تقوم به عبارة `ON UPDATE CASCADE` . بالطبع يمكنك التراجع عن ذلك لحماية بياناتك، وذلك بجعل حذف تنصيف ما غير ممكن ما زال هناك مواضيع مرتبطة بهذا التصنيف، إذا أردت القيام بذلك، فعليك استبدال `ON DELETE` `CASCADE` إلى `ON DELETE RESTRICT` . يوجد أيضاً عبارات `SET NULL` أي اجعله فارغاً و `NO ACTION` أي لا تقم بأي إجراء.

الآن، كل موضوع أصبح مرتبط بتصنيف ما. لنقم بربط المواضيع بالمستخدمين المنشئين لهم.

{% highlight sql %}

ALTER TABLE topics ADD FOREIGN KEY(topic_by) REFERENCES users(user_id) ON DELETE RESTRICT ON UPDATE CASCADE;

{% endhighlight %} 

المفتاح الخارجي هنا هو نفسه كسابقه، ولكن هناك فرق واحد: لا يمكن حذف المستخدم ما زال هناك مواضيع مرتبطة به، أو بالأحرى مرتبطة بـ `user_id` للمستخدم (رقمه التسلسلي في قاعدة البيانات). لم نضع هنا `ON DELETE CASCADE`  ﻷننا لا نريد للمعلومات المرتبطة بحساب ما والتي قد تكون قيمة أن تُحذف عندما يقرر المستخدم حذف حسابه. 
لإبقاء خيار حذف الحساب متاحاً للمستخدمين، يجب أن تقوم بإنشاء ميزة تنقل المواضيع لحساب "مجهول" عند حذف مستخدم لحسابه. وفي الواقع هذا ليش موضوع نقاشنا في هذا الشرح.

ربط التعليقات بالمواضيع:

{% highlight sql %}

ALTER TABLE posts ADD FOREIGN KEY(post_topic) REFERENCES topics(topic_id) ON DELETE CASCADE ON UPDATE CASCADE;

{% endhighlight %} 

وأخيراً، ربط كل تعليق بالمستخدم المنشئ له:

{% highlight sql %}

ALTER TABLE posts ADD FOREIGN KEY(post_by) REFERENCES users(user_id) ON DELETE RESTRICT ON UPDATE CASCADE;

{% endhighlight %} 

انتهى الجزء الخاص بقاعدة البيانات! لقد كان عملاً متعباً نوعاً ما، ولكن النتيجة تستحق هذا العمل، حيث حصلنا على قاعدة بيانات نموذجبة.

# ثانياً: مقدمة لنظام الترويسة/التذييل

كل صفحة في منتدانا تتطلب بعض الأشياء الأساسية، مثل بعض الترميزات والتنسيقات. ولذا سنقوم بتضمين ملف الترويسة header.php بأعلى كل صفحة في المنتدى، والتذييل footer.php أسفل كل صفحة. يتضمن ملف الترويسة الترميزات الأساسية وروابط للملفات التي يجب تحميلها لعرض المنتدى بشكل جيد، وكذلك بعض المعلومات المهمة حول المنتدى، مثل العنوان والأيقونة والشعار..

## ملف الترويسة header.php

{% highlight php %}

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="nl" lang="nl">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="description" content="A short description." />
    <meta name="keywords" content="put, keywords, here" />
    <title>PHP-MySQL forum</title>
    <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
<h1>My forum</h1>
    <div id="wrapper">
    <div id="menu">
        <a class="item" href="/forum/index.php">Home</a> -
        <a class="item" href="/forum/create_topic.php">Create a topic</a> -
        <a class="item" href="/forum/create_cat.php">Create a category</a>
         
        <div id="userbar">
        <div id="userbar">Hello Example. Not you? Log out.</div>
    </div>
        <div id="content">

{% endhighlight %} 

سنستخدم وسم `<div id="wrapper">`  لجعل تنسيق كامل الصفحة أسهل. الوسم `<div id="menu">` كما هو واضح يضم قائمة بروابط لصفحات الموقع التي سننشؤها لاحقاً. وسم `<div id="userbar">` سيستخدم كشريط علوي يضم معلومات مثل اسم المستخدم ورابط لتسجيل الخروج. والوسم الأخير سيحوي بشكل واضح المعلومات الفعلية للصفحة التي يكون بها المستخدم.

إذا كنت تقرأ بانتباه، فربما لاحظت أننا فقدنا شيئاً ما. فلم ننهي وسمي `<html>` و `<body>` كما هو واجب في لغة html. أي لم نكتب في نهاية ملف الترويسة `</body> >/html>`
والسبب هو أننا سنضعهم في ملف التذييل `footer.php` :

{% highlight php %}

</div><!-- content -->
</div><!-- wrapper -->
<div id="footer">Created for Nettuts+</div>
</body>
</html>

{% endhighlight %} 

عندما نضمّن ملفي الترويسة والتذييل في كل صفحة، فإن محتوى الصفحة الفعلي سيظهر بين الترويسة (بداية الصفحة) والتذييل (نهاية الصفحة). لهذه الطريقة عدة فوائد. أولها وأهمها أن كل شيئ سيكون منسق بشكل صحيح. مثال سريع :

{% highlight php %}

<?php
$error = false;
if($error == false)
{
    //the beautifully styled content, everything looks good
    echo '<div id="content">some text</div>';
}
else
{
    //bad looking, unstyled error :-( 
} 
?>

{% endhighlight %} 

كما ترى، إذا لم يحدث أخطاء في الصفحة فستظهر بشكل أنيق. أما اذا كان هناك خطأ، فكل شيئ سيكون مبعثر. ولهذا السبب يجب دائماً التأكد ليس من تنسيق المحتوى فقط، وإنما أيضاً من الأخطاء التي يمكن أن تحدث.

ميزة أخرى لهذه الطريقة (تضمين ملفي الترويسة والتذييل) هو إمكانية عمل تغييرات سريعة. فسترى أنك وبعد إنهاء هذا الشرح إذا أردت التعديل على ملف التذييل مثلاً footer.php، فسترى أن التذييل سينطبق مباشرة على كل صفحة في المنتدى. 

أخيراً سوف نقوم بإضافة بعض التنسيقات لملف الترويسة header.php والتي تزودنا بإظهارات وترميزات أساسية. لا شيئ معقد هنا، ولا داعي لفهم الكود.

{% highlight css %}

<style>
body {
    background-color: #4E4E4E;
    text-align: center;         /* make sure IE centers the page too */
}
 
#wrapper {
    width: 900px;
    margin: 0 auto;             /* center the page */
}
 
#content {
    background-color: #fff;
    border: 1px solid #000;
    float: left;
    font-family: Arial;
    padding: 20px 30px;
    text-align: left;
    width: 100%;                /* fill up the entire div */
}
 
#menu {
    float: left;
    border: 1px solid #000;
    border-bottom: none;        /* avoid a double border */
    clear: both;                /* clear:both makes sure the content div doesn't float next to this one but stays under it */
    width:100%;
    height:20px;
    padding: 0 30px;
    background-color: #FFF;
    text-align: left;
    font-size: 85%;
}
 
#menu a:hover {
    background-color: #009FC1;
}
 
#userbar {
    background-color: #fff;
    float: right;
    width: 250px;
}
 
#footer {
    clear: both;
}
 
/* begin table styles */
table {
    border-collapse: collapse;
    width: 100%;
}
 
table a {
    color: #000;
}
 
table a:hover {
    color:#373737;
    text-decoration: none;
}
 
th {
    background-color: #B40E1F;
    color: #F0F0F0;
}
 
td {
    padding: 5px;
}
 
/* Begin font styles */
h1, #footer {
    font-family: Arial;
    color: #F1F3F1;
}
 
h3 {margin: 0; padding: 0;}
 
/* Menu styles */
.item {
    background-color: #00728B;
    border: 1px solid #032472;
    color: #FFF;
    font-family: Arial;
    padding: 3px;
    text-decoration: none;
}
 
.leftpart {
    width: 70%;
}
 
.rightpart {
    width: 30%;
}
 
.small {
    font-size: 75%;
    color: #373737;
}
#footer {
    font-size: 65%;
    padding: 3px 0 0 0;
}
 
.topic-post {
    height: 100px;
    overflow: auto;
}
 
.post-content {
    padding: 30px;
}
 
textarea {
    width: 500px;
    height: 200px;
}
</style>

{% endhighlight %} 

# ثالثاً: البدء بالتنفيذ الفعلي

قبل أن نستطيع قراءة أي شيئ من قاعدة البيانات، يجب أن نقيم اتصال بها. وهذا ما سيقوم به ملف connect.php الذي سنضمنه بكل ملف ننشؤه.

{% highlight php %}

<?php
//connect.php
$server = 'localhost';
$username   = 'usernamehere';
$password   = 'passwordhere';
$database   = 'databasenamehere';
 
if(!mysql_connect($server, $username,  $password))
{
    exit('Error: could not establish database connection');
}
if(!mysql_select_db($database))
{
    exit('Error: could not select the database');
}
?>

{% endhighlight %} 

ببساطة استبدل فقط القيم الافتراضية للمتغيرات في أعلى الكود ببياناتك الخاصة. احفظ الملف ودعنا ننطلق للتكملة.

> **تحديث**: إذا كنت تستخدم php7 فلن يعمل الكود أعلاه، بل يجب كتابة الكود التالي مع استبدال القيم أيضاً

{% highlight php %}

<?php
try {
    $user = 'root';
    $pass = 'Password here';
    $dbh = new PDO('mysql:host=localhost;dbname=Name of Database Here', $user, $pass);

    $dbh = null;
} catch (PDOException $e) {
    print "Error!: " . $e->getMessage() . "<br/>";
    die();
}
?>

{% endhighlight %}

# رابعاً: عرض المنتدى

بما أننا بدأنا بتقنيات أساسية، سنقوم بعمل طريقة عرض مبسطة للمنتدى الآن. وبالتالي سنقوم بإنشاء الصفحة الرئيسية للمنتدى index.php

{% highlight php %}

<?php
//index.php
include 'connect.php';
include 'header.php';
         
echo '<tr>';
    echo '<td class="leftpart">';
        echo '<h3><a href="category.php?id=">Category name</a></h3> Category description goes here';
    echo '</td>';
    echo '<td class="rightpart">';
            echo '<a href="topic.php?id=">Topic subject</a> at 10-10';
    echo '</td>';
echo '</tr>';
include 'footer.php';
?>

{% endhighlight %} 

الآن اكتمل منتداك تقريباً. بفتحك لهذا الملف من السيرفر ستشاهد المنتدى بشكل أنيق وبسيط. سنقوم خلال بقية الشرح بتحديث هذا الملف لنحصل على النتيجة النهائية، خطوة بخطوة!

# خامساً: اشتراك مستخدم

دعنا الآن ننشئ نموذج اشتراك بسيط بلغة html حيث يمكن للمستخدمين الاشتراك بالمنتدى

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-2](/assets/2.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-2")

سنحتاج أيضاً لصفحة بلغة php لإرسال بيانات النموذج لقاعدة البيانات وإتمام اشتراك المستخدم. سنقوم باستخدام المتغير  `$_SERVER` .
المتغير `$_SERVER` يحوي مجموعة من القيم التي يتم تعيينها تلقائياً مع كل طلب. أحد هذه القيم هو `REQUEST_METHOD` . عندما يتم طلب صفحة بواسطة `GET` . فسيحمل هذا المتغير القيمة `GET` . وعندما يتم طلب الصفحة بواسطة `POST` ، فسيحمل المتغير القيمة `POST` . ولذا سنستخدم هذا المتغير لمعرفة إذا تم إرسال النموذج (بواسطة `POST`). انظر صفحة الاشتراك signup.php أدناه

{% highlight php %}

<?php
//signup.php
include 'connect.php';
include 'header.php';
 
echo '<h3>Sign up</h3>';
 
if($_SERVER['REQUEST_METHOD'] != 'POST')
{
    /*the form hasn't been posted yet, display it
      note that the action="" will cause the form to post to the same page it is on */
    echo '<form method="post" action="">
        Username: <input type="text" name="user_name" />
        Password: <input type="password" name="user_pass">
        Password again: <input type="password" name="user_pass_check">
        E-mail: <input type="email" name="user_email">
        <input type="submit" value="Submit" />
     </form>';
}
else
{
    /* so, the form has been posted, we'll process the data in three steps:
        1.  Check the data
        2.  Let the user refill the wrong fields (if necessary)
        3.  Save the data 
    */
    $errors = array(); /* declare the array for later use */
     
    if(isset($_POST['user_name']))
    {
        //the user name exists
        if(!ctype_alnum($_POST['user_name']))
        {
            $errors[] = 'The username can only contain letters and digits.';
        }
        if(strlen($_POST['user_name']) > 30)
        {
            $errors[] = 'The username cannot be longer than 30 characters.';
        }
    }
    else
    {
        $errors[] = 'The username field must not be empty.';
    }
     
     
    if(isset($_POST['user_pass']))
    {
        if($_POST['user_pass'] != $_POST['user_pass_check'])
        {
            $errors[] = 'The two passwords did not match.';
        }
    }
    else
    {
        $errors[] = 'The password field cannot be empty.';
    }
     
    if(!empty($errors)) /*check for an empty array, if there are errors, they're in this array (note the ! operator)*/
    {
        echo 'Uh-oh.. a couple of fields are not filled in correctly..';
        echo '<ul>';
        foreach($errors as $key => $value) /* walk through the array so all the errors get displayed */
        {
            echo '<li>' . $value . '</li>'; /* this generates a nice error list */
        }
        echo '</ul>';
    }
    else
    {
        //the form has been posted without, so save it
        //notice the use of mysql_real_escape_string, keep everything safe!
        //also notice the sha1 function which hashes the password
        $sql = "INSERT INTO
                    users(user_name, user_pass, user_email ,user_date, user_level)
                VALUES('" . mysql_real_escape_string($_POST['user_name']) . "',
                       '" . sha1($_POST['user_pass']) . "',
                       '" . mysql_real_escape_string($_POST['user_email']) . "',
                        NOW(),
                        0)";
                         
        $result = mysql_query($sql);
        if(!$result)
        {
            //something went wrong, display the error
            echo 'Something went wrong while registering. Please try again later.';
            //echo mysql_error(); //debugging purposes, uncomment when needed
        }
        else
        {
            echo 'Successfully registered. You can now <a href="signin.php">sign in</a> and start posting! :-)';
        }
    }
}
 
include 'footer.php';
?>

{% endhighlight %} 
 
**تحديث**: إذا كنت تستخدم الإصدارات الحديثة وبالتالي mysqli استخدم الكود التالي بدلأ من الكود أعلاه

{% highlight php %}

<?php
//signup.php
include 'connect.php';
include 'header.php';
 
echo '<h3>Sign up</h3>';
 
if($_SERVER['REQUEST_METHOD'] != 'POST')
{
    /*the form hasn't been posted yet, display it
      note that the action="" will cause the form to post to the same page it is on */
    echo '<form method="post" action="">
        Username: <input type="text" name="user_name" />
        Password: <input type="password" name="user_pass">
        Password again: <input type="password" name="user_pass_check">
        E-mail: <input type="email" name="user_email">
        <input type="submit" value="submit" />
     </form>';
}
else
{
    /* so, the form has been posted, we'll process the data in three steps:
        1.  Check the data
        2.  Let the user refill the wrong fields (if necessary)
        3.  Save the data 
    */
    $errors = array(); /* declare the array for later use */
     
    if(isset($_POST['user_name']))
    {
        //the user name exists
        if(!ctype_alnum($_POST['user_name']))
        {
            $errors[] = 'The username can only contain letters and digits.';
        }
        if(strlen($_POST['user_name']) > 30)
        {
            $errors[] = 'The username cannot be longer than 30 characters.';
        }
    }
    else
    {
        $errors[] = 'The username field must not be empty.';
    }
     
     
    if(isset($_POST['user_pass']))
    {
        if($_POST['user_pass'] != $_POST['user_pass_check'])
        {
            $errors[] = 'The two passwords did not match.';
        }
    }
    else
    {
        $errors[] = 'The password field cannot be empty.';
    }
     
    if(!empty($errors)) /*check for an empty array, if there are errors, they're in this array (note the ! operator)*/
    {
        echo 'Uh-oh.. a couple of fields are not filled in correctly..';
        echo '<ul>';
        foreach($errors as $key => $value) /* walk through the array so all the errors get displayed */
        {
            echo '<li>' . $value . '</li>'; /* this generates a nice error list */
        }
        echo '</ul>';
    }
    else
    {
        //the form has been posted without, so save it
        //notice the use of mysql_real_escape_string, keep everything safe!
        //also notice the sha1 function which hashes the password
                    $conn = mysqli_connect("localhost","root","Stccpe+2009","php");
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }  
        $sql = "INSERT INTO
                    users(user_name, user_pass, user_email ,user_date, user_level)
                VALUES('" . mysqli_real_escape_string($conn, $_POST['user_name']) . "',
                       '" . sha1($_POST['user_pass']) . "',
                       '" . mysqli_real_escape_string($conn, $_POST['user_email']) . "',
                        NOW(),
                        0)";
   
        $result = mysqli_query($conn,$sql);
        if(!$result)
        {
            //something went wrong, display the error
            echo 'Something went wrong while registering. Please try again later.';
            //echo mysql_error(); //debugging purposes, uncomment when needed
        }
        else
        {
            echo 'Successfully registered. You can now <a href="signin.php">sign in</a> and start posting! :-)';
        }
    }
}
 
include 'footer.php';
?>

{% endhighlight %}

العديد من التوضيحات ستجدها في التعليقات الموضوعة ضمن الكود، لذا تأكد من قراءتها. معالجة البيانات تتم على ثلاثة مراحل:

## التأكد من البيانات

اذا لم تكن البيانات صحيحة ومعبئة بشكل كامل، اعرض النموذج مرة أخرى.
اذا كانت جميع البيانات صحيحة ومعبئة، احفظ البيانات في قاعدة البيانات.

(ماذا تقصد بالتأكد من صحة البيانات اذا كانت البيانات تُدخل ﻷول مرة؟ أقصد بذلك أن هناك حقل مثلاً ليضع المستخدم بريده الإلكتروني، يتم تعريف هذا الحقل بلغة `html` على أنه بريد إلكتروني، يجب أن يحوي على `@` و نقطة ثم كوم أو نت أو أياً كان، إذا لم تكن البيانات المدخلة في هذا الحقل بالشكل المذكور، فالمستخدم في الواقع لم يدخل بريد إلكتروني فعلاً، وهناك بالتالي بيانات غير صحيحة في النموذج)

الجزء المتعلق بـ php على كل حال يشرح نفسه بنفسه، يبقى تعليمات SQL التي تحتاج بعض الشرح.

{% highlight sql %}

INSERT INTO
       users(user_name, user_pass, user_email ,user_date, user_level)
VALUES('" . mysql_real_escape_string($_POST['user_name']) . "',
       '" . sha1($_POST['user_pass']) . "',
       '" . mysql_real_escape_string($_POST['user_email']) . "',
       NOW(), 
       0);

{% endhighlight %} 

في السطر الأول لدينا عبارة `INSERT INTO` التي تستخدم لإضافة بيانات لقاعدة البيانات، وتم تحديد اسم الجدول في السطر الثاني. الكلمات التي بين قوسين تحدد أسماء الأعمدة التي نريد إدراج البيانات لها. عبارة VALUES تُخبر قاعدة البيانات أننا انتهينا من تحديد أسماء الأعمدة وجاء وقت تحديد القيم التي ستُضاف لهذه الأعمدة. ولدينا شيئ جديد هنا: `mysql_real_escape_string`. تستخدم هذه التعليمة لحماية بيانات المستخدم أثناء إرساله للنموذج، ويجب أن تُستخدم دائماً باستثاء بعض الحالات النادرة. السكريبتات التي لا تستخدم هذه التعليمة يكون اختراقها والوصول لبيانات النموذج المرسلة سهل جداً، فلا تخاطر بذلك واستخدم عبارة `mysql_real_escape_string()`.

> إيّاك أن تُدرج كلمة السر في قاعدة البيانات كما هي. يجب عليك دائماً تشفيرها.

كما رأيت ، لقد قمنا باستخدام عبارة `sha1()` لتشفير كلمة سر المستخدم قبل حفظها في قاعدة البيانات، تذكر دائماً عمل هذه الخطوة في كل نموذج تقوم بعمله ويحوي على كلمة سر. فلو فرضنا أن أحد المخترقين قام بالوصول لقاعدة البيانات، وكانت كلمات السر غير مشفرة، فسيصبح بإمكانه الولوج لحساب أي مستخدم أو أي مدير في المنتدى وعمل ما يحلو له، أما لو كانت كلمات السر مشفرة فلن يتمكن من فعل ذلك قبل أن يفك تشفيرهم، وهذا مستحيل تقريباً .

> من الممكن استخدام أي نوع تشفير آخر بدلاً من `sha1()` ، مثل `md5()` . أنا استخدم النوع `sha1()` ﻷن المقاييس أثبتت أن هذا النوع أسرع بقليل.

اذا نجحت عملية الاشتراك فستحصل على التالي 

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-3](/assets/3.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-3")

قم بتحديث صفحة قاعدة البيانات في phpMyAdmin ، يجب أن ترى تسجيلاً جديداً في جدول المستخدمين users

# سادساً: إضافة التفعيل ومستوى المستخدم

إن من المزايا الهامة في المنتدى هو الفرق بين المستخدم العادي والمدير/المشرف. وبما أننا نناقش هنا منتجى صغير وبسيط وأن إضافة مزايا سيأخذ وقتاً طويلاً، فسنركز هنا على عملية تسجيل الدخول وإضافة بعض المزايا للمدراء مثل إضافة تصنيفات جديدة وإغلاق نقاش.

والآن بعد إكمال الخطوة السابقة، سنقوم بجعل الحساب الذي أنشأته للتو حساب مدير. اذهب لـ phpMyAdmin واضغط على جدول المستخدمين users ثم اضغط على خيار Browse . سيظهر لك الحساب الذي أنشأته، اضغط على أيقونة التعديل edit وقم بتغيير قيمة الحقل `user_level` من 0 إلى 1 . 

حالياً لن تلاحظ أي فرق في المنتدى، ولكن عندما نضيف مزايا المدير سيصبح هناك فروقات في الصلاحيات بين الحساب العادي وهذا الحساب.

**عملية تسجيل الدخول تعمل كالتالي:**

* يقوم الزائر بإدخال بيانات المستخدم ويرسل النموذج.

* إذا كان اسم المستخدم وكلمة السر المدخلين صحيحين، فيمكن الآن بدء الجلسة (session)
اذا كان اسم المستخدم أو كلمة المرور غير صحيحين، نقوم بإظهار النموذج مرة أخرى مع رسالة خطأ.

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-4](/assets/6.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-4")

بالأسفل ملف تسجيل الدخول signin.php . اطلع على التعليقات ضمن الكود لفهم ما يجري

{% highlight php %}

<?php
//signin.php
include 'connect.php';
include 'header.php';
 
echo '<h3>Sign in</h3>';
 
//first, check if the user is already signed in. If that is the case, there is no need to display this page
if(isset($_SESSION['signed_in']) && $_SESSION['signed_in'] == true)
{
    echo 'You are already signed in, you can <a href="signout.php">sign out</a> if you want.';
}
else
{
    if($_SERVER['REQUEST_METHOD'] != 'POST')
    {
        /*the form hasn't been posted yet, display it
          note that the action="" will cause the form to post to the same page it is on */
        echo '<form method="post" action="">
            Username: <input type="text" name="user_name" />
            Password: <input type="password" name="user_pass">
            <input type="submit" value="Sign in" />
         </form>';
    }
    else
    {
        /* so, the form has been posted, we'll process the data in three steps:
            1.  Check the data
            2.  Let the user refill the wrong fields (if necessary)
            3.  Varify if the data is correct and return the correct response
        */
        $errors = array(); /* declare the array for later use */
         
        if(!isset($_POST['user_name']))
        {
            $errors[] = 'The username field must not be empty.';
        }
         
        if(!isset($_POST['user_pass']))
        {
            $errors[] = 'The password field must not be empty.';
        }
         
        if(!empty($errors)) /*check for an empty array, if there are errors, they're in this array (note the ! operator)*/
        {
            echo 'Uh-oh.. a couple of fields are not filled in correctly..';
            echo '<ul>';
            foreach($errors as $key => $value) /* walk through the array so all the errors get displayed */
            {
                echo '<li>' . $value . '</li>'; /* this generates a nice error list */
            }
            echo '</ul>';
        }
        else
        {
            //the form has been posted without errors, so save it
            //notice the use of mysql_real_escape_string, keep everything safe!
            //also notice the sha1 function which hashes the password
            $sql = "SELECT 
                        user_id,
                        user_name,
                        user_level
                    FROM
                        users
                    WHERE
                        user_name = '" . mysql_real_escape_string($_POST['user_name']) . "'
                    AND
                        user_pass = '" . sha1($_POST['user_pass']) . "'";
                         
            $result = mysql_query($sql);
            if(!$result)
            {
                //something went wrong, display the error
                echo 'Something went wrong while signing in. Please try again later.';
                //echo mysql_error(); //debugging purposes, uncomment when needed
            }
            else
            {
                //the query was successfully executed, there are 2 possibilities
                //1. the query returned data, the user can be signed in
                //2. the query returned an empty result set, the credentials were wrong
                if(mysql_num_rows($result) == 0)
                {
                    echo 'You have supplied a wrong user/password combination. Please try again.';
                }
                else
                {
                    //set the $_SESSION['signed_in'] variable to TRUE
                    $_SESSION['signed_in'] = true;
                     
                    //we also put the user_id and user_name values in the $_SESSION, so we can use it at various pages
                    while($row = mysql_fetch_assoc($result))
                    {
                        $_SESSION['user_id']    = $row['user_id'];
                        $_SESSION['user_name']  = $row['user_name'];
                        $_SESSION['user_level'] = $row['user_level'];
                    }
                     
                    echo 'Welcome, ' . $_SESSION['user_name'] . '. <a href="index.php">Proceed to the forum overview</a>.';
                }
            }
        }
    }
}
 
include 'footer.php';
?>

{% endhighlight %} 

**تحديث**: إذا كنت تستخدم الإصدارات الحديثة وبالتالي mysqli استخدم الكود التالي بدلأ من الكود أعلاه

{% highlight php %}


<?php
//signin.php
include 'connect.php';
include 'header.php';
 
echo '<h3>Sign in</h3>';
 
//first, check if the user is already signed in. If that is the case, there is no need to display this page
if(isset($_SESSION['signed_in']) && $_SESSION['signed_in'] == true)
{
    echo 'You are already signed in, you can <a href="signout.php">sign out</a> if you want.';
}
else
{
    if($_SERVER['REQUEST_METHOD'] != 'POST')
    {
        /*the form hasn't been posted yet, display it
          note that the action="" will cause the form to post to the same page it is on */
        echo '<form method="post" action="">
            Username: <input type="text" name="user_name" />
            Password: <input type="password" name="user_pass">
            <input type="submit" value="Sign in" />
         </form>';
    }
    else
    {
        /* so, the form has been posted, we'll process the data in three steps:
            1.  Check the data
            2.  Let the user refill the wrong fields (if necessary)
            3.  Varify if the data is correct and return the correct response
        */
        $errors = array(); /* declare the array for later use */
         
        if(!isset($_POST['user_name']))
        {
            $errors[] = 'The username field must not be empty.';
        }
         
        if(!isset($_POST['user_pass']))
        {
            $errors[] = 'The password field must not be empty.';
        }
         
        if(!empty($errors)) /*check for an empty array, if there are errors, they're in this array (note the ! operator)*/
        {
            echo 'Uh-oh.. a couple of fields are not filled in correctly..';
            echo '<ul>';
            foreach($errors as $key => $value) /* walk through the array so all the errors get displayed */
            {
                echo '<li>' . $value . '</li>'; /* this generates a nice error list */
            }
            echo '</ul>';
        }
        else
        {
            //the form has been posted without errors, so save it
            //notice the use of mysql_real_escape_string, keep everything safe!
            //also notice the sha1 function which hashes the password
$conn = mysqli_connect("localhost","root","Stccpe+2009","php");
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }  
            $sql = "SELECT 
                        user_id,
                        user_name,
                        user_level
                    FROM
                        users
                    WHERE
                        user_name = '" . mysqli_real_escape_string($conn, $_POST['user_name']) . "'
                    AND
                        user_pass = '" . sha1($_POST['user_pass']) . "'";
                         
            $result = mysqli_query($conn, $sql);
            if(!$result)
            {
                //something went wrong, display the error
                echo 'Something went wrong while signing in. Please try again later.';
                //echo mysql_error(); //debugging purposes, uncomment when needed
            }
            else
            {
                //the query was successfully executed, there are 2 possibilities
                //1. the query returned data, the user can be signed in
                //2. the query returned an empty result set, the credentials were wrong
                if(mysqli_num_rows($result) == 0)
                {
                    echo 'You have supplied a wrong user/password combination. Please try again.';
                }
                else
                {
                    //set the $_SESSION['signed_in'] variable to TRUE
                    $_SESSION['signed_in'] = true;
                     
                    //we also put the user_id and user_name values in the $_SESSION, so we can use it at various pages
                    while($row = mysqli_fetch_assoc($result))
                    {
                        $_SESSION['user_id']    = $row['user_id'];
                        $_SESSION['user_name']  = $row['user_name'];
                        $_SESSION['user_level'] = $row['user_level'];
                    }
                     
                    echo 'Welcome, ' . $_SESSION['user_name'] . '. <a href="index.php">Proceed to the forum overview</a>.';
                }
            }
        }
    }
}
 
include 'footer.php';
?>

{% endhighlight %}

كما لاحظت، هذه هي تعليمات SQL في الكود السابق

{% highlight sql %}

SELECT
    user_id,
    user_name,
    user_level
FROM
    users
WHERE
    user_name = '" . mysql_real_escape_string($_POST['user_name']) . "'
AND
    user_pass = '" . sha1($_POST['user_pass'])

{% endhighlight %} 

من الواضح أننا نقوم بالتأكد من البيانات المدخلة إذا كانت لمستخدم موجود بالفعل. هناك العديد من السكريبتات التي تستخرج كلمة السر من قاعدة البيانات وتقارنها مع تلك المدخلة في النموذج باستخدام php. ولكن القيام بذلك بواسطة تعليمات SQL مباشرة سيجعل العملية أكثر أمناً حيث أن العملية هذه تحصل في وسط قاعدة البيانات وليس ضمن تطبيقنا الوب (منتدانا).

إذا قام المستخدم بتسجيل الدخول بشكل صحيح، فسنقوم بعمل بضعة أشياء:

{% highlight php %}

<?php
//set the $_SESSION['signed_in'] variable to TRUE
$_SESSION['signed_in'] = true;
//we also put the user_id and user_name values in the $_SESSION, so we can use it at various pages
while($row = mysql_fetch_assoc($result))
{
    $_SESSION['user_id'] = $row['user_id'];
    $_SESSION['user_name'] = $row['user_name']; 
}
?>

{% endhighlight %} 

في البداية، قمنا بإعطاء المتغير `$_SESSION['signed_in']`  القيمة `true` أي أننا بدأنا الجلسة والمستخدم الآن مسجل الدخول. وسنقوم باستخدام هذا المتغير في صفحات أخرى للتأكد من أن المستخدم مسجل الدخول. أيضاً قمنا بوضع اسم المستخدم `username` ومعرفه `user_id` في المتغير `$_SESSION` للاستخدام في صفحات أخرى. أخيراً، سنقوم بعرض رابط لرئيسية المنتدى حيث يمكن للمستخدم البدء في الإبحار.

تسجيل الدخول بالطبع يتطلب وظيفة أخرى وهي تسجيل الخروج! في الواقع عملية تسجيل الخروج أسهل بكثير من عملية تسجيل الدخول، فبما أن جميع المعلومات مخزنة في متغيرات `$_SESSION` ، فكل ما علينا فعله هو إلغاء تعيينهم في هذا المتغير وعرض رسالة للمستخدم.

الآن قمنا بضبط متغيرات `$_SESSION` ، يمكننا تحديد اذا كان شخص ما مسجل الدخول. دعنا نقوم الآن بعمل تغيير أخير على ملف الترويسة header.php
قم باستبدال التالي في الملف:

{% highlight php %}

<div id="userbar">Hello Example. Not you? Log out.</div>

{% endhighlight %} 

إلى :

{% highlight php %}


<div id="userbar">
<?php
    session_start();
    if(isset($_SESSION['signed_in']))
    {
        echo 'Hello' . $_SESSION['user_name'] . '. Not you? <a href="signout.php">Sign out</a>';
    }
    else
    {
        echo '<a href="signin.php">Sign in</a> or <a href="signup.php">create an account</a>.';
    }
?>
</div>

{% endhighlight %} 

وبالتالي، إذا قام المستخدم بتسجيل الدخول، فسيرى اسمه معروض في بداية الصفحة مع رابط لصفحة تسجيل الخروج.

نجحت طريقة التفعيل! والآن يبدو منتدانا كالتالي :

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-5](/assets/4.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-5")

# سابعاً: إنشاء تصنيف

نحن نريد إنشاء تصانيف في المنتدى، لذا دعنا ننشئ نموذج لهذه العملية

{% highlight html %}

<form method="post" action="">
    Category name: <input type="text" name="cat_name" />
    Category description: <textarea name="cat_description" /></textarea>
    <input type="submit" value="Add category" />
 </form>

{% endhighlight %} 

تبدو هذه الخطوة مثل الخطوة الرابعة (اشتراك مستخدم). لذا لن أقوم بالشرح هنا ، فبما أنك متابع للخطوات فستكون قادراً على فهم الأمور بشكل سريع.

سنقوم تضمين النموذج في الأعلى ضمن صفحة إنشاء تصنيف :

{% highlight php %}

<?php
//create_cat.php
include 'connect.php';
 
if($_SERVER['REQUEST_METHOD'] != 'POST')
{
    //the form hasn't been posted yet, display it
    echo '<form method='post' action=''>
        Category name: <input type='text' name='cat_name' />
        Category description: <textarea name='cat_description' /></textarea>
        <input type='submit' value='Add category' />
     </form>'
}
else
{
    //the form has been posted, so save it
    $sql = ìINSERT INTO categories(cat_name, cat_description)
       VALUES('' . mysql_real_escape_string($_POST['cat_name']) . ì',
             '' . mysql_real_escape_string($_POST['cat_description']) . ì')';
    $result = mysql_query($sql);
    if(!$result)
    {
        //something went wrong, display the error
        echo 'Error' . mysql_error();
    }
    else
    {
        echo 'New category successfully added.';
    }
}
?>

{% endhighlight %} 

وكما ترى، لقد بدأنا السكريبت بفحص السيرفر $_SERVER ، بعد التأكد من أن المستخدم لديه صلاحيات المدير، والمطلوبة لإنشاء تصنيف، يتم عرض النموذج إذا لم يتم تعبئته وإرساله سابقاً، وإذا تم إرساله، يتم حفظ القيم. مرة أخرى ، يتم تحضير تعليمة SQL وتنفيذها.

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-6](/assets/5.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-6")

# ثامناً: إضافة تصنيفات للصفحة الرئيسية index.php

لقد قمنا بإنشاء بعض التصنيفات، ويمكننا الآن عرضهم في الصفحة الرئيسية. دعنا نضيف تعليمة SQL التالية لمنظقة المحتوى في الصفحة الرئيسية index.php

{% highlight sql %}

SELECT
    categories.cat_id,
    categories.cat_name,
    categories.cat_description,
FROM
    categories

{% endhighlight %} 

تقوم هذه التعليمة بتحديد جميع التصنيفات وأسمائهم ووصفهم من جدول التصنيفات. سنحتاج الآن لبضعة أسطر php لعرض النتائج. إذا قمنا بإضافة التعليمة كما فعلنا في الخطوات السابقة، فسيبدو الكود (الكود النهائي للصفحة الرئيسية index.php) على الشكل:

{% highlight php %}

<?php
//index.php
include 'connect.php';
include 'header.php';
 
$sql = "SELECT
            cat_id,
            cat_name,
            cat_description,
        FROM
            categories";
 
$result = mysql_query($sql);
 
if(!$result)
{
    echo 'The categories could not be displayed, please try again later.';
}
else
{
    if(mysql_num_rows($result) == 0)
    {
        echo 'No categories defined yet.';
    }
    else
    {
        //prepare the table
        echo '<table border="1">
              <tr>
                <th>Category</th>
                <th>Last topic</th>
              </tr>'; 
             
        while($row = mysql_fetch_assoc($result))
        {               
            echo '<tr>';
                echo '<td class="leftpart">';
                    echo '<h3><a href="category.php?id">' . $row['cat_name'] . '</a></h3>' . $row['cat_description'];
                echo '</td>';
                echo '<td class="rightpart">';
                            echo '<a href="topic.php?id=">Topic subject</a> at 10-10';
                echo '</td>';
            echo '</tr>';
        }
    }
}
 
include 'footer.php';
?>

{% endhighlight %} 

**تحديث**: لـ php7 واستخدام mysqli، يرجى استبدال السطر التالي الموجود في بداية الكود $result = mysql_query($sql); إلى:

{% highlight php %}

$conn = mysqli_connect("localhost","root","password","DatabaseName");
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
$result = mysqli_query($conn, $sql);

{% endhighlight %} 

لاحظ كيف استخدمنا حقل cat_id لإنشاء روابط لصفحة category.php . جميع الروابط لهذه السفحة ستبدو على الشكل:

		category.php?cat_id=x

حيث x يمكن أن يكون أي قيمة عددية بحسب التصنيف .

# تاسعاً: إنشاء موضوع

سنقوم في هذه الخطوة بجمع التقنيات التي تعلمناها في الخطوات السابقة. حيث سنقوم بالتأكد من أن المستخدم مسجل الدخول، سنقوم باستخدام تعليمة SQL لإنشاء موضوع ، وسننشئ نموذج html بسيط كواجهة مستخدم لإنشاء الموضوع.

إن هيكلية ملف إنشاء الموضوع create_topic.php من الصعب شرحها ضمن قائمة أو ما شابه، لذا قمت بكتابة شرح للهيكل العام للملف كتوضيح:

{% highlight php %}

<?php
if(user is signed in)
{
    //the user is not signed in
}
else
{
    //the user is signed in
    if(form has not been posted)
    {
        //show form
    }
    else
    {
        //process form
    }
}
?>

{% endhighlight %} 
وهذا هو الكود الحقيقي لهذا القسم من المنتدى ، راجع الشرح أسفل الكود لفهم ما يجري .

{% highlight php %}

<?php
//create_topic.php
include 'connect.php';
include 'header.php';
 
echo '<h2>Create a topic</h2>';
if($_SESSION['signed_in'] == false)
{
    //the user is not signed in
    echo 'Sorry, you have to be <a href="/forum/signin.php">signed in</a> to create a topic.';
}
else
{
    //the user is signed in
    if($_SERVER['REQUEST_METHOD'] != 'POST')
    {
        //the form hasn't been posted yet, display it
        //retrieve the categories from the database for use in the dropdown
        $sql = "SELECT
                    cat_id,
                    cat_name,
                    cat_description
                FROM
                    categories";
         
        $result = mysql_query($sql);
         
        if(!$result)
        {
            //the query failed, uh-oh :-(
            echo 'Error while selecting from database. Please try again later.';
        }
        else
        {
            if(mysql_num_rows($result) == 0)
            {
                //there are no categories, so a topic can't be posted
                if($_SESSION['user_level'] == 1)
                {
                    echo 'You have not created categories yet.';
                }
                else
                {
                    echo 'Before you can post a topic, you must wait for an admin to create some categories.';
                }
            }
            else
            {
         
                echo '<form method="post" action="">
                    Subject: <input type="text" name="topic_subject" />
                    Category:'; 
                 
                echo '<select name="topic_cat">';
                    while($row = mysql_fetch_assoc($result))
                    {
                        echo '<option value="' . $row['cat_id'] . '">' . $row['cat_name'] . '</option>';
                    }
                echo '</select>'; 
                     
                echo 'Message: <textarea name="post_content" /></textarea>
                    <input type="submit" value="Create topic" />
                 </form>';
            }
        }
    }
    else
    {
        //start the transaction
        $query  = "BEGIN WORK;";
        $result = mysql_query($query);
         
        if(!$result)
        {
            //Damn! the query failed, quit
            echo 'An error occured while creating your topic. Please try again later.';
        }
        else
        {
     
            //the form has been posted, so save it
            //insert the topic into the topics table first, then we'll save the post into the posts table
            $sql = "INSERT INTO 
                        topics(topic_subject,
                               topic_date,
                               topic_cat,
                               topic_by)
                   VALUES('" . mysql_real_escape_string($_POST['topic_subject']) . "',
                               NOW(),
                               " . mysql_real_escape_string($_POST['topic_cat']) . ",
                               " . $_SESSION['user_id'] . "
                               )";
                      
            $result = mysql_query($sql);
            if(!$result)
            {
                //something went wrong, display the error
                echo 'An error occured while inserting your data. Please try again later.' . mysql_error();
                $sql = "ROLLBACK;";
                $result = mysql_query($sql);
            }
            else
            {
                //the first query worked, now start the second, posts query
                //retrieve the id of the freshly created topic for usage in the posts query
                $topicid = mysql_insert_id();
                 
                $sql = "INSERT INTO
                            posts(post_content,
                                  post_date,
                                  post_topic,
                                  post_by)
                        VALUES
                            ('" . mysql_real_escape_string($_POST['post_content']) . "',
                                  NOW(),
                                  " . $topicid . ",
                                  " . $_SESSION['user_id'] . "
                            )";
                $result = mysql_query($sql);
                 
                if(!$result)
                {
                    //something went wrong, display the error
                    echo 'An error occured while inserting your post. Please try again later.' . mysql_error();
                    $sql = "ROLLBACK;";
                    $result = mysql_query($sql);
                }
                else
                {
                    $sql = "COMMIT;";
                    $result = mysql_query($sql);
                     
                    //after a lot of work, the query succeeded!
                    echo 'You have successfully created <a href="topic.php?id='. $topicid . '">your new topic</a>.';
                }
            }
        }
    }
}
 
include 'footer.php';
?>

{% endhighlight %} 

سأناقش هذه الصفحة على قسمين: عرض النموذج ومعالجة النموذج.

## عرض النموذج

لعرض النموذج فإننا نبدأ بتعليمات html بسيطة، ولكن في الواقع هناك شيئ خاص، ﻷننا نستخدم قائمة منسدلة، هذه القائمة المنسدلة يتم تعبئتها من خلال بيانات موجودة في قاعدة البيانات، يتم استخراج تلك البيانات باستخدام تعليمات SQL :

{% highlight sql %}

SELECT
    cat_id,
    cat_name,
    cat_description
FROM
    categories

{% endhighlight %} 

أعتقد أن هذا هو الجزء الغير واضح هنا، والآن كما ترى هو مجرد كود بسيط .

## معالجة النموذج

عملية حفظ الموضوع تتضمن مرحلتين: حفظ الموضوع في جدول المواضيع ضمن قاعدة البيانات، وحفظ أول تعليق في جدول التعليقات. وهذا يتطلب شيئ متقدم نوعاً ما وخارج موضوعنا هنا تقريباً، وهو يدعى إجراء `transaction` ، ويُقصد به أننا نبدأ بتنفيذ أمر البدء ثم التراجع إذا كان هناك أخطاء في قاعدة البيانات أو إنهاء التنفيذ عندما يجري كل شيئ بشكل صحيح.

{% highlight php %}

<?php
//start the transaction
$query  = "BEGIN WORK;";
$result = mysql_query($query);
//stop the transaction
$sql = "ROLLBACK;";
$result = mysql_query($sql);
//commit the transaction
$sql = "COMMIT;";
$result = mysql_query($sql);
?>

{% endhighlight %} 

أول تعليمة تستخدم لحفظ ابيانات هو تعليمة إنشاء موضوع، والتي تبدو على الشكل التالي :

{% highlight sql %}

INSERT INTO
    topics(topic_subject,
               topic_date,
               topic_cat,
               topic_by)
VALUES('" . mysql_real_escape_string($_POST['topic_subject']) . "',
       NOW(),
       " . mysql_real_escape_string($_POST['topic_cat']) . ",
       " . $_SESSION['user_id'] . ")

{% endhighlight %} 

في البداية تم تعريف الحقول، ثم القيم ليتم إدراجها في الحقول. لقد رأيت مثل هذه التعليمات سابقاً، حيث أنها مجرد تعليمات يتم تأمينها استخدام العبارة `musql_real_escape_string()` . القيمة الثانية : `NOW()` هي وظيفة في `SQL` لإدارج الوقت الحالي. القيمة الثالثة هي التي لم ترها من قبل، وهي تشير إلى معرف id صالح لتصنيف ما. والقيمة الأخيرة تشير لمعرف id مستخدم موجود بالفعل، وهو في حالتنا هي قيمة المتغير `$_SESSION['user_id']`.  خيث تم مناقشة هذا المتغير خلال خطوة تسجيل الدخول .

إذا تم تنفيذ الكود بدون أخطاء، فيتم الانتقال للخطوة التالية. تذكر أننا ما زالنا نجري إجراءاً هنا `transaction` . إذا حصلنا على أخطاء فسنستخدم تعليمة `ROLLBACK`.

{% highlight sql %}

INSERT INTO
        posts(post_content,
        post_date,
        post_topic,
        post_by)
VALUES
        ('" . mysql_real_escape_string($_POST['post_content']) . "',
         NOW(),
         " . $topicid . ",
         " . $_SESSION['user_id'] . ")

{% endhighlight %} 

إن أول شيئ نفعله هنا هو استخدام تعليمة `mysql_insert_id()` للحصول على آخر id تم توليده من حقل `topic_id` في جدول المواضيع. وكما وجدت في الخطوات الأولى، يتم توليد الـ `id` في قاعدة البيانات باستخدام تعليمة `auto_increment`.

ثم يتم إدراج المنشور في جدول المنشورات post table. تبدو هذه العملية مشابهة لعملية المواضيع، الفرق الوحيد بينهما هو أن المنشور يشير إلى الموضوع والموضوع يشير للتصنيف. لقد قررنا من البداية إنشاء تصميم بيانات جيد، وهذه هي النتيجة.

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-7](/assets/7.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-7")

# عاشراً : عرض التصنيفات

سوف نقوم بعمل صفحة عرض لتصنيف محدد. لقد أنشأنا تصنيفاً للتو ، ومن المفضل توفير إمكانية مشاهدة جميع المواضيع التي تتبع لهذا التصنيف. أولاً قم بإنشاء صفحة باسم category.php

**نحتاج هنا لعدة أمور:**

1.أمور نحتاجها لعرض التصنيف:

* `cat_name` (اسم التصنيف)

* `cat_description` (وصف التصنيف)

2.أمور نحتاجها لعرض المواضيع ضمن ذلك التصنيف:

* `topic_id`   (معرف الموضوع)

* `topic_subject`  (عنوان الموضوع)

* `topic_date`  (تاريخ الموضوع)

* `topic_cat`   (تصنيف الموضوع)

لنقم الآن بإنشاء تعليمتي SQL والتي تقوم باستخراج البيانات الني نريدها تحديداً من قاعدة البيانات

{% highlight sql %}

SELECT
    cat_id,
    cat_name,
    cat_description
FROM
    categories
WHERE
    cat_id = " . mysql_real_escape_string($_GET['id'])

{% endhighlight %} 

تقوم التعليمة أعلاه باستخراج جميع التصنيفات من قاعدة البيانات

{% highlight sql %}

SELECT 
    topic_id,
    topic_subject,
    topic_date,
    topic_cat
FROM
    topics
WHERE
    topic_cat = " . mysql_real_escape_string($_GET['id'])

{% endhighlight %} 

والآن ، الكود الكامل لملف category.php سيكون على الشكل التالي

{% highlight php %}

<?php
//category.php
include 'connect.php';
include 'header.php';
 
//first select the category based on $_GET['cat_id']
$sql = "SELECT
            cat_id,
            cat_name,
            cat_description
        FROM
            categories
        WHERE
            cat_id = " . mysql_real_escape_string($_GET['id']);
 
$result = mysql_query($sql);
 
if(!$result)
{
    echo 'The category could not be displayed, please try again later.' . mysql_error();
}
else
{
    if(mysql_num_rows($result) == 0)
    {
        echo 'This category does not exist.';
    }
    else
    {
        //display category data
        while($row = mysql_fetch_assoc($result))
        {
            echo '<h2>Topics in ′' . $row['cat_name'] . '′ category</h2>';
        }
     
        //do a query for the topics
        $sql = "SELECT  
                    topic_id,
                    topic_subject,
                    topic_date,
                    topic_cat
                FROM
                    topics
                WHERE
                    topic_cat = " . mysql_real_escape_string($_GET['id']);
         
        $result = mysql_query($sql);
         
        if(!$result)
        {
            echo 'The topics could not be displayed, please try again later.';
        }
        else
        {
            if(mysql_num_rows($result) == 0)
            {
                echo 'There are no topics in this category yet.';
            }
            else
            {
                //prepare the table
                echo '<table border="1">
                      <tr>
                        <th>Topic</th>
                        <th>Created at</th>
                      </tr>'; 
                     
                while($row = mysql_fetch_assoc($result))
                {               
                    echo '<tr>';
                        echo '<td class="leftpart">';
                            echo '<h3><a href="topic.php?id=' . $row['topic_id'] . '">' . $row['topic_subject'] . '</a><h3>';
                        echo '</td>';
                        echo '<td class="rightpart">';
                            echo date('d-m-Y', strtotime($row['topic_date']));
                        echo '</td>';
                    echo '</tr>';
                }
            }
        }
    }
}
 
include 'footer.php';
?>

{% endhighlight %} 

وهذه هي النتيجة النهائية لصفحة التصنيفات

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-8](/assets/8.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-8")

# الخطوة 11 : عرض المواضيع

إن تعليمات SQL في هذه الخطوة هي تعليمات معقدة. بالنسبة لكود php فسيكون كله مألوفاً لديك وشبيه بما سبق. لذا دعنا نلقي نظرة الآن على تعليمات SQL . حيث التعليمة الأولى تستخرج معلومات أساسية حول الموضوع:

{% highlight sql %}

SELECT
topic_id,
topic_subject
FROM
topics
WHERE
topics.topic_id = " . mysql_real_escape_string($_GET[
'id'])

{% endhighlight %} 

يتم عرض هذه المعلومات في رأس الجدول الذي سنستخدمه لعرض جميع البيانات. ثم سنستخرج جميع التعليقات على هذا الموضوع من قاعدة البيانات. التعليمة التالية تعطينا تماماً ما نريد:

{% highlight sql %}

SELECT
posts.post_topic,
posts.post_content,
posts.post_date,
posts.post_by,
users.user_id,
users.user_name
FROM
posts
LEFT JOIN
users
ON
posts.post_by = users.user_id
WHERE
posts.post_topic = " . mysql_real_escape_string($_GET[
'id'])

{% endhighlight %} 

والآن نريد معلومات من جدول المستخدمين users وجدول التعليقات replies لذا سنستخدم عبارة LEFT JOIN مرة أخرى. حيث يكون الشرط كالتالي: معرف المستخدم user id يجب أن يكون نفسه في حقل reply_by (مؤلف التعليق) . وبهذه الطريقة نستطيع عرض اسم المستخدم للمستخدم الذي قام بإضافة تعليق ما. 

العرض الأخير للمواضيع سيبدو على الشكل :

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-9](/assets/9.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-9")


# الخطوة 12 : إضافة تعليق

والآن دعنا ننهي آخر جزء متبقي لدينا من المنتدى، ألا وهو إمكانية إضافة تعليق. سنبدأ بعمل نموذج للتعليق (بلغة html) :

{% highlight html %}

<form method="post" action="reply.php?id=5">
<textarea name="reply-content"></textarea >
<input type="submit" value="Submit reply" />
</form>

{% endhighlight %} 

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-10](/assets/10.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-10")

وفي النهاية سيكون الكود الكامل لملف reply.php كالتالي:

{% highlight php %}

<?php
//reply.php
include 'connect.php';
include 'header.php';
if($_SERVER['REQUEST_METHOD'] != 'POST')
{
	//someone is calling the file directly, which we don't want
	echo 'This file cannot be called directly.';
}
else
{
	//check for sign in status
	if(!$_SESSION['signed_in'])
	{
		echo 'You must be signed in to post a reply.';
	}
	else
	{
		//a real user posted a real reply
		$sql = "INSERT INTO 
					posts(post_content,
							post_date,
							post_topic,
							post_by) 
				VALUES ('" . $_POST['reply-content'] . "',
						NOW(),
						" . mysql_real_escape_string($_GET['id']) . ",
						" . $_SESSION['user_id'] . ")";
						
		$result = mysql_query($sql);
		if(!$result)
		{
			echo 'Your reply has not been saved, please try again later.';
		}
		else
		{
			echo 'Your reply has been saved, check out <a href="topic.php?id=' . htmlentities($_GET['id']) . '">the topic</a>.';
		}
	}
}
include 'footer.php';
?>

{% endhighlight %}

انظر التعليقات ضمن الكود لفهم ما يجري.



نتأكد أولاً من وجود المستخدم ثم نضيف (ندرج) التعليق لقاعدة البيانات.

![كيفية عمل منتدى باستخدام php و MySQL من الصفر-11](/assets/11.png "كيفية عمل منتدى باستخدام php و MySQL من الصفر-11")

# الخطوة 13: تسجيل الخروج

يتم تسجيل الخروج من خلال الصفحة signout.php بالكود البسيط التالي:

{% highlight sql %}

<?php
// Initialize the session
session_start();
 
// Unset all of the session variables
$_SESSION = array();
 
// Destroy the session.
session_destroy();
 
// Redirect to login page
header("location: signout.php");
exit;
?>

{% endhighlight %} 

# النهاية

الآن وبعد قراءتك لهذا الشرح ستكون لديك المعرفة الكافية لبناء منتدى، أتمنى أن يكون الشرح واضحاً وأنك لم تعترك مع أية مشاكل في طريقك ..

إذا كان هناك أي غموض بالشرح أو واجهتك أي مشكلة فلا تتردد أبداً بمراسلتي أو ترك تعليق في الأسفل
