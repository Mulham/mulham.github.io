---
layout: post
date: 2020-02-04
title: أمثلة عملية في لغة سي
description: أمثلة عملية في لغة البرمجة سي مع الحل مأخوذة من دروس جامعية أكاديمية
type: tutorial
feature: /assets/posts/source-code.jpg
caption: Image by Christopher Kuszajewski from Pixabay 
tags: [برمجة, تعليم]
excerpt: فيما يلي أمثلة عملية في لغة البرمجة سي مع الحلول.الحلول بالنسبة للأسئلة التي تتطلب كتابة برامج ليست وحيدة أي يمكن أن يكون حلك لهذه الأسئلة أفضل، ويمكن اعتبار الحلول هنا أحد الحلول الممكنة.
---

فيما يلي أمثلة عملية في لغة البرمجة سي مع الحلول.

الحلول بالنسبة للأسئلة التي تتطلب كتابة برامج ليست وحيدة أي يمكن أن يكون حلك لهذه الأسئلة أفضل، ويمكن اعتبار الحلول هنا أحد الحلول الممكنة.


* Toc
{:toc}

# الأسئلة

1.
    فيما يلي برنامج بسيط بلغة سي، ما هو ناتج البرنامج عند التنفيذ ولماذا؟

        {% highlight c %}
        #include <stdio.h>

        int main() {
          
          int k = 54000;
          short s = k;
          printf("%d", s);

          return 0;
        }
          {% endhighlight %}

2.
    يحوي برنامج سي التالي على أخطاء، قم بتصحيحها

    {% highlight c %}
        #include <stdio

        int main() {
          char c = A;
          char d = B;

          scanf("%d", a);

          if (a % 2 == 0) {
             printf("%c: Number is even\n", c); 
          else {
             printf("%c: Number is odd\n", d); 
          }
          
          
          return 0;
     {% endhighlight %}


  مثال على المدخل:

  3

  مثال على الناتج: 

   B: Number is odd

3.
    اكتب برنامج يقرأ ثلاثة أعداد صحيحة ويُعطي أكبرهم

   مثال على المُدخل:

  <div dir="ltr">
  8 11 -443
  </div>


  مثال على الناتج:

  <div dir="ltr">
  11
  </div>

4.
  اكتب برنامجًا يقرأ عدد الدقائق ويُعطي الناتج بشكل ساعات ودقائق

  مثال على المُدخل: عدد صحيح أكبر من الصفر

   <div dir="ltr">
   546
   </div>

   مثال على الناتج: عدد الساعات والدقائق في حال إعطاء قيمة صحيحة، وإلا يعطي رسالة "Error"

   <div dir="ltr">
   9 Hours, 6 Minutes
   </div>

5.
  اكتب برنامجًا يقرأ حرف char ويكون الناتج بحسب المُدخل "رقم" أو "حرف" أو "رمز"

   مثال على المدخل:

   8

   مثال على الناتج:

   Number

   مثال على المدخل 2:

   ?

   مثال على الناتج 2:

   Symbol

6.
ماهو ناتج البرنامج التالي:

    {% highlight c %}
        #include <stdio.h>

        int a = 60;
        int b;

        int foo(int a, int b) {
            a = a * (-1);
            b = b + 11;
            
            return a;
        }

        void faa(int a) {
            a = a + 3;
        }

        int fuu() {
            return a - 2;
        }



        int main() {
            
            int c = 2;
            b = 3;
            
            foo(a,c);
            
            c = foo(a,b);
            
            faa(c);
            
            fuu();
            
            printf("%d", c);
            
            return 0;
        }
     {% endhighlight %}

7.
اكتب برنامجًا يقرأ عددين حقيقيين من المستخدم ويعطي أكبرهما.

   **بناء البرنامج:**

   * اكتب دالة اسمها **max** والتي تحوي على معاملَين (بارامترَين) وهما عددان حقيقيّان وتقوم هذه الدالة بإرجاع (return) عدد حقيقي.

   * اكتب الدالة الرئيسيّة **main** حيث يتم قراءة العددين الحقيقيين من المستخدم، ثم يتم استدعاء دالة max مع هذين العددين ثم يتم طباعة القيمة المُرجعة على الشاشة مع ثلاثة أرقام بعد الفاصلة.

   مثال على المُدخل:

   <div dir="ltr">
   3.6 16.4
   </div>


   مثال على الناتج:

   <div dir="ltr">

  16.400
  </div>


  مثال 2 على المُدخل:

  <div dir="ltr">

  -20 -35
  </div>

  مثال 2 على الناتج:
  <div dir="ltr">

  -20.000
  </div>


8.اكتب برنامجًا يقرأ من المستخدم عدد موجب صحيح ويعطي العاملي لذلك العدد.

   **بناء البرنامج:**

   * اكتب دالة اسمها **Factorial** والتي تحوي عدد موجب صحيح كمعامل وتقوم بإرجاع عدد صحيح. في حال كان المعامل ليس عددًا موجبًا يجب أن تقوم الدالة بإرجاع القيمة **-1**

   * اكتب الدالة الرئيسيّة **main** حيث يتم قراءة العدد الصحيح المطلوب حساب العاملي الخاص به من المستخدم. ثم استدعِ الدالة Factorial مع ذلك العدد واطبع الناتج المُرجع على الشاشة. إذا قامت الدالة Factorial بإرجاع القيمة -1 فقم بطباعة رسالة خطأ على الشاشة (انظر معالجة الأخطاء أدناه).

  **معالجة الأخطاء:** في حال قام المستخدم بإدخال قيمة سالبة فيتم طباعة رسالة الخطأ التالية على الشاشة:

  Wrong Input

  مثال على المُدخل:

  4

  مثال على الناتج:

  24

  مثال 2 على المُدخل:

  -19

  مثال 2 على الناتج:

  Wrong Input

  مثال 3 على المُدخل:

  0

  مثال 3 على الناتج:

  1

9.
 اكتب برنامجًا يقرأ 10 محارف (أحرف/أرقام/رموز) من المستخدم ثم يطبعها بعد وضع علامة الفاصلة `,` بينها.

   **بناء البرنامج:**

   * قم بتعريف مصفوفة Array في الدالة الرئيسية **main** لتحفظ المحارف العشرة بها.

   * اطلب من المستخدم إدخال المحارف العشرة وقم بحفظها في تلك المصفوفة

   * قم بطباعة عناصر المصفوفة (المحارف) مفصولة بفاصلة. (تنبيه: يجب أن لا يتم طباعة فاصلة بعد آخر مِحرَف)

  مثال على المُدخل:
  
  <div dir="ltr">
  2 % a b ( r ) ? t h
  </div>


  مثال على الناتج:

  <div dir="ltr">
  2,%,a,b,(,r,),?,t,h
  </div>


  مثال 2 على المُدخل:

  <div dir="ltr">
  a b c d e f g h i j
  </div>


  مثال 2 على الناتج:

  <div dir="ltr">
  a,b,c,d,e,f,g,h,i,j
  </div>


10.
اكتب برنامجًا يقرأ خمسة أعداد حقيقية من المستخدم ويطبع متوسطهم الحسابي (مجموع الأعداد على عددهم) على الشاشة.

   **بناء البرنامج:**

   * قم بتعريف مصفوفة Array في الدالة الرئيسية لتخزين الأعداد الخمسة بها.
  
   * احسب المتوسط الحسابي لعناصر المصفوفة وأعطِ الناتج على الشاشة مع ثلاثة أرقام بعد الفاصلة.

  مثال على المُدخل:

  <div dir="ltr">

  20.0 23 12 65 4
  </div>


  مثال على الناتج:

  <div dir="ltr">

  24.800
  </div>


  مثال 2 على المُدخل:

  <div dir="ltr">

  29.2 3.4 56.8 43 44
  </div>


  مثال 2 على الناتج:

  <div dir="ltr">

  35.280
  </div>



# الحلول

1. -11536 حيث تم تحويل متغير من نوع INT إلى Short والذي لايتسع للعدد 54000 فتم حذف البتات الزائدة منه ليصبح -11536

2.
    {% highlight c %}
        #include <stdio.h>

        int main() {
          char c = 'A';
          char d = 'B';	
          int a;
          // لقراءة عدد من المستخدم
          scanf("%d", &a);

          
          if (a % 2 == 0) {
        printf("%c: Number is even\n", c); 
          }
        else {
        printf("%c: Number is odd\n", d); 
        }
          
          
          return 0;
         }
    {% endhighlight %}

3.
    {% highlight c %} 
        #include <stdio.h>

        int main() {
          int a,b,c;
          scanf("%d", &a);
          scanf("%d", &b);
          scanf("%d", &c);
          int biggest_num = a;
          if (b>a){
            biggest_num = b;}
          if (c>biggest_num){
            biggest_num = c;} 
          printf("%d\n",biggest_num);
          return 0;
          }
    {% endhighlight %}

4.
    {% highlight c %}
         #include <stdio.h>

        int main() {
          int a,s,m;
          scanf("%d", &a);
          if (a >=0){
	          m = a % 60;
	          s = (a-m) / 60;
	          printf("%d Hours, %d Minutes", s,m);
          }
          else {
	          printf("Error");
          }
          return 0;
          }
    {% endhighlight %}

5.
    {% highlight c %}
        #include <stdio.h>

        int main()
        {
            char ch;
            scanf("%c", &ch);
            if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
            {
                printf("Letter");
            }
            else if(ch >= '0' && ch <= '9')
            {
                printf("Number");
            }
            else 
            {
                printf("Symbol");
            }

            return 0;
        }
    {% endhighlight %}

6.
   -60

7.
    {% highlight c %}
        #include <stdio.h>
        float max(float, float);
        int main() {
            
	        float a,b;
	        scanf("%f%f", &a, &b);
	        float c = max(a,b);
	        printf("%.3f", c);
	        
	        
            return 0;
        }
        float max(float a, float b){
	        if (a>b){
		        return a;
	        }
	        else{
		        return b;
	        }
        }
    {% endhighlight %}

8.
    {% highlight c %}
        #include <stdio.h>
        int Factorial(int);
        int main() {
	        int n;
	        scanf("%d", &n);
	        int r = Factorial(n);
	        if (r == -1){
		        printf("Wrong Input");
	        }
	        else{
		        printf("%d", r);
	        }
            return 0;
        }
        int Factorial(int n){
	        int c= -1;
	        
	        if (n>=0){
		        int a;
		        c = 1;
		        int i = 1;
		        a = n;
		        while (n-i >= 1){
			        a = a*(n-i);
			        i = i +1;
		        }
		        if (i > 1){
			        c = a;
		        }
		        
	        }
	        return c;
        }
    {% endhighlight %}

9.
    {% highlight c %}

        #include <stdio.h>

        int main() {
            char a[10];
	        char s;
	        short i =0;
	        while (i<10){
		        scanf("%c%c", &a[i], &s);
		        i = i + 1;
	        }
	        i = 0;
	        while (i<10){
		        printf("%c", a[i]);
		        if (i<9){
			        printf(",");
		        }
		        i = i + 1;
	        }
            return 0;
        }

    {% endhighlight %}

10.
    {% highlight c %}
        #include <stdio.h>

        int main() {
            double a[5];
	        double d = 0;
	        char s;
	        short i =0;
	        while (i<5){
		        scanf("%lf%c", &a[i], &s);
		        d = d + a[i];
		        i = i + 1;
	        }
	        d = d/5;
	        printf("%.3lf", d);
            return 0;
        }
    {% endhighlight %}

أرجو أن يكون المقال قد أفادك.

لمزيد من الأمثلة يرجى [الضغط هنا](https://mulham.github.io/c-language-examples2)

المرجع: درس مدخل إلى علم الحاسوب. د.بورجو يلدز - الجامعة التركية الألمانية
