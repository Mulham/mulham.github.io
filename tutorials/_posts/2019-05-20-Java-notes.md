---
layout: post
date: 2019-05-20
title: ملاحظات جافا
type: tutorial
comments: true

---

* Toc
{:toc}


# interface class
الكلاسة من هالنوع تعرف أول الشي كالتالي:

		public interface Name

تحتوي على Methoden بدون body أي فقط تعريف للدالات على الشكل مثلا:

		public boolean add(String s);

وهذا النوع من ال methods الذي لا يحوي body يدعى abstract methods

وبالتالي :  Interface class is a collection of abstract methods

an interface may also contain constants (تعريف متغيرات مع قيمهم), default methods (Konstruktormethoden), static methods

الـ interface class بتحل مشكلة، وهو إن التوريث بالجافا غير ممكن ﻷكثر من كلاس، هذا يعني، **لاااا** يمكن كتابة:

		public class Name extends name1, name2{

ولكن **يمكن** كتابة

		public class Name implements name1, name2{

لماذا التوريث غير مسموح في الجافا؟ لعدم حصول مشاكل فعندما يكون لدينا كلاس تأخذ من كلاسين في نفس الوقت ويكون بين تلك الكلاسين تعارض فأي دالة أو أمر يجب أن ينفذ الكلاس الوريث؟ وبالتالي كلاسات ال interface لايمكن أن يحدث فيها تعارض ﻷنها لا تحوي تعليمات ضمن ال methoden
ولكن! ال interface يمكن أن تحوي contants متغيرات مع قيمهم، ولكن من الأفضل عدم استخدام هذه الميزة لعدم حصول تعارض كما ذكرنا، في حالة التعارض ستظهر  compiler error
ولن يتم بناء البرنامج

وظيفتها (الصورة لدي غير مكتلمة هنا) تعمل بشكل قالب بيحدد الوظائف اللي لازم تكون بالكلاسات التابعة.

مثال على كلاس interface وكلاس تابعة
{% highlight java %}
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
{% endhighlight %} 

 
*******

# Abtract class

نفس ال interface بس بتحوي تعليمات ضمن ال methods وكمان لا يمكن إنشاء عنصر object منها يعني عنا مثلا كلاس student من نوع abtract فـ **ما منحسن** نقول

		Student s = new Student();

 An abstract class can have an abstract method without body and it can have methods with implementation (with body) also.

مثال:

{% highlight java %}
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

{% endhighlight %} 

مع ملاحظة هنا الدالة work من نوع abstract ودائما بس عنا دالة من هالنوع التابع كله لازم يكون abstract إجباري، بس مو شرط للتابع abstract انو يحوي abstract methods

 

ومثال للتابع الوريث subclass:

{% highlight java %}
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

{% endhighlight %} 


الـ subclass **لازم ويجب أن** ينفذ كل ال abstract methods يعني يرجع يكتبن ويعبيهن بالتعليمات، إلا إذا كان ال subclass أيضا abstract class، وهاد تقريبا الفرق إذا عملنا extends ل abstract class أو كلاس عادية.

يمكن لل abtract class أن تحوي main methods

وظيفتها تقديم دالات مع أوامرها جاهزة افتراضيا لاستخدامها بالتوابع الورثة.

# ملاحظات متفرقة

عندما يكون في الكلاس الرئيسي superclass دالة اساسية (Konstruktormethode) تتطلب ٢ سترينع إجباري رح نكتب في الـ Subclaase دالة super، مثال:

		Super(" ", " ");


الدالات من نوع static بامكاننا نستدعيها من كلاس تاني بدون انشاء عنصر من الكلاس، يعني بدل ما نكتب:
		Student s = new Student();
		s.hawa()

منكتب


		Student.hawa();

المتغير من نوع final مامنحسن نغير قيمته



# المراجع

* [Stackoverflow](https://stackoverflow.com/questions/10839131/implements-vs-extends-when-to-use-whats-the-difference)

* [Quora](https://www.quora.com/What-is-the-need-of-interface-in-Java)

* [stackoverflow](https://stackoverflow.com/questions/8064322/what-is-difference-to-extend-abstract-class-and-non-abstract-class)
* [journaldev](https://www.journaldev.com/1582/abstract-class-in-java)



