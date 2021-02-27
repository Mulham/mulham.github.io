---
layout: post
date: 2021-02-27
title: القاموس في لغة جافا
description: شرح صنف القاموس Dictionary ودالاته في لغة جافا مع مثال عملي
type: tutorial
feature: /assets/posts/dictionary-java.png
caption: Image by educative.io
tags: [برمجة, تعليم]
---

مرحبًا..وردتني بعض الأسئلة عبر البريد الإلكتروني عن القواميس في لغة جافا فأحببت تخصيص هذا المقال لشرح هذا النوع من البيانات في لغة جافا. حيث ستجد تعريفا وشرحا عاما عن القاموس ودالاته ثم في النهاية ستجد مثال عملي كامل عن تعريف القاموس واستخدام تلك الدالات بشكل عملي.


القاموس في لغة جافا وهو من مكتبة util.Dictionary هو أحد أنواع البيانات، وهو صنف abstract أي لايتم إنشاء عنصر منه (راجع [ملاحظات جافا](https://mulham.github.io/Java-notes/#abstract-class)

وهو عبارة عن زوج مفتاح-قيمة حيث يتم إدخال المفاتيح وقيمهم (مثلا المفتاح "العمر" والقيمة "26" والمفتاح "الطول" والقيمة "170" وهكذا). كما يمكن من اسمه كونه قاموسًا أن يستخدم فعلا لذلك، مثلا المفتاح الكلمة والقيمة ترجمتها أو مرادفها.

يمكن استخراج القيم بإعطاء مفاتيحها.

**تعريف القاموس في لغة جافا**

        public abstract class Dictionary extends Object

وهنا يجب ذكر أنه لإنشاء قاموس في لغة جافا فيجب اختيار صنف يحقق بناء زوج قيمة-مفتاح، مثل HashTables و HashMap و LinkedHashMap. يمكنك المتابعة الآن وفهم القاموس ودالاته دون الخوض في تفاصيل هؤلاء..

**الدالات في صنف القاموس**

1. إدراج زوج مفتاح قيمة: put(K key, V value)


        public abstract V put(K key, V value)

2. عرض جميع القيم في القاموس ()elements

        public abstract Enumeration elements()

3. عرض قيمة لمفتاح معين get(Object key)

        public abstract V get(Object key)

4. التحقق من خلو القاموس أو عدمه ()isEmpty: هذه الدالة تقوم بإرجاع true إذا كان القاموس فارغ أو false إن كان يحوي على الأقل زوج واحد من مفتاح-قيمة

        public abstract boolean isEmpty()

5. عرض جميع المفاتيح في القاموس ()keys

        public abstract Enumeration keys()


6. حذف مفتاح وقيمته وذلك بإعطاء المفتاح فقط: remove(Object key) وتقوم بإرجاع القيمة للمفتاح المعطى بعد حذفهم طبعا من القاموس

        public abstract V remove(Object key)

7. عرض عدد الأزواج مفتاح-قيمة الموجودين في القاموس (يمكن أن تفكر به أيضا على أنه عدد المفاتيح أو عدد القيم فكلاهما نفس العدد): ()size

        public abstract int size()


والآن لنرى مثالًا عمليا عن القاموس ودالاته المذكورة:

{% highlight java %}

// Java Program explaining util.Dictionary class Methods 
// put(), elements(), get(), isEmpty(), keys() 
// remove(), size() 
  
import java.util.*; //القاموس موجود في هذه المكتبة وعند كتابة رمز النجمة فهذا يعني
// أننا نريد استيراد كل عناصر المكتبة util حيث القاموس أحدها
public class New_Class 
{ 
    public static void main(String[] args) 
    { 
  
        // Initializing a Dictionary تهيئة القاموس
        Dictionary mulham = new Hashtable(); // hashtable تعريف قاموس باسم ملهم وربطه بـ
  
        // put() method 
        mulham.put("age", "26"); // إدراج مفتاح العمر والقيمة 26 للقاموس
        mulham.put("height", "172"); 
  
        // elements() method عرض قيم القاموس وذلك يجب أن يتم ضمن حلقة
        for (Enumeration i = mulham.elements(); i.hasMoreElements();) 
        { 
            System.out.println("Value in Dictionary : " + i.nextElement()); 
        } 
  
        // get() method : 
        System.out.println("\nValue at key = 6 : " + mulham.get("age")); 
        System.out.println("Value at key = 456 : " + mulham.get("height")); 
  
        // isEmpty() method : 
        System.out.println("\nThere is no key-value pair : " + mulham.isEmpty() + "\n"); 
  
        // keys() method : 
        for (Enumeration k = mulham.keys(); k.hasMoreElements();) 
        { 
            System.out.println("Keys in Dictionary : " + k.nextElement()); 
        } 
  
        // remove() method : 
        System.out.println("\nRemove : " + mulham.remove("age")); 
        System.out.println("Check the value of removed key : " + mulham.get("age")); 
  
        System.out.println("\nSize of Dictionary : " + mulham.size()); 
  
    } 
} 

{% endhighlight %}


إن كان لديك أي سؤال فلا تتردد في مراسلتي.

اقرأ أيضًا: [أمثلة في لغة جافا](https://mulham.github.io/%D8%A3%D9%85%D8%AB%D9%84%D8%A9-%D9%81%D9%8A-%D9%84%D8%BA%D8%A9-%D8%AC%D8%A7%D9%81%D8%A7/)

المراجع:

* <https://www.geeksforgeeks.org/java-util-dictionary-class-java/>
* <https://www.educative.io/edpresso/how-to-create-a-dictionary-in-java>
