---
permalink: /github/create-repo
layout: post
date: 2016-06-16
title: سلسلة دروس جِت هَب|إنشاء حزمة
hidden: true
type: tutorial
comments: true
---
 
الفهرس:

[الدرس الأول: التعريف بـ جِت هَب](intro)

الدرس الثاني:إنشاء حزمة في Github

[الدرس الثالث: نسخ حزمة في Github](fork-repo)

[الدرس الرابع: كيف تكون اجتماعياً في Github](being-social)

[الدرس الخامس: كيف تجعل عنوان بريدك الإلكتروني خاصاً في Github](keep-your-email-private)

![](https://help.github.com/assets/images/site/create-a-repo.gif)

* Toc
{:toc}

لوضع مشروعك على Github ، عليك بإنشاء حزمة أولاً لوضع المشروع بداخلها .. لذا دعنا ننشئ واحدة !

في Github يمكنك وضع جميع أنواع المشاريع داخل الحزم. الحزم الشخصية تتبع لحسابات المستخدمين، لذا وبعد اشتراكك بـ [Github](http://github.com) يمكنك إنشاء حزمتك الأولى !


# إنشاء حزمة جديدة في Github

1. في الزاوية أعلى اليمين ﻷي صفحة ، اضغط على العلامة + ثم اختر 
`New repository` أي حزمة جديدة .

	![](https://help.github.com/assets/images/help/repository/repo-create.png)


2. أنشئ اسم قصير و سهل تذكره لحزمتك .


	![](https://help.github.com/assets/images/help/repository/create-repository-name.png0/create-repository-name.png)

3. اختيارياً، أضف وصف لحزمتك . على سبيل المثال  " My first repository on Github" أي حزمتي الأولى في Github


	![](https://help.github.com/assets/images/help/repository/create-repository-desc.png)

4. اختر إما إنشاء حزمة عامة أو خاصة.

	![](https://help.github.com/assets/images/help/repository/create-repository-public-private.png)

	* الحزم العامة خيار رائع للبدء! إنها مجانية ومرئية ﻷي مستخدم على Github ، وبالتالي يمكنك الاستفادة من الشبكة التعاونية لـ Github .

	* الحزم الخاصة تتطلب خطوات بسيطة إضافية للإنشاء. إنها مدفوعة، ومتاحة فقط لك، أي لصاحب الحزمة، بالإضافة للمستخدمين الذين تختارهم أنت لمشاركة الحزمة معهم.


5. اختر `Initialize this repository with a README`.  أي استهلال الحزمة بملف اقرأني (لوضع معلومات عن الحزمة والتعريف بها وبوظيفتها ..) .


	![](https://help.github.com/assets/images/help/repository/create-repository-init-readme.png)

6. اضغط على `Create repository` أي إنشاء الحزمة .


![](https://help.github.com/assets/images/help/repository/create-repository-button.png)

تهانينا! لقد قمت بإنشاء حزمة جديدة بنجاح واستهلالها بملف "اقرأني" .

# إنشاء التغيير الأول

التغيير  commit ، أو التعديل ، هو تغيير لملف معين أو مجموعة ملفات ، تماماً عند حفظك ﻷي ملف ، باستثناء أنه في Git كل مرة تقوم بحفظ الملف يتم إنشاء معرف محدد ( `SHA` أو `hash` ) والذي يتيح لك الاحتفاظ بتسجيل عن التغييرات التي تمت ومتى ومن قبل من . تحتوي التغييرات عادة على رسالة التغيير والتي هي عبارة عن وصف مختصر  للتغييرات التي تمت على الملف أو مجموعة الملفات .

أي باختصار التغيير هو بمثابة أخذ لقطة سريعة لجميع الملفات في مشروعك عند نقظة زمن محددة .

عند إنشاؤك لحزمتك الأولى ، تستهلها بملف اقرأني `README` ، والذي هو أفضل مكان لتصف مشروعك بتفاصيل أوفى ، أو لإضافة بعض الوثائق مثل كيفية تنصيب واستخدام مشروعك . محتويات ملف اقرأني يظهر تلقائياً بالصفحة الرئيسية لحزمتك .

دعنا الآن ننشأ تغيير على ملف اقرأني :

1. ضمن قائمة الملفات لحزمتك ، اضغط على `README.md`


	![](https://help.github.com/assets/images/help/repository/create-commit-open-readme.png)

2. أعلى محتويات الملف ، اضغط على أيقونة التعديل (على شكل قلم)


3. ضمن عرض الكود ، اكتب معلومات عن نفسك .

	![](https://help.github.com/assets/images/help/repository/edit-readme-light.png)


4. أعلى المحتوى الجديد الذي أدخلته ، اضغط على Preview أي معاينة .


	![](https://help.github.com/assets/images/help/repository/edit-readme-preview-changes.png)


5. راجع التغييرات التي أجريتها للملف ، حيث ستجد المحتوى الجديد الذي أدخلته باللون الأخضر .


	![](https://help.github.com/assets/images/help/repository/create-commit-review.png)


6. أسفل الصفحة ، و تحت "Commit changes" أدخل رسالة تغيير قصيرة وواضحة تصف التغيير الذي أجريته للملف .


	![](https://help.github.com/assets/images/help/repository/write-commit-message-quick-pull.png)


7. اضغط على `Commit changes`


تهانينا! بهذا تكون قد أنشأت حزمة على Github تحتوي على ملف اقرأني `README` ، وأجريت تغييرك الأول في Github .

التالي : [نسخ حزمة](fork-repo) 
