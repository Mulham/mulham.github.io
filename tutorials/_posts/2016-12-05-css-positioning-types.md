---
layout: post
date: 2016-12-05
title: 5 أشياء قد لا تعرفها عن أنواع التوضّع في CSS
description: تقنيات CSS المعروفة منها والجديدة لتوضع العناصر 
type: tutorial
comments: true
tags: [إنترنت, تصميم, CSS]
feature: /assets/posts/css-code.jpg
caption: Image by StockSnap from Pixabay 
---

مرحباً ..
يمكن في هذه الأيام أن يقوم المطورون ببناء هيكليّة معقدة لصفحة الوب باستخدام تقنيات CSS المتعددة. لبعض هذه التقنيات تاريخ طويل (مثل floats)، بينما حاز البعض الآخر على الشعبية في السنوات الأخيرة (مثل flexbox).

سأقوم عزيزي القارئ في هذا المقال بإلقاء الضوء أكثر على تقنيات CSS الغير مشهورة تماماً والمتعلقة بطريقة تنسيق توضّع الحقول والمحتويات ضمن صفحة الوب.

ولكن قبل البدء بذلك دعنا نلقِ نظرة سريعة وضرورية على أنواع التوضّع المتاحة..

* Toc
{:toc}

# مراجعة ﻷنواع التوضّع المتاحة في CSS

تتيح لنا خاصية `position` في CSS تحديد نوع التوضّع لعنصر ما.

## خيارات خاصيّة التوضّع 'position'

إن القيمة الافتراضية لهذه الخاصية هي **static**. هذه القيمة تعني أن العنصر لم يتم تحديد موقعه، لتحديد توضعّه يجب تغيير هذه القيمة الافتراضية ﻷحد القيم التالية:

* `relative`

* `absolute`

* `fixed`

* `sticky`

يمكننا بعد ذلك استخدام خصائص الإزاحة لتحديد الموضع المطلوب للعنصر، وهذه الخصائص هي :

* `top`

* `right`

* `bottom`

* `left`

مع العلم أن القيمة المبدئيّة لهذه الخصائص هي `auto`

**مثال**: 

	div.relative {
	    position: relative;
	    right: 30px;
	    top: 10px;
	}

عليك دائماً أن تتذكر أن العنصر الذي تكون قيمة الخاصيّة `position` له هي `absolute` أو `fixed` يدعى العنصر المتوضّع بشكل مطلق/ أو العنصر مطلق التوضّع. يعني أنك لا يمكن أن تستخدم خصائص الإزاحة مع هذه القيم. لاحظ أيضاً أن العنصر المتوضّع يمكن أن يستخدم خاصيّة `z-index` والتي تحدد ترتيبه وأوليته في العرض (فوق الكل أم أسفل شيئ معين وما إلى ذلك، مثل ترتيب الطبقات في برامج التصميم).

## الاختلافات الرئيسية لخاصية التوضّع في CSS

دعنا الآن نناقش باختصار فروقات ثلاث رئيسية بين أنواع التوضّع المتاحة:

  * العنصر الذي تكون قيمة توضّعه absolute يكون محذوف بشكل كامل من العرض الطبيعي وتحتل مكانه العناصر المجاورة.

  * العنصر الذي تكون قيمة توضّعه relative أو sticky يحجز مكاناً خاصاً له ولا يمكن للعناصر المجاورة أن تحتل أي جزء من المساحة المجحوزة. ولكن إذا تم تطبيق أحد خصائص الإزاحة فإن هذه الإزاحة لا تحجز مكاناً خاصاً بحيث يتم تجاهلها من قبل باقي العناصر وقد يسبب ذلك تداخل العناصر فوق بعضها!

  * العنصر الذي تكون قيمة توضّعه fixed يتوضع دائماً بشكل ملائم للعرض (فيما عدا العناصر التي تحمل الخاصيّة `transform` والتي تدعمها جميع الإصدارات الأخيرة لمتصفحات الوب).

  * العنصر الذي تكون قيمة توضّعه sticky يتوضّع بشكل ملائم بالنسبة للعناصر المجاورة التي تحوي مربع التمرير (مثل خاصية `overflow: auto`). وإذا لم يتواجد مثل هذا العنصر فيتوضع بشكل ملائم للعرض.

أعرف أنك لم تفهم شيئأ .. وهذا ما أتوقعه أصلاً .. دعنا نجرب بشكل حي، فبالمثال والتجربة يزول الإشكال:

<p data-height="500" data-theme-id="0" data-slug-hash="vyjwWa" data-default-tab="result" data-user="mulham94" data-embed-version="2" data-pen-title="Overview of the available positioning types" class="codepen">See the Pen <a href="http://codepen.io/mulham94/pen/vyjwWa/">Overview of the available positioning types</a> by Mulham (<a href="http://codepen.io/mulham94">@mulham94</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

  > لا تزال وضعية التوضع sticky تعتبر تقنية تجريبية وتدعمها متصفحات محدودة فقط. يمكنك استخدام خاصية polyfill (مثل stickyfill) لإضافة هذه الميزة للمتصفحات التي لا تدعم sticky. 

# توضّع العناصر وفق النوع Absolute

قد يعرف الكثير منكم كيف يعمل هذا النوع من التوضّع، ولكن في بعض الأحيان يكون هذا النوع غير مفهوم ومربك للمصممين الجدد.

لهذا السبب قررت الحديث عنه في قائمة المفاهيم الغير معروفة كثيراً وإرفاق إطار للتجريب أيضاً.

وكما ذكرت سابقاً، العنصر الذي يكون نوع توضّعه absolute يكون عرضه ملائم لأقرب عنصر يحتويه. وطبعاً هذا في حالة أن العنصر الأب (الحاوي لعنصرنا من نوع absolute) لا يساوي نوع توضعه static. وبهذا، إن لم يكن لدى العنصر أي عنصر أب له قيمة توضع غير الافتراضية (static)، فسيتوضع هذا العنصر بشكل ملائم للعرض ككل.

لفهم ذلك أكثر دعنا نجرب هذا السلوك في العرض أدناه:

<p data-height="500" data-theme-id="0" data-slug-hash="dNKxae" data-default-tab="result" data-user="mulham94" data-embed-version="2" data-pen-title="Little-known thing #1 - Positioning elements with absolute positioning type" class="codepen">See the Pen <a href="http://codepen.io/mulham94/pen/dNKxae/">Little-known thing #1 - Positioning elements with absolute positioning type</a> by Mulham (<a href="http://codepen.io/mulham94">@mulham94</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

أعطينا في هذا العرض الصندوق الأخضر (الدائري) نوع توضّع مبدئي absolute مع قيم إزاحة `bottom:0` و `left:0`. كما لم نحدّد نوع التوضّع للعنصر الأب (الصندوق الأحمر). إلا أنّنا قمنا بتحديد توضّع الكود الخارجي (outer wrapper) مثل العنصر ضمن صنف `jumbotron`. لاحظ اختلاف توضّع الصندوق الأخضر باختلاف نوع التوضّع للعناصر الأب.

# تجاهل خاصية float للعناصر المتوضّعة بشكل مطلق

إذا كان العنصر يحوي خاصية float ليظهر إلى اليمين أو اليسار وقمنا بجعل نوعية توضّعه absolute أو fixed، فإن قيمة الخاصية float ستصبح `none` (يتم تجاهلها). وفي المقابل، فإذا جعلنا نوعيّة توضّعه relative فلن تتأثر قيمة float.


# العناصر المضمّنة المتوضّعة بشكل مطلق تكون كعناصر مستوى block


أي أن سلوكها كالعناصر التي تكون ككتلة، أي block-level .. غير واضح؟

العناصر المضمّنة التي يكون نوع توضّعها absolute أو fixed يكون لها خواص العناصر ذات المستوى block-level أي المستوى الأعلى وفي حال تعارض التوضّع فستوضع فوق العناصر ذات المستوى الأدنى. لإيضاح ذلك لدينا الجدول في الأسفل يلخِّص أنواع العناصر التي تُحوَّل إلى العناصر ذات مستوى block-level:

<p data-height="500" data-theme-id="0" data-slug-hash="OWwLBN" data-default-tab="result" data-user="mulham94" data-embed-version="2" data-pen-title="Little-known thing #3 - The inline elements which are absolutely positioned behave as block-level elements" class="codepen">See the Pen <a href="http://codepen.io/mulham94/pen/OWwLBN/">Little-known thing #3 - The inline elements which are absolutely positioned behave as block-level elements</a> by Mulham (<a href="http://codepen.io/mulham94">@mulham94</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

في هذه الحالة، قمنا بتعريف عنصرين مختلفين، الأوّل (الصندوق الأخضر) هو عنصر من متسوى block-level (مثل `div`) والثاني (الصندوق الأحمر) عنصر مضمّن (مثل `span`). وبالتالي لاحظ في البداية أن الصندوق الأخضر فقط هو الذي يظهر، بينما الأحمر غير ظاهر فعلياً ﻷننا أعطيناه عرض `width` وارتفاع `height` يمكن أن يُطبّقوا فقط على العناصر ذو المستوى block-level و inline-block، بالإضافة إلى أنه عنصر فارغ (لا يحوي عناصر ضمنه مثل مقطع نصي).

وعند جعل وضع التوضّع absolute أو fixed فإن العنصر (الأحمر) يظهر ﻷن سلوكه أصبح من مستوى block-level.

# الهوامش غير قابلة للطي في العناصر المتوضّعة بشكل مطلق

عند تلامس هامشان عموديان مع بعضهما فإنهما افتراضياً ينطويان ضمن هامش واحد تكون قيمتة محددّة بحسب قيمة الهامش الأكبر. يُعرف هذا السلوك باسم طيّ الهامش (margin collapsin).

وكما يحدث للهوامش في العناصر العائمة (ذات الخاصية float) فإن هوامش العناصر المتوضعة بشكل مطلق absolute لا تنطوي مع أي هامش آخر.

لنعاين المثال التالي:

<p data-height="500" data-theme-id="0" data-slug-hash="qRyBWG" data-default-tab="result" data-user="mulham94" data-embed-version="2" data-pen-title="Little-known thing #4 - The margins don’t collapse on absolutely positioned elements" class="codepen">See the Pen <a href="http://codepen.io/mulham94/pen/qRyBWG/">Little-known thing #4 - The margins don’t collapse on absolutely positioned elements</a> by Mulham (<a href="http://codepen.io/mulham94">@mulham94</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

يجوي العنصر في هذا المثال هامش يساوي `20px`، وإن هامشه العلوي `top` ينطوي (يتَّحد) مع الهامش العلوي `top` للعنصر الأب والذي قيمته أيضاً `20px`. وكما ترى، فعند اختيار نوع التوضع كمطلق absolute فإن الهامش `top` لا ينطوي مع الهوامش المناسبة للعناصر التي يقع ضمنها.

طبعاً واضح أن هذا السلوك هو المطلوب فنحن غالباً لا نريد للهوامش أن تتحد مع بعض.

**سؤال:** *كيف يمكنني منع الهوامش من الاتحاد؟*

حسناً .. يجب علينا وضع شيئ يمنعهم من ذلك. لنقل على سبيل المثال بعض الملء `padding` أو الحدود `border` (يجب علينا تطبيق ذلك على العناصر الرئيسية "الأب" أو "الابن" أي العناصر المُضمّنة). كما يوجد حل آخر وهو إضافة الصنف `clearfix` (والموجود في مثالنا) للعنصر الأب.

# توضّع العناصر بالبيكسل والنسب المئويّة

هل استخدمت سابقاً النسب المئويّة بدلاً من البيكسل لتحديد إزاحة عنصر ما؟ إذا كان جوابك نعم فربما لاحظت أن قيم الإزاحة المحسوبة تختلف بحسب وحدات CSS التي تختارها (بيكسل أو وحدة مئوية).

غير واضح؟ دعنا نرى أولاً ما يقوله الموقع الرسمي عن الإزاحات المعطاة بالنسب المئويّة:

> الإزاحة هي نسبة مئويّة لعرض الصندوق المحتوي للعنصر (`left` أو `right`) أو ارتفاعه (`top` أو `bottom`). بالنسبة للعناصر ذات التوضّع sticky فإن الإزاحة فيها هي النسبة المئويّة لتدفق عرض الجذر root (`left` أو `right`) أو ارتفاعه (`top` أو `bottom`).مسموح بالقيم السلبيّة كذلك.


أي أننا عندما نحدّد قيم الإزاحة بالنسب المئويّة، فإن مكان العنصر يتحدّد اعتماداً على العرض يميناً ويساراً (للإزاحات `left` و `right`) والارتفاع (للإزاحات `top` و `bottom`) للعنصر الأب.

يظهر المثال التالي هذا الاختلاف:

<p data-height="500" data-theme-id="0" data-slug-hash="qRyBMO" data-default-tab="result" data-user="mulham94" data-embed-version="2" data-pen-title="Little-known thing #5 - The difference between positioning elements with pixels and percentages" class="codepen">See the Pen <a href="http://codepen.io/mulham94/pen/qRyBMO/">Little-known thing #5 - The difference between positioning elements with pixels and percentages</a> by Mulham (<a href="http://codepen.io/mulham94">@mulham94</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

استخدمنا في هذا المثال البيكسل والنسب المئوية لتحريك العنصر. كن متأكداً بأنه عند تحديد الإزاحة بالبيكسل فإن العنصر يتحرك للمكان الذي نتوقعه.. جيد إلى هنا!

الآن عندما نختار السنب المئوية الوحدة CSS المطلوبة للإزاحة، فإن مكان العنصر سيعتمد على أبعاد العنصر الأب. في الأسفل رسم يبيّن حساب الموقع الجديد (بالنسب المئويّة):

<amp-img width="600" height="300" src="/assets/New_Position.png" alt="أنواع توضّع CSS"></amp-img>


**ملاحظة**: كما تعلم، فإن خاصية `transform` (بالإضافة لخصائص `translate` المختلفة) تتيح لنا أيضاً تغيرر موضع العنصر. ولكن يجب الانتباه إلى أنه عند اختيارنا للنسب المئويّة كوحدة CSS، فإن العنصر سيتوضّع وفقاً لأبعاده وليس وفقاً لأبعاد العنصر الأب (خلافاً للإزاحات).

# في النهاية ..

أتمنى أن يكون المقال أفادك .. لا تنسى .. عند وجود أي سؤال أو إضافة فيمكنك مراسلتي على البريد الظاهر في ترويسة جميع صفحات الموقع، أيضاً يمكنك فتح المناقشة وفق الرابط أدناه، كذلك يمكنك نشر الفائدة عبر مواقع التواصل :)

**هذه المقالة مترجمة وبتصرّف، يمكنك الاطلاع على [المصدر](https://scotch.io/bar-talk/5-things-you-might-not-know-about-the-css-positioning-types)**


