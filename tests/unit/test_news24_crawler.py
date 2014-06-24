# -*- coding: utf-8 -*-

import unittest

from dexter.models import Document
from dexter.models.support import db
from dexter.models.seeds import seed_db
from dexter.processing.crawlers import News24Crawler

class TestTimesliveCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = News24Crawler()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_canonicalise_url(self):
        self.assertEqual(self.crawler.canonicalise_url(
            'https://news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402'),
            'http://www.news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402')

    def test_extract_old_article_style_1(self):
        html = """



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://www.facebook.com/2008/fbml">
<head id="Head1"><meta name="description" content="Two men have been found guilty of raping a mother and daughter and killing the daughter, after breaking into their home to steal money for drugs. " /><script type='text/javascript'>(function(e){if(typeof e.za24_exk=='undefined')e.za24_exk=new Array;if(typeof e.za24_exkt=='undefined')e.za24_exkt=new Array})(window)
window.za24_exkt.push('weather');window.za24_exk.push('20');
</script><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><meta property="article:published_time" content="2014/04/02 10:17:46 AM"/><meta property="article:modified_time" content="2014/04/02 10:17:46 AM"/><meta property="article:expiration_time" content="2014/04/04 10:24:53 AM"/><meta property="twitter:card" content="summary"/><meta property="twitter:url" content="http://www.news24.com/SouthAfrica/News/Pair-found-guilty-of-rape-murder-20140402"/><meta property="twitter:title" content="Pair found guilty of rape, murder"/><meta property="twitter:site" content="News24"/><meta property="twitter:description" content="Two men have been found guilty of raping a mother and daughter and killing the daughter, after breaking into their home to steal money for drugs. "/><meta property="twitter:image" content="http://cdn.24.co.za/files/Cms/General/d/2721/a420a25fb557486785e98144d126f5d5.png"/><meta property="twitter:app:name:iphone" content="News24"/><meta property="twitter:app:id:iphone" content="310970460"/><meta property="twitter:app:name:ipad" content="News24"/><meta property="twitter:app:id:ipad" content="310970460"/><meta property="twitter:app:url:iphone" content="https://itunes.apple.com/za/app/news24/id310970460?mt=8"/><meta property="twitter:app:url:ipad" content="https://itunes.apple.com/za/app/news24/id310970460?mt=8"/><meta property="og:site_name" content="News24"/><meta property="fb:app_id" content="2363277980"/><meta property="fb:page_id" content="10227041841"/><meta property="og:title" content="Pair found guilty of rape, murder"/><meta property="og:type" content="article"/><meta property="og:url" content="http://www.news24.com/SouthAfrica/News/Pair-found-guilty-of-rape-murder-20140402"/><meta property="og:image" content="http://cdn.24.co.za/files/Cms/General/d/2679/2602089acbcd4e939480a21f0f1380d0.jpg"/><meta property="og:description" content="Two men have been found guilty of raping a mother and daughter and killing the daughter, after breaking into their home to steal money for drugs. "/><link rel="canonical" href="http://www.news24.com/SouthAfrica/News/Pair-found-guilty-of-rape-murder-20140402"/><script type="text/javascript" language="javascript">
var addthis_share =
{
url: "http://www.news24.com/SouthAfrica/News/Pair-found-guilty-of-rape-murder-20140402",
title: "Pair found guilty of rape, murder",
description: "Two men have been found guilty of raping a mother and daughter and killing the daughter, after breaking into their home to steal money for drugs.",
templates:
{
twitter: "{{title}}: {{url}} via @News24"
},
url_transforms: {
shorten: {
twitter: 'bitly'
}
},
shorteners: {
bitly: {
login: '24com',
apiKey: 'R_ca79efd5a0978fb80d1d853bac1dda83'
}}};
</script>
<title>
	Pair found guilty of rape, murder | News24
</title><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /><meta name="verify-v1" content="7Ni+Om+G5YH4bPtmBOm+5Qih2e8WRykbCvNJXRK9vbg=" /><meta name="bitly-verification" content="267098cc5a65" />   
     <!-- Mobile viewport optimized: j.mp/bplateviewport //-->
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <!-- For non-Retina iPhone, iPod Touch, and Android 2.1+ devices: -->
    <link rel="apple-touch-icon" href="../../images/ios/bookapple-touch-icon.png" />
     <!-- For first- and second-generation iPad: -->
    <link rel="apple-touch-icon" sizes="76x76" href="../../images/ios/bookapple-touch-icon-76x76.png" />
    <!-- For iPhone with high-resolution Retina display running iOS = 7: -->
    <link rel="apple-touch-icon" sizes="120x120" href="../../images/ios/bookapple-touch-icon-120x120.png" />
    <!-- For iPad with high-resolution Retina display running iOS = 7: -->
    <link rel="apple-touch-icon" sizes="152x152" href="../../images/ios/bookapple-touch-icon-152x152.png" /><link rel="SHORTCUT ICON" href="/favicon.ico" />
    <script type='text/javascript'>var _sf_startpt = (new Date()).getTime()</script>
    <link type="text/css" rel="stylesheet" href="http://static.24.co.za/5/styles/complete.css?v=20140319" /><link type="text/css" rel="stylesheet" href="http://scripts.24.co.za/libs/fancybox/jquery.fancybox.css?v=20140319" />
<!--[if gte IE 7]>
<link href="http://www.news24.com/Styles/ie7.css" type="text/css" rel="stylesheet">
<![endif]-->
<!--[if IE 7]><link href='http://www.news24.com/Styles/ie7.css' type='text/css' rel='stylesheet'><![endif]--><script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/minified/basescript1.js?v=20140319" ></script><script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/fancybox/fancybox-1.3.4.min.js?v=20140319" ></script>
    <script type="text/javascript">
        var $j = jQuery.noConflict();var isHomePage = false;document.domain = "news24.com";
    </script>
    
    <script sync type="text/javascript" src="http://scripts.24.co.za/libs/24com/portal/1.0/common.min.js?v=20140319"></script><script type="text/javascript">var _gaq = _gaq || [];_gaq.push(['_setDomainName', 'www.news24.com']);_gaq.push(['_setAccount', 'UA-45055449-1']);_gaq.push(['_trackPageview']);
                                    (function() {var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                                    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                                    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
                                    })();</script>
    
    
    <link id="alternateLink" rel="alternate" media="only screen and (max-width: 640px)" href="http://m.news24.com/news24/SouthAfrica/News/Pair-found-guilty-of-rape-murder-20140402"></link>
    

<meta name="keywords" content="johannesburg, crime" />
<meta name="news_keywords" content="johannesburg, crime" />
    <meta name="articleid" content="45517554-ffe3-4fea-bb92-0d02c82028d2"/>

<link href="http://scripts.24.co.za/libs/24com/comments/3.0.2/styles/comments.css" type="text/css" rel="stylesheet"></link>
<!-- Start of DClick Header -->
<!-- Site: /8900/24.com/Web/News24, Zone: /SouthAfrica/Articles, MapsTo: "News" -->

<script src='//www.googletagservices.com/tag/js/gpt.js' type='text/javascript' ></script>
<script src="http://scripts.24.co.za/libs/24com/Ads/3.0/24AdScript.min.js" language="JavaScript" type="text/javascript"></script>
<script language="JavaScript" type="text/javascript">//<![CDATA[
za24_AdSite = '/8900/24.com/Web/News24'; 
za24_AdZone = '/SouthAfrica/Articles';
za24_IsAsync  = false;
za24_InterstitialEnabled=true;
za24_KeywordType[1]='artid'; za24_Keywords[1]='45517554-ffe3-4fea-bb92-0d02c82028d2'; 
za24_KeywordType[2]='places'; za24_Keywords[2]='johannesburg'; 
za24_KeywordType[3]='topics'; za24_Keywords[3]='crime'; 

za24_AdSize[1]='1000x1000'; za24_AdPositionNo[1]='1'; 
za24_AdSize[2]='728x90'; za24_AdPositionNo[2]='1'; 
za24_AdSize[3]='300x600'; za24_AdPositionNo[3]='1'; 
za24_AdSize[4]='300x250'; za24_AdPositionNo[4]='1'; 
za24_AdSize[5]='468x120'; za24_AdPositionNo[5]='1'; 
za24_AdSize[6]='10x10'; za24_AdPositionNo[6]='1'; 
za24_AdSize[7]='278x76'; za24_AdPositionNo[7]='1'; 
za24_AdSize[8]='278x35'; za24_AdPositionNo[8]='1'; 
za24_AdSize[9]='200x400'; za24_AdPositionNo[9]='1'; 
za24_AdSize[10]='980x90'; za24_AdPositionNo[10]='1'; 
za24_InitAds();
//--></script>
<!-- End of DClick Header -->
</head>
<body>
    <!-- Start Alexa Certify Javascript -->
<script type="text/javascript">
    _atrk_opts = { atrk_acct: "qhC0h1agYe00yl", domain: "news24.com", dynamic: true };
    (function () { var as = document.createElement('script'); as.type = 'text/javascript'; as.async = true; as.src = "https://d31qbv1cthcecs.cloudfront.net/atrk.js"; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(as, s); })();
</script>
<noscript><img src="https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=qhC0h1agYe00yl" style="display:none" height="1" width="1" alt="" /></noscript>
<!-- End Alexa Certify Javascript -->
    <!-- COPYRIGHT EFFECTIVE MEASURE -->
    <script type="text/javascript">
        (function () {var em = document.createElement('script'); em.type = 'text/javascript'; em.async = true;
            em.src = ('https:' == document.location.protocol ? 'https://za-ssl' : 'http://za-cdn') + '.effectivemeasure.net/em.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(em, s);})();
    </script>
    <noscript><img src="http://za.effectivemeasure.net/em_image" alt="" style="position: absolute; left: -5px;" /></noscript>
    <!--END EFFECTIVE MEASURE CODE -->
    <form name="aspnetForm" method="post" id="aspnetForm">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJNTM2NzE1MzM3ZGQlVxP6ZJN+2XCtQmjsSfI0jMtiNQ==" />
</div>


<script type="text/javascript">
//<![CDATA[
var za24_displayAdUrl = 'http://www.news24.com/static/Ads/DisplayAd.html';//]]>
</script>

<div class="aspNetHidden">

	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAAZmtpz0Cx1/kbJO1rl1SO3UfLgYOaxGNxpcxlKlT9IObQH+ih4MEySCBlfYlvG/lO3w/h12H3MZPLcouy1JL6NJpTNihxCpIUCa2K/Ulzjx5fwGEjiXfG6Ja/hBBVaFQfSXBTON8y95OyLKox9y9pF3cg7LjA==" />
</div>
       
        <script type="text/javascript">
jQuery('head').append("<link href='http://scripts.24.co.za/libs/24com/ads/2.0/Style/TransAd.css?v=20140319' type='text/css' rel='stylesheet' ></link>")
</script>
<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/ads/2.0/script/TransAd.min.js?v=20140319"></script>
<script type="text/javascript">AdTemplate = "News24";</script>
<div id='ad-10x10-1' class='24ad10x10'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('10x10','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=10x10&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=10x10&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
        

<div id="leaderboard">
    <div class="adCenter">
        <div style="background-color:transparent;border-bottom:3px solid transparent;border-left:0px solid transparent;border-right:3px solid transparent;">
	        <div id='ad-728x90-1' class='24ad728x90'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('728x90','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=728x90&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=728x90&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
    </div>
    
</div>
        <div class="main_wrap relative">
            

            
    

<script type="text/javascript" language="text/javascript">
    jQuery(function () {
        var pushdown = jQuery("#pushDownAd");
        if (pushdown.height() < 20) { pushdown.css("display", "none") }
    });
</script>


<div class="grid_12">
    <div id="header" class="relative">
        <h1 id="news24HeaderLogo">
            <a href="http://www.news24.com/" title="News24.com Home">News24 News. Breaking News. First</a>
        </h1>
        

<div class="absolute update_time">LAST UPDATED: 2014-04-02, 10:21</div>
        <div class="div_0 absolute"></div>

        <div class="absolute">              
            <div class="header_featured_article">
    <div class="feature_head first absolute">
        <a href="http://voices.news24.com/kameel-premhid/2014/04/manuel-motlanthes-criticism-late/" id="lnkHeaderArtImage" target="_self"><img src="http://cdn.24.co.za/files/Cms/General/d/2670/5961bef8a9a4406a9f615f71a3c1bbfc.jpg" id="imgHeaderArticle" class="left" height="65" width="65" /></a>
        <h3 class="bold"><a href="http://voices.news24.com/kameel-premhid/2014/04/manuel-motlanthes-criticism-late/" data-track="outbound,home-header,topcompo-Manuel and Motlanthe\&#39;s criticism is too late" target="_self">Manuel and Motlanthe's criticism is too late</a></h3>
        <p>Trevor Manuel and Kgalema Motlanthe have both criticised the Zuma administration. Their sudden criticism comes too late, writes <strong>Kameel Premhid</strong>.</p>
    </div>
</div>

        </div>
        <div class="div_2 absolute"></div>

        
<div class="search_box absolute">
    <input id="txtSearchField" type="text" class="field absolute" onkeypress="var key=event.keyCode||event.which;if (key==13){submitSiteSearch(); return false;}" />
    <input type="submit" value="Search" class="btn absolute" onclick="submitSiteSearch(false);return false;" />   
</div>
<script type="text/javascript">
    var headerSearchUrl = 'http://www.news24.com/search?q={0}'; var headerAdvancedSearchUrl = 'http://googlesearch.news24.com/search?s=NWS&ref=NWS&q='; var txtSearchFieldClientId = "txtSearchField"; var btnSearchClientId = "btnSearch"; function submitSiteSearch() { var a = $j.trim($j("#" + txtSearchFieldClientId).val()); if (a.length > 0) { window.location.href = "/search?q=" + a } };
</script>
        

<div class="header_weather_box absolute">
    <div class="icon left">
    <a id="lnkModalItem" class="fireEventWeather weatherModal" style="display:none;"></a>
        <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=weather" id="lnkChangeWeather" class="city weatherModal" style="display: block">Cape Town</a>
        <img src="http://static.24.co.za/5/images/icons/forecastslarge/20.png" id="weatherImgMain" alt="Tons of rain. Morning clouds. Mild." />
    </div>
    <div class="div_3"></div>
    <div class="info left">
        <h2 id="mainTempDisplay">
            Wednesday
            <span>16-19&deg;C</span>
        </h2>
        <p id="mainDesc"><span id="spanMainDescription" style="cursor:default;" title="Tons of rain. Morning clouds. Mild.">Tons of rain. Morning clouds. Mild.</span></p>
        <ul id="weather_info_container">
            <li><a class="forecast absolute"  href="javascript:void(0)">7 day forecast</a> <!-- fire script here -->
                <ul id="weather_box_info" >
                    <li >
                        <table cellpadding="0" cellspacing="0" border="0" class="weather_drop_box">
                            
                                    <tr>
                                        <td class="d_day">Thursday</td>
                                        <td class="d_temp">16-22&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/2.png" alt="Mostly sunny. Mild." /></td>
                                        <td class="d_info">Mostly sunny. Mild.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Friday</td>
                                        <td class="d_temp">16-23&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/1.png" alt="Sunny. Mild." /></td>
                                        <td class="d_info">Sunny. Mild.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Saturday</td>
                                        <td class="d_temp">17-25&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/1.png" alt="Sunny. Warm." /></td>
                                        <td class="d_info">Sunny. Warm.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Sunday</td>
                                        <td class="d_temp">17-28&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/1.png" alt="Sunny. Pleasantly warm." /></td>
                                        <td class="d_info">Sunny. Pleasantly warm.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Monday</td>
                                        <td class="d_temp">21-29&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/2.png" alt="Mostly sunny. Warm." /></td>
                                        <td class="d_info">Mostly sunny. Warm.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Tuesday</td>
                                        <td class="d_temp">21-27&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/2.png" alt="More sun than clouds. Warm." /></td>
                                        <td class="d_info">More sun than clouds. Warm.</td>
                                    </tr>
                                
                            <tr>
                                <td colspan="4" height="10" valign="bottom" style="vertical-align:bottom">
                                    <div style="height:1px;border-bottom:1px solid #C6C6C6"></div>
                                    <div style="height:1px;border-top:1px solid #fff"></div>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="4" class="d_more_link" valign="top">
                                    <a href="http://weather.news24.com/sa/cape-town">More weather from Weather24 ></a>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="4" class="ad_link">
                                    <div id='ad-278x35-1' class='24ad278x35'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('278x35','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/Studio/SouthAfrica&sz=278x35&c=2056202428&t=artid%3d107354fc-e460-432f-8ec7-3519e4506df0%26Topics%3daprils+fool+joke%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/Studio/SouthAfrica&sz=278x35&c=2056202428&t=artid%3d107354fc-e460-432f-8ec7-3519e4506df0%26Topics%3daprils+fool+joke%26posno%3d1' border='0' alt=''></a></noscript>
                                </td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
    <div class="div_4"></div>
    <div class="left prodPlacement">        
        <a href="http://pubads.g.doubleclick.net/gampad/clk?id=44943070&iu=/8900/24.com/Web/News24" id="lnkHeaderWeatherSponsor" target="blank">Brought to<br />
        you by:<br />
        <img src="http://cdn.24.co.za/files/Cms/General/d/1655/d7d2b40e358940f09f295f9a9621f1ac.jpg" id="imgHeaderWeatherSponsor" width="66" height="9" border="0" /></a>
    </div>
</div>
<script type='text/javascript'>if(typeof(topStoriesArray)  != 'undefined') topStoriesArray.push({'name':'Cape Town Mostly sunny. Mild. 16-19','url':'http://weather.news24.com','icon':'/images/icons/Forecasts/2.ico'});</script>
        
<div class="nav_bar absolute" style="z-index:50">
    <ul id='nav' onmouseover='RemoveSelections();' onmouseout='SetSelections(defaultTabId);'>
<li class='nav_item ' id='tablink0' ><a href="http://www.news24.com/" data-track="outbound,nav,1stlevel-News">News</a>
<ul>
<li ><a  href="http://www.news24.com/SouthAfrica" data-track="outbound,nav,2ndlevel-South Africa">South Africa</a></li><li ><a  href="http://www.news24.com/Elections" data-track="outbound,nav,2ndlevel-Elections">Elections</a></li><li ><a  href="http://www.news24.com/World" data-track="outbound,nav,2ndlevel-World">World</a></li><li ><a  href="http://www.news24.com/Africa" data-track="outbound,nav,2ndlevel-Africa">Africa</a></li><li ><a  href="http://www.channel24.co.za" data-track="outbound,nav,2ndlevel-Entertainment">Entertainment</a></li><li ><a  href="http://www.news24.com/Green" data-track="outbound,nav,2ndlevel-Green">Green</a></li><li ><a  href="http://www.health24.com/news/1.asp" data-track="outbound,nav,2ndlevel-Health">Health</a></li></ul></li>
<li class='nav_item ' id='tablink1' ><a href="http://www.news24.com/Opinions" data-track="outbound,nav,1stlevel-Opinion">Opinion</a>
<ul>
<li><a href="http://voices.news24.com" data-track="outbound,nav,2ndlevel-Voices">Voices</a></li><li><a href="http://www.news24.com/MyNews24" data-track="outbound,nav,2ndlevel-MyNews24">MyNews24</a></li><li><a href="http://www.news24.com/Columnists" data-track="outbound,nav,2ndlevel-Columnists">Columnists</a></li></ul>
</li>
<li class='nav_item ' id='tablink2' ><a href="http://www.fin24.com" data-track="outbound,nav,1stlevel-Business">Business</a>
<ul>
<li ><a  href="http://www.fin24.com" data-track="outbound,nav,2ndlevel-News">News</a></li><li ><a  href="http://www.fin24.com/Markets" data-track="outbound,nav,2ndlevel-Markets">Markets</a></li><li ><a  href="http://www.fin24.com/Money/" data-track="outbound,nav,2ndlevel-Personal Finance">Personal Finance</a></li><li ><a  href="http://www.fin24.com/Opinion/Columnists/" data-track="outbound,nav,2ndlevel-Opinion">Opinion</a></li><li ><a  href="http://www.fin24.com/login" data-track="outbound,nav,2ndlevel-My Profile">My Profile</a></li></ul></li>
<li class='nav_item ' id='tablink3' ><a href="http://www.sport24.co.za" data-track="outbound,nav,1stlevel-Sport">Sport</a>
<ul>
<li ><a  href="http://www.sport24.co.za/" data-track="outbound,nav,2ndlevel-News">News</a></li><li ><a  href="http://www.sport24.co.za/Rugby/" data-track="outbound,nav,2ndlevel-Rugby">Rugby</a></li><li ><a  href="http://www.sport24.co.za/Cricket/" data-track="outbound,nav,2ndlevel-Cricket">Cricket</a></li><li ><a  href="http://www.sport24.co.za/Soccer/" data-track="outbound,nav,2ndlevel-Soccer">Soccer</a></li><li ><a  href="http://www.sport24.co.za/Golf/" data-track="outbound,nav,2ndlevel-Golf">Golf</a></li><li ><a  href="http://www.sport24.co.za/Tennis" data-track="outbound,nav,2ndlevel-Tennis">Tennis</a></li><li ><a  href="http://www.wheels24.co.za/FormulaOne/" data-track="outbound,nav,2ndlevel-Formula1">Formula1</a></li><li ><a  href=" http://www.sport24.co.za/OtherSport" data-track="outbound,nav,2ndlevel-Other Sport">Other Sport</a></li><li class='red'><a class='red' href="http://www.supersport.com/" data-track="outbound,nav,2ndlevel-SuperSport">SuperSport</a></li><li class='red'><a class='red' href="http://www.supersport.com/live-video" data-track="outbound,nav,2ndlevel-Live Streaming">Live Streaming</a></li><li class='red'><a class='red' href="http://www.supersport.com/video" data-track="outbound,nav,2ndlevel-Video Highlights">Video Highlights</a></li></ul></li>
<li class='nav_item no_arrow' id='tablink4' ><a href="http://www.news24.com/Technology" data-track="outbound,nav,1stlevel-Tech">Tech</a>
<li class='nav_item ' id='tablink5' ><a href="http://www.wheels24.co.za" data-track="outbound,nav,1stlevel-Motoring">Motoring</a>
<ul>
<li ><a  href="http://www.wheels24.co.za/news" data-track="outbound,nav,2ndlevel-News">News</a></li><li ><a  href="http://www.wheels24.co.za/NewModels/" data-track="outbound,nav,2ndlevel-New Models">New Models</a></li><li ><a  href="http://www.wheels24.co.za/4x4/" data-track="outbound,nav,2ndlevel-4x4">4x4</a></li><li ><a  href="http://www.wheels24.co.za/FormulaOne/" data-track="outbound,nav,2ndlevel-Formula One">Formula One</a></li><li ><a  href="http://www.wheels24.co.za/Motorsport/" data-track="outbound,nav,2ndlevel-Motorsport">Motorsport</a></li><li ><a  href="http://www.wheels24.co.za/BikesQuads/" data-track="outbound,nav,2ndlevel-Bikes">Bikes</a></li><li ><a  href="http://www.wheels24.co.za/Your-Wheels/" data-track="outbound,nav,2ndlevel-Your Wheels">Your Wheels</a></li></ul></li>
<li class='nav_item ' id='tablink6' ><a href="http://www.news24.com/Lifestyle" data-track="outbound,nav,1stlevel-Lifestyle">Lifestyle</a>
<ul>
<li ><a  href="http://www.health24.com/" data-track="outbound,nav,2ndlevel-Health">Health</a></li><li ><a  href="http://www.women24.com" data-track="outbound,nav,2ndlevel-Women">Women</a></li><li ><a  href="http://www.wheels24.co.za" data-track="outbound,nav,2ndlevel-Motoring">Motoring</a></li><li ><a  href="http://www.food24.com" data-track="outbound,nav,2ndlevel-Food">Food</a></li><li ><a  href="http://www.news24.com/Travel" data-track="outbound,nav,2ndlevel-Travel">Travel</a></li><li ><a  href="http://www.channel24.co.za/" data-track="outbound,nav,2ndlevel-Entertainment">Entertainment</a></li><li class='red'><a class='red' href="http://www.women24.com/rubybox" data-track="outbound,nav,2ndlevel-Shop Beauty">Shop Beauty</a></li><li ><a  href="http://www.parent24.com" data-track="outbound,nav,2ndlevel-Parent">Parent</a></li><li ><a  href="http://www.lazygamer.net" data-track="outbound,nav,2ndlevel-Games">Games</a></li><li class='red'><a class='red' href="http://www.mweb.co.za/games/Home.aspx?ref=news24nav" data-track="outbound,nav,2ndlevel-GameZone">GameZone</a></li><li class='red'><a class='red' href="http://love2meet.news24.com/s/" data-track="outbound,nav,2ndlevel-Dating">Dating</a></li></ul></li>
<li class='nav_item ' id='tablink7' ><a href="http://www.news24.com/Multimedia" data-track="outbound,nav,1stlevel-Multimedia">Multimedia</a>
<ul>
<li><a href="http://www.news24.com/multimedia" data-track="outbound,nav,2ndlevel-News">News</a></li><li><a href="http://www.sport24.co.za/multimedia" data-track="outbound,nav,2ndlevel-Sport">Sport</a></li><li><a href="http://www.channel24.co.za/Multimedia" data-track="outbound,nav,2ndlevel-Entertainment">Entertainment</a></li><li><a href="http://www.wheels24.co.za/multimedia" data-track="outbound,nav,2ndlevel-Motoring">Motoring</a></li><li><a href="http://www.women24.com/multimedia" data-track="outbound,nav,2ndlevel-Women">Women</a></li><li><a href="http://www.food24.com/multimedia" data-track="outbound,nav,2ndlevel-Food">Food</a></li><li><a href="http://www.parent24.com/multimedia" data-track="outbound,nav,2ndlevel-Parenting">Parenting</a></li><li><a href="http://www.news24.com/travel/multimedia" data-track="outbound,nav,2ndlevel-Travel">Travel</a></li><li><a href="http://www.health24.com/multimedia" data-track="outbound,nav,2ndlevel-Health">Health</a></li><li><a href="http://www.news24.com/multimedia/video" data-track="outbound,nav,2ndlevel-From our Studio">From our Studio</a></li></ul>
</li>
<li class='nav_item ' id='tablink8' ><a href="http://www.news24.com/SpecialReports" data-track="outbound,nav,1stlevel-Focus">Focus</a>
<ul>
<li><a href="http://www.news24.com/obituaries" data-track="outbound,nav,2ndlevel-Obituaries">Obituaries</a></li><li><a href="http://www.news24.com/Content/Africa/Zimbabwe" data-track="outbound,nav,2ndlevel-Zimbabwe">Zimbabwe</a></li><li><a href="http://www.health24.com/Medical/HIV-AIDS" data-track="outbound,nav,2ndlevel-Aids Focus">Aids Focus</a></li><li><a href="http://www.m24i.co.za/" data-track="outbound,nav,2ndlevel-Media24 Investigations">Media24 Investigations</a></li><li><a href="http://www.news24.com/Tags/Topics/good_news" data-track="outbound,nav,2ndlevel-Good News ">Good News </a></li><li><a href="http://www.citypress.co.za/" data-track="outbound,nav,2ndlevel-City Press">City Press</a></li><li><a href="http://www.news24.com/competitions" data-track="outbound,nav,2ndlevel-Competitions">Competitions</a></li></ul>
</li>
<li class='nav_item ' id='tablink9' ><a href="http://isizulu.news24.com" data-track="outbound,nav,1stlevel-isiZulu">isiZulu</a>
<ul>
<li><a href="http://isizulu.news24.com/NingizimuAfrika" data-track="outbound,nav,2ndlevel-Ningizimu Afrika ">Ningizimu Afrika </a></li><li><a href="http://isizulu.news24.com/Izindaba-Zami" data-track="outbound,nav,2ndlevel-Izindaba-Zami">Izindaba-Zami</a></li><li><a href="http://isizulu.news24.com/Ezemidlalo" data-track="outbound,nav,2ndlevel-Ezemidlalo">Ezemidlalo</a></li><li><a href="http://isizulu.news24.com/Afrika" data-track="outbound,nav,2ndlevel-Afrika">Afrika</a></li><li><a href="http://isizulu.news24.com/Umhlaba" data-track="outbound,nav,2ndlevel-Umhlaba">Umhlaba</a></li><li><a href="http://isizulu.news24.com/Ezokuzijabulisa" data-track="outbound,nav,2ndlevel-Ezokuzijabulisa">Ezokuzijabulisa</a></li><li><a href="http://isizulu.news24.com/Ezamabhizinisi" data-track="outbound,nav,2ndlevel-Ezamabhizinisi">Ezamabhizinisi</a></li></ul>
</li>
<li class='nav_item no_arrow' id='tablink10' ><a href="http://www.news24.com/Jobs/" data-track="outbound,nav,1stlevel-Jobs">Jobs</a>
<li class='nav_item no_arrow' id='tablink11' ><a href="http://www.news24.com/Property/" data-track="outbound,nav,1stlevel-Property">Property</a>
</ul>
<ul id='nav' onmouseover='RemoveSelections();' onmouseout='SetSelections(defaultTabId);'>
<li id='liContainer' class='sponsor_img'><a id='lnkSpecialNav' href='http://pubads.g.doubleclick.net/gampad/clk?id=51989710&iu=/8900/24.com/Web/News24' target='_self'><img id='lnkImg' src='http://cdn.24.co.za/files/Cms/General/d/2440/3f222735f4a746ab83d2b4d0b5955f73.gif' /></a>
<ul class='sponsor'>
<li class='sponsor-list-item'><a href='http://pubads.g.doubleclick.net/gampad/clk?id=57613510&iu=/8900/24.com/Web/News24' target='_self' data-track="outbound,nav,2ndlevel-Car Insurance">Car Insurance</a>
<li class='sponsor-list-item'><a href='http://pubads.g.doubleclick.net/gampad/clk?id=57613750&iu=/8900/24.com/Web/News24' target='_self' data-track="outbound,nav,2ndlevel-Home Insurance">Home Insurance</a>
<li class='sponsor-list-item'><a href='http://pubads.g.doubleclick.net/gampad/clk?id=57613990&iu=/8900/24.com/Web/News24' target='_self' data-track="outbound,nav,2ndlevel-Building Insurance">Building Insurance</a>
</ul>
</li>
</ul>

</div>
<script type='text/javascript'>menuJsonArray = [{"Url":"http://www.news24.com/SouthAfrica","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/Elections","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/World","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/Africa","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/Green","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://voices.news24.com","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/mynews24","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/columnists","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/Opinions","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/Technology","TabLinkIndex":4,"TabLinkToActivate":"tablink4"},{"Url":"http://www.news24.com/Travel","TabLinkIndex":6,"TabLinkToActivate":"tablink6"},{"Url":"http://love2meet.news24.com/s/","TabLinkIndex":6,"TabLinkToActivate":"tablink6"},{"Url":"http://www.news24.com/Lifestyle","TabLinkIndex":6,"TabLinkToActivate":"tablink6"},{"Url":"http://www.news24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.sport24.co.za/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.channel24.co.za/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.wheels24.co.za/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.women24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.food24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.parent24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/travel/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.health24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/multimedia/video","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/Multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/obituaries","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/africa/zimbabwe","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.health24.com/medical/hiv-aids","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.m24i.co.za/","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/tags/topics/good_news","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.citypress.co.za/","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/competitions","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/SpecialReports","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://isizulu.news24.com/ningizimuafrika","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/izindaba-zami","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/ezemidlalo","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/afrika","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/umhlaba","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/ezokuzijabulisa","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/ezamabhizinisi","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://www.news24.com/Jobs/","TabLinkIndex":10,"TabLinkToActivate":"tablink10"},{"Url":"http://www.news24.com/Property/","TabLinkIndex":11,"TabLinkToActivate":"tablink11"}];</script>

<script type="text/javascript" language="javascript">
    if ('False' == 'True')
        document.getElementById('main_nav').style.height = '33px';
</script>
    </div>
</div>
<div class="clear"></div>
<div id="pushDownAd">
    <div class="clear"></div>
    <div id='ad-980x90-1' class='24ad980x90'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('980x90','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=980x90&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=980x90&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>        
    <div class="clear"></div>
</div>
    <div class="container_12">
        <div class="clr10">&nbsp;</div>
        <div class="content_wrap socialnewsbasefix">
            <div class="left col640">
                
                
    <div id="article_special">
        

<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/article/1.0/articleGreyLinks.js"></script>
<script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/jquery.hoverintent.min.js?v=20140319" ></script>
<script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/jquery.cluetip.min.js?v=20140319" ></script>

<div class="article col626">
    
    <div class="spacer clr"></div>
	<h1 class="bold">Pair found guilty of rape, murder</h1>
	<span id="spnDate" class="block datestamp">2014-04-02 10:17</span>
	<div class="col300 right">
	    
	    <div class="spacer clr"></div>
        
        <div id="fb-root"></div>
<script type="text/javascript">
 (function (d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
 js.src = "//connect.facebook.net/en_GB/all.js#xfbml=1&appId=2363277980";
fjs.parentNode.insertBefore(js, fjs);
} (document, 'script', 'facebook-jssdk'));
</script>
<script type="text/javascript">
window.fbAsyncInit = function () {FB.Event.subscribe('edge.create', function (response) {
GA24.trackEvent('articles,sharelinks,fblike');
});};
var pinteresturl = '//assets.pinterest.com/js/pinit.js'
var twitterurl = '//platform.twitter.com/widgets.js'
var addthisurl ='//s7.addthis.com/js/250/addthis_widget.js#username=zamedia24'
$j.ajaxSetup({cache: true});
$j.getScript(pinteresturl)
$j.getScript(twitterurl)
$j.getScript(addthisurl,function(){
if(typeof(addthis) != 'undefined'){
$j('#article_toolbox_topright').show();
addthis.addEventListener('addthis.menu.share', function(evt) {
GA24.trackEvent('articles,sharelinks,' + evt.data.service);
});
}
});
$j.ajaxSetup({cache: false});
var addthis_config ={username: 'zamedia24',services_exclude: 'email,print',ui_open_windows: true,ui_language: 'en' };function googlePlusOneShareLink() {GA24.trackEvent('articles,sharelinks,googleplusone');
}function OpenPrintWindowShare() {var printUrl = 'http://www.news24.com/printArticle.aspx?iframe&aid=45517554-ffe3-4fea-bb92-0d02c82028d2&cid=1059';window.open(printUrl,'myPrintWindow','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=750,height=600');}</script><div class="spacer clr"></div>
<div id="article_toolbox_topright" style="border-bottom:solid #ebebeb 0px; border-top:solid #ffffff 1px; padding-left:0px;display:none;">
<div class="addthis_toolbox">
<a class="addthis_button_facebook_like" fb:like:action="recommend" fb:like:show_faces="false" fb:like:layout="button_count" fb:like:send="false"></a>
<a class="addthis_button_google_plusone" g:plusone:size="medium"></a>
<span><a href="http://pinterest.com/pin/create/button/?url=http://www.news24.com/SouthAfrica/News/Pair-found-guilty-of-rape-murder-20140402" class="pin-it-button" count-layout="horizontal">Pin It</a></span>
</div>
<div class="addthis_toolbox">
<a class="addthis_button_twitter"><span></span></a>
<a class="addthis_button_facebook"><span></span></a>
<a class="addthis_button at300b"><span></span></a>
<a class="email group" href="http://www.news24.com/sendToFriend.aspx?iframe&aid=45517554-ffe3-4fea-bb92-0d02c82028d2&cid=1059" title="Email"><span></span></a>
<a class="print" onclick="OpenPrintWindowShare()" title="Print"><span></span></a>
</div>
</div>
<div id="marging10Bottom"></div>

        <div class="spacer clr"></div>
	    

<script language="javascript" type="text/javascript">
    function popUP(url) {
        newwindow = window.open(url, 'name', 'height=800,width=500,scrollbars=yes,left=400');
        if (window.focus) { newwindow.focus() }
        return false;
    }
</script>

<div id="article_feature">
	<img id="image" title="" src="http://cdn.24.co.za/files/Cms/General/d/2679/2602089acbcd4e939480a21f0f1380d0.jpg" />
	<p class="text"> (<a href='http://www.shutterstock.com' target='_blank'>Shutterstock</a>)</p>
	<p class="bold">
	    <a id="lnkGalleries" href="http://www.news24.com/Multimedia">Multimedia</a>  &nbsp; · &nbsp; <a id="lnkUserGalleries" href="http://www.news24.com/Multimedia/MyNews24">User Galleries</a> &nbsp; · &nbsp; <a id="lnkNewsGalleries" href="http://www.news24.com/Multimedia/Category-Images">News in Pictures</a>
	    <span class="block red"><a class="group" href="http://uploads.news24.com?iframe">Send us your pictures</a>  &nbsp;·&nbsp; <a class="group" href="http://www.news24.com/FeedBack.aspx?iframe">Send us your stories</a></span>
	</p> 
</div>

	    <div class="spacer clr"></div>
        
        <div class="spacer clr"></div>	
	    

<script type="text/javascript">
    function scrollalert() { var a = $j("#scrollbox"); var b = $j("#scrollbox > #content"); if (a.length > 0) { if (a.length > 0 && a.scrollTop && b.height() <= a.scrollTop() + a.height() + 20) { $j("#imgAjaxLoad").show(); var data = { 'tag': $j("#hfTag").val(), 'tagGroup': $j("#hfTagGroup").val(), 'CurrentSiteId': "5", 'CmsArticleId': "45517554-ffe3-4fea-bb92-0d02c82028d2", 'index': $j("#hfBottomIndex").val(), 'selectedArticleIndex': $j("#hfSelectedArticleIndex").val(), 'directionToFetch': "Down" }; news24.getAjax("/Ajax/ArticleData/", "BuildArticleListByTag", data, onSuccessBottom, onFail) } setTimeout("scrollalert();", 500) } } function onSuccessBottom(a) { var b = parseInt($j("#hfBottomIndex").val()); if (a != "" && a != null) { $j("#hfBottomIndex").val(b + 5); setTimeout("$j('#imgAjaxLoad').hide();", 1e3); var c = $j("#RelatedLinks").html() + a; $j("#RelatedLinks").html(c) } else { setTimeout("$j('#imgAjaxLoad').hide();", 1e3); $j("#hfBottomIndex").val(-1) } } function onSuccessTop(a) { var b = parseInt($j("#hfTopIndex").val()); if (a != "" && a != null) { $j("#hfTopIndex").val(b - 5); setTimeout("$j('#imgAjaxLoad').hide();", 1e3); var c = a + $j("#RelatedLinks").html(); $j("#RelatedLinks").html(c); $j("#scrollbox").scrollTo("10") } else { setTimeout("$j('#imgAjaxLoad').hide();", 1e3); $j("#hfTopIndex").val(-1) } } function onFail() { } $j("document").ready(function () { scrollalert(); $j("#imgAjaxLoad").hide() })
</script>

<div id="relatedlinks_box">
    <div class="left"><h5 id="Relatedheader" class="bold">Related Links</h5><a id="taglink" class="relatedTag"></a></div>
    <div class="right"></div>
    <div class="clr"></div>
    
    
            <ul>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-Man held for rape, murder of girlfriend" href="http://www.news24.com/SouthAfrica/News/Man-held-for-rape-murder-of-girlfriend-20140108">Man held for rape, murder of girlfriend</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-Suspect denied bail in rape, murder case" href="http://www.news24.com/SouthAfrica/News/Suspect-denied-bail-in-rape-murder-case-20130306">Suspect denied bail in rape, murder case</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-Government clamps down on nyaope" href="http://www.news24.com/SouthAfrica/News/Government-clamps-down-on-nyaope-20140401">Government clamps down on nyaope</a></li>
        
            </ul>
        
    
    
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfTopIndex" id="hfTopIndex" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfBottomIndex" id="hfBottomIndex" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfTag" id="hfTag" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfTagGroup" id="hfTagGroup" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfSelectedArticleIndex" id="hfSelectedArticleIndex" />
</div>
	    

<div class=" rowdivider clr"></div>
<div class="kalahari_product left">
    <div id="pnlKalahariListing">
	
        
                <div>
                    <h4 class="left"><a href="http://etrader.kalahari.net/referral.asp?linkid=1869&partnerid=9113" target="_blank">kalahari.com</a></h4>
                    <ul class="left">
                        <li>
                            <a href="http://etrader.kalahari.net/referral.asp?linkid=5&amp;partnerid=9113&amp;sku=35274963" target="_blank">A Hedonist's Guide To... Johannesburg</a><br />
                            Explore the vibrant restaurants, bars and cultural life of Johannesburg before heading off for...
                            
                            Now R251.00
                            <br />
                            <a class="buynow" href="http://etrader.kalahari.net/referral.asp?linkid=5&amp;partnerid=9113&amp;sku=35274963" target="_blank">buy now</a>
                        </li>
                    </ul>
                </div>
            
    
</div>
    
</div>
<div class=" rowdivider clr"></div>
	    
        
	</div>
	<div class="ByLineWidth">
		<p class="left"></p>
	</div>
	<p class="clr_left"><p>Johannesburg - Two men have been found guilty of murder,
rape, and robbery, in the South Gauteng High Court sitting in Palm Ridge, <a href="http://www.iol.co.za/the-star" rel="" target="_self">The Star</a> reported on Wednesday.</p><p>Kyle Fredericks and Shinawaaz Ahmento, both aged 21, would
be sentenced on Wednesday by acting Judge Louis Vorster for murdering, raping,
and robbing Tracey-Lee Martins.</p><p>In April last year, the two broke into Martins's home in
Klipspruit West to rob her so they could get money for drugs, the paper
reported.</p><p>Ahmento raped Martins while she was in bed, then robbed her.
He was a frequent visitor at the house, the paper reported. </p><p>Fredericks strangled Martins with socks then threw the socks
down a drain.</p><p>Martins's son, who was aged 3 at the time, and his
74-year-old grandmother were also at the house at the time. Ahmento strangled
the older woman, who survived the attack, before robbing her as well.</p><p>The two then fled the scene, the paper reported.</p><p></p></p>
    
	<div id="_htmlAccreditationName">- SAPA</div>
	
	<p></p>
	


<div id="divKeywordsListing" class="read_more_slider">
    
            <b style="color:Gray">Read more on: &nbsp;&nbsp;</b>
        
            <b><a style="color:#0E2E5E;" href="/Tags/Places/johannesburg">johannesburg</a></b>                     
        &nbsp;|&nbsp;
            <b><a style="color:#0E2E5E;" href="/Tags/Topics/crime">crime</a></b>                     
        
</div>
    

<script type="text/javascript">
    function ReadMoreAction() { if ($j("div.read_more_slider").is(":inView") && !hidden) { $j("div#readMoreSlider").animate({ right: 0 }, 400); sliderVisible = true; isLoaded++; if (isLoaded == 1) { GA24.trackEvent("SouthAfrica-next-articlebox, show") } } } function HideReadMoreAction() { $j("div#readMoreSlider").animate({ right: -3e3 }, 400); sliderVisible = false } function CloseAction() { HideReadMoreAction(); hidden = true } var isLoaded = 0; var sliderVisible = false; var hidden = false; $j.extend($j.expr[":"], { inView: function (e) { return $j(e).offset().top + $j(e).height() <= $j(window).scrollTop() + $j(window).height() } }); $j(function () { setInterval("ReadMoreAction();", 500) }); $j(function () { var e = $j(window).scrollTop(); var t = e + $j(window).height(); var n = $j("div.read_more_slider").offset().top; var r = n + $j("div.read_more_slider").height(); return r <= t })
</script>
<div id="readMoreSlider">
    <div class="slider_title"><span>NEXT ON NEWS24</span><span class="right" style="cursor:pointer;" onclick="CloseAction()">X</span></div>
    <div class="slider_content">
        <a href='http://www.news24.com/SouthAfrica/News/Court-rules-against-Krejcir-on-Sars-affidavit-20140402' data-track="outbound,nextarticlebox"><img src="http://cdn.24.co.za/files/Cms/General/d/2609/a5ae9145e9b9403cbb8864ef30230e48.jpg" id="imgArticle" class="left" height="65" width="65" /></a>
	    <h4 class="bold"><a href='http://www.news24.com/SouthAfrica/News/Court-rules-against-Krejcir-on-Sars-affidavit-20140402' data-track="outbound,nextarticlebox" style="color:#fff;">Court rules against Krejcir on Sars affidavit</a></h4>
	    <div class="wrap_stampcomment" style="margin-top:10px;">
            <span class="block datestamp left" style="font-size:12px;color:#fff;">2014-04-02 09:02</span>
        </div>
    </div>
</div>
	<p></p>
    
</div>
<script type="text/javascript">
    $j(document).ready(function () { var a = $j("a.tips"); a.each(function () { var a = $j(this); a.attr("rel", "/Handlers/WhosWhoTooltip.ashx?url=" + a.attr("rel")) }); a.cluetip({ positionBy: "fixed", topOffset: "-230", leftOffset: "-30", sticky: true, dropShadow: false, showTitle: false, mouseOutClose: true, closeText: "", cluezIndex: 5100 }) })
</script>
        <div class="spacer clr">
            </div>
        

<script type="text/javascript" language="javascript">
	function openPrintWindow() {
		myPrintWindow = window.open('http://www.news24.com/printArticle.aspx?iframe&aid=45517554-ffe3-4fea-bb92-0d02c82028d2&cid=1059','myPrintWindow','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=750,height=600');
	}
</script>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#username=zamedia24"></script>
<div id="article_toolbox_bot" class="col626 left">
	<ul>
		<li class="email left" /><a class="group" href="http://www.news24.com/sendToFriend.aspx?iframe&aid=45517554-ffe3-4fea-bb92-0d02c82028d2&cid=1059">Email article</a>
		<li class="print left" /><a onclick="openPrintWindow()" href="#">Print article</a>
		<li class="get left" />GET NEWS24 ON: 
		<li class="mobile left" /><a href="http://mobile.24.com/?p=minisite_news">Your mobile</a>
		<li class="facebook left"/><a href="http://www.facebook.com/apps/application.php?api_key=90f449e533cd94a11213682bc9b2a23c">Your Facebook profile</a>
		<li class="clr" />
		<li class="share left" />SHARE:
		
	</ul>
	
	<div class="addthis_toolbox addthis_default_style">
	  <a class="addthis_button_facebook">Facebook</a>
	  <a class="addthis_button_twitter">Twitter</a>
	  <a class="addthis_button_google">Google</a>
	  <a class="addthis_button_digg">Digg</a>
	  <a class="addthis_button_delicious">Delicious</a>
	  <a class="addthis_button_yahoobkm">Yahoo</a>
	  <a class="addthis_button_compact" >More...</a>
	</div>
</div>
        <div class="spacer clr">
            </div>
        <div class="col620 adfix">
            <div id='ad-468x120-1' class='24ad468x120'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('468x120','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=468x120&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=468x120&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
        <div class="spacer clr">
            </div>
        <div class="col626">
            

<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/comments/3.0.2/scripts/comments.min.js"></script>
<script type="text/javascript" src="http://scripts.24.co.za/libs/json/json2.js"></script>
<script type="text/javascript">
    jQuery(function () {
        if (typeof onLogin !== "function") {
            jQuery.getScript("http://scripts.24.co.za/libs/24com/tina/1.0/LoginWindow.js");
        }
    });

    $j(function() {
        if (typeof commentControl !== "undefined") {
            // settings
            commentControl.sortOrder = "Asc";
            commentControl.pageSize = 20;
            commentControl.tinaBaseUrl = "http://auth.news24.com";
            commentControl.commentStatus = "Unmoderated";
            commentControl.lang = false ? "af" : "en";
            commentControl.locale = "en-za";
            commentControl.site = "News24";
            commentControl.breadCrumb = "News24|SouthAfrica|News" ;
            commentControl.objectId = "45517554-ffe3-4fea-bb92-0d02c82028d2";
            commentControl.isDev = false ;
            commentControl.canShowPostedComment = true ;
            commentControl.logOutUrl = "http://auth.news24.com/DeAuthenticate.aspx?surl=http://www.news24.com/SouthAfrica/News/Pair-found-guilty-of-rape-murder-20140402";
            commentControl.auth.user.id = "00000000-0000-0000-0000-000000000000";
            commentControl.auth.user.displayName = "";
            commentControl.auth.user.clickThrough = "";
            commentControl.auth.user.avatarUrl = "http://cdn.24.co.za/Files/RAP2/d/DefaultAvatar/Small.png";
            commentControl.auth.user.openIdType = 0 ;
            commentControl.FacebookHandlerUrl = "http://www.news24.com/FacebookToken.ashx";
            commentControl.cacheFacebookAvatar = true;
            commentControl.policyLink = "http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109";
            if (commentControl.auth.util.isFacebookProfile("")) {
                commentControl.auth.user.facebookProfileId = commentControl.auth.util.getFbProfileIdFromAvatarUrl("");
            }
            commentControl.init();
        }
    });
  
</script>
<p style="margin-bottom: 10px; margin-top: 5px;">
<a href="http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109">Read News24’s Comments Policy</a>
</p>



<div class="facebookComments">
    <p>24.com publishes all comments posted on articles provided that they adhere to our <a href="http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109" target="_blank" style="color:white;cursor:pointer;">Comments Policy</a>. Should you wish to report a comment for editorial review, please do so by clicking the 'Report Comment' button to the right of each comment.</p>
</div>
    <div id="comments_wrap">
        <div id="comment_on_story">
            <div class="fl">
                Comment on this story
            </div>
            <div class="xsmall normal to_lower fl" id="comment_count_wrap">
                <span id="lblTotalCommentCount">1</span>&nbsp;<span id="lblTotalCommentCountText">comment</span>
            </div>
            <div class="clr"></div>
        </div>

        
            <div class="comment_form_wrap" id="comment_article_form">
                <div class="comment_form_header to_upper bold">Add your comment</div>
                <div class="comment_form_result_msg bold hidden">Thank you, your comment has been submitted.</div>
                <div class="comment_form_user">
                    <div class="avatar_wrap fl">
                        <div><img alt="avatar" class="user_avatar_img" /></div>
                    </div>
                    <div class="author_name fl">
                        <a href="#" target="_blank" class="author_link bold user_name"></a>
                    </div>
                    <div class="logout_wrap fr">
                        <a href="#" class="smlr logout_link">Logout</a>
                    </div>
                    <div class="clr"></div>
                </div>
                <div class="comment_form_inner">
                    <span class="comment_form_label bold">Comment</span>
                    <span class="comment_form_remaining_text xsmall italic"><span>0</span> characters remaining</span>
                    <div class="textarea_wrap"><textarea rows="4"></textarea></div>
                    <div id="divFacebookCheckbox" class="facebook_checkbox">
                        <input type="checkbox" id="chk_facebook" checked="checked" /> <label for="chk_facebook" class="smlr">Share on Facebook</label>
                    </div>
                    <input type="button" value="Post Comment" class="button_submit to_upper smlr" />
                    <div class="ajax-loader hidden"></div>
                </div>
            </div>
        
        
        <div id="comments_list"></div>
        
        <div id="comment_reusables" class="hidden">
            <div class="comment_form_wrap" id="comment_reply_form">
                <div class="comment_form_header to_upper bold"></div>
                <div class="comment_form_user">
                    <div class="avatar_wrap fl">
                        <div><img alt="avatar" class="user_avatar_img" /></div>
                    </div>
                    <div class="author_name fl">
                        <a href="#" target="_blank" class="author_link bold user_name"></a>
                    </div>
                    <div class="logout_wrap fr">
                        <a href="#" class="smlr logout_link">Logout</a>
                    </div>
                    <div class="clr"></div>
                </div>
                <div class="comment_form_inner">
                    <span class="comment_form_label bold">Comment</span>
                    <span class="comment_form_remaining_text xsmall italic"><span>0</span> characters remaining</span>
                    <div class="textarea_wrap"><textarea rows="4"></textarea></div>
                    <div id="divFacebookCheckboxReply" class="facebook_checkbox">
                        <input type="checkbox" id="chk_facebook_reply" checked="checked" /> <label for="chk_facebook_reply" class="smlr">Share on Facebook</label>
                    </div>
                    <input type="button" value="Post Comment" class="button_submit to_upper smlr" />
                    <div class="ajax-loader hidden"></div>
                </div>
            </div>
        </div>

        <div id="comment_loader" class="hidden">
            <img src="http://scripts.24.co.za/libs/24com/comments/2.7/images/ajax-loader.gif" alt="Loading comments..." /> Loading comments...
        </div>

        <input type="button" id="btn_load_more" class="hidden to_upper smlr" value="Load More Comments" />
    </div>

        </div>
        <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/24com/contentrecommendation/2.0/keywordlogger.min.js?v=20140319" ></script>
<div id="other_stories" class="col626 left">
    <div id="googleAdContainer" style="float: left">
        <script type="text/javascript">
            google_ad_client = "pub-0710600889784454"; google_ad_slot = "5629899714"; google_ad_width = 336; google_ad_height = 280; $j(document).ready(function () { var data = { 'categoryBreadcrumb': 'SouthAfrica/News', 'articleId': '45517554-ffe3-4fea-bb92-0d02c82028d2' }; news24.getAjax("/Ajax/ArticleData/", "GetRecommendedArticles", data, function (res) { GetRecommendedArticlesCallback(res) }) }); function GetRecommendedArticlesCallback(res) { if (!res.error && res != "error") $j('#contentDiv').html(res); else $j('#contentDiv').remove() }
        </script>
        <script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
    </div>
    <div id="contentDiv" class="right" style="width:277px;padding-bottom:10px;"></div>
    <div class="clr"></div>
</div>
        <div class="spacer clr">
            </div>
        <div class="spacer clr">
            </div>
        
<iframe src="http://b.wm.co.za/24com.php?location=N&layout=wide" id="ifrWide" frameborder="0" width="630" height="152" scrolling="no" style="margin-left:-8px"></iframe>
<div class="clr10">&nbsp;</div>
        <div class="spacer clr">
            </div>
        <div id="divToHide">
    <div id="inside_news" class="col626 left">
    <h2 class="bold">Inside News24</h2>
	    <div id="wrap_carousel" class="relative block">
	      
		      <ul id="carousel" class="absolute">
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.women24.com/LoveAndSex/SexAndSizzle/Aftersex-selfie-trend-goes-viral-on-instagram-users-grossed-out-20140401" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2725/59f3146eb1d8497fa52ee59c58c44b9f.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.women24.com/LoveAndSex/SexAndSizzle/Aftersex-selfie-trend-goes-viral-on-instagram-users-grossed-out-20140401" data-track="outbound,home,inside-#Aftersex selfie? Ew!" target="_self">#Aftersex selfie? Ew!</a></h4>
                    <p>This is what happens when over sharing goes too far.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.news24.com/Travel/Multimedia/kululas-braai-in-the-sky-20140402" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2725/857226802ae148c791365c7c43b5a545.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.news24.com/Travel/Multimedia/kululas-braai-in-the-sky-20140402" data-track="outbound,home,inside-kulula\&#39;s sky braai" target="_self">kulula's sky braai</a></h4>
                    <p>We thought they were crazy, but kulula actually did it! Watch this video.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.food24.com/Drinks/Coffee" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2725/95a77f113aa84252bf20a119fa5757f1.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.food24.com/Drinks/Coffee" data-track="outbound,home,inside-Best coffees in Cape Town" target="_self">Best coffees in Cape Town</a></h4>
                    <p>A comprehensive list of great coffee shops in Cape Town. </p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.channel24.co.za/Gossip/News/8-very-real-emotions-we-all-experienced-when-we-found-out-that-Gareth-Cliff-was-leaving-5FM-20140331" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2724/50195a487b6d452cb351aa11856d8e22.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.channel24.co.za/Gossip/News/8-very-real-emotions-we-all-experienced-when-we-found-out-that-Gareth-Cliff-was-leaving-5FM-20140331" data-track="outbound,home,inside-Gareth is gone!" target="_self">Gareth is gone!</a></h4>
                    <p>8 emotions we all experienced. </p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.parent24.com/Teen_13-18/health_safety/Teen-addicted-to-selfies-attempts-suicide-20140328" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2670/ccd03e657bd74438a2e53b10586db97e.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.parent24.com/Teen_13-18/health_safety/Teen-addicted-to-selfies-attempts-suicide-20140328" data-track="outbound,home,inside-Addicted to selfies" target="_self">Addicted to selfies</a></h4>
                    <p>Selfie obsessed teen attempts to commit suicide.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.health24.com/Lifestyle/Environmental-health/News/Chinese-parents-offer-babies-for-adoption-on-internet-20140331" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2723/4dfefd798394492d8389468d2a8ec170.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.health24.com/Lifestyle/Environmental-health/News/Chinese-parents-offer-babies-for-adoption-on-internet-20140331" data-track="outbound,home,inside-Babies on offer" target="_self">Babies on offer</a></h4>
                    <p>Chinese parents are offering their babies for adoption on the internet.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.news24.com/Multimedia/Video/SouthAfrica/Top-5-April-Fools-jokes-20140401" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2724/8bcec918b7034cf39befd67b824cd914.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.news24.com/Multimedia/Video/SouthAfrica/Top-5-April-Fools-jokes-20140401" data-track="outbound,home,inside-Top 5 April Fools\&#39; jokes" target="_self">Top 5 April Fools' jokes</a></h4>
                    <p> We round up our top five April Fools' pranks. Watch.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.news24.com/Travel/Multimedia/Crazy-kayak-waterfall-drop-20140331" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2723/c1bb60ef40fe4582a88fdd61f1872cba.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.news24.com/Travel/Multimedia/Crazy-kayak-waterfall-drop-20140331" data-track="outbound,home,inside-Crazy kayaker!" target="_self">Crazy kayaker!</a></h4>
                    <p>Insane GoPro footage of a kayaker doing an 18-metre drop. </p>
		        </div>
		      </li>
	        
	          </ul>
	        
	    </div>
    </div>	
    <div id="" class="left col13"> </div>
</div>
<div class="clr">&nbsp;</div>


        <div class="spacer clr">
            </div>
        

<div id="promotion_box" class="left col626">
    <div id='ad-1x1-1' class='24ad1x1'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('1x1','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=1x1&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=1x1&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
</div>
    </div>

            </div>
            <div id="right_column" class="grey_grad left col299">
                
    <div class="personallogin">
        <div id="PanelLogIn">
	
    <div class="welcome">
        <h2 class="bold">Welcome to News24</h2>
        <div class="login_block"><a href="javascript:void(0)" class="submit_button">Login | Sign Up</a></div>
    </div>
    <div class="clr"></div>
    

<div class="uploadblack">
    <div class="blackblock_heading">Get Published!</div>
    <div class="blackblock_upload"><strong>UPLOAD</strong></div>
    <div class="blackblock_icons">
        <a class="tooltip call2action" href="http://uploads.news24.com/#story">
            <img width="24" height="24" border="0" alt="" src='http://static.24.co.za/5/images/profile/article_icon.jpg'>
            <span><b>Click here<br>to upload<br>your article</b></span>
        </a>
        <a class="tooltip call2action" href="http://uploads.news24.com/#images">
            <img width="24" height="24" border="0" alt="" src='http://static.24.co.za/5/images/profile/camera_icon.jpg'>
            <span><b>Click here<br />to upload<br />your photo</b></span>
        </a>
        <a class="tooltip call2action" href="http://uploads.news24.com/#videos">
            <img width="24" height="24" border="0" alt="" src='http://static.24.co.za/5/images/profile/video_icon.jpg'>
            <span><b>Click here<br>to upload<br>your video</b></span>
        </a>
    </div>
</div>

</div>


        <div class="clr">
        </div>
    </div>
    

<script language="javascript" type="text/javascript">
    var tabsClass = { tabSetArray: new Array, classOn: "tabs_on", classOff: "tabs_off", addTabs: function (a) { tabs = document.getElementById(a).getElementsByTagName("div"); for (x in tabs) { if (typeof tabs[x].id != "undefined") { this.tabSetArray.push(tabs[x].id) } else { } } }, switchTab: function (a) { for (x in this.tabSetArray) { tabItem = this.tabSetArray[x]; dataElement = document.getElementById(tabItem + "_data"); if (dataElement) { if (dataElement.style.display != "none") { dataElement.style.display = "none" } else { } } else { } tabElement = document.getElementById(tabItem); if (tabElement) { if (tabElement.className != this.classOff) { tabElement.className = this.classOff } else { } } else { } } document.getElementById(a.id + "_data").style.display = ""; a.className = this.classOn } }
</script>

<div id="most_box" class="col299 tabs">
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td>
                <div id="mostTabContainer" class="localised tabNavigation tab-menu">
	                <div id="tab_read" class="tabs_on left" onmouseover="tabsClass.switchTab(this);">Most Read</div>
                    <div id="tab_comment" class="tabs_off left" onmouseover="tabsClass.switchTab(this);">Most Commented</div>
                    <div id="tab_area" class="tabs_off left" onmouseover="tabsClass.switchTab(this);">News In Your Area</div>
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <div id="tab_read_data" class="tab-wrapper">
                    <ul class="bold">
                            <li><a data-track="outbound,mostread,mostread-Top 5 April Fools\&#39; jokes" href="http://www.news24.com/Multimedia/Video/SouthAfrica/Top-5-April-Fools-jokes-20140401">Top 5 April Fools' jokes</a><span class='watch'><a href='http://www.news24.com/Multimedia/Video/SouthAfrica/Top-5-April-Fools-jokes-20140401'>watch</a></span></li>
                        
                            <li><a data-track="outbound,mostread,mostread-This man says he knows what happened to Flight MH370" href="http://www.news24.com/Travel/Flights/This-man-says-he-knows-what-happened-to-Flight-MH370-20140328">This man says he knows what happened to Flight MH370</a></li>
                        
                            <li><a data-track="outbound,mostread,mostread-DA takes on Nkandla in April Fools joke" href="http://www.news24.com/Elections/News/DA-takes-on-Nkandla-in-April-Fools-joke-20140401">DA takes on Nkandla in April Fools joke</a></li>
                        
                            <li><a data-track="outbound,mostread,mostread-Top 5 Sexiest Women in Sport" href="http://www.sport24.co.za/Multimedia/Babes-in-Sport/Top-5-Sexiest-Women-in-Sport-20140401">Top 5 Sexiest Women in Sport</a><span class='watch'><a href='http://www.sport24.co.za/Multimedia/Babes-in-Sport/Top-5-Sexiest-Women-in-Sport-20140401'>watch</a></span></li>
                        
                            <li><a data-track="outbound,mostread,mostread-8 emotions we all experienced when we found out that Gareth Cliff was leaving 5FM" href="http://www.channel24.co.za/Gossip/News/8-very-real-emotions-we-all-experienced-when-we-found-out-that-Gareth-Cliff-was-leaving-5FM-20140331">8 emotions we all experienced when we found out that Gareth Cliff was leaving 5FM</a></li>
                        </ul>
                    <div class="spacer clr"></div>
                    <a id="lnkReadMore" Class="lnkMore" href="http://www.news24.com/TopStories">More..</a>
                </div>
                <div id="tab_comment_data" class="tab-wrapper" style="display: none;">
                    <div class="clr"></div>
                    <ul class="bold">
                            <li><a data-track="outbound,mostread,mostcommented-ANC takes DA to court over SMSes" href="http://www.news24.com/Elections/News/ANC-takes-DA-to-court-over-SMSes-20140402">ANC takes DA to court over SMSes</a></li>
                        
                            <li><a data-track="outbound,mostread,mostcommented-Zille accepts \&#39;elecnomination\&#39; challenge" href="http://www.news24.com/Elections/News/Zille-accepts-elecnomination-challenge-20140331">Zille accepts 'elecnomination' challenge</a></li>
                        
                            <li><a data-track="outbound,mostread,mostcommented-ANC distances itself from Nkandla" href="http://www.news24.com/SouthAfrica/Politics/ANC-distances-itself-from-Nkandla-20140331">ANC distances itself from Nkandla</a></li>
                        
                            <li><a data-track="outbound,mostread,mostcommented-Zuma an immoral agent unfit to lead SA - UDM" href="http://www.news24.com/Elections/News/Zuma-an-immoral-agent-unfit-to-lead-SA-UDM-20140331">Zuma an immoral agent unfit to lead SA - UDM</a></li>
                        
                            <li><a data-track="outbound,mostread,mostcommented-Zuma\&#39;s Nkandla comments \&#39;an insult\&#39;" href="http://www.news24.com/SouthAfrica/Politics/Zumas-Nkandla-comments-an-insult-20140331-2">Zuma's Nkandla comments 'an insult'</a></li>
                        </ul>
                    <div class="spacer clr"></div>                        
                    <a id="lnkCommentMore" Class="lnkMore" href="http://www.news24.com/TopStories">More..</a>
                </div>
                <div id="tab_area_data" class="tab-wrapper" style="display: none;">
                    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=mostread" id="lnkModalDisplay" class="userLocationModal right change_link">[change area]</a>
                    <h4 class="left most_head bold">News in Cape Town</h4>
                    <div class="clr"></div>
                    <ul class="bold">
                            <li><a data-track="outbound,mostread,mostreadarea-Retired  MP travel benefits not ANC idea - chief whip" href="http://www.news24.com/SouthAfrica/Politics/Retired-MP-travel-benefits-not-ANC-idea-chief-whip-20140401">Retired  MP travel benefits not ANC idea - chief whip</a></li>
                        
                            <li><a data-track="outbound,mostread,mostreadarea-Arms committee failed to table report - DA" href="http://www.news24.com/SouthAfrica/Politics/Arms-committee-failed-to-table-report-DA-20140401">Arms committee failed to table report - DA</a></li>
                        
                            <li><a data-track="outbound,mostread,mostreadarea-Top cop apologises to Khayelitsha residents" href="http://www.news24.com/SouthAfrica/News/Top-cop-apologises-to-Khayelitsha-residents-20140401">Top cop apologises to Khayelitsha residents</a></li>
                        
                            <li><a data-track="outbound,mostread,mostreadarea-Cape Town women in court for R2m fraud" href="http://www.news24.com/SouthAfrica/News/Cape-Town-women-in-court-for-R2m-fraud-20140401">Cape Town women in court for R2m fraud</a></li>
                        
                            <li><a data-track="outbound,mostread,mostreadarea-Journalist to appeal dismissal over DA MP application" href="http://www.news24.com/Elections/News/Journalist-to-appeal-dismissal-over-DA-MP-application-20140401">Journalist to appeal dismissal over DA MP application</a></li>
                        </ul>
                </div>
                <script type="text/javascript">
                      tabsClass.addTabs("mostTabContainer");
			    </script>
            </td>
        </tr>
        <tr>
            <td>
                <div class="ad278X35 outsurance"><!-- outsurance Ad -->
	                <div id='ad-278x76-1' class='24ad278x76'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('278x76','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=278x76&c=1281501862&t=artid%3d7206864e-3b57-4565-b85d-1c298028909c%26Places%3djohannesburg%26Topics%3deducation%2ccrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=278x76&c=1281501862&t=artid%3d7206864e-3b57-4565-b85d-1c298028909c%26Places%3djohannesburg%26Topics%3deducation%2ccrime%26posno%3d1' border='0' alt=''></a></noscript>
                </div>
            </td>
        </tr>
    </table>
    <a id="lnkModalItem" class="fireEventMost locationModal" style="display:none;"></a>
</div>

    <div class="spacer clr">
        </div>
    <div class="ad300X600 col300">
        <div id='ad-300x600-1' class='24ad300x600'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('300x600','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=300x600&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=300x600&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
    </div>
    <div class="spacer clr">
        </div>
    
    <div class="spacer clr">
        </div>
    
    <div class="spacer clr">
        </div>
    <div id="fb_social"></div>
<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/SocialNews/3.0/scripts/socialnews.min.js?v=20140319" type="text/javascript"></script>
<script type="text/javascript" >
jQuery('head').append('<link rel="stylesheet" href="http://scripts.24.co.za/libs/24com/SocialNews/3.0/styles/socialnews.css?v=20140319" type="text/css" />');
jQuery(document).ready(function(){
FBSocialNews.settings.siteDomain="www.news24.com";
FBSocialNews.settings.parentDomain="www.news24.com";
FBSocialNews.settings.activityServiceUrl="http://fbactivity.24.com/";
FBSocialNews.settings.appID="2363277980";
FBSocialNews.settings.tinaBaseUrl="http://auth.news24.com";
FBSocialNews.settings.isArticle=true;
FBSocialNews.settings.actionType='read';
FBSocialNews.settings.overrideFriendActivity=false;
if(typeof LanguageResource != 'undefined')FBSocialNews.settings.language=LanguageResource.languages.eng;
FBSocialNews.userProfile.hasPermission=false;
FBSocialNews.init();
});
</script>
<div class="clr socialspacer"></div>
<a href="/SocialSharingPopup.aspx" class="iframe socialSharePopup" style="display:none;"></a>

    <div class="spacer clr">
        </div>
    
    
    

<script language="javascript" type="text/javascript">
    $j(document).ready(function () { var a = "capetown"; if (a == "" || a == "default") { $j("#tab_traffic_data").attr("class", "tab-wrapper") } }); var tabsInfoClass = { tabInfoSetArray: new Array, classOn: "tabs_on left", classOff: "tabs_off left", addTabs: function (a) { tabs = document.getElementById(a).getElementsByTagName("div"); for (x in tabs) { if (typeof tabs[x].id != "undefined") { this.tabInfoSetArray.push(tabs[x].id) } else { } } }, switchTab: function (a) { for (x in this.tabInfoSetArray) { tabItem = this.tabInfoSetArray[x]; dataElement = document.getElementById(tabItem + "_data"); if (dataElement) { if (dataElement.style.display != "none") { dataElement.style.display = "none" } else { } } else { } tabElement = document.getElementById(tabItem); if (tabElement) { if (tabElement.className != this.classOff) { tabElement.className = this.classOff } else { } } else { } } document.getElementById(a.id + "_data").style.display = ""; a.className = this.classOn } }
</script>

<div class="clr10">&nbsp;</div>
<div id="weather_box" class="col299 relative tabs2">
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td>
                <div id="infoTabContainer" class="tabNavigation tab-menu">
                    <div id="tab_traffic" class="tabs_on left" onmouseover="tabsInfoClass.switchTab(this);">Traffic</div>
                    <div id="tab_lottery" class="tabs_off left" onmouseover="tabsInfoClass.switchTab(this);">Lottery</div>
                </div>
            </td>
        </tr>
        <tr>
            <td class="relative">
                <div id="tab_traffic_data" class="tab-wrapper-beta">

<div id="traffic_box">
    <div class="traffic_header">
        <!--<h3 class="bold left">Traffic</h3>//-->
        <div class="dropdown left"><select id='ddlTrafficRegions'><option value='' >Select region..</option><option value='Gauteng' >Gauteng</option><option value='Western Cape' selected='selected'>Western Cape</option><option value='KwaZulu-Natal' >KwaZulu-Natal</option><option value='Free State' >Free State</option><option value='Northern Cape' >Northern Cape</option><option value='Limpopo' >Limpopo</option><option value='Eastern Cape' >Eastern Cape</option><option value='Mpumalanga' >Mpumalanga</option><option value='North West' >North West</option></select></div>
    </div>
    <div class="traffic_container">
        <div class="clr5 clr">&nbsp;</div>
        <div id="trafic-container" class="left">
            <ul><li><span class='day'>Wednesday</span>&nbsp;<span class='location'>Cape Town - 10:04 AM</span><br/><span class='road'>Road name: N1 Inbound</span><br/><span class='description'>SLOW TRAFFIC between Lower Church Street and the Waterfront exit via the Elevated Freeway</span></li><li><span class='day'>Wednesday</span>&nbsp;<span class='location'>Cape Town - 09:49 AM</span><br/><span class='road'>Road name: N1 Inbound</span><br/><span class='description'>Earlier ACCIDENT before the N1 Koeberg Interchange has been CLEARED - DELAYS from the N7 Highway</span></li></ul>
        </div>
        <div class="clr5 clr">&nbsp;</div>
        <a href="http://www.news24.com/Traffic/WESTERN_CAPE" id="lnkMore" class="block bold">More traffic reports...</a>
        <div class="clr5 clr">&nbsp;</div>
        <a href="http://pubads.g.doubleclick.net/gampad/clk?id=58119910&iu=/8900/24.com/Web/News24" id="lnkSponsor" target="_blank"><img src="http://cdn.24.co.za/files/Cms/General/d/2707/2c5f0da27a154cad93b7448a2e620359.jpg" id="imgSponsor" /></a>
        <script type="text/javascript">
            $j(document).ready(function () { $j("#ddlTrafficRegions").change(function () { var e = $j("OPTION:selected", this).val(); var t = "traffic/" + e.replace(" ", "_").toUpperCase(); $j("#lnkMore").html("<a id='lnkMore' href='" + t + "' class='block bold'>More traffic reports...</a>"); $j("#trafic-container").hide(); news24.getAjax("/Ajax/TrafficData/", "GetTraffic", { 'location': e }, function (e) { $j("#trafic-container").html(e); $j("#trafic-container").fadeIn("slow") }) }) });
        </script>
    </div>
</div></div>
                <div id="tab_lottery_data" class="tab-wrapper" style="display: none;">Here are the winning Powerball numbers from the Tuesday, 01 April&nbsp;draw.<br /><br />14, 17, 24, 27, 34 Powerball 4<br /><br /><strong>SMS the word Powerball to 31222 to get lotto numbers sent directly to your phone. The service costs just R10 per month.<br /><br />To unsubscribe, reply with the words Stop Powerball.</strong><br />
<div class="spacer clr"></div>
<a href="http://www.news24.com/Lottery" id="lnkMoreLotto" class="block bold">More lotto numbers...</a></div>
                <script type="text/javascript">tabsInfoClass.addTabs("infoTabContainer");</script>
            </td>
        </tr>
    </table>
</div>
<div class="spacer clr"></div>
    <div class="spacer clr">
        </div>
    <div class="ad300X250 col300">
        <div id='ad-300x250-1' class='24ad300x250'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('300x250','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=300x250&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=300x250&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
    </div>
    <div class="spacer clr">
        </div>
    
<script type="text/javascript">
    function InsuranceDealsGoTo(a) { $j("#sponsor_carousel").jcarousel("scroll", a, true); $j("#sponsor_carousel").jcarousel("reload"); return false } function movenext() { $j("#sponsor_carousel").jcarousel("next"); return false } function moveback() { $j("#sponsor_carousel").jcarousel("prev"); return false } function mycarousel_itemFirstInCallback(a, b, c, d) { var e = c; $j("div#adlist ul li").removeClass("selected"); $j("div#adlist ul li").removeAttr("style"); $j("div#adlist ul a").removeAttr("style"); $j("#ad_" + e).parent().addClass("selected"); $j("#ad_" + e).parent().attr("style", "background-color:" + colors[e] + ";color:" + textcolors[e]); $j("#ad_" + e).attr("style", "color:" + textcolors[e]); $j("#jcarousel-prev").unbind("click"); $j("#jcarousel-next").unbind("click"); if (e == 1) { $j("#jcarousel-prev").removeClass("jcarousel-prev-disabled").addClass("jcarousel-prev-disabled"); $j("#jcarousel-prev").attr("disabled", "disabled"); $j("#jcarousel-prev").unbind("click") } else { $j("#jcarousel-prev").removeClass("jcarousel-prev-disabled"); $j("#jcarousel-prev").attr("disabled", ""); $j("#jcarousel-prev").bind("click", moveback) } if (e == last) { $j("#jcarousel-next").removeClass("jcarousel-next-disabled").addClass("jcarousel-next-disabled"); $j("#jcarousel-next").attr("disabled", "disabled"); $j("#jcarousel-next").unbind("click") } else { $j("#jcarousel-next").removeClass("jcarousel-next-disabled"); $j("#jcarousel-next").attr("disabled", ""); $j("#jcarousel-next").bind("click", movenext) } } $j(document).ready(function () { $j('#jcarousel-next').bind('click', movenext); $j('#jcarousel-prev').bind('click', moveback); var randomnumber = Math.floor(Math.random() *0 +1); $j("#sponsor_carousel").jcarousel({ scroll: 1, start: randomnumber, itemFirstInCallback: mycarousel_itemFirstInCallback, buttonNextHTML: null, buttonPrevHTML: null }); $j("#sponsored_holder").removeClass("tabLoader") });
</script>


<div class="spacer clr"></div>
    

<div id="the_accordion" class="tabLoader">
    <div id="accordion" class="col299 relative">
        <h3 id="headerTag" class="toggler toggler_pers">
    <a href="http://www.careers24.com/cape-town-jobs" class="bold toggler_anchor">Jobs in Cape Town</a>
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=careers" id="lnkModalDisplay" class="careersModal right" style="padding-right:5px;text-transform:lowercase;font-size:11px">[change area]</a>
</h3>
<div class="element">
    <div id="divToHide">
        <h4 id="headerCareersRegion" class="bold item" style="font-size:11px;">Jobs in Western Cape region</h4>
        
	         <div class="item">
                
                    <h4 class="bold">
                        <a data-track="outbound,rightnav-listings,careers-Order Clerk" href="http://www.careers24.com/jobs/adverts/453886-order-clerk-western-cape/" target="_blank">Order Clerk</a></h4>
                        <img src="http://static.24.co.za/5/images/lazy/86x48.jpg" class="right job" width="86" height="48" data-src="http://www.careers24.com/_resx/imageresource/4354677D87CE6109A53E2C351D55B0B1DFCB305F-52677-86-48-0" />
                    <p>
                        Western Cape<br/>Main Solution Recruiters<br/>R9000</p>
                    
                    <div class="clr">
                    </div>
                </div>
          
	         <div class="item">
                
                    <h4 class="bold">
                        <a data-track="outbound,rightnav-listings,careers-Financial Manager" href="http://www.careers24.com/jobs/adverts/453974-financial-manager-western-cape/" target="_blank">Financial Manager</a></h4>
                        
                    <p>
                        Western Cape<br/>Adept Recruitment (Pty) Ltd<br/>R30000 - R35000</p>
                    
                    <div class="clr">
                    </div>
                </div>
          
	         <div class="item">
                
                    <h4 class="bold">
                        <a data-track="outbound,rightnav-listings,careers-Client Support Specialist (IT)" href="http://www.careers24.com/jobs/adverts/453947-client-support-specialist-it-western-cape/" target="_blank">Client Support Specialist (IT)</a></h4>
                        <img src="http://static.24.co.za/5/images/lazy/86x48.jpg" class="right job" width="86" height="48" data-src="http://www.careers24.com/_resx/imageresource/A2A5B419FE3BABFCEAFD4A243E589CFA08EAC25A-2020-86-48-0" />
                    <p>
                        Western Cape<br/>Persona Staff<br/>Market Related</p>
                    
                    <div class="clr">
                    </div>
                </div>
          
	    <div class="item browse bold">
		    <a href="http://www.careers24.com/cape-town-jobs" target="_blank">Browse more Cape Town jobs...</a>
	    </div>
	    <div class="item">
                <div class="left" style="margin-left: 0px; width: 140px;">
                    <ul>
                        
                                <li>
                                    <a href='http://www.careers24.com/port-elizabeth-jobs' title='Port Elizabeth Jobs'>
                                        Port Elizabeth Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/pretoria-jobs' title='Pretoria Jobs'>
                                        Pretoria Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/jobs-in-north-west' title='North West Jobs'>
                                        North West Jobs
                                    </a> 
                                </li>
                            
                    </ul>
                </div>
                <div class="left" style="margin-right:13px">
                    <ul>
                        
                                <li>
                                    <a href='http://www.careers24.com/admin-jobs' title='Admin Jobs'>
                                        Admin Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/mining-jobs' title='Mining Jobs'>
                                        Mining Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/accounting-jobs' title='Accounting Jobs'>
                                        Accounting Jobs
                                    </a> 
                                </li>
                            
                    </ul>
                </div>
                <div class="clr"></div>
        </div>
	    <div class="item bold last">
		    <a href="http://www.careers24.com/candidate/register/" target="_blank">Register your CV...</a><br/>
		    <a href="http://www.careers24.com/jobs/alert/" target="_blank">Get Job alerts in your e-mail...</a><br/>
		    <a href="http://www.careers24.com/recruiters/" target="_blank">RECRUITERS – Advertise your jobs here</a>
	    </div>
        <a id="lnkModalItem" class="fireEventCareers careersModal" style="display:none;"></a>
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler toggler_pers">
    <a href="http://www.property24.com" class="bold toggler_anchor">Property</a>
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=property" id="lnkModalDisplay" class="propertyModal right" style="padding-right:5px;text-transform:lowercase;font-size:11px">[change area]</a>
</h3>
<div class="element">
    <div id="divToHide">
        
        
                <div class="item">
	                <div class="wrapper">
	                <a href="http://www.property24.com/for-sale/paarl/western-cape/344?ListingNumber=P24-101698265" id="lnkThumb">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages.property24.com%2fFetchImage.ashx%3fresource%3dproperty%26listingtype%3dsale%26id%3d101698265%3a1%26size%3dmedium" />
                    </a>
                    </div>
                    <div class="wrapper">
		            <h4 class="bold"><a data-track="outbound,rightnav-listings,property-HOUSES FOR SALE IN Paarl" href="http://www.property24.com/for-sale/paarl/western-cape/344?ListingNumber=P24-101698265" target="_blank">HOUSES FOR SALE IN Paarl</a></h4>
		            <p><span class="block">Houses</span>
		            <span class="block bold">R 2 950 000</span></p>
                    </div>
		            <div class="clr"></div>
	            </div>
            
                <div class="item">
	                <div class="wrapper">
	                <a href="http://www.property24.com/for-sale/cape-town/western-cape/432?ListingNumber=P24-101710300" id="lnkThumb">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages.property24.com%2fFetchImage.ashx%3fresource%3dproperty%26listingtype%3dsale%26id%3d101710300%3a1%26size%3dmedium" />
                    </a>
                    </div>
                    <div class="wrapper">
		            <h4 class="bold"><a data-track="outbound,rightnav-listings,property-HOUSES FOR SALE IN Cape Town, Camps Bay" href="http://www.property24.com/for-sale/cape-town/western-cape/432?ListingNumber=P24-101710300" target="_blank">HOUSES FOR SALE IN Cape Town, Camps Bay</a></h4>
		            <p><span class="block">Houses</span>
		            <span class="block bold">R 7 200 000</span></p>
                    </div>
		            <div class="clr"></div>
	            </div>
            
                <div class="item">
	                <div class="wrapper">
	                <a href="http://www.property24.com/for-sale/cape-town/western-cape/432?ListingNumber=P24-101705458" id="lnkThumb">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages.property24.com%2fFetchImage.ashx%3fresource%3dproperty%26listingtype%3dsale%26id%3d101705458%3a1%26size%3dmedium" />
                    </a>
                    </div>
                    <div class="wrapper">
		            <h4 class="bold"><a data-track="outbound,rightnav-listings,property-HOUSES FOR SALE IN Cape Town, Constantia" href="http://www.property24.com/for-sale/cape-town/western-cape/432?ListingNumber=P24-101705458" target="_blank">HOUSES FOR SALE IN Cape Town, Constantia</a></h4>
		            <p><span class="block">Houses</span>
		            <span class="block bold">R 3 800 000</span></p>
                    </div>
		            <div class="clr"></div>
	            </div>
            
        <a id="lnkModalItem" class="fireEventProperty propertyModal" style="display:none;"></a>
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler" style="height:15px;"><a href="http://www.gotravel24.com/" class="bold">Travel</a> - Look, Book, Go!</h3>
<div class="element">
    <div id="divToHide">
	    <div class="item travel"><!-- add travel class -->
		    <h4 class="bold"><a id="lnkTitle" href="http://holidays.gotravel24.com/ku/holidayoffer.jsp?Destination=NL_SCHOOLS_OUT_MRU_GT,RG,RB&amp;utm_source=holidays&amp;utm_medium=focus&amp;utm_campaign=mar_schoolout">Magical Mauritius holidays</a></h4>
		    <img src="http://static.24.co.za/5/images/lazy/110x65.jpg" id="imgThumbnail" width="110" height="65" class="right" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fwww.gotravel24.com%2ffiles%2fpreskil_ext_02.jpg" />
		    Check out these great Mauritius holiday specials from R12 875 per person sharing. Includes accommodation, return flights and airport transfers.
		    <span class="item browse bold block"><a id="lnkPackages" href="http://holidays.gotravel24.com/ku/holidayoffer.jsp?Destination=NL_SCHOOLS_OUT_MRU_GT,RG,RB&amp;utm_source=holidays&amp;utm_medium=focus&amp;utm_campaign=mar_schoolout">Book now!</a></span>
	    </div>
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler"><a href="http://etrader.kalahari.com/referral.asp?linkid=3442&partnerid=9180" class="bold">Kalahari.com</a> - shop online today</h3>
<div class="element">
    <div id="divToHide">
        
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?Ntt=The+Real+Meal+Revolution&amp;searchCategories=4294966903&amp;N=4294966903&amp;Ntk=def&amp;pageSize=12&amp;linkId=1441122&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?Ntt=The+Real+Meal+Revolution&amp;searchCategories=4294966903&amp;N=4294966903&amp;Ntk=def&amp;pageSize=12&amp;linkId=1441122&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">The Real Meal Revolution </a></h4>
		              <p style="word-wrap:break-word;">The goal of The Real Meal Revolution is to change your life by teaching you how to take charge of your weight and your health through the way you eat. Order now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=21204+18262&amp;Ns=p_salestd%7c0&amp;linkId=1602077&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=21204+18262&amp;Ns=p_salestd%7c0&amp;linkId=1602077&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">Sleep & stress medicine</a></h4>
		              <p style="word-wrap:break-word;">Rest easy with our range of health and stress remedies. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/Merchandising-Category/N-g06Z1z141o6?linkId=1602075&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/Merchandising-Category/N-g06Z1z141o6?linkId=1602075&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">Great Easter deals at kalahari.com</a></h4>
		              <p style="word-wrap:break-word;">Get 2 inspirational, gospel or kids DVDs for just R99, as well as many other amazing deals. Offer valid while stocks last. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=19849&amp;linkId=1520747&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=19849&amp;linkId=1520747&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">kalahari.com #1 selling product</a></h4>
		              <p style="word-wrap:break-word;">gobii eReader + FREE wall charger and leatherette cover now R599, save R340. Offer valid while stocks last. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item last">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=20155&amp;linkId=1489277&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=20155&amp;linkId=1489277&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">25% off new & bestselling movies</a></h4>
		              <p style="word-wrap:break-word;">Choose from blockbuster titles including Despicable Me 2, Gravity, Frozen, The Hunger Games: Catching Fire and many more. Offer valid while stocks last. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler toggler">
    <a href="http://www.olx.co.za/" class="bold toggler_anchor"> OLX Free Classifieds</a>
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=kalahari" id="lnkModalDisplay" class="kalahariModal right" style="padding-right:5px;text-transform:lowercase;font-size:11px">[change area]</a>
</h3>
<div class="element">
    <div id="divToHide">
        
	          <div style="min-height:100px;" class="item">
                    <a href="http://capetown.olx.co.za/samsung-galaxy-s4-iid-559689336" id="lnkThumb" target="_blank">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" id="imgKalahari" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages04.olx-st.com%2fui%2f7%2f99%2f36%2ft_1382642518_559689336_3.jpg" />
                    </a>
		            <h4 class="bold"><a id="lnkArticle" href="http://capetown.olx.co.za/samsung-galaxy-s4-iid-559689336" target="_blank">Samsung Galaxy s4</a></h4>
		            <p style="word-wrap:break-word;">Mobile, Cell Phones in South Africa, Western Cape, Cape Town. Date October 24</p>
	          </div>
          
	          <div style="min-height:100px;" class="item">
                    <a href="http://capetown.olx.co.za/best-bargain-in-big-bay-iid-559891688" id="lnkThumb" target="_blank">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" id="imgKalahari" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages02.olx-st.com%2fui%2f1%2f24%2f88%2ft_1382699383_559891688_1.jpg" />
                    </a>
		            <h4 class="bold"><a id="lnkArticle" href="http://capetown.olx.co.za/best-bargain-in-big-bay-iid-559891688" target="_blank">Best bargain in big bay</a></h4>
		            <p style="word-wrap:break-word;">Real Estate, Houses - Apartments for Sale in South Africa, Western Cape, Cape Town. Date October 25</p>
	          </div>
          
	          <div style="min-height:100px;" class="item last">
                    <a href="http://capetown.olx.co.za/vw-golf-6-1-6-trendline-excellent-condition-iid-559891037" id="lnkThumb" target="_blank">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" id="imgKalahari" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages02.olx-st.com%2fui%2f7%2f17%2f37%2ft_1382699205_559891037_1.jpg" />
                    </a>
		            <h4 class="bold"><a id="lnkArticle" href="http://capetown.olx.co.za/vw-golf-6-1-6-trendline-excellent-condition-iid-559891037" target="_blank">VW Golf 6, 1.6 Trendline (Excellent condition)</a></h4>
		            <p style="word-wrap:break-word;">Vehicles, Cars in South Africa, Western Cape, Cape Town. Date October 25</p>
	          </div>
          
        <a id="lnkModalItem" class="fireEventKalahari kalahariModal" style="display:none;"></a>
        <div class="clr"></div>
        
    </div>
</div>
    </div>
</div>
    <div class="spacer clr">
        </div>
    
    

<div id="sponsor_box" class="col299 relative">
	<h3 class="bold">Sponsored links</h3>
    
		<table class="sponsor" width="280" border="0" cellpadding="0" cellspacing="0">
		  <tbody>
	  
		  <tr>
			<td style="width:35px;"><a href="../../Controls/Common/#" id="lnkSponsorImg"><img src="http://cdn.24.co.za/files/Cms/General/d/1946/c127ed56cafc46d8bef570a12d88bd6a.png" style="width:27px;" /></a></td>
			<td align="left"><a href="http://ad.doubleclick.net/clk;258342228;14949887;z?http://direct.infax.co.za/signup/media24/index.html" target="_blank">Free Fax2Mail</a></td>
			<td>&nbsp;</td>
	  
		</tbody></table>
	  
</div>
    <div class="spacer clr">
        </div>
    <div class="clr10 clr"> </div>
<script src="http://scripts.24.co.za/libs/kalahari/2.1/Scripts/kalahari.carousel.widget.js" type="text/javascript"></script>
<div id="oprahwidgetcontainer">
<script type="text/javascript">
jQuery('head').append("<link href='http://scripts.24.co.za/libs/kalahari/2.1/Styles/kalahari.carousel.css' type='text/css' rel='stylesheet' ></link>")
var Widget = new kalaharicarouselwidget({
sku: [48435681, 47824635, 48388933, 44612858,47332294],
token: "563",
container: "oprahwidgetcontainer",
visible:1,
refUrl: 'URL: http://www.kalahari.com/?linkId=46213&affiliateId=563&linkType=ORDER_REFERRAL'
});
</script>
</div>
<div class="clr10 clr"> </div>


    <div class="spacer clr">
        </div>
    

<script type="text/javascript">
    jQuery(function () {
        var submitFunc = function() { window.open('http://www.pricecheck.co.za/search/?utm_source=news24&utm_medium=affiliate&utm_campaign=sidebar&search=' + jQuery('#txtPriceCheckSearch').val()) };jQuery("#btnPriceCheckSubmit").click(submitFunc);jQuery("#txtPriceCheckSearch").keypress(function(e){if(e.keyCode===13){submitFunc();return false}})});
</script>

<div class="pricecheckBlock">
    <a href="http://www.pricecheck.co.za/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" target="_blank" id="lnkPriceCheckHeader" style="height:51px;left:0;position:absolute;top:0;width:298px;"></a>
    <div class="priceContent">
        <div class="priceBlurb">
            <p><a href="http://www.pricecheck.co.za/offers/14787662/BlackBerry+Bold+9780/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" id="aLink" target="_blank">BlackBerry Bold 9780</a></p>
            <p>BlackBerry 6
Engage your world with BlackBerry 6 OS on the...</p>
            <p>
                <a href="http://www.pricecheck.co.za/offers/14787662/BlackBerry+Bold+9780/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" id="aLinkPrice" style="color:#ec3b27;" target="_blank">
                    <span style="font-weight:normal">From</span> <strong>R3049.00</strong>
                </a>
            </p>
        </div>
        <div class="priceImage"><a href="http://www.pricecheck.co.za/offers/14787662/BlackBerry+Bold+9780/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" id="aLinkImage" target="_blank"><img src="http://static.24.co.za/5/images/lazy/65x65.jpg" id="imgThumb" data-src="http://images3.pricecheck.co.za/images/objects/hash/product/aac/572/2eb/image_small_14787662.jpg" /></a></div>
    </div>
    <div class="clr"></div>
    <div class="priceShopping">
        <h4>I'm shopping for:</h4>
        <input type="text" class="priceSearch" id="txtPriceCheckSearch" />
        <input type="button" class="priceSubmit" value="LET'S GO!" id="btnPriceCheckSubmit" />
    </div>
</div>
    <div class="spacer clr">
        </div>
    
<div class="facebook_block">
    <iframe src="http://www.facebook.com/plugins/likebox.php?href=http%3A%2F%2Fwww.facebook.com%2Fpages%2FNews24com%2F10227041841&width=300&height=245&show_faces=true&colorscheme=light&stream=false&show_border=true&header=false" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:300px; height:245px;" allowTransparency="true"></iframe>
</div>
    <div class="spacer clr">
        </div>
    

<div id="horoscopes_tab" class="tab-wrapper horoscope relative">
    <div class="horoscope_header"> Horoscopes</div>
    <div class="horoscope_women"><img src="http://static.24.co.za/5/images/women_horoscope.png" width="120" height="21" border="0" /></div>
	<div class="horoscope_midlevel">
        <div class="zodiac">
		    <select onchange="toggleSubmit(this)" name="ptype" id="ptype" class="absolute">
			     <option selected="selected" value="aquarius">Aquarius  (20 Jan - 18 Feb)</option>
			     <option value="aries">Aries  (21 Mar - 20 Apr)</option>
			     <option value="cancer">Cancer  (21Jun - 21 Jul)</option>
			     <option value="capricorn">Capricorn  (21Dec - 19 Jan)</option>
			     <option value="gemini">Gemini  (21 May - 20 Jun)</option>
			     <option value="leo">Leo  (22 Jul - 21 Aug)</option>
			     <option value="libra">Libra  (22 Sep - 22 Oct)</option>
			     <option value="pisces">Pisces  (19 Feb - 20 Mar)</option>
			     <option value="sagittarius">Sagittarius (22 Nov - 20 Dec)</option>
			     <option value="scorpio">Scorpio  (23 Oct - 21 Nov)</option>
			     <option value="taurus">Taurus  (21 Apr - 20 May)</option>
			     <option value="virgo">Virgo  (22 Aug - 21 Sep)</option>
    	      </select>
	    </div>
        
                    <div id="d0" style="display:block;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Aquarius_icon.gif" alt="Aquarius" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aquarius" title="Aquarius" alt="Aquarius" data-track="outbound,home,horoscope-aquarius">Aquarius</a></h5>
                           <p>Your mind is full and you may want to curl up in a comfy place at home and just escape into the world of imagination either...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aquarius" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-aquarius">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d1" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Aries_icon.gif" alt="Aries" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aries" title="Aries" alt="Aries" data-track="outbound,home,horoscope-aries">Aries</a></h5>
                           <p>Impatience and frustration could create tension for you today. You may have to compromise and take the middle path to avoid...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aries" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-aries">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d2" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Cancer_icon.gif" alt="Cancer" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Cancer" title="Cancer" alt="Cancer" data-track="outbound,home,horoscope-cancer">Cancer</a></h5>
                           <p>You may be going over the top in your enthusiasm to have fun and please the crowd. Try and find the middle road of moderation...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Cancer" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-cancer">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d3" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Capricorn_icon.gif" alt="Capricorn" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Capricorn" title="Capricorn" alt="Capricorn" data-track="outbound,home,horoscope-capricorn">Capricorn</a></h5>
                           <p>Things seem to be intense right now, but an unexpected visit from someone could draw you away from the intensities and help you to...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Capricorn" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-capricorn">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d4" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Gemini_icon.gif" alt="Gemini" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Gemini" title="Gemini" alt="Gemini" data-track="outbound,home,horoscope-gemini">Gemini</a></h5>
                           <p>Your rational mind is awake and you are able to focus and organise things a lot better today. Put your restless energy into...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Gemini" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-gemini">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d5" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Leo_icon.gif" alt="Leo" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Leo" title="Leo" alt="Leo" data-track="outbound,home,horoscope-leo">Leo</a></h5>
                           <p>You may have an impulsive urge to expand your horizons and explore your possibilities. You don`t want to be tied down today. ...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Leo" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-leo">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d6" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Libra_icon.gif" alt="Libra" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Libra" title="Libra" alt="Libra" data-track="outbound,home,horoscope-libra">Libra</a></h5>
                           <p>You may want to treat your loved one with something close to your heart. This could be a gift, a delicious meal or even just some...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Libra" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-libra">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d7" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Pisces_icon.gif" alt="Pisces" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Pisces" title="Pisces" alt="Pisces" data-track="outbound,home,horoscope-pisces">Pisces</a></h5>
                           <p>You may find your enthusiasm and your energy levels don`t match up today. You may get swept away in your desire to have fun. ...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Pisces" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-pisces">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d8" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Sagittarius_icon.gif" alt="Sagittarius" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Sagittarius" title="Sagittarius" alt="Sagittarius" data-track="outbound,home,horoscope-sagittarius">Sagittarius</a></h5>
                           <p>The underlying tension may be that you have been spending a lot of time helping others and right now you just want to have some...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Sagittarius" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-sagittarius">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d9" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Scorpio_icon.gif" alt="Scorpio" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Scorpio" title="Scorpio" alt="Scorpio" data-track="outbound,home,horoscope-scorpio">Scorpio</a></h5>
                           <p>Your partner may surprise you and help you to enjoy the moment rather than worrying about all the things that seem to be...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Scorpio" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-scorpio">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d10" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Taurus_icon.gif" alt="Taurus" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Taurus" title="Taurus" alt="Taurus" data-track="outbound,home,horoscope-taurus">Taurus</a></h5>
                           <p>Indulgence and extravagance may be a strong temptation. You have the desire and the energy to do things, but you want to stay...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Taurus" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-taurus">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d11" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Virgo_icon.gif" alt="Virgo" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Virgo" title="Virgo" alt="Virgo" data-track="outbound,home,horoscope-virgo">Virgo</a></h5>
                           <p>Today may be a good day to start by jotting down your thoughts and creating some kind of structure to work with. ...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Virgo" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-virgo">read more</a></p>                               	              
	                    </div>
	                 </div>
          
	</div>
    <div class="perfect_match">
        <a href="http://love2meet.news24.com/" data-track="outbound,home,horoscope-love2meet.news24.com">Who’s your perfect match?<br />
<span>Click here to find out!</span></a>
    </div>
</div>


<script type="text/javascript">
    function toggleSubmit(obj) { count = 0; while (document.getElementById("d" + count)) { document.getElementById("d" + count).style.display = "none"; count++ } document.getElementById("d" + obj.selectedIndex).style.display = "block" } var date = new Date; var day = date.getDate(); var month = date.getMonth(); var currentZodiac; switch (month) { case 0: { if (day >= 20) currentZodiac = "aquarius"; else currentZodiac = "sagittarius"; break }; case 1: { if (day >= 19) currentZodiac = "pisces"; else currentZodiac = "aquarius"; break }; case 2: { if (day >= 21) currentZodiac = "aries"; else currentZodiac = "pisces"; break }; case 3: { if (day >= 21) currentZodiac = "taurus"; else currentZodiac = "aries"; break }; case 4: { if (day >= 21) currentZodiac = "gemini"; else currentZodiac = "taurus"; break }; case 5: { if (day >= 21) currentZodiac = "cancer"; else currentZodiac = "gemini"; break }; case 6: { if (day >= 22) currentZodiac = "leo"; else currentZodiac = "cancer"; break }; case 7: { if (day >= 22) currentZodiac = "virgo"; else currentZodiac = "leo"; break }; case 8: { if (day >= 22) currentZodiac = "libra"; else currentZodiac = "virgo"; break }; case 9: { if (day >= 23) currentZodiac = "scorpio"; else currentZodiac = "libra"; break }; case 10: { if (day >= 22) currentZodiac = "sagittarius"; else currentZodiac = "scorpio"; break }; case 11: { if (day >= 21) currentZodiac = "capricorn"; else currentZodiac = "sagittarius"; break } } $j(".zodiac #ptype").val(currentZodiac); toggleSubmit($j(".zodiac #ptype")[0])</script>
    <div class="spacer clr">
        </div>
    <div class="col299 relative endcolumn">
        </div>

            </div>
            <div class="spacer clr white"></div>
        </div>
        <div id="footer" class="relative clr">
                       
            

<div class="clr10 clr">&nbsp;</div>
<div id="divServices" class="services left">
  <h3 class="bold">services</h3>
  
      <div class="item left">
        <a href="http://www.news24.com/Newsletters" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/167/3d5262fc76764b0abd11667baf454f84.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/Newsletters" target="_top">E-mail Alerts</a></strong>
        The latest headlines in your inbox 
        </p>
      </div>
    
      <div class="item left">
        <a href="http://www.news24.com/SiteElements/Services/News24-RSS-Feeds-20111202-2" target="_self"><img src="http://cdn.24.co.za/files/Cms/General/d/495/7125197ea74a4880879e2bd187f630c9.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/SiteElements/Services/News24-RSS-Feeds-20111202-2" target="_self">RSS feeds</a></strong>
        News delivered really simply.
        </p>
      </div>
    
      <div class="item left">
        <a href="http://m.news24.com/news24" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/167/decc890f19a644579a0c033e19edbc40.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://m.news24.com/news24" target="_top">Mobile</a></strong>
        News24 on your mobile or PDA
        </p>
      </div>
    
      <div class="item left last">
        <a href="http://www.news24.com/Newsletters" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/167/432cbe0789a040e9ae3627685a099a0e.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/Newsletters" target="_top">E-mail Newsletters</a></strong>
        You choose what you want 
        </p>
      </div>
    
      <div class="item left">
        <a href="http://www.news24.com/xArchive/News24/Get-News24-on-your-iPhone-20090428" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/495/e2ae1ce7a6c74cd19e793cb31873a54e.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/xArchive/News24/Get-News24-on-your-iPhone-20090428" target="_top">News24 on your iPhone</a></strong>
        Get News24 headlines on your iPhone.
        </p>
      </div>
    
      <div class="item left">
        <a href="http://mobile.24.com/?p=minisite_news" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/168/7c086371afe44063bfadd3ff26fde57d.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://mobile.24.com/?p=minisite_news" target="_top">SMS Alerts</a></strong>
        Get breaking news stories via SMS.
        </p>
      </div>
    
      <div class="item left">
        <a href="http://blogs.24.com/" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/168/4a134cf303084f35bec18b1262fecf3e.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://blogs.24.com/" target="_top">Blogs</a></strong>
        Your opinion on you, me and everyone. 

        </p>
      </div>
    
      <div class="item left last">
        <a href="http://opencalais.com/" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/175/09ea1738b1764dca88d3100f383052c1.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://opencalais.com/" target="_top">Calais</a></strong>
        Website keywords automated by OpenCalais.
        </p>
      </div>
    
</div>
<div class="clr">&nbsp;</div>
            

<div id="footernav" class="relative">
  	<a href="http://www.24.com" class="absolute logo24"><img class="absolute logo24" width="56" height="42" src="http://static.24.co.za/5/images/24com_logo.png"/></a>
	<a href="http://www.dmma.co.za/" class="absolute dmma" title="Digital Media &amp; Marketing Association" target="_blank"><img src="http://static.24.co.za/5/images/footer_logo_dmma.png" width="102" height="52" alt="Digital Media &amp; Marketing Association" border="0" class="absolute dmma" /></a>
	
    <div class="copy absolute">
	    <ul>
	        
		            <li><a href="http://www.news24.com/search">Search</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/SiteElements/Footer/About-Us-20090703-4">About Us</a> ·</li>  
	            
		            <li><a href="http://www.thespacestation.co.za/channel/news24/">Advertise on News24</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/SiteElements/Services/Terms-and-Conditions-20120413">Terms & Conditions</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/PressReleases">Press Releases</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/Jobs/">Jobs at News24</a> ·</li>  
	            
            <li><a id="lnkFooterContactUs" class="group" href="http://www.news24.com/FeedBack.aspx?iframe" class="footerLink">Contact us</a></li>
        </ul>
        <div class="clr10 clr">&nbsp;</div>
        
        &copy; 2014 24.com. All rights reserved.
    </div>
 
</div>

        </div>
        <div class="clr white"></div>
    </div>

            

<div id="socialbarHPStories">
    <div id="socialbar-newstories" class="bottom">
        <span onclick="HPRedirect('http://www.news24.com/');">There are&nbsp;<strong>new stories</strong>&nbsp;on the homepage. Click here to see them.</span>
        <div id="close" onclick=" CloseNewStoriesPopup(); ">&nbsp;</div>
        <div class="arrow"></div>
    </div>
</div>
            <div id="retail_ad_spacer"></div> 
        </div>
        <div id='ad-1000x1000-1' class='24ad1000x1000'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('1000x1000','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=1000x1000&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=1000x1000&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
        <div id='ad-20x20-1' class='24ad20x20'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('20x20','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=20x20&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=20x20&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
        <div id="ad300bottom">
            <div id='ad-980x415-1' class='24ad980x415'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('980x415','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=980x415&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=980x415&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
        <div class="clr"></div>
    

<script type="text/javascript">
//<![CDATA[
var gotravelCount=5;//]]>
</script>

<div id="CmsStats" style="z-index:-1; visibility:hidden;">
<script type="text/javascript" language="JavaScript" >
var cmsStatsImage = new Image();
cmsStatsImage.src = "http://stats.24.com/content/image.articleview?rnd=635320311272715457&s=5&c=1059&a=45517554-ffe3-4fea-bb92-0d02c82028d2&t=Pair+found+guilty+of+rape%2c+murder&ct=SouthAfrica/News&u=http%3a%2f%2fwww.news24.com%2fSouthAfrica%2fNews%2fPair-found-guilty-of-rape-murder-20140402&uid=&luid=&sn=";
</script>
<noscript>
<img src="http://stats.24.com/content/image.articleview?rnd=635320311272715457&s=5&c=1059&a=45517554-ffe3-4fea-bb92-0d02c82028d2&t=Pair+found+guilty+of+rape%2c+murder&ct=SouthAfrica/News&u=http%3a%2f%2fwww.news24.com%2fSouthAfrica%2fNews%2fPair-found-guilty-of-rape-murder-20140402&uid=&luid=&sn=" alt=""/>
</noscript>
</div>

<script type="text/javascript">
//<![CDATA[
var _virtualPath = 'http://www.news24.com/';//]]>
</script>
</form>
    
    



    <div class="personalisationContainer">
        <div class="personalisationNav">
            <div class="topNavWrapper">
                <div class="left bold headerLinks">
                    <span id="site_languages_dropdown"><a href="http://www.news24.com" data-track="outbound,topbar,news24.com" class="deepblue bold">News24</a></span>
                </div>
                <div class="site_languages">
                    <div style="color: #848484;">
                        English</div>
                    <div style="margin-top: 10px;">
                        <a href="http://afrikaans.news24.com">Afrikaans</a></div>
                    <div style="margin-top: 10px;">
                        <a href="http://isizulu.news24.com">isiZulu</a></div>
                </div>
                <div class="bold headerLinks left" style="margin-left:5px;">
                    <span class="grey">|&nbsp;&nbsp;<a href="http://www.olx.co.za" data-track="outbound,topbar,olx.co.za" class="grey bold">OLX</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://www.pricecheck.co.za/" data-track="outbound,topbar,pricecheck.co.za" class="grey bold">PriceCheck</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://www.property24.com" data-track="outbound,topbar,property24.com" class="grey bold">Property24</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://etrader.kalahari.com/referral.asp?linkid=7002&partnerid=9180" data-track="outbound,topbar,kalahari.com" class="grey bold">Kalahari.com</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://www.careers24.com" data-track="outbound,topbar,careers24.com" class="grey bold">Careers24</a></span>
                </div>
            </div>
            

<script type="text/javascript">
    function CheckUsernameAvailable() { var a = $j("#txtUsername").val(); var b = new RegExp("^[a-zA-Z0-9-_]*$"); if (!a == "") { if (!a.match(b)) $j("#originalHeader").fadeOut("fast", function () { $j("#headerUsernameError").html("Your username may not contain any spaces or special characters.").fadeIn("fast") }); else news24.getAjax("/Ajax/UgcData/", "CheckUsernameAvailability", { 'username': a }, CheckUsernameAvailableCallback) } else $j("#originalHeader").fadeOut("fast", function () { $j("#headerUsernameError").html('Please enter a username and then click "Register"').fadeIn("fast") }) } function CheckUsernameAvailableCallback(a) { if (!a.error && a != "error") { if (a == true) { $j("#enterUsernameDiv").fadeOut("fast", function () { $j("#spanNewUsername").html($j("#txtUsername").val()); $j("#txtDisplayName").val($j("#txtUsername").val()); $j("#personaliseProfileDiv").fadeIn("fast") }) } else $j("#originalHeader").fadeOut("fast", function () { $j("#headerUsernameError").html("Sorry, that username is not available").fadeIn("fast") }) } } function ResetAvatar() { $j.ajax({ url: "/AvatarRemove.axd?filename=" + $j("#avatarImage").attr("src"), type: "POST" }); $j("#avatarImage").attr("src", user.avatarUrl); $j("#btnResetAvatar").fadeOut() } function SaveUserProfile() {$j("#displayNameError").fadeOut("fast"); $j("#profileSaveError").fadeOut("fast"); var a = true; var b = escape($j("#txtDisplayName").val()); user.bio = escape($j("#txtAboutMe").val()); user.avatarUrl = $j("#avatarImage").attr("src"); user.name = escape($j("#txtUsername").val()); if (b == "") { a = false; $j("#displayNameError").fadeIn("fast") } else user.displayName = b; if (a) { $j("#personaliseProfileDiv").fadeOut("fast"); $j(".saveProfile").fadeIn("fast"); var data = JSON.stringify({ userSettings: user }); news24.getAjax("/Ajax/UgcData/", "SaveTinaProfile", data, SaveUserProfileCallback, null, "POST") }} function SaveUserProfileCallback(a) { if (!a.error && a.value != "error") { if (a.value === "upload") { $j(".saveProfile").fadeOut("fast"); $j("#personaliseProfileDiv").fadeIn("fast"); $j("a.call2action").click(); user.referrer = "" } else { $j("#fancybox-close").click(); location.reload(true) } } else { $j(".saveProfile").fadeOut("fast"); $j("#personaliseProfileDiv").fadeIn("fast"); $j("#profileSaveError").fadeIn("fast") } } function CheckCharacterCount(a) { a = a || window.event; var b = a.keyCode; if (b == 8 || b == 46) return true; else if ($j("#txtAboutMe").val().length < 1e3) return true; else return false } var user = { name: "", displayName: "", userid: "", avatarUrl: "", bio: "", referrer: "" }; var hasProfile = ""; $j(document).ready(function () { $j("#createProfileFire").fancybox({ padding: 0, centerOnScroll: true }); var a = $j("#btnUploadAvatar"); var b = $j("#avatarError"); new AjaxUpload(a, { action: "/AvatarUpload.axd", name: "uploadfile", data: { userid: user.userid }, onSubmit: function (a, c) { if (!(c && /^(jpg|png|jpeg|gif)$/.test(c))) { b.html("Only JPG, PNG or GIF files are allowed").fadeIn(); return false } b.html("Uploading...").fadeIn() }, onComplete: function (a, c) { b.html(""); if (!c.error) { var d = $j($j(c)[1]).html(); if (d != "error") { user.avatarUrl = $j("#avatarImage").attr("src"); $j("#avatarImage").attr("src", d); b.fadeOut().html(""); $j("#btnResetAvatar").fadeIn() } else b.html("* The image you selected could not be uploaded.").fadeIn() } else b.html("* The image you selected could not be uploaded.").fadeIn() } }); if (hasProfile == "true") { $j("#enterUsernameDiv").hide(); $j("#spanNewUsername").html(unescape(user.name)); $j("#txtDisplayName").val(unescape(user.displayName)); $j("#txtAboutMe").val(unescape(user.bio)); $j("#personaliseProfileDiv").show() } })
</script>

<a id="createProfileFire" style="display:none;" href="#createProfileModal">&nbsp;</a>
<input type="hidden" name="userid" value="" />
<div style="display:none;">
    <div id="createProfileModal">
        <div id="enterUsernameDiv">
            <div class="userheader"><h2>Hello&nbsp;<strong></strong></h2></div>
            <div class="step1_content">
                <h3>Create Profile</h3>
                 <p>Creating your profile will enable you to submit photos and stories to get published on News24.</p><br />
                <h3 id="originalHeader">Please provide a username for your profile page:</h3>
                <h3 id="headerUsernameError" style="display:none"></h3>
                <p>This username must be unique, cannot be edited and will be used in the URL to your profile page across the entire 24.com network.</p>
                <div class="formborder">
                    <input type="text" id="txtUsername" class="username_form" />
                </div>
            </div>
            <div class="reg_btn2"><input type="button" id="btnRegister" value="Register" onclick="CheckUsernameAvailable();" /></div>
        </div>
        <div id="personaliseProfileDiv" style="display:none;">
            <div class="userheader"><h2>Hello&nbsp;<strong><span id="spanNewUsername"></span></strong></h2></div>
            <div class="step2_content">
                <h3>Choose a display name:</h3>
                <div class="formborder">
                    <input type="text" id="txtDisplayName" />
                </div>
                <span id="displayNameError" >* You must provide a display name.</span>
                <h3>Edit your avatar:</h3>
                <div class="changeprofile">
                    <img id="avatarImage" height="35" width="35" />
                    <span class="selectp_img">Select an image file on your computer (max 4MB):</span>
                    <input type="button" id="btnUploadAvatar" value="Upload" />
                    <input type="button" id="btnResetAvatar" value="Reset" onclick="ResetAvatar();"  style="display:none;"/>
                    <span id="avatarError">* The image you selected could not be uploaded.</span>
                </div>
                <h3>Tell us a bit about yourself:</h3>
                <textarea id="txtAboutMe" cols="55" rows="6" onkeydown="return CheckCharacterCount(event);"></textarea>
                <div id="profileSaveError" style="color:Red;font-size:12px;display:none;">* Your profile could not be saved at the moment. Please try again later.</div>
            </div>
            <div class="reg_btn"><input type="button" id="btnSaveUserProfile" value="Save" onclick="SaveUserProfile();" /></div>
        </div>
        <div class="saveProfile" style="text-align:center;display:none;">
            <div style="height:170px;">&nbsp;</div>
            <div style="height:40px;">
                <h3 style="font-weight:bold;font-size: 20px;">Saving your profile</h3>
                <img src="http://static.24.co.za/5/images/ajax-loader-bar.gif" />
            </div>
            <div style="height:170px;">&nbsp;</div>
        </div>
    </div>
</div>
            
<div id="toppanel">
    <div class="tab right">
        
        <div id="pnlLoggedOut">
	
            <ul class="loggedOut">
                <li id="togglePanel" class="logout"><a id="openPanel" class="point_down" href="javascript:void(0);">Login / SignUp</a> <a id="closePanel" style="display: none;" class="point_up" href="#">Login / SignUp</a> </li>
            </ul>
        
</div>
    </div>
    <div id="pnlSettings">
	
        <div id="panel">
            <div class="content">
                <h1 class="bold">
                    Settings</h1>
                
                <div id="divModalContent">
                    <div class="info">
                        <a href="#" class="name">Location Settings</a><br />
                        <p>
                            News24 allows you to edit the display of certain components based on a location.
                            If you wish to personalise the page based on your preferences, please select a
                            location for each component and click "Submit" in order for the changes to
                            take affect.</p>
                    </div>
                    <div class="info left">
                        <div class="left selectBox">
                            <label>
                                Most Read Block</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selUserLocation" id="selUserLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="capetown">Cape Town</option>
		<option value="george">George</option>
		<option value="johannesburg">Johannesburg</option>
		<option value="pretoria">Pretoria</option>
		<option value="eastlondon">East London</option>
		<option value="portelizabeth">Port Elizabeth</option>
		<option value="bloemfontein">Bloemfontein</option>
		<option value="durban">Durban</option>
		<option value="pietermaritzburg">Pietermaritzburg</option>
		<option value="polokwane">Polokwane</option>
		<option value="nelspruit">Mbombela</option>
		<option value="kimberley">Kimberley</option>
		<option value="mafikeng">Mahikeng</option>
	</select>
                            <span id="userLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Weather</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selWeatherLocation" id="selWeatherLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="capetown">Cape Town</option>
		<option value="george">George</option>
		<option value="johannesburg">Johannesburg</option>
		<option value="pretoria">Pretoria</option>
		<option value="eastlondon">East London</option>
		<option value="portelizabeth">Port Elizabeth</option>
		<option value="bloemfontein">Bloemfontein</option>
		<option value="durban">Durban</option>
		<option value="pietermaritzburg">Pietermaritzburg</option>
		<option value="polokwane">Polokwane</option>
		<option value="nelspruit">Mbombela</option>
		<option value="kimberley">Kimberley</option>
		<option value="mafikeng">Mahikeng</option>
	</select>
                            <span id="weatherLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Traffic</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selTrafficLocation" id="selTrafficLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="western cape">Western Cape</option>
		<option value="gauteng">Gauteng</option>
		<option value="eastern cape">Eastern Cape</option>
		<option value="free state">Free State</option>
		<option value="kwazulu-natal">KwaZulu-Natal</option>
		<option value="limpopo">Limpopo</option>
		<option value="mpumalanga">Mpumalanga</option>
		<option value="northern cape">Northern Cape</option>
		<option value="north-west">North-West</option>
	</select>
                            <span id="trafficLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Jobs</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selJobLocation" id="selJobLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="western cape">Western Cape</option>
		<option value="gauteng">Gauteng</option>
		<option value="eastern cape">Eastern Cape</option>
		<option value="free state">Free State</option>
		<option value="kwazulu-natal">KwaZulu-Natal</option>
		<option value="limpopo">Limpopo</option>
		<option value="mpumalanga">Mpumalanga</option>
		<option value="northern cape">Northern Cape</option>
		<option value="north-west">North-West</option>
	</select>
                            <span id="careersLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Property Listings</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selPropertyLocation" id="selPropertyLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="western cape">Western Cape</option>
		<option value="gauteng">Gauteng</option>
		<option value="eastern cape">Eastern Cape</option>
		<option value="free state">Free State</option>
		<option value="kwazulu-natal">KwaZulu-Natal</option>
		<option value="limpopo">Limpopo</option>
		<option value="mpumalanga">Mpumalanga</option>
		<option value="northern cape">Northern Cape</option>
		<option value="north-west">North-West</option>
	</select>
                            <span id="propertyLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Kalahari Listings</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selKalahariLocation" id="selKalahariLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="capetown">Cape Town</option>
		<option value="george">George</option>
		<option value="johannesburg">Johannesburg</option>
		<option value="pretoria">Pretoria</option>
		<option value="eastlondon">East London</option>
		<option value="portelizabeth">Port Elizabeth</option>
		<option value="bloemfontein">Bloemfontein</option>
		<option value="durban">Durban</option>
		<option value="pietermaritzburg">Pietermaritzburg</option>
		<option value="polokwane">Polokwane</option>
		<option value="nelspruit">Mbombela</option>
		<option value="kimberley">Kimberley</option>
		<option value="mafikeng">Mahikeng</option>
	</select>
                            <span id="kalahariLocationError" style="display: none; color: Red;">*</span>
                            <p id="errorMessage" style="display: none; color: Red;">
                                Please select a value from the drop down box.</p>
                        </div>
                        <br />
                        <div class="left" style="clear:both;">
                            <input id="btCloseSettings" type="button" name="submit" value="Close" class="bt_login" />
                            <input id="bntSaveLocations" type="button" name="submit" value="Save" class="bt_login" />
                        </div>
                    </div>
                </div>
                <div id="savingSettings" style="display: none;">
                    <div class="info" style="margin-top: 95px; text-align: center;">
                        <h3 style="font-weight: bold; font-size: 20px; margin-bottom: 20px;">
                            Saving your settings</h3>
                        <img src="http://static.24.co.za/5/images/ajax-loader-bar.gif"  />
                    </div>
                </div>
            </div>
        </div>
        <!-- /login -->
    
</div>
    <div id="logoutPanel">
        <div class="content">
            <h1 class="bold">
                Facebook Sign-In</h1>
            <div>
                <div class="info">
                    <p>
                        <strong>Hi News addict,</strong>
                    </p>
                    <p>
                        Join the News24 Community to be involved in breaking the news.
                    </p>
                    <p>
                        Log in with Facebook to comment and personalise news, weather and listings.
                    </p>                
                    <div class="facebook_login">                          
                        <a href="javascript:void(0);" class="submit_button">
                            <img src="http://static.24.co.za/5/images/facebookicon_login.png" width="228" height="75" border="0" title="Login with your Facebook account" alt="Login with your Facebook account" /></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
    function setLocationDropdowns() { $j("#selUserLocation")[0].selectedIndex = $j("#selUserLocation").attr("orig"); $j("#selWeatherLocation")[0].selectedIndex = $j("#selWeatherLocation").attr("orig"); $j("#selTrafficLocation")[0].selectedIndex = $j("#selTrafficLocation").attr("orig"); $j("#selJobLocation")[0].selectedIndex = $j("#selJobLocation").attr("orig"); $j("#selPropertyLocation")[0].selectedIndex = $j("#selPropertyLocation").attr("orig"); $j("#selKalahariLocation")[0].selectedIndex = $j("#selKalahariLocation").attr("orig") } $j("#open").click(function () { $j("div#panel").slideDown("slow"); setLocationDropdowns() }); $j("#openPanel,#closePanel").click(function () { if ($j("div#logoutPanel").is(":visible")) { $j("div#logoutPanel").hide("fast") } else { $j("div#logoutPanel").slideDown("fast") } }); $j("#close,#btCloseSettings").click(function () { $j("div#panel").slideUp("fast"); setLocationDropdowns() }); $j("#toggle a,#btCloseSettings").click(function () { $j("#toggle a").toggle(); if ($j(".top_user_profile_edit").is(":visible")) { $j("#toppanel #lnkEditProfile").attr("class", "point_down"); $j(".top_user_profile_edit").hide() } }); $j("#togglePanel a").click(function () { $j("#togglePanel a").toggle() }); $j("#bntSaveLocations").click(function () { $j("#divModalContent").hide(); $j("#savingSettings").fadeIn("slow"); var a = "/Handlers/SaveLocations.ashx?"; a += "UserLocation=" + $j("#selUserLocation").val() + "&"; a += "WeatherLocation=" + $j("#selWeatherLocation").val() + "&"; a += "TrafficLocation=" + $j("#selTrafficLocation").val() + "&"; a += "JobLocation=" + $j("#selJobLocation").val() + "&"; + "&"; a += "PropertyLocation=" + $j("#selPropertyLocation").val() + "&"; a += "KalahariLocation=" + $j("#selKalahariLocation").val(); $j.ajax({ type: "GET", url: a, success: function (a) { if (a != "error") { location.reload(true) } } }); return false }); $j("#btnLogout").click(function () { window.location = "http://auth.news24.com/DeAuthenticate.aspx?surl=http://www.news24.com/SouthAfrica/News/Pair-found-guilty-of-rape-murder-20140402" }); $j("#toppanel li.user").click(function () { if ($j(".top_user_profile_edit").is(":visible")) $j("#toppanel #lnkEditProfile").attr("class", "point_down"); else $j("#toppanel #lnkEditProfile").attr("class", "point_up"); $j(".top_user_profile_edit").toggle(); $j("#toggle a.close").hide(); $j("#toggle a.open").show(); $j("div#panel").slideUp("fast"); setLocationDropdowns() });
</script>

            <div class="clr10">&nbsp;</div>
        </div>
    </div>
    
    
    <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/json/json2.js?v=20140319" ></script>
    <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/24com/tina/1.0/loginwindow.js?v=20140319" ></script>
    
    <script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/minified/basescript2.min.js?v=20140319" ></script>
    
    <script type="text/javascript">
        $j(document).ready(function () {$j("a.group,a.mynewspics").easyTooltip();});
        $j('.submit_button').click(function () { OpenTinaLoginWindow(); });
         function OpenTinaLoginWindow(permission) {
            json = { refreshPage: true, loginProvider: 'Facebook', tinaBaseUrl: 'http://auth.news24.com' };
            json.scope = this;
             if (permission)
                 json.permission = permission;
             Tina.openLoginWindow(json);
         }
        tinaUrl = 'http://auth.news24.com';
    </script>
    

    
        
        <script type='text/javascript'>
            var SiteSection = window.location.pathname.replace(/^\/([^\/]*).*$/, '$1');
            if (SiteSection == "")
                SiteSection = "HomePage";
            var _sf_async_config = {}; _sf_async_config.uid = 8959; _sf_async_config.domain = "news24.com"; _sf_async_config.sections = SiteSection ; _sf_async_config.authors = "News24"; (function () { function a() { window._sf_endpt = (new Date).getTime(); var a = document.createElement("script"); a.setAttribute("language", "javascript"); a.setAttribute("type", "text/javascript"); a.setAttribute("src", ("https:" == document.location.protocol ? "https://a248.e.akamai.net/chartbeat.download.akamai.com/102508/" : "http://static.chartbeat.com/") + "js/chartbeat.js"); document.body.appendChild(a) } var b = window.onload; window.onload = typeof window.onload != "function" ? a : function () { b(); a() } })()
        </script>
    <script type="text/javascript">
var idleInterval;var idleTime = 0;
$j(document).ready(function() {
if(!jQuery.cookie('closeidlead')){
idleInterval = setInterval("timerIncrement()", 1000); 
$j(this).mousemove(function(e) {idleTime = 0;});
$j(this).keypress(function(e) {idleTime = 0;});
$j(this).click(function (e) {idleTime = 0;});
}
});
function timerIncrement() {
idleTime = idleTime + 1;
if (idleTime == 1800) {
clearInterval(idleInterval);
GA24.trackEvent('IdleAd,open');
var popupUrl = '/IdlePopupPage.html?domain=' + document.domain + '&zone=' + za24_AdZone; 
$j("<a href='" + popupUrl + "'></a>" ).fancybox({'width':730,'height':508, 'type': 'iframe', 'padding': '0px', 'scrolling':'auto'}).click();
} 
}
</script>

    <div id='ad-200x400-1' class='24ad200x400'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('200x400','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=200x400&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=200x400&c=985738808&t=artid%3d45517554-ffe3-4fea-bb92-0d02c82028d2%26Places%3djohannesburg%26Topics%3dcrime%26posno%3d1' border='0' alt=''></a></noscript>
</body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.news24.com/SouthAfrica/News/Pair-found-guilty-of-rape-murder-20140402'
        self.crawler.extract(doc, html)

        self.maxDiff = None

        self.assertEqual(doc.title, u'Pair found guilty of rape, murder')
        self.assertEqual(doc.summary, 'Two men have been found guilty of raping a mother and daughter and killing the daughter, after breaking into their home to steal money for drugs. ')
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '02 04 2014')
        self.assertEqual(doc.author.name, "SAPA")
        self.assertEqual(doc.medium.name, 'News24')

        self.assertEqual(doc.text, u"\n\nJohannesburg - Two men have been found guilty of murder, rape, and robbery, in the South Gauteng High Court sitting in Palm Ridge, The Star reported on Wednesday.\n\nKyle Fredericks and Shinawaaz Ahmento, both aged 21, would be sentenced on Wednesday by acting Judge Louis Vorster for murdering, raping, and robbing Tracey-Lee Martins.\n\nIn April last year, the two broke into Martins's home in Klipspruit West to rob her so they could get money for drugs, the paper reported.\n\nAhmento raped Martins while she was in bed, then robbed her. He was a frequent visitor at the house, the paper reported. \n\nFredericks strangled Martins with socks then threw the socks down a drain.\n\nMartins's son, who was aged 3 at the time, and his 74-year-old grandmother were also at the house at the time. Ahmento strangled the older woman, who survived the attack, before robbing her as well.\n\nThe two then fled the scene, the paper reported.\n\n\n\n\n\n")

    def test_extract_old_article_style(self):
        html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://www.facebook.com/2008/fbml">
<head id="Head1"><meta name="description" content="Authorities kept hundreds of thousands of people out of their beds after a magnitude-8.2 earthquake struck off Chile&#39;s northern coast. " /><script type='text/javascript'>(function(e){if(typeof e.za24_exk=='undefined')e.za24_exk=new Array;if(typeof e.za24_exkt=='undefined')e.za24_exkt=new Array})(window)
window.za24_exkt.push('weather');window.za24_exk.push('20');
</script><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><meta property="article:published_time" content="2014/04/02 08:40:39 AM"/><meta property="article:modified_time" content="2014/04/02 08:40:39 AM"/><meta property="article:expiration_time" content="2014/04/04 09:59:30 AM"/><meta property="twitter:card" content="summary"/><meta property="twitter:url" content="http://www.news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402"/><meta property="twitter:title" content="Chile president cautious as 8.2 quake kills 5"/><meta property="twitter:site" content="News24"/><meta property="twitter:description" content="Authorities kept hundreds of thousands of people out of their beds after a magnitude-8.2 earthquake struck off Chile&#39;s northern coast. "/><meta property="twitter:image" content="http://cdn.24.co.za/files/Cms/General/d/2725/791dd800c8de44f194de27bc7ea86fac.jpg"/><meta property="twitter:app:name:iphone" content="News24"/><meta property="twitter:app:id:iphone" content="310970460"/><meta property="twitter:app:name:ipad" content="News24"/><meta property="twitter:app:id:ipad" content="310970460"/><meta property="twitter:app:url:iphone" content="https://itunes.apple.com/za/app/news24/id310970460?mt=8"/><meta property="twitter:app:url:ipad" content="https://itunes.apple.com/za/app/news24/id310970460?mt=8"/><meta property="og:site_name" content="News24"/><meta property="fb:app_id" content="2363277980"/><meta property="fb:page_id" content="10227041841"/><meta property="og:title" content="Chile president cautious as 8.2 quake kills 5"/><meta property="og:type" content="article"/><meta property="og:url" content="http://www.news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402"/><meta property="og:image" content="http://cdn.24.co.za/files/Cms/General/d/2233/e3756fe9d85942c9869789c22ce0963c.jpg"/><meta property="og:description" content="Authorities kept hundreds of thousands of people out of their beds after a magnitude-8.2 earthquake struck off Chile&#39;s northern coast. "/><link rel="canonical" href="http://www.news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402"/><script type="text/javascript" language="javascript">
var addthis_share =
{
url: "http://www.news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402",
title: "Chile president cautious as 8.2 quake kills 5",
description: "Authorities kept hundreds of thousands of people out of their beds after a magnitude-8.2 earthquake struck off Chile's northern coast.",
templates:
{
twitter: "{{title}}: {{url}} via @News24"
},
url_transforms: {
shorten: {
twitter: 'bitly'
}
},
shorteners: {
bitly: {
login: '24com',
apiKey: 'R_ca79efd5a0978fb80d1d853bac1dda83'
}}};
</script>
<title>
	Chile president cautious as 8.2 quake kills 5 | News24
</title><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /><meta name="verify-v1" content="7Ni+Om+G5YH4bPtmBOm+5Qih2e8WRykbCvNJXRK9vbg=" /><meta name="bitly-verification" content="267098cc5a65" />   
     <!-- Mobile viewport optimized: j.mp/bplateviewport //-->
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <!-- For non-Retina iPhone, iPod Touch, and Android 2.1+ devices: -->
    <link rel="apple-touch-icon" href="../../images/ios/bookapple-touch-icon.png" />
     <!-- For first- and second-generation iPad: -->
    <link rel="apple-touch-icon" sizes="76x76" href="../../images/ios/bookapple-touch-icon-76x76.png" />
    <!-- For iPhone with high-resolution Retina display running iOS = 7: -->
    <link rel="apple-touch-icon" sizes="120x120" href="../../images/ios/bookapple-touch-icon-120x120.png" />
    <!-- For iPad with high-resolution Retina display running iOS = 7: -->
    <link rel="apple-touch-icon" sizes="152x152" href="../../images/ios/bookapple-touch-icon-152x152.png" /><link rel="SHORTCUT ICON" href="/favicon.ico" />
    <script type='text/javascript'>var _sf_startpt = (new Date()).getTime()</script>
    <link type="text/css" rel="stylesheet" href="http://static.24.co.za/5/styles/complete.css?v=20140319" /><link type="text/css" rel="stylesheet" href="http://scripts.24.co.za/libs/fancybox/jquery.fancybox.css?v=20140319" />
<!--[if gte IE 7]>
<link href="http://www.news24.com/Styles/ie7.css" type="text/css" rel="stylesheet">
<![endif]-->
<!--[if IE 7]><link href='http://www.news24.com/Styles/ie7.css' type='text/css' rel='stylesheet'><![endif]--><script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/minified/basescript1.js?v=20140319" ></script><script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/fancybox/fancybox-1.3.4.min.js?v=20140319" ></script>
    <script type="text/javascript">
        var $j = jQuery.noConflict();var isHomePage = false;document.domain = "news24.com";
    </script>
    
    <script sync type="text/javascript" src="http://scripts.24.co.za/libs/24com/portal/1.0/common.min.js?v=20140319"></script><script type="text/javascript">var _gaq = _gaq || [];_gaq.push(['_setDomainName', 'www.news24.com']);_gaq.push(['_setAccount', 'UA-45055449-1']);_gaq.push(['_trackPageview']);
                                    (function() {var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                                    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                                    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
                                    })();</script>
    
    
    <link id="alternateLink" rel="alternate" media="only screen and (max-width: 640px)" href="http://m.news24.com/news24/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402"></link>
    

<meta name="keywords" content="michelle bachelet, chile, earthquakes" />
<meta name="news_keywords" content="michelle bachelet, chile, earthquakes" />
    <meta name="articleid" content="23a7c7b3-778f-44cc-8ce2-d9a79664db16"/>

<link href="http://scripts.24.co.za/libs/24com/comments/3.0.2/styles/comments.css" type="text/css" rel="stylesheet"></link>
<!-- Start of DClick Header -->
<!-- Site: /8900/24.com/Web/News24, Zone: /World/Articles, MapsTo: "News" -->

<script src='//www.googletagservices.com/tag/js/gpt.js' type='text/javascript' ></script>
<script src="http://scripts.24.co.za/libs/24com/Ads/3.0/24AdScript.min.js" language="JavaScript" type="text/javascript"></script>
<script language="JavaScript" type="text/javascript">//<![CDATA[
za24_AdSite = '/8900/24.com/Web/News24'; 
za24_AdZone = '/World/Articles';
za24_IsAsync  = false;
za24_InterstitialEnabled=false;
za24_KeywordType[1]='artid'; za24_Keywords[1]='23a7c7b3-778f-44cc-8ce2-d9a79664db16'; 
za24_KeywordType[2]='people'; za24_Keywords[2]='michelle bachelet'; 
za24_KeywordType[3]='places'; za24_Keywords[3]='chile'; 
za24_KeywordType[4]='topics'; za24_Keywords[4]='earthquakes'; 

za24_AdSize[1]='1000x1000'; za24_AdPositionNo[1]='1'; 
za24_AdSize[2]='728x90'; za24_AdPositionNo[2]='1'; 
za24_AdSize[3]='300x600'; za24_AdPositionNo[3]='1'; 
za24_AdSize[4]='300x250'; za24_AdPositionNo[4]='1'; 
za24_AdSize[5]='468x120'; za24_AdPositionNo[5]='1'; 
za24_AdSize[6]='10x10'; za24_AdPositionNo[6]='1'; 
za24_AdSize[7]='278x76'; za24_AdPositionNo[7]='1'; 
za24_AdSize[8]='278x35'; za24_AdPositionNo[8]='1'; 
za24_AdSize[9]='200x400'; za24_AdPositionNo[9]='1'; 
za24_AdSize[10]='980x90'; za24_AdPositionNo[10]='1'; 
za24_InitAds();
//--></script>
<!-- End of DClick Header -->
</head>
<body>
    <!-- Start Alexa Certify Javascript -->
<script type="text/javascript">
    _atrk_opts = { atrk_acct: "qhC0h1agYe00yl", domain: "news24.com", dynamic: true };
    (function () { var as = document.createElement('script'); as.type = 'text/javascript'; as.async = true; as.src = "https://d31qbv1cthcecs.cloudfront.net/atrk.js"; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(as, s); })();
</script>
<noscript><img src="https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=qhC0h1agYe00yl" style="display:none" height="1" width="1" alt="" /></noscript>
<!-- End Alexa Certify Javascript -->
    <!-- COPYRIGHT EFFECTIVE MEASURE -->
    <script type="text/javascript">
        (function () {var em = document.createElement('script'); em.type = 'text/javascript'; em.async = true;
            em.src = ('https:' == document.location.protocol ? 'https://za-ssl' : 'http://za-cdn') + '.effectivemeasure.net/em.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(em, s);})();
    </script>
    <noscript><img src="http://za.effectivemeasure.net/em_image" alt="" style="position: absolute; left: -5px;" /></noscript>
    <!--END EFFECTIVE MEASURE CODE -->
    <form name="aspnetForm" method="post" id="aspnetForm">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJNTM2NzE1MzM3ZGQlVxP6ZJN+2XCtQmjsSfI0jMtiNQ==" />
</div>


<script type="text/javascript">
//<![CDATA[
var za24_displayAdUrl = 'http://www.news24.com/static/Ads/DisplayAd.html';//]]>
</script>

<div class="aspNetHidden">

	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAAZmtpz0Cx1/kbJO1rl1SO3UfLgYOaxGNxpcxlKlT9IObQH+ih4MEySCBlfYlvG/lO3w/h12H3MZPLcouy1JL6NJpTNihxCpIUCa2K/Ulzjx5fwGEjiXfG6Ja/hBBVaFQfSXBTON8y95OyLKox9y9pF3cg7LjA==" />
</div>
       
        <script type="text/javascript">
jQuery('head').append("<link href='http://scripts.24.co.za/libs/24com/ads/2.0/Style/TransAd.css?v=20140319' type='text/css' rel='stylesheet' ></link>")
</script>
<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/ads/2.0/script/TransAd.min.js?v=20140319"></script>
<script type="text/javascript">AdTemplate = "News24";</script>
<div id='ad-10x10-1' class='24ad10x10'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('10x10','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=10x10&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=10x10&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
        

<div id="leaderboard">
    <div class="adCenter">
        <div style="background-color:transparent;border-bottom:3px solid transparent;border-left:0px solid transparent;border-right:3px solid transparent;">
	        <div id='ad-728x90-1' class='24ad728x90'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('728x90','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=728x90&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=728x90&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
    </div>
    
</div>
        <div class="main_wrap relative">
            

            
    

<script type="text/javascript" language="text/javascript">
    jQuery(function () {
        var pushdown = jQuery("#pushDownAd");
        if (pushdown.height() < 20) { pushdown.css("display", "none") }
    });
</script>


<div class="grid_12">
    <div id="header" class="relative">
        <h1 id="news24HeaderLogo">
            <a href="http://www.news24.com/" title="News24.com Home">News24 News. Breaking News. First</a>
        </h1>
        

<div class="absolute update_time">LAST UPDATED: 2014-04-02, 09:41</div>
        <div class="div_0 absolute"></div>

        <div class="absolute">              
            <div class="header_featured_article">
    <div class="feature_head first absolute">
        <a href="http://www.news24.com/World/News/Activists-say-Syria-conflict-death-toll-hits-150-344-20140401" id="lnkHeaderArtImage" target="_self"><img src="http://cdn.24.co.za/files/Cms/General/d/2725/e7c2d6575e3845249f0d0db7d4376b90.jpg" id="imgHeaderArticle" class="left" height="65" width="65" /></a>
        <h3 class="bold"><a href="http://www.news24.com/World/News/Activists-say-Syria-conflict-death-toll-hits-150-344-20140401" data-track="outbound,home-header,topcompo-Activists say Syria conflict death toll hits 150 344" target="_self">Activists say Syria conflict death toll hits 150 344</a></h3>
        <p>The death toll from Syria's 3-year conflict now exceeds 150 000, activists say as fighting rages on.</p>
    </div>
</div>

        </div>
        <div class="div_2 absolute"></div>

        
<div class="search_box absolute">
    <input id="txtSearchField" type="text" class="field absolute" onkeypress="var key=event.keyCode||event.which;if (key==13){submitSiteSearch(); return false;}" />
    <input type="submit" value="Search" class="btn absolute" onclick="submitSiteSearch(false);return false;" />   
</div>
<script type="text/javascript">
    var headerSearchUrl = 'http://www.news24.com/search?q={0}'; var headerAdvancedSearchUrl = 'http://googlesearch.news24.com/search?s=NWS&ref=NWS&q='; var txtSearchFieldClientId = "txtSearchField"; var btnSearchClientId = "btnSearch"; function submitSiteSearch() { var a = $j.trim($j("#" + txtSearchFieldClientId).val()); if (a.length > 0) { window.location.href = "/search?q=" + a } };
</script>
        

<div class="header_weather_box absolute">
    <div class="icon left">
    <a id="lnkModalItem" class="fireEventWeather weatherModal" style="display:none;"></a>
        <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=weather" id="lnkChangeWeather" class="city weatherModal" style="display: block">Cape Town</a>
        <img src="http://static.24.co.za/5/images/icons/forecastslarge/20.png" id="weatherImgMain" alt="Tons of rain. Morning clouds. Mild." />
    </div>
    <div class="div_3"></div>
    <div class="info left">
        <h2 id="mainTempDisplay">
            Wednesday
            <span>16-19&deg;C</span>
        </h2>
        <p id="mainDesc"><span id="spanMainDescription" style="cursor:default;" title="Tons of rain. Morning clouds. Mild.">Tons of rain. Morning clouds. Mild.</span></p>
        <ul id="weather_info_container">
            <li><a class="forecast absolute"  href="javascript:void(0)">7 day forecast</a> <!-- fire script here -->
                <ul id="weather_box_info" >
                    <li >
                        <table cellpadding="0" cellspacing="0" border="0" class="weather_drop_box">
                            
                                    <tr>
                                        <td class="d_day">Thursday</td>
                                        <td class="d_temp">16-22&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/2.png" alt="Mostly sunny. Mild." /></td>
                                        <td class="d_info">Mostly sunny. Mild.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Friday</td>
                                        <td class="d_temp">16-23&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/1.png" alt="Sunny. Mild." /></td>
                                        <td class="d_info">Sunny. Mild.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Saturday</td>
                                        <td class="d_temp">17-25&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/1.png" alt="Sunny. Warm." /></td>
                                        <td class="d_info">Sunny. Warm.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Sunday</td>
                                        <td class="d_temp">17-28&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/1.png" alt="Sunny. Pleasantly warm." /></td>
                                        <td class="d_info">Sunny. Pleasantly warm.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Monday</td>
                                        <td class="d_temp">21-29&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/2.png" alt="Mostly sunny. Warm." /></td>
                                        <td class="d_info">Mostly sunny. Warm.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Tuesday</td>
                                        <td class="d_temp">21-27&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/2.png" alt="More sun than clouds. Warm." /></td>
                                        <td class="d_info">More sun than clouds. Warm.</td>
                                    </tr>
                                
                            <tr>
                                <td colspan="4" height="10" valign="bottom" style="vertical-align:bottom">
                                    <div style="height:1px;border-bottom:1px solid #C6C6C6"></div>
                                    <div style="height:1px;border-top:1px solid #fff"></div>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="4" class="d_more_link" valign="top">
                                    <a href="http://weather.news24.com/sa/cape-town">More weather from Weather24 ></a>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="4" class="ad_link">
                                    <div id='ad-278x35-1' class='24ad278x35'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('278x35','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/Homepage&sz=278x35&c=1937775045&t=posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/Homepage&sz=278x35&c=1937775045&t=posno%3d1' border='0' alt=''></a></noscript>
                                </td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
    <div class="div_4"></div>
    <div class="left prodPlacement">        
        <a href="http://pubads.g.doubleclick.net/gampad/clk?id=44943070&iu=/8900/24.com/Web/News24" id="lnkHeaderWeatherSponsor" target="blank">Brought to<br />
        you by:<br />
        <img src="http://cdn.24.co.za/files/Cms/General/d/1655/d7d2b40e358940f09f295f9a9621f1ac.jpg" id="imgHeaderWeatherSponsor" width="66" height="9" border="0" /></a>
    </div>
</div>
<script type='text/javascript'>if(typeof(topStoriesArray)  != 'undefined') topStoriesArray.push({'name':'Cape Town Mostly sunny. Mild. 16-19','url':'http://weather.news24.com','icon':'/images/icons/Forecasts/2.ico'});</script>
        
<div class="nav_bar absolute" style="z-index:50">
    <ul id='nav' onmouseover='RemoveSelections();' onmouseout='SetSelections(defaultTabId);'>
<li class='nav_item ' id='tablink0' ><a href="http://www.news24.com/" data-track="outbound,nav,1stlevel-News">News</a>
<ul>
<li ><a  href="http://www.news24.com/SouthAfrica" data-track="outbound,nav,2ndlevel-South Africa">South Africa</a></li><li ><a  href="http://www.news24.com/Elections" data-track="outbound,nav,2ndlevel-Elections">Elections</a></li><li ><a  href="http://www.news24.com/World" data-track="outbound,nav,2ndlevel-World">World</a></li><li ><a  href="http://www.news24.com/Africa" data-track="outbound,nav,2ndlevel-Africa">Africa</a></li><li ><a  href="http://www.channel24.co.za" data-track="outbound,nav,2ndlevel-Entertainment">Entertainment</a></li><li ><a  href="http://www.news24.com/Green" data-track="outbound,nav,2ndlevel-Green">Green</a></li><li ><a  href="http://www.health24.com/news/1.asp" data-track="outbound,nav,2ndlevel-Health">Health</a></li></ul></li>
<li class='nav_item ' id='tablink1' ><a href="http://www.news24.com/Opinions" data-track="outbound,nav,1stlevel-Opinion">Opinion</a>
<ul>
<li><a href="http://voices.news24.com" data-track="outbound,nav,2ndlevel-Voices">Voices</a></li><li><a href="http://www.news24.com/MyNews24" data-track="outbound,nav,2ndlevel-MyNews24">MyNews24</a></li><li><a href="http://www.news24.com/Columnists" data-track="outbound,nav,2ndlevel-Columnists">Columnists</a></li></ul>
</li>
<li class='nav_item ' id='tablink2' ><a href="http://www.fin24.com" data-track="outbound,nav,1stlevel-Business">Business</a>
<ul>
<li ><a  href="http://www.fin24.com" data-track="outbound,nav,2ndlevel-News">News</a></li><li ><a  href="http://www.fin24.com/Markets" data-track="outbound,nav,2ndlevel-Markets">Markets</a></li><li ><a  href="http://www.fin24.com/Money/" data-track="outbound,nav,2ndlevel-Personal Finance">Personal Finance</a></li><li ><a  href="http://www.fin24.com/Opinion/Columnists/" data-track="outbound,nav,2ndlevel-Opinion">Opinion</a></li><li ><a  href="http://www.fin24.com/login" data-track="outbound,nav,2ndlevel-My Profile">My Profile</a></li></ul></li>
<li class='nav_item ' id='tablink3' ><a href="http://www.sport24.co.za" data-track="outbound,nav,1stlevel-Sport">Sport</a>
<ul>
<li ><a  href="http://www.sport24.co.za/" data-track="outbound,nav,2ndlevel-News">News</a></li><li ><a  href="http://www.sport24.co.za/Rugby/" data-track="outbound,nav,2ndlevel-Rugby">Rugby</a></li><li ><a  href="http://www.sport24.co.za/Cricket/" data-track="outbound,nav,2ndlevel-Cricket">Cricket</a></li><li ><a  href="http://www.sport24.co.za/Soccer/" data-track="outbound,nav,2ndlevel-Soccer">Soccer</a></li><li ><a  href="http://www.sport24.co.za/Golf/" data-track="outbound,nav,2ndlevel-Golf">Golf</a></li><li ><a  href="http://www.sport24.co.za/Tennis" data-track="outbound,nav,2ndlevel-Tennis">Tennis</a></li><li ><a  href="http://www.wheels24.co.za/FormulaOne/" data-track="outbound,nav,2ndlevel-Formula1">Formula1</a></li><li ><a  href=" http://www.sport24.co.za/OtherSport" data-track="outbound,nav,2ndlevel-Other Sport">Other Sport</a></li><li class='red'><a class='red' href="http://www.supersport.com/" data-track="outbound,nav,2ndlevel-SuperSport">SuperSport</a></li><li class='red'><a class='red' href="http://www.supersport.com/live-video" data-track="outbound,nav,2ndlevel-Live Streaming">Live Streaming</a></li><li class='red'><a class='red' href="http://www.supersport.com/video" data-track="outbound,nav,2ndlevel-Video Highlights">Video Highlights</a></li></ul></li>
<li class='nav_item no_arrow' id='tablink4' ><a href="http://www.news24.com/Technology" data-track="outbound,nav,1stlevel-Tech">Tech</a>
<li class='nav_item ' id='tablink5' ><a href="http://www.wheels24.co.za" data-track="outbound,nav,1stlevel-Motoring">Motoring</a>
<ul>
<li ><a  href="http://www.wheels24.co.za/news" data-track="outbound,nav,2ndlevel-News">News</a></li><li ><a  href="http://www.wheels24.co.za/NewModels/" data-track="outbound,nav,2ndlevel-New Models">New Models</a></li><li ><a  href="http://www.wheels24.co.za/4x4/" data-track="outbound,nav,2ndlevel-4x4">4x4</a></li><li ><a  href="http://www.wheels24.co.za/FormulaOne/" data-track="outbound,nav,2ndlevel-Formula One">Formula One</a></li><li ><a  href="http://www.wheels24.co.za/Motorsport/" data-track="outbound,nav,2ndlevel-Motorsport">Motorsport</a></li><li ><a  href="http://www.wheels24.co.za/BikesQuads/" data-track="outbound,nav,2ndlevel-Bikes">Bikes</a></li><li ><a  href="http://www.wheels24.co.za/Your-Wheels/" data-track="outbound,nav,2ndlevel-Your Wheels">Your Wheels</a></li></ul></li>
<li class='nav_item ' id='tablink6' ><a href="http://www.news24.com/Lifestyle" data-track="outbound,nav,1stlevel-Lifestyle">Lifestyle</a>
<ul>
<li ><a  href="http://www.health24.com/" data-track="outbound,nav,2ndlevel-Health">Health</a></li><li ><a  href="http://www.women24.com" data-track="outbound,nav,2ndlevel-Women">Women</a></li><li ><a  href="http://www.wheels24.co.za" data-track="outbound,nav,2ndlevel-Motoring">Motoring</a></li><li ><a  href="http://www.food24.com" data-track="outbound,nav,2ndlevel-Food">Food</a></li><li ><a  href="http://www.news24.com/Travel" data-track="outbound,nav,2ndlevel-Travel">Travel</a></li><li ><a  href="http://www.channel24.co.za/" data-track="outbound,nav,2ndlevel-Entertainment">Entertainment</a></li><li class='red'><a class='red' href="http://www.women24.com/rubybox" data-track="outbound,nav,2ndlevel-Shop Beauty">Shop Beauty</a></li><li ><a  href="http://www.parent24.com" data-track="outbound,nav,2ndlevel-Parent">Parent</a></li><li ><a  href="http://www.lazygamer.net" data-track="outbound,nav,2ndlevel-Games">Games</a></li><li class='red'><a class='red' href="http://www.mweb.co.za/games/Home.aspx?ref=news24nav" data-track="outbound,nav,2ndlevel-GameZone">GameZone</a></li><li class='red'><a class='red' href="http://love2meet.news24.com/s/" data-track="outbound,nav,2ndlevel-Dating">Dating</a></li></ul></li>
<li class='nav_item ' id='tablink7' ><a href="http://www.news24.com/Multimedia" data-track="outbound,nav,1stlevel-Multimedia">Multimedia</a>
<ul>
<li><a href="http://www.news24.com/multimedia" data-track="outbound,nav,2ndlevel-News">News</a></li><li><a href="http://www.sport24.co.za/multimedia" data-track="outbound,nav,2ndlevel-Sport">Sport</a></li><li><a href="http://www.channel24.co.za/Multimedia" data-track="outbound,nav,2ndlevel-Entertainment">Entertainment</a></li><li><a href="http://www.wheels24.co.za/multimedia" data-track="outbound,nav,2ndlevel-Motoring">Motoring</a></li><li><a href="http://www.women24.com/multimedia" data-track="outbound,nav,2ndlevel-Women">Women</a></li><li><a href="http://www.food24.com/multimedia" data-track="outbound,nav,2ndlevel-Food">Food</a></li><li><a href="http://www.parent24.com/multimedia" data-track="outbound,nav,2ndlevel-Parenting">Parenting</a></li><li><a href="http://www.news24.com/travel/multimedia" data-track="outbound,nav,2ndlevel-Travel">Travel</a></li><li><a href="http://www.health24.com/multimedia" data-track="outbound,nav,2ndlevel-Health">Health</a></li><li><a href="http://www.news24.com/multimedia/video" data-track="outbound,nav,2ndlevel-From our Studio">From our Studio</a></li></ul>
</li>
<li class='nav_item ' id='tablink8' ><a href="http://www.news24.com/SpecialReports" data-track="outbound,nav,1stlevel-Focus">Focus</a>
<ul>
<li><a href="http://www.news24.com/obituaries" data-track="outbound,nav,2ndlevel-Obituaries">Obituaries</a></li><li><a href="http://www.news24.com/Content/Africa/Zimbabwe" data-track="outbound,nav,2ndlevel-Zimbabwe">Zimbabwe</a></li><li><a href="http://www.health24.com/Medical/HIV-AIDS" data-track="outbound,nav,2ndlevel-Aids Focus">Aids Focus</a></li><li><a href="http://www.m24i.co.za/" data-track="outbound,nav,2ndlevel-Media24 Investigations">Media24 Investigations</a></li><li><a href="http://www.news24.com/Tags/Topics/good_news" data-track="outbound,nav,2ndlevel-Good News ">Good News </a></li><li><a href="http://www.citypress.co.za/" data-track="outbound,nav,2ndlevel-City Press">City Press</a></li><li><a href="http://www.news24.com/competitions" data-track="outbound,nav,2ndlevel-Competitions">Competitions</a></li></ul>
</li>
<li class='nav_item ' id='tablink9' ><a href="http://isizulu.news24.com" data-track="outbound,nav,1stlevel-isiZulu">isiZulu</a>
<ul>
<li><a href="http://isizulu.news24.com/NingizimuAfrika" data-track="outbound,nav,2ndlevel-Ningizimu Afrika ">Ningizimu Afrika </a></li><li><a href="http://isizulu.news24.com/Izindaba-Zami" data-track="outbound,nav,2ndlevel-Izindaba-Zami">Izindaba-Zami</a></li><li><a href="http://isizulu.news24.com/Ezemidlalo" data-track="outbound,nav,2ndlevel-Ezemidlalo">Ezemidlalo</a></li><li><a href="http://isizulu.news24.com/Afrika" data-track="outbound,nav,2ndlevel-Afrika">Afrika</a></li><li><a href="http://isizulu.news24.com/Umhlaba" data-track="outbound,nav,2ndlevel-Umhlaba">Umhlaba</a></li><li><a href="http://isizulu.news24.com/Ezokuzijabulisa" data-track="outbound,nav,2ndlevel-Ezokuzijabulisa">Ezokuzijabulisa</a></li><li><a href="http://isizulu.news24.com/Ezamabhizinisi" data-track="outbound,nav,2ndlevel-Ezamabhizinisi">Ezamabhizinisi</a></li></ul>
</li>
<li class='nav_item no_arrow' id='tablink10' ><a href="http://www.news24.com/Jobs/" data-track="outbound,nav,1stlevel-Jobs">Jobs</a>
<li class='nav_item no_arrow' id='tablink11' ><a href="http://www.news24.com/Property/" data-track="outbound,nav,1stlevel-Property">Property</a>
</ul>
<ul id='nav' onmouseover='RemoveSelections();' onmouseout='SetSelections(defaultTabId);'>
<li id='liContainer' class='sponsor_img'><a id='lnkSpecialNav' href='http://pubads.g.doubleclick.net/gampad/clk?id=51989710&iu=/8900/24.com/Web/News24' target='_self'><img id='lnkImg' src='http://cdn.24.co.za/files/Cms/General/d/2440/3f222735f4a746ab83d2b4d0b5955f73.gif' /></a>
<ul class='sponsor'>
<li class='sponsor-list-item'><a href='http://pubads.g.doubleclick.net/gampad/clk?id=57613510&iu=/8900/24.com/Web/News24' target='_self' data-track="outbound,nav,2ndlevel-Car Insurance">Car Insurance</a>
<li class='sponsor-list-item'><a href='http://pubads.g.doubleclick.net/gampad/clk?id=57613750&iu=/8900/24.com/Web/News24' target='_self' data-track="outbound,nav,2ndlevel-Home Insurance">Home Insurance</a>
<li class='sponsor-list-item'><a href='http://pubads.g.doubleclick.net/gampad/clk?id=57613990&iu=/8900/24.com/Web/News24' target='_self' data-track="outbound,nav,2ndlevel-Building Insurance">Building Insurance</a>
</ul>
</li>
</ul>

</div>
<script type='text/javascript'>menuJsonArray = [{"Url":"http://www.news24.com/SouthAfrica","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/Elections","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/World","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/Africa","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/Green","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://voices.news24.com","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/mynews24","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/columnists","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/Opinions","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/Technology","TabLinkIndex":4,"TabLinkToActivate":"tablink4"},{"Url":"http://www.news24.com/Travel","TabLinkIndex":6,"TabLinkToActivate":"tablink6"},{"Url":"http://love2meet.news24.com/s/","TabLinkIndex":6,"TabLinkToActivate":"tablink6"},{"Url":"http://www.news24.com/Lifestyle","TabLinkIndex":6,"TabLinkToActivate":"tablink6"},{"Url":"http://www.news24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.sport24.co.za/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.channel24.co.za/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.wheels24.co.za/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.women24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.food24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.parent24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/travel/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.health24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/multimedia/video","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/Multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/obituaries","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/africa/zimbabwe","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.health24.com/medical/hiv-aids","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.m24i.co.za/","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/tags/topics/good_news","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.citypress.co.za/","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/competitions","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/SpecialReports","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://isizulu.news24.com/ningizimuafrika","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/izindaba-zami","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/ezemidlalo","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/afrika","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/umhlaba","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/ezokuzijabulisa","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/ezamabhizinisi","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://www.news24.com/Jobs/","TabLinkIndex":10,"TabLinkToActivate":"tablink10"},{"Url":"http://www.news24.com/Property/","TabLinkIndex":11,"TabLinkToActivate":"tablink11"}];</script>

<script type="text/javascript" language="javascript">
    if ('False' == 'True')
        document.getElementById('main_nav').style.height = '33px';
</script>
    </div>
</div>
<div class="clear"></div>
<div id="pushDownAd">
    <div class="clear"></div>
    <div id='ad-980x90-1' class='24ad980x90'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('980x90','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=980x90&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=980x90&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>        
    <div class="clear"></div>
</div>
    <div class="container_12">
        <div class="clr10">&nbsp;</div>
        <div class="content_wrap socialnewsbasefix">
            <div class="left col640">
                
                
    <div id="article_special">
        

<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/article/1.0/articleGreyLinks.js"></script>
<script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/jquery.hoverintent.min.js?v=20140319" ></script>
<script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/jquery.cluetip.min.js?v=20140319" ></script>

<div class="article col626">
    
    <div class="spacer clr"></div>
	<h1 class="bold">Chile president cautious as 8.2 quake kills 5</h1>
	<span id="spnDate" class="block datestamp">2014-04-02 08:40</span>
	<div class="col300 right">
	    
	    <div class="spacer clr"></div>
        
        <div id="fb-root"></div>
<script type="text/javascript">
 (function (d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
 js.src = "//connect.facebook.net/en_GB/all.js#xfbml=1&appId=2363277980";
fjs.parentNode.insertBefore(js, fjs);
} (document, 'script', 'facebook-jssdk'));
</script>
<script type="text/javascript">
window.fbAsyncInit = function () {FB.Event.subscribe('edge.create', function (response) {
GA24.trackEvent('articles,sharelinks,fblike');
});};
var pinteresturl = '//assets.pinterest.com/js/pinit.js'
var twitterurl = '//platform.twitter.com/widgets.js'
var addthisurl ='//s7.addthis.com/js/250/addthis_widget.js#username=zamedia24'
$j.ajaxSetup({cache: true});
$j.getScript(pinteresturl)
$j.getScript(twitterurl)
$j.getScript(addthisurl,function(){
if(typeof(addthis) != 'undefined'){
$j('#article_toolbox_topright').show();
addthis.addEventListener('addthis.menu.share', function(evt) {
GA24.trackEvent('articles,sharelinks,' + evt.data.service);
});
}
});
$j.ajaxSetup({cache: false});
var addthis_config ={username: 'zamedia24',services_exclude: 'email,print',ui_open_windows: true,ui_language: 'en' };function googlePlusOneShareLink() {GA24.trackEvent('articles,sharelinks,googleplusone');
}function OpenPrintWindowShare() {var printUrl = 'http://www.news24.com/printArticle.aspx?iframe&aid=23a7c7b3-778f-44cc-8ce2-d9a79664db16&cid=1073';window.open(printUrl,'myPrintWindow','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=750,height=600');}</script><div class="spacer clr"></div>
<div id="article_toolbox_topright" style="border-bottom:solid #ebebeb 0px; border-top:solid #ffffff 1px; padding-left:0px;display:none;">
<div class="addthis_toolbox">
<a class="addthis_button_facebook_like" fb:like:action="recommend" fb:like:show_faces="false" fb:like:layout="button_count" fb:like:send="false"></a>
<a class="addthis_button_google_plusone" g:plusone:size="medium"></a>
<span><a href="http://pinterest.com/pin/create/button/?url=http://www.news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402" class="pin-it-button" count-layout="horizontal">Pin It</a></span>
</div>
<div class="addthis_toolbox">
<a class="addthis_button_twitter"><span></span></a>
<a class="addthis_button_facebook"><span></span></a>
<a class="addthis_button at300b"><span></span></a>
<a class="email group" href="http://www.news24.com/sendToFriend.aspx?iframe&aid=23a7c7b3-778f-44cc-8ce2-d9a79664db16&cid=1073" title="Email"><span></span></a>
<a class="print" onclick="OpenPrintWindowShare()" title="Print"><span></span></a>
</div>
</div>
<div id="marging10Bottom"></div>

        <div class="spacer clr"></div>
	    

<script language="javascript" type="text/javascript">
    function popUP(url) {
        newwindow = window.open(url, 'name', 'height=800,width=500,scrollbars=yes,left=400');
        if (window.focus) { newwindow.focus() }
        return false;
    }
</script>

<div id="article_feature">
	<img id="image" title="Michelle Bachelet (File, AFP)" src="http://cdn.24.co.za/files/Cms/General/d/2233/e3756fe9d85942c9869789c22ce0963c.jpg" alt="Michelle Bachelet (File, AFP)" />
	<p class="text">Michelle Bachelet (File, AFP)</p>
	<p class="bold">
	    <a id="lnkGalleries" href="http://www.news24.com/Multimedia">Multimedia</a>  &nbsp; · &nbsp; <a id="lnkUserGalleries" href="http://www.news24.com/Multimedia/MyNews24">User Galleries</a> &nbsp; · &nbsp; <a id="lnkNewsGalleries" href="http://www.news24.com/Multimedia/Category-Images">News in Pictures</a>
	    <span class="block red"><a class="group" href="http://uploads.news24.com?iframe">Send us your pictures</a>  &nbsp;·&nbsp; <a class="group" href="http://www.news24.com/FeedBack.aspx?iframe">Send us your stories</a></span>
	</p> 
</div>

	    <div class="spacer clr"></div>
        
        <div class="spacer clr"></div>	
	    

<script type="text/javascript">
    function scrollalert() { var a = $j("#scrollbox"); var b = $j("#scrollbox > #content"); if (a.length > 0) { if (a.length > 0 && a.scrollTop && b.height() <= a.scrollTop() + a.height() + 20) { $j("#imgAjaxLoad").show(); var data = { 'tag': $j("#hfTag").val(), 'tagGroup': $j("#hfTagGroup").val(), 'CurrentSiteId': "5", 'CmsArticleId': "23a7c7b3-778f-44cc-8ce2-d9a79664db16", 'index': $j("#hfBottomIndex").val(), 'selectedArticleIndex': $j("#hfSelectedArticleIndex").val(), 'directionToFetch': "Down" }; news24.getAjax("/Ajax/ArticleData/", "BuildArticleListByTag", data, onSuccessBottom, onFail) } setTimeout("scrollalert();", 500) } } function onSuccessBottom(a) { var b = parseInt($j("#hfBottomIndex").val()); if (a != "" && a != null) { $j("#hfBottomIndex").val(b + 5); setTimeout("$j('#imgAjaxLoad').hide();", 1e3); var c = $j("#RelatedLinks").html() + a; $j("#RelatedLinks").html(c) } else { setTimeout("$j('#imgAjaxLoad').hide();", 1e3); $j("#hfBottomIndex").val(-1) } } function onSuccessTop(a) { var b = parseInt($j("#hfTopIndex").val()); if (a != "" && a != null) { $j("#hfTopIndex").val(b - 5); setTimeout("$j('#imgAjaxLoad').hide();", 1e3); var c = a + $j("#RelatedLinks").html(); $j("#RelatedLinks").html(c); $j("#scrollbox").scrollTo("10") } else { setTimeout("$j('#imgAjaxLoad').hide();", 1e3); $j("#hfTopIndex").val(-1) } } function onFail() { } $j("document").ready(function () { scrollalert(); $j("#imgAjaxLoad").hide() })
</script>

<div id="relatedlinks_box">
    <div class="left"><h5 id="Relatedheader" class="bold">Related Links</h5><a id="taglink" class="relatedTag"></a></div>
    <div class="right"></div>
    <div class="clr"></div>
    
    
            <ul>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-Earthquake, tsunami hits Chile 5 dead" href="http://www.news24.com/Green/News/Earthquake-tsunami-hits-Chile-5-dead-20140402">Earthquake, tsunami hits Chile 5 dead</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-8.2 quake hits northern Chile" href="http://www.news24.com/World/News/5-dead-as-82-quake-hits-northern-Chile-20140402">8.2 quake hits northern Chile</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-Chile hit by 6.7 earthquake" href="http://www.news24.com/Green/News/Chile-hit-by-67-earthquake-20140317">Chile hit by 6.7 earthquake</a></li>
        
            </ul>
        
    
    
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfTopIndex" id="hfTopIndex" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfBottomIndex" id="hfBottomIndex" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfTag" id="hfTag" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfTagGroup" id="hfTagGroup" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfSelectedArticleIndex" id="hfSelectedArticleIndex" />
</div>
	    

<div class=" rowdivider clr"></div>
<div class="kalahari_product left">
    <div id="pnlKalahariListing">
	
        
                <div>
                    <h4 class="left"><a href="http://etrader.kalahari.net/referral.asp?linkid=1869&partnerid=9113" target="_blank">kalahari.com</a></h4>
                    <ul class="left">
                        <li>
                            <a href="http://etrader.kalahari.net/referral.asp?linkid=5&amp;partnerid=9113&amp;sku=32603014" target="_blank">Earthquakes</a><br />
                            Focuses on the furious power of nature unleashed.
                            
                            Now R778.00
                            <br />
                            <a class="buynow" href="http://etrader.kalahari.net/referral.asp?linkid=5&amp;partnerid=9113&amp;sku=32603014" target="_blank">buy now</a>
                        </li>
                    </ul>
                </div>
            
    
</div>
    
</div>
<div class=" rowdivider clr"></div>
	    
        
	</div>
	<div class="ByLineWidth">
		<p class="left"></p>
	</div>
	<p class="clr_left">Santiago - Authorities kept hundreds of thousands of people out of their beds early on Wednesday after a magnitude-8.2 earthquake struck off Chile's northern coast. <br /><br />Five people were crushed to death or suffered fatal heart attacks, a remarkably low toll for such a powerful shift in the Earth's crust.<br /><br />The extent of damage from Tuesday night's quake couldn't be fully assessed before daybreak, President Michelle Bachelet said, but she wasn't taking any chances. She declared a state of emergency in the region and sent a military plane with 100 anti-riot police to join 300 soldiers deployed to prevent looting and round up escaped prisoners.<br /><br />The shaking loosed landslides that blocked roads, knocked out power for thousands, damaged an airport and provoked fires that destroyed several businesses. About 300 inmates escaped from a women's prison in the city of Iquique. <br /><br />In Arica, another city close to the quake's offshore epicentre, hospitals treated minor injuries, and some homes made of adobe were destroyed, authorities said. Chilean Interior Minister Rodrigo Penailillo announced the five deaths.<br /><br />Bachelet's government extended its tsunami warnings for northernmost Chile long after they were lifted elsewhere. Its mandatory evacuation orders remained in effect until nearly dawn for coastal areas north of Antofogasta, a decision backed by the Pacific Tsunami Warning Centre in Hawaii.<br /><br />"We regard the coast line of Chile as still dangerous, so we're maintaining the warning," geophysicist Gerard Fryer told The Associated Press.<br /><br /><strong>Significant aftershocks</strong><br /><br />Bachelet, who just returned to the presidency three weeks ago, spoke well after midnight, five hours after the quake struck.<br /><br />It was not lost on many Chileans that the last time she presided over a major quake, days before the end of her 2006-10 term, her emergency preparedness office prematurely waved off a tsunami danger.<br /><br />Most of the 500 dead from that magnitude-8.8 tremor survived the shaking, only to be caught in killer waves in a disaster that destroyed 220 000 homes and washed away large parts of many coastal communities.<br /><br />"The country has done a good job of confronting the emergency. I call on everyone to stay calm and follow the authorities' instructions," Bachelet tweeted after Tuesday night's temblor.<br /><br />When she finally addressed the nation, she said her interior minister would monitor the tsunami threat throughout the night and co-ordinate the emergency response. "Classes have been suspended, and we will be able to know the extent of the damage in the light of day," she added.<br /><br />The tsunami warning centre cancelled tsunami watches for areas other than northern Chile and southern Peru. The only US impact might be higher waves on Wednesday for Hawaii's swimmers and surfers, it said.<br /><br />The US Geological Survey initially reported the quake at 8.0, but later upgraded the magnitude of the quake that struck 99km northwest of Iquique. <br /><br />More than 20 significant aftershocks followed, including a 6.2 tremor. More aftershocks and even a larger quake could not be ruled out, said seismologist Mario Pardo at the University of Chile.<br /><br />Psychiatrist Ricardo Yevenes said he was with a patient in Arica when the big one hit.<br /><br />"It quickly began to move the entire office, things were falling," he told local television. "Almost the whole city is in darkness."<br /><br />The quake was so strong that the shaking experienced in Bolivia's capital about 470km away was the equivalent of a 4.5-magnitude tremor, authorities there said.<br /><br />Chile is one of the world's most earthquake-prone countries because just off the coast, the Nazca tectonic plate plunges beneath the South American plate, pushing the towering Andes cordillera to ever-higher altitudes.<br /><br />The latest activity began with a strong magnitude-6.7 quake on 16 March that caused more than 100 000 people to briefly evacuate low-lying areas. <br /><br />Hundreds of smaller quakes followed in the weeks since, keeping people on edge as scientists said there was no way to tell if the unusual string of tremors was a harbinger of an impending disaster.<br /></p>
    
	<div id="_htmlAccreditationName">- AP</div>
	
	<p></p>
	


<div id="divKeywordsListing" class="read_more_slider">
    
            <b style="color:Gray">Read more on: &nbsp;&nbsp;</b>
        
            <b><a style="color:#0E2E5E;" href="/Tags/People/michelle_bachelet">michelle bachelet</a></b>                     
        &nbsp;|&nbsp;
            <b><a style="color:#0E2E5E;" href="/Tags/Places/chile">chile</a></b>                     
        &nbsp;|&nbsp;
            <b><a style="color:#0E2E5E;" href="/Tags/Topics/earthquakes">earthquakes</a></b>                     
        
</div>
    

<script type="text/javascript">
    function ReadMoreAction() { if ($j("div.read_more_slider").is(":inView") && !hidden) { $j("div#readMoreSlider").animate({ right: 0 }, 400); sliderVisible = true; isLoaded++; if (isLoaded == 1) { GA24.trackEvent("World-next-articlebox, show") } } } function HideReadMoreAction() { $j("div#readMoreSlider").animate({ right: -3e3 }, 400); sliderVisible = false } function CloseAction() { HideReadMoreAction(); hidden = true } var isLoaded = 0; var sliderVisible = false; var hidden = false; $j.extend($j.expr[":"], { inView: function (e) { return $j(e).offset().top + $j(e).height() <= $j(window).scrollTop() + $j(window).height() } }); $j(function () { setInterval("ReadMoreAction();", 500) }); $j(function () { var e = $j(window).scrollTop(); var t = e + $j(window).height(); var n = $j("div.read_more_slider").offset().top; var r = n + $j("div.read_more_slider").height(); return r <= t })
</script>
<div id="readMoreSlider">
    <div class="slider_title"><span>NEXT ON NEWS24</span><span class="right" style="cursor:pointer;" onclick="CloseAction()">X</span></div>
    <div class="slider_content">
        <a href='http://www.news24.com/World/News/Jet-mystery-may-never-be-solved-Malaysia-police-20140402' data-track="outbound,nextarticlebox"><img src="http://cdn.24.co.za/files/Cms/General/d/89/2c9c943a628d41d7ac8d7f796a68a511.jpg" id="imgArticle" class="left" height="65" width="65" /></a>
	    <h4 class="bold"><a href='http://www.news24.com/World/News/Jet-mystery-may-never-be-solved-Malaysia-police-20140402' data-track="outbound,nextarticlebox" style="color:#fff;">Jet mystery may never be solved - Malaysia police</a></h4>
	    <div class="wrap_stampcomment" style="margin-top:10px;">
            <span class="block datestamp left" style="font-size:12px;color:#fff;">2014-04-02 08:23</span>
        </div>
    </div>
</div>
	<p></p>
    
</div>
<script type="text/javascript">
    $j(document).ready(function () { var a = $j("a.tips"); a.each(function () { var a = $j(this); a.attr("rel", "/Handlers/WhosWhoTooltip.ashx?url=" + a.attr("rel")) }); a.cluetip({ positionBy: "fixed", topOffset: "-230", leftOffset: "-30", sticky: true, dropShadow: false, showTitle: false, mouseOutClose: true, closeText: "", cluezIndex: 5100 }) })
</script>
        <div class="spacer clr">
            </div>
        

<script type="text/javascript" language="javascript">
	function openPrintWindow() {
		myPrintWindow = window.open('http://www.news24.com/printArticle.aspx?iframe&aid=23a7c7b3-778f-44cc-8ce2-d9a79664db16&cid=1073','myPrintWindow','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=750,height=600');
	}
</script>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#username=zamedia24"></script>
<div id="article_toolbox_bot" class="col626 left">
	<ul>
		<li class="email left" /><a class="group" href="http://www.news24.com/sendToFriend.aspx?iframe&aid=23a7c7b3-778f-44cc-8ce2-d9a79664db16&cid=1073">Email article</a>
		<li class="print left" /><a onclick="openPrintWindow()" href="#">Print article</a>
		<li class="get left" />GET NEWS24 ON: 
		<li class="mobile left" /><a href="http://mobile.24.com/?p=minisite_news">Your mobile</a>
		<li class="facebook left"/><a href="http://www.facebook.com/apps/application.php?api_key=90f449e533cd94a11213682bc9b2a23c">Your Facebook profile</a>
		<li class="clr" />
		<li class="share left" />SHARE:
		
	</ul>
	
	<div class="addthis_toolbox addthis_default_style">
	  <a class="addthis_button_facebook">Facebook</a>
	  <a class="addthis_button_twitter">Twitter</a>
	  <a class="addthis_button_google">Google</a>
	  <a class="addthis_button_digg">Digg</a>
	  <a class="addthis_button_delicious">Delicious</a>
	  <a class="addthis_button_yahoobkm">Yahoo</a>
	  <a class="addthis_button_compact" >More...</a>
	</div>
</div>
        <div class="spacer clr">
            </div>
        <div class="col620 adfix">
            <div id='ad-468x120-1' class='24ad468x120'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('468x120','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=468x120&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=468x120&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
        <div class="spacer clr">
            </div>
        <div class="col626">
            

<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/comments/3.0.2/scripts/comments.min.js"></script>
<script type="text/javascript" src="http://scripts.24.co.za/libs/json/json2.js"></script>
<script type="text/javascript">
    jQuery(function () {
        if (typeof onLogin !== "function") {
            jQuery.getScript("http://scripts.24.co.za/libs/24com/tina/1.0/LoginWindow.js");
        }
    });

    $j(function() {
        if (typeof commentControl !== "undefined") {
            // settings
            commentControl.sortOrder = "Asc";
            commentControl.pageSize = 20;
            commentControl.tinaBaseUrl = "http://auth.news24.com";
            commentControl.commentStatus = "Unmoderated";
            commentControl.lang = false ? "af" : "en";
            commentControl.locale = "en-za";
            commentControl.site = "News24";
            commentControl.breadCrumb = "News24|World|News" ;
            commentControl.objectId = "23a7c7b3-778f-44cc-8ce2-d9a79664db16";
            commentControl.isDev = false ;
            commentControl.canShowPostedComment = true ;
            commentControl.logOutUrl = "http://auth.news24.com/DeAuthenticate.aspx?surl=http://www.news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402";
            commentControl.auth.user.id = "00000000-0000-0000-0000-000000000000";
            commentControl.auth.user.displayName = "";
            commentControl.auth.user.clickThrough = "";
            commentControl.auth.user.avatarUrl = "http://cdn.24.co.za/Files/RAP2/d/DefaultAvatar/Small.png";
            commentControl.auth.user.openIdType = 0 ;
            commentControl.FacebookHandlerUrl = "http://www.news24.com/FacebookToken.ashx";
            commentControl.cacheFacebookAvatar = true;
            commentControl.policyLink = "http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109";
            if (commentControl.auth.util.isFacebookProfile("")) {
                commentControl.auth.user.facebookProfileId = commentControl.auth.util.getFbProfileIdFromAvatarUrl("");
            }
            commentControl.init();
        }
    });
  
</script>
<p style="margin-bottom: 10px; margin-top: 5px;">
<a href="http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109">Read News24’s Comments Policy</a>
</p>



<div class="facebookComments">
    <p>24.com publishes all comments posted on articles provided that they adhere to our <a href="http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109" target="_blank" style="color:white;cursor:pointer;">Comments Policy</a>. Should you wish to report a comment for editorial review, please do so by clicking the 'Report Comment' button to the right of each comment.</p>
</div>
    <div id="comments_wrap">
        <div id="comment_on_story">
            <div class="fl">
                Comment on this story
            </div>
            <div class="xsmall normal to_lower fl" id="comment_count_wrap">
                <span id="lblTotalCommentCount">1</span>&nbsp;<span id="lblTotalCommentCountText">comment</span>
            </div>
            <div class="clr"></div>
        </div>

        
            <div class="comment_form_wrap" id="comment_article_form">
                <div class="comment_form_header to_upper bold">Add your comment</div>
                <div class="comment_form_result_msg bold hidden">Thank you, your comment has been submitted.</div>
                <div class="comment_form_user">
                    <div class="avatar_wrap fl">
                        <div><img alt="avatar" class="user_avatar_img" /></div>
                    </div>
                    <div class="author_name fl">
                        <a href="#" target="_blank" class="author_link bold user_name"></a>
                    </div>
                    <div class="logout_wrap fr">
                        <a href="#" class="smlr logout_link">Logout</a>
                    </div>
                    <div class="clr"></div>
                </div>
                <div class="comment_form_inner">
                    <span class="comment_form_label bold">Comment</span>
                    <span class="comment_form_remaining_text xsmall italic"><span>0</span> characters remaining</span>
                    <div class="textarea_wrap"><textarea rows="4"></textarea></div>
                    <div id="divFacebookCheckbox" class="facebook_checkbox">
                        <input type="checkbox" id="chk_facebook" checked="checked" /> <label for="chk_facebook" class="smlr">Share on Facebook</label>
                    </div>
                    <input type="button" value="Post Comment" class="button_submit to_upper smlr" />
                    <div class="ajax-loader hidden"></div>
                </div>
            </div>
        
        
        <div id="comments_list"></div>
        
        <div id="comment_reusables" class="hidden">
            <div class="comment_form_wrap" id="comment_reply_form">
                <div class="comment_form_header to_upper bold"></div>
                <div class="comment_form_user">
                    <div class="avatar_wrap fl">
                        <div><img alt="avatar" class="user_avatar_img" /></div>
                    </div>
                    <div class="author_name fl">
                        <a href="#" target="_blank" class="author_link bold user_name"></a>
                    </div>
                    <div class="logout_wrap fr">
                        <a href="#" class="smlr logout_link">Logout</a>
                    </div>
                    <div class="clr"></div>
                </div>
                <div class="comment_form_inner">
                    <span class="comment_form_label bold">Comment</span>
                    <span class="comment_form_remaining_text xsmall italic"><span>0</span> characters remaining</span>
                    <div class="textarea_wrap"><textarea rows="4"></textarea></div>
                    <div id="divFacebookCheckboxReply" class="facebook_checkbox">
                        <input type="checkbox" id="chk_facebook_reply" checked="checked" /> <label for="chk_facebook_reply" class="smlr">Share on Facebook</label>
                    </div>
                    <input type="button" value="Post Comment" class="button_submit to_upper smlr" />
                    <div class="ajax-loader hidden"></div>
                </div>
            </div>
        </div>

        <div id="comment_loader" class="hidden">
            <img src="http://scripts.24.co.za/libs/24com/comments/2.7/images/ajax-loader.gif" alt="Loading comments..." /> Loading comments...
        </div>

        <input type="button" id="btn_load_more" class="hidden to_upper smlr" value="Load More Comments" />
    </div>

        </div>
        <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/24com/contentrecommendation/2.0/keywordlogger.min.js?v=20140319" ></script>
<div id="other_stories" class="col626 left">
    <div id="googleAdContainer" style="float: left">
        <script type="text/javascript">
            google_ad_client = "pub-0710600889784454"; google_ad_slot = "5629899714"; google_ad_width = 336; google_ad_height = 280; $j(document).ready(function () { var data = { 'categoryBreadcrumb': 'World/News', 'articleId': '23a7c7b3-778f-44cc-8ce2-d9a79664db16' }; news24.getAjax("/Ajax/ArticleData/", "GetRecommendedArticles", data, function (res) { GetRecommendedArticlesCallback(res) }) }); function GetRecommendedArticlesCallback(res) { if (!res.error && res != "error") $j('#contentDiv').html(res); else $j('#contentDiv').remove() }
        </script>
        <script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
    </div>
    <div id="contentDiv" class="right" style="width:277px;padding-bottom:10px;"></div>
    <div class="clr"></div>
</div>
        <div class="spacer clr">
            </div>
        <div class="spacer clr">
            </div>
        
<iframe src="http://b.wm.co.za/24com.php?location=N&layout=wide" id="ifrWide" frameborder="0" width="630" height="152" scrolling="no" style="margin-left:-8px"></iframe>
<div class="clr10">&nbsp;</div>
        <div class="spacer clr">
            </div>
        <div id="divToHide">
    <div id="inside_news" class="col626 left">
    <h2 class="bold">Inside News24</h2>
	    <div id="wrap_carousel" class="relative block">
	      
		      <ul id="carousel" class="absolute">
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.women24.com/LoveAndSex/SexAndSizzle/Aftersex-selfie-trend-goes-viral-on-instagram-users-grossed-out-20140401" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2725/59f3146eb1d8497fa52ee59c58c44b9f.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.women24.com/LoveAndSex/SexAndSizzle/Aftersex-selfie-trend-goes-viral-on-instagram-users-grossed-out-20140401" data-track="outbound,home,inside-#Aftersex selfie? Ew!" target="_self">#Aftersex selfie? Ew!</a></h4>
                    <p>This is what happens when over sharing goes too far.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.news24.com/Travel/Multimedia/kululas-braai-in-the-sky-20140402" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2725/857226802ae148c791365c7c43b5a545.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.news24.com/Travel/Multimedia/kululas-braai-in-the-sky-20140402" data-track="outbound,home,inside-kulula\&#39;s sky braai" target="_self">kulula's sky braai</a></h4>
                    <p>We thought they were crazy, but kulula actually did it! Watch this video.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.food24.com/Drinks/Coffee" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2725/95a77f113aa84252bf20a119fa5757f1.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.food24.com/Drinks/Coffee" data-track="outbound,home,inside-Best coffees in Cape Town" target="_self">Best coffees in Cape Town</a></h4>
                    <p>A comprehensive list of great coffee shops in Cape Town. </p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.channel24.co.za/Gossip/News/8-very-real-emotions-we-all-experienced-when-we-found-out-that-Gareth-Cliff-was-leaving-5FM-20140331" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2724/50195a487b6d452cb351aa11856d8e22.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.channel24.co.za/Gossip/News/8-very-real-emotions-we-all-experienced-when-we-found-out-that-Gareth-Cliff-was-leaving-5FM-20140331" data-track="outbound,home,inside-Gareth is gone!" target="_self">Gareth is gone!</a></h4>
                    <p>8 emotions we all experienced. </p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.parent24.com/Teen_13-18/health_safety/Teen-addicted-to-selfies-attempts-suicide-20140328" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2670/ccd03e657bd74438a2e53b10586db97e.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.parent24.com/Teen_13-18/health_safety/Teen-addicted-to-selfies-attempts-suicide-20140328" data-track="outbound,home,inside-Addicted to selfies" target="_self">Addicted to selfies</a></h4>
                    <p>Selfie obsessed teen attempts to commit suicide.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.health24.com/Lifestyle/Environmental-health/News/Chinese-parents-offer-babies-for-adoption-on-internet-20140331" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2723/4dfefd798394492d8389468d2a8ec170.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.health24.com/Lifestyle/Environmental-health/News/Chinese-parents-offer-babies-for-adoption-on-internet-20140331" data-track="outbound,home,inside-Babies on offer" target="_self">Babies on offer</a></h4>
                    <p>Chinese parents are offering their babies for adoption on the internet.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.news24.com/Multimedia/Video/SouthAfrica/Top-5-April-Fools-jokes-20140401" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2724/8bcec918b7034cf39befd67b824cd914.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.news24.com/Multimedia/Video/SouthAfrica/Top-5-April-Fools-jokes-20140401" data-track="outbound,home,inside-Top 5 April Fools\&#39; jokes" target="_self">Top 5 April Fools' jokes</a></h4>
                    <p> We round up our top five April Fools' pranks. Watch.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.news24.com/Travel/Multimedia/Crazy-kayak-waterfall-drop-20140331" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2723/c1bb60ef40fe4582a88fdd61f1872cba.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.news24.com/Travel/Multimedia/Crazy-kayak-waterfall-drop-20140331" data-track="outbound,home,inside-Crazy kayaker!" target="_self">Crazy kayaker!</a></h4>
                    <p>Insane GoPro footage of a kayaker doing an 18-metre drop. </p>
		        </div>
		      </li>
	        
	          </ul>
	        
	    </div>
    </div>	
    <div id="" class="left col13"> </div>
</div>
<div class="clr">&nbsp;</div>


        <div class="spacer clr">
            </div>
        

<div id="promotion_box" class="left col626">
    <div id='ad-1x1-1' class='24ad1x1'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('1x1','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=1x1&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=1x1&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
</div>
    </div>

            </div>
            <div id="right_column" class="grey_grad left col299">
                
    <div class="personallogin">
        <div id="PanelLogIn">
	
    <div class="welcome">
        <h2 class="bold">Welcome to News24</h2>
        <div class="login_block"><a href="javascript:void(0)" class="submit_button">Login | Sign Up</a></div>
    </div>
    <div class="clr"></div>
    

<div class="uploadblack">
    <div class="blackblock_heading">Get Published!</div>
    <div class="blackblock_upload"><strong>UPLOAD</strong></div>
    <div class="blackblock_icons">
        <a class="tooltip call2action" href="http://uploads.news24.com/#story">
            <img width="24" height="24" border="0" alt="" src='http://static.24.co.za/5/images/profile/article_icon.jpg'>
            <span><b>Click here<br>to upload<br>your article</b></span>
        </a>
        <a class="tooltip call2action" href="http://uploads.news24.com/#images">
            <img width="24" height="24" border="0" alt="" src='http://static.24.co.za/5/images/profile/camera_icon.jpg'>
            <span><b>Click here<br />to upload<br />your photo</b></span>
        </a>
        <a class="tooltip call2action" href="http://uploads.news24.com/#videos">
            <img width="24" height="24" border="0" alt="" src='http://static.24.co.za/5/images/profile/video_icon.jpg'>
            <span><b>Click here<br>to upload<br>your video</b></span>
        </a>
    </div>
</div>

</div>


        <div class="clr">
        </div>
    </div>
    

<script language="javascript" type="text/javascript">
    var tabsClass = { tabSetArray: new Array, classOn: "tabs_on", classOff: "tabs_off", addTabs: function (a) { tabs = document.getElementById(a).getElementsByTagName("div"); for (x in tabs) { if (typeof tabs[x].id != "undefined") { this.tabSetArray.push(tabs[x].id) } else { } } }, switchTab: function (a) { for (x in this.tabSetArray) { tabItem = this.tabSetArray[x]; dataElement = document.getElementById(tabItem + "_data"); if (dataElement) { if (dataElement.style.display != "none") { dataElement.style.display = "none" } else { } } else { } tabElement = document.getElementById(tabItem); if (tabElement) { if (tabElement.className != this.classOff) { tabElement.className = this.classOff } else { } } else { } } document.getElementById(a.id + "_data").style.display = ""; a.className = this.classOn } }
</script>

<div id="most_box" class="col299 tabs">
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td>
                <div id="mostTabContainer" class="localised tabNavigation tab-menu">
	                <div id="tab_read" class="tabs_on left" onmouseover="tabsClass.switchTab(this);">Most Read</div>
                    <div id="tab_comment" class="tabs_off left" onmouseover="tabsClass.switchTab(this);">Most Commented</div>
                    <div id="tab_area" class="tabs_off left" onmouseover="tabsClass.switchTab(this);">News In Your Area</div>
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <div id="tab_read_data" class="tab-wrapper">
                    <ul class="bold">
                            <li><a data-track="outbound,mostread,mostread-Top 5 April Fools\&#39; jokes" href="http://www.news24.com/Multimedia/Video/SouthAfrica/Top-5-April-Fools-jokes-20140401">Top 5 April Fools' jokes</a><span class='watch'><a href='http://www.news24.com/Multimedia/Video/SouthAfrica/Top-5-April-Fools-jokes-20140401'>watch</a></span></li>
                        
                            <li><a data-track="outbound,mostread,mostread-This man says he knows what happened to Flight MH370" href="http://www.news24.com/Travel/Flights/This-man-says-he-knows-what-happened-to-Flight-MH370-20140328">This man says he knows what happened to Flight MH370</a></li>
                        
                            <li><a data-track="outbound,mostread,mostread-DA takes on Nkandla in April Fools joke" href="http://www.news24.com/Elections/News/DA-takes-on-Nkandla-in-April-Fools-joke-20140401">DA takes on Nkandla in April Fools joke</a></li>
                        
                            <li><a data-track="outbound,mostread,mostread-Top 5 Sexiest Women in Sport" href="http://www.sport24.co.za/Multimedia/Babes-in-Sport/Top-5-Sexiest-Women-in-Sport-20140401">Top 5 Sexiest Women in Sport</a><span class='watch'><a href='http://www.sport24.co.za/Multimedia/Babes-in-Sport/Top-5-Sexiest-Women-in-Sport-20140401'>watch</a></span></li>
                        
                            <li><a data-track="outbound,mostread,mostread-Gareth Cliff is leaving 5FM" href="http://www.channel24.co.za/Gossip/News/Gareth-Cliff-is-leaving-5FM-20140331">Gareth Cliff is leaving 5FM</a></li>
                        </ul>
                    <div class="spacer clr"></div>
                    <a id="lnkReadMore" Class="lnkMore" href="http://www.news24.com/TopStories">More..</a>
                </div>
                <div id="tab_comment_data" class="tab-wrapper" style="display: none;">
                    <div class="clr"></div>
                    <ul class="bold">
                            <li><a data-track="outbound,mostread,mostcommented-Zille accepts \&#39;elecnomination\&#39; challenge" href="http://www.news24.com/Elections/News/Zille-accepts-elecnomination-challenge-20140331">Zille accepts 'elecnomination' challenge</a></li>
                        
                            <li><a data-track="outbound,mostread,mostcommented-ANC distances itself from Nkandla" href="http://www.news24.com/SouthAfrica/Politics/ANC-distances-itself-from-Nkandla-20140331">ANC distances itself from Nkandla</a></li>
                        
                            <li><a data-track="outbound,mostread,mostcommented-Zuma an immoral agent unfit to lead SA - UDM" href="http://www.news24.com/Elections/News/Zuma-an-immoral-agent-unfit-to-lead-SA-UDM-20140331">Zuma an immoral agent unfit to lead SA - UDM</a></li>
                        
                            <li><a data-track="outbound,mostread,mostcommented-Zuma\&#39;s Nkandla comments \&#39;an insult\&#39;" href="http://www.news24.com/SouthAfrica/Politics/Zumas-Nkandla-comments-an-insult-20140331-2">Zuma's Nkandla comments 'an insult'</a></li>
                        
                            <li><a data-track="outbound,mostread,mostcommented-I didn\&#39;t ask for Nkandla upgrade - Zuma" href="http://www.news24.com/Elections/News/I-didnt-ask-for-Nkandla-upgrade-Zuma-20140331">I didn't ask for Nkandla upgrade - Zuma</a></li>
                        </ul>
                    <div class="spacer clr"></div>                        
                    <a id="lnkCommentMore" Class="lnkMore" href="http://www.news24.com/TopStories">More..</a>
                </div>
                <div id="tab_area_data" class="tab-wrapper" style="display: none;">
                    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=mostread" id="lnkModalDisplay" class="userLocationModal right change_link">[change area]</a>
                    <h4 class="left most_head bold">News in Cape Town</h4>
                    <div class="clr"></div>
                    <ul class="bold">
                            <li><a data-track="outbound,mostread,mostreadarea-Retired  MP travel benefits not ANC idea - chief whip" href="http://www.news24.com/SouthAfrica/Politics/Retired-MP-travel-benefits-not-ANC-idea-chief-whip-20140401">Retired  MP travel benefits not ANC idea - chief whip</a></li>
                        
                            <li><a data-track="outbound,mostread,mostreadarea-Arms committee failed to table report - DA" href="http://www.news24.com/SouthAfrica/Politics/Arms-committee-failed-to-table-report-DA-20140401">Arms committee failed to table report - DA</a></li>
                        
                            <li><a data-track="outbound,mostread,mostreadarea-Top cop apologises to Khayelitsha residents" href="http://www.news24.com/SouthAfrica/News/Top-cop-apologises-to-Khayelitsha-residents-20140401">Top cop apologises to Khayelitsha residents</a></li>
                        
                            <li><a data-track="outbound,mostread,mostreadarea-Cape Town women in court for R2m fraud" href="http://www.news24.com/SouthAfrica/News/Cape-Town-women-in-court-for-R2m-fraud-20140401">Cape Town women in court for R2m fraud</a></li>
                        
                            <li><a data-track="outbound,mostread,mostreadarea-Journalist to appeal dismissal over DA MP application" href="http://www.news24.com/Elections/News/Journalist-to-appeal-dismissal-over-DA-MP-application-20140401">Journalist to appeal dismissal over DA MP application</a></li>
                        </ul>
                </div>
                <script type="text/javascript">
                      tabsClass.addTabs("mostTabContainer");
			    </script>
            </td>
        </tr>
        <tr>
            <td>
                <div class="ad278X35 outsurance"><!-- outsurance Ad -->
	                <div id='ad-278x76-1' class='24ad278x76'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('278x76','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=278x76&c=833984065&t=artid%3d7a8a7f3f-8779-49d1-80d3-d5bbdf5c1147%26People%3djonathan+pollard%26Places%3disrael%2cus%26Topics%3despionage%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=278x76&c=833984065&t=artid%3d7a8a7f3f-8779-49d1-80d3-d5bbdf5c1147%26People%3djonathan+pollard%26Places%3disrael%2cus%26Topics%3despionage%26posno%3d1' border='0' alt=''></a></noscript>
                </div>
            </td>
        </tr>
    </table>
    <a id="lnkModalItem" class="fireEventMost locationModal" style="display:none;"></a>
</div>

    <div class="spacer clr">
        </div>
    <div class="ad300X600 col300">
        <div id='ad-300x600-1' class='24ad300x600'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('300x600','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=300x600&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=300x600&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
    </div>
    <div class="spacer clr">
        </div>
    
    <div class="spacer clr">
        </div>
    
    <div class="spacer clr">
        </div>
    <div id="fb_social"></div>
<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/SocialNews/3.0/scripts/socialnews.min.js?v=20140319" type="text/javascript"></script>
<script type="text/javascript" >
jQuery('head').append('<link rel="stylesheet" href="http://scripts.24.co.za/libs/24com/SocialNews/3.0/styles/socialnews.css?v=20140319" type="text/css" />');
jQuery(document).ready(function(){
FBSocialNews.settings.siteDomain="www.news24.com";
FBSocialNews.settings.parentDomain="www.news24.com";
FBSocialNews.settings.activityServiceUrl="http://fbactivity.24.com/";
FBSocialNews.settings.appID="2363277980";
FBSocialNews.settings.tinaBaseUrl="http://auth.news24.com";
FBSocialNews.settings.isArticle=true;
FBSocialNews.settings.actionType='read';
FBSocialNews.settings.overrideFriendActivity=false;
if(typeof LanguageResource != 'undefined')FBSocialNews.settings.language=LanguageResource.languages.eng;
FBSocialNews.userProfile.hasPermission=false;
FBSocialNews.init();
});
</script>
<div class="clr socialspacer"></div>
<a href="/SocialSharingPopup.aspx" class="iframe socialSharePopup" style="display:none;"></a>

    <div class="spacer clr">
        </div>
    
    
    

<script language="javascript" type="text/javascript">
    $j(document).ready(function () { var a = "capetown"; if (a == "" || a == "default") { $j("#tab_traffic_data").attr("class", "tab-wrapper") } }); var tabsInfoClass = { tabInfoSetArray: new Array, classOn: "tabs_on left", classOff: "tabs_off left", addTabs: function (a) { tabs = document.getElementById(a).getElementsByTagName("div"); for (x in tabs) { if (typeof tabs[x].id != "undefined") { this.tabInfoSetArray.push(tabs[x].id) } else { } } }, switchTab: function (a) { for (x in this.tabInfoSetArray) { tabItem = this.tabInfoSetArray[x]; dataElement = document.getElementById(tabItem + "_data"); if (dataElement) { if (dataElement.style.display != "none") { dataElement.style.display = "none" } else { } } else { } tabElement = document.getElementById(tabItem); if (tabElement) { if (tabElement.className != this.classOff) { tabElement.className = this.classOff } else { } } else { } } document.getElementById(a.id + "_data").style.display = ""; a.className = this.classOn } }
</script>

<div class="clr10">&nbsp;</div>
<div id="weather_box" class="col299 relative tabs2">
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td>
                <div id="infoTabContainer" class="tabNavigation tab-menu">
                    <div id="tab_traffic" class="tabs_on left" onmouseover="tabsInfoClass.switchTab(this);">Traffic</div>
                    <div id="tab_lottery" class="tabs_off left" onmouseover="tabsInfoClass.switchTab(this);">Lottery</div>
                </div>
            </td>
        </tr>
        <tr>
            <td class="relative">
                <div id="tab_traffic_data" class="tab-wrapper-beta">

<div id="traffic_box">
    <div class="traffic_header">
        <!--<h3 class="bold left">Traffic</h3>//-->
        <div class="dropdown left"><select id='ddlTrafficRegions'><option value='' >Select region..</option><option value='Western Cape' selected='selected'>Western Cape</option><option value='Gauteng' >Gauteng</option><option value='KwaZulu-Natal' >KwaZulu-Natal</option><option value='Free State' >Free State</option><option value='Northern Cape' >Northern Cape</option><option value='Limpopo' >Limpopo</option><option value='Eastern Cape' >Eastern Cape</option><option value='Mpumalanga' >Mpumalanga</option><option value='North West' >North West</option></select></div>
    </div>
    <div class="traffic_container">
        <div class="clr5 clr">&nbsp;</div>
        <div id="trafic-container" class="left">
            <ul><li><span class='day'>Wednesday</span>&nbsp;<span class='location'>Bellville - 09:46 AM</span><br/><span class='road'>Road name: N1 Inbound</span><br/><span class='description'>DELAYS between the R300 Highway and the Durban Road exit</span></li><li><span class='day'>Wednesday</span>&nbsp;<span class='location'>Paarl - 09:45 AM</span><br/><span class='road'>Road name: N1 Westbound</span><br/><span class='description'>ACCIDENT in the right lane before the Klapmuts exit - expect delays</span></li></ul>
        </div>
        <div class="clr5 clr">&nbsp;</div>
        <a href="http://www.news24.com/Traffic/WESTERN_CAPE" id="lnkMore" class="block bold">More traffic reports...</a>
        <div class="clr5 clr">&nbsp;</div>
        <a href="http://pubads.g.doubleclick.net/gampad/clk?id=58119910&iu=/8900/24.com/Web/News24" id="lnkSponsor" target="_blank"><img src="http://cdn.24.co.za/files/Cms/General/d/2707/2c5f0da27a154cad93b7448a2e620359.jpg" id="imgSponsor" /></a>
        <script type="text/javascript">
            $j(document).ready(function () { $j("#ddlTrafficRegions").change(function () { var e = $j("OPTION:selected", this).val(); var t = "traffic/" + e.replace(" ", "_").toUpperCase(); $j("#lnkMore").html("<a id='lnkMore' href='" + t + "' class='block bold'>More traffic reports...</a>"); $j("#trafic-container").hide(); news24.getAjax("/Ajax/TrafficData/", "GetTraffic", { 'location': e }, function (e) { $j("#trafic-container").html(e); $j("#trafic-container").fadeIn("slow") }) }) });
        </script>
    </div>
</div></div>
                <div id="tab_lottery_data" class="tab-wrapper" style="display: none;">Here are the winning Powerball numbers from the Tuesday, 01 April&nbsp;draw.<br /><br />14, 17, 24, 27, 34 Powerball 4<br /><br /><strong>SMS the word Powerball to 31222 to get lotto numbers sent directly to your phone. The service costs just R10 per month.<br /><br />To unsubscribe, reply with the words Stop Powerball.</strong><br />
<div class="spacer clr"></div>
<a href="http://www.news24.com/Lottery" id="lnkMoreLotto" class="block bold">More lotto numbers...</a></div>
                <script type="text/javascript">tabsInfoClass.addTabs("infoTabContainer");</script>
            </td>
        </tr>
    </table>
</div>
<div class="spacer clr"></div>
    <div class="spacer clr">
        </div>
    <div class="ad300X250 col300">
        <div id='ad-300x250-1' class='24ad300x250'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('300x250','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=300x250&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=300x250&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
    </div>
    <div class="spacer clr">
        </div>
    
<script type="text/javascript">
    function InsuranceDealsGoTo(a) { $j("#sponsor_carousel").jcarousel("scroll", a, true); $j("#sponsor_carousel").jcarousel("reload"); return false } function movenext() { $j("#sponsor_carousel").jcarousel("next"); return false } function moveback() { $j("#sponsor_carousel").jcarousel("prev"); return false } function mycarousel_itemFirstInCallback(a, b, c, d) { var e = c; $j("div#adlist ul li").removeClass("selected"); $j("div#adlist ul li").removeAttr("style"); $j("div#adlist ul a").removeAttr("style"); $j("#ad_" + e).parent().addClass("selected"); $j("#ad_" + e).parent().attr("style", "background-color:" + colors[e] + ";color:" + textcolors[e]); $j("#ad_" + e).attr("style", "color:" + textcolors[e]); $j("#jcarousel-prev").unbind("click"); $j("#jcarousel-next").unbind("click"); if (e == 1) { $j("#jcarousel-prev").removeClass("jcarousel-prev-disabled").addClass("jcarousel-prev-disabled"); $j("#jcarousel-prev").attr("disabled", "disabled"); $j("#jcarousel-prev").unbind("click") } else { $j("#jcarousel-prev").removeClass("jcarousel-prev-disabled"); $j("#jcarousel-prev").attr("disabled", ""); $j("#jcarousel-prev").bind("click", moveback) } if (e == last) { $j("#jcarousel-next").removeClass("jcarousel-next-disabled").addClass("jcarousel-next-disabled"); $j("#jcarousel-next").attr("disabled", "disabled"); $j("#jcarousel-next").unbind("click") } else { $j("#jcarousel-next").removeClass("jcarousel-next-disabled"); $j("#jcarousel-next").attr("disabled", ""); $j("#jcarousel-next").bind("click", movenext) } } $j(document).ready(function () { $j('#jcarousel-next').bind('click', movenext); $j('#jcarousel-prev').bind('click', moveback); var randomnumber = Math.floor(Math.random() *0 +1); $j("#sponsor_carousel").jcarousel({ scroll: 1, start: randomnumber, itemFirstInCallback: mycarousel_itemFirstInCallback, buttonNextHTML: null, buttonPrevHTML: null }); $j("#sponsored_holder").removeClass("tabLoader") });
</script>


<div class="spacer clr"></div>
    

<div id="the_accordion" class="tabLoader">
    <div id="accordion" class="col299 relative">
        <h3 id="headerTag" class="toggler toggler_pers">
    <a href="http://www.careers24.com/cape-town-jobs" class="bold toggler_anchor">Jobs in Cape Town</a>
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=careers" id="lnkModalDisplay" class="careersModal right" style="padding-right:5px;text-transform:lowercase;font-size:11px">[change area]</a>
</h3>
<div class="element">
    <div id="divToHide">
        <h4 id="headerCareersRegion" class="bold item" style="font-size:11px;">Jobs in Western Cape region</h4>
        
	         <div class="item">
                
                    <h4 class="bold">
                        <a data-track="outbound,rightnav-listings,careers-QA Test Engineer" href="http://www.careers24.com/jobs/adverts/453972-qa-test-engineer-western-cape/" target="_blank">QA Test Engineer</a></h4>
                        
                    <p>
                        Western Cape<br/>People Source (Pty) Ltd<br/>Market Related</p>
                    
                    <div class="clr">
                    </div>
                </div>
          
	         <div class="item">
                
                    <h4 class="bold">
                        <a data-track="outbound,rightnav-listings,careers-Order Clerk" href="http://www.careers24.com/jobs/adverts/453886-order-clerk-western-cape/" target="_blank">Order Clerk</a></h4>
                        <img src="http://static.24.co.za/5/images/lazy/86x48.jpg" class="right job" width="86" height="48" data-src="http://www.careers24.com/_resx/imageresource/4354677D87CE6109A53E2C351D55B0B1DFCB305F-52677-86-48-0" />
                    <p>
                        Western Cape<br/>Main Solution Recruiters<br/>R9000</p>
                    
                    <div class="clr">
                    </div>
                </div>
          
	         <div class="item">
                
                    <h4 class="bold">
                        <a data-track="outbound,rightnav-listings,careers-Client Support Specialist (IT)" href="http://www.careers24.com/jobs/adverts/453947-client-support-specialist-it-western-cape/" target="_blank">Client Support Specialist (IT)</a></h4>
                        <img src="http://static.24.co.za/5/images/lazy/86x48.jpg" class="right job" width="86" height="48" data-src="http://www.careers24.com/_resx/imageresource/A2A5B419FE3BABFCEAFD4A243E589CFA08EAC25A-2020-86-48-0" />
                    <p>
                        Western Cape<br/>Persona Staff<br/>Market Related</p>
                    
                    <div class="clr">
                    </div>
                </div>
          
	    <div class="item browse bold">
		    <a href="http://www.careers24.com/cape-town-jobs" target="_blank">Browse more Cape Town jobs...</a>
	    </div>
	    <div class="item">
                <div class="left" style="margin-left: 0px; width: 140px;">
                    <ul>
                        
                                <li>
                                    <a href='http://www.careers24.com/kimberley-jobs' title='Kimberley Jobs'>
                                        Kimberley Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/jobs-in-eastern-cape' title='Eastern Cape Jobs'>
                                        Eastern Cape Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/jobs-in-north-west' title='North West Jobs'>
                                        North West Jobs
                                    </a> 
                                </li>
                            
                    </ul>
                </div>
                <div class="left" style="margin-right:13px">
                    <ul>
                        
                                <li>
                                    <a href='http://www.careers24.com/construction-jobs' title='Construction Jobs'>
                                        Construction Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/medical-jobs' title='Medical Jobs'>
                                        Medical Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/admin-jobs' title='Admin Jobs'>
                                        Admin Jobs
                                    </a> 
                                </li>
                            
                    </ul>
                </div>
                <div class="clr"></div>
        </div>
	    <div class="item bold last">
		    <a href="http://www.careers24.com/candidate/register/" target="_blank">Register your CV...</a><br/>
		    <a href="http://www.careers24.com/jobs/alert/" target="_blank">Get Job alerts in your e-mail...</a><br/>
		    <a href="http://www.careers24.com/recruiters/" target="_blank">RECRUITERS – Advertise your jobs here</a>
	    </div>
        <a id="lnkModalItem" class="fireEventCareers careersModal" style="display:none;"></a>
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler toggler_pers">
    <a href="http://www.property24.com" class="bold toggler_anchor">Property</a>
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=property" id="lnkModalDisplay" class="propertyModal right" style="padding-right:5px;text-transform:lowercase;font-size:11px">[change area]</a>
</h3>
<div class="element">
    <div id="divToHide">
        
        
                <div class="item">
	                <div class="wrapper">
	                <a href="http://www.property24.com/for-sale/durbanville/western-cape/439?ListingNumber=P24-101710966" id="lnkThumb">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages.property24.com%2fFetchImage.ashx%3fresource%3dproperty%26listingtype%3dsale%26id%3d101710966%3a1%26size%3dmedium" />
                    </a>
                    </div>
                    <div class="wrapper">
		            <h4 class="bold"><a data-track="outbound,rightnav-listings,property-HOUSES FOR SALE IN Durbanville" href="http://www.property24.com/for-sale/durbanville/western-cape/439?ListingNumber=P24-101710966" target="_blank">HOUSES FOR SALE IN Durbanville</a></h4>
		            <p><span class="block">Houses</span>
		            <span class="block bold">R 1 750 000</span></p>
                    </div>
		            <div class="clr"></div>
	            </div>
            
                <div class="item">
	                <div class="wrapper">
	                <a href="http://www.property24.com/for-sale/somerset-west/western-cape/390?ListingNumber=P24-101711952" id="lnkThumb">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages.property24.com%2fFetchImage.ashx%3fresource%3dproperty%26listingtype%3dsale%26id%3d101711952%3a1%26size%3dmedium" />
                    </a>
                    </div>
                    <div class="wrapper">
		            <h4 class="bold"><a data-track="outbound,rightnav-listings,property-HOUSES FOR SALE IN Somerset West, Heldervue" href="http://www.property24.com/for-sale/somerset-west/western-cape/390?ListingNumber=P24-101711952" target="_blank">HOUSES FOR SALE IN Somerset West, Heldervue</a></h4>
		            <p><span class="block">Houses</span>
		            <span class="block bold">R 1 999 000</span></p>
                    </div>
		            <div class="clr"></div>
	            </div>
            
                <div class="item">
	                <div class="wrapper">
	                <a href="http://www.property24.com/for-sale/cape-town/western-cape/432?ListingNumber=P24-101710300" id="lnkThumb">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages.property24.com%2fFetchImage.ashx%3fresource%3dproperty%26listingtype%3dsale%26id%3d101710300%3a1%26size%3dmedium" />
                    </a>
                    </div>
                    <div class="wrapper">
		            <h4 class="bold"><a data-track="outbound,rightnav-listings,property-HOUSES FOR SALE IN Cape Town, Camps Bay" href="http://www.property24.com/for-sale/cape-town/western-cape/432?ListingNumber=P24-101710300" target="_blank">HOUSES FOR SALE IN Cape Town, Camps Bay</a></h4>
		            <p><span class="block">Houses</span>
		            <span class="block bold">R 7 200 000</span></p>
                    </div>
		            <div class="clr"></div>
	            </div>
            
        <a id="lnkModalItem" class="fireEventProperty propertyModal" style="display:none;"></a>
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler" style="height:15px;"><a href="http://www.gotravel24.com/" class="bold">Travel</a> - Look, Book, Go!</h3>
<div class="element">
    <div id="divToHide">
	    <div class="item travel"><!-- add travel class -->
		    <h4 class="bold"><a id="lnkTitle" href="http://holidays.gotravel24.com/ku/holidayoffer.jsp?Destination=NL_SCHOOLS_OUT_MRU_GT,RG,RB&amp;utm_source=holidays&amp;utm_medium=focus&amp;utm_campaign=mar_schoolout">Magical Mauritius holidays</a></h4>
		    <img src="http://static.24.co.za/5/images/lazy/110x65.jpg" id="imgThumbnail" width="110" height="65" class="right" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fwww.gotravel24.com%2ffiles%2fpreskil_ext_02.jpg" />
		    Check out these great Mauritius holiday specials from R12 875 per person sharing. Includes accommodation, return flights and airport transfers.
		    <span class="item browse bold block"><a id="lnkPackages" href="http://holidays.gotravel24.com/ku/holidayoffer.jsp?Destination=NL_SCHOOLS_OUT_MRU_GT,RG,RB&amp;utm_source=holidays&amp;utm_medium=focus&amp;utm_campaign=mar_schoolout">Book now!</a></span>
	    </div>
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler"><a href="http://etrader.kalahari.com/referral.asp?linkid=3442&partnerid=9180" class="bold">Kalahari.com</a> - shop online today</h3>
<div class="element">
    <div id="divToHide">
        
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?Ntt=The+Real+Meal+Revolution&amp;searchCategories=4294966903&amp;N=4294966903&amp;Ntk=def&amp;pageSize=12&amp;linkId=1441122&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?Ntt=The+Real+Meal+Revolution&amp;searchCategories=4294966903&amp;N=4294966903&amp;Ntk=def&amp;pageSize=12&amp;linkId=1441122&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">The Real Meal Revolution </a></h4>
		              <p style="word-wrap:break-word;">The goal of The Real Meal Revolution is to change your life by teaching you how to take charge of your weight and your health through the way you eat. Order now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=21204+18262&amp;Ns=p_salestd%7c0&amp;linkId=1602077&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=21204+18262&amp;Ns=p_salestd%7c0&amp;linkId=1602077&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">Sleep & stress medicine</a></h4>
		              <p style="word-wrap:break-word;">Rest easy with our range of health and stress remedies. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/Merchandising-Category/N-g06Z1z141o6?linkId=1602075&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/Merchandising-Category/N-g06Z1z141o6?linkId=1602075&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">Great Easter deals at kalahari.com</a></h4>
		              <p style="word-wrap:break-word;">Get 2 inspirational, gospel or kids DVDs for just R99, as well as many other amazing deals. Offer valid while stocks last. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=19849&amp;linkId=1520747&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=19849&amp;linkId=1520747&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">kalahari.com #1 selling product</a></h4>
		              <p style="word-wrap:break-word;">gobii eReader + FREE wall charger and leatherette cover now R599, save R340. Offer valid while stocks last. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item last">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=20155&amp;linkId=1489277&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=20155&amp;linkId=1489277&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">25% off new & bestselling movies</a></h4>
		              <p style="word-wrap:break-word;">Choose from blockbuster titles including Despicable Me 2, Gravity, Frozen, The Hunger Games: Catching Fire and many more. Offer valid while stocks last. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler toggler">
    <a href="http://www.olx.co.za/" class="bold toggler_anchor"> OLX Free Classifieds</a>
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=kalahari" id="lnkModalDisplay" class="kalahariModal right" style="padding-right:5px;text-transform:lowercase;font-size:11px">[change area]</a>
</h3>
<div class="element">
    <div id="divToHide">
        
	          <div style="min-height:100px;" class="item">
                    <a href="http://capetown.olx.co.za/samsung-galaxy-s4-iid-559689336" id="lnkThumb" target="_blank">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" id="imgKalahari" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages04.olx-st.com%2fui%2f7%2f99%2f36%2ft_1382642518_559689336_3.jpg" />
                    </a>
		            <h4 class="bold"><a id="lnkArticle" href="http://capetown.olx.co.za/samsung-galaxy-s4-iid-559689336" target="_blank">Samsung Galaxy s4</a></h4>
		            <p style="word-wrap:break-word;">Mobile, Cell Phones in South Africa, Western Cape, Cape Town. Date October 24</p>
	          </div>
          
	          <div style="min-height:100px;" class="item">
                    <a href="http://capetown.olx.co.za/best-bargain-in-big-bay-iid-559891688" id="lnkThumb" target="_blank">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" id="imgKalahari" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages02.olx-st.com%2fui%2f1%2f24%2f88%2ft_1382699383_559891688_1.jpg" />
                    </a>
		            <h4 class="bold"><a id="lnkArticle" href="http://capetown.olx.co.za/best-bargain-in-big-bay-iid-559891688" target="_blank">Best bargain in big bay</a></h4>
		            <p style="word-wrap:break-word;">Real Estate, Houses - Apartments for Sale in South Africa, Western Cape, Cape Town. Date October 25</p>
	          </div>
          
	          <div style="min-height:100px;" class="item last">
                    <a href="http://capetown.olx.co.za/vw-golf-6-1-6-trendline-excellent-condition-iid-559891037" id="lnkThumb" target="_blank">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" id="imgKalahari" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages02.olx-st.com%2fui%2f7%2f17%2f37%2ft_1382699205_559891037_1.jpg" />
                    </a>
		            <h4 class="bold"><a id="lnkArticle" href="http://capetown.olx.co.za/vw-golf-6-1-6-trendline-excellent-condition-iid-559891037" target="_blank">VW Golf 6, 1.6 Trendline (Excellent condition)</a></h4>
		            <p style="word-wrap:break-word;">Vehicles, Cars in South Africa, Western Cape, Cape Town. Date October 25</p>
	          </div>
          
        <a id="lnkModalItem" class="fireEventKalahari kalahariModal" style="display:none;"></a>
        <div class="clr"></div>
        
    </div>
</div>
    </div>
</div>
    <div class="spacer clr">
        </div>
    
    

<div id="sponsor_box" class="col299 relative">
	<h3 class="bold">Sponsored links</h3>
    
		<table class="sponsor" width="280" border="0" cellpadding="0" cellspacing="0">
		  <tbody>
	  
		  <tr>
			<td style="width:35px;"><a href="../../Controls/Common/#" id="lnkSponsorImg"><img src="http://cdn.24.co.za/files/Cms/General/d/1946/c127ed56cafc46d8bef570a12d88bd6a.png" style="width:27px;" /></a></td>
			<td align="left"><a href="http://ad.doubleclick.net/clk;258342228;14949887;z?http://direct.infax.co.za/signup/media24/index.html" target="_blank">Free Fax2Mail</a></td>
			<td>&nbsp;</td>
	  
		</tbody></table>
	  
</div>
    <div class="spacer clr">
        </div>
    <div class="clr10 clr"> </div>
<script src="http://scripts.24.co.za/libs/kalahari/2.1/Scripts/kalahari.carousel.widget.js" type="text/javascript"></script>
<div id="oprahwidgetcontainer">
<script type="text/javascript">
jQuery('head').append("<link href='http://scripts.24.co.za/libs/kalahari/2.1/Styles/kalahari.carousel.css' type='text/css' rel='stylesheet' ></link>")
var Widget = new kalaharicarouselwidget({
sku: [47866962,47237432,48181896,45827052,46112817],
token: "563",
container: "oprahwidgetcontainer",
visible:1,
refUrl: 'URL: http://www.kalahari.com/?linkId=46213&affiliateId=563&linkType=ORDER_REFERRAL'
});
</script>
</div>
<div class="clr10 clr"> </div>


    <div class="spacer clr">
        </div>
    

<script type="text/javascript">
    jQuery(function () {
        var submitFunc = function() { window.open('http://www.pricecheck.co.za/search/?utm_source=news24&utm_medium=affiliate&utm_campaign=sidebar&search=' + jQuery('#txtPriceCheckSearch').val()) };jQuery("#btnPriceCheckSubmit").click(submitFunc);jQuery("#txtPriceCheckSearch").keypress(function(e){if(e.keyCode===13){submitFunc();return false}})});
</script>

<div class="pricecheckBlock">
    <a href="http://www.pricecheck.co.za/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" target="_blank" id="lnkPriceCheckHeader" style="height:51px;left:0;position:absolute;top:0;width:298px;"></a>
    <div class="priceContent">
        <div class="priceBlurb">
            <p><a href="http://www.pricecheck.co.za/offers/23376500/Samsung+Galaxy+Tab+P7500+10.1+Tablet+With+WiFi+&+3G/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" id="aLink" target="_blank">Samsung Galaxy Tab P7500 10.1&quot; Tablet With WiFi &amp; 3G</a></p>
            <p>Samsung Galaxy Tab 10.1 gives you a better experience for...</p>
            <p>
                <a href="http://www.pricecheck.co.za/offers/23376500/Samsung+Galaxy+Tab+P7500+10.1+Tablet+With+WiFi+&+3G/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" id="aLinkPrice" style="color:#ec3b27;" target="_blank">
                    <span style="font-weight:normal">From</span> <strong>R4999.00</strong>
                </a>
            </p>
        </div>
        <div class="priceImage"><a href="http://www.pricecheck.co.za/offers/23376500/Samsung+Galaxy+Tab+P7500+10.1+Tablet+With+WiFi+&+3G/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" id="aLinkImage" target="_blank"><img src="http://static.24.co.za/5/images/lazy/65x65.jpg" id="imgThumb" data-src="http://images1.pricecheck.co.za/images/objects/hash/product/e7b/9cd/8f0/image_small_23376500.jpg" /></a></div>
    </div>
    <div class="clr"></div>
    <div class="priceShopping">
        <h4>I'm shopping for:</h4>
        <input type="text" class="priceSearch" id="txtPriceCheckSearch" />
        <input type="button" class="priceSubmit" value="LET'S GO!" id="btnPriceCheckSubmit" />
    </div>
</div>
    <div class="spacer clr">
        </div>
    
<div class="facebook_block">
    <iframe src="http://www.facebook.com/plugins/likebox.php?href=http%3A%2F%2Fwww.facebook.com%2Fpages%2FNews24com%2F10227041841&width=300&height=245&show_faces=true&colorscheme=light&stream=false&show_border=true&header=false" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:300px; height:245px;" allowTransparency="true"></iframe>
</div>
    <div class="spacer clr">
        </div>
    

<div id="horoscopes_tab" class="tab-wrapper horoscope relative">
    <div class="horoscope_header"> Horoscopes</div>
    <div class="horoscope_women"><img src="http://static.24.co.za/5/images/women_horoscope.png" width="120" height="21" border="0" /></div>
	<div class="horoscope_midlevel">
        <div class="zodiac">
		    <select onchange="toggleSubmit(this)" name="ptype" id="ptype" class="absolute">
			     <option selected="selected" value="aquarius">Aquarius  (20 Jan - 18 Feb)</option>
			     <option value="aries">Aries  (21 Mar - 20 Apr)</option>
			     <option value="cancer">Cancer  (21Jun - 21 Jul)</option>
			     <option value="capricorn">Capricorn  (21Dec - 19 Jan)</option>
			     <option value="gemini">Gemini  (21 May - 20 Jun)</option>
			     <option value="leo">Leo  (22 Jul - 21 Aug)</option>
			     <option value="libra">Libra  (22 Sep - 22 Oct)</option>
			     <option value="pisces">Pisces  (19 Feb - 20 Mar)</option>
			     <option value="sagittarius">Sagittarius (22 Nov - 20 Dec)</option>
			     <option value="scorpio">Scorpio  (23 Oct - 21 Nov)</option>
			     <option value="taurus">Taurus  (21 Apr - 20 May)</option>
			     <option value="virgo">Virgo  (22 Aug - 21 Sep)</option>
    	      </select>
	    </div>
        
                    <div id="d0" style="display:block;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Aquarius_icon.gif" alt="Aquarius" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aquarius" title="Aquarius" alt="Aquarius" data-track="outbound,home,horoscope-aquarius">Aquarius</a></h5>
                           <p>Your mind is full and you may want to curl up in a comfy place at home and just escape into the world of imagination either...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aquarius" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-aquarius">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d1" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Aries_icon.gif" alt="Aries" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aries" title="Aries" alt="Aries" data-track="outbound,home,horoscope-aries">Aries</a></h5>
                           <p>Impatience and frustration could create tension for you today. You may have to compromise and take the middle path to avoid...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aries" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-aries">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d2" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Cancer_icon.gif" alt="Cancer" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Cancer" title="Cancer" alt="Cancer" data-track="outbound,home,horoscope-cancer">Cancer</a></h5>
                           <p>You may be going over the top in your enthusiasm to have fun and please the crowd. Try and find the middle road of moderation...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Cancer" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-cancer">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d3" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Capricorn_icon.gif" alt="Capricorn" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Capricorn" title="Capricorn" alt="Capricorn" data-track="outbound,home,horoscope-capricorn">Capricorn</a></h5>
                           <p>Things seem to be intense right now, but an unexpected visit from someone could draw you away from the intensities and help you to...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Capricorn" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-capricorn">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d4" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Gemini_icon.gif" alt="Gemini" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Gemini" title="Gemini" alt="Gemini" data-track="outbound,home,horoscope-gemini">Gemini</a></h5>
                           <p>Your rational mind is awake and you are able to focus and organise things a lot better today. Put your restless energy into...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Gemini" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-gemini">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d5" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Leo_icon.gif" alt="Leo" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Leo" title="Leo" alt="Leo" data-track="outbound,home,horoscope-leo">Leo</a></h5>
                           <p>You may have an impulsive urge to expand your horizons and explore your possibilities. You don`t want to be tied down today. ...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Leo" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-leo">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d6" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Libra_icon.gif" alt="Libra" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Libra" title="Libra" alt="Libra" data-track="outbound,home,horoscope-libra">Libra</a></h5>
                           <p>You may want to treat your loved one with something close to your heart. This could be a gift, a delicious meal or even just some...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Libra" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-libra">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d7" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Pisces_icon.gif" alt="Pisces" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Pisces" title="Pisces" alt="Pisces" data-track="outbound,home,horoscope-pisces">Pisces</a></h5>
                           <p>You may find your enthusiasm and your energy levels don`t match up today. You may get swept away in your desire to have fun. ...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Pisces" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-pisces">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d8" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Sagittarius_icon.gif" alt="Sagittarius" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Sagittarius" title="Sagittarius" alt="Sagittarius" data-track="outbound,home,horoscope-sagittarius">Sagittarius</a></h5>
                           <p>The underlying tension may be that you have been spending a lot of time helping others and right now you just want to have some...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Sagittarius" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-sagittarius">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d9" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Scorpio_icon.gif" alt="Scorpio" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Scorpio" title="Scorpio" alt="Scorpio" data-track="outbound,home,horoscope-scorpio">Scorpio</a></h5>
                           <p>Your partner may surprise you and help you to enjoy the moment rather than worrying about all the things that seem to be...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Scorpio" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-scorpio">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d10" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Taurus_icon.gif" alt="Taurus" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Taurus" title="Taurus" alt="Taurus" data-track="outbound,home,horoscope-taurus">Taurus</a></h5>
                           <p>Indulgence and extravagance may be a strong temptation. You have the desire and the energy to do things, but you want to stay...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Taurus" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-taurus">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d11" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Virgo_icon.gif" alt="Virgo" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Virgo" title="Virgo" alt="Virgo" data-track="outbound,home,horoscope-virgo">Virgo</a></h5>
                           <p>Today may be a good day to start by jotting down your thoughts and creating some kind of structure to work with. ...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Virgo" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-virgo">read more</a></p>                               	              
	                    </div>
	                 </div>
          
	</div>
    <div class="perfect_match">
        <a href="http://love2meet.news24.com/" data-track="outbound,home,horoscope-love2meet.news24.com">Who’s your perfect match?<br />
<span>Click here to find out!</span></a>
    </div>
</div>


<script type="text/javascript">
    function toggleSubmit(obj) { count = 0; while (document.getElementById("d" + count)) { document.getElementById("d" + count).style.display = "none"; count++ } document.getElementById("d" + obj.selectedIndex).style.display = "block" } var date = new Date; var day = date.getDate(); var month = date.getMonth(); var currentZodiac; switch (month) { case 0: { if (day >= 20) currentZodiac = "aquarius"; else currentZodiac = "sagittarius"; break }; case 1: { if (day >= 19) currentZodiac = "pisces"; else currentZodiac = "aquarius"; break }; case 2: { if (day >= 21) currentZodiac = "aries"; else currentZodiac = "pisces"; break }; case 3: { if (day >= 21) currentZodiac = "taurus"; else currentZodiac = "aries"; break }; case 4: { if (day >= 21) currentZodiac = "gemini"; else currentZodiac = "taurus"; break }; case 5: { if (day >= 21) currentZodiac = "cancer"; else currentZodiac = "gemini"; break }; case 6: { if (day >= 22) currentZodiac = "leo"; else currentZodiac = "cancer"; break }; case 7: { if (day >= 22) currentZodiac = "virgo"; else currentZodiac = "leo"; break }; case 8: { if (day >= 22) currentZodiac = "libra"; else currentZodiac = "virgo"; break }; case 9: { if (day >= 23) currentZodiac = "scorpio"; else currentZodiac = "libra"; break }; case 10: { if (day >= 22) currentZodiac = "sagittarius"; else currentZodiac = "scorpio"; break }; case 11: { if (day >= 21) currentZodiac = "capricorn"; else currentZodiac = "sagittarius"; break } } $j(".zodiac #ptype").val(currentZodiac); toggleSubmit($j(".zodiac #ptype")[0])</script>
    <div class="spacer clr">
        </div>
    <div class="col299 relative endcolumn">
        </div>

            </div>
            <div class="spacer clr white"></div>
        </div>
        <div id="footer" class="relative clr">
                       
            

<div class="clr10 clr">&nbsp;</div>
<div id="divServices" class="services left">
  <h3 class="bold">services</h3>
  
      <div class="item left">
        <a href="http://www.news24.com/Newsletters" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/167/3d5262fc76764b0abd11667baf454f84.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/Newsletters" target="_top">E-mail Alerts</a></strong>
        The latest headlines in your inbox 
        </p>
      </div>
    
      <div class="item left">
        <a href="http://www.news24.com/SiteElements/Services/News24-RSS-Feeds-20111202-2" target="_self"><img src="http://cdn.24.co.za/files/Cms/General/d/495/7125197ea74a4880879e2bd187f630c9.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/SiteElements/Services/News24-RSS-Feeds-20111202-2" target="_self">RSS feeds</a></strong>
        News delivered really simply.
        </p>
      </div>
    
      <div class="item left">
        <a href="http://m.news24.com/news24" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/167/decc890f19a644579a0c033e19edbc40.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://m.news24.com/news24" target="_top">Mobile</a></strong>
        News24 on your mobile or PDA
        </p>
      </div>
    
      <div class="item left last">
        <a href="http://www.news24.com/Newsletters" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/167/432cbe0789a040e9ae3627685a099a0e.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/Newsletters" target="_top">E-mail Newsletters</a></strong>
        You choose what you want 
        </p>
      </div>
    
      <div class="item left">
        <a href="http://www.news24.com/xArchive/News24/Get-News24-on-your-iPhone-20090428" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/495/e2ae1ce7a6c74cd19e793cb31873a54e.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/xArchive/News24/Get-News24-on-your-iPhone-20090428" target="_top">News24 on your iPhone</a></strong>
        Get News24 headlines on your iPhone.
        </p>
      </div>
    
      <div class="item left">
        <a href="http://mobile.24.com/?p=minisite_news" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/168/7c086371afe44063bfadd3ff26fde57d.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://mobile.24.com/?p=minisite_news" target="_top">SMS Alerts</a></strong>
        Get breaking news stories via SMS.
        </p>
      </div>
    
      <div class="item left">
        <a href="http://blogs.24.com/" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/168/4a134cf303084f35bec18b1262fecf3e.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://blogs.24.com/" target="_top">Blogs</a></strong>
        Your opinion on you, me and everyone. 

        </p>
      </div>
    
      <div class="item left last">
        <a href="http://opencalais.com/" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/175/09ea1738b1764dca88d3100f383052c1.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://opencalais.com/" target="_top">Calais</a></strong>
        Website keywords automated by OpenCalais.
        </p>
      </div>
    
</div>
<div class="clr">&nbsp;</div>
            

<div id="footernav" class="relative">
  	<a href="http://www.24.com" class="absolute logo24"><img class="absolute logo24" width="56" height="42" src="http://static.24.co.za/5/images/24com_logo.png"/></a>
	<a href="http://www.dmma.co.za/" class="absolute dmma" title="Digital Media &amp; Marketing Association" target="_blank"><img src="http://static.24.co.za/5/images/footer_logo_dmma.png" width="102" height="52" alt="Digital Media &amp; Marketing Association" border="0" class="absolute dmma" /></a>
	
    <div class="copy absolute">
	    <ul>
	        
		            <li><a href="http://www.news24.com/search">Search</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/SiteElements/Footer/About-Us-20090703-4">About Us</a> ·</li>  
	            
		            <li><a href="http://www.thespacestation.co.za/channel/news24/">Advertise on News24</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/SiteElements/Services/Terms-and-Conditions-20120413">Terms & Conditions</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/PressReleases">Press Releases</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/Jobs/">Jobs at News24</a> ·</li>  
	            
            <li><a id="lnkFooterContactUs" class="group" href="http://www.news24.com/FeedBack.aspx?iframe" class="footerLink">Contact us</a></li>
        </ul>
        <div class="clr10 clr">&nbsp;</div>
        
        &copy; 2014 24.com. All rights reserved.
    </div>
 
</div>

        </div>
        <div class="clr white"></div>
    </div>

            

<div id="socialbarHPStories">
    <div id="socialbar-newstories" class="bottom">
        <span onclick="HPRedirect('http://www.news24.com/');">There are&nbsp;<strong>new stories</strong>&nbsp;on the homepage. Click here to see them.</span>
        <div id="close" onclick=" CloseNewStoriesPopup(); ">&nbsp;</div>
        <div class="arrow"></div>
    </div>
</div>
            <div id="retail_ad_spacer"></div> 
        </div>
        <div id='ad-1000x1000-1' class='24ad1000x1000'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('1000x1000','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=1000x1000&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=1000x1000&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
        <div id='ad-20x20-1' class='24ad20x20'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('20x20','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=20x20&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=20x20&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
        <div id="ad300bottom">
            <div id='ad-980x415-1' class='24ad980x415'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('980x415','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=980x415&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=980x415&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
        <div class="clr"></div>
    

<script type="text/javascript">
//<![CDATA[
var gotravelCount=5;//]]>
</script>

<div id="CmsStats" style="z-index:-1; visibility:hidden;">
<script type="text/javascript" language="JavaScript" >
var cmsStatsImage = new Image();
cmsStatsImage.src = "http://stats.24.com/content/image.articleview?rnd=635320296005569347&s=5&c=1073&a=23a7c7b3-778f-44cc-8ce2-d9a79664db16&t=Chile+president+cautious+as+8.2+quake+kills+5&ct=World/News&u=http%3a%2f%2fwww.news24.com%2fWorld%2fNews%2fChile-president-cautious-as-82-quake-kills-5-20140402&uid=&luid=&sn=";
</script>
<noscript>
<img src="http://stats.24.com/content/image.articleview?rnd=635320296005569347&s=5&c=1073&a=23a7c7b3-778f-44cc-8ce2-d9a79664db16&t=Chile+president+cautious+as+8.2+quake+kills+5&ct=World/News&u=http%3a%2f%2fwww.news24.com%2fWorld%2fNews%2fChile-president-cautious-as-82-quake-kills-5-20140402&uid=&luid=&sn=" alt=""/>
</noscript>
</div>

<script type="text/javascript">
//<![CDATA[
var _virtualPath = 'http://www.news24.com/';//]]>
</script>
</form>
    
    



    <div class="personalisationContainer">
        <div class="personalisationNav">
            <div class="topNavWrapper">
                <div class="left bold headerLinks">
                    <span id="site_languages_dropdown"><a href="http://www.news24.com" data-track="outbound,topbar,news24.com" class="deepblue bold">News24</a></span>
                </div>
                <div class="site_languages">
                    <div style="color: #848484;">
                        English</div>
                    <div style="margin-top: 10px;">
                        <a href="http://afrikaans.news24.com">Afrikaans</a></div>
                    <div style="margin-top: 10px;">
                        <a href="http://isizulu.news24.com">isiZulu</a></div>
                </div>
                <div class="bold headerLinks left" style="margin-left:5px;">
                    <span class="grey">|&nbsp;&nbsp;<a href="http://www.olx.co.za" data-track="outbound,topbar,olx.co.za" class="grey bold">OLX</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://www.pricecheck.co.za/" data-track="outbound,topbar,pricecheck.co.za" class="grey bold">PriceCheck</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://www.property24.com" data-track="outbound,topbar,property24.com" class="grey bold">Property24</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://etrader.kalahari.com/referral.asp?linkid=7002&partnerid=9180" data-track="outbound,topbar,kalahari.com" class="grey bold">Kalahari.com</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://www.careers24.com" data-track="outbound,topbar,careers24.com" class="grey bold">Careers24</a></span>
                </div>
            </div>
            

<script type="text/javascript">
    function CheckUsernameAvailable() { var a = $j("#txtUsername").val(); var b = new RegExp("^[a-zA-Z0-9-_]*$"); if (!a == "") { if (!a.match(b)) $j("#originalHeader").fadeOut("fast", function () { $j("#headerUsernameError").html("Your username may not contain any spaces or special characters.").fadeIn("fast") }); else news24.getAjax("/Ajax/UgcData/", "CheckUsernameAvailability", { 'username': a }, CheckUsernameAvailableCallback) } else $j("#originalHeader").fadeOut("fast", function () { $j("#headerUsernameError").html('Please enter a username and then click "Register"').fadeIn("fast") }) } function CheckUsernameAvailableCallback(a) { if (!a.error && a != "error") { if (a == true) { $j("#enterUsernameDiv").fadeOut("fast", function () { $j("#spanNewUsername").html($j("#txtUsername").val()); $j("#txtDisplayName").val($j("#txtUsername").val()); $j("#personaliseProfileDiv").fadeIn("fast") }) } else $j("#originalHeader").fadeOut("fast", function () { $j("#headerUsernameError").html("Sorry, that username is not available").fadeIn("fast") }) } } function ResetAvatar() { $j.ajax({ url: "/AvatarRemove.axd?filename=" + $j("#avatarImage").attr("src"), type: "POST" }); $j("#avatarImage").attr("src", user.avatarUrl); $j("#btnResetAvatar").fadeOut() } function SaveUserProfile() {$j("#displayNameError").fadeOut("fast"); $j("#profileSaveError").fadeOut("fast"); var a = true; var b = escape($j("#txtDisplayName").val()); user.bio = escape($j("#txtAboutMe").val()); user.avatarUrl = $j("#avatarImage").attr("src"); user.name = escape($j("#txtUsername").val()); if (b == "") { a = false; $j("#displayNameError").fadeIn("fast") } else user.displayName = b; if (a) { $j("#personaliseProfileDiv").fadeOut("fast"); $j(".saveProfile").fadeIn("fast"); var data = JSON.stringify({ userSettings: user }); news24.getAjax("/Ajax/UgcData/", "SaveTinaProfile", data, SaveUserProfileCallback, null, "POST") }} function SaveUserProfileCallback(a) { if (!a.error && a.value != "error") { if (a.value === "upload") { $j(".saveProfile").fadeOut("fast"); $j("#personaliseProfileDiv").fadeIn("fast"); $j("a.call2action").click(); user.referrer = "" } else { $j("#fancybox-close").click(); location.reload(true) } } else { $j(".saveProfile").fadeOut("fast"); $j("#personaliseProfileDiv").fadeIn("fast"); $j("#profileSaveError").fadeIn("fast") } } function CheckCharacterCount(a) { a = a || window.event; var b = a.keyCode; if (b == 8 || b == 46) return true; else if ($j("#txtAboutMe").val().length < 1e3) return true; else return false } var user = { name: "", displayName: "", userid: "", avatarUrl: "", bio: "", referrer: "" }; var hasProfile = ""; $j(document).ready(function () { $j("#createProfileFire").fancybox({ padding: 0, centerOnScroll: true }); var a = $j("#btnUploadAvatar"); var b = $j("#avatarError"); new AjaxUpload(a, { action: "/AvatarUpload.axd", name: "uploadfile", data: { userid: user.userid }, onSubmit: function (a, c) { if (!(c && /^(jpg|png|jpeg|gif)$/.test(c))) { b.html("Only JPG, PNG or GIF files are allowed").fadeIn(); return false } b.html("Uploading...").fadeIn() }, onComplete: function (a, c) { b.html(""); if (!c.error) { var d = $j($j(c)[1]).html(); if (d != "error") { user.avatarUrl = $j("#avatarImage").attr("src"); $j("#avatarImage").attr("src", d); b.fadeOut().html(""); $j("#btnResetAvatar").fadeIn() } else b.html("* The image you selected could not be uploaded.").fadeIn() } else b.html("* The image you selected could not be uploaded.").fadeIn() } }); if (hasProfile == "true") { $j("#enterUsernameDiv").hide(); $j("#spanNewUsername").html(unescape(user.name)); $j("#txtDisplayName").val(unescape(user.displayName)); $j("#txtAboutMe").val(unescape(user.bio)); $j("#personaliseProfileDiv").show() } })
</script>

<a id="createProfileFire" style="display:none;" href="#createProfileModal">&nbsp;</a>
<input type="hidden" name="userid" value="" />
<div style="display:none;">
    <div id="createProfileModal">
        <div id="enterUsernameDiv">
            <div class="userheader"><h2>Hello&nbsp;<strong></strong></h2></div>
            <div class="step1_content">
                <h3>Create Profile</h3>
                 <p>Creating your profile will enable you to submit photos and stories to get published on News24.</p><br />
                <h3 id="originalHeader">Please provide a username for your profile page:</h3>
                <h3 id="headerUsernameError" style="display:none"></h3>
                <p>This username must be unique, cannot be edited and will be used in the URL to your profile page across the entire 24.com network.</p>
                <div class="formborder">
                    <input type="text" id="txtUsername" class="username_form" />
                </div>
            </div>
            <div class="reg_btn2"><input type="button" id="btnRegister" value="Register" onclick="CheckUsernameAvailable();" /></div>
        </div>
        <div id="personaliseProfileDiv" style="display:none;">
            <div class="userheader"><h2>Hello&nbsp;<strong><span id="spanNewUsername"></span></strong></h2></div>
            <div class="step2_content">
                <h3>Choose a display name:</h3>
                <div class="formborder">
                    <input type="text" id="txtDisplayName" />
                </div>
                <span id="displayNameError" >* You must provide a display name.</span>
                <h3>Edit your avatar:</h3>
                <div class="changeprofile">
                    <img id="avatarImage" height="35" width="35" />
                    <span class="selectp_img">Select an image file on your computer (max 4MB):</span>
                    <input type="button" id="btnUploadAvatar" value="Upload" />
                    <input type="button" id="btnResetAvatar" value="Reset" onclick="ResetAvatar();"  style="display:none;"/>
                    <span id="avatarError">* The image you selected could not be uploaded.</span>
                </div>
                <h3>Tell us a bit about yourself:</h3>
                <textarea id="txtAboutMe" cols="55" rows="6" onkeydown="return CheckCharacterCount(event);"></textarea>
                <div id="profileSaveError" style="color:Red;font-size:12px;display:none;">* Your profile could not be saved at the moment. Please try again later.</div>
            </div>
            <div class="reg_btn"><input type="button" id="btnSaveUserProfile" value="Save" onclick="SaveUserProfile();" /></div>
        </div>
        <div class="saveProfile" style="text-align:center;display:none;">
            <div style="height:170px;">&nbsp;</div>
            <div style="height:40px;">
                <h3 style="font-weight:bold;font-size: 20px;">Saving your profile</h3>
                <img src="http://static.24.co.za/5/images/ajax-loader-bar.gif" />
            </div>
            <div style="height:170px;">&nbsp;</div>
        </div>
    </div>
</div>
            
<div id="toppanel">
    <div class="tab right">
        
        <div id="pnlLoggedOut">
	
            <ul class="loggedOut">
                <li id="togglePanel" class="logout"><a id="openPanel" class="point_down" href="javascript:void(0);">Login / SignUp</a> <a id="closePanel" style="display: none;" class="point_up" href="#">Login / SignUp</a> </li>
            </ul>
        
</div>
    </div>
    <div id="pnlSettings">
	
        <div id="panel">
            <div class="content">
                <h1 class="bold">
                    Settings</h1>
                
                <div id="divModalContent">
                    <div class="info">
                        <a href="#" class="name">Location Settings</a><br />
                        <p>
                            News24 allows you to edit the display of certain components based on a location.
                            If you wish to personalise the page based on your preferences, please select a
                            location for each component and click "Submit" in order for the changes to
                            take affect.</p>
                    </div>
                    <div class="info left">
                        <div class="left selectBox">
                            <label>
                                Most Read Block</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selUserLocation" id="selUserLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="capetown">Cape Town</option>
		<option value="george">George</option>
		<option value="johannesburg">Johannesburg</option>
		<option value="pretoria">Pretoria</option>
		<option value="eastlondon">East London</option>
		<option value="portelizabeth">Port Elizabeth</option>
		<option value="bloemfontein">Bloemfontein</option>
		<option value="durban">Durban</option>
		<option value="pietermaritzburg">Pietermaritzburg</option>
		<option value="polokwane">Polokwane</option>
		<option value="nelspruit">Mbombela</option>
		<option value="kimberley">Kimberley</option>
		<option value="mafikeng">Mahikeng</option>
	</select>
                            <span id="userLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Weather</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selWeatherLocation" id="selWeatherLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="capetown">Cape Town</option>
		<option value="george">George</option>
		<option value="johannesburg">Johannesburg</option>
		<option value="pretoria">Pretoria</option>
		<option value="eastlondon">East London</option>
		<option value="portelizabeth">Port Elizabeth</option>
		<option value="bloemfontein">Bloemfontein</option>
		<option value="durban">Durban</option>
		<option value="pietermaritzburg">Pietermaritzburg</option>
		<option value="polokwane">Polokwane</option>
		<option value="nelspruit">Mbombela</option>
		<option value="kimberley">Kimberley</option>
		<option value="mafikeng">Mahikeng</option>
	</select>
                            <span id="weatherLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Traffic</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selTrafficLocation" id="selTrafficLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="western cape">Western Cape</option>
		<option value="gauteng">Gauteng</option>
		<option value="eastern cape">Eastern Cape</option>
		<option value="free state">Free State</option>
		<option value="kwazulu-natal">KwaZulu-Natal</option>
		<option value="limpopo">Limpopo</option>
		<option value="mpumalanga">Mpumalanga</option>
		<option value="northern cape">Northern Cape</option>
		<option value="north-west">North-West</option>
	</select>
                            <span id="trafficLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Jobs</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selJobLocation" id="selJobLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="western cape">Western Cape</option>
		<option value="gauteng">Gauteng</option>
		<option value="eastern cape">Eastern Cape</option>
		<option value="free state">Free State</option>
		<option value="kwazulu-natal">KwaZulu-Natal</option>
		<option value="limpopo">Limpopo</option>
		<option value="mpumalanga">Mpumalanga</option>
		<option value="northern cape">Northern Cape</option>
		<option value="north-west">North-West</option>
	</select>
                            <span id="careersLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Property Listings</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selPropertyLocation" id="selPropertyLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="western cape">Western Cape</option>
		<option value="gauteng">Gauteng</option>
		<option value="eastern cape">Eastern Cape</option>
		<option value="free state">Free State</option>
		<option value="kwazulu-natal">KwaZulu-Natal</option>
		<option value="limpopo">Limpopo</option>
		<option value="mpumalanga">Mpumalanga</option>
		<option value="northern cape">Northern Cape</option>
		<option value="north-west">North-West</option>
	</select>
                            <span id="propertyLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Kalahari Listings</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selKalahariLocation" id="selKalahariLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="capetown">Cape Town</option>
		<option value="george">George</option>
		<option value="johannesburg">Johannesburg</option>
		<option value="pretoria">Pretoria</option>
		<option value="eastlondon">East London</option>
		<option value="portelizabeth">Port Elizabeth</option>
		<option value="bloemfontein">Bloemfontein</option>
		<option value="durban">Durban</option>
		<option value="pietermaritzburg">Pietermaritzburg</option>
		<option value="polokwane">Polokwane</option>
		<option value="nelspruit">Mbombela</option>
		<option value="kimberley">Kimberley</option>
		<option value="mafikeng">Mahikeng</option>
	</select>
                            <span id="kalahariLocationError" style="display: none; color: Red;">*</span>
                            <p id="errorMessage" style="display: none; color: Red;">
                                Please select a value from the drop down box.</p>
                        </div>
                        <br />
                        <div class="left" style="clear:both;">
                            <input id="btCloseSettings" type="button" name="submit" value="Close" class="bt_login" />
                            <input id="bntSaveLocations" type="button" name="submit" value="Save" class="bt_login" />
                        </div>
                    </div>
                </div>
                <div id="savingSettings" style="display: none;">
                    <div class="info" style="margin-top: 95px; text-align: center;">
                        <h3 style="font-weight: bold; font-size: 20px; margin-bottom: 20px;">
                            Saving your settings</h3>
                        <img src="http://static.24.co.za/5/images/ajax-loader-bar.gif"  />
                    </div>
                </div>
            </div>
        </div>
        <!-- /login -->
    
</div>
    <div id="logoutPanel">
        <div class="content">
            <h1 class="bold">
                Facebook Sign-In</h1>
            <div>
                <div class="info">
                    <p>
                        <strong>Hi News addict,</strong>
                    </p>
                    <p>
                        Join the News24 Community to be involved in breaking the news.
                    </p>
                    <p>
                        Log in with Facebook to comment and personalise news, weather and listings.
                    </p>                
                    <div class="facebook_login">                          
                        <a href="javascript:void(0);" class="submit_button">
                            <img src="http://static.24.co.za/5/images/facebookicon_login.png" width="228" height="75" border="0" title="Login with your Facebook account" alt="Login with your Facebook account" /></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
    function setLocationDropdowns() { $j("#selUserLocation")[0].selectedIndex = $j("#selUserLocation").attr("orig"); $j("#selWeatherLocation")[0].selectedIndex = $j("#selWeatherLocation").attr("orig"); $j("#selTrafficLocation")[0].selectedIndex = $j("#selTrafficLocation").attr("orig"); $j("#selJobLocation")[0].selectedIndex = $j("#selJobLocation").attr("orig"); $j("#selPropertyLocation")[0].selectedIndex = $j("#selPropertyLocation").attr("orig"); $j("#selKalahariLocation")[0].selectedIndex = $j("#selKalahariLocation").attr("orig") } $j("#open").click(function () { $j("div#panel").slideDown("slow"); setLocationDropdowns() }); $j("#openPanel,#closePanel").click(function () { if ($j("div#logoutPanel").is(":visible")) { $j("div#logoutPanel").hide("fast") } else { $j("div#logoutPanel").slideDown("fast") } }); $j("#close,#btCloseSettings").click(function () { $j("div#panel").slideUp("fast"); setLocationDropdowns() }); $j("#toggle a,#btCloseSettings").click(function () { $j("#toggle a").toggle(); if ($j(".top_user_profile_edit").is(":visible")) { $j("#toppanel #lnkEditProfile").attr("class", "point_down"); $j(".top_user_profile_edit").hide() } }); $j("#togglePanel a").click(function () { $j("#togglePanel a").toggle() }); $j("#bntSaveLocations").click(function () { $j("#divModalContent").hide(); $j("#savingSettings").fadeIn("slow"); var a = "/Handlers/SaveLocations.ashx?"; a += "UserLocation=" + $j("#selUserLocation").val() + "&"; a += "WeatherLocation=" + $j("#selWeatherLocation").val() + "&"; a += "TrafficLocation=" + $j("#selTrafficLocation").val() + "&"; a += "JobLocation=" + $j("#selJobLocation").val() + "&"; + "&"; a += "PropertyLocation=" + $j("#selPropertyLocation").val() + "&"; a += "KalahariLocation=" + $j("#selKalahariLocation").val(); $j.ajax({ type: "GET", url: a, success: function (a) { if (a != "error") { location.reload(true) } } }); return false }); $j("#btnLogout").click(function () { window.location = "http://auth.news24.com/DeAuthenticate.aspx?surl=http://www.news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402" }); $j("#toppanel li.user").click(function () { if ($j(".top_user_profile_edit").is(":visible")) $j("#toppanel #lnkEditProfile").attr("class", "point_down"); else $j("#toppanel #lnkEditProfile").attr("class", "point_up"); $j(".top_user_profile_edit").toggle(); $j("#toggle a.close").hide(); $j("#toggle a.open").show(); $j("div#panel").slideUp("fast"); setLocationDropdowns() });
</script>

            <div class="clr10">&nbsp;</div>
        </div>
    </div>
    
    
    <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/json/json2.js?v=20140319" ></script>
    <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/24com/tina/1.0/loginwindow.js?v=20140319" ></script>
    
    <script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/minified/basescript2.min.js?v=20140319" ></script>
    
    <script type="text/javascript">
        $j(document).ready(function () {$j("a.group,a.mynewspics").easyTooltip();});
        $j('.submit_button').click(function () { OpenTinaLoginWindow(); });
         function OpenTinaLoginWindow(permission) {
            json = { refreshPage: true, loginProvider: 'Facebook', tinaBaseUrl: 'http://auth.news24.com' };
            json.scope = this;
             if (permission)
                 json.permission = permission;
             Tina.openLoginWindow(json);
         }
        tinaUrl = 'http://auth.news24.com';
    </script>
    

    
        
        <script type='text/javascript'>
            var SiteSection = window.location.pathname.replace(/^\/([^\/]*).*$/, '$1');
            if (SiteSection == "")
                SiteSection = "HomePage";
            var _sf_async_config = {}; _sf_async_config.uid = 8959; _sf_async_config.domain = "news24.com"; _sf_async_config.sections = SiteSection ; _sf_async_config.authors = "News24"; (function () { function a() { window._sf_endpt = (new Date).getTime(); var a = document.createElement("script"); a.setAttribute("language", "javascript"); a.setAttribute("type", "text/javascript"); a.setAttribute("src", ("https:" == document.location.protocol ? "https://a248.e.akamai.net/chartbeat.download.akamai.com/102508/" : "http://static.chartbeat.com/") + "js/chartbeat.js"); document.body.appendChild(a) } var b = window.onload; window.onload = typeof window.onload != "function" ? a : function () { b(); a() } })()
        </script>
    <script type="text/javascript">
var idleInterval;var idleTime = 0;
$j(document).ready(function() {
if(!jQuery.cookie('closeidlead')){
idleInterval = setInterval("timerIncrement()", 1000); 
$j(this).mousemove(function(e) {idleTime = 0;});
$j(this).keypress(function(e) {idleTime = 0;});
$j(this).click(function (e) {idleTime = 0;});
}
});
function timerIncrement() {
idleTime = idleTime + 1;
if (idleTime == 1800) {
clearInterval(idleInterval);
GA24.trackEvent('IdleAd,open');
var popupUrl = '/IdlePopupPage.html?domain=' + document.domain + '&zone=' + za24_AdZone; 
$j("<a href='" + popupUrl + "'></a>" ).fancybox({'width':730,'height':508, 'type': 'iframe', 'padding': '0px', 'scrolling':'auto'}).click();
} 
}
</script>

    <div id='ad-200x400-1' class='24ad200x400'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('200x400','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/World/Articles&sz=200x400&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/World/Articles&sz=200x400&c=650617686&t=artid%3d23a7c7b3-778f-44cc-8ce2-d9a79664db16%26People%3dmichelle+bachelet%26Places%3dchile%26Topics%3dearthquakes%26posno%3d1' border='0' alt=''></a></noscript>
</body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.news24.com/World/News/Chile-president-cautious-as-82-quake-kills-5-20140402'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, 'Chile president cautious as 8.2 quake kills 5')
        self.assertEqual(doc.summary, "Authorities kept hundreds of thousands of people out of their beds after a magnitude-8.2 earthquake struck off Chile's northern coast. ")
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '02 04 2014')
        self.assertEqual(doc.author.name, "AP")
        self.assertEqual(doc.medium.name, 'News24')

        self.assertEqual(doc.text, u'Santiago - Authorities kept hundreds of thousands of people out of their beds early on Wednesday after a magnitude-8.2 earthquake struck off Chile\'s northern coast. Five people were crushed to death or suffered fatal heart attacks, a remarkably low toll for such a powerful shift in the Earth\'s crust.The extent of damage from Tuesday night\'s quake couldn\'t be fully assessed before daybreak, President Michelle Bachelet said, but she wasn\'t taking any chances. She declared a state of emergency in the region and sent a military plane with 100 anti-riot police to join 300 soldiers deployed to prevent looting and round up escaped prisoners.The shaking loosed landslides that blocked roads, knocked out power for thousands, damaged an airport and provoked fires that destroyed several businesses. About 300 inmates escaped from a women\'s prison in the city of Iquique. In Arica, another city close to the quake\'s offshore epicentre, hospitals treated minor injuries, and some homes made of adobe were destroyed, authorities said. Chilean Interior Minister Rodrigo Penailillo announced the five deaths.Bachelet\'s government extended its tsunami warnings for northernmost Chile long after they were lifted elsewhere. Its mandatory evacuation orders remained in effect until nearly dawn for coastal areas north of Antofogasta, a decision backed by the Pacific Tsunami Warning Centre in Hawaii."We regard the coast line of Chile as still dangerous, so we\'re maintaining the warning," geophysicist Gerard Fryer told The Associated Press.Significant aftershocksBachelet, who just returned to the presidency three weeks ago, spoke well after midnight, five hours after the quake struck.It was not lost on many Chileans that the last time she presided over a major quake, days before the end of her 2006-10 term, her emergency preparedness office prematurely waved off a tsunami danger.Most of the 500 dead from that magnitude-8.8 tremor survived the shaking, only to be caught in killer waves in a disaster that destroyed 220 000 homes and washed away large parts of many coastal communities."The country has done a good job of confronting the emergency. I call on everyone to stay calm and follow the authorities\' instructions," Bachelet tweeted after Tuesday night\'s temblor.When she finally addressed the nation, she said her interior minister would monitor the tsunami threat throughout the night and co-ordinate the emergency response. "Classes have been suspended, and we will be able to know the extent of the damage in the light of day," she added.The tsunami warning centre cancelled tsunami watches for areas other than northern Chile and southern Peru. The only US impact might be higher waves on Wednesday for Hawaii\'s swimmers and surfers, it said.The US Geological Survey initially reported the quake at 8.0, but later upgraded the magnitude of the quake that struck 99km northwest of Iquique. More than 20 significant aftershocks followed, including a 6.2 tremor. More aftershocks and even a larger quake could not be ruled out, said seismologist Mario Pardo at the University of Chile.Psychiatrist Ricardo Yevenes said he was with a patient in Arica when the big one hit."It quickly began to move the entire office, things were falling," he told local television. "Almost the whole city is in darkness."The quake was so strong that the shaking experienced in Bolivia\'s capital about 470km away was the equivalent of a 4.5-magnitude tremor, authorities there said.Chile is one of the world\'s most earthquake-prone countries because just off the coast, the Nazca tectonic plate plunges beneath the South American plate, pushing the towering Andes cordillera to ever-higher altitudes.The latest activity began with a strong magnitude-6.7 quake on 16 March that caused more than 100 000 people to briefly evacuate low-lying areas. Hundreds of smaller quakes followed in the weeks since, keeping people on edge as scientists said there was no way to tell if the unusual string of tremors was a harbinger of an impending disaster.\n\n\n\n')
        

    def test_extract_new_article_style(self):
        html = """



<!DOCTYPE html>
<!--[if IE 7]><html class="ie7" lang="en"> <![endif]-->
<!--[if IE 8]><html class="ie8" lang="en"> <![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js" lang="en">
<!--<![endif]-->
<head><meta name="description" content="Tau SA has lodged an objection against President Jacob Zuma as a candidate in the 7 May general elections, the agriculture union says." /><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><meta name="viewport" content="width=device-width" /><title>
	TAU SA objects to Zuma candidacy | News24
</title><meta property="article:published_time" content="2014/04/02 07:11:50 AM"/><meta property="article:modified_time" content="2014/04/02 07:11:50 AM"/><meta property="article:expiration_time" content="2014/04/04 09:56:51 AM"/><meta property="twitter:card" content="summary"/><meta property="twitter:url" content="http://www.news24.com/elections/news/tau-sa-objects-to-zuma-candidacy-20140401"/><meta property="twitter:title" content="TAU SA objects to Zuma candidacy"/><meta property="twitter:site" content="News24"/><meta property="twitter:description" content="Tau SA has lodged an objection against President Jacob Zuma as a candidate in the 7 May general elections, the agriculture union says."/><meta property="twitter:image" content="http://cdn.24.co.za/files/Cms/General/d/2725/ff726a9c38b8463889ec023c4ff1361f.jpg"/><meta property="twitter:app:name:iphone" content="News24"/><meta property="twitter:app:id:iphone" content="310970460"/><meta property="twitter:app:name:ipad" content="News24"/><meta property="twitter:app:id:ipad" content="310970460"/><meta property="twitter:app:url:iphone" content="https://itunes.apple.com/za/app/news24/id310970460?mt=8"/><meta property="twitter:app:url:ipad" content="https://itunes.apple.com/za/app/news24/id310970460?mt=8"/><meta property="og:site_name" content="News24"/><meta property="fb:app_id" content="2363277980"/><meta property="fb:page_id" content="10227041841"/><meta property="og:title" content="TAU SA objects to Zuma candidacy"/><meta property="og:type" content="article"/><meta property="og:url" content="http://www.news24.com/elections/news/tau-sa-objects-to-zuma-candidacy-20140401"/><meta property="og:image" content="http://cdn.24.co.za/files/Cms/General/d/2218/1de6a3d1226d4698916def9161a0a9f7.jpg"/><meta property="og:description" content="Tau SA has lodged an objection against President Jacob Zuma as a candidate in the 7 May general elections, the agriculture union says."/><link rel="canonical" href="http://www.news24.com/elections/news/tau-sa-objects-to-zuma-candidacy-20140401"/><script type="text/javascript" language="javascript">
var addthis_share =
{
url: "http://www.news24.com/elections/news/tau-sa-objects-to-zuma-candidacy-20140401",
title: "TAU SA objects to Zuma candidacy",
description: "Tau SA has lodged an objection against President Jacob Zuma as a candidate in the 7 May general elections, the agriculture union says.",
templates:
{
twitter: "{{title}}: {{url}} via @News24"
},
url_transforms: {
shorten: {
twitter: 'bitly'
}
},
shorteners: {
bitly: {
login: '24com',
apiKey: 'R_ca79efd5a0978fb80d1d853bac1dda83'
}}};
</script>
<link type="text/css" rel="stylesheet" href="http://www.news24.com/elections/styles/site.css?v=201404012" /><link type="text/css" rel="stylesheet" href="http://www.news24.com/elections/styles/socialshare.css?v=201404012" /><link type="text/css" rel="stylesheet" href="http://www.news24.com/elections/styles/font-awesome.min.css?v=201404012" /><link type="text/css" rel="stylesheet" href="http://scripts.24.co.za/libs/fancybox/jquery.fancybox.css?v=201404012" /><script type="text/javascript" language="javascript" src="http://www.news24.com/elections/scripts/common-top.min.js?v=201404012" ></script><script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/fancybox/fancybox-1.3.4.min.js?v=201404012" ></script>
        <script type="text/javascript">
            var $j = jQuery.noConflict();
            document.domain = "news24.com";
            var _sf_startpt = (new Date()).getTime();
            var tinaUrl = 'http://auth.news24.com';
            var logoutUrl = 'http://auth.news24.com/DeAuthenticate.aspx?surl=http://wwwelections.news24.com//Elections/news/tau-sa-objects-to-zuma-candidacy-20140401';
        </script>
    <script sync type="text/javascript" src="http://scripts.24.co.za/libs/24com/portal/1.0/common.min.js?v=201404012"></script><script type="text/javascript">var _gaq = _gaq || [];_gaq.push(['_setDomainName', 'www.news24.com']);_gaq.push(['_setAccount', 'UA-45055449-1']);_gaq.push(['_trackPageview']);
                                    (function() {var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                                    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                                    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
                                    })();</script>
    

<link href="http://scripts.24.co.za/libs/24com/comments/3.0.1/styles/comments.min.css" type="text/css" rel="stylesheet"></link>
<!-- Start of DClick Header -->
<!-- Site: /8900/24.com/Web/News24, Zone: /Elections, MapsTo: "News" -->

<script src='//www.googletagservices.com/tag/js/gpt.js' type='text/javascript' ></script>
<script src="http://scripts.24.co.za/libs/24com/Ads/3.0/24AdScript.min.js" language="JavaScript" type="text/javascript"></script>
<script language="JavaScript" type="text/javascript">//<![CDATA[
za24_AdSite = '/8900/24.com/Web/News24'; 
za24_AdZone = '/Elections';
za24_IsAsync  = false;
za24_InterstitialEnabled=false;
za24_KeywordType[1]='artid'; za24_Keywords[1]='d084f70b-ffb0-4723-b3bd-769daa09255f'; 
za24_KeywordType[2]='companies'; za24_Keywords[2]='iec,tau sa'; 
za24_KeywordType[3]='people'; za24_Keywords[3]='jacob zuma,pansy tlakula'; 
za24_KeywordType[4]='topics'; za24_Keywords[4]='elections 2014,politics'; 

za24_AdSize[1]='728x90'; za24_AdPositionNo[1]='1'; 
za24_AdSize[2]='300x600'; za24_AdPositionNo[2]='1'; 
za24_AdSize[3]='300x250'; za24_AdPositionNo[3]='1'; 
za24_AdSize[4]='300x250'; za24_AdPositionNo[4]='2'; 
za24_AdSize[5]='1000x1000'; za24_AdPositionNo[5]='1'; 
za24_AdSize[6]='278x76'; za24_AdPositionNo[6]='1'; 
za24_InitAds();
//--></script>
<!-- End of DClick Header -->
</head>
<body>
    <!-- EM CODE -->
    <script type="text/javascript">
        (function () { var em = document.createElement('script'); em.type = 'text/javascript'; em.async = true; em.src = ('https:' == document.location.protocol ? 'https://za-ssl' : 'http://za-cdn') + '.effectivemeasure.net/em.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(em, s); })();
    </script>
    <noscript>
        <img src="//za.effectivemeasure.net/em_image" alt="" style="position: absolute; left: -5px;" />
    </noscript>
    <!--EM CODE -->

    <form name="form1" method="post" id="form1">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="dkFGrz8ujGT6umzYWKTWA6pIgDqSxOkw0+JUVt24mcEv8tPMKl8bKwmtAfqe2DxnBWw6fAsKj4Zxg03s++oYfvER+QU=" />
</div>

<div class="aspNetHidden">

	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="1wJh/owCpUZGNhe3SuqiLpaMNFGS88N2vMQkUWcCkXPDJX68gvjrOJ+mPhMhlzp2wagTkwLiB/T5sdcAP6MAWg5nYvCN4oxoVsI4/dg6WbI5CtzLbCxmk9PHE6ND17+du7A3VziPR/kAZYs2I5xZbW/CYyHhPHXSehzCtERE/skqM7tI" />
</div>
        <script type="text/javascript">if(typeof za24_Keywords != "undefined") za24_Keywords ="iec,tausa,jacobzuma,pansytlakula,elections2014,politics";</script>
        <div style="display: none;">
            <script type="text/javascript">
jQuery('head').append("<link href='http://scripts.24.co.za/libs/24com/ads/2.0/Style/TransAd.css?v=201404012' type='text/css' rel='stylesheet' ></link>")
</script>
<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/ads/2.0/script/TransAd.min.js?v=201404012"></script>
<div id='ad-10x10-1' class='24ad10x10'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('10x10','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/Elections&sz=10x10&c=1034390231&t=artid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26Companies%3diec%2ctau+sa%26People%3djacob+zuma%2cpansy+tlakula%26Topics%3delections+2014%2cpolitics%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/Elections&sz=10x10&c=1034390231&t=artid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26Companies%3diec%2ctau+sa%26People%3djacob+zuma%2cpansy+tlakula%26Topics%3delections+2014%2cpolitics%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
       <div id="ad-728x90-1" class="24ad728x90">
            <div id="ad-728x90-1_ad_container" class="leaderboard">
	            <div id='ad-728x90-1' class='24ad728x90'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('728x90','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/Elections&sz=728x90&c=1034390231&t=artid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26Companies%3diec%2ctau+sa%26People%3djacob+zuma%2cpansy+tlakula%26Topics%3delections+2014%2cpolitics%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/Elections&sz=728x90&c=1034390231&t=artid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26Companies%3diec%2ctau+sa%26People%3djacob+zuma%2cpansy+tlakula%26Topics%3delections+2014%2cpolitics%26posno%3d1' border='0' alt=''></a></noscript>
            </div>
        </div>
        <header class="header">
            
<div class="container headblock">
    <div id="header-top">
        <div class="news24-logo">
            <a class="n24" href="/" title="News24">
            </a>
        </div>
        <div class="weather">
            

<div class="header_weather_box">
    <a href="/UserLocationModal.aspx?iframe&control=weather&fromlog=true" id="lnkModalItem" class="fireEventWeather weatherModal" style="display:none;"></a>
    <h2 id="mainTempDisplay" class="weather-status">
        <a href="javascript:UserLoginCheck(false, 'fireEventWeather', false);" id="lnkChangeWeather" class="city">CAPE TOWN</a>
        <img src="/Elections/images/icons/ForecastsLarge/20.png" id="weatherImgMain" alt="Heavy rain. Mostly cloudy. Mild." />
    </h2>
    <div class="min-temperature"><span class='min_text'>MIN</span><span class='min_temp'>16</span></div>
    <div class="max-temperature"><span class='max_text'>MAX</span><span class='max_temp'>20</span></div>
    <a href="http://pubads.g.doubleclick.net/gampad/clk?id=44943070&iu=/8900/24.com/Web/News24" id="lnkHeaderWeatherSponsor" class="weather-sponsored" target="blank"></a>
    <div class="forecast-7-days" id="weather_info_container">
        <a class="forecast" href="javascript:void(0)"><span class="seven">7</span> <span class="day">day</span></a>
            <ul id="weather_box_info">
                <li>
                    <table cellpadding="0" cellspacing="0" border="0" class="weather_drop_box">
                        
                                <tr>
                                    <td class="d_day">
                                        Thursday</td>
                                    <td class="d_temp">
                                        17-22&deg;c</td>
                                    <td class="d_icon" valign="bottom">
                                        <img src="/images/icons/Forecasts/2.png" alt="More sun than clouds. Mild." /></td>
                                    <td class="d_info">
                                        More sun than clouds. Mild.</td>
                                </tr>
                            
                                <tr>
                                    <td class="d_day">
                                        Friday</td>
                                    <td class="d_temp">
                                        16-23&deg;c</td>
                                    <td class="d_icon" valign="bottom">
                                        <img src="/images/icons/Forecasts/1.png" alt="Sunny. Mild." /></td>
                                    <td class="d_info">
                                        Sunny. Mild.</td>
                                </tr>
                            
                                <tr>
                                    <td class="d_day">
                                        Saturday</td>
                                    <td class="d_temp">
                                        16-25&deg;c</td>
                                    <td class="d_icon" valign="bottom">
                                        <img src="/images/icons/Forecasts/1.png" alt="Sunny. Mild." /></td>
                                    <td class="d_info">
                                        Sunny. Mild.</td>
                                </tr>
                            
                                <tr>
                                    <td class="d_day">
                                        Sunday</td>
                                    <td class="d_temp">
                                        17-28&deg;c</td>
                                    <td class="d_icon" valign="bottom">
                                        <img src="/images/icons/Forecasts/1.png" alt="Sunny. Warm." /></td>
                                    <td class="d_info">
                                        Sunny. Warm.</td>
                                </tr>
                            
                                <tr>
                                    <td class="d_day">
                                        Monday</td>
                                    <td class="d_temp">
                                        21-28&deg;c</td>
                                    <td class="d_icon" valign="bottom">
                                        <img src="/images/icons/Forecasts/2.png" alt="Mostly sunny. Warm." /></td>
                                    <td class="d_info">
                                        Mostly sunny. Warm.</td>
                                </tr>
                            
                                <tr>
                                    <td class="d_day">
                                        Tuesday</td>
                                    <td class="d_temp">
                                        19-28&deg;c</td>
                                    <td class="d_icon" valign="bottom">
                                        <img src="/images/icons/Forecasts/1.png" alt="Sunny. Warm." /></td>
                                    <td class="d_info">
                                        Sunny. Warm.</td>
                                </tr>
                            
                        <tr>
                            <td colspan="4" height="10" valign="bottom" style="vertical-align: bottom">
                                <div style="height: 1px; border-bottom: 1px solid #C6C6C6"></div>
                                <div style="height: 1px; border-top: 1px solid #fff"></div>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="4" class="d_more_link" valign="top">
                                <a href="http://weather.news24.com/sa/cape-town">More weather from Weather24 ></a>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="4" class="ad_link">
                                <div id='ad-278x35-1' class='24ad278x35'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('278x35','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/Elections&sz=278x35&c=344780861&t=artid%3da93fe1ee-a688-4f6b-903c-dbc9055eb9df%26Companies%3dff+plus%2cacdp%2cudm%2cagang+sa%2ciec%2cazapo%2cifp%2ceff%26People%3dpansy+tlakula%2cmamphela+ramphele%2cthuli+madonsela%2cjacob+zuma%2cbantu+holomisa%2cjulius+malema%26Places%3dpretoria%26Topics%3delections+2014%2cpolitics%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/Elections&sz=278x35&c=344780861&t=artid%3da93fe1ee-a688-4f6b-903c-dbc9055eb9df%26Companies%3dff+plus%2cacdp%2cudm%2cagang+sa%2ciec%2cazapo%2cifp%2ceff%26People%3dpansy+tlakula%2cmamphela+ramphele%2cthuli+madonsela%2cjacob+zuma%2cbantu+holomisa%2cjulius+malema%26Places%3dpretoria%26Topics%3delections+2014%2cpolitics%26posno%3d1' border='0' alt=''></a></noscript>
                            </td>
                        </tr>
                    </table>
                </li>
            </ul>
    </div>
</div>

        </div>
    </div>
    <div id="header-bottom">
        <a id="lnkLogo" class="elections-logo" href="/Elections/">ELECTIONS</a>
        <div class="twitter">
            <div class="twitter-icon"></div>
            <div class="twitter-feed">
<script type="text/javascript" language="javascript">
    $j(function () {
        var scripUrl = "/Elections/Scripts/juitter.min.js";
        var searchByWords = $j("#twitterSearchPhrase").val();
        var updateInterval = $j("#twitterUpdateInterval").val();

        if (!$j.Juitter) {
            $j.getScript(scripUrl, function () {
                juitterInit();
            });
        }
        else {
            juitterInit();
        }

        var juitterInit = function() {
            $j.Juitter({
                searchType: "fromUser",
                searchObject: searchByWords + "+exclude:retweets",
                updateInterval: updateInterval,
                lang: "en",
                live: "live-60",
                placeHolder: "juitterContainer",
                loadMSG: "image/gif",
                imgName: "images/loaders/loader_big.gif",
                total: 15,
                readMore: "",
                nameUser: "image",
                openExternalLinks: "newWindow",
                filter: "sex->*BAD word*,porn->*BAD word*,fuck->*BAD word*,shit->*BAD word*"
            });

            $j("#juitterSearch").submit(function() {
                $j.Juitter({
                    searchType: "fromUser",
                    searchObject: $j(".juitterSearch").val(),
                    live: "live-20", // it will be updated every 180 seconds/3 minutes
                    filter: "sex->*BAD word*,porn->*BAD word*,fuck->*BAD word*,shit->*BAD word*",
                    showAvatar: false
                });
                return false;
            });
        };
    });
</script>
<input type="hidden" name="ctl00$ctl00$header$headerTwitter$twitterSearchPhrase" id="twitterSearchPhrase" value="#2014SAelections" />
<input type="hidden" name="ctl00$ctl00$header$headerTwitter$twitterUpdateInterval" id="twitterUpdateInterval" value="60000" />
<div id="twitterPlaceHolder" class="twitter_box left">
    <div id="juitterPlaceHolder" class="col200 left">
        <div id="juitterContainer">
        </div>
    </div>
</div></div>
        </div>
        <div class="download">
        <div class="download-app"></div>
            <a href="https://itunes.apple.com/za/app/news24-elections/id736560036?mt=8" id="lnkAppleDownload" class="apple-download" target="_blank" title="Apple"> </a>
            <a href="https://play.google.com/store/apps/details?id=za.co.elections24" id="lnkAndroidDownload" class="android-download" target="_blank" title="Android"></a>
        </div>
        <div class="left-label"></div>
        <div class="right-label"></div>
    </div>
</div>
            

<nav class="navbar">
	<div class="row">
        <ul class="nav container">
        
        <li class="divider-vertical"><a class="nav_item " data-track="nav,Home" href="/Elections/" target="_self">Home</a></li>
    
        <li class="divider-vertical"><a class="nav_item " data-track="nav,Maps" href="/Elections/Results" target="_self">Maps</a></li>
    
        <li class="divider-vertical"><a class="nav_item  selected" data-track="nav,News" href="/Elections/News" target="_self">News</a></li>
    
        <li class="divider-vertical"><a class="nav_item " data-track="nav,Multimedia" href="/Elections/Multimedia" target="_self">Multimedia</a></li>
    
        <li class="divider-vertical"><a class="nav_item " data-track="nav,Parties" href="/Elections/parties" target="_self">Parties</a></li>
    
        <li class="divider-vertical"><a class="nav_item " data-track="nav,Where to Vote" href="/Elections/WhereToVote" target="_self">Where to Vote</a></li>
    
        <li class="divider-vertical"><a class="nav_item " data-track="nav,Have You Registered?" href="http://www.news24.com/Elections/amiregistered" target="_self">Check Your ID</a></li>
    
           
            <li class="searchbox">
                <input name="ctl00$ctl00$ctl12$txtSearchField" type="text" id="txtSearchField" maxlength="30" placeholder="Search" class="search_field" size="50" onkeypress="var key=event.keyCode||event.which;if (key==13){submitSiteSearch(); return false;}" />
                
            </li>
        </ul>
    </div>
</nav>

<script type="text/javascript">
    var headerSearchUrl = 'http://www.news24.com/search?q={0}'; var txtSearchFieldClientId = "txtSearchField"; function submitSiteSearch() { var a = $j.trim($j("#" + txtSearchFieldClientId).val()); if (a.length > 0) { window.location.href = "/search?q=" + a } };
</script>
        </header>
        <div id="main_wrapper" class="container">
            <div class="row">
                
    
    
    <section class="span8 article-content article_shadow_box">
        

<section class="breadcrumb_block">
    <ul class='breadcrumb'><li><a href='http://www.news24.com/elections'>Elections</a> &nbsp;&gt;&nbsp; </li><li><a href='http://www.news24.com/elections/news'>News</a>  </li></ul>
</section>
        <a id="lnkMoreInCategory" class="more-news" href="http://www.news24.com/elections/news">More News</a>
        <script type="text/javascript" language="javascript" src="http://www.news24.com/elections/scripts/jquery.cluetip.min.js?v=201404012" ></script>
<article>
    <div class="article_header">
        <h1>TAU SA objects to Zuma candidacy</h1>
        <div class="byline"></div>
        <div class="article-share">
            


<!-- AddThis Button BEGIN -->
<div id="addThisShare" class="add_this_share addthis_toolbox social_sharing addthis_floating_style addthis_32x32_style" style="display: none">
    <span class="share-title">SHARE THIS</span>
    <ul style="list-style: none; margin: 0px">
        <li><a class="addthis_button_facebook facebook"></a></li>
        <li><a class="addthis_button_twitter twitter"></a></li>
        <li><a class="addthis_button_google_plusone_share googleplus"></a></li>
        <li><a class="addthis_button_email email"></a></li>
        <li><a class="addthis_button_compact additional"></a></li>   
    </ul>
</div>
<script type="text/javascript">var addthis_config = { "data_track_addressbar": false };</script>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#username=zamedia24"></script>
<!-- AddThis Button END -->


            <span class="datestamp">2014-04-02 07:11</span>
        </div>
    </div>
    <div id="articleImageContainer" class="article-image">
        <img src="http://cdn.24.co.za/files/Cms/General/d/2688/b115317e230140a296e3ce0ed2132b24.jpg" id="imgArticleImage" />
        <div class="caption"><span class="source"></span></div>
    </div>
    <p>Johannesburg - Tau SA has lodged an objection against President <a href="http://whoswho.co.za/jacob-zuma-927" title="" rel="http://www.Whoswho.co.za/hover.php?uid=927" class="tips">Jacob Zuma</a> as a candidate in the 7 May general elections, the agriculture union said on Tuesday. </p><p>It sent a letter to Electoral Commission of SA (IEC) chairperson <a href="http://whoswho.co.za/faith-tlakula-4375" title="" rel="http://www.Whoswho.co.za/hover.php?uid=4375" class="tips">Pansy Tlakula</a> with its objection against Zuma's number one position on the list of African National Congress candidates.</p><p>"He [Zuma] has been recently implicated in a report of the Public Protector regarding possible irregular expenses on his Nkandla homestead, and the fact that he could have misled Parliament on this issue," Tau SA wrote.</p><p>"The full investigation into the so-called weapons scandal [arms inquiry] has not yet been finalised and his name was mentioned in some of the reports on this issue."</p><p>The union said it was of the opinion that an MP had to be free of any suspected involvement in corruption, misappropriation of funds and misleading Parliament.</p><p>"For this reason we object to his nomination as a candidate."</p><p>The deadline for objections to National Assembly and provincial legislature candidates nominated by political parties was 17:00 on Tuesday.</p><p>In terms of the Electoral Act, anyone, including the chief electoral officer, may object to the nomination of a candidate.</p><p>An objection can be made on three grounds: If a candidate does not qualify to stand in the election, if the prescribed acceptance of nomination is not signed by the candidate, and if no undertaking signed by the candidate that he/she is bound by the Electoral Code of Conduct is submitted.</p><p>The IEC would consider all objections and inform the objector and the party of its decision by 17:00 on 7 April. It was not clear on Tuesday evening how many objections the IEC had received.</p><p>The Institute for Accountability in Southern Africa has also filed an objection against Zuma's nomination. The institute said its objection was lodged ex abundante cautela (from excessive caution) as the ANC was still considering the objection letter and had not yet responded substantively to it.</p><p>In an open letter sent to the IEC the institute includes arguments based on the Public Protector's "Secure in Comfort" report on Zuma's Nkandla residence. Also contained in the letter is mention of review proceedings, which the Democratic Alliance has pending against the decision to withdraw 783 charges of corruption, fraud, money laundering and racketeering against Zuma.</p>
    <div id="accreditationName">- SAPA</div>
    
    <div class="share_right">


<!-- AddThis Button BEGIN -->
<div id="addThisShare" class="add_this_share addthis_toolbox social_sharing addthis_floating_style addthis_32x32_style" style="display: none">
    <span class="share-title">SHARE THIS</span>
    <ul style="list-style: none; margin: 0px">
        <li><a class="addthis_button_facebook facebook"></a></li>
        <li><a class="addthis_button_twitter twitter"></a></li>
        <li><a class="addthis_button_google_plusone_share googleplus"></a></li>
        <li><a class="addthis_button_email email"></a></li>
        <li><a class="addthis_button_compact additional"></a></li>   
    </ul>
</div>
<script type="text/javascript">var addthis_config = { "data_track_addressbar": false };</script>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#username=zamedia24"></script>
<!-- AddThis Button END -->

</div>
    

<div id="divKeywordsListing" class="read_more_tags">
    
            <span class="read_more">Read more on: </span>
        
            <span class="tags"><a href="/Tags/Companies/iec">iec</a></span>                     
        &nbsp;|&nbsp;
            <span class="tags"><a href="/Tags/Companies/tau_sa">tau sa</a></span>                     
        &nbsp;|&nbsp;
            <span class="tags"><a href="/Tags/People/jacob_zuma">jacob zuma</a></span>                     
        &nbsp;|&nbsp;
            <span class="tags"><a href="/Tags/People/pansy_tlakula">pansy tlakula</a></span>                     
        &nbsp;|&nbsp;
            <span class="tags"><a href="/Tags/Topics/elections_2014">elections 2014</a></span>                     
        &nbsp;|&nbsp;
            <span class="tags"><a href="/Tags/Topics/politics">politics</a></span>                     
        
</div><br />
    
        <div class="more-articles">
    
        <a href="/Elections/results" id="lnkArticleNav" class="btn_more-articles">Results Maps</a>
    
        <a href="/Elections/Multimedia" id="lnkArticleNav" class="btn_more-articles">Multimedia</a>
    
        <a href="/Elections/Parties" id="lnkArticleNav" class="btn_more-articles">Parties</a>
    
        <a href="/Elections/vote" id="lnkArticleNav" class="btn_more-articles">Polls</a>
    
        </div>
    
</article>

<script type="text/javascript">
    $j(document).ready(function () { var a = $j("a.tips"); a.each(function () { var a = $j(this); a.attr("rel", "/Handlers/WhosWhoTooltip.ashx?url=" + a.attr("rel")) }); a.cluetip({ positionBy: "fixed", topOffset: "-230", leftOffset: "-30", sticky: true, dropShadow: false, showTitle: false, mouseOutClose: true, closeText: "", cluezIndex: 5100 }) })
</script>
        

<div class="more_in_cat">
<span class="more_in_title">More In This Category</span>
    <div class="more_item_container">
    
            <div class="more_items">
                <a href="http://www.news24.com/elections/news/anc-takes-da-to-court-over-smses-20140402" id="lnkThumbnail" class="thumbnailed">
                    
                    <img src="http://cdn.24.co.za/files/Cms/General/d/2511/9afad53c1121457fb38b89e7d42cb499.png" id="imgThumbnail" />
                </a>
                <a id="lnkArticleTitle" class="more_cat_title" href="http://www.news24.com/elections/news/anc-takes-da-to-court-over-smses-20140402">ANC takes DA to court over SMSes</a>
                <p class="more_copy">The North Gauteng High Court is to hear an urgent application by the ANC to stop the DA from sending out an SMS accusing President Jacob Zuma of stealing public money.
</p>
            </div>
        
            <div class="more_items">
                <a href="http://www.news24.com/elections/news/malema-iec-had-potential-to-sleep-with-politicians-20140401" id="lnkThumbnail" class="thumbnailed">
                    
                    <img src="http://cdn.24.co.za/files/Cms/General/d/2725/d2c824bcad9d414788e1c8c1d4398931.jpg" id="imgThumbnail" />
                </a>
                <a id="lnkArticleTitle" class="more_cat_title" href="http://www.news24.com/elections/news/malema-iec-had-potential-to-sleep-with-politicians-20140401">Malema: IEC had potential to 'sleep with politicians'</a>
                <p class="more_copy">The Electoral Commission of SA should be scrutinised to determine whether it was conducting business with politically aligned companies, EFF leader Julius Malema says.</p>
            </div>
        
            <div class="more_items">
                <a href="http://www.news24.com/elections/news/tlakula-has-7-days-to-resign-malema-20140401" id="lnkThumbnail" class="thumbnailed">
                    
                    <img src="http://cdn.24.co.za/files/Cms/General/d/2722/f7130344be564824aa92a1ce359962d2.jpg" id="imgThumbnail" />
                </a>
                <a id="lnkArticleTitle" class="more_cat_title" href="http://www.news24.com/elections/news/tlakula-has-7-days-to-resign-malema-20140401">Tlakula has 7 days to resign - Malema</a>
                <p class="more_copy">Opposition parties will initiate legal proceedings against the Independent Electoral Commission of SA if chairperson Pansy Tlakula does not resign, EFF leader Julius Malema says.</p>
            </div>
        
            <div class="more_items">
                <a href="http://www.news24.com/elections/news/journalist-to-appeal-dismissal-over-da-mp-application-20140401" id="lnkThumbnail" class="thumbnailed">
                    
                    <img src="http://cdn.24.co.za/files/Cms/General/d/2724/a55c73e74702460aa24395b443b3ec2d.jpg" id="imgThumbnail" />
                </a>
                <a id="lnkArticleTitle" class="more_cat_title" href="http://www.news24.com/elections/news/journalist-to-appeal-dismissal-over-da-mp-application-20140401">Journalist to appeal dismissal over DA MP application</a>
                <p class="more_copy">Business Report senior journalist Donwald Pressly will appeal his dismissal by Independent Newspapers for seeking political office with the DA.</p>
            </div>
        
    </div>
</div>
        

<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/comments/3.0.1/scripts/comments.min.js"></script>
<script type="text/javascript" src="http://scripts.24.co.za/libs/json/json2.js"></script>
<script type="text/javascript">
<!--
    // if this script has already been loaded, dont load it again.
    jQuery(function () {
        if (typeof onLogin !== "function") {
            jQuery.getScript("http://scripts.24.co.za/libs/24com/tina/1.0/LoginWindow.js");
        }
    });
-->
</script>

<script type="text/javascript">

<!--
    $j(function() {
        if (typeof commentControl !== "undefined") {
            // settings
            commentControl.sortOrder = "Asc";
            commentControl.pageSize = 20;
            commentControl.tinaBaseUrl = "http://auth.news24.com";
            commentControl.commentStatus = "Unmoderated";
            commentControl.lang = false ? "af" : "en";
            commentControl.locale = "en-za";
            commentControl.site = "News24";
            commentControl.breadCrumb = "News24|Elections|News" ;
            commentControl.objectId = "d084f70b-ffb0-4723-b3bd-769daa09255f";
            commentControl.isDev = false ;
            commentControl.canShowPostedComment = true ;
            commentControl.logOutUrl = "http://auth.news24.com/DeAuthenticate.aspx?surl=http://www.news24.com/elections/news/tau-sa-objects-to-zuma-candidacy-20140401";
            commentControl.auth.user.id = "00000000-0000-0000-0000-000000000000";
            commentControl.auth.user.displayName = "";
            commentControl.auth.user.clickThrough = "";
            commentControl.auth.user.avatarUrl = "http://cdn.24.co.za/Files/RAP2/d/DefaultAvatar/Small.png";
            commentControl.auth.user.openIdType = 0 ;
            commentControl.FacebookHandlerUrl = "/Elections/FacebookToken.ashx";
            commentControl.cacheFacebookAvatar = true;
            commentControl.policyLink = "http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109";
            if (commentControl.auth.util.isFacebookProfile("")) {
                commentControl.auth.user.facebookProfileId = commentControl.auth.util.getFbProfileIdFromAvatarUrl("");
            }
            commentControl.init();
        }
    });
-->
</script>


<span class="comments_title">Comments</span>
<section class="comments_block" id="commentsSection">
    <a href="http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109" id="A1" class="comment_policy"><b>Read News24’s Comments Policy</b></a>

<div class="facebookComments">
    <p>24.com publishes all comments posted on articles provided that they adhere to our <a href="http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109" target="_blank" style="color:white;cursor:pointer;">Comments Policy</a>. Should you wish to report a comment for editorial review, please do so by clicking the 'Report Comment' button to the right of each comment.</p>
</div>
    <div id="comments_wrap">
        <!-- comment on story header -->
        <div id="comment_on_story">
            <div class="fl">
                Comment on this story
            </div>
            <div class="xsmall normal to_lower fl" id="comment_count_wrap">
                <span id="lblTotalCommentCount">76</span>&nbsp;<span id="lblTotalCommentCountText">comments</span>
            </div>
            <div class="clr"></div>
        </div>

        <!-- messages (disabled/closed etc) -->
        
        
        <!-- comment box -->
        
            <div class="comment_form_wrap" id="comment_article_form">
                <div class="comment_form_header to_upper bold">Add your comment</div>
                <div class="comment_form_result_msg bold hidden">Thank you, your comment has been submitted.</div>
                <div class="comment_form_user">
                    <div class="avatar_wrap fl">
                        <div>
                            <img alt="avatar" class="user_avatar_img" />
                        </div>
                    </div>
                    <div class="author_name fl">
                        <a href="#" target="_blank" class="author_link bold user_name"></a>
                    </div>
                    <div class="logout_wrap fr">
                        <a href="#" class="smlr logout_link">Logout</a>
                    </div>
                    <div class="clr"></div>
                </div>
                <div class="comment_form_inner">
                    <span class="comment_form_label bold">Comment</span>
                    <span class="comment_form_remaining_text xsmall italic"><span>0</span> characters remaining</span>
                    <div class="textarea_wrap">
                        <textarea rows="4"></textarea>
                    </div>
                    <div id="divFacebookCheckbox" class="facebook_checkbox">
                        <input type="checkbox" id="chk_facebook" checked="checked" style="float:left;margin-right:10px;" /> <label for="chk_facebook" class="smlr">Share on Facebook</label>
                    </div>
                    <input type="button" value="Post Comment" class="button_submit to_upper smlr" />
                    <div class="ajax-loader hidden"></div>
                </div>
            </div>
        
        
        <!-- comments -->
        <div id="comments_list"></div>
        
        <!-- reusables -->
        <div id="comment_reusables" class="hidden">
            <!-- comment box -->
            <div class="comment_form_wrap" id="comment_reply_form">
                <div class="comment_form_header to_upper bold"></div>
                <div class="comment_form_user">
                    <div class="avatar_wrap fl">
                        <div>
                            <img alt="avatar" class="user_avatar_img" />
                        </div>
                    </div>
                    <div class="author_name fl">
                        <a href="#" target="_blank" class="author_link bold user_name"></a>
                    </div>
                    <div class="logout_wrap fr">
                        <a href="#" class="smlr logout_link">Logout</a>
                    </div>
                    <div class="clr"></div>
                </div>
                <div class="comment_form_inner">
                    <span class="comment_form_label bold">Comment</span>
                    <span class="comment_form_remaining_text xsmall italic"><span>0</span> characters remaining</span>
                    <div class="textarea_wrap">
                        <textarea rows="4"></textarea>
                    </div>
                    <div id="divFacebookCheckboxReply" class="facebook_checkbox">
                        <input type="checkbox" id="chk_facebook_reply" checked="checked" /> <label for="chk_facebook_reply" class="smlr">Share on Facebook</label>
                    </div>
                    <input type="button" value="Post Comment" class="button_submit to_upper smlr" />
                    <div class="ajax-loader hidden"></div>
                </div>
            </div>
        </div>

        <!-- loading -->
        <div id="comment_loader" class="hidden">
            <img src="http://scripts.24.co.za/libs/24com/comments/2.7/images/ajax-loader.gif" alt="Loading comments..." /> Loading comments...
        </div>

        <!-- load more button -->
        <input type="button" id="btn_load_more" class="hidden to_upper smlr" value="Load More Comments" />
    </div>
</section>

    </section>
    
        
    <aside class="span4 sidebar">
        



<div class="welcome">
    <span id="welcomeMessage" class="ugc-title">
        Welcome
    </span>
    

<div class="uploadblack">
    <div class="blackblock_icons">
        <span>UPLOAD</span>
        <a class="call2action" href="http://uploads.news24.com/#images">
            <img width="24" height="24" border="0" alt="" src='/elections/images/icon_gallery.jpg'>
        </a>
        <a class="call2action" href="http://uploads.news24.com/#story">
            <img width="24" height="24" border="0" alt="" src='/elections/images/icon_pen.jpg'>
        </a>
    </div>
</div>
</div>




  <style>
  label {
    display: inline-block;
    width: 5em;
  }
  </style>
<div class="party_selection">
    <div class="party_dropdowns_container">
        <div class="party_block" title="Select a party and location for more specific news and information.">
            <img class="selected_party_image" />
            <span class="selected_party"></span>
            <span class="down_arrow">dwn</span>
        </div>
        <div class="location_block"  title="Select a party and location for more specific news and information.">
            <span class="selected_location"></span>
            <span class="down_arrow">dwn</span>
        </div>
        <div class="select_party_container">
            <div class="party_dropdown" style="display:none;"></div>
        </div>
        <div class="party_selected_container">
            <div class="related-party-options" style="display:none;">
                <a class="party_news_link">Latest News</a>
                <a class="party_history_link">Party History</a>
                <div class="change_party">Change Party</div>
            </div>
        </div>
        <div class="select_location_container">
            <div class="location_dropdown" style="display:none;"></div>
        </div>
        <div class="location_selected_container">
            <div class="location-options" style="display:none;">
                <a class="where_to_vote_link">Where to vote</a>
                <div class="change_location">Change Location</div>
            </div>
        </div>
    </div>
    <div class="select_party_loader"></div>
</div>
<script>jQuery(function(){PartyAndLocationObject.partyList = [{"Abbr": "VF+", "Name": "PARTY: Freedom Front Plus", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/1223/eb6610eea288480eb9a087df6857d29f.jpg", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-freedom-front-plus-20100625"}, {"Abbr": "UDM", "Name": "PARTY: United Democratic Movement", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/1342/885231a1a74b4dc1976f6f014d4cacef.jpg", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-united-democratic-movement-20100625"}, {"Abbr": "IFP", "Name": "PARTY: Inkatha Freedom Party", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/2255/6883c95c8da5416c9a35628db4c0d6c3.jpg", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-inkatha-freedom-party-20100625"}, {"Abbr": "EFF", "Name": "PARTY: Economic Freedom Fighters", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/1936/677f2052e309486da717b946b749c7e7.png", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-eff-20131023"}, {"Abbr": "DA", "Name": "PARTY: Democratic Alliance", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/1915/212c5d63325a4bf8a31934d7f98fba9a.jpg", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-democratic-alliance-20131105"}, {"Abbr": "COPE", "Name": "PARTY: Congress of the People", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/2564/134ea2322ea3485b958fd48e97e0edd1.jpg", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-congress-of-the-people-20100625"}, {"Abbr": "ANC", "Name": "PARTY: African National Congress", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/2402/b782ed7703b64ed68bfa0138ee084d9e.jpg", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-african-national-congress-20100625"}, {"Abbr": "AGANG SA", "Name": "PARTY: Agang SA", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/465/c17395dd76c341fab3881ded84b4b0eb.jpg", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-agang-sa-20131023"}, {"Abbr": "ACDP", "Name": "PARTY: African Christian Democratic Party", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/2667/da9c00c00ec24abda0058a3aa615791f.jpg", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-african-christian-democratic-party-20100625"}, {"Abbr": "ID", "Name": "PARTY: Independent Democrats", "ImageUrl": "http://cdn.24.co.za/files/Cms/General/d/489/4f7da914c2144c4fbb11ac4d7d9eebad.jpg", "PartyPageUrl": "http://www.news24.com/elections/partyinfo/party-independent-democrats-20100625"}];PartyAndLocationObject.locationList = [{"Name": "Eastern Cape", "ID": "EC"}, {"Name": "Free State", "ID": "FS"}, {"Name": "Gauteng", "ID": "GP"}, {"Name": "KwaZulu-Natal", "ID": "KN"}, {"Name": "Limpopo", "ID": "LP"}, {"Name": "Mpumalanga", "ID": "MP"}, {"Name": "North West", "ID": "NW"}, {"Name": "Northern Cape", "ID": "NC"}, {"Name": "Western Cape", "ID": "WC"}];PartyAndLocationObject.selectedLocation = 'western cape';PartyAndLocationObject.init();});</script>
    
      <script>
          $j(function () {
              $j("[title]").tooltip();
          });
  </script>


        

<div class="related-links">
    <div class="related_head">
        <h2>Most Popular</h2>
    </div>
    <ul>
        <li><a id="lnkArticleTitle" href="http://www.news24.com/elections/news/da-takes-on-nkandla-in-april-fools-joke-20140401">DA takes on Nkandla in April Fools joke</a></li><li><a id="lnkArticleTitle" href="http://www.news24.com/elections/news/zille-accepts-elecnomination-challenge-20140331">Zille accepts 'elecnomination' challenge</a></li><li><a id="lnkArticleTitle" href="http://www.news24.com/elections/news/tlakula-has-7-days-to-resign-malema-20140401">Tlakula has 7 days to resign - Malema</a></li><li><a id="lnkArticleTitle" href="http://www.news24.com/elections/news/anc-takes-da-to-court-over-smses-20140402">ANC takes DA to court over SMSes</a></li><li><a id="lnkArticleTitle" href="http://www.news24.com/elections/news/tau-sa-objects-to-zuma-candidacy-20140401">TAU SA objects to Zuma candidacy</a></li>
    </ul>
     <div class="ad278X35 outsurance">
	    <div id='ad-278x76-1' class='24ad278x76'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('278x76','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/Elections&sz=278x76&c=599263459&t=artid%3d6fa15d3d-50bb-4e16-9e17-e232b66442f2%26Companies%3dpublic+protector%2canc%26People%3djacob+zuma%26Places%3dcape+town%26Topics%3dpolitics%2cnkandla+upgrade%2celections+2014%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/Elections&sz=278x76&c=599263459&t=artid%3d6fa15d3d-50bb-4e16-9e17-e232b66442f2%26Companies%3dpublic+protector%2canc%26People%3djacob+zuma%26Places%3dcape+town%26Topics%3dpolitics%2cnkandla+upgrade%2celections+2014%26posno%3d1' border='0' alt=''></a></noscript>
    </div>
</div>
        <div class="adblocktower noad300x600pos1">
            <div id='ad-300x600-1' class='24ad300x600'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('300x600','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/Elections&sz=300x600&c=1034390231&t=artid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26Companies%3diec%2ctau+sa%26People%3djacob+zuma%2cpansy+tlakula%26Topics%3delections+2014%2cpolitics%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/Elections&sz=300x600&c=1034390231&t=artid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26Companies%3diec%2ctau+sa%26People%3djacob+zuma%2cpansy+tlakula%26Topics%3delections+2014%2cpolitics%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
        <div class="spacer clr"></div>
        

<div class="related-links">
    <div class="related_head">
        <h2>Related Links</h2>
    </div>
    <ul>
        
                <li>
                    <a id="lnkRelatedTitle" href="http://www.news24.com/southafrica/politics/da-to-submit-more-evidence-on-zuma-20140401">DA to submit more 'evidence' on Zuma</a>
                </li>
            
                <li>
                    <a id="lnkRelatedTitle" href="http://www.news24.com/elections/news/i-didnt-ask-for-nkandla-upgrade-zuma-20140331">I didn't ask for Nkandla upgrade - Zuma</a>
                </li>
            
                <li>
                    <a id="lnkRelatedTitle" href="http://www.news24.com/elections/news/malema-zuma-must-rot-in-jail-20140329">Malema: Zuma must rot in jail</a>
                </li>
            
    </ul>
</div>

        

<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/vote/1.0/24WeeklyPoll.js?v=2"></script>

<script type="text/javascript">
    articleID = '7b920e0b-a889-4ac2-a37b-f38760009f9d';
</script>
<div id="vote" class="poll">
    <div class="poll-head">
        <h2>Poll</h2>
    </div>
    <p>
        Do you the IEC chairperson Pansy Tlakula should resign?</p>
    <div id="viewVote">
        
                <table class="clr" cellpadding="2" border="0">
                    <tbody>
            
                <tr>
                    <td valign="middle" class="poll_left">
                        <input type="radio" name="SelectedVoteOption" id="SelectedVoteOption" class="radio" value="831a084e-cfb8-429f-8479-f92b368d4e97">
                    </td>
                    <td valign="middle">
                        <span>Yes, she must be held accountable</span>
                    </td>
                </tr>
            
                <tr>
                    <td valign="middle" class="poll_left">
                        <input type="radio" name="SelectedVoteOption" id="SelectedVoteOption" class="radio" value="fb74976d-567f-46f4-bfe6-459ca9d21823">
                    </td>
                    <td valign="middle">
                        <span>Will it change anything?</span>
                    </td>
                </tr>
            
                <tr>
                    <td valign="middle" class="poll_left">
                        <input type="radio" name="SelectedVoteOption" id="SelectedVoteOption" class="radio" value="6d737ea7-dc98-4be3-9276-2715989c4e78">
                    </td>
                    <td valign="middle">
                        <span>Let her stay</span>
                    </td>
                </tr>
            
                </tbody> </table>
            
        <div class="buttons">
            <input name="ctl00$ctl00$MainBodyPlaceholder$BodyContentPlaceholder$PollBlock$btnVote" type="button" id="btnVote" class="vote" value="VOTE" onclick="addVoteOption($j(&#39;input[name=SelectedVoteOption]:checked&#39;).val(), &#39;7b920e0b-a889-4ac2-a37b-f38760009f9d&#39;, &#39;Elections/Vote&#39;);" />
            <input name="results" value="Results" class="result" type="button" onclick="javascript: ShowVoteDiv();" />
        </div>
    </div>
    <div id="writeVote" style="display: none">
        
                <table class="clr" cellpadding="2" border="0">
                    <tbody>
            
                <tr>
                    <td valign="middle">
                        <div class="item">
                            <p class="choice">
                                Yes, she must be held accountable
                                <span class="votes">
                                    77%
                                    77
                                    votes</span>
                            </p>
                            <p class="progressBar">
                                <span><em style="left: 77px;">
                                    77</em> </span>
                            </p>
                        </div>
                    </td>
                </tr>
            
                <tr>
                    <td valign="middle">
                        <div class="item">
                            <p class="choice">
                                Will it change anything?
                                <span class="votes">
                                    12%
                                    12
                                    votes</span>
                            </p>
                            <p class="progressBar">
                                <span><em style="left: 12px;">
                                    12</em> </span>
                            </p>
                        </div>
                    </td>
                </tr>
            
                <tr>
                    <td valign="middle">
                        <div class="item">
                            <p class="choice">
                                Let her stay
                                <span class="votes">
                                    11%
                                    11
                                    votes</span>
                            </p>
                            <p class="progressBar">
                                <span><em style="left: 11px;">
                                    11</em> </span>
                            </p>
                        </div>
                    </td>
                </tr>
            
                </tbody> </table>
            
    </div>
    <div class="more-poll">
        <a id="lnkMorePoll" href="/Elections/Vote">More Polls</a>
    </div>
</div>
        
    </aside>


            </div>
        </div>
        <div style="display: none;">
            <div id='ad-1000x1000-1' class='24ad1000x1000'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('1000x1000','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/Elections&sz=1000x1000&c=1034390231&t=artid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26Companies%3diec%2ctau+sa%26People%3djacob+zuma%2cpansy+tlakula%26Topics%3delections+2014%2cpolitics%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/Elections&sz=1000x1000&c=1034390231&t=artid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26Companies%3diec%2ctau+sa%26People%3djacob+zuma%2cpansy+tlakula%26Topics%3delections+2014%2cpolitics%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
        
    
    


        

<div class="pre_footer ">
    <div class="footer_left">
    <a href="http://www.news24.com" class="n24">
    </a>
        <span class="footer_left-text"> A NEWS24 WEBSITE</span>
    </div>
    <div class="terms">
            <a class="footerContactLink contact-modal" href="/FeedBack.aspx?iframe">CONTACT US</a> | <a class="footerContactLink" href="http://www.news24.com/SiteElements/Services/Terms-and-Conditions-20120413">TERMS &amp; CONDITIONS</a>
    </div>
    <div class="social">
        <a class="twitter" target="_blank" href="https://twitter.com/news24">t</a>
        <a class="facebook" target="_blank" href="https://www.facebook.com/news24">f</a>
    </div>
    <div style="clear:both"></div>
</div>
    
<script type='text/javascript'> $j('#viewVote').show(); $j('#writeVote').hide();</script>
<div id="CmsStats" style="z-index:-1; visibility:hidden;">
<script type="text/javascript" language="JavaScript" >
var cmsStatsImage = new Image();
cmsStatsImage.src = "http://stats.24.com/content/image.articleview?rnd=635320294111125916&s=5&c=1040&a=d084f70b-ffb0-4723-b3bd-769daa09255f&t=TAU+SA+objects+to+Zuma+candidacy&ct=Elections/news&u=http%3a%2f%2fwww.news24.com%2fElections%2fTemplates%2fDesktop%2fArticles%2fArticleDefault.aspx%3fcid%3d1040%26aid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26sid%3d5%26cb%3dElections%252fnews&uid=&luid=&sn=";
</script>
<noscript>
<img src="http://stats.24.com/content/image.articleview?rnd=635320294111125916&s=5&c=1040&a=d084f70b-ffb0-4723-b3bd-769daa09255f&t=TAU+SA+objects+to+Zuma+candidacy&ct=Elections/news&u=http%3a%2f%2fwww.news24.com%2fElections%2fTemplates%2fDesktop%2fArticles%2fArticleDefault.aspx%3fcid%3d1040%26aid%3dd084f70b-ffb0-4723-b3bd-769daa09255f%26sid%3d5%26cb%3dElections%252fnews&uid=&luid=&sn=" alt=""/>
</noscript>
</div>
</form>
    <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/json/json2.js?v=201404012" ></script>
    <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/24com/tina/1.0/LoginWindow.js?v=201404012" ></script>
    <script type="text/javascript" language="javascript" src="http://www.news24.com/elections/scripts/common-bottom.min.js?v=201404012" ></script>
    

 <script type='text/javascript'>
     var SiteSection = window.location.pathname.replace(/^\/([^\/]*).*$/, '$1');
     if (SiteSection == "")
         SiteSection = "Election HomePage";
     var _sf_async_config = {}; _sf_async_config.uid = 8959; _sf_async_config.domain = "news24.com"; _sf_async_config.sections = SiteSection; _sf_async_config.authors = "News24"; (function () { function a() { window._sf_endpt = (new Date).getTime(); var a = document.createElement("script"); a.setAttribute("language", "javascript"); a.setAttribute("type", "text/javascript"); a.setAttribute("src", ("https:" == document.location.protocol ? "https://a248.e.akamai.net/chartbeat.download.akamai.com/102508/" : "http://static.chartbeat.com/") + "js/chartbeat.js"); document.body.appendChild(a) } var b = window.onload; window.onload = typeof window.onload != "function" ? a : function () { b(); a() } })()
        </script>

    <script type="text/javascript">
         $j('.submit_button').click(function () { OpenTinaLoginWindow(); });
         function OpenTinaLoginWindow(permission) {
             json = { refreshPage: true, loginProvider: 'Facebook', tinaBaseUrl: 'http://auth.news24.com' };
            json.scope = this;

            if (permission)
                json.permission = permission;

            Tina.openLoginWindow(json);
        }
    </script>
</body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.news24.com/elections/news/tau-sa-objects-to-zuma-candidacy-20140401'
        self.crawler.extract(doc, html)

        self.maxDiff = None

        self.assertEqual(doc.title, 'TAU SA objects to Zuma candidacy')
        self.assertEqual(doc.summary, 'Tau SA has lodged an objection against President Jacob Zuma as a candidate in the 7 May general elections, the agriculture union says.')
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '02 04 2014')
        self.assertEqual(doc.author.name, "SAPA")
        self.assertEqual(doc.medium.name, 'News24')

        self.assertEqual(doc.text, u'Johannesburg - Tau SA has lodged an objection against President Jacob Zuma as a candidate in the 7 May general elections, the agriculture union said on Tuesday. \n\nIt sent a letter to Electoral Commission of SA (IEC) chairperson Pansy Tlakula with its objection against Zuma\'s number one position on the list of African National Congress candidates.\n\n"He [Zuma] has been recently implicated in a report of the Public Protector regarding possible irregular expenses on his Nkandla homestead, and the fact that he could have misled Parliament on this issue," Tau SA wrote.\n\n"The full investigation into the so-called weapons scandal [arms inquiry] has not yet been finalised and his name was mentioned in some of the reports on this issue."\n\nThe union said it was of the opinion that an MP had to be free of any suspected involvement in corruption, misappropriation of funds and misleading Parliament.\n\n"For this reason we object to his nomination as a candidate."\n\nThe deadline for objections to National Assembly and provincial legislature candidates nominated by political parties was 17:00 on Tuesday.\n\nIn terms of the Electoral Act, anyone, including the chief electoral officer, may object to the nomination of a candidate.\n\nAn objection can be made on three grounds: If a candidate does not qualify to stand in the election, if the prescribed acceptance of nomination is not signed by the candidate, and if no undertaking signed by the candidate that he/she is bound by the Electoral Code of Conduct is submitted.\n\nThe IEC would consider all objections and inform the objector and the party of its decision by 17:00 on 7 April. It was not clear on Tuesday evening how many objections the IEC had received.\n\nThe Institute for Accountability in Southern Africa has also filed an objection against Zuma\'s nomination. The institute said its objection was lodged ex abundante cautela (from excessive caution) as the ANC was still considering the objection letter and had not yet responded substantively to it.\n\nIn an open letter sent to the IEC the institute includes arguments based on the Public Protector\'s "Secure in Comfort" report on Zuma\'s Nkandla residence. Also contained in the letter is mention of review proceedings, which the Democratic Alliance has pending against the decision to withdraw 783 charges of corruption, fraud, money laundering and racketeering against Zuma.')
        
    def test_extract_article_style_2(self):
        html = """



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://www.facebook.com/2008/fbml">
<head id="Head1"><meta name="description" content="The wife of the man accused of abusing her and their five children and holding them captive has appeared in court, where her case was postponed for a bail application." /><script type='text/javascript'>(function(e){if(typeof e.za24_exk=='undefined')e.za24_exk=new Array;if(typeof e.za24_exkt=='undefined')e.za24_exkt=new Array})(window)
window.za24_exkt.push('weather');window.za24_exk.push('4');
</script><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><meta property="article:published_time" content="2014-06-24 02:04:30 PM"/><meta property="article:modified_time" content="2014-06-24 02:04:30 PM"/><meta property="article:expiration_time" content="2014-06-26 03:20:28 PM"/><meta property="twitter:card" content="summary"/><meta property="twitter:url" content="http://www.news24.com/SouthAfrica/News/House-of-horrors-wife-appears-in-court-20140624"/><meta property="twitter:title" content="&#39;House of horrors&#39; wife appears in court"/><meta property="twitter:site" content="News24"/><meta property="twitter:description" content="The wife of the man accused of abusing her and their five children and holding them captive has appeared in court, where her case was postponed for a bail application."/><meta property="twitter:image" content="http://cdn.24.co.za/files/Cms/General/d/2768/631a355e7d9a42be88089321d2f71502.jpg"/><meta property="twitter:app:name:iphone" content="News24"/><meta property="twitter:app:id:iphone" content="310970460"/><meta property="twitter:app:name:ipad" content="News24"/><meta property="twitter:app:id:ipad" content="310970460"/><meta property="twitter:app:url:iphone" content="https://itunes.apple.com/za/app/news24/id310970460?mt=8"/><meta property="twitter:app:url:ipad" content="https://itunes.apple.com/za/app/news24/id310970460?mt=8"/><meta property="og:site_name" content="News24"/><meta property="fb:app_id" content="2363277980"/><meta property="fb:page_id" content="10227041841"/><meta property="og:title" content="'House of horrors' wife appears in court"/><meta property="og:type" content="article"/><meta property="og:url" content="http://www.news24.com/SouthAfrica/News/House-of-horrors-wife-appears-in-court-20140624"/><meta property="og:image" content="http://cdn.24.co.za/files/Cms/General/d/2667/bf817f060b584c33afb8a4cb430de2a3.jpg"/><meta property="og:description" content="The wife of the man accused of abusing her and their five children and holding them captive has appeared in court, where her case was postponed for a bail application."/><link rel="canonical" href="http://www.news24.com/SouthAfrica/News/House-of-horrors-wife-appears-in-court-20140624"/><script type="text/javascript" language="javascript">
var addthis_share =
{
url: "http://www.news24.com/SouthAfrica/News/House-of-horrors-wife-appears-in-court-20140624",
title: "'House of horrors' wife appears in court",
description: "The wife of the man accused of abusing her and their five children and holding them captive has appeared in court, where her case was postponed for a bail application.",
templates:
{
twitter: "{{title}}: {{url}} via @News24"
},
url_transforms: {
shorten: {
twitter: 'bitly'
}
},
shorteners: {
bitly: {
login: '24com',
apiKey: 'R_ca79efd5a0978fb80d1d853bac1dda83'
}}};
</script>
<title>
	'House of horrors' wife appears in court | News24
</title><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /><meta name="verify-v1" content="7Ni+Om+G5YH4bPtmBOm+5Qih2e8WRykbCvNJXRK9vbg=" /><meta name="bitly-verification" content="267098cc5a65" />   
     <!-- Mobile viewport optimized: j.mp/bplateviewport //-->
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <!-- For non-Retina iPhone, iPod Touch, and Android 2.1+ devices: -->
    <link rel="apple-touch-icon" href="../../images/ios/bookapple-touch-icon.png" />
     <!-- For first- and second-generation iPad: -->
    <link rel="apple-touch-icon" sizes="76x76" href="../../images/ios/bookapple-touch-icon-76x76.png" />
    <!-- For iPhone with high-resolution Retina display running iOS = 7: -->
    <link rel="apple-touch-icon" sizes="120x120" href="../../images/ios/bookapple-touch-icon-120x120.png" />
    <!-- For iPad with high-resolution Retina display running iOS = 7: -->
    <link rel="apple-touch-icon" sizes="152x152" href="../../images/ios/bookapple-touch-icon-152x152.png" /><link rel="SHORTCUT ICON" href="/favicon.ico" />
    <script type='text/javascript'>var _sf_startpt = (new Date()).getTime()</script>
    <link type="text/css" rel="stylesheet" href="http://static.24.co.za/5/styles/complete.css?v=20140620" /><link type="text/css" rel="stylesheet" href="http://scripts.24.co.za/libs/fancybox/jquery.fancybox.css?v=20140620" />
<!--[if gte IE 7]>
<link href="http://www.news24.com/Styles/ie7.css" type="text/css" rel="stylesheet">
<![endif]-->
<!--[if IE 7]><link href='http://www.news24.com/Styles/ie7.css' type='text/css' rel='stylesheet'><![endif]--><script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/minified/basescript1.js?v=20140620" ></script><script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/fancybox/fancybox-1.3.4.min.js?v=20140620" ></script>
    <script type="text/javascript">
        var $j = jQuery.noConflict();var isHomePage = false;document.domain = "news24.com";
    </script>
    
    <script sync type="text/javascript" src="http://scripts.24.co.za/libs/24com/portal/1.0/common.min.js?v=20140620"></script><script type="text/javascript">var _gaq = _gaq || [];_gaq.push(['_setDomainName', 'www.news24.com']);_gaq.push(['_setAccount', 'UA-45055449-1']);_gaq.push(['_trackPageview']);
                                    (function() {var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                                    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                                    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
                                    })();</script>
    
    
    <link id="alternateLink" rel="alternate" media="only screen and (max-width: 640px)" href="http://m.news24.com/news24/SouthAfrica/News/House-of-horrors-wife-appears-in-court-20140624"></link>
    

<meta name="keywords" content="johannesburg, crime, child abuse" />
<meta name="news_keywords" content="johannesburg, crime, child abuse" />
    <meta name="articleid" content="1370d9df-3a3f-4eed-9c29-a3d036173ac4"/>

<link href="http://scripts.24.co.za/libs/24com/comments/3.0.2/styles/comments.css" type="text/css" rel="stylesheet"></link>
<!-- Start of DClick Header -->
<!-- Site: /8900/24.com/Web/News24, Zone: /SouthAfrica/Articles, MapsTo: "News" -->

<script src='//www.googletagservices.com/tag/js/gpt.js' type='text/javascript' ></script>
<script src="http://scripts.24.co.za/libs/24com/Ads/3.0/24AdScript.min.js" language="JavaScript" type="text/javascript"></script>
<script language="JavaScript" type="text/javascript">//<![CDATA[
za24_AdSite = '/8900/24.com/Web/News24'; 
za24_AdZone = '/SouthAfrica/Articles';
za24_IsAsync  = false;
za24_InterstitialEnabled=true;
za24_KeywordType[1]='artid'; za24_Keywords[1]='1370d9df-3a3f-4eed-9c29-a3d036173ac4'; 
za24_KeywordType[2]='places'; za24_Keywords[2]='johannesburg'; 
za24_KeywordType[3]='topics'; za24_Keywords[3]='crime,child abuse'; 

za24_AdSize[1]='1000x1000'; za24_AdPositionNo[1]='1'; 
za24_AdSize[2]='728x90'; za24_AdPositionNo[2]='1'; 
za24_AdSize[3]='300x600'; za24_AdPositionNo[3]='1'; 
za24_AdSize[4]='300x250'; za24_AdPositionNo[4]='1'; 
za24_AdSize[5]='468x120'; za24_AdPositionNo[5]='1'; 
za24_AdSize[6]='10x10'; za24_AdPositionNo[6]='1'; 
za24_AdSize[7]='278x76'; za24_AdPositionNo[7]='1'; 
za24_AdSize[8]='278x35'; za24_AdPositionNo[8]='1'; 
za24_AdSize[9]='200x400'; za24_AdPositionNo[9]='1'; 
za24_AdSize[10]='980x90'; za24_AdPositionNo[10]='1'; 
za24_InitAds();
//--></script>
<!-- End of DClick Header -->
</head>
<body>
    <!-- Start Alexa Certify Javascript -->
<script type="text/javascript">
    _atrk_opts = { atrk_acct: "qhC0h1agYe00yl", domain: "news24.com", dynamic: true };
    (function () { var as = document.createElement('script'); as.type = 'text/javascript'; as.async = true; as.src = "https://d31qbv1cthcecs.cloudfront.net/atrk.js"; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(as, s); })();
</script>
<noscript><img src="https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=qhC0h1agYe00yl" style="display:none" height="1" width="1" alt="" /></noscript>
<!-- End Alexa Certify Javascript -->
    <!-- COPYRIGHT EFFECTIVE MEASURE -->
    <script type="text/javascript">
        (function () {var em = document.createElement('script'); em.type = 'text/javascript'; em.async = true;
            em.src = ('https:' == document.location.protocol ? 'https://za-ssl' : 'http://za-cdn') + '.effectivemeasure.net/em.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(em, s);})();
    </script>
    <noscript><img src="http://za.effectivemeasure.net/em_image" alt="" style="position: absolute; left: -5px;" /></noscript>
    <!--END EFFECTIVE MEASURE CODE -->
    <form name="aspnetForm" method="post" id="aspnetForm">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJMTcxNTY0OTA1ZGQW6vNhyWzSvAx2GSJ/MzQaNC2H9A==" />
</div>


<script type="text/javascript">
//<![CDATA[
var za24_displayAdUrl = 'http://www.news24.com/static/Ads/DisplayAd.html';//]]>
</script>

<div class="aspNetHidden">

	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAAa1BYUt6IflRataqYJyh8AufLgYOaxGNxpcxlKlT9IObQH+ih4MEySCBlfYlvG/lO3w/h12H3MZPLcouy1JL6NJpTNihxCpIUCa2K/Ulzjx5fwGEjiXfG6Ja/hBBVaFQfQh8dMBqWKFZeFkyhEiMsF4/822Sg==" />
</div>
       
        <script type="text/javascript">
jQuery('head').append("<link href='http://scripts.24.co.za/libs/24com/ads/2.0/Style/TransAd.css?v=20140620' type='text/css' rel='stylesheet' ></link>")
</script>
<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/ads/2.0/script/TransAd.min.js?v=20140620"></script>
<script type="text/javascript">AdTemplate = "News24";</script>
<div id='ad-10x10-1' class='24ad10x10'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('10x10','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=10x10&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=10x10&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
        

<div id="leaderboard">
    <div class="adCenter">
        <div style="background-color:transparent;border-bottom:3px solid transparent;border-left:0px solid transparent;border-right:3px solid transparent;">
	        <div id='ad-728x90-1' class='24ad728x90'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('728x90','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=728x90&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=728x90&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
    </div>
    
</div>
        <div class="main_wrap relative">
            

            
    

<script type="text/javascript" language="text/javascript">
    jQuery(function () {
        var pushdown = jQuery("#pushDownAd");
        if (pushdown.height() < 20) { pushdown.css("display", "none") }
    });
</script>


<div class="grid_12">
    <div id="header" class="relative">
        <h1 id="news24HeaderLogo">
            <a href="http://www.news24.com/" title="News24.com Home">News24 News. Breaking News. First</a>
        </h1>
        

<div class="absolute update_time">LAST UPDATED: 2014-06-24, 15:10</div>
        <div class="div_0 absolute"></div>

        <div class="absolute">              
            <div class="header_featured_article">
    <div class="feature_head first absolute">
        <a href="http://voices.news24.com/kamela-mahlakwane/2014/06/gratuity-tipping-wrong-guy/" id="lnkHeaderArtImage" target="_self"><img src="http://cdn.24.co.za/files/Cms/General/d/2636/e4450272be1646549fee65ae3b394aa0.jpg" id="imgHeaderArticle" class="left" height="65" width="65" /></a>
        <h3 class="bold"><a href="http://voices.news24.com/kamela-mahlakwane/2014/06/gratuity-tipping-wrong-guy/" data-track="outbound,home-header,topcompo-Are we tipping the wrong people?" target="_self">Are we tipping the wrong people?</a></h3>
        <p>Should we tip all people who deliver us services? And if so, does that mean we will just pay them extra to do what they are supposed to? asks <strong>Dr Kamela Mahlakwane</strong>.</p>
    </div>
</div>

        </div>
        <div class="div_2 absolute"></div>

        
<div class="search_box absolute">
    <input id="txtSearchField" type="text" class="field absolute" onkeypress="var key=event.keyCode||event.which;if (key==13){submitSiteSearch(); return false;}" />
    <input type="submit" value="Search" class="btn absolute" onclick="submitSiteSearch(false);return false;" />   
</div>
<script type="text/javascript">
    var headerSearchUrl = 'http://www.news24.com/search?q={0}'; var headerAdvancedSearchUrl = 'http://googlesearch.news24.com/search?s=NWS&ref=NWS&q='; var txtSearchFieldClientId = "txtSearchField"; var btnSearchClientId = "btnSearch"; function submitSiteSearch() { var a = $j.trim($j("#" + txtSearchFieldClientId).val()); if (a.length > 0) { window.location.href = "/search?q=" + a } };
</script>
        

<div class="header_weather_box absolute">
    <div class="icon left">
    <a id="lnkModalItem" class="fireEventWeather weatherModal" style="display:none;"></a>
        <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=weather" id="lnkChangeWeather" class="city weatherModal" style="display: block">Cape Town</a>
        <img src="http://static.24.co.za/5/images/icons/forecastslarge/4.png" id="weatherImgMain" alt="Afternoon clouds. Mild." />
    </div>
    <div class="div_3"></div>
    <div class="info left">
        <h2 id="mainTempDisplay">
            Wednesday
            <span>15-18&deg;C</span>
        </h2>
        <p id="mainDesc"><span id="spanMainDescription" style="cursor:default;" title="Afternoon clouds. Mild.">Afternoon clouds. Mild.</span></p>
        <ul id="weather_info_container">
            <li><a class="forecast absolute"  href="javascript:void(0)">7 day forecast</a> <!-- fire script here -->
                <ul id="weather_box_info" >
                    <li >
                        <table cellpadding="0" cellspacing="0" border="0" class="weather_drop_box">
                            
                                    <tr>
                                        <td class="d_day">Thursday</td>
                                        <td class="d_temp">14-16&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/20.png" alt="Heavy rain. Morning clouds. Cool." /></td>
                                        <td class="d_info">Heavy rain. Morning clouds. Cool.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Friday</td>
                                        <td class="d_temp">13-16&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/4.png" alt="Morning clouds. Cool." /></td>
                                        <td class="d_info">Morning clouds. Cool.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Saturday</td>
                                        <td class="d_temp">11-18&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/1.png" alt="Sunny. Mild." /></td>
                                        <td class="d_info">Sunny. Mild.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Sunday</td>
                                        <td class="d_temp">12-18&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/5.png" alt="High level clouds. Mild." /></td>
                                        <td class="d_info">High level clouds. Mild.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Monday</td>
                                        <td class="d_temp">11-16&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/4.png" alt="Morning clouds. Cool." /></td>
                                        <td class="d_info">Morning clouds. Cool.</td>
                                    </tr>
                                
                                    <tr>
                                        <td class="d_day">Tuesday</td>
                                        <td class="d_temp">9-16&deg;c</td>
                                        <td class="d_icon" valign="bottom"><img src="http://static.24.co.za/5/images/icons/forecasts/5.png" alt="High level clouds. Cool." /></td>
                                        <td class="d_info">High level clouds. Cool.</td>
                                    </tr>
                                
                            <tr>
                                <td colspan="4" height="10" valign="bottom" style="vertical-align:bottom">
                                    <div style="height:1px;border-bottom:1px solid #C6C6C6"></div>
                                    <div style="height:1px;border-top:1px solid #fff"></div>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="4" class="d_more_link" valign="top">
                                    <a href="http://weather.news24.com/sa/cape-town">More weather from Weather24 ></a>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="4" class="ad_link">
                                    <div id='ad-278x35-1' class='24ad278x35'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('278x35','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/Africa/Articles&sz=278x35&c=867796154&t=artid%3d288eb505-863d-4e71-8097-eaad289ed0bc%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/Africa/Articles&sz=278x35&c=867796154&t=artid%3d288eb505-863d-4e71-8097-eaad289ed0bc%26posno%3d1' border='0' alt=''></a></noscript>
                                </td>
                            </tr>
                        </table>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
    <div class="div_4"></div>
    <div class="left prodPlacement">        
        <a href="http://pubads.g.doubleclick.net/gampad/clk?id=44943070&iu=/8900/24.com/Web/News24" id="lnkHeaderWeatherSponsor" target="blank">Brought to<br />
        you by:<br />
        <img src="http://cdn.24.co.za/files/Cms/General/d/1655/d7d2b40e358940f09f295f9a9621f1ac.jpg" id="imgHeaderWeatherSponsor" width="66" height="9" border="0" /></a>
    </div>
</div>
<script type='text/javascript'>if(typeof(topStoriesArray)  != 'undefined') topStoriesArray.push({'name':'Cape Town Heavy rain. Morning clouds. Cool. 15-18','url':'http://weather.news24.com','icon':'/images/icons/Forecasts/20.ico'});</script>
        <div id="navBar" class="nav_bar absolute" style="z-index:50;top: 115px !important;">
    <ul id='nav' onmouseover='RemoveSelections();' onmouseout='SetSelections(defaultTabId);'>
<li class='nav_item ' id='tablink0' ><a href="http://www.news24.com/" data-track="outbound,nav,1stlevel-News">News</a>
<ul>
<li ><a  href="http://www.news24.com/SouthAfrica" data-track="outbound,nav,2ndlevel-South Africa">South Africa</a></li><li ><a  href="http://www.news24.com/Elections" data-track="outbound,nav,2ndlevel-Elections">Elections</a></li><li ><a  href="http://www.news24.com/World" data-track="outbound,nav,2ndlevel-World">World</a></li><li ><a  href="http://www.news24.com/Africa" data-track="outbound,nav,2ndlevel-Africa">Africa</a></li><li ><a  href="http://www.channel24.co.za" data-track="outbound,nav,2ndlevel-Entertainment">Entertainment</a></li><li ><a  href="http://www.news24.com/Green" data-track="outbound,nav,2ndlevel-Green">Green</a></li><li ><a  href="http://www.health24.com/news/1.asp" data-track="outbound,nav,2ndlevel-Health">Health</a></li></ul></li>
<li class='nav_item ' id='tablink1' ><a href="http://www.news24.com/Opinions" data-track="outbound,nav,1stlevel-Opinion">Opinion</a>
<ul>
<li><a href="http://voices.news24.com" data-track="outbound,nav,2ndlevel-Voices">Voices</a></li><li><a href="http://www.news24.com/MyNews24" data-track="outbound,nav,2ndlevel-MyNews24">MyNews24</a></li><li><a href="http://www.news24.com/Columnists" data-track="outbound,nav,2ndlevel-Columnists">Columnists</a></li></ul>
</li>
<li class='nav_item ' id='tablink2' ><a href="http://www.fin24.com" data-track="outbound,nav,1stlevel-Business">Business</a>
<ul>
<li ><a  href="http://www.fin24.com" data-track="outbound,nav,2ndlevel-News">News</a></li><li ><a  href="http://www.fin24.com/Markets" data-track="outbound,nav,2ndlevel-Markets">Markets</a></li><li ><a  href="http://www.fin24.com/Money/" data-track="outbound,nav,2ndlevel-Personal Finance">Personal Finance</a></li><li ><a  href="http://www.fin24.com/Opinion/Columnists/" data-track="outbound,nav,2ndlevel-Opinion">Opinion</a></li><li ><a  href="http://www.fin24.com/login" data-track="outbound,nav,2ndlevel-My Profile">My Profile</a></li></ul></li>
<li class='nav_item ' id='tablink3' ><a href="http://www.sport24.co.za" data-track="outbound,nav,1stlevel-Sport">Sport</a>
<ul>
<li ><a  href="http://www.sport24.co.za/" data-track="outbound,nav,2ndlevel-News">News</a></li><li ><a  href="http://www.sport24.co.za/Rugby/" data-track="outbound,nav,2ndlevel-Rugby">Rugby</a></li><li ><a  href="http://www.sport24.co.za/Cricket/" data-track="outbound,nav,2ndlevel-Cricket">Cricket</a></li><li ><a  href="http://www.sport24.co.za/Soccer/" data-track="outbound,nav,2ndlevel-Soccer">Soccer</a></li><li ><a  href="http://www.sport24.co.za/Golf/" data-track="outbound,nav,2ndlevel-Golf">Golf</a></li><li ><a  href="http://www.sport24.co.za/Tennis" data-track="outbound,nav,2ndlevel-Tennis">Tennis</a></li><li ><a  href="http://www.wheels24.co.za/FormulaOne/" data-track="outbound,nav,2ndlevel-Formula1">Formula1</a></li><li ><a  href=" http://www.sport24.co.za/OtherSport" data-track="outbound,nav,2ndlevel-Other Sport">Other Sport</a></li><li class='red'><a class='red' href="http://www.supersport.com/" data-track="outbound,nav,2ndlevel-SuperSport">SuperSport</a></li><li class='red'><a class='red' href="http://www.supersport.com/live-video" data-track="outbound,nav,2ndlevel-Live Streaming">Live Streaming</a></li><li class='red'><a class='red' href="http://www.supersport.com/video" data-track="outbound,nav,2ndlevel-Video Highlights">Video Highlights</a></li></ul></li>
<li class='nav_item no_arrow' id='tablink4' ><a href="http://www.fin24.com/Tech/" data-track="outbound,nav,1stlevel-Tech">Tech</a>
<li class='nav_item ' id='tablink5' ><a href="http://www.wheels24.co.za" data-track="outbound,nav,1stlevel-Motoring">Motoring</a>
<ul>
<li ><a  href="http://www.wheels24.co.za/news" data-track="outbound,nav,2ndlevel-News">News</a></li><li ><a  href="http://www.wheels24.co.za/NewModels/" data-track="outbound,nav,2ndlevel-New Models">New Models</a></li><li ><a  href="http://www.wheels24.co.za/4x4/" data-track="outbound,nav,2ndlevel-4x4">4x4</a></li><li ><a  href="http://www.wheels24.co.za/FormulaOne/" data-track="outbound,nav,2ndlevel-Formula One">Formula One</a></li><li ><a  href="http://www.wheels24.co.za/Motorsport/" data-track="outbound,nav,2ndlevel-Motorsport">Motorsport</a></li><li ><a  href="http://www.wheels24.co.za/BikesQuads/" data-track="outbound,nav,2ndlevel-Bikes">Bikes</a></li><li ><a  href="http://www.wheels24.co.za/Your-Wheels/" data-track="outbound,nav,2ndlevel-Your Wheels">Your Wheels</a></li></ul></li>
<li class='nav_item ' id='tablink6' ><a href="http://www.news24.com/Lifestyle" data-track="outbound,nav,1stlevel-Lifestyle">Lifestyle</a>
<ul>
<li ><a  href="http://www.health24.com/" data-track="outbound,nav,2ndlevel-Health">Health</a></li><li ><a  href="http://www.women24.com" data-track="outbound,nav,2ndlevel-Women">Women</a></li><li ><a  href="http://www.wheels24.co.za" data-track="outbound,nav,2ndlevel-Motoring">Motoring</a></li><li ><a  href="http://www.food24.com" data-track="outbound,nav,2ndlevel-Food">Food</a></li><li ><a  href="http://www.news24.com/Travel" data-track="outbound,nav,2ndlevel-Travel">Travel</a></li><li ><a  href="http://www.channel24.co.za/" data-track="outbound,nav,2ndlevel-Entertainment">Entertainment</a></li><li class='red'><a class='red' href="http://www.women24.com/rubybox" data-track="outbound,nav,2ndlevel-Shop Beauty">Shop Beauty</a></li><li ><a  href="http://www.parent24.com" data-track="outbound,nav,2ndlevel-Parent">Parent</a></li><li ><a  href="http://www.lazygamer.net" data-track="outbound,nav,2ndlevel-Games">Games</a></li><li class='red'><a class='red' href="http://www.mweb.co.za/games/Home.aspx?ref=news24nav" data-track="outbound,nav,2ndlevel-GameZone">GameZone</a></li><li class='red'><a class='red' href="http://love2meet.news24.com/s/" data-track="outbound,nav,2ndlevel-Dating">Dating</a></li></ul></li>
<li class='nav_item ' id='tablink7' ><a href="http://www.news24.com/Multimedia" data-track="outbound,nav,1stlevel-Multimedia">Multimedia</a>
<ul>
<li><a href="http://www.news24.com/multimedia" data-track="outbound,nav,2ndlevel-News">News</a></li><li><a href="http://www.sport24.co.za/multimedia" data-track="outbound,nav,2ndlevel-Sport">Sport</a></li><li><a href="http://www.channel24.co.za/Multimedia" data-track="outbound,nav,2ndlevel-Entertainment">Entertainment</a></li><li><a href="http://www.wheels24.co.za/multimedia" data-track="outbound,nav,2ndlevel-Motoring">Motoring</a></li><li><a href="http://www.women24.com/multimedia" data-track="outbound,nav,2ndlevel-Women">Women</a></li><li><a href="http://www.food24.com/multimedia" data-track="outbound,nav,2ndlevel-Food">Food</a></li><li><a href="http://www.parent24.com/multimedia" data-track="outbound,nav,2ndlevel-Parenting">Parenting</a></li><li><a href="http://www.news24.com/travel/multimedia" data-track="outbound,nav,2ndlevel-Travel">Travel</a></li><li><a href="http://www.health24.com/multimedia" data-track="outbound,nav,2ndlevel-Health">Health</a></li><li><a href="http://www.news24.com/live" data-track="outbound,nav,2ndlevel-Video">Video</a></li></ul>
</li>
<li class='nav_item ' id='tablink8' ><a href="http://www.news24.com/SpecialReports" data-track="outbound,nav,1stlevel-Focus">Focus</a>
<ul>
<li><a href="http://www.news24.com/obituaries" data-track="outbound,nav,2ndlevel-Obituaries">Obituaries</a></li><li><a href="http://www.news24.com/Content/Africa/Zimbabwe" data-track="outbound,nav,2ndlevel-Zimbabwe">Zimbabwe</a></li><li><a href="http://www.health24.com/Medical/HIV-AIDS" data-track="outbound,nav,2ndlevel-Aids Focus">Aids Focus</a></li><li><a href="http://www.m24i.co.za/" data-track="outbound,nav,2ndlevel-Media24 Investigations">Media24 Investigations</a></li><li><a href="http://www.news24.com/Tags/Topics/good_news" data-track="outbound,nav,2ndlevel-Good News ">Good News </a></li><li><a href="http://www.citypress.co.za/" data-track="outbound,nav,2ndlevel-City Press">City Press</a></li><li><a href="http://www.news24.com/competitions" data-track="outbound,nav,2ndlevel-Competitions">Competitions</a></li></ul>
</li>
<li class='nav_item ' id='tablink9' ><a href="http://isizulu.news24.com" data-track="outbound,nav,1stlevel-isiZulu">isiZulu</a>
<ul>
<li><a href="http://isizulu.news24.com/NingizimuAfrika" data-track="outbound,nav,2ndlevel-Ningizimu Afrika ">Ningizimu Afrika </a></li><li><a href="http://isizulu.news24.com/Izindaba-Zami" data-track="outbound,nav,2ndlevel-Izindaba-Zami">Izindaba-Zami</a></li><li><a href="http://isizulu.news24.com/Ezemidlalo" data-track="outbound,nav,2ndlevel-Ezemidlalo">Ezemidlalo</a></li><li><a href="http://isizulu.news24.com/Afrika" data-track="outbound,nav,2ndlevel-Afrika">Afrika</a></li><li><a href="http://isizulu.news24.com/Umhlaba" data-track="outbound,nav,2ndlevel-Umhlaba">Umhlaba</a></li><li><a href="http://isizulu.news24.com/Ezokuzijabulisa" data-track="outbound,nav,2ndlevel-Ezokuzijabulisa">Ezokuzijabulisa</a></li><li><a href="http://isizulu.news24.com/Ezamabhizinisi" data-track="outbound,nav,2ndlevel-Ezamabhizinisi">Ezamabhizinisi</a></li></ul>
</li>
<li class='nav_item no_arrow' id='tablink10' ><a href="http://www.news24.com/Jobs/" data-track="outbound,nav,1stlevel-Jobs">Jobs</a>
<li class='nav_item no_arrow' id='tablink11' ><a href="http://www.news24.com/Property/" data-track="outbound,nav,1stlevel-Property">Property</a>
</ul>
<ul id='nav' onmouseover='RemoveSelections();' onmouseout='SetSelections(defaultTabId);'>
<li id='liContainer' class='sponsor_img'><a id='lnkSpecialNav' href='http://pubads.g.doubleclick.net/gampad/clk?id=51989710&iu=/8900/24.com/Web/News24' target='_self'><img id='lnkImg' src='http://cdn.24.co.za/files/Cms/General/d/2440/3f222735f4a746ab83d2b4d0b5955f73.gif' /></a>
<ul class='sponsor'>
<li class='sponsor-list-item'><a href='http://pubads.g.doubleclick.net/gampad/clk?id=57613510&iu=/8900/24.com/Web/News24' target='_self' data-track="outbound,nav,2ndlevel-Car Insurance">Car Insurance</a>
<li class='sponsor-list-item'><a href='http://pubads.g.doubleclick.net/gampad/clk?id=57613750&iu=/8900/24.com/Web/News24' target='_self' data-track="outbound,nav,2ndlevel-Home Insurance">Home Insurance</a>
<li class='sponsor-list-item'><a href='http://pubads.g.doubleclick.net/gampad/clk?id=57613990&iu=/8900/24.com/Web/News24' target='_self' data-track="outbound,nav,2ndlevel-Building Insurance">Building Insurance</a>
</ul>
</li>
</ul>

</div>
<script type='text/javascript'>menuJsonArray = [{"Url":"http://www.news24.com/SouthAfrica","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/Elections","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/World","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/Africa","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/Green","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://www.news24.com/","TabLinkIndex":0,"TabLinkToActivate":"tablink0"},{"Url":"http://voices.news24.com","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/mynews24","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/columnists","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/Opinions","TabLinkIndex":1,"TabLinkToActivate":"tablink1"},{"Url":"http://www.news24.com/Travel","TabLinkIndex":6,"TabLinkToActivate":"tablink6"},{"Url":"http://love2meet.news24.com/s/","TabLinkIndex":6,"TabLinkToActivate":"tablink6"},{"Url":"http://www.news24.com/Lifestyle","TabLinkIndex":6,"TabLinkToActivate":"tablink6"},{"Url":"http://www.news24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.sport24.co.za/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.channel24.co.za/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.wheels24.co.za/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.women24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.food24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.parent24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/travel/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.health24.com/multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/live","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/Multimedia","TabLinkIndex":7,"TabLinkToActivate":"tablink7"},{"Url":"http://www.news24.com/obituaries","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/africa/zimbabwe","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.health24.com/medical/hiv-aids","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.m24i.co.za/","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/tags/topics/good_news","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.citypress.co.za/","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/competitions","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://www.news24.com/SpecialReports","TabLinkIndex":8,"TabLinkToActivate":"tablink8"},{"Url":"http://isizulu.news24.com/ningizimuafrika","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/izindaba-zami","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/ezemidlalo","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/afrika","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/umhlaba","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/ezokuzijabulisa","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com/ezamabhizinisi","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://isizulu.news24.com","TabLinkIndex":9,"TabLinkToActivate":"tablink9"},{"Url":"http://www.news24.com/Jobs/","TabLinkIndex":10,"TabLinkToActivate":"tablink10"},{"Url":"http://www.news24.com/Property/","TabLinkIndex":11,"TabLinkToActivate":"tablink11"}];</script>

<script type="text/javascript" language="javascript">
    if ('False' == 'True')
        document.getElementById('main_nav').style.height = '33px';
</script>
    </div>
</div>
<div class="clear"></div>
<div id="pushDownAd">
    <div class="clear"></div>
    <div id='ad-980x90-1' class='24ad980x90'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('980x90','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=980x90&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=980x90&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>        
    <div class="clear"></div>
</div>
    <div class="container_12">
        <div class="clr10">&nbsp;</div>
        <div class="content_wrap socialnewsbasefix">
            <div class="left col640">
                
                
    <div id="article_special">
        

<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/article/1.0/articleGreyLinks.js"></script>
<script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/jquery.hoverintent.min.js?v=20140620" ></script>
<script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/jquery.cluetip.min.js?v=20140620" ></script>

<div class="article col626">
    
    <div class="spacer clr"></div>
	<h1 class="bold">'House of horrors' wife appears in court</h1>
	<span id="spnDate" class="block datestamp">2014-06-24 14:04</span>
	<div class="col300 right">
	    
	    <div class="spacer clr"></div>
        
        <div id="fb-root"></div>
<script type="text/javascript">
 (function (d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
 js.src = "//connect.facebook.net/en_GB/all.js#xfbml=1&appId=2363277980";
fjs.parentNode.insertBefore(js, fjs);
} (document, 'script', 'facebook-jssdk'));
</script>
<script type="text/javascript">
window.fbAsyncInit = function () {FB.Event.subscribe('edge.create', function (response) {
GA24.trackEvent('articles,sharelinks,fblike');
});};
var pinteresturl = '//assets.pinterest.com/js/pinit.js'
var twitterurl = '//platform.twitter.com/widgets.js'
var addthisurl ='//s7.addthis.com/js/250/addthis_widget.js#username=zamedia24'
$j.ajaxSetup({cache: true});
$j.getScript(pinteresturl)
$j.getScript(twitterurl)
$j.getScript(addthisurl,function(){
if(typeof(addthis) != 'undefined'){
$j('#article_toolbox_topright').show();
addthis.addEventListener('addthis.menu.share', function(evt) {
GA24.trackEvent('articles,sharelinks,' + evt.data.service);
});
}
});
$j.ajaxSetup({cache: false});
var addthis_config ={username: 'zamedia24',services_exclude: 'email,print',ui_open_windows: true,ui_language: 'en' };function googlePlusOneShareLink() {GA24.trackEvent('articles,sharelinks,googleplusone');
}function OpenPrintWindowShare() {var printUrl = '/printArticle.aspx?iframe&aid=1370d9df-3a3f-4eed-9c29-a3d036173ac4&cid=1059';window.open(printUrl,'myPrintWindow','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=750,height=600');}</script><div class="spacer clr"></div>
<div id="article_toolbox_topright" style="border-bottom:solid #ebebeb 0px; border-top:solid #ffffff 1px; padding-left:0px;display:none;">
<div class="addthis_toolbox">
<a class="addthis_button_facebook_like" fb:like:action="recommend" fb:like:show_faces="false" fb:like:layout="button_count" fb:like:send="false"></a>
<a class="addthis_button_google_plusone" g:plusone:size="medium"></a>
<span><a href="http://pinterest.com/pin/create/button/?url=http://www.news24.com/SouthAfrica/News/House-of-horrors-wife-appears-in-court-20140624" class="pin-it-button" count-layout="horizontal">Pin It</a></span>
</div>
<div class="addthis_toolbox">
<a class="addthis_button_twitter"><span></span></a>
<a class="addthis_button_facebook"><span></span></a>
<a class="addthis_button at300b"><span></span></a>
<a class="email group" href="http://www.news24.com/sendToFriend.aspx?iframe&aid=1370d9df-3a3f-4eed-9c29-a3d036173ac4&cid=1059" title="Email"><span></span></a>
<a class="print" onclick="OpenPrintWindowShare()" title="Print"><span></span></a>
</div>
</div>
<div id="marging10Bottom"></div>

        <div class="spacer clr"></div>
	    

<script language="javascript" type="text/javascript">
    function popUP(url) {
        newwindow = window.open(url, 'name', 'height=800,width=500,scrollbars=yes,left=400');
        if (window.focus) { newwindow.focus() }
        return false;
    }
</script>

<div id="article_feature">
	<img id="image" title="" src="http://cdn.24.co.za/files/Cms/General/d/2667/bf817f060b584c33afb8a4cb430de2a3.jpg" />
	<p class="text"> (<a href='http://www.shutterstock.com' target='_blank'>Shutterstock</a>)</p>
	<p class="bold">
	    <a id="lnkGalleries" href="http://www.news24.com/Multimedia">Multimedia</a>  &nbsp; · &nbsp; <a id="lnkUserGalleries" href="http://www.news24.com/Multimedia/MyNews24">User Galleries</a> &nbsp; · &nbsp; <a id="lnkNewsGalleries" href="http://www.news24.com/Multimedia/Category-Images">News in Pictures</a>
	    <span class="block red"><a class="group" href="http://uploads.news24.com?iframe">Send us your pictures</a>  &nbsp;·&nbsp; <a class="group" href="http://www.news24.com/FeedBack.aspx?iframe">Send us your stories</a></span>
	</p> 
</div>

	    <div class="spacer clr"></div>
        
        <div class="spacer clr"></div>	
	    

<script type="text/javascript">
    function scrollalert() { var a = $j("#scrollbox"); var b = $j("#scrollbox > #content"); if (a.length > 0) { if (a.length > 0 && a.scrollTop && b.height() <= a.scrollTop() + a.height() + 20) { $j("#imgAjaxLoad").show(); var data = { 'tag': $j("#hfTag").val(), 'tagGroup': $j("#hfTagGroup").val(), 'CurrentSiteId': "5", 'CmsArticleId': "1370d9df-3a3f-4eed-9c29-a3d036173ac4", 'index': $j("#hfBottomIndex").val(), 'selectedArticleIndex': $j("#hfSelectedArticleIndex").val(), 'directionToFetch': "Down" }; news24.getAjax("/Ajax/ArticleData/", "BuildArticleListByTag", data, onSuccessBottom, onFail) } setTimeout("scrollalert();", 500) } } function onSuccessBottom(a) { var b = parseInt($j("#hfBottomIndex").val()); if (a != "" && a != null) { $j("#hfBottomIndex").val(b + 5); setTimeout("$j('#imgAjaxLoad').hide();", 1e3); var c = $j("#RelatedLinks").html() + a; $j("#RelatedLinks").html(c) } else { setTimeout("$j('#imgAjaxLoad').hide();", 1e3); $j("#hfBottomIndex").val(-1) } } function onSuccessTop(a) { var b = parseInt($j("#hfTopIndex").val()); if (a != "" && a != null) { $j("#hfTopIndex").val(b - 5); setTimeout("$j('#imgAjaxLoad').hide();", 1e3); var c = a + $j("#RelatedLinks").html(); $j("#RelatedLinks").html(c); $j("#scrollbox").scrollTo("10") } else { setTimeout("$j('#imgAjaxLoad').hide();", 1e3); $j("#hfTopIndex").val(-1) } } function onFail() { } $j("document").ready(function () { scrollalert(); $j("#imgAjaxLoad").hide() })
</script>

<div id="relatedlinks_box">
    <div class="left"><h5 id="Relatedheader" class="bold">Related Links</h5><a id="taglink" class="relatedTag"></a></div>
    <div class="right"></div>
    <div class="clr"></div>
    
    
            <ul>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-\&#39;House of horrors\&#39; wife due in court" href="http://www.news24.com/SouthAfrica/News/House-of-horrors-wife-due-in-court-20140624">'House of horrors' wife due in court</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-\&#39;House of horror\&#39; mother arrested - report" href="http://www.news24.com/SouthAfrica/News/House-of-horror-mother-arrested-20140623">'House of horror' mother arrested - report</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-\&#39;House of horrors\&#39; may become safe house" href="http://www.news24.com/SouthAfrica/News/House-of-horrors-may-become-safe-house-20140613">'House of horrors' may become safe house</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-Springs ‘Monster’ dad case postponed" href="http://www.news24.com/SouthAfrica/News/Springs-Monster-dad-case-postponed-20140612">Springs ‘Monster’ dad case postponed</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-\&#39;House of horrors\&#39; dad back in court" href="http://www.news24.com/SouthAfrica/News/House-of-horrors-dad-back-in-court-20140612">'House of horrors' dad back in court</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-\&#39;House of horrors\&#39; dad admits punching boy" href="http://www.news24.com/SouthAfrica/News/House-of-horrors-dad-admits-punching-boy-20140531">'House of horrors' dad admits punching boy</a></li>
        
            <li class="bold"><a data-track="outbound,articles,relatedlinks-Neighbours tell of \&#39;house of horrors\&#39; boy\&#39;s pleas" href="http://www.news24.com/SouthAfrica/News/Neighbours-tell-of-house-of-horrors-boys-pleas-20140529">Neighbours tell of 'house of horrors' boy's pleas</a></li>
        
            </ul>
        
    
   
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfTopIndex" id="hfTopIndex" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfBottomIndex" id="hfBottomIndex" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfTag" id="hfTag" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfTagGroup" id="hfTagGroup" />
    <input type="hidden" name="ctl00$ctl00$MainBodyPlaceholder$Column1Placeholder$articlePaged$articleRelatedlinks$hfSelectedArticleIndex" id="hfSelectedArticleIndex" />
</div>
	    

<div class=" rowdivider clr"></div>
<div class="kalahari_product left">
    <div id="pnlKalahariListing">
	
        
                <div>
                    <h4 class="left"><a href="http://etrader.kalahari.net/referral.asp?linkid=1869&partnerid=9113" target="_blank">kalahari.com</a></h4>
                    <ul class="left">
                        <li>
                            <a href="http://etrader.kalahari.net/referral.asp?linkid=5&amp;partnerid=9113&amp;sku=35274963" target="_blank">A Hedonist's Guide To... Johannesburg</a><br />
                            Explore the vibrant restaurants, bars and cultural life of Johannesburg before heading off for...
                            
                            Now R251.00
                            <br />
                            <a class="buynow" href="http://etrader.kalahari.net/referral.asp?linkid=5&amp;partnerid=9113&amp;sku=35274963" target="_blank">buy now</a>
                        </li>
                    </ul>
                </div>
            
    
</div>
    
</div>
<div class=" rowdivider clr"></div>
	    
        
	</div>
	<div class="ByLineWidth">
		
	</div>
	<article id="article-body" class="clr_left"><p>Johannesburg - The wife of the man accused of abusing her
and their five children and holding them captive appeared in the Springs
Magistrate's Court on Tuesday, <a href="http://www.beeld.com/nuus/2014-06-24-monster-se-vrou-bly-in-aanhouding">Beeld</a> reported.</p><p>The matter was postponed to 1 July for a formal bail
application, according to the report.</p><p>She was arrested for defeating the ends of justice on Monday
when she decided not to co-operate with police and reportedly refused to
testify against her husband.</p><p>Magistrate Roy le Roux told the woman she was the second
accused in the case.</p><p>In addition to defeating the ends of justice she faces the
same charges as her husband - attempted murder, child abuse, and assault.</p><p>The woman's 36-year-old husband, who cannot be named to
protect the identity of his family members, was arrested last month after
allegedly assaulting his wife and five children and keeping them captive.</p><p>He was denied bail by the court earlier this month. His case
was postponed to 25 July.</p><p>The man was arrested in May after his badly beaten
11-year-old son fled the family's house in Springs and ran to a neighbour to
beg for help. The neighbour called police.</p><p>The man allegedly kept his wife and five children, aged
between two and 16, captive in the house for several years and assaulted them.</p></article>
    
	<div id="_htmlAccreditationName">- SAPA</div>
	
	<p></p>
	


<div id="divKeywordsListing" class="read_more_slider">
    
            <b style="color:Gray">Read more on: &nbsp;&nbsp;</b>
        
            <b><a style="color:#0E2E5E;" href="/Tags/Places/johannesburg">johannesburg</a></b>                     
        &nbsp;|&nbsp;
            <b><a style="color:#0E2E5E;" href="/Tags/Topics/crime">crime</a></b>                     
        &nbsp;|&nbsp;
            <b><a style="color:#0E2E5E;" href="/Tags/Topics/child_abuse">child abuse</a></b>                     
        
</div>
    

<script type="text/javascript">
    function ReadMoreAction() { if ($j("div.read_more_slider").is(":inView") && !hidden) { $j("div#readMoreSlider").animate({ right: 0 }, 400); sliderVisible = true; isLoaded++; if (isLoaded == 1) { GA24.trackEvent("SouthAfrica-next-articlebox, show") } } } function HideReadMoreAction() { $j("div#readMoreSlider").animate({ right: -3e3 }, 400); sliderVisible = false } function CloseAction() { HideReadMoreAction(); hidden = true } var isLoaded = 0; var sliderVisible = false; var hidden = false; $j.extend($j.expr[":"], { inView: function (e) { return $j(e).offset().top + $j(e).height() <= $j(window).scrollTop() + $j(window).height() } }); $j(function () { setInterval("ReadMoreAction();", 500) }); $j(function () { var e = $j(window).scrollTop(); var t = e + $j(window).height(); var n = $j("div.read_more_slider").offset().top; var r = n + $j("div.read_more_slider").height(); return r <= t })
</script>
<div id="readMoreSlider">
    <div class="slider_title"><span>NEXT ON NEWS24</span><span class="right" style="cursor:pointer;" onclick="CloseAction()">X</span></div>
    <div class="slider_content">
        <a href='http://www.news24.com/SouthAfrica/News/Cops-still-probing-deaths-of-8-illegal-miners-20140624' data-track="outbound,nextarticlebox"><img src="http://cdn.24.co.za/files/Cms/General/d/2779/dee09c9f1bbe4dfbac4bd4f022dc48fa.jpg" id="imgArticle" class="left" height="65" width="65" /></a>
	    <h4 class="bold"><a href='http://www.news24.com/SouthAfrica/News/Cops-still-probing-deaths-of-8-illegal-miners-20140624' data-track="outbound,nextarticlebox" style="color:#fff;">Cops still probing deaths of 8 illegal miners</a></h4>
	    <div class="wrap_stampcomment" style="margin-top:10px;">
            <span class="block datestamp left" style="font-size:12px;color:#fff;">2014-06-24 13:32</span>
        </div>
    </div>
</div>
	<p></p>
    
</div>
<script type="text/javascript">
    $j(document).ready(function () { var a = $j("a.tips"); a.each(function () { var a = $j(this); a.attr("rel", "/Handlers/WhosWhoTooltip.ashx?url=" + a.attr("rel")) }); a.cluetip({ positionBy: "fixed", topOffset: "-230", leftOffset: "-30", sticky: true, dropShadow: false, showTitle: false, mouseOutClose: true, closeText: "", cluezIndex: 5100 }) })
</script>
        <div class="spacer clr">
            </div>
        

<script type="text/javascript" language="javascript">
	function openPrintWindow() {
		myPrintWindow = window.open('http://www.news24.com/printArticle.aspx?iframe&aid=1370d9df-3a3f-4eed-9c29-a3d036173ac4&cid=1059','myPrintWindow','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=750,height=600');
	}
</script>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#username=zamedia24"></script>
<div id="article_toolbox_bot" class="col626 left">
	<ul>
		<li class="email left" /><a class="group" href="http://www.news24.com/sendToFriend.aspx?iframe&aid=1370d9df-3a3f-4eed-9c29-a3d036173ac4&cid=1059">Email article</a>
		<li class="print left" /><a onclick="openPrintWindow()" href="#">Print article</a>
		<li class="get left" />GET NEWS24 ON: 
		<li class="mobile left" /><a href="http://mobile.24.com/?p=minisite_news">Your mobile</a>
		<li class="facebook left"/><a href="http://www.facebook.com/apps/application.php?api_key=90f449e533cd94a11213682bc9b2a23c">Your Facebook profile</a>
		<li class="clr" />
		<li class="share left" />SHARE:
		
	</ul>
	
	<div class="addthis_toolbox addthis_default_style">
	  <a class="addthis_button_facebook">Facebook</a>
	  <a class="addthis_button_twitter">Twitter</a>
	  <a class="addthis_button_google">Google</a>
	  <a class="addthis_button_digg">Digg</a>
	  <a class="addthis_button_delicious">Delicious</a>
	  <a class="addthis_button_yahoobkm">Yahoo</a>
	  <a class="addthis_button_compact" >More...</a>
	</div>
</div>
        <div class="spacer clr">
            </div>
        <div class="col620 adfix">
            <div id='ad-468x120-1' class='24ad468x120'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('468x120','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=468x120&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=468x120&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
        <div class="spacer clr">
            </div>
        <div class="col626">
            

<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/comments/3.0.2/scripts/comments.min.js"></script>
<script type="text/javascript" src="http://scripts.24.co.za/libs/json/json2.js"></script>
<script type="text/javascript">
    jQuery(function () {
        if (typeof onLogin !== "function") {
            jQuery.getScript("http://scripts.24.co.za/libs/24com/tina/1.0/LoginWindow.js");
        }
    });

    $j(function() {
        if (typeof commentControl !== "undefined") {
            // settings
            commentControl.sortOrder = "Asc";
            commentControl.pageSize = 20;
            commentControl.tinaBaseUrl = "http://auth.news24.com";
            commentControl.commentStatus = "Unmoderated";
            commentControl.lang = false ? "af" : "en";
            commentControl.locale = "en-za";
            commentControl.site = "News24";
            commentControl.breadCrumb = "News24|SouthAfrica|News" ;
            commentControl.objectId = "1370d9df-3a3f-4eed-9c29-a3d036173ac4";
            commentControl.isDev = false ;
            commentControl.canShowPostedComment = true ;
            commentControl.logOutUrl = "http://auth.news24.com/DeAuthenticate.aspx?surl=http://www.news24.com/SouthAfrica/News/House-of-horrors-wife-appears-in-court-20140624";
            commentControl.auth.user.id = "00000000-0000-0000-0000-000000000000";
            commentControl.auth.user.displayName = "";
            commentControl.auth.user.clickThrough = "";
            commentControl.auth.user.avatarUrl = "http://cdn.24.co.za/Files/RAP2/d/DefaultAvatar/Small.png";
            commentControl.auth.user.openIdType = 0 ;
            commentControl.FacebookHandlerUrl = "http://www.news24.com/FacebookToken.ashx";
            commentControl.cacheFacebookAvatar = true;
            commentControl.policyLink = "http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109";
            if (commentControl.auth.util.isFacebookProfile("")) {
                commentControl.auth.user.facebookProfileId = commentControl.auth.util.getFbProfileIdFromAvatarUrl("");
            }
            commentControl.init();
        }
    });
  
</script>
<p style="margin-bottom: 10px; margin-top: 5px;">
<a href="http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109">Read News24’s Comments Policy</a>
</p>



<div class="facebookComments">
    <p>24.com publishes all comments posted on articles provided that they adhere to our <a href="http://www.news24.com/MyNews24/YourStory/News24s-Comments-Policy-20101109" target="_blank" style="color:white;cursor:pointer;">Comments Policy</a>. Should you wish to report a comment for editorial review, please do so by clicking the 'Report Comment' button to the right of each comment.</p>
</div>
    <div id="comments_wrap">
        <div id="comment_on_story">
            <div class="fl">
                Comment on this story
            </div>
            <div class="xsmall normal to_lower fl" id="comment_count_wrap">
                <span id="lblTotalCommentCount">10</span>&nbsp;<span id="lblTotalCommentCountText">comments</span>
            </div>
            <div class="clr"></div>
        </div>

        
            <div class="comment_form_wrap" id="comment_article_form">
                <div class="comment_form_header to_upper bold">Add your comment</div>
                <div class="comment_form_result_msg bold hidden">Thank you, your comment has been submitted.</div>
                <div class="comment_form_user">
                    <div class="avatar_wrap fl">
                        <div><img alt="avatar" class="user_avatar_img" /></div>
                    </div>
                    <div class="author_name fl">
                        <a href="#" target="_blank" class="author_link bold user_name"></a>
                    </div>
                    <div class="logout_wrap fr">
                        <a href="#" class="smlr logout_link">Logout</a>
                    </div>
                    <div class="clr"></div>
                </div>
                <div class="comment_form_inner">
                    <span class="comment_form_label bold">Comment</span>
                    <span class="comment_form_remaining_text xsmall italic"><span>0</span> characters remaining</span>
                    <div class="textarea_wrap"><textarea rows="4"></textarea></div>
                    <div id="divFacebookCheckbox" class="facebook_checkbox">
                        <input type="checkbox" id="chk_facebook" checked="checked" /> <label for="chk_facebook" class="smlr">Share on Facebook</label>
                    </div>
                    <input type="button" value="Post Comment" class="button_submit to_upper smlr" />
                    <div class="ajax-loader hidden"></div>
                </div>
            </div>
        
        
        <div id="comments_list"></div>
        
        <div id="comment_reusables" class="hidden">
            <div class="comment_form_wrap" id="comment_reply_form">
                <div class="comment_form_header to_upper bold"></div>
                <div class="comment_form_user">
                    <div class="avatar_wrap fl">
                        <div><img alt="avatar" class="user_avatar_img" /></div>
                    </div>
                    <div class="author_name fl">
                        <a href="#" target="_blank" class="author_link bold user_name"></a>
                    </div>
                    <div class="logout_wrap fr">
                        <a href="#" class="smlr logout_link">Logout</a>
                    </div>
                    <div class="clr"></div>
                </div>
                <div class="comment_form_inner">
                    <span class="comment_form_label bold">Comment</span>
                    <span class="comment_form_remaining_text xsmall italic"><span>0</span> characters remaining</span>
                    <div class="textarea_wrap"><textarea rows="4"></textarea></div>
                    <div id="divFacebookCheckboxReply" class="facebook_checkbox">
                        <input type="checkbox" id="chk_facebook_reply" checked="checked" /> <label for="chk_facebook_reply" class="smlr">Share on Facebook</label>
                    </div>
                    <input type="button" value="Post Comment" class="button_submit to_upper smlr" />
                    <div class="ajax-loader hidden"></div>
                </div>
            </div>
        </div>

        <div id="comment_loader" class="hidden">
            <img src="http://scripts.24.co.za/libs/24com/comments/2.7/images/ajax-loader.gif" alt="Loading comments..." /> Loading comments...
        </div>

        <input type="button" id="btn_load_more" class="hidden to_upper smlr" value="Load More Comments" />
    </div>

        </div>
        <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/24com/contentrecommendation/2.0/keywordlogger.min.js?v=20140620" ></script>
<div id="other_stories" class="col626 left">
    <div id="googleAdContainer" style="float: left">
        <script type="text/javascript">
            google_ad_client = "pub-0710600889784454"; google_ad_slot = "5629899714"; google_ad_width = 336; google_ad_height = 280; $j(document).ready(function () { var data = { 'categoryBreadcrumb': 'SouthAfrica/News', 'articleId': '1370d9df-3a3f-4eed-9c29-a3d036173ac4' }; news24.getAjax("/Ajax/ArticleData/", "GetRecommendedArticles", data, function (res) { GetRecommendedArticlesCallback(res) }) }); function GetRecommendedArticlesCallback(res) { if (!res.error && res != "error") $j('#contentDiv').html(res); else $j('#contentDiv').remove() }
        </script>
        <script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
    </div>
    <div id="contentDiv" class="right" style="width:277px;padding-bottom:10px;"></div>
    <div class="clr"></div>
</div>
        <div class="spacer clr">
            </div>
        <div class="spacer clr">
            </div>
        
<iframe src="http://b.wm.co.za/24com.php?location=N&layout=wide" id="ifrWide" frameborder="0" width="630" height="152" scrolling="no" style="margin-left:-8px"></iframe>
<div class="clr10">&nbsp;</div>
        <div class="spacer clr">
            </div>
        <div id="divToHide">
    <div id="inside_news" class="col626 left">
    <h2 class="bold">Inside News24</h2>
	    <div id="wrap_carousel" class="relative block">
	      
		      <ul id="carousel" class="absolute">
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.channel24.co.za/Music/News/Robin-Thickes-new-music-video-is-uncomfortably-awesome-20140624" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2796/f3974fafb47f4c86a026efacb37b236f.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.channel24.co.za/Music/News/Robin-Thickes-new-music-video-is-uncomfortably-awesome-20140624" data-track="outbound,home,inside-This is really awkward!" target="_self">This is really awkward!</a></h4>
                    <p>Robin Thicke's soppy new video!</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.sport24.co.za/Soccer/WorldCup/" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2797/faf08856691a443980224159f2fb9215.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.sport24.co.za/Soccer/WorldCup/" data-track="outbound,home,inside-All the news from the SWC" target="_self">All the news from the SWC</a></h4>
                    <p>Stay up-to-date with Sport24's special Brazil 2014 section.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.health24.com/Medical/Hypertension/Effects-on-the-body/Gout-and-diet-20120721" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2791/5c43a0c536d04715a27242a1c9587345.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.health24.com/Medical/Hypertension/Effects-on-the-body/Gout-and-diet-20120721" data-track="outbound,home,inside-Is your diet causing gout?" target="_self">Is your diet causing gout?</a></h4>
                    <p>Cut out these 14 foods to prevent gout.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.parent24.com/School_7-12/health_safety/Terrifying-road-safety-video-opts-for-gruesome-warning-20140623" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2796/dd2df972ab3f4176b5c33ad4aa9a362f.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.parent24.com/School_7-12/health_safety/Terrifying-road-safety-video-opts-for-gruesome-warning-20140623" data-track="outbound,home,inside-Scary road safety ad" target="_self">Scary road safety ad</a></h4>
                    <p>Road safety PSA opts for drastic measures to achieve effect.</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.food24.com/Recipes-and-Menus/Easy-Weekday-Meals" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/168/abf07351bffb462e81e3e3522258d3e8.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.food24.com/Recipes-and-Menus/Easy-Weekday-Meals" data-track="outbound,home,inside-Easy weekday meals" target="_self">Easy weekday meals</a></h4>
                    <p>Easy chicken pie, beef enchiladas. mac 'n cheese and more. </p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.news24.com/Travel/Guides/Island-Escapes/Reunion-Island-volcano-erupts-giving-adventurers-a-rare-sight-20140623" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/168/c8abf0530cc04432830519c7cbfef733.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.news24.com/Travel/Guides/Island-Escapes/Reunion-Island-volcano-erupts-giving-adventurers-a-rare-sight-20140623" data-track="outbound,home,inside-Thrilling eruption" target="_self">Thrilling eruption</a></h4>
                    <p>Reunion island visitors are being spoiled with a rare sight... </p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.parent24.com/Toddler_1-2/SoftAndShiny/3-year-old-girl-donates-her-hair-to-cancer-patients-20140620" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2794/6de83b695cd942e8a26a64f74c35b8e3.gif" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.parent24.com/Toddler_1-2/SoftAndShiny/3-year-old-girl-donates-her-hair-to-cancer-patients-20140620" data-track="outbound,home,inside-Viral: Toddler\&#39;s hair inspires!" target="_self">Viral: Toddler's hair inspires!</a></h4>
                    <p>Watch: 3 year old Emily donates her hair to cancer patients</p>
		        </div>
		      </li>
	        
	          <li>
		        <div class="item left">
                    <div class="img_wrap">
                        <a href="http://www.fin24.com/Savings/YourVoice/Another-chance-to-bag-R2-000-in-cash-20140620" target="_self"><img src="http://static.24.co.za/5/images/lazy/137x125.jpg" width="130" height="114" data-src="http://cdn.24.co.za/files/Cms/General/d/2795/83d011d4fb45419a8bc76e8e221b51ef.jpg" /></a>
                    </div>    
                    <h4 class="bold"><a href="http://www.fin24.com/Savings/YourVoice/Another-chance-to-bag-R2-000-in-cash-20140620" data-track="outbound,home,inside-Win R2 000!" target="_self">Win R2 000!</a></h4>
                    <p>Add your voice to Fin24's Savings Issue & stand a chance of bagging R2 000.</p>
		        </div>
		      </li>
	        
	          </ul>
	        
	    </div>
    </div>	
    <div id="" class="left col13"> </div>
</div>
<div class="clr">&nbsp;</div>


        <div class="spacer clr">
            </div>
        

<div id="promotion_box" class="left col626">
    <div id='ad-1x1-1' class='24ad1x1'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('1x1','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=1x1&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=1x1&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
</div>
    </div>

            </div>
            <div id="right_column" class="grey_grad left col299">
                
    <div class="personallogin">
        <div id="PanelLogIn">
	
    <div class="welcome">
        <h2 class="bold">Welcome to News24</h2>
        <div class="login_block"><a href="javascript:void(0)" class="submit_button">Login | Sign Up</a></div>
    </div>
    <div class="clr"></div>
    

<div class="uploadblack">
    <div class="blackblock_heading">Get Published!</div>
    <div class="blackblock_upload"><strong>UPLOAD</strong></div>
    <div class="blackblock_icons">
        <a class="tooltip call2action" href="http://uploads.news24.com/#story">
            <img width="24" height="24" border="0" alt="" src='http://static.24.co.za/5/images/profile/article_icon.jpg'>
            <span><b>Click here<br>to upload<br>your article</b></span>
        </a>
        <a class="tooltip call2action" href="http://uploads.news24.com/#images">
            <img width="24" height="24" border="0" alt="" src='http://static.24.co.za/5/images/profile/camera_icon.jpg'>
            <span><b>Click here<br />to upload<br />your photo</b></span>
        </a>
        <a class="tooltip call2action" href="http://uploads.news24.com/#videos">
            <img width="24" height="24" border="0" alt="" src='http://static.24.co.za/5/images/profile/video_icon.jpg'>
            <span><b>Click here<br>to upload<br>your video</b></span>
        </a>
    </div>
</div>

</div>


        <div class="clr">
        </div>
    </div>
    


<script language="javascript" type="text/javascript">
    var tabsClass = { tabSetArray: new Array, classOn: "tabs_on", classOff: "tabs_off", addTabs: function (a) { tabs = document.getElementById(a).getElementsByTagName("div"); for (x in tabs) { if (typeof tabs[x].id != "undefined") { this.tabSetArray.push(tabs[x].id) } else { } } }, switchTab: function (a) { for (x in this.tabSetArray) { tabItem = this.tabSetArray[x]; dataElement = document.getElementById(tabItem + "_data"); if (dataElement) { if (dataElement.style.display != "none") { dataElement.style.display = "none" } else { } } else { } tabElement = document.getElementById(tabItem); if (tabElement) { if (tabElement.className != this.classOff) { tabElement.className = this.classOff } else { } } else { } } document.getElementById(a.id + "_data").style.display = ""; a.className = this.classOn } }
</script>

<div id="most_box" class="col299 tabs">
    
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        
          <tr>
            <td>
                <div id="mostTabContainer" class="localised tabNavigation tab-menu">
	                <div id="tab_read" class="tabs_on left" onmouseover="tabsClass.switchTab(this);">Most Read</div>
                    <div id="tab_comment" class="tabs_off left" onmouseover="tabsClass.switchTab(this);">Most Commented</div>
                    <div id="tab_area" class="tabs_off left" onmouseover="tabsClass.switchTab(this);">News In Your Area</div>
                </div>
            </td>
        </tr>
        <tr>
            <td>
                

<div id="tab_read_data" class="tab-wrapper">
    <ul class="bold">
            <li><a data-track="outbound,mostread,mostread-Why shouldn\&#39;t we notice Maimane\&#39;s wife\&#39;s race?" href="http://www.news24.com/Columnists/TOMolefe/Why-shouldnt-we-notice-Maimanes-wifes-race-20140623">Why shouldn't we notice Maimane's wife's race?</a></li>
        
            <li><a data-track="outbound,mostread,mostread-Local actor violently attacked and robbed in Knysna" href="http://www.channel24.co.za/News/Local/Local-actor-violently-attacked-and-robbed-in-Knysna-20140624">Local actor violently attacked and robbed in Knysna</a></li>
        
            <li><a data-track="outbound,mostread,mostread-Zuma put up for sale in ad - report" href="http://www.news24.com/SouthAfrica/News/Zuma-put-up-for-sale-in-ad-report-20140623">Zuma put up for sale in ad - report</a></li>
        
            <li><a data-track="outbound,mostread,mostread-Amcu ends five-month platinum strike" href="http://www.fin24.com/Economy/Amcu-ends-five-month-platinum-strike-20140623">Amcu ends five-month platinum strike</a></li>
        
            <li><a data-track="outbound,mostread,mostread-Mayor held for Mandela funeral fraud" href="http://www.news24.com/SouthAfrica/News/Mayor-held-for-Mandela-funeral-fraud-20140623">Mayor held for Mandela funeral fraud</a></li>
        </ul>
    <div class="spacer clr"></div>
    <a id="lnkReadMore" Class="lnkMore" href="http://www.news24.com/TopStories">More..</a>
</div>
                

<div id="tab_comment_data" class="tab-wrapper" style="display: none;">
    <div class="clr"></div>
    <ul class="bold">
            <li><a data-track="outbound,mostread,mostcommented-Corruption is a cancer - ANC" href="http://www.news24.com/SouthAfrica/Politics/Corruption-is-a-cancer-ANC-20140623">Corruption is a cancer - ANC</a></li>
        
            <li><a data-track="outbound,mostread,mostcommented-Derby-Lewis’s wife to approach protector" href="http://www.news24.com/SouthAfrica/News/Derby-Lewiss-wife-to-approach-protector-20140623">Derby-Lewis’s wife to approach protector</a></li>
        
            <li><a data-track="outbound,mostread,mostcommented-Zuma put up for sale in ad - report" href="http://www.news24.com/SouthAfrica/News/Zuma-put-up-for-sale-in-ad-report-20140623">Zuma put up for sale in ad - report</a></li>
        
            <li><a data-track="outbound,mostread,mostcommented-SA\&#39;s youngest doctor loves his country" href="http://www.news24.com/SouthAfrica/News/SAs-youngest-doctor-loves-his-country-20140622">SA's youngest doctor loves his country</a></li>
        
            <li><a data-track="outbound,mostread,mostcommented-Plan to share farms with workers on track" href="http://www.news24.com/SouthAfrica/News/Plan-to-share-farms-with-workers-on-track-20140622">Plan to share farms with workers on track</a></li>
        </ul>
    <div class="spacer clr"></div>                        
    <a id="lnkCommentMore" Class="lnkMore" href="http://www.news24.com/TopStories">More..</a>
</div>
<div id="tab_area_data" class="tab-wrapper" style="display: none;">
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=mostread" id="lnkModalDisplay" class="userLocationModal right change_link">[change area]</a>
    <h4 id="areaHeading" class="left most_head bold">News in Cape Town</h4>    
    <div class="clr"></div>
    <ul class="bold">
            <li><a data-track="outbound,mostread,mostreadarea-School holiday fun at the Table Mountain Cableway" href="http://www.news24.com/Travel/South-Africa/School-holiday-fun-at-the-Table-Mountain-Cableway-20140624">School holiday fun at the Table Mountain Cableway</a></li>
        
            <li><a data-track="outbound,mostread,mostreadarea-R179m for small firms in the Cape" href="http://www.fin24.com/Entrepreneurs/News/R179m-for-small-firms-in-the-Cape-20140620">R179m for small firms in the Cape</a></li>
        
            <li><a data-track="outbound,mostread,mostreadarea-PIs, cop in court for homeless man\&#39;s murder" href="http://www.news24.com/SouthAfrica/News/PIs-cop-in-court-for-homeless-mans-murder-20140624">PIs, cop in court for homeless man's murder</a></li>
        
            <li><a data-track="outbound,mostread,mostreadarea-Rocking the Daisies announces big international headliner" href="http://www.channel24.co.za/Music/News/Rocking-the-Daisies-announces-big-international-headliner-20140624">Rocking the Daisies announces big international headliner</a></li>
        
            <li><a data-track="outbound,mostread,mostreadarea-Paralegal to decide on plea bargain or trial" href="http://www.news24.com/SouthAfrica/News/Paralegal-to-decide-on-plea-bargain-or-trial-20140624">Paralegal to decide on plea bargain or trial</a></li>
        </ul>
</div>               
                <script type="text/javascript">
                      tabsClass.addTabs("mostTabContainer");
			    </script>
            </td>
        </tr>
        <tr>
            <td>
                <div class="ad278X35 outsurance"><!-- outsurance Ad -->
	                <div id='ad-278x76-1' class='24ad278x76'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('278x76','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=278x76&c=1118552289&t=artid%3ddf8ae1f0-3fbc-4e4a-9a59-c7c9a69f36f1%26Companies%3dlonmin%26Places%3dmahikeng%26Topics%3dmarikana+inquiry%2cmining+unrest%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=278x76&c=1118552289&t=artid%3ddf8ae1f0-3fbc-4e4a-9a59-c7c9a69f36f1%26Companies%3dlonmin%26Places%3dmahikeng%26Topics%3dmarikana+inquiry%2cmining+unrest%26posno%3d1' border='0' alt=''></a></noscript>
                </div>
            </td>
        </tr>
    </table>
    <a id="lnkModalItem" class="fireEventMost locationModal" style="display:none;"></a>
</div>

    <div class="spacer clr">
        </div>
    <div class="ad300X600 col300">
        <div id='ad-300x600-1' class='24ad300x600'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('300x600','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=300x600&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=300x600&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
    </div>
    <div class="spacer clr">
        </div>
    
    
<div id='bgColour' class='left relative sitewide_block ' style='background:#e7e7e7 url(http://cdn.24.co.za/files/Cms/General/d/2787/9a247e3983d84616908254d7baf70ff4.jpg) no-repeat top left; width:292px;border:4px solid #005e00 ;background-color:#e7e7e7;' ><div class="media_wrapper False">
<div class="generic_header">
<div style='min-height: 50px; max-height: 100px; margin: -6px -6px -6px -7px; min-width: 100%;height:150px!important;'></div>
</div>

<div class="clr borderdotted">&nbsp;</div>
<div class='news_item'>
<a href="http://www.sport24.co.za/Soccer/SWC-team-after-Round-Two-20140623-2" target="_blank" data-track="SitewideComponent,SWC-team-after-Round-Two-20140623-2"><img src="http://cdn.24.co.za/files/Cms/General/d/2763/b389d2840f434cb6a816a13d28d5ff43.jpg"  class="left" width="65" height="65"/></a>
<h4><a href="http://www.sport24.co.za/Soccer/SWC-team-after-Round-Two-20140623-2" data-track="SitewideComponent,SWC-team-after-Round-Two-20140623-2" style="color:#005e00">SWC team after Round Two</a></h4>
<p>The SWC is in full swing and after tonight, four teams will be heading for the airport. Here is the team of tournament, so far.</p>
</div>

<div class="clr borderdotted">&nbsp;</div>
<ul>
<li>
<a href="http://www.sport24.co.za/Soccer/WorldCup/Schedule">Find out when your team is playing</a>
</li>
<li>
<a href="http://www.sport24.co.za/Soccer/WorldCup/Results">Catch up with the latest results</a>
</li>
<li>
<a href="http://www.sport24.co.za/Soccer/WorldCup/Logs">See who's leading the pack</a>
</li>
</ul>

<div class="clr borderdotted">&nbsp;</div>
<h2 class="bold" id="secondHeadingColor"><a href="http://www.sport24.co.za/soccer/worldcup/multimedia" style="color:#005e00!important">Latest World Cup multimedia</a></h2>
<div class="media_images left">
<div class="clr"></div>
<div class="multsitewideFalse" style="float: left;">
<a href="http://www.sport24.co.za/Soccer/WorldCup/Multimedia/World-Cup-mascots-dirty-dancing-20140624" target="_blank" id="lnkGallery" class="gallery_list"><img src='/images/lazy/65x65.jpg' data-src="http://cdn.24.co.za/files/Cms/General/d/2796/a7293a1e91e34a47b180b5a314fc54da.png" width="65" height="65"/></a>
</div>
<div id="multTitleSiteWideHoverFalse0" class="multiBlueGrey" style="margin-left: 0px; width: 258px;background-color:#005e00;">
<div style="margin-top: -20px;margin-left: 0px; position: absolute;border-color: transparent transparent #005e00 transparent;border-style: solid;border-width: 0px 20px 20px 20px;height: 0px;width: 0px;"></div>
<span style="font-size: 13px; font-weight: bold;color:#ffffff!important;">World Cup mascot's dirty dancing</span></div>
<div class="multsitewideFalse" style="float: left;">
<a href="http://www.sport24.co.za/Soccer/WorldCup/Multimedia/Top-10-SWC-WAGS-20140619" target="_blank" id="lnkGallery" class="gallery_list"><img src='/images/lazy/65x65.jpg' data-src="http://cdn.24.co.za/files/Cms/General/d/2760/fd2b3b3cb1b44834aa70b23807a36506.jpg" width="65" height="65"/></a>
</div>
<div id="multTitleSiteWideHoverFalse1" class="multiBlueGrey" style="margin-left: 0px; width: 258px;background-color:#005e00;">
<div style="margin-top: -20px;margin-left: 70px; position: absolute;border-color: transparent transparent #005e00 transparent;border-style: solid;border-width: 0px 20px 20px 20px;height: 0px;width: 0px;"></div>
<span style="font-size: 13px; font-weight: bold;color:#ffffff!important;">Top 10 SWC WAGS</span></div>
<div class="multsitewideFalse" style="float: left;">
<a href="http://www.sport24.co.za/Soccer/WorldCup/Multimedia/SWC-WAG-of-the-Week-20140619" target="_blank" id="lnkGallery" class="gallery_list"><img src='/images/lazy/65x65.jpg' data-src="http://cdn.24.co.za/files/Cms/General/d/2759/6564a92fc33a4fd7b54bf63c230b0b22.jpg" width="65" height="65"/></a>
</div>
<div id="multTitleSiteWideHoverFalse2" class="multiBlueGrey" style="margin-left: 0px; width: 258px;background-color:#005e00;">
<div style="margin-top: -20px;margin-left: 140px; position: absolute;border-color: transparent transparent #005e00 transparent;border-style: solid;border-width: 0px 20px 20px 20px;height: 0px;width: 0px;"></div>
<span style="font-size: 13px; font-weight: bold;color:#ffffff!important;">SWC WAG of the Week</span></div>
<div class="multsitewideFalse" style="float: left;">
<a href="http://www.sport24.co.za/Soccer/WorldCup/Multimedia/Body-painted-SWC-babes-20140613" target="_blank" id="lnkGallery" class="gallery_list"><img src='/images/lazy/65x65.jpg' data-src="http://cdn.24.co.za/files/Cms/General/d/2787/1f4fea494d454e129ca7f3a908841a7a.jpg" width="65" height="65"/></a>
</div>
<div id="multTitleSiteWideHoverFalse3" class="multiBlueGrey" style="margin-left: 0px; width: 258px;background-color:#005e00;">
<div style="margin-top: -20px;margin-left: 210px; position: absolute;border-color: transparent transparent #005e00 transparent;border-style: solid;border-width: 0px 20px 20px 20px;height: 0px;width: 0px;"></div>
<span style="font-size: 13px; font-weight: bold;color:#ffffff!important;">Body painted SWC babes</span></div>
<div class="clr"></div>
</div>

<a href="http://pubads.g.doubleclick.net/gampad/clk?id=81443350&iu=/8900/24.com/Web/Sport24" target="_blank" data-track="SitewideComponent,SponsorAdBanner,News24" alt=" " title=" "><img src='/images/lazy/65x65.jpg' data-src="http://cdn.24.co.za/files/Cms/General/d/2795/b66af6d23d8c489dbe4214e64e6a12fe.jpg" /></a>
</div>
<div class="clr"></div>
</div>

<script type="text/javascript">
jQuery(document).ready(function () {
$j('.multsitewideFalse').each(function (index) {
$j(this).hover(function () { $j('.media_wrapper.False .multiBlueGrey').hide(); $j("#multTitleSiteWideHoverFalse" + index).show(); });
});
setTimeout(function() {$j('#multTitleSiteWideHoverFalse0').show();},0);
});
</script>
<div class="clr" style="height: 10px;"></div>


    <div class="spacer clr">
        </div>
    
    <div class="spacer clr">
        </div>
    <div id="fb_social"></div>
<script type="text/javascript" src="http://scripts.24.co.za/libs/24com/SocialNews/3.0/scripts/socialnews.min.js?v=20140620" type="text/javascript"></script>
<script type="text/javascript" >
jQuery('head').append('<link rel="stylesheet" href="http://scripts.24.co.za/libs/24com/SocialNews/3.0/styles/socialnews.css?v=20140620" type="text/css" />');
jQuery(document).ready(function(){
FBSocialNews.settings.siteDomain="www.news24.com";
FBSocialNews.settings.parentDomain="www.news24.com";
FBSocialNews.settings.activityServiceUrl="http://fbactivity.24.com/";
FBSocialNews.settings.appID="2363277980";
FBSocialNews.settings.tinaBaseUrl="http://auth.news24.com";
FBSocialNews.settings.isArticle=true;
FBSocialNews.settings.actionType='read';
FBSocialNews.settings.overrideFriendActivity=false;
if(typeof LanguageResource != 'undefined')FBSocialNews.settings.language=LanguageResource.languages.eng;
FBSocialNews.userProfile.hasPermission=false;
FBSocialNews.init();
});
</script>
<div class="clr socialspacer"></div>
<a href="/SocialSharingPopup.aspx" class="iframe socialSharePopup" style="display:none;"></a>

    <div class="spacer clr">
        </div>
    
    
    

<script language="javascript" type="text/javascript">
    $j(document).ready(function () { var a = "capetown"; if (a == "" || a == "default") { $j("#tab_traffic_data").attr("class", "tab-wrapper") } }); var tabsInfoClass = { tabInfoSetArray: new Array, classOn: "tabs_on left", classOff: "tabs_off left", addTabs: function (a) { tabs = document.getElementById(a).getElementsByTagName("div"); for (x in tabs) { if (typeof tabs[x].id != "undefined") { this.tabInfoSetArray.push(tabs[x].id) } else { } } }, switchTab: function (a) { for (x in this.tabInfoSetArray) { tabItem = this.tabInfoSetArray[x]; dataElement = document.getElementById(tabItem + "_data"); if (dataElement) { if (dataElement.style.display != "none") { dataElement.style.display = "none" } else { } } else { } tabElement = document.getElementById(tabItem); if (tabElement) { if (tabElement.className != this.classOff) { tabElement.className = this.classOff } else { } } else { } } document.getElementById(a.id + "_data").style.display = ""; a.className = this.classOn } }
</script>

<div class="clr10">&nbsp;</div>
<div id="weather_box" class="col299 relative tabs2">
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td>
                <div id="infoTabContainer" class="tabNavigation tab-menu">
                    <div id="tab_traffic" class="tabs_on left" onmouseover="tabsInfoClass.switchTab(this);">Traffic</div>
                    <div id="tab_lottery" class="tabs_off left" onmouseover="tabsInfoClass.switchTab(this);">Lottery</div>
                </div>
            </td>
        </tr>
        <tr>
            <td class="relative">
                <div id="tab_traffic_data" class="tab-wrapper-beta">

<div id="traffic_box">
    <div class="traffic_header">
        <!--<h3 class="bold left">Traffic</h3>//-->
        <div class="dropdown left"><select id='ddlTrafficRegions'><option value='' >Select region..</option><option value='Gauteng' >Gauteng</option><option value='KwaZulu-Natal' >KwaZulu-Natal</option><option value='Western Cape' selected='selected'>Western Cape</option><option value='Free State' >Free State</option><option value='Northern Cape' >Northern Cape</option><option value='Eastern Cape' >Eastern Cape</option><option value='North West' >North West</option><option value='Mpumalanga' >Mpumalanga</option></select></div>
    </div>
    <div class="traffic_container">
        <div class="clr5 clr">&nbsp;</div>
        <div id="trafic-container" class="left">
            <ul><li><span class='day'>Tuesday</span>&nbsp;<span class='location'>Table View - 15:09 PM</span><br/><span class='road'>Road name: Marine Drive Southbound</span><br/><span class='description'>TRUCK ACCIDENT in Sunset Beach - delays from Table View</span></li><li><span class='day'>Tuesday</span>&nbsp;<span class='location'>Epping - 15:06 PM</span><br/><span class='road'>Road name: N7 Vanguard Drive Northbound</span><br/><span class='description'>DELAYS approaching Bofors Circle</span></li></ul>
        </div>
        <div class="clr5 clr">&nbsp;</div>
        <a href="http://www.news24.com/Traffic/WESTERN_CAPE" id="lnkMore" class="block bold">More traffic reports...</a>
        <div class="clr5 clr">&nbsp;</div>
        <a id="lnkSponsor"></a>
        <script type="text/javascript">
            $j(document).ready(function () { $j("#ddlTrafficRegions").change(function () { var e = $j("OPTION:selected", this).val(); var t = "traffic/" + e.replace(" ", "_").toUpperCase(); $j("#lnkMore").html("<a id='lnkMore' href='" + t + "' class='block bold'>More traffic reports...</a>"); $j("#trafic-container").hide(); news24.getAjax("/Ajax/TrafficData/", "GetTraffic", { 'location': e }, function (e) { $j("#trafic-container").html(e); $j("#trafic-container").fadeIn("slow") }) }) });
        </script>
    </div>
</div></div>
                <div id="tab_lottery_data" class="tab-wrapper" style="display: none;">Here are the winning Lotto numbers for the Saturday, 21 June draw.<br />&nbsp;2, 5, 8, 16, 36, 38 Bonus 17<br /><br />Lotto Plus: 2, 8, 25, 35, 43, 49 Bonus 21<br /><br /><strong>SMS the word Lotto to 31222 to get Lotto numbers sent directly to your phone. The service costs just R10 per month.<br /><br /></strong><br /><br /><strong>To unsubscribe, reply with the words Stop Lotto. <br /></strong><br />
<div class="spacer clr"></div>
<a href="http://www.news24.com/Lottery" id="lnkMoreLotto" class="block bold">More lotto numbers...</a></div>
                <script type="text/javascript">tabsInfoClass.addTabs("infoTabContainer");</script>
            </td>
        </tr>
    </table>
</div>
<div class="spacer clr"></div>
    <div class="spacer clr">
        </div>
    <div class="ad300X250 col300">
        <div id='ad-300x250-1' class='24ad300x250'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('300x250','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=300x250&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=300x250&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
    </div>
    <div class="spacer clr">
        </div>
    
<script type="text/javascript">
    function InsuranceDealsGoTo(a) { $j("#sponsor_carousel").jcarousel("scroll", a, true); $j("#sponsor_carousel").jcarousel("reload"); return false } function movenext() { $j("#sponsor_carousel").jcarousel("next"); return false } function moveback() { $j("#sponsor_carousel").jcarousel("prev"); return false } function mycarousel_itemFirstInCallback(a, b, c, d) { var e = c; $j("div#adlist ul li").removeClass("selected"); $j("div#adlist ul li").removeAttr("style"); $j("div#adlist ul a").removeAttr("style"); $j("#ad_" + e).parent().addClass("selected"); $j("#ad_" + e).parent().attr("style", "background-color:" + colors[e] + ";color:" + textcolors[e]); $j("#ad_" + e).attr("style", "color:" + textcolors[e]); $j("#jcarousel-prev").unbind("click"); $j("#jcarousel-next").unbind("click"); if (e == 1) { $j("#jcarousel-prev").removeClass("jcarousel-prev-disabled").addClass("jcarousel-prev-disabled"); $j("#jcarousel-prev").attr("disabled", "disabled"); $j("#jcarousel-prev").unbind("click") } else { $j("#jcarousel-prev").removeClass("jcarousel-prev-disabled"); $j("#jcarousel-prev").attr("disabled", ""); $j("#jcarousel-prev").bind("click", moveback) } if (e == last) { $j("#jcarousel-next").removeClass("jcarousel-next-disabled").addClass("jcarousel-next-disabled"); $j("#jcarousel-next").attr("disabled", "disabled"); $j("#jcarousel-next").unbind("click") } else { $j("#jcarousel-next").removeClass("jcarousel-next-disabled"); $j("#jcarousel-next").attr("disabled", ""); $j("#jcarousel-next").bind("click", movenext) } } $j(document).ready(function () { $j('#jcarousel-next').bind('click', movenext); $j('#jcarousel-prev').bind('click', moveback); var randomnumber = Math.floor(Math.random() *0 +1); $j("#sponsor_carousel").jcarousel({ scroll: 1, start: randomnumber, itemFirstInCallback: mycarousel_itemFirstInCallback, buttonNextHTML: null, buttonPrevHTML: null }); $j("#sponsored_holder").removeClass("tabLoader") });
</script>


<div class="spacer clr"></div>
    

<div id="the_accordion" class="tabLoader">
    <div id="accordion" class="col299 relative">
        <h3 id="headerTag" class="toggler toggler_pers">
    <a href="http://www.careers24.com/cape-town-jobs" class="bold toggler_anchor">Jobs in Cape Town</a>
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=careers" id="lnkModalDisplay" class="careersModal right" style="padding-right:5px;text-transform:lowercase;font-size:11px">[change area]</a>
</h3>
<div class="element">
    <div id="divToHide">
        <h4 id="headerCareersRegion" class="bold item" style="font-size:11px;">Jobs in Western Cape region</h4>
        
	         <div class="item">
                
                    <h4 class="bold">
                        <a data-track="outbound,rightnav-listings,careers-PS896 BEQUEST &amp; MAJOR DONOR OFFICER, NPO" href="http://www.careers24.com/jobs/adverts/480556-ps896-bequest-major-donor-officer-npo-cape-town-southern-suburbs/" target="_blank">PS896 BEQUEST & MAJOR DONOR OFFICER, NPO</a></h4>
                        <img src="http://static.24.co.za/5/images/lazy/86x48.jpg" class="right job" width="86" height="48" data-src="/imagecache.axd?url=http%3a%2f%2fwww.careers24.com%2f_resx%2fimageresource%2f95A7FC908DBD21FC76C7966745B60B4BE1338E7C-975-86-48-0" />
                    <p>
                        Cape Town Southern Suburbs<br/>Anchor Executive Recruitment (Pty) Ltd<br/></p>
                    
                    <div class="clr">
                    </div>
                </div>
          
	         <div class="item">
                
                    <h4 class="bold">
                        <a data-track="outbound,rightnav-listings,careers-Supply Chain Manager" href="http://www.careers24.com/jobs/adverts/476801-supply-chain-manager-cape-town/" target="_blank">Supply Chain Manager</a></h4>
                        <img src="http://static.24.co.za/5/images/lazy/86x48.jpg" class="right job" width="86" height="48" data-src="/imagecache.axd?url=http%3a%2f%2fwww.careers24.com%2f_resx%2fimageresource%2f6BF54C4B72E35F6E046C9BFC548394BE3D3562DA-88300-86-48-0" />
                    <p>
                        Cape Town<br/>Purple Door Recruitment (Pty) Ltd<br/>R8 000 - R10 500 Per Month</p>
                    
                    <div class="clr">
                    </div>
                </div>
          
	         <div class="item">
                
                    <h4 class="bold">
                        <a data-track="outbound,rightnav-listings,careers-IT DEVELOPER" href="http://www.careers24.com/jobs/adverts/468923-it-developer-milnerton/" target="_blank">IT DEVELOPER</a></h4>
                        
                    <p>
                        Milnerton<br/>CR Solutions<br/></p>
                    
                    <div class="clr">
                    </div>
                </div>
          
	    <div class="item browse bold">
		    <a href="http://www.careers24.com/cape-town-jobs" target="_blank">Browse more Cape Town jobs...</a>
	    </div>
	    <div class="item">
                <div class="left" style="margin-left: 0px; width: 140px;">
                    <ul>
                        
                                <li>
                                    <a href='http://www.careers24.com/pretoria-jobs' title='Pretoria Jobs'>
                                        Pretoria Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/kimberley-jobs' title='Kimberley Jobs'>
                                        Kimberley Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/jobs-in-gauteng' title='Gauteng Jobs'>
                                        Gauteng Jobs
                                    </a> 
                                </li>
                            
                    </ul>
                </div>
                <div class="left" style="margin-right:13px">
                    <ul>
                        
                                <li>
                                    <a href='http://www.careers24.com/call-centre-jobs' title='Call Centre Jobs'>
                                        Call Centre Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/insurance-jobs' title='Insurance Jobs'>
                                        Insurance Jobs
                                    </a> 
                                </li>
                            
                                <li>
                                    <a href='http://www.careers24.com/admin-jobs' title='Admin Jobs'>
                                        Admin Jobs
                                    </a> 
                                </li>
                            
                    </ul>
                </div>
                <div class="clr"></div>
        </div>
	    <div class="item bold last">
		    <a href="http://www.careers24.com/candidate/register/" target="_blank">Register your CV...</a><br/>
		    <a href="http://www.careers24.com/jobs/alert/" target="_blank">Get Job alerts in your e-mail...</a><br/>
		    <a href="http://www.careers24.com/recruiters/" target="_blank">RECRUITERS – Advertise your jobs here</a>
	    </div>
        <a id="lnkModalItem" class="fireEventCareers careersModal" style="display:none;"></a>
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler toggler_pers">
    <a href="http://www.property24.com" class="bold toggler_anchor">Property</a>
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=property" id="lnkModalDisplay" class="propertyModal right" style="padding-right:5px;text-transform:lowercase;font-size:11px">[change area]</a>
</h3>
<div class="element">
    <div id="divToHide">
        
        
                <div class="item">
	                <div class="wrapper">
	                <a href="http://www.property24.com/for-sale/stellenbosch/western-cape/459?ListingNumber=P24-101889409" id="lnkThumb">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages.property24.com%2fFetchImage.ashx%3fuid%3d49047324%26size%3dmedium" />
                    </a>
                    </div>
                    <div class="wrapper">
		            <h4 class="bold"><a data-track="outbound,rightnav-listings,property-HOUSES FOR SALE IN Stellenbosch, De Zalze Winelands Golf Estate" href="http://www.property24.com/for-sale/stellenbosch/western-cape/459?ListingNumber=P24-101889409" target="_blank">HOUSES FOR SALE IN Stellenbosch, De Zalze Winelands Golf Estate</a></h4>
		            <p><span class="block">Houses</span>
		            <span class="block bold">R 19 750 000</span></p>
                    </div>
		            <div class="clr"></div>
	            </div>
            
                <div class="item">
	                <div class="wrapper">
	                <a href="http://www.property24.com/for-sale/cape-town/western-cape/432?ListingNumber=P24-101901444" id="lnkThumb">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages.property24.com%2fFetchImage.ashx%3fuid%3d49375200%26size%3dmedium" />
                    </a>
                    </div>
                    <div class="wrapper">
		            <h4 class="bold"><a data-track="outbound,rightnav-listings,property-TOWNHOUSES FOR SALE IN Cape Town, Camps Bay" href="http://www.property24.com/for-sale/cape-town/western-cape/432?ListingNumber=P24-101901444" target="_blank">TOWNHOUSES FOR SALE IN Cape Town, Camps Bay</a></h4>
		            <p><span class="block">Townhouses</span>
		            <span class="block bold">R 12 950 000</span></p>
                    </div>
		            <div class="clr"></div>
	            </div>
            
                <div class="item">
	                <div class="wrapper">
	                <a href="http://www.property24.com/for-sale/hermanus/western-cape/400?ListingNumber=P24-101903202" id="lnkThumb">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages.property24.com%2fFetchImage.ashx%3fuid%3d49433175%26size%3dmedium" />
                    </a>
                    </div>
                    <div class="wrapper">
		            <h4 class="bold"><a data-track="outbound,rightnav-listings,property-HOUSES FOR SALE IN Hermanus, Onrus" href="http://www.property24.com/for-sale/hermanus/western-cape/400?ListingNumber=P24-101903202" target="_blank">HOUSES FOR SALE IN Hermanus, Onrus</a></h4>
		            <p><span class="block">Houses</span>
		            <span class="block bold">R 2 250 000</span></p>
                    </div>
		            <div class="clr"></div>
	            </div>
            
        <a id="lnkModalItem" class="fireEventProperty propertyModal" style="display:none;"></a>
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler" style="height:15px;"><a href="http://www.gotravel24.com/" class="bold">Travel</a> - Look, Book, Go!</h3>
<div class="element">
    <div id="divToHide">
	    <div class="item travel"><!-- add travel class -->
		    <h4 class="bold"><a id="lnkTitle" href="http://holidays.gotravel24.com/ku/holidayoffer.jsp?Destination=MASSINGA_GT,RG,RB&amp;utm_source=holidays&amp;utm_medium=focus&amp;utm_campaign=may_massinga">Magical Massinga</a></h4>
		    <img src="http://static.24.co.za/5/images/lazy/110x65.jpg" id="imgThumbnail" width="110" height="65" class="right" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fwww.gotravel24.com%2ffiles%2fmassinga_ext_05.jpg" />
		    Spend 5 nights at the gorgeous Massinga Beach Lodge in Mozambique and only pay for 4 from R13 220 per person sharing. Includes return flights, accommodation, transfers and romantic turndown.
		    <span class="item browse bold block"><a id="lnkPackages" href="http://holidays.gotravel24.com/ku/holidayoffer.jsp?Destination=MASSINGA_GT,RG,RB&amp;utm_source=holidays&amp;utm_medium=focus&amp;utm_campaign=may_massinga">Book now!</a></span>
	    </div>
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler"><a href="http://etrader.kalahari.com/referral.asp?linkid=3442&partnerid=9180" class="bold">Kalahari.com</a> - shop online today</h3>
<div class="element">
    <div id="divToHide">
        
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=20090&amp;Ns=p_sales30days%7c1&amp;linkId=2103600&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=20090&amp;Ns=p_sales30days%7c1&amp;linkId=2103600&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">Top trending eBooks</a></h4>
		              <p style="word-wrap:break-word;">The Real Meal Revolution by Tim Noakes, Laaste Dans, Drienie by Steve Hofmeyr, Jeffrey Archer’s Be Careful What You Wish For and many more. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=24047&amp;linkId=2088165&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=24047&amp;linkId=2088165&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">Mind blowing deals on electronics!</a></h4>
		              <p style="word-wrap:break-word;">Save up to 35% on electronics. Offer valid while stocks last. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=24097&amp;linkId=2088164&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=24097&amp;linkId=2088164&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">Up to 50% off outdoor & braai</a></h4>
		              <p style="word-wrap:break-word;">Hurry and grab some mind blowing deals on outdoor and braai products. Offer valid while stocks last. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item">
                    <div class="left">
                        <a href="http://www.kalahari.com/s?N=23678+4294965726&amp;linkId=1988113&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/s?N=23678+4294965726&amp;linkId=1988113&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">2 DVDs for R99</a></h4>
		              <p style="word-wrap:break-word;">Save big on blockbuster movies including Man Of Steel, Pacific Rim, The Avengers and many more. Offer valid while stocks last. Shop now!</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
                <div class="item last">
                    <div class="left">
                        <a href="http://www.kalahari.com/electronics-mobile-phones/N-1z141o9Z1z141o6Z1z13t9vZd8m?linkId=1988444&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank"></a>
                    </div>
                    <div class="left" style="width:200px;padding:0 0 0 5px;">
		              <h4 class="bold"><a href="http://www.kalahari.com/electronics-mobile-phones/N-1z141o9Z1z141o6Z1z13t9vZd8m?linkId=1988444&amp;affiliateId=563&amp;linkType=ORDER_REFERRAL" target="blank">New gobii smartphones! </a></h4>
		              <p style="word-wrap:break-word;">Front and rear camera's, dual SIM capability and 200MB of FREE Cell C data every month for 12 months, are just some of the many features on these smartphones. Get yours now! Shop here.</p>
                    </div>
                    <div class="clr"></div>
	            </div>
                <div class="clr"></div>
            
        <div class="clr"></div>
        
    </div>
</div>
        <h3 id="headerTag" class="toggler toggler">
    <a href="http://www.olx.co.za/" class="bold toggler_anchor"> OLX Free Classifieds</a>
    <a href="http://www.news24.com/UserLocationModal.aspx?iframe&control=kalahari" id="lnkModalDisplay" class="kalahariModal right" style="padding-right:5px;text-transform:lowercase;font-size:11px">[change area]</a>
</h3>
<div class="element">
    <div id="divToHide">
        
	          <div style="min-height:100px;" class="item">
                    <a href="http://capetown.olx.co.za/samsung-galaxy-s4-iid-559689336" id="lnkThumb" target="_blank">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" id="imgKalahari" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages04.olx-st.com%2fui%2f7%2f99%2f36%2ft_1382642518_559689336_3.jpg" />
                    </a>
		            <h4 class="bold"><a id="lnkArticle" href="http://capetown.olx.co.za/samsung-galaxy-s4-iid-559689336" target="_blank">Samsung Galaxy s4</a></h4>
		            <p style="word-wrap:break-word;">Mobile, Cell Phones in South Africa, Western Cape, Cape Town. Date October 24</p>
	          </div>
          
	          <div style="min-height:100px;" class="item">
                    <a href="http://capetown.olx.co.za/best-bargain-in-big-bay-iid-559891688" id="lnkThumb" target="_blank">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" id="imgKalahari" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages02.olx-st.com%2fui%2f1%2f24%2f88%2ft_1382699383_559891688_1.jpg" />
                    </a>
		            <h4 class="bold"><a id="lnkArticle" href="http://capetown.olx.co.za/best-bargain-in-big-bay-iid-559891688" target="_blank">Best bargain in big bay</a></h4>
		            <p style="word-wrap:break-word;">Real Estate, Houses - Apartments for Sale in South Africa, Western Cape, Cape Town. Date October 25</p>
	          </div>
          
	          <div style="min-height:100px;" class="item last">
                    <a href="http://capetown.olx.co.za/vw-golf-6-1-6-trendline-excellent-condition-iid-559891037" id="lnkThumb" target="_blank">
                        <img src="http://static.24.co.za/5/images/lazy/128x100.jpg" id="imgKalahari" class="left" width="128" height="100" data-src="http://www.news24.com/imagecache.axd?url=http%3a%2f%2fimages02.olx-st.com%2fui%2f7%2f17%2f37%2ft_1382699205_559891037_1.jpg" />
                    </a>
		            <h4 class="bold"><a id="lnkArticle" href="http://capetown.olx.co.za/vw-golf-6-1-6-trendline-excellent-condition-iid-559891037" target="_blank">VW Golf 6, 1.6 Trendline (Excellent condition)</a></h4>
		            <p style="word-wrap:break-word;">Vehicles, Cars in South Africa, Western Cape, Cape Town. Date October 25</p>
	          </div>
          
        <a id="lnkModalItem" class="fireEventKalahari kalahariModal" style="display:none;"></a>
        <div class="clr"></div>
        
    </div>
</div>
    </div>
</div>
    <div class="spacer clr">
        </div>
    
    

<div id="sponsor_box" class="col299 relative">
	<h3 class="bold">Sponsored links</h3>
    
		<table class="sponsor" width="280" border="0" cellpadding="0" cellspacing="0">
		  <tbody>
	  
		  <tr>
			<td style="width:35px;"><a href="../../Controls/Common/#" id="lnkSponsorImg"><img src="http://cdn.24.co.za/files/Cms/General/d/2750/8ed416ece6764870bde5b0f2f59ba50a.png" style="width:27px;" /></a></td>
			<td align="left"><a href="http://pubads.g.doubleclick.net/gampad/clk?id=64882990&amp;iu=/8900/24.com/Web/News24/Homepage" target="_blank">Online Loans, Instant Approval</a></td>
			<td>&nbsp;</td>
	  
			<td style="width:35px;"><a href="../../Controls/Common/#" id="lnkSponsorImg"><img src="http://cdn.24.co.za/files/Cms/General/d/2735/032cce50a4fc45819f69e20b0f5831bb.jpg" style="width:27px;" /></a></td>
			<td align="left"><a href="http://pubads.g.doubleclick.net/gampad/clk?id=73484470&amp;iu=/8900/24.com/Web/News24" target="_blank">Personal Loan inseconds  </a></td>
		  </tr>
	  
		</tbody></table>
	  
</div>
    <div class="spacer clr">
        </div>
    <div class="clr10 clr"> </div>
<script src="http://scripts.24.co.za/libs/kalahari/2.2/Scripts/kalahari.carousel.widget.js" type="text/javascript"></script>
<div id="oprahwidgetcontainer">
<script type="text/javascript">
jQuery('head').append("<link href='http://scripts.24.co.za/libs/kalahari/2.2/Styles/kalahari.carousel.css' type='text/css' rel='stylesheet' ></link>")
var Widget = new kalaharicarouselwidget({
sku: [46656550,47824635,33940581,47332198,46848097],
token: "563",
container: "oprahwidgetcontainer",
visible:1,
refUrl: 'URL: http://www.kalahari.com/?linkId=46213&affiliateId=563&linkType=ORDER_REFERRAL'
});
</script>
</div>
<div class="clr10 clr"> </div>


    <div class="spacer clr">
        </div>
    

<script type="text/javascript">
    jQuery(function () {
        var submitFunc = function() { window.open('http://www.pricecheck.co.za/search/?utm_source=news24&utm_medium=affiliate&utm_campaign=sidebar&search=' + jQuery('#txtPriceCheckSearch').val()) };jQuery("#btnPriceCheckSubmit").click(submitFunc);jQuery("#txtPriceCheckSearch").keypress(function(e){if(e.keyCode===13){submitFunc();return false}})});
</script>

<div class="pricecheckBlock">
    <a href="http://www.pricecheck.co.za/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" target="_blank" id="lnkPriceCheckHeader" style="height:51px;left:0;position:absolute;top:0;width:298px;"></a>
    <div class="priceContent">
        <div class="priceBlurb">
            <p><a href="http://www.pricecheck.co.za/offers/30413329/BlackBerry+Curve+9380/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" id="aLink" target="_blank">BlackBerry Curve 9380</a></p>
            <p>The first BlackBerry Curve smartphone with a touch screen
Stay connected...</p>
            <p>
                <a href="http://www.pricecheck.co.za/offers/30413329/BlackBerry+Curve+9380/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" id="aLinkPrice" style="color:#ec3b27;" target="_blank">
                    <span style="font-weight:normal">From</span> <strong>R1799.00</strong>
                </a>
            </p>
        </div>
        <div class="priceImage"><a href="http://www.pricecheck.co.za/offers/30413329/BlackBerry+Curve+9380/?utm_source=news_24&utm_medium=affiliate&utm_campaign=sidebar" id="aLinkImage" target="_blank"><img src="http://static.24.co.za/5/images/lazy/65x65.jpg" id="imgThumb" data-src="http://images2.pricecheck.co.za/images/objects/hash/product/d35/662/bfa/image_small_30413329.jpg" /></a></div>
    </div>
    <div class="clr"></div>
    <div class="priceShopping">
        <h4>I'm shopping for:</h4>
        <input type="text" class="priceSearch" id="txtPriceCheckSearch" />
        <input type="button" class="priceSubmit" value="LET'S GO!" id="btnPriceCheckSubmit" />
    </div>
</div>
    <div class="spacer clr">
        </div>
    
<div class="facebook_block">
    <iframe src="http://www.facebook.com/plugins/likebox.php?href=http%3A%2F%2Fwww.facebook.com%2Fpages%2FNews24com%2F10227041841&width=300&height=245&show_faces=true&colorscheme=light&stream=false&show_border=true&header=false" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:300px; height:245px;" allowTransparency="true"></iframe>
</div>
    <div class="spacer clr">
        </div>
    

<div id="horoscopes_tab" class="tab-wrapper horoscope relative">
    <div class="horoscope_header"> Horoscopes</div>
    <div class="horoscope_women"><img src="http://static.24.co.za/5/images/women_horoscope.png" width="120" height="21" border="0" /></div>
	<div class="horoscope_midlevel">
        <div class="zodiac">
		    <select onchange="toggleSubmit(this)" name="ptype" id="ptype" class="absolute">
			     <option selected="selected" value="aquarius">Aquarius  (20 Jan - 18 Feb)</option>
			     <option value="aries">Aries  (21 Mar - 20 Apr)</option>
			     <option value="cancer">Cancer  (21Jun - 21 Jul)</option>
			     <option value="capricorn">Capricorn  (21Dec - 19 Jan)</option>
			     <option value="gemini">Gemini  (21 May - 20 Jun)</option>
			     <option value="leo">Leo  (22 Jul - 21 Aug)</option>
			     <option value="libra">Libra  (22 Sep - 22 Oct)</option>
			     <option value="pisces">Pisces  (19 Feb - 20 Mar)</option>
			     <option value="sagittarius">Sagittarius (22 Nov - 20 Dec)</option>
			     <option value="scorpio">Scorpio  (23 Oct - 21 Nov)</option>
			     <option value="taurus">Taurus  (21 Apr - 20 May)</option>
			     <option value="virgo">Virgo  (22 Aug - 21 Sep)</option>
    	      </select>
	    </div>
        
                    <div id="d0" style="display:block;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Aquarius_icon.gif" alt="Aquarius" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aquarius" title="Aquarius" alt="Aquarius" data-track="outbound,home,horoscope-aquarius">Aquarius</a></h5>
                           <p>Something at home may have stirred up your emotions. You may need to find a creative or fun outlet to let go of inner tensions....<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aquarius" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-aquarius">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d1" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Aries_icon.gif" alt="Aries" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aries" title="Aries" alt="Aries" data-track="outbound,home,horoscope-aries">Aries</a></h5>
                           <p>You may find you are in a chatty mood and have a lot to say. There is a strong energy of excitement and you are in the mood to...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Aries" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-aries">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d2" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Cancer_icon.gif" alt="Cancer" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Cancer" title="Cancer" alt="Cancer" data-track="outbound,home,horoscope-cancer">Cancer</a></h5>
                           <p>You may be in the midst of people, meetings and other social obligations, but inwardly you may have the urge to escape and a need...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Cancer" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-cancer">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d3" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Capricorn_icon.gif" alt="Capricorn" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Capricorn" title="Capricorn" alt="Capricorn" data-track="outbound,home,horoscope-capricorn">Capricorn</a></h5>
                           <p>Things may be slightly fragmented as you may be stretched in so many directions. There may be technical problems or things may not...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Capricorn" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-capricorn">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d4" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Gemini_icon.gif" alt="Gemini" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Gemini" title="Gemini" alt="Gemini" data-track="outbound,home,horoscope-gemini">Gemini</a></h5>
                           <p>People may notice you today and are attracted to you. You have a magnetic energy that may draw attention. You are in a flirty and...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Gemini" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-gemini">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d5" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Leo_icon.gif" alt="Leo" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Leo" title="Leo" alt="Leo" data-track="outbound,home,horoscope-leo">Leo</a></h5>
                           <p>There is an undercurrent of excitement that could lead you to act or speak impulsively or jump into something too quickly. You...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Leo" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-leo">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d6" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Libra_icon.gif" alt="Libra" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Libra" title="Libra" alt="Libra" data-track="outbound,home,horoscope-libra">Libra</a></h5>
                           <p>Over the next few days you need to brace yourself for unexpected and unpredictable circumstances.  Simplify, stay centred and...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Libra" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-libra">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d7" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Pisces_icon.gif" alt="Pisces" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Pisces" title="Pisces" alt="Pisces" data-track="outbound,home,horoscope-pisces">Pisces</a></h5>
                           <p>Venus and the Moon are connected showering you with strong feelings of love and affection. There is an element of excitement and...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Pisces" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-pisces">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d8" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Sagittarius_icon.gif" alt="Sagittarius" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Sagittarius" title="Sagittarius" alt="Sagittarius" data-track="outbound,home,horoscope-sagittarius">Sagittarius</a></h5>
                           <p>There is an emphasis on partner, relating and connecting in a loving and affectionate way. The Gemini Moon and Gemini Venus add a...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Sagittarius" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-sagittarius">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d9" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Scorpio_icon.gif" alt="Scorpio" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Scorpio" title="Scorpio" alt="Scorpio" data-track="outbound,home,horoscope-scorpio">Scorpio</a></h5>
                           <p>The emphasis is on mental sharpness and nerves. Your intuition is sharp and it is important to connect to those “gut instincts” as...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Scorpio" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-scorpio">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d10" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Taurus_icon.gif" alt="Taurus" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Taurus" title="Taurus" alt="Taurus" data-track="outbound,home,horoscope-taurus">Taurus</a></h5>
                           <p>Comfort and indulgence are still top of the list. You have strong desires and needs and it may be hard to think clearly as your...<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Taurus" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-taurus">read more</a></p>                               	              
	                    </div>
	                 </div>
          
                    <div id="d11" style="display:none;">
	                   <img src="http://static.24.co.za/5/images/lazy/65x65.jpg" class="left" data-src="http://www.women24.com/Images/icons/starsigns/Virgo_icon.gif" alt="Virgo" />
	                    <div class="item relative">
                           <h5><a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Virgo" title="Virgo" alt="Virgo" data-track="outbound,home,horoscope-virgo">Virgo</a></h5>
                           <p>The research that you have been working on may be needed in your working environment today....<a href="http://www.women24.com/BooksAndAstrology/Astrology/DailyHoroscope/Virgo" class="readmore" alt="...read more" title="...read more" data-track="outbound,home,horoscope-virgo">read more</a></p>                               	              
	                    </div>
	                 </div>
          
	</div>
    <div class="perfect_match">
        <a href="http://love2meet.news24.com/" data-track="outbound,home,horoscope-love2meet.news24.com">Who’s your perfect match?<br />
<span>Click here to find out!</span></a>
    </div>
</div>


<script type="text/javascript">
    function toggleSubmit(obj) { count = 0; while (document.getElementById("d" + count)) { document.getElementById("d" + count).style.display = "none"; count++ } document.getElementById("d" + obj.selectedIndex).style.display = "block" } var date = new Date; var day = date.getDate(); var month = date.getMonth(); var currentZodiac; switch (month) { case 0: { if (day >= 20) currentZodiac = "aquarius"; else currentZodiac = "sagittarius"; break }; case 1: { if (day >= 19) currentZodiac = "pisces"; else currentZodiac = "aquarius"; break }; case 2: { if (day >= 21) currentZodiac = "aries"; else currentZodiac = "pisces"; break }; case 3: { if (day >= 21) currentZodiac = "taurus"; else currentZodiac = "aries"; break }; case 4: { if (day >= 21) currentZodiac = "gemini"; else currentZodiac = "taurus"; break }; case 5: { if (day >= 21) currentZodiac = "cancer"; else currentZodiac = "gemini"; break }; case 6: { if (day >= 22) currentZodiac = "leo"; else currentZodiac = "cancer"; break }; case 7: { if (day >= 22) currentZodiac = "virgo"; else currentZodiac = "leo"; break }; case 8: { if (day >= 22) currentZodiac = "libra"; else currentZodiac = "virgo"; break }; case 9: { if (day >= 23) currentZodiac = "scorpio"; else currentZodiac = "libra"; break }; case 10: { if (day >= 22) currentZodiac = "sagittarius"; else currentZodiac = "scorpio"; break }; case 11: { if (day >= 21) currentZodiac = "capricorn"; else currentZodiac = "sagittarius"; break } } $j(".zodiac #ptype").val(currentZodiac); toggleSubmit($j(".zodiac #ptype")[0])</script>
    <div class="spacer clr">
        </div>
    <div class="col299 relative endcolumn">
        </div>

            </div>
            <div class="spacer clr white"></div>
        </div>
        <div id="footer" class="relative clr">
                       
            

<div class="clr10 clr">&nbsp;</div>
<div id="divServices" class="services left">
  <h3 class="bold">services</h3>
  
      <div class="item left">
        <a href="http://www.news24.com/Newsletters" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/167/3d5262fc76764b0abd11667baf454f84.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/Newsletters" target="_top">E-mail Alerts</a></strong>
        The latest headlines in your inbox 
        </p>
      </div>
    
      <div class="item left">
        <a href="http://www.news24.com/SiteElements/Services/News24-RSS-Feeds-20111202-2" target="_self"><img src="http://cdn.24.co.za/files/Cms/General/d/495/7125197ea74a4880879e2bd187f630c9.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/SiteElements/Services/News24-RSS-Feeds-20111202-2" target="_self">RSS feeds</a></strong>
        News delivered really simply.
        </p>
      </div>
    
      <div class="item left">
        <a href="http://m.news24.com/news24" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/167/decc890f19a644579a0c033e19edbc40.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://m.news24.com/news24" target="_top">Mobile</a></strong>
        News24 on your mobile or PDA
        </p>
      </div>
    
      <div class="item left last">
        <a href="http://www.news24.com/Newsletters" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/167/432cbe0789a040e9ae3627685a099a0e.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/Newsletters" target="_top">E-mail Newsletters</a></strong>
        You choose what you want 
        </p>
      </div>
    
      <div class="item left">
        <a href="http://www.news24.com/xArchive/News24/Get-News24-on-your-iPhone-20090428" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/495/e2ae1ce7a6c74cd19e793cb31873a54e.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://www.news24.com/xArchive/News24/Get-News24-on-your-iPhone-20090428" target="_top">News24 on your iPhone</a></strong>
        Get News24 headlines on your iPhone.
        </p>
      </div>
    
      <div class="item left">
        <a href="http://mobile.24.com/?p=minisite_news" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/168/7c086371afe44063bfadd3ff26fde57d.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://mobile.24.com/?p=minisite_news" target="_top">SMS Alerts</a></strong>
        Get breaking news stories via SMS.
        </p>
      </div>
    
      <div class="item left">
        <a href="http://blogs.24.com/" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/168/4a134cf303084f35bec18b1262fecf3e.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://blogs.24.com/" target="_top">Blogs</a></strong>
        Your opinion on you, me and everyone. 

        </p>
      </div>
    
      <div class="item left last">
        <a href="http://opencalais.com/" target="_top"><img src="http://cdn.24.co.za/files/Cms/General/d/175/09ea1738b1764dca88d3100f383052c1.png" class="left" width="42" height="42" /></a>
        <p><strong class="block bold"><a href="http://opencalais.com/" target="_top">Calais</a></strong>
        Website keywords automated by OpenCalais.
        </p>
      </div>
    
</div>
<div class="clr">&nbsp;</div>
            

<div id="footernav" class="relative">
  	<a href="http://www.24.com" class="absolute logo24"><img class="absolute logo24" width="56" height="42" src="http://static.24.co.za/5/images/24com_logo.png"/></a>
	<a href="http://www.iabsa.net/" class="absolute dmma" title="Interactive Advertising Bureau" target="_blank"><img src="http://static.24.co.za/5/images/iablogo.png" width="71" height="50" alt="Interactive Advertising Bureau" border="0" class="absolute dmma" /></a>
	
    <div class="copy absolute">
	    <ul>
	        
		            <li><a href="http://www.news24.com/search">Search</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/SiteElements/Footer/About-Us-20090703-4">About Us</a> ·</li>  
	            
		            <li><a href="http://www.thespacestation.co.za/channel/news24/">Advertise on News24</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/SiteElements/Services/Terms-and-Conditions-20120413">Terms & Conditions</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/PressReleases">Press Releases</a> ·</li>  
	            
		            <li><a href="http://www.news24.com/Jobs/">Jobs at News24</a> ·</li>  
	            
            <li><a id="lnkFooterContactUs" class="group" href="http://www.news24.com/FeedBack.aspx?iframe" class="footerLink">Contact us</a></li>
        </ul>
        <div class="clr10 clr">&nbsp;</div>
        
        &copy; 2014 24.com. All rights reserved.
    </div>
 
</div>

        </div>
        <div class="clr white"></div>
    </div>

            

<div id="socialbarHPStories">
    <div id="socialbar-newstories" class="bottom">
        <span onclick="HPRedirect('http://www.news24.com/');">There are&nbsp;<strong>new stories</strong>&nbsp;on the homepage. Click here to see them.</span>
        <div id="close" onclick=" CloseNewStoriesPopup(); ">&nbsp;</div>
        <div class="arrow"></div>
    </div>
</div>
            <div id="retail_ad_spacer"></div> 
        </div>
        <div id='ad-1000x1000-1' class='24ad1000x1000'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('1000x1000','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=1000x1000&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=1000x1000&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
        <div id='ad-20x20-1' class='24ad20x20'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('20x20','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=20x20&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=20x20&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
        <div id="ad300bottom">
            <div id='ad-980x415-1' class='24ad980x415'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('980x415','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=980x415&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=980x415&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
        </div>
        <div class="clr"></div>
    

<script type="text/javascript">
//<![CDATA[
var gotravelCount=5;//]]>
</script>

<div id="CmsStats" style="z-index:-1; visibility:hidden;">
<script type="text/javascript" language="JavaScript" >
var cmsStatsImage = new Image();
cmsStatsImage.src = "http://stats.24.com/content/image.articleview?rnd=635392200724189615&s=5&c=1059&a=1370d9df-3a3f-4eed-9c29-a3d036173ac4&t=%27House+of+horrors%27+wife+appears+in+court&ct=SouthAfrica/News&u=http%3a%2f%2fwww.news24.com%2fSouthAfrica%2fNews%2fHouse-of-horrors-wife-appears-in-court-20140624&uid=&luid=&sn=";
</script>
<noscript>
<img src="http://stats.24.com/content/image.articleview?rnd=635392200724189615&s=5&c=1059&a=1370d9df-3a3f-4eed-9c29-a3d036173ac4&t=%27House+of+horrors%27+wife+appears+in+court&ct=SouthAfrica/News&u=http%3a%2f%2fwww.news24.com%2fSouthAfrica%2fNews%2fHouse-of-horrors-wife-appears-in-court-20140624&uid=&luid=&sn=" alt=""/>
</noscript>
</div>

<script type="text/javascript">
//<![CDATA[
var _virtualPath = 'http://www.news24.com/';//]]>
</script>
</form>
    
    



    <div class="personalisationContainer">
        <div class="personalisationNav">
            <div class="topNavWrapper">
                <div class="left bold headerLinks">
                    <span id="site_languages_dropdown"><a href="http://www.news24.com" data-track="outbound,topbar,news24.com" class="deepblue bold">News24</a></span>
                </div>
                <div class="site_languages">
                    <div style="color: #848484;">
                        English</div>
                    <div style="margin-top: 10px;">
                        <a href="http://afrikaans.news24.com">Afrikaans</a></div>
                    <div style="margin-top: 10px;">
                        <a href="http://isizulu.news24.com">isiZulu</a></div>
                </div>
                <div class="bold headerLinks left" style="margin-left:5px;">
                    <span class="grey">|&nbsp;&nbsp;<a href="http://www.olx.co.za" data-track="outbound,topbar,olx.co.za" class="grey bold">OLX</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://www.pricecheck.co.za/" data-track="outbound,topbar,pricecheck.co.za" class="grey bold">PriceCheck</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://www.property24.com" data-track="outbound,topbar,property24.com" class="grey bold">Property24</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://etrader.kalahari.com/referral.asp?linkid=7002&partnerid=9180" data-track="outbound,topbar,kalahari.com" class="grey bold">Kalahari.com</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://www.careers24.com" data-track="outbound,topbar,careers24.com" class="grey bold">Careers24</a></span>
                </div>
            </div>
            

<script type="text/javascript">
    function CheckUsernameAvailable() { var a = $j("#txtUsername").val(); var b = new RegExp("^[a-zA-Z0-9-_]*$"); if (!a == "") { if (!a.match(b)) $j("#originalHeader").fadeOut("fast", function () { $j("#headerUsernameError").html("Your username may not contain any spaces or special characters.").fadeIn("fast") }); else news24.getAjax("/Ajax/UgcData/", "CheckUsernameAvailability", { 'username': a }, CheckUsernameAvailableCallback) } else $j("#originalHeader").fadeOut("fast", function () { $j("#headerUsernameError").html('Please enter a username and then click "Register"').fadeIn("fast") }) } function CheckUsernameAvailableCallback(a) { if (!a.error && a != "error") { if (a == true) { $j("#enterUsernameDiv").fadeOut("fast", function () { $j("#spanNewUsername").html($j("#txtUsername").val()); $j("#txtDisplayName").val($j("#txtUsername").val()); $j("#personaliseProfileDiv").fadeIn("fast") }) } else $j("#originalHeader").fadeOut("fast", function () { $j("#headerUsernameError").html("Sorry, that username is not available").fadeIn("fast") }) } } function ResetAvatar() { $j.ajax({ url: "/AvatarRemove.axd?filename=" + $j("#avatarImage").attr("src"), type: "POST" }); $j("#avatarImage").attr("src", user.avatarUrl); $j("#btnResetAvatar").fadeOut() } function SaveUserProfile() {$j("#displayNameError").fadeOut("fast"); $j("#profileSaveError").fadeOut("fast"); var a = true; var b = escape($j("#txtDisplayName").val()); user.bio = escape($j("#txtAboutMe").val()); user.avatarUrl = $j("#avatarImage").attr("src"); user.name = escape($j("#txtUsername").val()); if (b == "") { a = false; $j("#displayNameError").fadeIn("fast") } else user.displayName = b; if (a) { $j("#personaliseProfileDiv").fadeOut("fast"); $j(".saveProfile").fadeIn("fast"); var data = JSON.stringify({ userSettings: user }); news24.getAjax("/Ajax/UgcData/", "SaveTinaProfile", data, SaveUserProfileCallback, null, "POST") }} function SaveUserProfileCallback(a) { if (!a.error && a.value != "error") { if (a.value === "upload") { $j(".saveProfile").fadeOut("fast"); $j("#personaliseProfileDiv").fadeIn("fast"); $j("a.call2action").click(); user.referrer = "" } else { $j("#fancybox-close").click(); location.reload(true) } } else { $j(".saveProfile").fadeOut("fast"); $j("#personaliseProfileDiv").fadeIn("fast"); $j("#profileSaveError").fadeIn("fast") } } function CheckCharacterCount(a) { a = a || window.event; var b = a.keyCode; if (b == 8 || b == 46) return true; else if ($j("#txtAboutMe").val().length < 1e3) return true; else return false } var user = { name: "", displayName: "", userid: "", avatarUrl: "", bio: "", referrer: "" }; var hasProfile = ""; $j(document).ready(function () { $j("#createProfileFire").fancybox({ padding: 0, centerOnScroll: true }); var a = $j("#btnUploadAvatar"); var b = $j("#avatarError"); new AjaxUpload(a, { action: "/AvatarUpload.axd", name: "uploadfile", data: { userid: user.userid }, onSubmit: function (a, c) { if (!(c && /^(jpg|png|jpeg|gif)$/.test(c))) { b.html("Only JPG, PNG or GIF files are allowed").fadeIn(); return false } b.html("Uploading...").fadeIn() }, onComplete: function (a, c) { b.html(""); if (!c.error) { var d = $j($j(c)[1]).html(); if (d != "error") { user.avatarUrl = $j("#avatarImage").attr("src"); $j("#avatarImage").attr("src", d); b.fadeOut().html(""); $j("#btnResetAvatar").fadeIn() } else b.html("* The image you selected could not be uploaded.").fadeIn() } else b.html("* The image you selected could not be uploaded.").fadeIn() } }); if (hasProfile == "true") { $j("#enterUsernameDiv").hide(); $j("#spanNewUsername").html(unescape(user.name)); $j("#txtDisplayName").val(unescape(user.displayName)); $j("#txtAboutMe").val(unescape(user.bio)); $j("#personaliseProfileDiv").show() } })
</script>

<a id="createProfileFire" style="display:none;" href="#createProfileModal">&nbsp;</a>
<input type="hidden" name="userid" value="" />
<div style="display:none;">
    <div id="createProfileModal">
        <div id="enterUsernameDiv">
            <div class="userheader"><h2>Hello&nbsp;<strong></strong></h2></div>
            <div class="step1_content">
                <h3>Create Profile</h3>
                 <p>Creating your profile will enable you to submit photos and stories to get published on News24.</p><br />
                <h3 id="originalHeader">Please provide a username for your profile page:</h3>
                <h3 id="headerUsernameError" style="display:none"></h3>
                <p>This username must be unique, cannot be edited and will be used in the URL to your profile page across the entire 24.com network.</p>
                <div class="formborder">
                    <input type="text" id="txtUsername" class="username_form" />
                </div>
            </div>
            <div class="reg_btn2"><input type="button" id="btnRegister" value="Register" onclick="CheckUsernameAvailable();" /></div>
        </div>
        <div id="personaliseProfileDiv" style="display:none;">
            <div class="userheader"><h2>Hello&nbsp;<strong><span id="spanNewUsername"></span></strong></h2></div>
            <div class="step2_content">
                <h3>Choose a display name:</h3>
                <div class="formborder">
                    <input type="text" id="txtDisplayName" />
                </div>
                <span id="displayNameError" >* You must provide a display name.</span>
                <h3>Edit your avatar:</h3>
                <div class="changeprofile">
                    <img id="avatarImage" height="35" width="35" />
                    <span class="selectp_img">Select an image file on your computer (max 4MB):</span>
                    <input type="button" id="btnUploadAvatar" value="Upload" />
                    <input type="button" id="btnResetAvatar" value="Reset" onclick="ResetAvatar();"  style="display:none;"/>
                    <span id="avatarError">* The image you selected could not be uploaded.</span>
                </div>
                <h3>Tell us a bit about yourself:</h3>
                <textarea id="txtAboutMe" cols="55" rows="6" onkeydown="return CheckCharacterCount(event);"></textarea>
                <div id="profileSaveError" style="color:Red;font-size:12px;display:none;">* Your profile could not be saved at the moment. Please try again later.</div>
            </div>
            <div class="reg_btn"><input type="button" id="btnSaveUserProfile" value="Save" onclick="SaveUserProfile();" /></div>
        </div>
        <div class="saveProfile" style="text-align:center;display:none;">
            <div style="height:170px;">&nbsp;</div>
            <div style="height:40px;">
                <h3 style="font-weight:bold;font-size: 20px;">Saving your profile</h3>
                <img src="http://static.24.co.za/5/images/ajax-loader-bar.gif" />
            </div>
            <div style="height:170px;">&nbsp;</div>
        </div>
    </div>
</div>
            
<div id="toppanel">
    <div class="tab right">
        
        <div id="pnlLoggedOut">
	
            <ul class="loggedOut">
                <li id="togglePanel" class="logout"><a id="openPanel" class="point_down" href="javascript:void(0);">Login / SignUp</a> <a id="closePanel" style="display: none;" class="point_up" href="#">Login / SignUp</a> </li>
            </ul>
        
</div>
    </div>
    <div id="pnlSettings">
	
        <div id="panel">
            <div class="content">
                <h1 class="bold">
                    Settings</h1>
                
                <div id="divModalContent">
                    <div class="info">
                        <a href="#" class="name">Location Settings</a><br />
                        <p>
                            News24 allows you to edit the display of certain components based on a location.
                            If you wish to personalise the page based on your preferences, please select a
                            location for each component and click "Submit" in order for the changes to
                            take affect.</p>
                    </div>
                    <div class="info left">
                        <div class="left selectBox">
                            <label>
                                Most Read Block</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selUserLocation" id="selUserLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="capetown">Cape Town</option>
		<option value="george">George</option>
		<option value="johannesburg">Johannesburg</option>
		<option value="pretoria">Pretoria</option>
		<option value="eastlondon">East London</option>
		<option value="portelizabeth">Port Elizabeth</option>
		<option value="bloemfontein">Bloemfontein</option>
		<option value="durban">Durban</option>
		<option value="pietermaritzburg">Pietermaritzburg</option>
		<option value="polokwane">Polokwane</option>
		<option value="nelspruit">Mbombela</option>
		<option value="kimberley">Kimberley</option>
		<option value="mafikeng">Mahikeng</option>
	</select>
                            <span id="userLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Weather</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selWeatherLocation" id="selWeatherLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="capetown">Cape Town</option>
		<option value="george">George</option>
		<option value="johannesburg">Johannesburg</option>
		<option value="pretoria">Pretoria</option>
		<option value="eastlondon">East London</option>
		<option value="portelizabeth">Port Elizabeth</option>
		<option value="bloemfontein">Bloemfontein</option>
		<option value="durban">Durban</option>
		<option value="pietermaritzburg">Pietermaritzburg</option>
		<option value="polokwane">Polokwane</option>
		<option value="nelspruit">Mbombela</option>
		<option value="kimberley">Kimberley</option>
		<option value="mafikeng">Mahikeng</option>
	</select>
                            <span id="weatherLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Traffic</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selTrafficLocation" id="selTrafficLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="western cape">Western Cape</option>
		<option value="gauteng">Gauteng</option>
		<option value="eastern cape">Eastern Cape</option>
		<option value="free state">Free State</option>
		<option value="kwazulu-natal">KwaZulu-Natal</option>
		<option value="limpopo">Limpopo</option>
		<option value="mpumalanga">Mpumalanga</option>
		<option value="northern cape">Northern Cape</option>
		<option value="north-west">North-West</option>
	</select>
                            <span id="trafficLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Jobs</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selJobLocation" id="selJobLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="western cape">Western Cape</option>
		<option value="gauteng">Gauteng</option>
		<option value="eastern cape">Eastern Cape</option>
		<option value="free state">Free State</option>
		<option value="kwazulu-natal">KwaZulu-Natal</option>
		<option value="limpopo">Limpopo</option>
		<option value="mpumalanga">Mpumalanga</option>
		<option value="northern cape">Northern Cape</option>
		<option value="north-west">North-West</option>
	</select>
                            <span id="careersLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Property Listings</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selPropertyLocation" id="selPropertyLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="western cape">Western Cape</option>
		<option value="gauteng">Gauteng</option>
		<option value="eastern cape">Eastern Cape</option>
		<option value="free state">Free State</option>
		<option value="kwazulu-natal">KwaZulu-Natal</option>
		<option value="limpopo">Limpopo</option>
		<option value="mpumalanga">Mpumalanga</option>
		<option value="northern cape">Northern Cape</option>
		<option value="north-west">North-West</option>
	</select>
                            <span id="propertyLocationError" style="display: none; color: Red;">*</span>
                        </div>
                        <div class="left selectBox">
                            <label>
                                Kalahari Listings</label><br />
                            <select name="ctl00$ctl00$personalisationMenu$selKalahariLocation" id="selKalahariLocation" class="location" orig="2">
		<option value="">Change your location</option>
		<option value="default">National</option>
		<option selected="selected" value="capetown">Cape Town</option>
		<option value="george">George</option>
		<option value="johannesburg">Johannesburg</option>
		<option value="pretoria">Pretoria</option>
		<option value="eastlondon">East London</option>
		<option value="portelizabeth">Port Elizabeth</option>
		<option value="bloemfontein">Bloemfontein</option>
		<option value="durban">Durban</option>
		<option value="pietermaritzburg">Pietermaritzburg</option>
		<option value="polokwane">Polokwane</option>
		<option value="nelspruit">Mbombela</option>
		<option value="kimberley">Kimberley</option>
		<option value="mafikeng">Mahikeng</option>
	</select>
                            <span id="kalahariLocationError" style="display: none; color: Red;">*</span>
                            <p id="errorMessage" style="display: none; color: Red;">
                                Please select a value from the drop down box.</p>
                        </div>
                        <br />
                        <div class="left" style="clear:both;">
                            <input id="btCloseSettings" type="button" name="submit" value="Close" class="bt_login" />
                            <input id="bntSaveLocations" type="button" name="submit" value="Save" class="bt_login" />
                        </div>
                    </div>
                </div>
                <div id="savingSettings" style="display: none;">
                    <div class="info" style="margin-top: 95px; text-align: center;">
                        <h3 style="font-weight: bold; font-size: 20px; margin-bottom: 20px;">
                            Saving your settings</h3>
                        <img src="http://static.24.co.za/5/images/ajax-loader-bar.gif"  />
                    </div>
                </div>
            </div>
        </div>
        <!-- /login -->
    
</div>
    <div id="logoutPanel">
        <div class="content">
            <h1 class="bold">
                Facebook Sign-In</h1>
            <div>
                <div class="info">
                    <p>
                        <strong>Hi News addict,</strong>
                    </p>
                    <p>
                        Join the News24 Community to be involved in breaking the news.
                    </p>
                    <p>
                        Log in with Facebook to comment and personalise news, weather and listings.
                    </p>                
                    <div class="facebook_login">                          
                        <a href="javascript:void(0);" class="submit_button">
                            <img src="http://static.24.co.za/5/images/facebookicon_login.png" width="228" height="75" border="0" title="Login with your Facebook account" alt="Login with your Facebook account" /></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
    function setLocationDropdowns() { $j("#selUserLocation")[0].selectedIndex = $j("#selUserLocation").attr("orig"); $j("#selWeatherLocation")[0].selectedIndex = $j("#selWeatherLocation").attr("orig"); $j("#selTrafficLocation")[0].selectedIndex = $j("#selTrafficLocation").attr("orig"); $j("#selJobLocation")[0].selectedIndex = $j("#selJobLocation").attr("orig"); $j("#selPropertyLocation")[0].selectedIndex = $j("#selPropertyLocation").attr("orig"); $j("#selKalahariLocation")[0].selectedIndex = $j("#selKalahariLocation").attr("orig") } $j("#open").click(function () { $j("div#panel").slideDown("slow"); setLocationDropdowns() }); $j("#openPanel,#closePanel").click(function () { if ($j("div#logoutPanel").is(":visible")) { $j("div#logoutPanel").hide("fast") } else { $j("div#logoutPanel").slideDown("fast") } }); $j("#close,#btCloseSettings").click(function () { $j("div#panel").slideUp("fast"); setLocationDropdowns() }); $j("#toggle a,#btCloseSettings").click(function () { $j("#toggle a").toggle(); if ($j(".top_user_profile_edit").is(":visible")) { $j("#toppanel #lnkEditProfile").attr("class", "point_down"); $j(".top_user_profile_edit").hide() } }); $j("#togglePanel a").click(function () { $j("#togglePanel a").toggle() }); $j("#bntSaveLocations").click(function () { $j("#divModalContent").hide(); $j("#savingSettings").fadeIn("slow"); var a = "/Handlers/SaveLocations.ashx?"; a += "UserLocation=" + $j("#selUserLocation").val() + "&"; a += "WeatherLocation=" + $j("#selWeatherLocation").val() + "&"; a += "TrafficLocation=" + $j("#selTrafficLocation").val() + "&"; a += "JobLocation=" + $j("#selJobLocation").val() + "&"; + "&"; a += "PropertyLocation=" + $j("#selPropertyLocation").val() + "&"; a += "KalahariLocation=" + $j("#selKalahariLocation").val(); $j.ajax({ type: "GET", url: a, success: function (a) { if (a != "error") { location.reload(true) } } }); return false }); $j("#btnLogout").click(function () { window.location = "http://auth.news24.com/DeAuthenticate.aspx?surl=http://www.news24.com/SouthAfrica/News/House-of-horrors-wife-appears-in-court-20140624" }); $j("#toppanel li.user").click(function () { if ($j(".top_user_profile_edit").is(":visible")) $j("#toppanel #lnkEditProfile").attr("class", "point_down"); else $j("#toppanel #lnkEditProfile").attr("class", "point_up"); $j(".top_user_profile_edit").toggle(); $j("#toggle a.close").hide(); $j("#toggle a.open").show(); $j("div#panel").slideUp("fast"); setLocationDropdowns() });
</script>

            <div class="clr10">&nbsp;</div>
        </div>
    </div>
    
    
    <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/json/json2.js?v=20140620" ></script>
    <script type="text/javascript" language="javascript" src="http://scripts.24.co.za/libs/24com/tina/1.0/loginwindow.js?v=20140620" ></script>
    
    <script type="text/javascript" language="javascript" src="http://static.24.co.za/5/scripts/minified/basescript2.min.js?v=20140620" ></script>
    
    <script type="text/javascript">
        $j(document).ready(function () {$j("a.group,a.mynewspics").easyTooltip();});
        $j('.submit_button').click(function () { OpenTinaLoginWindow(); });
         function OpenTinaLoginWindow(permission) {
            json = { refreshPage: true, loginProvider: 'Facebook', tinaBaseUrl: 'http://auth.news24.com' };
            json.scope = this;
             if (permission)
                 json.permission = permission;
             Tina.openLoginWindow(json);
         }
        tinaUrl = 'http://auth.news24.com';
    </script>
    

    
        
<script type='text/javascript'>
    var SiteSection = window.location.pathname.replace(/^\/([^\/]*).*$/, '$1');
    if (SiteSection == "")
        SiteSection = "HomePage";
    var _sf_async_config = {}; _sf_async_config.uid = 8959; _sf_async_config.domain = "news24.com"; _sf_async_config.sections = SiteSection ; _sf_async_config.authors = "News24"; (function () { function a() { window._sf_endpt = (new Date).getTime(); var a = document.createElement("script"); a.setAttribute("language", "javascript"); a.setAttribute("type", "text/javascript"); a.setAttribute("src", ("https:" == document.location.protocol ? "https://a248.e.akamai.net/chartbeat.download.akamai.com/102508/" : "http://static.chartbeat.com/") + "js/chartbeat.js"); document.body.appendChild(a) } var b = window.onload; window.onload = typeof window.onload != "function" ? a : function () { b(); a() } })()
</script>
    <script type="text/javascript">
var idleInterval;var idleTime = 0;
$j(document).ready(function() {
if(!jQuery.cookie('closeidlead')){
idleInterval = setInterval("timerIncrement()", 1000); 
$j(this).mousemove(function(e) {idleTime = 0;});
$j(this).keypress(function(e) {idleTime = 0;});
$j(this).click(function (e) {idleTime = 0;});
}
});
function timerIncrement() {
idleTime = idleTime + 1;
if (idleTime == 1800) {
clearInterval(idleInterval);
GA24.trackEvent('IdleAd,open');
var popupUrl = '/IdlePopupPage.html?domain=' + document.domain + '&zone=' + za24_AdZone; 
$j("<a href='" + popupUrl + "'></a>" ).fancybox({'width':730,'height':508, 'type': 'iframe', 'padding': '0px', 'scrolling':'auto'}).click();
} 
}
</script>

    <div id='ad-200x400-1' class='24ad200x400'><script type='text/javascript'>if(typeof za24_DisplayAd != 'undefined') za24_DisplayAd('200x400','1');</script></div><noscript><a href='http://pubads.g.doubleclick.net/gampad/jump?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=200x400&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' target='_blank'><img src='http://pubads.g.doubleclick.net/gampad/ad?iu=/8900/24.com/Web/News24/SouthAfrica/Articles&sz=200x400&c=634586355&t=artid%3d1370d9df-3a3f-4eed-9c29-a3d036173ac4%26Places%3djohannesburg%26Topics%3dcrime%2cchild+abuse%26posno%3d1' border='0' alt=''></a></noscript>
</body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.news24.com/SouthAfrica/News/House-of-horrors-wife-appears-in-court-20140624'
        self.crawler.extract(doc, html)

        self.maxDiff = None

        self.assertEqual(doc.title, u"'House of horrors' wife appears in court")
        self.assertEqual(doc.summary, 'The wife of the man accused of abusing her and their five children and holding them captive has appeared in court, where her case was postponed for a bail application.')
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '24 06 2014')
        self.assertEqual(doc.author.name, "SAPA")
        self.assertEqual(doc.medium.name, 'News24')

        self.assertEqual(doc.text, u"""Johannesburg - The wife of the man accused of abusing her and their five children and holding them captive appeared in the Springs Magistrate's Court on Tuesday, Beeld reported.

The matter was postponed to 1 July for a formal bail application, according to the report.

She was arrested for defeating the ends of justice on Monday when she decided not to co-operate with police and reportedly refused to testify against her husband.

Magistrate Roy le Roux told the woman she was the second accused in the case.

In addition to defeating the ends of justice she faces the same charges as her husband - attempted murder, child abuse, and assault.

The woman's 36-year-old husband, who cannot be named to protect the identity of his family members, was arrested last month after allegedly assaulting his wife and five children and keeping them captive.

He was denied bail by the court earlier this month. His case was postponed to 25 July.

The man was arrested in May after his badly beaten 11-year-old son fled the family's house in Springs and ran to a neighbour to beg for help. The neighbour called police.

The man allegedly kept his wife and five children, aged between two and 16, captive in the house for several years and assaulted them.""")
