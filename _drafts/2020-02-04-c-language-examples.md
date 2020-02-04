---
layout: post
date: 2020-02-04
title: أمثلة عملية في لغة سي
description: أمثلة عملية في لغة البرمجة سي مع الحل مأخوذة من دروس جامعية أكاديمية
type: tutorial
comments: true
tags: [برمجة, تعليم] 
---

فيما يلي أمثلة عملية في لغة البرمجة سي مع الحلول.

1. فيما يلي برنامج بسيط بلغة سي، ما هو ناتج البرنامج عند التنفيذ ولماذا؟

        #include <stdio.h>

        int main() {
          
          int k = 54000;
          short s = k;
          printf("%d", s);

          return 0;
        }

2. يحوي برنامج سي التالي على أخطاء، قم بتصحيحها

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

    مثال على المدخل:
     3
    مثال على الناتج: 
    B: Number is odd

3. اكتب برنامج يقرأ ثلاثة أعداد صحيحة ويُعطي أكبرهم

    مثال على المُدخل:
    8 11 -443
    مثال على الناتج:
    11

4. اكتب برنامجًا يقرأ عدد الدقائق ويُعطي الناتج بشكل ساعات ودقائق

    مثال على المُدخل: عدد صحيح أكبر من الصفر
    546
    مثال على الناتج: عدد الساعات والدقائق في حال إعطاء قيمة صحيحة، وإلا يعطي رسالة "Error"
    9 Hours, 6 Minutes

5. اكتب برنامجًا يقرأ حرف char ويكون الناتج بحسب المُدخل "رقم" أو "حرف" أو "رمز"

    مثال على المدخل:
    8
    مثال على الناتج:
    Number
    مثال على المدخل 2:
    ?
    مثال على الناتج 2:
    Symbol

6. ماهو ناتج البرنامج التالي:


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

7. 

الحل:

1. -11536 حيث تم تحويل متغير من نوع INT إلى Short والذي لايتسع للعدد 54000 فتم حذف البتات الزائدة منه ليصبح -11536

2. 

        #include <stdio.h>

        int main() {
          char c = 'A';
          char d = 'B';	
          int a;
          // einlesen einer Zahl vom Benutzer
          scanf("%d", &a);

          
          if (a % 2 == 0) {
        printf("%c: Number is even\n", c); 
          }
        else {
        printf("%c: Number is odd\n", d); 
        }
          
          
          return 0;
         }

3.

        #include <stdio.h>

        int main() {
          int a,b,c;
          scanf("%d", &a);
          scanf("%d", &b);
          scanf("%d", &c);
          int grosste_zahl = a;
          if (b>a){
            grosste_zahl = b;}
          if (c>grosste_zahl){
            grosste_zahl = c;} 
          printf("%d\n",grosste_zahl);
          return 0;
          }

4. 

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

5.

        #include <stdio.h>

        int main()
        {
            char ch;
            scanf("%c", &ch);
            if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
            {
                printf("Buchstabe");
            }
            else if(ch >= '0' && ch <= '9')
            {
                printf("Zahl");
            }
            else 
            {
                printf("Zeichen");
            }

            return 0;
        }

6. -60
