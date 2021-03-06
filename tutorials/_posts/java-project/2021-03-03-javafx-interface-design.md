---
layout: post
date: 2021-03-02
title: تصميم الواجهة في تطبيق جافا إف إكس
description: تصميم نوافذ تطبيق جافا إف إكس في محرر الواجهة Gluon
type: tutorial
hidden : true
---

{: .notice} 
هذه الصفحة جزء من شرح [بناء تطبيق جافا إف إكس من الصفر](/java-project-from-scratch)


لنقم الآن بجعل النافذة الأولى للتطبيق هي نافذة تسجيل الدخول.

ضمن تطبيق IntelliJ اضغط على ملف sample.fxml باليمين ثم Refactor ثم Rename واجعل اسمه الجديد login.fxml وبنفس الطريقة غير اسم الملف Controller الموجود ضمن المجلد controller إلى LoginController ولاحظ أننا نكتب أسماء ملفات الجافا بحيث تبدأ بحرف كبير دائمًا.


# تصميم نافذة تسجيل الدخول

اضغط باليمين على الملف login.fxml واختر Open in SceneBuilder

في القائمة Hierarchy أسفل يسار البرنامج ستجد عنصر GridPane اضغط عليه باليمين واختر Delete، ثم في القائمة Container أعلاه اسحب العنصر AnchorPane وافلته في القائمة Hierarchy كما في الصورة:


{% include image.html layout="responsive" width="400" height="300" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/Gluon1.png" alt="شرح برنامج تصميم الواجهة لتطبيق جافا - محرر جلون Gluon 1" %}

بعد ذلك يمكنك تغيير خصائص هذا العنصر الذي سيحتوي باقي العناصر، مثلا يمكن تغيير أبعاده بالذهاب للقائمة Layout على اليمين وتغيير Pref Width من 600 لـ 700 كما في الصورة السابقة.

الآن لنقم بإضافة حقلي اسم المستخدم وكلمة المرور ونضعهم في وسط النافذة، ابحث في مربع البحث (أعلى اليسار) على TextField ثم بمواصلة النقر عليه اسحبه للنافذة التي لدينا في المنتصف، واصل النقر عليه وحركه ضمن النافذة ولاحظ الخطوط الظاهرة لتبين لك منتصف النافذة أفقيا وعموديا، قم بوضع الحقل في المنتصف تمامًا بالنسبة للطول وللعرض بحيث ترى خطين يتقاطعان مع بعضهما. 

يمكنك توسيع هذا الحقل عرضًا ليتسنى للمستخدم تعبئة الحقل لاحقا بشكل جيد.

الآن قم بالبحث مجددا عن حقل PasswordField، عند سحبه للنافذة، وبعد تغيير عرض الحقل الأول ستلاحظ أن هناك خطان جدد سيظهرون عند تحريك الحقل الأخير هذا، خط لمحاذاة هذا الحقل مع الحقل السابق يمينا وخط لمحاذاته يسارا كما في الصورة:

{% include image.html layout="responsive" width="400" height="300" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/Gluon2.gif" alt=" شرح برنامج تصميم الواجهة لتطبيق جافا - محرر جلون Gluon 2 " %}


هذه الخطوط يمكن استخدامها دائمًا لتنسيق الحقول ومحاذاتها مع بعضها ومع النافذة عموما.

هل لاحظت وجود قسم أحمر أعلى النافذة في الصورة السابقة؟ لقد وضعت هذا القسم لعرض عنوان النافذة الموجودين فيها أو اسم التطبيق في نافذة البداية. يمكنك عمل نفس الشي بالبحث عن AnchorPane واضافته لأعلى النافذة بالحجم المناسب، ثم تغيير اللون للأحمر مثلا من القائمة Properties على اليمين ستجد حقل Style اختر fx-background-color- ثم حدد اللون في الحقل بجانبه، كما في الصورة:

{% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/fx-background-color-gluon.png" alt=" شرح برنامج تصميم الواجهة لتطبيق جافا - محرر جلون Gluon 3" %}


حقل تحديد اللون الأخير هذا يمكن إدخال اللون به باللغة الإنجليزية مثلا "red" أو "blue" أو إذا أردنا ألوان أكثر تحديدا فيمكن أن تذهب لجوجل وتكتب "color picker" سيظهر لك قسم يمكنك اختيار اللون الذي تريد منه ثم نسخ كود HEX الخاص به ولصقه في الحقل هنا.

**ملاحظة:** إذا كنت تريد حذف لون الخلفية تمامًا أي زر بلا خلفية (شفاف تمامًا) فيمكنك كتابة none في حقل اللون. 


ولإضافة حقل نصي لقسم العناوين الأحمر الذي أضفناه، حيث سنكتب لاحقا اسم التطبيق أو النافذة في ذلك الحقل النصي، قم بالبحث عن Label وإفلاته ضمن المنطقة الحمراء.

لاحظ أن الـ label الأخير المضاف سيكون عنصرا من المنطقة الحمراء "AnchorPane" كما هو مبين في قسم Hierarchy أسفل يسار البرنامج لديك وكما في الصورة

{% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/gluon-hierarchy.png" alt="شرح برنامج تصميم الواجهة لتطبيق جافا - محرر جلون Gluon 4" %}

الآن قم بالحبث عن Button وإضافته أسفل حقلي اسم المستخدم وكلمة المرور، والذي سيكون زر تسجيل الدخول.

يمكنك دائما تجربة الواجهة من خلال النقر على خيار Preview في الأعلى ثم Show Preview in Window كما هو موضح في الصورة 

{% include image.html layout="responsive" width="400" height="200" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/gluon-preview.png" alt="شرح برنامج تصميم الواجهة لتطبيق جافا - محرر جلون Gluon 5" %}

أخيرًا قم بإضافة Label جديد أسفر الزر الأخير الذي أضفته، هذا الحقل النصي سنستخدمه لاحقا لعرض رسائل الخطأ للمستخدم، مثل الرسالة "اسم المستخدم أو كلمة المرور خاطئة" وغيرها ربما..

الآن لنقم بالتخصيص أكثر وثم تجهيز النافذة هذه للبدء بالبرمجة..


# تخصيص الواجهة

## تغيير الألوان

لاحظت أعلاه كيف قمنا بتغيير لون الحقل في الأعلى إلى الأحمر وهذا أحد أجزاء التخصيص.

الآن لنقم بتغيير لون زر تسجيل الدخول حيث أنه افتراضيا لونه بلون الخلفية وهذا يجعله غير واضح تماما.

انقر على الزر ضمن النافذة وبنفس الطريقة أعلاه يمكنك الذهاب في القائمة اليمنى Properties ثم Style حيث سيكون fx-background-color- ثم أدخل اللون بالحقل المجاور. سأختاره أنا أسود "black" ثم سأقوم بتغيير لون الخط للأبيض للوضوح، وهذا ستراه في نفس القسم في الأعلى "Text Fill" وستراه مضبوطا على Black، سأغيره أنا للأبيض.

## استخدام أيقونات للبرنامج

يمكنك استخدام أيقونات ووضعها في النافذة لتحسين جمالية تطبيقك، كأن تضيف مثلا بجانب حقل كلمة المرور أيقونة مفتاح وما إلى ذلك.

هناك مواقع على الإنترنت تتيح لك استخدام أيقوناتها وصورها مجانا وحتى للاستخدام التجاري أيضًا، منهم موقع [material.io](https://material.io/icons).

ولإضافة الأيقونات والصور لتطبيقك فهناك حقل في محرر الواجهة يدعى "ImageView" حيث يمكنك تحديد مسار الصورة من خصائص هذا الحقل.

## النص وتلميحات المستخدم

كما تلاحظ فالزر الذي وضعناه مكتوب عليه Button ونريد هنا تغييره لـ "تسجيل الدخول"، قم بالنقر عليه واكتب في حقل Text على اليمين (ضمن قسم Properties) عبارة "تسجيل الدخول".

لاحط أن عرض الزر تغير بناء على النص جديد، قم بإعادة تموضع الزر ليصبح في الوسط من جديد.

الآن وكما هو ملاحظ فإن حقول الإدخال فارغة، وبالتالي كيف سيعرف المستخدم ماالذي يجب إدخاله في كل حقل؟ إذًا لا بد من كتابة عبارة توضح المطلوب. انقر على الحقل الأول الخاص باسم المستخدم وستجد على اليمين حقل باسم "Prompt text" قم بإدخال العبارة "اسم المستخدم" فيه.

ونفس الشيئ بالنسبة لحقل كلمة السر.

**ملاحظة:** ماهو الفرق بين الحقلين Prompt text  و Text؟

الفرق هو أن الحقل Text يضبط نص الحقل المحدد، ليصبح هذا النص قابل للتحديد والنسخ ويُعطى أيضًا كقيمة في البرمجة، أي أننا يمكننا لاحقا استدعاء والحصول على نص الحقل ذلك برمجيًا، بينما الحقل Prompt text لا يضبط نص الحقل بل يبقى عمليا نص الحقل فارغا وإنما يتم إضافة تلميح للمستخدم، هذا التلميح غير قابل للتحديد أو النسخ ويُزال تلقائيًا بمجرد بدء المستخدم بالكتابة، ولو أضفنا التلميح كـ text فسيضطر المستخدم لحذف ذلك النص ليتمكن من تفريغ الحقل وكتابة اسم المستخدم الخاص به وهذا لا نريده طبعا.


لاحظ أنه يمكن تغيير جهة الحقل (النص) لليمين بدل اليسار من خيار Alignment كما في الصورة

{% include image.html layout="responsive" width="400" height="500" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/gluon-text-alignment.png" alt="شرح برنامج تصميم الواجهة لتطبيق جافا - محرر جلون Gluon 6" %}


الآن قم بتغيير نص الحقل Label في الأعلى ليحمل اسم التطبيق، مثلا "مشروع جافا" ولاحظ أنه يمكنك تغيير حجم ولون الخط من الإعدادات في نفس القسم على اليمين.

الحقل الأخير Label الذي أضفناه أسفل الزر قم بحذف النص الخاص به تمامًا، حيث نريد للحقل أن يكون افتراضيًا غير مرئي على الإطلاق، فقط عند حدوث خطأ ما سنضبط النص الخاص به من الكود البرمجي.

قم بمعاينة الواجهة كما هو موضح سابقا للتأكد من أن كل شيئ على مايرام ثم احفظ عملك بالذهاب من الأعلى يسارا للقائمة File ثم Save. عند الضغط على Save هنا فسيتم حفظ عملنا في الملف login.fxml الموجود في المشروع. ويبقى ربطه بملف جافا للتحكم بعناصر النافذة هذه برمجيًا.

# إضافة مايلزم للبرمجة

الآن سنقوم بثلاثة أشياء سريعًا:

1. إعطاء id لكل حقل
2. ربط النافذة هذه بكود الجافا أي بالـ Controller
3. نسخ الكود ولصقه في ملف الـ Controller لتحديثه


الخطوة الأولى تتم ببساطة بالضغط على الحقل ثم ستجد على اليمين قسم Code به حقل fx:id قم بإعطاء اسم id فريد له ويعبر عنه، مثلا حقل اسم المستخدم سيكون username_field (لاحظ أنه لايمكن استخدام الفراغات، هذه الـ ids سيتم استخدامها في البرمجة لاحقا) كما في الصورة:

{% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/gluon-ids.png" alt="شرح برنامج تصميم الواجهة لتطبيق جافا - محرر جلون Gluon 7" %}

والخطوة الثانية تتم بالذهاب يسارا لقسم Controller (سيكون أسفل يسار الشاشة) وفي حقل Controller class سنقوم بإدخال ملف الجافا المراد ربط هذه النافذة به مع مساره، والذي هو في حالتنا "LoginController" والمسار يبدأ من مجلد sample لذا سأكتب في هذا الحقل "sample.controller.LoginController" كما في الصورة:

{% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/gluon-controller.png" alt="شرح برنامج تصميم الواجهة لتطبيق جافا - محرر جلون Gluon 8" %}

أخيرا **وبعد حفظ تعديلاتنا** إلى الآن، نذهب في الأعلى يسارا للقائمة view (بجانب زر File) ثم آخر خيار "Show sample controller skeleton" ستظهر لك نافذة، اضغط أسفلها يمينا على الخيار Full ثم انسخ الكود بأكمله بالضغط على زر copy

{% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/gluon-sample-skeleton.png" alt="نسخ كود جافا من محرر جلون Gluon 9" %}

أغلق الآن برنامج محرر الواجهة واذهب ضمن برنامج IntelliJ للملف LoginController وقم بتحديد كل شيئ فيه وحذفه ثم لصق ما نسخته بدلا منه، وتم.

**ملاحظة:** قم دائمًا بحذف كل شيئ داخل دالة void initialize فهو غير مهم

هكذا يتم تصميم النوافذ وتعريفهم في الكود، لذا لن أكرر لاحقا شرح عمل أي نافذة أخرى، فجميعهم يتم عملهم بنفس الخطوات.

# تأثيرات إضافية

يمكن إضافة صنف (كلاس) جافا إضافي مثلا من أجل عمل بعض التأثيرات، مثلًا عندما يتم ملء نموذج تسجيل الدخول بمعلومات خاطئة يهتز حقلي اسم المستخدم وكلمة المرور للدلالة على أن المعلومات التي تحتويها غير صحيحة، لعمل هذا الاهتزاز يمكنك إنشاء مجلد animations بالضغط باليمين على مجلد sample ثم New ثم Package.

بعد ذلك انقر باليمين على المجلد الجديد animations ثم New ثم Java Class وقم بتسميته Shaker واجعل محتواه كالتالي:


{% highlight java %}

package sample.animations;

import javafx.animation.TranslateTransition;
import javafx.scene.Node;
import javafx.util.Duration;

public class Shaker {
    private TranslateTransition translateTransition;

    public Shaker(Node node){
        translateTransition = new TranslateTransition(Duration.millis(50), node);   //مدة الانتقال
        translateTransition.setFromX(0f);   //بدء الحركة من المسافة 0 على محور الإكس
        translateTransition.setByX(10f);    // وحتى المسافة 10
        translateTransition.setCycleCount(2);   //تكرار الهزة مرتين
        translateTransition.setAutoReverse(true);   //عكس العملية لعودة الحقول لمكانها الأصلي في النهاية
    }

    public void shake(){
        translateTransition.playFromStart();    //لبدء الحركة
    }


}
{% endhighlight %}


وبهذا يمكننا لاحقا استدعاء الصنف هذا عند أي عنصر لإضافة حركة الاهتزاز المكتوبة إليه.

يمكنك الآن تشغيل البرنامج للتأكد من أنه يعمل وكل شيئ على مايرام.



**ملاحظة:** قم بتغيير أبعاد نوافذ البرنامج من ملف Main.java في السطر التالي إلى الأبعاد التي وضعتها في محرر الواجهة:

        primaryStage.setScene(new Scene(root, 700, 400));

كما يمكنك تغيير العنوان الذي يظهر في شريط العناوين من نفس الملف

**ملاحظة2:** ستلاحظ عند تشغيل البرنامج وتكبير النافذة أن العناصر لا تتغير وفق حجم النافذة الجديد، لحل هذه المشكلة يجب استخدم العنصر GridPane بدلا من AnchorPane في محرر الواجهة، ولكن شرحنا هذا لا يشمل شرح GridPane.



****

**التالي:** [الربط مع قاعدة البيانات](/java-database-handler)


