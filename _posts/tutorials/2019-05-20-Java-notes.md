---
date: 2019-05-20
title: ملاحظات جافا
description: ملاحظات هامة لمبتدئي لغة جافا والفروقات الرئيسية بين بعض أنواع الأصناف (interface classes vs abstract classes..)
tags: [Java, برمجة]
image:
  path: /assets/posts/java.jpg
  alt: "Java is annoying by Azhaaarry is licensed under CC BY-NC-ND 2.0" 
---

الملاحظات في الأسفل هي في الحقيقة ملاحظات عن مبادئ البرمجة كائنية التوجه (object oriented programming) ولكن في لغة جافا تحديدا (حيث أن البرمجة كائنية التوجه هي مبادئ موجودة في العديد من لغات البرمجة)

* Toc
{:toc}


## interface class
يُعرّف الصنف من هذا النوع على الشكل التالي:

		public interface Name

تحتوي هذه الأصناف على دالّات Methods بدون متن body أي فقط تعريف للدالات، مثلًا على الشكل:

		public boolean add(String s);

وهذا النوع من الدالات methods الذي لا يحوي متن body يدعى abstract methods

وبالتالي تكون الأصناف من نوع interface عبارة عن مجموعة من الدالات ذات النوع abstract أي collection of abtract methods

يمكن أن تحتوي أصناف الـ interface على ثوابت أيضا، أي تعريف متغيرات مع إعطاء قيمهم، وأيضًا دالات رئيسية default methods ودالات ثابتة static methods 

الـ interface class تحل مشكلة التوريث في لغة جافا، حيث أنه غير ممكن لصنف أن يرث من أكثر من صنف آخر، هذا يعني أنه **لا** يمكن كتابة:

		public class Name extends name1, name2{

ولكن **يمكن** كتابة:

		public class Name implements name1, name2{

لماذا التوريث ﻷكثر من صنف غير مسموح في الجافا؟ لعدم حصول مشاكل فعندما يكون لدينا صنف class يرث صنفين في نفس الوقت ويكون بين تلك الأصناف تعارض (دالتين لها نفس الاسم مثلا) فلا يمكن تحديد أي دالة أو أمر يجب أن ينفذ الصنف الوارث! ولكن عند الوراثة من صنفي interface لايمكن أن يحدث فيها تعارض ﻷنها لا تحوي تعليمات ضمن التوابع methods.

ولكن! الـ interface يمكن أن يحوي constants متغيرات مع قيمهم، ولكن من الأفضل عدم استخدام هذه الميزة لعدم حصول تعارض كما ذكرنا، في حالة التعارض ستظهر  compiling error
ولن يتم بناء البرنامج

وظيفة أصناف ال interface:  تعمل بشكل قالب يحدد الوظائف التي يجب أن تكون بالأصناف التابعة.

مثال على صنف interface وصنف تابع له
```java
 public interface ExampleInterface {
    public void doAction();
    public String doThis(int number);
 }

 public class sub implements ExampleInterface {
     public void doAction() {
       //specify what must happen
     }

     public String doThis(int number) {
       //specfiy what must happen
     }
 }
```

## Abstract class

نفس ال interface ولكن تحوي تعليمات ضمن ال methods، كما لا يمكن إنشاء عنصر (object) منها، يعني لدينا مثلا صنف student من نوع abtract فـ **لايمكن** كتابة:

		Student s = new Student();

يمكن للصنف من نوع abstract أن يحوي توابع abstract methods بمتن body أو توابع بدون متن.

مثال:

```java
//abstract class
public abstract class Person {
	
	private String name;
	private String gender;
	
	public Person(String nm, String gen){
		this.name=nm;
		this.gender=gen;
	}
	
	//abstract method
	public abstract void work();
	
	@Override
	public String toString(){
		return "Name="+this.name+"::Gender="+this.gender;
	}

	public void changeName(String newName) {
		this.name = newName;
	}	
}

```

مع ملاحظة هنا أن الدالة work من نوع abstract، ودائما عندما يكون لدينا دالة من هذا النوع فالـ class كله يجب أن يكون abstract بشكل إجباريّ، والعكس غير صحيح، أي ليس من الشرط على الـ  abstract class أن تحوي abstract methods

 

ومثال للتابع الوريث subclass:

```java
package com.journaldev.design;

public class Employee extends Person {
	
	private int empId;
	
	public Employee(String nm, String gen, int id) {
		super(nm, gen);
		this.empId=id;
	}

	@Override
	public void work() {
		if(empId == 0){
			System.out.println("Not working");
		}else{
			System.out.println("Working as employee!!");
		}
	}
	
	public static void main(String args[]){
		//coding in terms of abstract classes
		Person student = new Employee("Dove","Female",0);
		Person employee = new Employee("Pankaj","Male",123);
		student.work();
		employee.work();
		//using method implemented in abstract class - inheritance
		employee.changeName("Pankaj Kumar");
		System.out.println(employee.toString());
	}

}

```


الـ subclass **يجب أن** ينفّذ كل ال abstract methods، أي يعيد كتابتهم وملأهم بالتعليمات، إلّا إذا كان التابع الوارث subclass أيضا abstract class، وهذا هو تقريبا الفرق بين عمل extends لـ abstract class أو صنف عادي.

يمكن لل abtract class أن تحوي main methods

وظيفتها تقديم دالات مع أوامرها جاهزة افتراضيًا لاستخدامها بالتوابع الورثة.

## ملاحظات متفرقة

عندما يكون في الكلاس الرئيسي المُوَرِّث superclass دالة رئيسيّة (default method) تتطلب ٢ سترينع (نص) مثلًا، فيجب أن نكتب في أول سطر في الـدالة الرئيسية في الـتابع الوارث Subclaase دالة ()super، مثال:

		super("a", "b");


الدالات من نوع static بامكاننا أن نستدعيها من صنف آخر بدون انشاء عنصر من الصنف، أي بدلًا من كتابة:

```java
Student s = new Student();
s.hawa();
```
نكتب:


		Student.hawa();

المتغيرات من نوع final لايمكننا تغيير قيمتها


هل لديك سؤال أو معلومة إضافية؟ يرجى مشاركتنا إياها في التعليقات لإضافتها للنص الأصلي

## المراجع

* [Stackoverflow](https://stackoverflow.com/questions/10839131/implements-vs-extends-when-to-use-whats-the-difference)

* [Quora](https://www.quora.com/What-is-the-need-of-interface-in-Java)

* [stackoverflow](https://stackoverflow.com/questions/8064322/what-is-difference-to-extend-abstract-class-and-non-abstract-class)
* [journaldev](https://www.journaldev.com/1582/abstract-class-in-java)

