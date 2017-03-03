---
permalink: /joomla/create-template
layout: post
date: 2016-06-18
title: "إنشاء قوالب Joomla"
hidden: true
comments: true
---

* Toc
{:toc}


# مقدمة


إن هدف هذا الشرح هو إعطاء مقدمة عن إنشاء قوالب Joomla ، حيث سيغطي هذا الشرح الأكواد والملفات الأساسية لإنشاء قالب بسيط ، حيث الأكواد المقدمة هنا يمكنك نسخها ولصقها مع تعديل بسيط فقط .


# إنشاء مجلد القالب


لإنشاء قالب بسيط ، أنشأ مجلد جديد ضمن مجلد templates . وقم بتسمية هذا المجلد باسم القالب الذي تود إنشاؤه ، مثل : mynewtemplate


باستخدام محرر النصوص المفضل لديك قم بإنشاء الملفات index.php و templateDetails.xml ، ولإبقاء الأمور منظمة ، أنشأ مجلدين جديدين باسم images و css ، داخل مجلد css أنشأ ملف وسمه template.css


على الرغم من أنه يمكنك وضع كود css مباشرة ضمن ملف index.php ، ولكن معظم مطوري المواقع يفضلون وضع أكواد css في ملفات منفصلة والتي يمكن استدعاؤها واستخدامها لعدة صفحات باستخدام الوسم link . هذا قد يقلل وقت تحميل صفحاتك ، حيث الملفات المنفصلة يتم وضعها ضمن الملفات المؤقتة في متصفحات المستخدمين .


وهنا ملخص الملفات والمجلدات الأساسية التي يجب إنشاؤها لإنشاء قالب Joomla بسيط :


* mynewtemplate/

* css/

	* template.css

* images/

* index.php

* templateDetails.xml


## إنشاء ملف templateDetails.xml


إن ملف templateDetails.xml أساسي ، وبدونه لن يتم رؤية قالبك من قبل joomla . هذا الملف يحمل مفاتيح metadata عن القالب .


كود الملف يختلف قليلاً حسب إصدار Joomla .


للإصدار 1.5 استخدم التالي :

{% highlight xml %}

    <?xml version="1.0" encoding="utf-8"?>


    <!DOCTYPE install PUBLIC "-//Joomla! 1.5//DTD template 1.0//EN" "http://www.joomla.org/xml/dtd/1.5/template-install.dtd">


    <install version="1.5" type="template">


    <name>mynewtemplate</name>


    <creationDate>2008-05-01</creationDate>


    <author>John Doe</author>


    <authorEmail>john@example.com</authorEmail>


    <authorUrl>http://www.example.com</authorUrl>;


    <copyright>John Doe 2008</copyright>


    <license>GNU/GPL</license>


    <version>1.0.2</version>


    <description>My New Template</description>


    <files>


    <filename>index.php</filename>


    <filename>templateDetails.xml</filename>


    <folder>images</folder>


    <folder>css</folder>


    </files>


    <positions>


    <position>breadcrumb</position>


    <position>left</position>


    <position>right</position>


    <position>top</position>


    <position>user1</position>


    <position>user2</position>


    <position>user3</position>


    <position>user4</position>


    <position>footer</position>


    </positions>


    </install>

{% endhighlight %}

للإصدار 2.5 وما بعد استخدم التالي ، فقط غير version=”2.5” إلى الإصدار الذي تستخدمه من جملة

{% highlight xml %}

    <?xml version="1.0" encoding="utf-8"?>


    <extension version="2.5" type="template">


    <name>mynewtemplate</name>


    <creationDate>2008-05-01</creationDate>


    <author>John Doe</author>


    <authorEmail>john@example.com</authorEmail>


    <authorUrl>http://www.example.com</authorUrl>;


    <copyright>John Doe 2008</copyright>


    <license>GNU/GPL</license>


    <version>1.0.2</version>


    <description>My New Template</description>


    <files>


    <filename>index.php</filename>


    <filename>templateDetails.xml</filename>


    <folder>images</folder>


    <folder>css</folder>


    </files>


    <positions>


    <position>breadcrumb</position>


    <position>left</position>


    <position>right</position>


    <position>top</position>


    <position>user1</position>


    <position>user2</position>


    <position>user3</position>


    <position>user4</position>


    <position>footer</position>


    </positions>


    </extension>

{% endhighlight %}

لذا ، وكما ترى لدينا مجموعة من المعلومات بين الوسوم `<element>` . أفضل ما تقوم به هو نسخ ولصق هذا الكود في ملف templateDetails.xml لديك . وغير قليلاً بعض المعلومات داخل مثلا `<name>` و `<author>` .


قسم `<files>` يجب أن يحتوي على جميع الملفات التي تستخدمها ( على الأغلب لا تعرف أسماءهم بعد ، لا تقلق .. يمكنك تحديث ذلك لاحقاً ) .


عنصر `<folder>` يمكن أن يستخدم لتعريف مجلد بأكلمه مرة واحدة .


أبق ترتيب العناصر كما هي ، فهذا هو الترتيب الشائع والذي يمكنك من الانتقال بسهولة من القالب البسيط .


## إنشاء ملف index.php


(هذا الشرح لإصدارات 2.5 و 3x من Joomla )


ملف index.php أصبح الأساس لكل صفحة تعرض بواسطة Joomla . بشكل أساسي ، أنت تصنع هنا صفحة إنترنت (كأي صفحة HTML ) ولكن ضع كود PHP حيث يجب أن تكون محتويات موقعك . يعمل القالب بإضافة كود Joomla داخل أماكن الوحدات النمطية module والجزء المكون لقالبك . أي شيئ مضاف للقالب سيظهر بجميع الصفحات إلا إذا كان الكود مضاف ﻷحد هذه الأقسام بواسطة Joomla ( أو كود مخصص) .


هذه الصفحة في الأسفل تظهر الكود البدائي والقابل للنسخ واللصق داخل تصميمك الخاص .


### البداية :


قالب جملة يبدأ بالأسطر التالية :

{% highlight php %}

    <?php defined( '_JEXEC' ) or die( 'Restricted access' );?>


    <!DOCTYPE html>


    <html xmlns="http://www.w3.org/1999/xhtml"


    xml:lang="<?php echo $this->language; ?>" lang="<?php echo $this->language; ?>" >

{% endhighlight %}

السطر الأول يمنع المتطفلين من مشاهدة الكود .


السطر الثاني هو تحديد نوع الملف Document Type Declaration (DOCTYPE) ، والذي يخبر المتصفح أي نوع من HTML تستخدمه الصفحة . النوع المستخدم في الأعلى هو HTML5 ، وهو أحدث إصدار من HTML والذي يحوي العديد من المزايا الجديدة .


السطر الثالث يبدأ ملفنا الـ HTML ويصف اللغة التي يستخدمها الموقع . ملف الـ html مقسم لجزأين ، الرأس head والجسم body ، الرأس يحوي معلومات حول الملف والجسم يحوي كود الموقع والذي يتحكم بالتنسيق


### رأس القالب

{% highlight php %}

    <head>


    <jdoc:include type="head" />


    <link rel="stylesheet" href="<?php echo $this->baseurl ?>/templates/system/css/system.css" type="text/css" />


    <link rel="stylesheet" href="<?php echo $this->baseurl ?>/templates/system/css/general.css" type="text/css" />


    <link rel="stylesheet" href="<?php echo $this->baseurl ?>/templates/<?php echo $this->template; ?>/css/template.css" type="text/css" />


    </head>

{% endhighlight %}

### جسم القالب

{% highlight php %}

    <body>


    <jdoc:include type="modules" name="top" />


    <jdoc:include type="component" />


    <jdoc:include type="modules" name="bottom" />


    </body>

{% endhighlight %}

في الحقيقة هذا يكفي ! نعم إنه جسم بدائي جداً ولكنه يفي بالغرض ، كل شيئ آخر سيتم القيام به من قبل Joomla.


### Module Positions



يوجد في الأعلى السطر الذي يحتوي الأمر `name=”top”` والذي يضيف module position يدعى `top` ويتيح لجملة استبدال الوحدات النمطية لهذا القسم من القالب ، الأمر `type=”component”` يحوي جميع المقالات والمحتويات الرئيسية ، وهو هام جداً ، ويتم وضعه في منتصف القالب .



> يمكنك إضافة أسطرك الخاصة في أي مكان تريد في الجسم ، ولكن عليك إضافة أسطر مماثلة في ملف templateDetails.xml والذي يتم تنفيذه جنباً إلى جنب مع ملف index.php في قالبك



### النهاية



أنه قالبك بالوسم


    </html>



## صور مخصصة:



يمكنك إضافة صورك الخاصة في أي مكان في القالب ، وذلك من خلال إضافة السطر التالي

{% highlight php %}

    <img src="<?php echo $this->baseurl; ?>/images/stories/myimage.png" alt="Custom image" class="customImage" />

{% endhighlight %}

فقط قم بتغيير مسار واسم الصورة حسب ما يناسب ..



## CSS مخصص



يمكنك إضافة ستايلك الخاص css كما في التالي

{% highlight php %}

    <link rel="stylesheet" href="<?php echo $this->baseurl ?>/templates/<?php echo $this->template;?>/css/styles.css" type="text/css" />

{% endhighlight %}

كل سطر يتم إضافته يجب أن يكون له سطر مقابل في ملف templateDetails.xml للقالب



فيما يلي الملف النهائي لذلك :

{% highlight php %}

   <?php defined( '_JEXEC' ) or die( 'Restricted access' );?>


    <!DOCTYPE html>


    <html xml:lang="<?php echo $this->language; ?>" lang="<?php echo $this->language; ?>" >


    <head>


    <jdoc:include type="head" />


    <link rel="stylesheet" href="<?php echo $this->baseurl ?>/templates/mynewtemplate/css/template.css" type="text/css" />


    </head>


    <body>


    <jdoc:include type="modules" name="top" />


    <jdoc:include type="component" />


    <jdoc:include type="modules" name="bottom" />


    </body>


    </html>

{% endhighlight %}

# اختبار القالب :



قم بإيجاد القالب في مدير القوالب Template Manager ، اختر قالبك واضغط على Default لجعله القالب الافتراضي



في إصدار جملة 1.5 ستجد القالب مباشرة في مدير القوالب Template Manager والذي يمكن الوصول عبر Extensions > Template Manager



في إصدار جملة 2.5 وما بعد ستحتاج أولاً لإخبار جملة بأن لديك قالب جديد ، هذا الخيار يدعى Discover Extensions ويمكن الوصول له عبر Extensions > Extension Manager > Discover ، عندها اضغط على Discover لاكتشاف القالب ، بعد ذلك اضغط على Install لتنصيبه . الآن يجب أن يظهر القالب في مدير القوالب Template Manager والذي يمكن الوصول إليه عبر Extensions > Template Manager



لاحظ أن يمكنك إنشاء قالبك خارج جملة وتنصيبه بعد ذلك ببساطة كأي إضافة عادية ..



# تحزيم قالب للتنصيب



مجلد يحتوي عدة ملفات مبعثرة ليس طريقة جيدة لعمل حزمة (قالب ، إضافة .. إلخ) . لذا الخطوة الأخيرة هو عمل حزمة . وهي أرشيف مضغوط يحوي المجلد المنشأ وجميع الملفات . يمكن للحزمة أن تكون بلاحقة zip أو tar.gz أو tar.bz2



وأخيراً ، فقد قمت الآن بعمل قالب بسيط ، قد لا يبدو جميلاً جداً ، لذا فعيلك الآن بدء تجربتك مع التنسيق والستايل css .



