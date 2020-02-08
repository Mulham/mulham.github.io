---
layout: post
date: 2020-02-08
title: تمارين محلولة في لغة البرمجة سي C
description: تمارين محلولة في لغة البرمجة سي مأخوذة من منهاج مدخل لعلم الحاسوب في الجامعة التركية الألمانية
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

# الأسئلة

1.
  اكتب برنامجًا يقرأ 9 أرقام من المستخدم ويحفظها في مصفوفة 3x3 ثم يطبعها كما في المثال المعطى أدناه.



  مثال على المُدخل: 

   <div dir="ltr">
   1 3 4 6 7 4 5 4 7
   </div>

   مثال على الناتج:

   <div dir="ltr">
   1 3 4

   6 7 4

   5 4 7
   </div>

2.
  اكتب برنامجًا يمكنه جمع مصفوفتين 3x3 باستخدام الخطوات التالية:

  * قم بأخذ 9 أعداد من المستخدم واحفظها في مصفوفة

  * خذ 9 أعداد أخرى من المستخدم واحفظها في مصفوفة ثانية

  * قم بجمع هاتين المصفوفتين

  * قم بإعطاء النتيجة كما في المثال أدناه

  **تلميح:** للتذكير فإن جمع مصفوفتين يكون كما هو موضح أدناه

  <amp-img width="400" height="200" src="/assets/arrays-sum.png" alt="أمثلة وتمارين في لغة البرمجة سي - جمع مصفوفتين"></amp-img>
 

   مثال على المدخل:

   1 3 4 6 7 4 5 4 7 8 9 12 11 3 45 6 34 2

   مثال على الناتج:

  <div dir="ltr">
   9 12 16

   17 10 49

   11 38 9
  </div>


3.
اكتب برنامجًا يستطيع ضرب أي مصفوفتين مربعتين بأي حجم (2x2 أو 3x3 ..إلخ).

   **بناء البرنامج:**

   * خذ عدد موجب صحيح من المستخدم والذي سيكون بُعد المصفوفة المربعة

   * خذ من المستخدم أعدادًا كافية بقدر عناصر مصفوفتين ذات البُعد الذي تم إدخاله في الخطوة السابقة لتملأ المصفوفتين

   * اضرب المصفوفتين وأعطِ الناتج على الشاشة


  **تلميح:** للتذكير فإن ضرب مصفوفتين يكون كما هو موضح أدناه

  <amp-img width="500" height="200" src="/assets/arrays-multiplication.png" alt="أمثلة وتمارين في لغة البرمجة سي - ضرب مصفوفتين"></amp-img>


   مثال على المُدخل:

   <div dir="ltr">
   2 3 4 5 6 7 8 9 10
   </div>


   مثال على الناتج:

   <div dir="ltr">

  57 64

  89 100
  </div>

4.
المطلوب حساب محدد مصفوفة 3x3. 


   * يجب أن يقرأ البرنامج عناصر المصفوفة ذات البعد 3x3 ومن ثم حساب المُحدِّد وإعطاء النتيجة

   *  يمكن حساب مُحدِّد مصفوفة 3x3 وفق قاعدة ساروس التالية:

   ليكن لدينا المصفوفة:

    <amp-img width="200" height="130" src="/assets/array.png" alt="أمثلة وتمارين في لغة البرمجة سي - حساب محدد مصفوفة"></amp-img>

   يكون المحدد:

    <amp-img width="450" height="100" src="/assets/sarrus.png" alt="أمثلة وتمارين في لغة البرمجة سي - قاعدة ساروس"></amp-img>

  مثال على المُدخل:

  1 2 3 4 5 6 7 8 9

  مثال على الناتج:

  0

  

5.
 يتطلب تحديد فيما إذا كانت كلمة أو عبارة لها خاصية [مالا يستحيل بالإنعكاس](https://ar.wikipedia.org/wiki/قلب_مستو) (مثل خوخ تقرأ بالإتجاهين، Mum كذلك..)


   **بناء البرنامج:**

   * اطلب من المستخدم كلمة أو عبارة نصية واحفظها في مصفوفة من نوع char

   * قم بطباعة "**yes**" في حال كانت العبارة لا تستحيل بالإنعكاس، و "**no**" فيما عدا ذلك. إذا كان المٌدخل من المستخدم غير صالح (كأن يُدخِل أرقامًا بدلًا من أحرف) قم بطباعة "**Wrong Input**"

  مثال على المُدخل:
  

  otto



  مثال على الناتج:


  yes



# الحلول


1.
    {% highlight c %}
    #include <stdio.h>
    int main(){
	int a[3][3], i=0, j=0;
	while (i<3){
		while (j<3){
			scanf("%d", &a[i][j]);
			j = j+1;
		}
		j = 0;
		i = i+1;
	}
	i = 0;
	j = 0;
	while (i<3){
		while (j<3){
			printf("%d",a[i][j]);
            if (j<2){
                printf(" ");
            }
			j = j+1;
		}
	   	printf("\n");
		j = 0;
		i = i+1;
	}
	return 0;
    }
    {% endhighlight %}

2.
    {% highlight c %} 
    #include <stdio.h>
    int main(){
	int a[3][3], i=0, j=0;
	while (i<3){
		while (j<3){
			scanf("%d", &a[i][j]);
			j = j+1;
		}
		j = 0;
		i = i+1;
	}
	i = 0;
	j = 0;
	int b[3][3];
	while (i<3){
		while (j<3){
			scanf("%d", &b[i][j]);
			j = j+1;
		}
		j = 0;
		i = i+1;
	}
	i = 0;
	j = 0;
	while (i<3){
		while (j<3){
			printf("%d",a[i][j]+b[i][j]);
            if (j<2){
                printf(" ");
            }
			j = j+1;
		}
	   	printf("\n");
		j = 0;
		i = i+1;
	}
	return 0;
    }
    {% endhighlight %}

3.
    {% highlight c %}
    #include <stdio.h>
    int main(){
	int n;
	scanf("%d", &n);
	int a[n][n], i=0, j=0;
	int multiply[n][n];
	while (i<n){
		while (j<n){
			scanf("%d", &a[i][j]);
			j = j+1;
		}
		j = 0;
		i = i+1;
	}
	i = 0;
	j = 0;
	int b[n][n];
	while (i<n){
		while (j<n){
			scanf("%d", &b[i][j]);
			j = j+1;
		}
		j = 0;
		i = i+1;
	}
	i = 0;
	j = 0;
	int k, sum = 0;
	for (i = 0; i < n; i++) {
      for (j = 0; j < n; j++) {
        for (k = 0; k < n; k++) {
          sum = sum + a[i][k]*b[k][j];
        }
 
        multiply[i][j] = sum;
        sum = 0;
      }
    }
 
    for (i = 0; i < n; i++) {
      for (j = 0; j < n; j++){
        printf("%d", multiply[i][j]);
		if(j<n-1){
			printf(" ");
		}
		}
      printf("\n");
    }
	return 0;
    }

    {% endhighlight %}

4.
    {% highlight c %}
    #include <stdio.h>
    int main(){
	int a[3][3];
	int i = 0, j = 0, sum;
	while (i<3){
		while (j < 3){
			scanf("%d", &a[i][j]);
			j = j+1;
		}
		j=0;
		i=i+1;
	}
	j = 0;
	i = 0;
	sum = a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[0][2]*a[1][0]*a[2][1]-a[0][2]*a[1][1]*a[2][0]-a[0][1]*a[1][0]*a[2][2]-a[0][0]*a[1][2]*a[2][1];
	printf("%d", sum);
	return 0;
    }
    {% endhighlight %}

5.
    {% highlight c %}
    #include <stdio.h>

 
    int main(){
	char s[16];	//maximum 16 letter 

	
	
		int i =0;
		while (i<16){
			s[i] = 0;
			i = i+1;
		}
		scanf("%s", &s);
		i = 0;
		int len;
		while (i<16){
			if (s[i] == 0){
				len = i;
				i = 16;
			}
			i = i+1;
		}
		
		char reverse[len];
	i = 0;
	int j = 2;
	int x = len;
	while (i<len){
		if (!(s[i]>=97 && s[i]<=122)){
			j = 0;
		}
		reverse[x-1] = s[i];
		i = i+1;
		x = x-1;
	}
	i = 0;

	
	while (i<len){
		if (!(s[i]==reverse[i])){
			j = 3;
			i = 16;
		}
		i = i+1;
	}

	if (j==0){
		printf("Wrong Input");
		
	}
	else if (j == 3){
			printf("no");
	}
	else{
		printf("yes");
	}

	return 0;
    }

          
    {% endhighlight %}



أرجو أن يكون المقال قد أفادك.

المرجع: درس مدخل إلى علم الحاسوب. د.بورجو يلدز - الجامعة التركية الألمانية
