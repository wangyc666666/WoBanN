function loadProperties(a){if("undefined"!=typeof jQuery.i18n)if($.isEmptyObject(jQuery.i18n.map)){var a=a||getlanguage();jQuery.i18n.properties({name:"main",path:"/Languages/",mode:"map",language:a,callback:function(){loadPropertiesForAsync("")}})}else loadPropertiesForAsync("")}function loadPlaceholder(a){$(a).each(function(){var a=$(this),b=jQuery.i18n.map[a.data("localizeph")],c=new Array;a.children().each(function(a,b){c[a+1]=$(this).html()});var b=b.formatPlaceholder(c);a.is("input[type=text]")||a.is("input[type=password]")||a.is("input[type=email]")||a.is("textarea")?a.attr("placeholder",b):a.is("input[type=button]")||a.is("input[type=submit]")?a.attr("value",b):a.html(b),$(this).removeAttr("data-localizeph")})}function loadForAsync(){var a=getlanguage();jQuery.i18n.properties({name:"main",path:"/Languages/",mode:"map",language:a,callback:function(){}})}function loadPropertiesForAsync(a){var b="",c="",d="";""!=a&&"undefined"!=typeof a?(b="#"+a+" [data-localize]",c="#"+a+" [data-localizetitle]",d="#"+a+" [data-localizeph]"):(b="[data-localize]",c="[data-localizetitle]",d="[data-localizeph]");var e=jQuery.i18n.map.sty_msg_dataprocessing;return""!=e&&"undefined"!=typeof e||loadForAsync(),$.isEmptyObject(jQuery.i18n.map)?"":($(b).each(function(){var a=$(this),b=jQuery.i18n.map[a.data("localize")];a.is("input[type=text]")||a.is("input[type=password]")||a.is("input[type=email]")||a.is("textarea")?a.attr("placeholder",b):a.is("input[type=button]")||a.is("input[type=submit]")?a.attr("value",b):a.text(b)}),$(c).each(function(){var a=$(this),b=jQuery.i18n.map[a.data("localizetitle")];a.attr("title",b)}),void loadPlaceholder(d))}function getCookie(a){for(var b=a+"=",c=document.cookie.split(";"),d=0;d<c.length;d++){for(var e=c[d];" "==e.charAt(0);)e=e.substring(1);if(e.indexOf(b)!=-1)return e.substring(b.length,e.length)}return""}function getlanguage(){var a=getCookie("COOKIE_LANGAGES");return""==a&&(a="zh"),a}function getDays(a,b){var c=new Date(a.formatDate("yyyy-MM-dd")),d=new Date(b.formatDate("yyyy-MM-dd"));return iDays=parseInt(Math.abs(c-d)/1e3/60/60/24),iDays}function GetDateStringForDate(a,b,c){var d="",e=substractDate(new Date,a),f=60,g=3600,h=86400;if(e<f){var i="";i="en"==c?" Seconds ago":"ha"==c?"秒鐘前":"秒钟前";var j=Math.round(e);j<1&&(j=1),d=j+i}else if(e<g){var i="";i="en"==c?" minutes ago":"ha"==c?"分鐘前":"分钟前",d=Math.round(e/f)+i}else if(e<h){var i="";i="en"==c?" hour ago":"ha"==c?"小時前":"小时前",d=Math.round(e/g)+i}else{var k=getDays(new Date,a);d=1==k?"en"==c?"Yday "+GetDateLang(a,4,c):"ha"==c?"昨天 "+GetDateLang(a,4,c):"昨天 "+GetDateLang(a,4,c):2==k?"en"==c?"DBY "+GetDateLang(a,4,c):"ha"==c?"前天 "+GetDateLang(a,4,c):"前天 "+GetDateLang(a,4,c):GetDateLang(a,b,c)}return d}function GetDateLang(a,b,c){if(null==a||""==a||"undefined"==typeof a)return"-";var d=typeof a;"string"==d&&(a=new Date(a.replace(/-/g,"/")));var e="";if(c.toLowerCase().indexOf("en")>-1)switch(b){case 1:e=a.formatDate("MMM dd,yyyy");break;case 10:e=GetDateStringForDate(a,1,c);break;case 2:e=a.formatDate("MMM dd,yyyy hh:mm TT");break;case 20:e=GetDateStringForDate(a,2,c);break;case 3:e=a.formatDate("MMM dd");break;case 30:e=GetDateStringForDate(a,3,c);break;case 4:e=a.formatDate("hh:mm TT")}else if(c.toLowerCase().indexOf("ha")>-1)switch(b){case 1:e=a.formatDate("yyyy-MM-dd");break;case 10:e=GetDateStringForDate(a,1,c);break;case 2:e=a.formatDate("yyyy-MM-dd HH:mm");break;case 20:e=GetDateStringForDate(a,2,c);break;case 3:e=a.formatDate("MM-dd");break;case 30:e=GetDateStringForDate(a,3,c);break;case 4:e=a.formatDate("HH:mm")}else switch(b){case 1:e=a.formatDate("yyyy-MM-dd");break;case 10:e=GetDateStringForDate(a,1,c);break;case 2:e=a.formatDate("yyyy-MM-dd HH:mm");break;case 20:e=GetDateStringForDate(a,2,c);break;case 3:e=a.formatDate("MM-dd");break;case 30:e=GetDateStringForDate(a,3,c);break;case 4:e=a.formatDate("HH:mm")}return e}String.prototype.formatPlaceholder=function(){if(0==arguments.length)return this;if(0==arguments[0].length)return this;for(var a=this,b=0;b<arguments[0].length;b++){var c="";""!=arguments[0][b+1]&&"undefined"!=typeof arguments[0][b+1]&&(c=arguments[0][b+1]),a=a.replace(new RegExp("\\{"+b+"\\}","g"),c)}return a},Date.prototype.formatDate=function(a){var b=this,c=function(a,b){b||(b=2),a=new String(a);for(var c=0,d="";c<b-a.length;c++)d+="0";return d+a};return a.replace(/"[^"]*"|'[^']*'|\b(?:d{1,4}|M{1,4}|yy(?:yy)?|([hHmstT])\1?|[lLZ])\b/g,function(a){switch(a){case"d":return b.getDate();case"dd":return c(b.getDate());case"ddd":return["Sun","Mon","Tue","Wed","Thr","Fri","Sat"][b.getDay()];case"dddd":return["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][b.getDay()];case"M":return b.getMonth()+1;case"MM":return c(b.getMonth()+1);case"MMM":return["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][b.getMonth()];case"MMMM":return["January","February","March","April","May","June","July","August","September","October","November","December"][b.getMonth()];case"yy":return new String(b.getFullYear()).substr(2);case"yyyy":return b.getFullYear();case"h":return b.getHours()%12||12;case"hh":return c(b.getHours()%12||12);case"H":return b.getHours();case"HH":return c(b.getHours());case"m":return b.getMinutes();case"mm":return c(b.getMinutes());case"s":return b.getSeconds();case"ss":return c(b.getSeconds());case"l":return b.getMilliseconds();case"ll":return c(b.getMilliseconds());case"tt":return b.getHours()<12?"am":"pm";case"TT":return b.getHours()<12?"AM":"PM"}})};var substractDate=function(a,b){var c=typeof a,d=typeof b;return"string"==c&&(a=new Date(a)),"string"==d&&(b=new Date(b)),(a-b)/1e3};