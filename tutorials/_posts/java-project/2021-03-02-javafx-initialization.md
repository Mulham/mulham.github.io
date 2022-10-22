---
layout: post
date: 2021-03-02
title: تهيئة بيئة العمل لتطبيق جافا إف إكس
description: تهيئة محرر الكود IntelliJ ومحرر الواجهة Gluon لتطبيق جافا إف إكس
type: tutorial
hidden : true
---

{: .notice} 
هذه الصفحة جزء من شرح [بناء تطبيق جافا إف إكس من الصفر](/java-project-from-scratch)


# تهيئة المحرر

كما هو مذكور فسنعمل على برنامج IntelliJ Edu المجاني، بعد تنصيبه وفتحه قم بالذهاب من الأعلى لقائمة File ثم New ثم Project.

بعدها ستظهر لك نافذة كما في الصورة:

{% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/new-javafx-project.png" alt="تهيئة محرر الكود IntelliJ للعمل على تطبيق جافا إف إكس" %}

1. اختر من القائمة اليسرى خيار Java FX

2. من الأعلى ستجد خيار "Project SDK" من المستحسن أن تعمل على نفس الإصدار الذي أعمل عليه وهو 15 أو مافوق

3. اضغط في النهاية في الأسفل على زر Next


في النافذة التي تليها قم بإعطاء اسم لمشروعك، مثلا "java-project" واضغط في الأسفل على Finish

الآن سيفتح البرنامج على مشروعك الجديد، على اليسار ستجد شجرة الملفات الخاصة بمشروعك، اضغط على السهم بجانب اسم المشروع لعرض الملفات التي بداخله ثم اضغط باليمين على مجلد src واختر New ثم module-Info.java كما في الصورة:

{% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/java-module-info.png" alt="كتابة معلومات تطبيق جافا module info" %}



ثم داخل الملف على اليمين قم بكتابة التالي (مع تغيير الاسم إن لم يكن اسم مشروعك java-project):

        module java.project {
            requires javafx.fxml;
            requires javafx.controls;
            requires javafx.graphics;
            opens sample;
        }

اضغط الآن من الأعلى على قائمة File ثم Project Structure. ستظهر لك نافذة كما في الصورة

{% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/IntelliJ-project-structure.png" alt="إعدادات المشروع في محرر الكود IntelliJ" %}

1. اضغط من القائمة اليسارية على خيار Project

2. تأكد من اختيارك للـ SDK الصحيح في حقل Project SDK

3. من القائمة اليسارية مجددا اضغط على خيار Libraries

4. اضغط على زر + أعلى القائمة الوسطى ثم اختر Java كما في الصورة

{% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/IntelliJ-project-libraries.png" alt="طريقة إضافة مكتبات لبرنامج IntellıJ" %}

بعدها في متصفح الملفات اختر المجلد Javafx-sdk الذي قمت بتحميله (كما وضحت في فقرة المتطلبات) ثم اختر مجلد lib الذي بداخله واضغط على ok. ثم قم بإغلاق النافذة الأصل بالضغط على ok مجددًا.

**ملاحظة:** عند تشغيل الكود الخاص بي ستجد في قسم المكتبات الموضح أعلاه مكتبات مضافة مسبقا، قم بحذفها بالكامل حيث أن مساراتها لن تتوافق لديك، ثم أضف المكتبات الموجودة لديك كما هو مشروح.

الآن من اليمين في الأعلى سترى زر تشغيل أخضر قم بالضغط عليه لتشغيل المشروع، إن ظهرت لك نافذة فارغة باسم "Hello World" فهذا يعني أن كل شيئ على مايرام، أما إن ظهرت أخطاء فقم بالذهاب من الأعلى بجانب زر التشغيل لخيار Main أو أيا كان اسمه ثم Edit Configurations وتأكد من الـ SDK للمشروع أنه مضبوط بشكل صحيح وأن ملف  Main معرف كما في الصورة

{% include image.html layout="responsive" width="400" height="300" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/IntelliJ-run-configurations.png" alt="إعدادات تشغيل تطبيق جافا في برنامج إنتيلي جي" %}


# استخدام محرر واجهة خارجي

محرر الواجهة أو باني المشاهد أو Scene Builder هو التطبيق الذي يتيح لك تصميم نوافذ برنامجك، مثل اختيار الأزرار والحقول وأماكنهم في النافذة وإعطاء كل حقل id مخصص. وهذه العملية ضمن محرر الواجهة تتم بشكل سلس جدا بالسحب والإفلات، فقط قم بسحب الزر أو الحقل أو أي عنصر تريده للمكان الذي ترغب في النافذة.

محررات البرمجة أو مايسمى IDE تأتي غالبا مع محرر واجهة مبني معهم، ولكن محرر الواجهة الافتراضي ذاك مزاياه محدودة والتعامل معه غير سلس تماما، لذلك سنقوم باستخدام محرر واجهة خارجي يدعى Gloun Scene Builder.

بعد تنصيب البرنامج لديك، ضمن المشروع في برنامج IntelliJ اذهب إلى قائمة File ثم Settings، بعد ذلك وكما هو موضح في الصورة:


{% include image.html layout="responsive" width="400" height="300" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/IntelliJ-setting-SceneBuilder.png" alt="الإعدادات في برنامج إنتيلي جي" %}


1. اذهب من القائمة اليسرى لخيار Languages & Frameworks 

2. ثم اضغط على خيار JavaFX 

3. قم بتعريف المسار الصحيح حيث يوجد ملف Gloun Scene Builder القابل للتشغيل (على الويندوز يكون بلاحقة exe)

الآن إذا قمت بالضغط باليمين على أي ملف ينتهي بـ .fxml مثل الملف sample.fxml ثم اخترت Open in SceneBuilder فيجب أن يفتح المشهد ضمن برنامج Gluon.

# إضافة مكتبات لمحرر الواجهة

{: .notice}
هذا القسم من الشرح لن نستخدمه في تطبيقنا ولكنني تركته للاطلاع

ضمن برنامج Gluon ستجد في الأعلى على اليسار حقل للبحث وعلى يمينه أيقونة الإعدادات، اضغط عليها واختر JAR/FXML Manager كما في الصورة

{% include image.html layout="responsive" width="300" height="300" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/Gluon-add-library.png" alt="إضافة مكتبات لمحرر الواجهة جلون Gluon" %}

ثم اختر "Add Library/FXML from file system" كما في الصورة


{% include image.html layout="responsive" width="300" height="300" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/Gluon-jfoenix.png" alt="طريقة إضافة مكتبة لباني المشاهد Gluon" %}

سيظهر لك مستعرض الملفات، حيث يمكنك اختيار المكتبة الخارجية التي قمت بتحميلها وتود إضافتها، لتجدها قد ظهرت على القائمة كما في الصورة أعلاه.


****


**التالي:** [هيكلة المشروع](/java-project-structure)

