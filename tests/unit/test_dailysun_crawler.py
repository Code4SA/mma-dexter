# -*- coding: utf-8 -*-

import unittest

from dexter.models import Document, db
from dexter.models.seeds import seed_db
from dexter.processing.crawlers import DailysunCrawler

class TestTimesliveCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = DailysunCrawler()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_canonicalise_url(self):
        self.assertEqual(self.crawler.canonicalise_url(
            'http://www.dailysun.mobi/news/read/5227/cop-fiddles-and-wants-free-sex-shows-say-magoshas/'),
            'http://dailysun.mobi/news/read/5227/cop-fiddles-and-wants-free-sex-shows-say-magoshas')

    def test_extract(self):
        html = """

<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "http://www.wapforum.org/DTD/xhtml-mobile10.dtd"><html>
	<head>
		<meta http-equiv="expires" content="-1">
		<meta http-equiv="Cache-Control" content="no-cache">
		<meta http-equiv="Pragma" content="no-cache">
		<meta http-equiv="Content-type" content="text/html; charset=UTF-8" />
		<title>Daily Sun Mobi</title>
		<link rel="stylesheet" type="text/css" href="/mobile/cached/640x480/css/reset.css" />		<link rel="stylesheet" type="text/css" href="/mobile/cached/640x480/css/mobile/default.css" />				
	<link rel="stylesheet" type="text/css" href="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/css/70/default.css" />
	<link rel="stylesheet" type="text/css" href="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/css/70/touch.css" />
		
					<style type="text/css">
				body { width: 640px; margin: 0 auto; }
			</style>
		
		
                    <script type="text/javascript"><!--
                var xtkey=false;
                if(document.addEventListener){document.addEventListener('keydown',function(){xtkey=true},false);document.addEventListener('keyup',function(){xtkey=false},false);}
                else if(document.attachEvent){document.attachEvent('onkeydown',function(){xtkey=true});document.attachEvent('onkeyup',function(){xtkey=false});}
                function xt_click(obj,type,section,page,x1,x2,x3,x4,x5){var xtImg=new Image(),xtDate=new Date(),xtScr=window.screen,xtNav=window.navigator,xtObj=null;var xtSrc='http://logw310.ati-host.net/hit.xiti?s=xxxxxx&s2='+section+'&p='+page+((type=='F')?'':(type=='M')?'&a='+x1+'&m1='+x2+'&m2='+x3+'&m3='+x4+'&m4='+x5:'&clic='+x1)+'&hl='+xtDate.getHours()+'x'+xtDate.getMinutes()+'x'+xtDate.getSeconds();if(parseFloat(xtNav.appVersion)>=4){xtSrc+='&r='+xtScr.width+'x'+xtScr.height+'x'+xtScr.pixelDepth+'x'+xtScr.colorDepth;}xtImg.src=xtSrc;xtImg.onload=function(){xtImg.onload=null;};if(obj.nodeName!='A'){var xelp=obj.parentNode;while(xelp){if(xelp.nodeName=='A'){xtObj=xelp;break;}xelp=xelp.parentNode;}}
                    else{xtObj=obj;}if(xtObj){xtObj.target=xtObj.target||'_self';if(x2&&(type=='C')){xtObj.href=x2;if(x3){xtObj.target='_blank';}else{xtObj.target='_self';}}if(!xtkey){if(xtObj.target.toLowerCase()=='_self'){setTimeout('self.location.href="'+xtObj.href+'"',500);return false;}else
                    if(xtObj.target.toLowerCase()=='_top'){setTimeout('top.location.href="'+xtObj.href+'"',500);return false;}else
                    if(xtObj.target.toLowerCase()=='_parent'){setTimeout('parent.location.href="'+xtObj.href+'"',500);return false;}}}else
                    if(x2&&(type=='C')){if(x3){setTimeout('(window.open("'+x2+'","_blank")).focus();',500);}else{setTimeout('self.location.href="'+x2+'"',500);}}xtkey=false;return true;}
                //-->
            </script>
            	</head>
<body>
	
	<script type="text/javascript" src="/js/mobile/gears_init.js"></script>
	<script type="text/javascript" src="/js/mobile/xui.js"></script>
	<script type="text/javascript" src="/js/mobile/plugins.js"></script>
	<script type="text/javascript" src="/js/mobile/custom.js"></script>
	<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
	<script type="text/javascript" src="http://code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
	<div id="page-wrapper">
		<script type="text/javascript">
  			(function() {
 			   var em = document.createElement('script'); em.type = 'text/javascript'; em.async = true;
   			   em.src = ('https:' == document.location.protocol ? 'https://za-ssl' : 'http://za-cdn') + '.effectivemeasure.net/em.js';
   			   var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(em, s);
			  })();
		</script>
		<noscript>
			<img src="//za.effectivemeasure.net/em_image" alt="" style="position:absolute; left:-5px;" />
		</noscript>
		<img src="http://za.effectivemeasure.net/em_image" alt="" width="1" height="1" />
		<div id="page-header">
							<a href="/"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/uploads/70/headerImage.wide_469x180.jpg" alt="Daily Sun Mobi" style="height:auto;width: 100%;" width="469" height="180" /></a>
				&nbsp; &nbsp; <a href="/news" class="back"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_landbou/img/back_64x64.gif" alt="Go back a page" width="64" height="64" /></a>
					</div>

		<div class="advertisement"><div align="center" style="font-size:small;font-style:normal;font-weight:normal;margin-top:3px;margin-bottom:3px"><a href="http://googleads.g.doubleclick.net/aclk?sa=L&amp;ai=CSxz4D8Y6U_LaEIP38gOYtIGoAseBpvEEAAAQASC3pasdUNaQ9eEGYMfVhI6cJsgBA6kC8nRgMfhSeT7gAgCoAwGqBKoBT9D3fVmaV1p2t5JvS6oqhJ12LqQ8rS6wXeuPuzEI5FuZFPwvI7VtvzhMxgitSAMcCJxDaLBGiIOhYkGU2JUjJCtud4-lHDwsMpUExmxYcQoweIRTi_TIDrN3YQRlbO3yQXnvVZLnaFB8fLhCCoPIR3-OD6n7GMXHVO6thS_NHAuXl9tb0llN51QySyIqYF49uNncouHB0zNd1RahIyC7igrWHbFsrr9ua5XgBAGgBhQ&amp;num=0&amp;sig=AOD64_3g2QH96T0i7tuFVMk6gSzA-vkXkg&amp;client=ca-pub-6255253699155664&amp;adurl=http://cuddlykoala.telesure.yomohost.co.za/campaign.php%3Fid%3D3997" target="_blank"><img src="http://pagead2.googlesyndication.com/simgad/3508678514699156351" alt="" border="0" height="50" width="300"></a><br/></div></div>
		
		<div id="content-wrapper">
			
                                    <p class="align-center">You are not currently logged in, <a href="/login">Login</a> or <a href="/register">Register</a></p>
                                
            
<h1 class="iconized"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/news_63x61.gif" alt="" width="63" height="61" />News articles</h1><div class="filter"><form action="/news" id="readForm" method="post" accept-charset="utf-8"><div style="display:none;"><input type="hidden" name="_method" value="POST" /></div><table>    <td class="submit"> </td></tr><tr>	<td class="field"><select name="data[category]" id="category">
<option value="">All categories</option>
<option value="2">News</option>
<option value="1440">Entertainment</option>
</select></td>	<td class="submit"><input type="submit" value="GO" /></td>    </tr></table></form></div><div class="article-fullview item-fullview">
	<h2 class="sub-heading">Cop fiddles and wants free sex shows, say magoshas</h2>
		<p class="publish-date"><strong>Published:</strong> Tuesday, 2014/04/01</p>

								<div class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_mobile/remote/www.hermanustimes.co.za/uploads/ArticlePhotos/135330/622b79a3-a1df-48ec-910e-b81b40237bac_the20Magoshas4_330x240_B.jpg" alt="" style="max-width:95%;height:auto;" width="330" height="240" /></div>
			
	<p><strong>THE magoshas say he is a <br />cruel cop who seems to enjoy making their tough lives even tougher.</strong></p>
<p><em>He doesn’t bonk them but he pushes his fingers inside them, he takes their money and he beats them.</em></p>
<p>HE EVEN FORCES THEM TO OPEN THEIR LEGS SO HE CAN TAKE PICTURES OF THEIR PRIVATE PARTS.</p>
<p>The magoshas who work in Tembisa, Ekurhuleni agree that the cop, a section manager at Olifantsfontein cop shop in Midrand, does things to them because he likes to humiliate and hurt them.</p>
<div id="U300447188694JkC" class="text">
<div class="p">An angry magosha told <em class="i">Daily Sun </em>it is not an easy job.</div>
<div class="p">“We don’t lie on a comfortable bed with nice sheets. We do the business in the bushes and we get thorns in our backsides,” she said.</div>
<div class="p">“We want this cop to leave us alone. We want him to be arrested for this.”</div>
<div class="p">A 36-year-old magosha told <em class="i">Daily Sun </em>this same cop was on TV before for dragging a magosha on the ground and beating her. A case was opened but the women got no help from the cops.</div>
<div class="p">“When we go to the station they tell us to go away because we are stinking or they arrest us,” she said.</div>
<div class="p">The women aged between 23 and 58 come from different parts of the country and charge between R15 and R50 a time.</div>
<div class="p">But the perverted cop shows no mercy. He takes the little bit of money they earn for himself and if he is in a bad mood, the women get beaten and spend a night in jail.</div>
<div class="p">A gogo magosha (58) who is supposed to be on pension said they do this work because they need the money. “We don’t do this for fun. We have kids to feed,” she said.</div>
<div class="p">“Its very embarrassing for someone my age to be opening my legs for a pervert to have a look at my private parts.”</div>
<div class="p">The magoshas complain that the cop makes them pay “tax” because they don’t pay it to the government.</div>
<div class="p">On Friday some of the women were arrested and some allegedly beaten by the cop and his friends.</div>
<div class="p">“If you are unlucky enough to get caught, your clothes and your customer’s clothes get burnt and the customer has to pay a R1 500 fine,” said one of the women.</div>
<div class="p">The women said the cop wants to own them so they can work for him and pay him.</div>
<div class="p">“This man is making our lives impossible. We don’t work for him,” said a magosha.</div>
<div class="p"><span id="U300445860050UqF" class="span">)</span> Olifantsfontein Police Station’s Colonel John Mosowe said no law enforcement members are allowed to turn away complainants.</div>
<div class="p">“I have advised the ladies to open a case. This case and the one opened last year will be formally investigated,” he said.</div>
</div>
	<p class="meta">
		<strong>By:</strong> SIBONGILE MABENA	</p>
	
			<div class="actions" style="text-align: center;">
			<a href="/news/comments/5227/cop-fiddles-and-wants-free-sex-shows-say-magoshas"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/view-comments_288x46.gif" alt="View comments" style="max-width:49%;height:auto;" width="288" height="46" /></a>		
		<a href="/news/comments/add/5227/cop-fiddles-and-wants-free-sex-shows-say-magoshas"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/add-comment_288x46.gif" alt="Add comment" style="max-width:49%;height:auto;" width="288" height="46" /></a>	</div>	
	<div class="social-sharing">
<a href="/send-to-friend?u=http%3A%2F%2Fdailysun.mobi%2Fnews%2Fread%2F5227%2Fcop-fiddles-and-wants-free-sex-shows-say-magoshas&amp;n=Cop+fiddles+and+wants+free+sex+shows%2C+say+magoshas&amp;t=news+article&amp;r=%2Fnews%2Fread%2F5227%2Fcop-fiddles-and-wants-free-sex-shows-say-magoshas"><img src="/mobile/cached/640x480/img/social/email_82x34.gif" alt="Email to a friend" style="max-width:35%;height:auto;" onclick="return xt_click(this,&#039;C&#039;,&#039;2&#039;,&#039;E-Mail&#039;,&#039;S&#039;)" width="82" height="34" /></a>&nbsp;<a href="http://m.facebook.com/sharer.php?u=http%3A%2F%2Fdailysun.mobi%2Fnews%2Fread%2F5227%2Fcop-fiddles-and-wants-free-sex-shows-say-magoshas&amp;t=Cop+fiddles+and+wants+free+sex+shows%2C+say+magoshas"><img src="/mobile/cached/640x480/img/social/facebook_35x34.gif" alt="Share on Facebook" style="max-width:15%;height:auto;" onclick="return xt_click(this,&#039;C&#039;,&#039;2&#039;,&#039;Facebook&#039;,&#039;S&#039;)" width="35" height="34" /></a>&nbsp;<a href="http://mobile.twitter.com/home?status=Cop+fiddles+and+wants+free+sex+shows%2C+say+magoshas http%3A%2F%2Fdailysun.mobi%2Fnews%2Fread%2F5227%2Fcop-fiddles-and-wants-free-sex-shows-say-magoshas"><img src="/mobile/cached/640x480/img/social/twitter_35x34.gif" alt="Tweet this!" style="max-width:15%;height:auto;" onclick="return xt_click(this,&#039;C&#039;,&#039;2&#039;,&#039;Twitter&#039;,&#039;S&#039;)" width="35" height="34" /></a>&nbsp;<a href="http://m.delicious.com/save?v=5&amp;noui&amp;title=Cop+fiddles+and+wants+free+sex+shows%2C+say+magoshas&amp;url=http%3A%2F%2Fdailysun.mobi%2Fnews%2Fread%2F5227%2Fcop-fiddles-and-wants-free-sex-shows-say-magoshas"><img src="/mobile/cached/640x480/img/social/delicious_35x34.gif" alt="Share on Delicious" style="max-width:15%;height:auto;" onclick="return xt_click(this,&#039;C&#039;,&#039;2&#039;,&#039;Delicious&#039;,&#039;S&#039;)" width="35" height="34" /></a></div>

    
            <p class="align-right"><a href="/news/read/5225/anc-has-confidence-in-the-president">Read next article</a></p>
    
</div>

	<div class="main-navigation">
					<table>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/home_63x61.gif" alt="" width="63" height="61" /></td>
						<td><a href="/">Home</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/news_63x61.gif" alt="" width="63" height="61" /></td>
						<td><a href="/news">News</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_mobile/remote/netlocal.mobi/uploads/70/custom_pages/custom_page-12-1368010836-usgje0bs03_63x62.png" alt="" width="63" height="62" /></td>
						<td><a href="/custom/custom_pages/index/12">Sport</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_uploads/navigation/tournaments/logo_64x64.png" alt="" width="64" height="64" /></td>
						<td><a href="/tournaments">PSL &amp; Cups</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/weather_63x61.gif" alt="" width="63" height="61" /></td>
						<td><a href="/weather">Weather</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/multimedia_63x61.gif" alt="" width="63" height="61" /></td>
						<td><a href="/galleries-and-videos">Galleries &amp; videos</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_mobile/remote/netlocal.mobi/uploads/70/custom_pages/custom_page-8-1370169748-05evw98ao3_64x42.png" alt="" width="64" height="42" /></td>
						<td><a href="/custom/custom_pages/index/8">SunPower</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_mobile/remote/netlocal.mobi/uploads/70/custom_pages/custom_page-41-1370282431-pp2cfr7sa_64x64.jpg" alt="" width="64" height="64" /></td>
						<td><a href="/custom/custom_pages/index/41">SunStuff</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_mobile/remote/netlocal.mobi/uploads/70/custom_pages/custom_page-28-1370168552-m5ww6ix6sa_64x64.jpg" alt="" width="64" height="64" /></td>
						<td><a href="/custom/custom_pages/index/28">Horoscopes</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
									<tr>
						<td class="image"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_mobile/remote/netlocal.mobi/uploads/70/custom_pages/custom_page-25-1369745616-4u3kbmdybi_63x62.png" alt="" width="63" height="62" /></td>
						<td><a href="/custom/custom_pages/index/25">Contact Daily Sun</a></td>
													<td class="image more"><img src="/mobile/cached/640x480/mnt/webshare/app_webroot_theme/site_dailysun/img/navigation/more_64x64.gif" alt="" width="64" height="64" /></td>
											</tr>
							</table>
			</div>


<div class="secondary-navigation">
 <table>
		<tr class="netlocal-divider">
			<td class="image" style="text-align:left">
						<a href="http://www.facebook.com/sadailysun"><img src="/mobile/cached/640x480/img/social/facebook_35x34.gif" alt="Visit our Facebook Page" onclick="return xt_click(this,&#039;C&#039;,&#039;2&#039;,&#039;Facebook&#039;,&#039;S&#039;)" width="35" height="34" /></a>			<a href="http://www.twitter.com/dailysunsa"><img src="/mobile/cached/640x480/img/social/twitter_35x34.gif" alt="Tweet this!" onclick="return xt_click(this,&#039;C&#039;,&#039;2&#039;,&#039;Twitter&#039;,&#039;S&#039;)" width="35" height="34" /></a>						</td>
		</tr>
</table>
</div>		</div>

		
		<div id="page-footer">
			<div class="footer-navigation">

    <a href="/">Home</a> | <a href="/news">News</a> | <a href="/weather">Weather</a> | <a href="/galleries-and-videos">Galleries &amp; videos</a> | <a href="/contact-us">Contact us</a> | <a href="/terms">Terms</a> | <a href="/register">Register</a> | <a href="/login">Login</a> | <a href="http://netlocal.mobi/">Netlocal</a></div>			<p class="copyright">
								Copyright &copy; 2014 <em>Daily Sun Mobi</em>.			</p>
		</div>

		
					<div><img src="/img/ga.php?utmac=MO-40664933-1&amp;utmn=1037940373&amp;guid=ON&amp;utmr=-&amp;utmp=%2Fnews%2Fread%2F5227%2Fcop-fiddles-and-wants-free-sex-shows-say-magoshas" alt="" width="1" height="1" /></div>
			</div>

            <div id="AT-Tag">
            <script type="text/javascript">
                <!--
                xtpage = "";
                Xt_param = 's=538012&di=0&idclient=&p='+xtpage;
                xtn2 = "2";
                xt_multc = "";
                //all the xi indicators (like "&x1=...&x2=....&x3=...")
                xt_an = ""; //user ID
                xt_ac = ""; //category ID
                //do not modify below
                if(window.xtparam!=null){window.xtparam+="&s2="+xtn2+"&ac="+xt_ac+"&an="+xt_an+xt_multc;}else{window.xtparam="&s2="+xtn2+"&ac="+xt_ac+"&an="+xt_an+xt_multc;};
                if (window.xtparam!=null){Xt_param+=xtparam;}
                try {Xt_r = top.document.referrer;}
                catch(e) {Xt_r = document.referrer; }
                Xt_h = new Date();
                Xt_i = '<img width="1" height="1" src="http://logw310.ati-host.net/hit.xiti?'+Xt_param;
                Xt_i += '&hl='+Xt_h.getHours()+'x'+Xt_h.getMinutes()+'x'+Xt_h.getSeconds();
                if(parseFloat(navigator.appVersion)>=4)
                {Xt_s=screen;Xt_i+='&r='+Xt_s.width+'x'+Xt_s.height+'x'+Xt_s.pixelDepth+'x'+Xt_s.colorDepth;}
                document.write(Xt_i+'&ref='+Xt_r.replace(/[<>"]/g, '').replace(/&/g, '$')+'" >');
                //-->
            </script>
        </div>
        <noscript>
            <div id="xiti-logo-noscript">
                <img width="1" height="1" src="http://logw310.ati-host.net/hit.xiti?s=538012&amp;amp;s2=2&amp;amp;p=&amp;amp;idclient=&amp;amp;di=0&amp;amp;ac=&amp;amp;an=&amp;amp;" alt="WebAnalytics - AT Internet" />
            </div>
        </noscript>
    
    <!-- 152.111.196.43 -->

	</body>
</html>

"""
        
        doc = Document()
        doc.url = 'http://dailysun.mobi/news/read/5227/cop-fiddles-and-wants-free-sex-shows-say-magoshas'
        self.crawler.extract(doc, html)

        self.maxDiff = None

        self.assertEqual(doc.title, 'Cop fiddles and wants free sex shows, say magoshas')
        self.assertEqual(doc.summary, None)
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '01 04 2014')
        self.assertEqual(doc.author.name, 'SIBONGILE MABENA')
        self.assertEqual(doc.medium.name, 'Daily Sun')

        self.assertEqual(doc.text, u'THE magoshas say he is a cruel cop who seems to enjoy making their tough lives even tougher.\n\nHe doesn\u2019t bonk them but he pushes his fingers inside them, he takes their money and he beats them.\n\nHE EVEN FORCES THEM TO OPEN THEIR LEGS SO HE CAN TAKE PICTURES OF THEIR PRIVATE PARTS.\n\nThe magoshas who work in Tembisa, Ekurhuleni agree that the cop, a section manager at Olifantsfontein cop shop in Midrand, does things to them because he likes to humiliate and hurt them.')
        
