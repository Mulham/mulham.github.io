---
layout: post
title: أضف فانوس رمضان المتحرك لمدونتك
date: 2014-06-18
type: blog
comments: true
tags: [إنترنت, تصميم]
---


<center><img src="/assets/beautiful-islamic-ramadan-widget-for-blogger.png" title="أضف فانوس رمضان المتحرك لمدونتك" alt="أضف فانوس رمضان المتحرك لمدونتك"></center>

هنا تجد طريقة إضافة فانوس رمضان المتحرك أعلى يسار الصفحة في مدونات بلوجر، كما يمكن إضافته في أي موقع كان.


1. اذهب للوحة تحكم بلوجر

2. اذهب لصفحة "القالب" ثم اضغط على زر "تحرير HTML"

3. ابحث بالضغط على <kbd>Ctrl</kbd> + <kbd>F</kbd> عن السمة `</body>`
    
4. انسخ والصق الكود التالي **فوقها**

{% highlight HTML %}

     <!--  Ramadan Lantern taken from Mulham.github.io -->
    <div align='center'>
    <table border='0' cellpadding='0' cellspacing='0' width='900'>
    <tr>
    <td height='0' width='900'>
    <div style='float:top right; position:absolute; overflow:visible; left:45px; top:0px; height:192px; width:144px z-index: 9999;'><object border='0' classid='clsid:D27CDB6E-AE6D-11CF-96B8-444553540000' codebase='http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0' height='144' id='obj2' width='192'><param name='movie' value='http://netoopscodes.googlecode.com/svn/branches/swf/ramzan-hanging-lanterns.swf'/><param name='quality' value='High'/><param name='wmode' value='transparent'/><embed height='144' name='obj2' pluginspage='http://www.macromedia.com/go/getflashplayer' quality='High' src='http://netoopscodes.googlecode.com/svn/branches/swf/ramzan-hanging-lanterns.swf' type='application/x-shockwave-flash' width='192' wmode='transparent'/></object>
    </div>
    </td>
    </tr>
    </table>
    </div>
    <!--  End Ramadan Lantern taken from Mulham.github.io -->

{% endhighlight %}

 اضغط على حفظ النموذج ثم شاهد النتيجة مباشرة في مدونتك.
