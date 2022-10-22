---
layout: post
date: 2020-07-01
title: أمثلة متقدمة في لغة سي مع الحل
description: أمثلة عملية في التعامل مع الوقت وتعديل الملفات في لغة البرمجة سي مع الحل مأخوذة من دروس جامعية أكاديمية
type: tutorial
feature: /assets/posts/source-code.jpg
caption: Image by Christopher Kuszajewski from Pixabay 
tags: [برمجة, تعليم]
hidden: true
---

إليك تمارين محلولة في لغة البرمجة سي. وهي تتمة للأمثلة التي بدأناها هنا:

* [أمثلة عملية في لغة سي](https://mulham.github.io/c-language-examples/)

وأعيد التنويه بأن الحلول هنا ليست مثالية وإنما هي أحد الحلول الممكنة.

* Toc
{:toc}


# 1. التعامل مع الوقت في لغة سي

 اكتب برنامجًا بلغة سي لعد الثواني (مع أجزاء الثانية) بشكل مستمر.


**الحل:**
    {% highlight c %}

#include <stdio.h>
#include <time.h>
#define NO_SEC 15
    int main(){
    double sec;
    int cnt=0,period;
    period=(int)CLOCKS_PER_SEC*NO_SEC;
    time_t start,current=0;
    start=clock();
    while(current<period){
        current=clock();
        sec=(double)(current-start)/CLOCKS_PER_SEC;
        printf("%f\n",sec);
    }
} 

    {% endhighlight %}

# 2. تعديل الملفات في لغة سي

اكتب سكريبت "tab2space" والذي يقوم بتحويل أحرف زر الـ <kbd>tab</kbd> إلى فراغات (زر التاب يعطي عادة أربع أو ثمانية فراغات والمطلوب اختصارها بفراغ واحد). افترض في هذا المثال أن الـ "تاب" هو أربع فراغات. السكريبت يجب أن يتم تشغيله بالأمر التالي:

        cat text_with_tabs.txt | ./tab2space > text_without_tabs.txt

لإظهار النتيجة يمكنك ببساطة استخدام الدالة ()printf.

**الحل:**

في البداية أعتقد أن السؤال يحتاج لشرح لتتضح لك الأمور تمامًا. الأمر المعطى والذي يجب تشغيل سكريبتك (الكود) من خلاله يستخدم [الأمر cat](/linux/cat) ثم اسم الملف الذي يحوي عدة "tabs" لتحويلها لفراغات وحيدة، واسم الملف هذا هو "text_with_tabs.txt" وسيكون اسم الكود الخاص بك (والقابل للتنفيذ أي بعد عمل compiling) هو "tab2space" وسنكتب الناتج للملف "text_without_tabs.txt" الذي سيتم إنشاءه عند تنفيذ الأمر.

من المفيد قراءة الملاحظات الموجودة في الصفحة [هنا](/linux/intro) والتي تتحدث عن أساسيات أوامر لينكس لفهم مثلا وظيفة الرمز `|` في الأمر أعلاه وغيره من الأمور الأساسية.

الآن لنأتي للكود (الحل)

{% highlight c %}

#include <stdio.h>

int main (void) {

    int c;

    while ((c = getchar ()) != EOF)
    {
        if (c == '\r') continue;
        if (c == '\n') {        /* handle newlines/carriage-returns */
            putchar (c);
            while ((c = getchar ()) == '\n' || c == '\r') {}
            if (c != EOF) ungetc (c, stdin); else break;
            continue;
        }
        if (c == ' ' || c == '\t') {  /* spaces & tabs */
            putchar (' ');
            while ((c = getchar ()) == ' ' || c == '\t') {}
            if (c != EOF) ungetc (c, stdin); else break;
            continue;
        }
        putchar (c);
    }
    return 0;
}

{% endhighlight %}

**شرح الحل:**

* يتم قراءة الملف المُعطى حرفًا حرفًا للبحث عن أربع فراغات متتالية، وهكذا إلى الوصول لنهاية الملف والذي يُرمز له بـ (EOF) ويعني "End Of File" أي "نهاية الملف"

* يقوم الكود بالبحث عن سطر جديد (رمز السطر الجديد في نظام لينكس n\ وفي نظام ويندوز r\ ) 

* عندما يجد الكود فراغ أو تاب (أربع فراغات متتالية ويُرمز له t\ ) يقوم البرنامج باستبدالهام بفراغ واحد.


مقال متعلق: [التعامل مع الملفات بلغة سي](/التعامل-مع-الملفات-بلغة-سي)

