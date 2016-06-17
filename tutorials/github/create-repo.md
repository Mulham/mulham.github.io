---
layout: post
date: 2016-06-16
title: سلسلة دروس جِت هَب|إنشاء حزمة
---
 
الفهرس:

[الدرس الأول: التعريف بـ جِت هَب](intro)

الدرس الثاني:إنشاء حزمة في Github

[الدرس الثالث: نسخ حزمة في Github](fork-repo)

[الدرس الرابع: كيف تكون اجتماعياً في Github](being-social)

[الدرس الخامس: كيف تجعل عنوان بريدك الإلكتروني خاصاً في Github](keep-your-email-private)

![](http://3.bp.blogspot.com/-pn6MWxr4MiQ/VCVbcYShIzI/AAAAAAAABe8/X1y4ivuomUI/s1600/create-a-repo-87765eb11840d8b33ef9d1d91b182eed.gif)

* Toc
{:toc}

لوضع مشروعك على Github ، عليك بإنشاء حزمة أولاً لوضع المشروع بداخلها .. لذا دعنا ننشئ واحدة !

في Github يمكنك وضع جميع أنواع المشاريع داخل الحزم. الحزم الشخصية تتبع لحسابات المستخدمين، لذا وبعد اشتراكك بـ [Github](http://github.com) يمكنك إنشاء حزمتك الأولى !


# إنشاء حزمة جديدة في Github

1.في الزاوية أعلى اليمين ﻷي صفحة ، اضغط على العلامة + ثم اختر 
`New repository` أي حزمة جديدة .

![](http://2.bp.blogspot.com/-YFcN71GSJBI/VCVcR1fV0aI/AAAAAAAABfE/i0myMRcwTZ4/s1600/repo-create.png)


2.أنشأ اسم قصير و سهل تذكره لحزمتك .


![](http://4.bp.blogspot.com/-Tz1em5aWHBY/VCVcv6Kta9I/AAAAAAAABfM/CZodjcouJAw/s1600/create-repository-name.png)

3.اختيارياً، أضف وصف لحزمتك . على سبيل المثال  " My first repository on Github" أي حزمتي الأولى في Github


![](http://1.bp.blogspot.com/-42HTcDFLZwo/VCVdTWgqycI/AAAAAAAABfU/cuBP4U8dwEM/s1600/create-repository-desc.png)

4.اختر إما إنشاء حزمة عامة أو خاصة.

![](http://3.bp.blogspot.com/-dkhm1345ihs/VCVdkGnsfuI/AAAAAAAABfc/NX2DNOKClZQ/s1600/create-repository-public-private.png)

  * الحزم العامة خيار رائع للبدء! إنها مجانية ومرئية ﻷي مستخدم على Github ، وبالتالي يمكنك الاستفادة من الشبكة التعاونية لـ Github .

  * الحزم الخاصة تتطلب خطوات بسيطة إضافية للإنشاء. إنها مدفوعة، ومتاحة فقط لك، أي لصاحب الحزمة، بالإضافة للمستخدمين الذين تختارهم أنت لمشاركة الحزمة معهم.


5.اختر `Initialize this repository with a README`.  أي استهلال الحزمة بملف اقرأني (لوضع معلومات عن الحزمة والتعريف بها وبوظيفتها ..) .


![](http://4.bp.blogspot.com/-uUYeB1q7Y7Y/VCVd_KbRJkI/AAAAAAAABfk/WMciVz4rBp0/s1600/create-repository-init-readme.png)

6.اضغط على `Create repository` أي إنشاء الحزمة .


![](http://1.bp.blogspot.com/--gdl4qhKwuM/VCVeMSzkvvI/AAAAAAAABfs/dD5rezbr3m4/s1600/create-repository-button.png)

تهانينا! لقد قمت بإنشاء حزمة جديدة بنجاح واستهلالها بملف "اقرأني" .

# إنشاء التغيير الأول

التغيير  commit ، أو التعديل ، هو تغيير لملف معين أو مجموعة ملفات ، تماماً عند حفظك ﻷي ملف ، باستثناء أنه في Git كل مرة تقوم بحفظ الملف يتم إنشاء معرف محدد ( `SHA` أو `hash` ) والذي يتيح لك الاحتفاظ بتسجيل عن التغييرات التي تمت ومتى ومن قبل من . تحتوي التغييرات عادة على رسالة التغيير والتي هي عبارة عن وصف مختصر  للتغييرات التي تمت على الملف أو مجموعة الملفات .

أي باختصار التغيير هو بمثابة أخذ لقطة سريعة لجميع الملفات في مشروعك عند نقظة زمن محددة .

عند إنشاؤك لحزمتك الأولى ، تستهلها بملف اقرأني `README` ، والذي هو أفضل مكان لتصف مشروعك بتفاصيل أوفى ، أو لإضافة بعض الوثائق مثل كيفية تنصيب واستخدام مشروعك . محتويات ملف اقرأني يظهر تلقائياً بالصفحة الرئيسية لحزمتك .

دعنا الآن ننشأ تغيير على ملف اقرأني :

1.ضمن قائمة الملفات لحزمتك ، اضغط على `README.md`


![](http://4.bp.blogspot.com/-hpxy9PI1sw8/VCVe5yWVLYI/AAAAAAAABf0/U9vvqKGU1go/s1600/create-commit-open-readme.png)

2.أعلى محتويات الملف ، اضغط على أيقونة التعديل (على شكل قلم)


3.ضمن عرض الكود ، اكتب معلومات عن نفسك .

![](http://3.bp.blogspot.com/-0h3-khYlCGE/VCVf-C2EO-I/AAAAAAAABgI/ZNQG7uGgpzE/s1600/edit-readme-light.png)


4.أعلى المحتوى الجديد الذي أدخلته ، اضغط على Preview أي معاينة .


![](http://4.bp.blogspot.com/-WxiOM1Bjokw/VCVgGaCXveI/AAAAAAAABgQ/0c9MyHfujX0/s1600/edit-readme-preview.png)


5.راجع التغييرات التي أجريتها للملف ، حيث ستجد المحتوى الجديد الذي أدخلته باللون الأخضر .


![](http://4.bp.blogspot.com/-PDQlNyJ67Gg/VCVgQ4VsL4I/AAAAAAAABgY/eBpQYiqikZo/s1600/create-commit-review.png)


6.أسفل الصفحة ، و تحت "Commit changes" أدخل رسالة تغيير قصيرة وواضحة تصف التغيير الذي أجريته للملف .


![](http://3.bp.blogspot.com/-EXTc6I2ylu0/VCVgZgiBf-I/AAAAAAAABgg/A9y_6N_Hcw8/s1600/create-commit-commit-changes.png)


7.اضغط على `Commit changes`


تهانينا! بهذا تكون قد أنشأت حزمة على Github تحتوي على ملف اقرأني `README` ، وأجريت تغييرك الأول في Github .

التالي : [نسخ حزمة](fork-repo) 