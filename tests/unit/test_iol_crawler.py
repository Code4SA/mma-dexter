# -*- coding: utf-8 -*-

import unittest

from dexter.models import Document, db
from dexter.models.seeds import seed_db
from dexter.processing.crawlers import IOLCrawler

class TestIOLCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = IOLCrawler()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_extract(self):
        html = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<!-- Start LegacyAppFragment name="Head" -->

	
		


<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />


<script type="text/javascript" src="/Scripts/mobile_detection.js">
</script>

<script type="text/javascript">
directToMobileSite();
</script>

<link rel="stylesheet" type="text/css" href="/css/atexStyle.css" />
<link rel="stylesheet" type="text/css" href="/css/iol_style.css" />
<link rel="stylesheet" type="text/css" href="/css/iol_layout_style.css" />
<link rel="stylesheet" type="text/css" href="/css/gallery_style.css" />
<link rel="stylesheet" type="text/css" href="/css/tn3.css" />
<link href='http://fonts.googleapis.com/css?family=Archivo+Black' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Oswald:400,700' rel='stylesheet' type='text/css'>
	
<script src="/Scripts/cufon-yui.js" type="text/javascript"></script>
<script src="/Scripts/Impact_400.font.js" type="text/javascript"></script>

<!-- include jQuery library -->
<script type="text/javascript" src="/Scripts/jquery.min.js"></script>
<!-- include tn3 plugin -->
<script type="text/javascript" src="/Scripts/jquery.tn3lite.min.js"></script>

<link rel="stylesheet" type="text/css" href="/Scripts/jquery.fancybox-1.3.1.css" media="screen" />

<!--[if IE 6]>
<link rel="stylesheet" type="text/css" href="css/iol_style_ie6.css" />
<![endif]-->

<link rel="shortcut icon" href="/images/iol_favicon.jpg" />	
	
  <link rel="stylesheet" type="text/css" href="http://www.iol.co.za/cmlink/style-7.10062">
  <link rel="stylesheet" type="text/css" href="http://www.iol.co.za/cmlink/motoring-style-7.3937">

  
        <link rel="alternate" type="application/rss+xml" title="Home Page RSS" href="http://www.iol.co.za/cmlink/home-page-rss-1.1538217" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="TV Box Teaser RSS" href="http://www.iol.co.za/cmlink/tv-box-teaser-rss-1.1537631" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Anene Booysen" href="http://www.iol.co.za/cmlink/anene-booysen-1.1468146" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Lance Armstrong Hot Topic feed" href="http://www.iol.co.za/cmlink/lance-armstrong-hot-topic-feed-1.1454231" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="US Elections 2012 RSS feed" href="http://www.iol.co.za/cmlink/us-elections-2012-rss-feed-1.1417822" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Malema RSS FEED" href="http://www.iol.co.za/cmlink/malema-rss-feed-1.1390238" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Dewani RSS feed" href="http://www.iol.co.za/cmlink/dewani-rss-feed-1.1376644" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Marikana feed" href="http://www.iol.co.za/cmlink/marikana-feed-1.1376639" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="News RSS Multimedia Videos Feed" href="http://www.iol.co.za/cmlink/news-rss-multimedia-videos-feed-1.1152520" />
        
        <link rel="alternate" type="application/rss+xml" title="News RSS Multimedia Galleries Feed" href="http://www.iol.co.za/cmlink/news-rss-multimedia-galleries-feed-1.1149195" />
        
        <link rel="alternate" type="application/rss+xml" title="Editors Pick Extended RSS" href="http://www.iol.co.za/cmlink/editors-pick-extended-rss-1.1137157" />
        
        <link rel="alternate" type="application/rss+xml" title="News Africa Extended" href="http://www.iol.co.za/cmlink/news-africa-extended-1.679216" />
        
        <link rel="alternate" type="application/rss+xml" title="Soccer Soccer Extended RSS" href="http://www.iol.co.za/cmlink/soccer-soccer-extended-rss-1.679215" />
        
        <link rel="alternate" type="application/rss+xml" title="Most Commmented Stories" href="http://www.iol.co.za/cmlink/most-commmented-stories-1.1625" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Most Viewed Stories" href="http://www.iol.co.za/cmlink/most-viewed-stories-1.1624" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Home Page Extended" href="http://www.iol.co.za/cmlink/home-page-extended-1.628986" />
        
        <link rel="alternate" type="application/rss+xml" title="Sport Extended" href="http://www.iol.co.za/cmlink/sport-extended-1.628987" />
        
        <link rel="alternate" type="application/rss+xml" title="Sport Rugby Extended" href="http://www.iol.co.za/cmlink/sport-rugby-extended-1.628988" />
        
        <link rel="alternate" type="application/rss+xml" title="Sport Cricket Extended" href="http://www.iol.co.za/cmlink/sport-cricket-extended-1.628989" />
        
        <link rel="alternate" type="application/rss+xml" title="News Back Page Extended" href="http://www.iol.co.za/cmlink/news-back-page-extended-1.628990" />
        
        <link rel="alternate" type="application/rss+xml" title="News South Africa Extended" href="http://www.iol.co.za/cmlink/news-south-africa-extended-1.679178" />
        
        <link rel="alternate" type="application/rss+xml" title="News World Extended" href="http://www.iol.co.za/cmlink/news-world-extended-1.679217" />
        
        <link rel="alternate" type="application/rss+xml" title="Sport Golf Extended" href="http://www.iol.co.za/cmlink/sport-golf-extended-1.679220" />
        
        <link rel="alternate" type="application/rss+xml" title="Western Cape Extended" href="http://www.iol.co.za/cmlink/western-cape-extended-1.679223" />
        
        <link rel="alternate" type="application/rss+xml" title="News Gauteng Extended" href="http://www.iol.co.za/cmlink/news-gauteng-extended-1.679235" />
        
        <link rel="alternate" type="application/rss+xml" title="News KwaZulu-Natal Extended" href="http://www.iol.co.za/cmlink/news-kwazulu-natal-extended-1.679236" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Video RSS" href="http://www.iol.co.za/cmlink/motoring-video-rss-1.1371016" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Pictures RSS" href="http://www.iol.co.za/cmlink/motoring-pictures-rss-1.1371011" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Extended RSS" href="http://www.iol.co.za/cmlink/motoring-extended-rss-1.1000700" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Category Extended RSS" href="http://www.iol.co.za/cmlink/motoring-category-extended-rss-1.832089" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Latest Launches Category Extended RSS" href="http://www.iol.co.za/cmlink/motoring-latest-launches-category-extended-rss-1.832096" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Road Tests Category Extended RSS" href="http://www.iol.co.za/cmlink/motoring-road-tests-category-extended-rss-1.832100" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring F1 Category Extended RSS" href="http://www.iol.co.za/cmlink/motoring-f1-category-extended-rss-1.832106" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Motorsport Category Extended RSS" href="http://www.iol.co.za/cmlink/motoring-motorsport-category-extended-rss-1.832108" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Bike Quads Karts Categpry Extended RSS" href="http://www.iol.co.za/cmlink/motoring-bike-quads-karts-categpry-extended-rss-1.832115" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring 4X4 Category Extended RSS" href="http://www.iol.co.za/cmlink/motoring-4x4-category-extended-rss-1.832117" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Speacial Features Category Extended RSS" href="http://www.iol.co.za/cmlink/motoring-speacial-features-category-extended-rss-1.832119" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Industry News Category RSS" href="http://www.iol.co.za/cmlink/motoring-industry-news-category-rss-1.832120" />
        
        <link rel="alternate" type="application/rss+xml" title="Motoring Bike Category Extended RSS" href="http://www.iol.co.za/cmlink/motoring-bike-category-extended-rss-1.875147" />
      

    <title>Cellphone crackdown - first busts - IOL Motoring Industry News | IOL.co.za</title>




<meta name="keywords" content="" />
<meta name="description" content="" />
<meta name="author" content="" />
<meta name="google-site-verification" content="YmiNpvzQrHdqXOi__ytAIEQM_vjpAQvum7AZW5rs1xE" /> 		
<meta http-equiv="expires" content="1396430054660" />
	

<script type="text/javascript" src="/Scripts/menu.js"></script>


  <script type="text/javascript">
    <!--
    function MM_showHideLayers() { //v9.0
      var i,p,v,obj,args=MM_showHideLayers.arguments;
      for (i=0; i<(args.length-2); i+=3) 
      with (document) if (getElementById && ((obj=getElementById(args[i]))!=null)) { v=args[i+2];
        if (obj.style) { obj=obj.style; v=(v=='show')?'visible':(v=='hide')?'hidden':v; }
        obj.visibility=v; } 
    }
    function MM_swapImgRestore() { //v3.0
      var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
    }
    function MM_preloadImages() { //v3.0
      var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
        var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
        if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
    }
    
    function MM_findObj(n, d) { //v4.01
      var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
        d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
      if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
      for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
      if(!x && d.getElementById) x=d.getElementById(n); return x;
    }
    
    function MM_swapImage() { //v3.0
      var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
       if ((x=MM_findObj(a[i]))!=null)
	   	{
		document.MM_sr[j++]=x;
		if(!x.oSrc) x.oSrc=x.src;
		x.src=a[i+2];
		}
    }
    //-->
  </script>
  
  
<!-- End LegacyAppFragment name="Head" -->	

        

      </head>
<body onload="MM_preloadImages('/images/multimedia_gal_prev2.jpg','/images/multimedia_gal_next2.jpg','/images/multimedia_gal_forward2.gif','/images/multimedia_gal_back2.gif','/images/a_tool_email_2.jpg','/images/a_tool_print_2.jpg','/images/pagination_prev_hov.jpg','/images/pagination_next_hov.jpg'); naming();  ">
    <div class="top-ad-wrapper">
	
		      
                  
    
      
                
<div id="top_container" align="center">

    	  
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4348952|0|225|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4348952|0|225|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4348952|0|225|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      	
</div>













          
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4348954|0|16|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4348954|0|16|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4348954|0|16|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
          
        
        
                        <!-- BEGIN EFFECTIVE MEASURE CODE -->
<!-- COPYRIGHT EFFECTIVE MEASURE -->
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
<!--END EFFECTIVE MEASURE CODE -->
      
      
      
  
      		      
                  
    
      
        
<div id="top_container" align="center">

    
</div>












  <div class="sponsored_links">
    <div class="sponsored_links_head"><p class="sponsored_link_head_text">Sponsored Links:</p></div>
    <div class="sponsored_links_cont">  
      <ul class="sponsored_link_cont">
        		  <li>
			    <a href="http://www.ioldeals.co.za/"  target='_blank' style="margin: 0px 0px 0px 5px;">IOL Deals</a>
		  </li>
				  <li>
			    <a href="http://www.iolproperty.co.za/"  target='_blank' style="margin: 0px 0px 0px 5px;">IOL Property</a>
		  </li>
				  <li>
			    <a href="http://www.ioldating.co.za"  target='_blank' style="margin: 0px 0px 0px 5px;">IOL Dating</a>
		  </li>
				  <li>
			    <a href="http://www.wegotads.co.za"  target='_blank' style="margin: 0px 0px 0px 5px;">WeGotAds</a>
		  </li>
				  <li>
			    <a href="http://www.ioljobs.co.za/"  target='_blank' style="margin: 0px 0px 0px 5px;">IOL Jobs</a>
		  </li>
		      </ul>
    </div>
  </div>

      
  
      		
  </div>
		  <div id="wrapper">
			<div id="masthead" class="masthead">
	          
                  
    
      
          <div class="logo">
	<a href="http://www.iol.co.za:80/motoring" >
              






                   <img title='' height='69' style='' alt='IOL_motoring2' width='312' class='pics' src='/polopoly_fs/iol-motoring2-1.989389!/image/1252442279.png_gen/derivatives/absolute/1252442279.png' />    	  	</a>
  </div>

  

          
        <div class="search_box">
<div id="cse-search-form" style="width: 300px;float: left">Loading</div>
<script src="http://www.google.com/jsapi" type="text/javascript"></script>
<script type="text/javascript"> 
  google.load('search', '1', {language : 'en', style : google.loader.themes.ESPRESSO});
  google.setOnLoadCallback(function() {
    var customSearchOptions = {};  var customSearchControl = new google.search.CustomSearchControl(
      'partner-pub-7576204233346138:2203392007', customSearchOptions);
    customSearchControl.setResultSetSize(google.search.Search.FILTERED_CSE_RESULTSET);
    var options = new google.search.DrawOptions();
    options.enableSearchboxOnly("http://www.iol.co.za/search-results-page");
    customSearchControl.draw('cse-search-form', options);
  }, true);
</script>
</div>

      
  
      	  	  <div class="clearing"></div>
    </div>

	
		<div id="navigation">
	          
                  
    
      
        


  	<div class="nav_home_sections">
      <div id="home_navigation">
        <p class="nav_home_text_sections">
		  <img src="/images/nav_logo.jpg" alt="IOL - logo" title="" class="nav_logo" />
		  <a href="/"  rel="nav_home_submenus">Home</a>
		</p>
      </div>
	  <div id="nav_home_submenus" class="tabcontent">
        <div class="nav_home_submenus">
	      	      <ul>
                	                                    	                                    	                             <li><a href="http://www.iol.co.za:80/news"  class=""  rel="navigation2226" >News</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/business"  class=""  rel="navigation2545" >Business</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/sport"  class=""  rel="navigation2228" >Sport</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring"  class=""  rel="navigation2572" >Motoring</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/tonight"  class=""  rel="navigation2901" >Tonight</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/lifestyle"  class=""  rel="navigation2227" >Lifestyle</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/travel"  class=""  rel="navigation2835" >Travel</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/scitech"  class=""  rel="navigation2750" >SciTech</a></li>
                      	                                    	                             <li><a href="http://www.iol.co.za:80/blogs"  class=""  rel="navigation2230" >Blogs</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/newspapers"  class=""  rel="navigation2231" >Newspapers</a></li>
                      	                                                	                				        	                 <li><a href="http://www.wegotads.co.za"  class=""  rel="navigation1620826"  target='_blank'>Classifieds</a></li>
                                  	                				        	                 <li><a href="http://www.iolproperty.co.za"  class=""  rel="navigation1620809"  target='_blank'>Property</a></li>
                                  	                				        	                 <li><a href="http://ioljobs.co.za/"  class=""  rel="navigation11578664"  target='_blank'>Jobs</a></li>
                      	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                            </ul>
    	    </div>
      </div>
	</div>
		      	      	      	      	      	            	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      				<div class="nav_links_sections">
      <div id="ddtabs3" class="solidblockmenu">
        	      <ul>
                	                             <li><a href="http://www.iol.co.za:80/motoring/latest-launches"  class=""  rel="navigation2573" >Latest Launches</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/road-tests"  class=""  rel="navigation2574" >Road Tests</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/f1-grand-prix"  class=""  rel="navigation2575" >F1 Grand Prix</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/motorsport"  class=""  rel="navigation2576" >Motorsport</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes-quads-karts"  class=""  rel="navigation2577" >Bikes , Quads & Karts</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/4-x-4"  class=""  rel="navigation2578" >4 X 4</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/special-features"  class=""  rel="navigation2579" >Special Features</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/industry-news"  class=""  rel="navigation2580" >Industry News</a></li>
                      	                                    	                            </ul>
    	  </div>	
	  	  	
                <div id="navigation2573" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation2574" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation2575" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation2576" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation2577" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation2578" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation2579" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation2580" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation2582" class="tabcontent">
        <div class="second_level_menu">
		              	      <ul>
                	                             <li><a href="http://www.iol.co.za:80/motoring/cars/alfa-romeo"  class=""  rel="navigation2588" >Alfa Romeo</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/aston-martin"  class=""  rel="navigation21965" >Aston Martin</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/audi"  class=""  rel="navigation2589" >Audi</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/bentley"  class=""  rel="navigation2590" >Bentley</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/bmw"  class=""  rel="navigation2591" >BMW</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/chrysler"  class=""  rel="navigation2592" >Chrysler</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/citroen"  class=""  rel="navigation2593" >Citroen</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/daimler"  class=""  rel="navigation2596" >Daimler</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/daihatsu"  class=""  rel="navigation2595" >Daihatsu</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/daewoo"  class=""  rel="navigation2594" >Daewoo</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/faw"  class=""  rel="navigation21966" >FAW</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/fiat"  class=""  rel="navigation2597" >Fiat</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/ford"  class=""  rel="navigation2598" >Ford</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/foton"  class=""  rel="navigation21967" >Foton</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/geely"  class=""  rel="navigation21968" >Geely</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/gwm"  class=""  rel="navigation21969" >GWM</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/honda"  class=""  rel="navigation2599" >Honda</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/hyundai"  class=""  rel="navigation2600" >Hyundai</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/infiniti"  class=""  rel="navigation21970" >Infiniti</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/isuzu"  class=""  rel="navigation2601" >Isuzu</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/jaguar"  class=""  rel="navigation2602" >Jaguar</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/jeep"  class=""  rel="navigation2603" >Jeep</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/jmc"  class=""  rel="navigation21971" >JMC</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/kia"  class=""  rel="navigation2604" >Kia</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/lamborghini"  class=""  rel="navigation21972" >Lamborghini</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/land-rover"  class=""  rel="navigation2605" >Land Rover</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/lexus"  class=""  rel="navigation2606" >Lexus</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/mazda"  class=""  rel="navigation2607" >Mazda</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/mclaren"  class=""  rel="navigation21973" >McLaren</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/mercedes"  class=""  rel="navigation2608" >Mercedes</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/mg"  class=""  rel="navigation2609" >MG</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/mini"  class=""  rel="navigation2610" >Mini</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/mitsubishi"  class=""  rel="navigation2611" >Mitsubishi</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/nissan"  class=""  rel="navigation2612" >Nissan</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/opel"  class=""  rel="navigation2613" >Opel</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/peugeot"  class=""  rel="navigation2614" >Peugeot</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/porsche"  class=""  rel="navigation2615" >Porsche</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/renault"  class=""  rel="navigation2616" >Renault</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/rolls-royce"  class=""  rel="navigation21974" >Rolls Royce</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/rover"  class=""  rel="navigation2617" >Rover</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/saab"  class=""  rel="navigation2618" >Saab</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/smart"  class=""  rel="navigation21975" >Smart</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/ssangyong"  class=""  rel="navigation2619" >SsangYong</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/subaru"  class=""  rel="navigation2620" >Subaru</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/suzuki"  class=""  rel="navigation2621" >Suzuki</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/toyota"  class=""  rel="navigation2622" >Toyota</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/volkswagen"  class=""  rel="navigation2623" >Volkswagen</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/volvo"  class=""  rel="navigation2624" >Volvo</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/other"  class=""  rel="navigation2625" >Other</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/chevrolet"  class=""  rel="navigation2626" >Chevrolet</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/tata"  class=""  rel="navigation2627" >Tata</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/mahindra"  class=""  rel="navigation2628" >Mahindra</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/ferrari"  class=""  rel="navigation2629" >Ferrari</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/dodge"  class=""  rel="navigation2630" >Dodge</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/lotus"  class=""  rel="navigation2631" >Lotus</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/proton"  class=""  rel="navigation2633" >Proton</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/seat"  class=""  rel="navigation2634" >Seat</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/hummer"  class=""  rel="navigation2635" >Hummer</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/cadillac"  class=""  rel="navigation2636" >Cadillac</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/chery"  class=""  rel="navigation2637" >Chery</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/cars/maserati"  class=""  rel="navigation2638" >Maserati</a></li>
              </ul>
    		          </div>
      </div>
          <div id="navigation2583" class="tabcontent">
        <div class="second_level_menu">
		              	      <ul>
                	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/aprilia"  class=""  rel="navigation2661" >Aprilia</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/bimota"  class=""  rel="navigation2660" >Bimota</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/bmw"  class=""  rel="navigation2659" >BMW</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/buell"  class=""  rel="navigation2658" >Buell</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/cagiva"  class=""  rel="navigation2657" >Cagiva</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/ducati"  class=""  rel="navigation2656" >Ducati</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/gilera"  class=""  rel="navigation2655" >Gilera</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/harley-davidson"  class=""  rel="navigation2654" >Harley Davidson</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/honda"  class=""  rel="navigation2653" >Honda</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/kawasaki"  class=""  rel="navigation2652" >Kawasaki</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/ktm"  class=""  rel="navigation2651" >KTM</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/kymco"  class=""  rel="navigation2650" >Kymco</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/laverda"  class=""  rel="navigation2649" >Laverda</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/moto-guzzi"  class=""  rel="navigation2648" >Moto Guzzi</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/other"  class=""  rel="navigation2647" >Other</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/sundiro"  class=""  rel="navigation2646" >Sundiro</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/suzuki"  class=""  rel="navigation2645" >Suzuki</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/triumph"  class=""  rel="navigation2644" >Triumph</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/vespa"  class=""  rel="navigation2643" >Vespa</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/yamaha"  class=""  rel="navigation2642" >Yamaha</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/loncin"  class=""  rel="navigation2641" >Loncin</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/hyosung"  class=""  rel="navigation2640" >Hyosung</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring/bikes/vuka"  class=""  rel="navigation2639" >Vuka</a></li>
              </ul>
    		          </div>
      </div>
            </div> 
			  		  		  		  		  		  		  		  				  		                		  		  		<div class="nav_add">
		        				      </div>
	<script type="text/javascript">
	  	    ddtabmenu.definemenu("ddtabs3", 7)
	      </script>
	<script type="text/javascript">
      ddtabmenu.definemenu("home_navigation")
    </script>
  


      
  
      	  	</div>
	
								<div id="nav_devider"></div>
		        	
		  <div id="col_1_2_3_container_sections">
		
	  	    	    <div id="col_1_2">
		              


	<img src='http://www.iol.co.za/logger/p.gif?a=1.1335083&amp;d=/2.225/2.572/2.580' alt='' />


          <div class="article-white">
      <h1 class="article_headers">Cellphone crackdown - first busts</h1>
      <p class="byline">
						  	              		    July 5 2012 at 02:10pm <br/>
		                   By Murray Williams
	          </p>
              <p class="comment_call_to_action"><a class="lrc_btm_text" href="#comments_start">Comment on this story</a></p>
            <hr />
	 
	  <div class="ctx_content">
<!-- C-ON-TEXT_CONTENT_START --> 

      <div id="article_container">
        <div class="aticle_column">
                      <div class="aticle_video">
        	                                <!-- Main Editorial Image -->
                    			      			                                      <img src="/polopoly_fs/iol-mot-pic-jul5-cell-phone-impoundment-1-1.1335082!/image/2802609312.jpg_gen/derivatives/box_300/2802609312.jpg" alt="IOL mot pic jul5 Cell phone impoundment 1" title=""  class="pics"/>
				  <p class="captions_credit_article">INLSA</p>
                  <p class="captions">Taxi driver Jean-Benoit Biyoko was caught talking on his phone while driving in Long Street. Picture: Henk Kruger</p>
                  <p class="captions"></p>
                                          </div>
                                <p class="related_articles">Related Stories</p>
			
</li>
			
			
            <ul class="menu_tab_lists_related">
        	  				
								
								<li><a class="related_articles" href="http://www.iol.co.za:80/motoring/industry-news/cellphone-use-it-you-ll-lose-it-1.1333846">Cellphone: Use it, you'll lose it!</a></li>
												
								
								<li><a class="related_articles" href="http://www.iol.co.za:80/news/south-africa/kwazulu-natal/kzn-drivers-could-also-lose-phones-1.1333884">KZN drivers could also lose phones</a></li>
								        	</ul>
                    
		  
		  
		  
		  
		  		  		  		    <!--PSTYLE=WT Web Text-->
<p class="arcticle_text">The first cellphone confiscation has taken place in Cape Town, as the new law was enforced for the first time. </p> 
					  		    
<p class="arcticle_text">As of today, drivers who are caught talking on their phones while driving, without headsets or hands-free kits, will have their handsets confiscated by traffic officers. </p> 
					  		    
<p class="arcticle_text">The first driver caught this morning was Jean-Benoit Biyoko, a taxi driver. Traffic officers nabbed him in Long Street in the CBD. </p> 
					  		    
<p class="arcticle_text">The traffic service's Maxine Jordaan reported: &ldquo;He didn't have a driving licence on him and he was taken to Gallows Hill traffic department. </p> 
					  		    
<p class="arcticle_text">&ldquo;His cellphone, a Nokia E63, had a SIM card and memory card in it, which he kept, and he kept his pouch too. </p> 
					  		    
<p class="arcticle_text"><strong>&ldquo;The gentleman was very co-operative and said he was sorry.&rdquo;</strong> </p> 
						  				  		        		    		  		    
<p class="arcticle_text">Jordaan said Biyoko had been fined R500 for talking on his cellphone while driving and would be permitted to collect his phone 24 hours after it was confiscated - on Friday morning. </p> 
					  		    
<p class="arcticle_text">The new City law was to be enforced across the city this afternoon, with officers from the undercover 'Ghost Squad', and other officers, deployed on major commuter routes. </p> 
					  		    
<p class="arcticle_text">Officers' vehicles will carry special boxes, in which confiscated phones will be placed once they have been logged and sealed in protective pouches. They will then be stored in the traffic department's safe at Gallows Hill. </p> 
					  		    
<p class="arcticle_text"><strong>No fee is required to reclaim a confiscated phone.</strong> </p> 
					  		    
<p class="arcticle_text">The bylaw was introduced by safety and security Mayco member JP Smith, who has received praise from across the country for the action against drivers who continue to flout the law. </p> 
					  		    
<p class="arcticle_text">Smith said camera and video evidence would be used whenever possible to back up officers' observations. </p> 
						  				  		        		    		  		    
<p class="arcticle_text">&ldquo;We're hoping that everybody will finally get the message, grab those hands-free kits and start using cellphones legally&rdquo;, Smith said. </p> 
					  		    
<p class="arcticle_text">&ldquo;We issue a minimum of 8000 fines a month for illegal cellphone use while driving. But it's not changing behaviour, so we must find a more powerful disincentive. </p> 
					  		    
<p class="arcticle_text">&ldquo;Illegal cellphone use is classified as 'distracted driving' and is one of the four ost dangerous driving habits, with speeding, drinking and driving and not wearing seatbelts.&rdquo; - Cape Argus </p> 
					  		  		  
		  																					                                        <p><a href="http://www.iol.co.za/newsletters" target="_blank">Motoring newsletter - click here to keep up to speed with the best in motoring</a></p>
						  		  
		  
		  		    		  

        </div>
	  <!-- .aticle_column -->
        
        
	  </div>  
	  
	  
	  
	  
<!-- C-ON-TEXT_CONTENT_END -->
</div> 

  
	  


<div class="article-ad-cont">


<!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Articles // Page: ROS // Placement: IOL Article ROS-MPU Content-300 x 250 (4390488) // created at: Apr 16, 2013 2:56:37 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4390488|0|170|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4390488|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4390488|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="300" height="250"></a></noscript>
<!-- End of JavaScript Tag -->
	
</div>	

<div style="width:320px; float: left;">	  
	  <br />
      <a name="sharinganchor"></a>
	  		<table>
            	<tr>
            		<td>
                       <script src="http://connect.facebook.net/en_US/all.js#xfbml=1"></script><fb:like show_faces="true" width="450" action="recommend"></fb:like>
                    </td>
                </tr>
		</table>
		

        <div class="article_tool">
		            <!-- AddThis Button BEGIN -->
<div class="addthis_toolbox addthis_default_style addthis_32x32_style">
<a class="addthis_button_preferred_1"></a>
<a class="addthis_button_preferred_2"></a>
<a class="addthis_button_preferred_3"></a>
<a class="addthis_button_preferred_4"></a>
<a class="addthis_button_compact"></a>
<a class="addthis_counter addthis_bubble_style"></a>
</div>
<script type="text/javascript">var addthis_config = {"data_track_addressbar":true};</script>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#pubid=ra-4fc86a501732950d">
</script>
<script>
var addthis_share = {
    url_transforms: {
	clean: true, shorten: 
	{ twitter: "bitly"}
	},
    shorteners: {bitly : { login: "IOLDev",apiKey: "R_f3b73cf80cbc877f864aeeb27c9233a6"} }
};
</script>


<!-- AddThis Button END -->







        </div> <!--  .article_tool" -->
		
		


                                                                                                                                                                                                                                                                                                                                                                                                                      <span class="storify-this">
       <input type="image" src="/images/share_button.png" name="storify">
    </span>
	
    <div class="images">
    <a href="http://www.iol.co.za/newsletters" target="_blank"><img src="/images/sign-up.jpg" alt="sign up" class="storify-this"/></a>
    </div>
</div>  





<div class="comments_ad_space">&nbsp;</div>

  	    <!-- Render the Comments -->
                  


  <div class="comments_text">
	<a name="comments_start">&nbsp;</a>
<h3>Comment Guidelines</h3>
<hr />
<br />
<ol>
<li>Please read our <a href="http://www.iol.co.za/comment-guidelines" target="_blank" >comment guidelines</a>.</li>
<li>Login and register, if you haven&rsquo; t already.</li>
<li>Write your comment in the block below and click (Post As)</li>
<li><strong>Has a comment offended you?</strong> Hover your mouse over the comment and wait until a small triangle appears on the right-hand side. Click triangle (<img src="/images/disqus-triangle.png" />) and select "Flag as inappropriate". Our moderators will take action if need be.</p>&nbsp;
</li>


</ol>
<p>

</div>



<div id="disqus_thread" style="margin: 20px 0px 20px 0px; padding: 20px 0px 0px 0px;"></div>
<script type="text/javascript">   
    /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
	var disqus_identifier = '1335083';
    var disqus_shortname = 'iol'; // required: replace example with your forum shortname
	var disqus_title = "Cellphone crackdown - first busts";

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
	





	    	  	  
	</div>
  
                    <div style="clear:both"></div>
	    </div>
	  
	    	    <div id="col_3">
		              
                  
    
      
        


    <div id="related_stories">
    <div id="ContentId(7.4210)" class="related_head" >
    <div id="related_head" class="menu_tab">
      <ul class="menu_tab">
	    		 	     	    		<li>
             <a href="http://www.iol.co.za:80/motoring" rel="most_viewed_body">Most Viewed</a>
        </li>
      </ul>
    </div>
    </div>
          <div id="$most_viewed_body" class="related_tab_1">
        <ul class="menu_tab_lists">
		  		    		      <li><a href="http://www.iol.co.za:80/motoring/industry-news/criminal-record-for-traffic-offenders-1.1668477" class="menu_tab_lists">Criminal record for traffic offenders</a>
                        			  </li>
  		    		  		    		      <li><a href="http://www.iol.co.za:80/motoring/industry-news/clarkson-in-trouble-for-racist-joke-1.1668621" class="menu_tab_lists">Clarkson in trouble for 'racist' joke</a>
                        			  </li>
  		    		  		    		      <li><a href="http://www.iol.co.za:80/motoring/cars/ford/ford-s-cortina-is-coming-back-1.1669059" class="menu_tab_lists">Ford's Cortina is coming back</a>
                        			  </li>
  		    		  		    		      <li><a href="http://www.iol.co.za:80/motoring/cars/volkswagen/down-memory-lane-as-golf-turns-40-1.1668019" class="menu_tab_lists">Down memory lane as Golf turns 40</a>
                                      <img src="/images/icons_pics_gray_bg.gif">
            			  </li>
  		    		  		    		      <li><a href="http://www.iol.co.za:80/motoring/special-features/road-rage-driver-gets-instant-karma-1.1667987" class="menu_tab_lists">Road rage driver gets instant karma</a>
                                      <img src="/images/icons_vids_gray_bg.gif">
            			  </li>
  		    		  		    		  		    		  		    		  		    		  		    		          </ul>
      </div>
          <div id="$most_viewed_body" class="related_tab_2">
        <ul class="menu_tab_lists">
		          </ul>
      </div>
      </div>
<script type="text/javascript">
  ddtabmenu.definemenu("ContentId(7.4210)",0)
</script>
 
          
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4348955|0|170|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4348955|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4348955|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
          
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4348950|0|632|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4348950|0|632|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4348950|0|632|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
          
        
  <div id="top_social_networks_container">
    <div class="top_social_networks">
	  <table>
		<tr>
		  <td><p class="top_social_networks_text">Join us <span class="tsnt_on">on</span></p></td>
		  <td width="35" align="center"><a href="https://www.facebook.com/iolmotoring" target="_blank"><img src="/images/facebook_top.gif" alt="IOL-Social networks" title="" class="pics" /></a></td>
		  <td width="35" align="center"><a href="http://twitter.com/iolmotoring" target="_blank"><img src="/images/tweeter_top.gif" alt="IOL-Social networks" title="" class="pics" /></a></td>
		  <td width="35" align="center"><a href="http://www.iol.co.za:80/rss" target="_blank"><img src="/images/rss_top.gif" class="pics" alt="IOL-Social networks" title="" /></a></td>
		  <td width="35" align="center"><a href="http://www.iol.co.za/newsletters" class="tsnt_on"  target='_blank'><img src="/images/newsletter_top.gif" class="pics" alt="IOL-Social networks" title="" /></a></td>
		
		</tr>
	  </table>
	</div>
  </div>
  
  
 
          
        
        
                        <style>
.right_forms {width:120px;
 float: left; height: 30px;padding: 4px 2px 4px 10px; margin: 10px 20px 
20px 0px; #margin: 0px 20px 20px 0px; font-size: 12px;border: solid 1px 
#9aa2af;}

.right_forms2 {width:120px; float: left; height: 
30px;padding: 4px 2px 4px 10px; margin: 10px 0px 20px 0px; #margin: 0px 
0px 20px 0px; font-size: 12px;border: solid 1px #9aa2af;}</style>
<div id="poll_links_head"><p class="sp_links_headers">Find articles by manufacturer</p></div>
<div style="width: 268px; height: 52px; #height: 38px; padding: 15px 15px 5px 15px; margin: 0px 0px 20px 0px; border: solid 1px #9aa2af;">
<form id="aform">
<select id="mymenu" size="1" class="right_forms">
<option value="nothing" selected="selected"><strong>Select a Car</strong></option>
<option value="http://www.iol.co.za/motoring/cars/alfa-romeo">Alfa Romeo</option>
<option value="http://www.iol.co.za/motoring/cars/audi">Audi</option>
<option value="http://www.iol.co.za/motoring/cars/bentley">Bentley</option>
<option value="http://www.iol.co.za/motoring/cars/bmw">BMW</option>
<option value="http://www.iol.co.za/motoring/cars/cadillac">Cadillac</option>
<option value="http://www.iol.co.za/motoring/cars/chevrolet">Chevrolet</option>
<option value="http://www.iol.co.za/motoring/cars/chery">Chery</option>
<option value="http://www.iol.co.za/motoring/cars/chrysler">Chrysler</option>
<option value="http://www.iol.co.za/motoring/cars/citroen">Citroen</option>
<option value="http://www.iol.co.za/motoring/cars/daewoo">Daewoo</option>
<option value="http://www.iol.co.za/motoring/cars/daihatsu">Daihatsu</option>
<option value="http://www.iol.co.za/motoring/cars/daimler">Daimler</option>
<option value="http://www.iol.co.za/motoring/cars/dodge">Dodge</option>
<option value="http://www.iol.co.za/motoring/cars/ferrari">Ferrari</option>
<option value="http://www.iol.co.za/motoring/cars/fiat">Fiat</option>
<option value="http://www.iol.co.za/motoring/cars/ford">Ford</option>
<option value="http://www.iol.co.za/motoring/cars/honda">Honda</option>
<option value="http://www.iol.co.za/motoring/cars/hummer">Hummer</option>
<option value="http://www.iol.co.za/motoring/cars/hyundai">Hyundai</option>
<option value="http://www.iol.co.za/motoring/cars/isuzu">Isuzu</option>
<option value="http://www.iol.co.za/motoring/cars/jaguar">Jaguar</option>
<option value="http://www.iol.co.za/motoring/cars/jeep">Jeep</option>
<option value="http://www.iol.co.za/motoring/cars/kia">Kia</option>
<option value="http://www.iol.co.za/motoring/cars/land-rover">Land Rover</option>
<option value="http://www.iol.co.za/motoring/cars/lexus">Lexus</option>
<option value="http://www.iol.co.za/motoring/cars/lotus">Lotus</option>
<option value="http://www.iol.co.za/motoring/cars/mahindra">Mahindra</option>
<option value="http://www.iol.co.za/motoring/cars/maserati">Maserati</option>
<option value="http://www.iol.co.za/motoring/cars/mazda">Mazda</option>
<option value="http://www.iol.co.za/motoring/cars/mercedes">Mercedes Benz</option>
<option value="http://www.iol.co.za/motoring/cars/mg">MG</option>
<option value="http://www.iol.co.za/motoring/cars/mini">Mini</option>
<option value="http://www.iol.co.za/motoring/cars/mitsubishi">Mitsubishi</option>
<option value="http://www.iol.co.za/motoring/cars/nissan">Nissan</option>
<option value="http://www.iol.co.za/motoring/cars/opel">Opel</option>
<option value="http://www.iol.co.za/motoring/cars/peugeot">Peugeot</option>
<option value="http://www.iol.co.za/motoring/cars/porsche">Porsche</option>
<option value="http://www.iol.co.za/motoring/cars/proton">Proton</option>
<option
 
value="http://www.iol.co.za/motoring/cars/renault">Renault</option><option
 
value="http://www.iol.co.za/motoring/cars/rover">Rover</option><option
 
value="http://www.iol.co.za/motoring/cars/saab">Saab</option><option
 
value="http://www.iol.co.za/motoring/cars/seat">Seat</option><option
 
value="http://www.iol.co.za/motoring/cars/ssangyong">SsangYong</option><option
 
value="http://www.iol.co.za/motoring/cars/subaru">Subaru</option><option
 
value="http://www.iol.co.za/motoring/cars/suzuki">Suzuki</option><option
 
value="http://www.iol.co.za/motoring/cars/tata">Tata</option><option
 
value="http://www.iol.co.za/motoring/cars/toyota">Toyota</option><option
 
value="http://www.iol.co.za/motoring/cars/volkswagen">Volkswagen</option><option
 
value="http://www.iol.co.za/motoring/cars/volvo">Volvo</option></select></form>

<form
 id="aform">
<select id="mymenu2" size="1" class="right_forms2">
<option value="nothing" selected="selected">Select a 
Bike</option>
<option 
value="http://www.iol.co.za/motoring/bikes/aprilia">Aprilia</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/bimota">Bimota</option>
<option
 value="http://www.iol.co.za/motoring/bikes/bmw">BMW</option>
<option 
value="http://www.iol.co.za/motoring/bikes/buell">Buell</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/cagiva">Cagiva</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/ducati">Dukati</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/gilera">Gilera</option>
<option
 value="http://www.iol.co.za/motoring/bikes/harley-davidson">Harley 
Davidson</option>
<option 
value="http://www.iol.co.za/motoring/bikes/honda">Honda</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/hyosung">Hyosung</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/kawasaki">Kawasaki</option>
<option
 value="http://www.iol.co.za/motoring/bikes/ktm">KTM</option>
<option 
value="http://www.iol.co.za/motoring/bikes/kymco">Kymco</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/laverda">Laverda</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/loncin">Loncin</option>
<option
 value="http://www.iol.co.za/motoring/bikes/moto-guzzi">Moto 
Guzzi</option>
<option 
value="http://www.iol.co.za/motoring/bikes/other">Other</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/sundiro">Sundiro</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/suzuki">Suzuki</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/triumph">Triumph</option>
<option
 
value="http://www.iol.co.za/motoring/bikes/vespa">Vespa</option>
<option
 value="http://www.iol.co.za/motoring/bikes/vuka">Vuka</option>
<option 
value="http://www.iol.co.za/motoring/bikes/yamaha">Yamaha</option>

</select>
</form>



<script
 type="text/javascript">

var selectmenu=document.getElementById("mymenu2")
selectmenu.onchange=function(){ //run some code when "onchange" event fires
 var chosenoption=this.options[this.selectedIndex] //this refers to"selectmenu"
 if (chosenoption.value!="nothing"){
  window.open(chosenoption.value, "_self", "") //open target site (based on option's value attr) in new window
 }
}




var selectmenu=document.getElementById("mymenu")
selectmenu.onchange=function(){ //run some code when "onchange" event fires
 var chosenoption=this.options[this.selectedIndex] //this refers to 
"selectmenu"
 if (chosenoption.value!="nothing"){
  window.open(chosenoption.value, "_self", "") //open target site (based on option's value attr) in new window
 }
}



</script>






</div>



















      
      
          
        		 
 



<div id="sp_links">
  <div id="sp_links_head"><p class="sp_links_headers">Services </p></div>
  <div id="sp_links_body">
    <div id="sp_links_text_left">
      <ul class="menu_tab_lists">
                                                      <li><a href="http://adserver.adtech.de/?adlink%7C3.0%7C585%7C1102745%7C1%7C16%7CAdId=8055572;BnId=2;link=http://www.hyundai.co.za/index.cfm?event=i20" rel="nofollow" class="menu_tab_lists" >The New i20</a></li>
                                                                                  <li><a href="http://adserver.adtech.de/?adlink%7C3.0%7C585%7C1102745%7C1%7C16%7CAdId=8129288;BnId=1;link=http://www.alloutlotto.com/?affiliateCode=8" rel="nofollow" class="menu_tab_lists" >Play UK Lottery - Go AllOut</a></li>
                                                                                  <li><a href="http://adserver.adtech.de/?adlink%7C3.0%7C567%7C1104792%7C1%7C16%7CAdId=9017502;BnId=1;link=http://www.dialdirect.co.za/express-claims?vdn=15962" rel="nofollow" class="menu_tab_lists" >Save up to 25% on your insurance: Dial Direct</a></li>
                                                                                  <li><a href="http://iol.datingbuzz.com/s/a/16404" rel="nofollow" class="menu_tab_lists" >Searching for Love and Friendship</a></li>
                                          </ul>
    </div>
    <div id="sp_links_text_right">
      <ul class="menu_tab_lists">
                                                						                        <li><a href="http://adserver.adtech.de/?adlink%7C3.0%7C585%7C1102745%7C1%7C16%7CAdId=8189092;BnId=3;link=http://www.metropolitan.co.za/digital/iol/index.htm" rel="nofollow" class="menu_tab_lists"  target='_blank'>Funeral cover from R36 p.m.</a></li>
                                                          						                        <li><a href="http://adserver.adtech.de/?adlink|3.0|585|1102745|1|16|AdId=7548793;BnId=1;link=http://adserver.adtech.de/?adlink|3.0|559|2122637|1|16|AdId=7540407;BnId=1;link=http://www.oldmutual.co.za/personal/educ" rel="nofollow" class="menu_tab_lists"  target='_blank'>Education plan from R150/m</a></li>
                                                          						                        <li><a href="http://adserver.adtech.de/?adlink|3.0|585|1102745|1|16|AdId=8067860;BnId=1;link=http://www.1lifedirect.co.za/quick-quote/?vdn=21474" rel="nofollow" class="menu_tab_lists"  target='_blank'>Simple affordable life cover</a></li>
                                                          						                        <li><a href="http://www.iolproperty.co.za " rel="nofollow" class="menu_tab_lists"  target='_blank'>Property </a></li>
                        </ul>
    </div>
  </div>
</div>

          
        
        
                                  <div id="jobs_prop_class_motor"> 
              <div id="71741373356533" class="third_col_head">
                <ul class="menu_tab">
                                      <li>
                                              <a href="http://www.iolproperty.co.za" target="_blank" rel="menu_tab_171741373356533">
                                            Property</a>
                    </li>
                                     <li>
                                              <a href="http://www.wegotads.co.za" target="_blank" rel="menu_tab_271741373356533">
                                            Classifieds</a>
                    </li>
                                     <li>
                                              <a href="http://www.iolmotoring.co.za" target="_blank" rel="menu_tab_371741373356533">
                                            Motors</a>
                    </li>
                                </ul> 
             </div>
                            <div id="menu_tab_171741373356533" class="menu_tab_1">
							   <div style="width: 300px; height:140px; overflow:hidden; border: 0px; border:none;"> <iframe src="http://www.iolproperty.co.za/featured_property.jsp?type=new_home" style="width: 310px; height:150px; overflow:hidden;  border:none;"  frameborder="0"> </iframe>  </div>
               </div>
                            <div id="menu_tab_271741373356533" class="menu_tab_2">
							   <div style="width: 300px; height: 140px; background-image: url('/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/wegotads_bg.jpg'); position: absolute; top: 0px; float: left; z-index: 19px;">
<div style=" width:130px; height:111px; float:left; margin:0px 0px 0px 0px; padding:0px;">
 <a href="http://www.wegotads.co.za/"><img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/wegotads_pic.jpg" alt="" border="0"/>
</a>
 </div>
 
 <div style=" width: 162px; float:left; margin:11px 0px 0px 0px; padding:0px; height: 101px;">
<p style="margin-top: 0px; margin-left:0px; padding: 0 7px ; clear: inherit;">
Whether you are a buyer or seller, wegotads is your online marketplace.  <br /> 
<a href="http://www.wegotads.co.za/" class="teasers_right_read_more">Wegotads &raquo;</a><br /></p>
</div>

<div>
<div style="width:142px; float:left; margin: 0px 15px 0px 5px;"><a href="http://www.wegotads.co.za/"><img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/your_local_market_place.jpg" alt="" border="0"/>

</a></div>
<div style="float:left; margin: 0px 5px 0px 10px;" ><a href="http://www.wegotads.co.za/">
<img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/wegotads_logo.jpg" alt="" border="0"/>
</a></div>
</div>
</div>
               </div>
                            <div id="menu_tab_371741373356533" class="menu_tab_3">
							   <div style="width: 300px; height: 140px; background-image: url('/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/jobs_bg.png'); position: absolute; top: 0px; float: left; z-index: 19px;">
<div style=" width:130px; height:111px; float:left; margin:1px 0px 0px 0px; padding:0px;">
 <a href="http://www.motoring.co.za/"><img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/motors_car.jpg" alt="" border="0"/>
</a>
 </div>
 
 <div style=" width: 162px; float:left; margin:11px 0px 0px 0px; padding:0px; height: 101px;">
<p style="margin-top: 0px; margin-left:0px; padding: 0 7px ; clear: inherit;">
Buying a car has never been easy. Motoring.co.za contains a large database of car listings with a user friendly search. <br /> 
<a href="http://www.motoring.co.za/" class="teasers_right_read_more">Start searching today &raquo;</a><br /></p>
</div>

<div>
<div style=" width: 111px; float:left; margin: 0px 15px 0px 5px;"><a href="http://www.wegotads.co.za/bluefin.cmp?cPath=16001&cstr=Motors&sfid=1"><img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/cars_for_sale.jpg" alt="" border="0"/>

</a></div>
<div style="width: 148px; float:left;" ><a href="http://www.motoring.co.za/">
<img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/motoring_logo.jpg" alt="" border="0"/>
</a></div>
</div>
</div>
               </div>
                        </div>
           <script type="text/javascript">
             ddtabmenu.definemenu("71741373356533",0)
            </script>
      
      
          
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4348951|0|170|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4348951|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4348951|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
      
  
                                      
                  
    
      
        


 	
			    <script type="text/javascript">
        $(document).ready(function() {
           var voteuid = new Date().getTime();
           $.get('http://www.iol.co.za:80/motoring/industry-news/7.12480?ot=inmsa.AjaxPageLayout.ot&r=http://www.iol.co.za:80/motoring/industry-news/cellphone-crackdown-first-busts-1.1335083&view=right&voteuid='+voteuid, loadPoll7_12480HTML);
        });
        function loadPoll7_12480HTML(pollHTML) {            $('div#poll7_12480').html(pollHTML);
        }
    </script>

    <div id="poll7_12480" class="poll_container">

    </div>
		
	<div>
			</div>
	
	
	
	
	
	
      
  
                                      
                  
    
      
        
        
                        <div id="bd">
<div id="bd_head"><p class="bd_headers">Business Directory</p></div>
<div id="bd_body">
<script type='text/javascript' src='http://adsfeed3.brabys.co.za/www/delivery/spcjs.php?id=4&amp;target=_blank'></script>


<div class="bd_images">

<script type='text/javascript'><!--// <![CDATA[
    /* [id10] IOL Motoring - Zone 1 */
    OA_show(10);
// ]]> --></script><noscript><a target='_blank' href='http://adsfeed3.brabys.co.za/www/delivery/ck.php?n=16c645a'><img border='0' alt='' src='http://adsfeed3.brabys.co.za/www/delivery/avw.php?zoneid=10&amp;n=16c645a' /></a></noscript>


</div>
<div class="bd_images">
<script type='text/javascript'><!--// <![CDATA[
    /* [id11] IOL Motoring - Zone 2 */
    OA_show(11);
// ]]> --></script><noscript><a target='_blank' href='http://adsfeed3.brabys.co.za/www/delivery/ck.php?n=366e59c'><img border='0' alt='' src='http://adsfeed3.brabys.co.za/www/delivery/avw.php?zoneid=11&amp;n=366e59c' /></a></noscript>


</div>
<div class="bd_images">
<script type='text/javascript'><!--// <![CDATA[
    /* [id12] IOL Motoring - Zone 3 */
    OA_show(12);
// ]]> --></script><noscript><a target='_blank' href='http://adsfeed3.brabys.co.za/www/delivery/ck.php?n=751b39d'><img border='0' alt='' src='http://adsfeed3.brabys.co.za/www/delivery/avw.php?zoneid=12&amp;n=751b39d' /></a></noscript>


</div>
<div class="bd_images">
<script type='text/javascript'><!--// <![CDATA[
    /* [id14] IOL Motoring - Zone 4 */
    OA_show(14);
// ]]> --></script><noscript><a target='_blank' href='http://adsfeed3.brabys.co.za/www/delivery/ck.php?n=130868b'><img border='0' alt='' src='http://adsfeed3.brabys.co.za/www/delivery/avw.php?zoneid=14&amp;n=130868b' /></a></noscript>

</div>

</div>

</div>



      
      
          
                <div class="dating-shopping-mobile">
  <div class="dating-shopping-mobile_text_container">
      






                   <img title='' height='25' style='' alt='IOL Travel' width='150' class='pics' src='/polopoly_fs/iol-travel-1.2128!/image/1137364646.png_gen/derivatives/absolute/1137364646.png' />        <p class="dating-shopping-mobile_text"><a href="http://www.iol.co.za/travel" class="dating-shopping-mobile_text"  target='_blank'>Make sure you find the best available airfares with our easy-to-use search engine.</a></p>
  </div>
  <div class="dating-shopping-mobile_pic">
	<a href="http://www.iol.co.za/travel"  target='_blank'>
	          






                   <img title='' height='91' style='' alt='Travel_pic_enw' width='100' class='pics' src='/polopoly_fs/travel-pic-enw-1.2179!/image/2351897088.jpg_gen/derivatives/absolute/2351897088.jpg' />          	</a>
  </div>
</div>


      
  
                	    </div>
	  	  <div style="clear:both"></div>
      </div>
	
        <div id="footer">

	          
                  
    
      
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4348949|0|225|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4348949|0|225|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4348949|0|225|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
          
        <div class="breadcrum_cont">
  <p class="breadcrum"><strong>You are here:</strong>
        	      <a href="http://www.iol.co.za:80/" class="breadcrum">IOL</a><span class="separator"> / </span> 
	  	      <a href="http://www.iol.co.za:80/motoring" class="breadcrum">Motoring</a><span class="separator"> / </span> 
	  	      <a href="http://www.iol.co.za:80/motoring/industry-news" class="breadcrum">Industry News</a><span class="separator"> / </span> 
	        Cellphone crackdown - first busts 
    </p>
</div>

          
        
  <div id="iol_services">
    <div id="iol_services_head">
      <p><img src="/images/iol-services-logo.gif" alt="IOL-Services" title=""/><br />
      <b>We like to make your life easier</b></p>
    </div>
    <div id="iol_services_cont">
      <div class="iol_services_cont_pic">
		<a href="http://www.iol.co.za:80/rss" target="_blank"><img src="/images/footer_rss_feeds.gif" alt="IOL - RSS Feeds" title="" class="pics" /></a>
	  </div>
      <div class="iol_services_cont_text">
		<p><strong><a href="http://www.iol.co.za:80/rss" class="highlights_head" target="_blank">RSS feeds</a></strong>
		<br />
		<a href="http://www.iol.co.za:80/rss" class="footer-links">Subscribe</a> to one of our feeds and receive instant news.</p>
	  </div>
      <div class="iol_services_cont_pic">
		<a href="http://m.iol.co.za/"><img src="/images/footer_mobile.gif" alt="IOL - Mobile" title="" class="pics" /></a>
	  </div>
      <div class="iol_services_cont_text2">
		<p><strong><a href="http://m.iol.co.za/" target="_blank" class="highlights_head">Mobile</a></strong>
		<br /> Browse IOL on your phone at <a href="http://m.iol.co.za/" target="_blank" class="footer-links">m.iol.co.za.</a></p>
	  </div>
      <div class="iol_services_cont_pic">
		<a href="http://www.iol.co.za/newsletters"  target='_blank'><img src="/images/footer_newsletters.gif" alt="IOL - Headlights" title="" class="pics" /></a>
	  </div>
      <div class="iol_services_cont_text">
		<p><strong><a href="http://www.iol.co.za/newsletters"  class="highlights_head"  target='_blank'>Newsletters</a></strong>
		<br />Subscribe to our <a href="http://www.iol.co.za/newsletters" class="footer-links"  target='_blank'> newsletters.</a> News delivered to your inbox!</p>
	  </div>
	  <div class="iol_services_cont_pic3"><a href="http://twitter.com/iolmotoring" target="_blank"><img src="/images/tweeter_top.gif" alt="IOL - Headlights" title="" class="pics" /></a></div>
      <div class="iol_services_cont_text3"><p><strong><a href="http://twitter.com/iolmotoring" target="_blank" class="highlights_head">Twitter</a></strong><br /><a href="http://twitter.com/iolmotoring" class="footer-links">Join us now</a></p></div>
	  <div class="iol_services_cont_pic3"><a href="https://www.facebook.com/iolmotoring"><img src="/images/facebook_top.gif" target="_blank" alt="IOL - Headlights" title="" class="pics" /></a></div>
      <div class="iol_services_cont_text3"><p><strong><a href="https://www.facebook.com/iolmotoring" target="_blank" class="highlights_head">Facebook</a></strong><br /><a href="https://www.facebook.com/iolmotoring" class="footer-links">Join us now</a></p></div>

    </div>  
  </div>

          
        
<div>
 
                  
    
  
  
      </div>
 
 
 
<div id="foot_note">
  <div class="foot_note_text">
	      	  	        <p class="foot_note"><a href="http://www.iol.co.za/about-iol-1.458" class="foot_note" >About IOL</a></p>
	            	  	        <p class="foot_note"><a href="http://www.inlsubs.co.za/" class="foot_note" >Subscriptions</a></p>
	          </div>
        <div class="foot_note_text">
                	  	        <p class="foot_note"><a href="http://www.iol.co.za/about-iol-1.458" class="foot_note" >Feedback</a></p>
	            	  	        <p class="foot_note"><a href="http://www.iol.co.za/about-iol-1.458" class="foot_note" >Contact Us</a></p>
	          </div>
        <div class="foot_note_text">
                	  	        <p class="foot_note"><a href="http://www.iol.co.za/advertising-1.459" class="foot_note" >Advertising</a></p>
	            	  	        <p class="foot_note"><a href="http://www.iol.co.za/site-map" class="foot_note" >Sitemap</a></p>
	          </div>
        <div class="foot_note_text">
                	  	        <p class="foot_note"><a href="http://www.iol.co.za/terms-conditions-1.462" class="foot_note" >Terms & Conditions</a></p>
	            	  	        <p class="foot_note"><a href="http://www.iol.co.za/our-privacy-policy-1.599" class="foot_note" >Privacy Policy</a></p>
	        </div>

  <div id="online_publishers_etc">
	  	  	      <a href="http://www.dmma.co.za"  target='_blank'>
	      






                   <img title='' height='43' style='' alt='DMMA' width='112' class='online_publishers_etc' src='/polopoly_fs/dmma-1.679181!/image/686797677.jpg_gen/derivatives/absolute/686797677.jpg' />          </a>
	  	      <a href="http://the-acap.org/acap-enabled.php"  target='_blank'>
	      






                   <img title='' height='43' style='' alt='Footer_ACAP' width='48' class='online_publishers_etc' src='/polopoly_fs/footer-acap-1.438!/image/2019830826.jpg_gen/derivatives/absolute/2019830826.jpg' />          </a>
	  	      <a href="http://www.presscouncil.org.za/"  target='_blank'>
	      






                   <img title='' height='43' style='' alt='Press_council' width='77' class='online_publishers_etc' src='/polopoly_fs/press-council-1.444!/image/43941698.jpg_gen/derivatives/absolute/43941698.jpg' />          </a>
	  	  </div>

  <div id="footer_copywrite">
    <p class="foot_note">© Copyright 1999 - 2012 Independent Online, a division of Independent Newspapers (Pty) Limited. The copyright in the literary and artistic works contained in this online news publication and its other related and connected websites, as well as in the published editions of group newspapers, their supplements and any other content or material, belongs exclusively to Independent Newspapers (Pty) Limited unless otherwise stated.<br />

The reproduction of any content or material contained in this online news publication and its other related websites as well as the published editions of group newspapers and their supplements is expressly reserved to the publisher, Independent Newspapers (Pty) Limited, under Section 12(7) of the Copyright Act of 1978. Reliance on the information contained in the online news publications and other related content published on this website is done at your own risk and subject to our “terms and conditions”. Independent Newspapers (Pty) Limited has committed itself to The Press Code of Professional Practice which prescribes that news must be reported in a truthful, accurate, fair and balanced manner. If we don't live up to the Press Code please contact The Press Ombudsman 2nd Floor, 7 St David’s Park, St David’s Place, Parktown, 2193 or PO Box 47221, Parklands 2121 or email pressombudsman@ombudsman.org.za (www.ombudsman.org.za) or telephone  011 484 3612/8.</p>
</p>
  </div>


</div>






          
        
        
                        <script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(
['_setAccount', 'UA-425302-12'],
['_trackPageview'],
['newSite._setAccount', 'UA-17710838-1'],
['newSite._trackPageview']
);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();


  _gaq.push(['_setCustomVar',
      1,                  
      'Section',          
      'Lifestyle',    
      3
   ]);

</script>

      
      
      
  
      	  	
    </div>	

  </div>
 </div>

<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
    var disqus_shortname = 'iol'; // required: replace example with your forum shortname
	var disqus_developer = 1;

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function () {
        var s = document.createElement('script'); s.async = true;
        s.type = 'text/javascript';
        s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';
        (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
    }());
</script>
 

<!-- C|ON|TEXT ad tag -->

<!-- Front:iolfront03.mhs.onsite.hosting.co.za -->
<!-- Timestamp:1396430054660 -->
      </body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.iol.co.za/motoring/industry-news/cellphone-crackdown-first-busts-1.1335083#.UzvU562SxWs'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, 'Cellphone crackdown - first busts')
        self.assertEqual(doc.summary, None)
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '05 07 2012')
        self.assertEqual(doc.author.name, 'Murray Williams')
        self.assertEqual(doc.medium.name, 'IOL')

        self.assertEqual(doc.text, u"The first cellphone confiscation has taken place in Cape Town, as the new law was enforced for the first time. \n\nAs of today, drivers who are caught talking on their phones while driving, without headsets or hands-free kits, will have their handsets confiscated by traffic officers. \n\nThe first driver caught this morning was Jean-Benoit Biyoko, a taxi driver. Traffic officers nabbed him in Long Street in the CBD. \n\nThe traffic service's Maxine Jordaan reported: \u201cHe didn't have a driving licence on him and he was taken to Gallows Hill traffic department. \n\n\u201cHis cellphone, a Nokia E63, had a SIM card and memory card in it, which he kept, and he kept his pouch too. \n\n\u201cThe gentleman was very co-operative and said he was sorry.\u201d \n\nJordaan said Biyoko had been fined R500 for talking on his cellphone while driving and would be permitted to collect his phone 24 hours after it was confiscated - on Friday morning. \n\nThe new City law was to be enforced across the city this afternoon, with officers from the undercover 'Ghost Squad', and other officers, deployed on major commuter routes. \n\nOfficers' vehicles will carry special boxes, in which confiscated phones will be placed once they have been logged and sealed in protective pouches. They will then be stored in the traffic department's safe at Gallows Hill. \n\nNo fee is required to reclaim a confiscated phone. \n\nThe bylaw was introduced by safety and security Mayco member JP Smith, who has received praise from across the country for the action against drivers who continue to flout the law. \n\nSmith said camera and video evidence would be used whenever possible to back up officers' observations. \n\n\u201cWe're hoping that everybody will finally get the message, grab those hands-free kits and start using cellphones legally\u201d, Smith said. \n\n\u201cWe issue a minimum of 8000 fines a month for illegal cellphone use while driving. But it's not changing behaviour, so we must find a more powerful disincentive. \n\n\u201cIllegal cellphone use is classified as 'distracted driving' and is one of the four ost dangerous driving habits, with speeding, drinking and driving and not wearing seatbelts.\u201d - Cape Argus ")
        

    def test_isolezwe(self):
        html = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<!-- Start LegacyAppFragment name="Head" -->

	
		


<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />


<script type="text/javascript" src="/Scripts/mobile_detection.js">
</script>

<script type="text/javascript">
directToMobileSite();
</script>

<link rel="stylesheet" type="text/css" href="/css/atexStyle.css" />
<link rel="stylesheet" type="text/css" href="/css/iol_style.css" />
<link rel="stylesheet" type="text/css" href="/css/iol_layout_style.css" />
<link rel="stylesheet" type="text/css" href="/css/gallery_style.css" />
<link rel="stylesheet" type="text/css" href="/css/tn3.css" />
<link href='http://fonts.googleapis.com/css?family=Archivo+Black' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Oswald:400,700' rel='stylesheet' type='text/css'>
	
<script src="/Scripts/cufon-yui.js" type="text/javascript"></script>
<script src="/Scripts/Impact_400.font.js" type="text/javascript"></script>

<!-- include jQuery library -->
<script type="text/javascript" src="/Scripts/jquery.min.js"></script>
<!-- include tn3 plugin -->
<script type="text/javascript" src="/Scripts/jquery.tn3lite.min.js"></script>

<link rel="stylesheet" type="text/css" href="/Scripts/jquery.fancybox-1.3.1.css" media="screen" />

<!--[if IE 6]>
<link rel="stylesheet" type="text/css" href="css/iol_style_ie6.css" />
<![endif]-->

<link rel="shortcut icon" href="/images/iol_favicon.jpg" />	
	
  <link rel="stylesheet" type="text/css" href="http://www.iol.co.za/cmlink/style-7.10062">
  <link rel="stylesheet" type="text/css" href="http://www.iol.co.za/cmlink/isolezwe-style-7.4947">

  
        <link rel="alternate" type="application/rss+xml" title="Home Page RSS" href="http://www.iol.co.za/cmlink/home-page-rss-1.1538217" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="TV Box Teaser RSS" href="http://www.iol.co.za/cmlink/tv-box-teaser-rss-1.1537631" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Anene Booysen" href="http://www.iol.co.za/cmlink/anene-booysen-1.1468146" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Lance Armstrong Hot Topic feed" href="http://www.iol.co.za/cmlink/lance-armstrong-hot-topic-feed-1.1454231" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="US Elections 2012 RSS feed" href="http://www.iol.co.za/cmlink/us-elections-2012-rss-feed-1.1417822" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Malema RSS FEED" href="http://www.iol.co.za/cmlink/malema-rss-feed-1.1390238" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Dewani RSS feed" href="http://www.iol.co.za/cmlink/dewani-rss-feed-1.1376644" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Marikana feed" href="http://www.iol.co.za/cmlink/marikana-feed-1.1376639" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="News RSS Multimedia Videos Feed" href="http://www.iol.co.za/cmlink/news-rss-multimedia-videos-feed-1.1152520" />
        
        <link rel="alternate" type="application/rss+xml" title="News RSS Multimedia Galleries Feed" href="http://www.iol.co.za/cmlink/news-rss-multimedia-galleries-feed-1.1149195" />
        
        <link rel="alternate" type="application/rss+xml" title="Editors Pick Extended RSS" href="http://www.iol.co.za/cmlink/editors-pick-extended-rss-1.1137157" />
        
        <link rel="alternate" type="application/rss+xml" title="News Africa Extended" href="http://www.iol.co.za/cmlink/news-africa-extended-1.679216" />
        
        <link rel="alternate" type="application/rss+xml" title="Soccer Soccer Extended RSS" href="http://www.iol.co.za/cmlink/soccer-soccer-extended-rss-1.679215" />
        
        <link rel="alternate" type="application/rss+xml" title="Most Commmented Stories" href="http://www.iol.co.za/cmlink/most-commmented-stories-1.1625" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Most Viewed Stories" href="http://www.iol.co.za/cmlink/most-viewed-stories-1.1624" />
        <?xml-stylesheet href="/css/rss.xsl" type="text/xsl" media="screen"?>
        
        <link rel="alternate" type="application/rss+xml" title="Home Page Extended" href="http://www.iol.co.za/cmlink/home-page-extended-1.628986" />
        
        <link rel="alternate" type="application/rss+xml" title="Sport Extended" href="http://www.iol.co.za/cmlink/sport-extended-1.628987" />
        
        <link rel="alternate" type="application/rss+xml" title="Sport Rugby Extended" href="http://www.iol.co.za/cmlink/sport-rugby-extended-1.628988" />
        
        <link rel="alternate" type="application/rss+xml" title="Sport Cricket Extended" href="http://www.iol.co.za/cmlink/sport-cricket-extended-1.628989" />
        
        <link rel="alternate" type="application/rss+xml" title="News Back Page Extended" href="http://www.iol.co.za/cmlink/news-back-page-extended-1.628990" />
        
        <link rel="alternate" type="application/rss+xml" title="News South Africa Extended" href="http://www.iol.co.za/cmlink/news-south-africa-extended-1.679178" />
        
        <link rel="alternate" type="application/rss+xml" title="News World Extended" href="http://www.iol.co.za/cmlink/news-world-extended-1.679217" />
        
        <link rel="alternate" type="application/rss+xml" title="Sport Golf Extended" href="http://www.iol.co.za/cmlink/sport-golf-extended-1.679220" />
        
        <link rel="alternate" type="application/rss+xml" title="Western Cape Extended" href="http://www.iol.co.za/cmlink/western-cape-extended-1.679223" />
        
        <link rel="alternate" type="application/rss+xml" title="News Gauteng Extended" href="http://www.iol.co.za/cmlink/news-gauteng-extended-1.679235" />
        
        <link rel="alternate" type="application/rss+xml" title="News KwaZulu-Natal Extended" href="http://www.iol.co.za/cmlink/news-kwazulu-natal-extended-1.679236" />
      

    <title>EzikaMalema zethule abazo eKZN - Isolezwe | IOL.co.za</title>




<meta name="keywords" content="" />
<meta name="description" content="" />
<meta name="author" content="Independent Newspapers Online" />
<meta name="google-site-verification" content="YmiNpvzQrHdqXOi__ytAIEQM_vjpAQvum7AZW5rs1xE" /> 		
<meta http-equiv="expires" content="1396429893915" />
	

<script type="text/javascript" src="/Scripts/menu.js"></script>


  <script type="text/javascript">
    <!--
    function MM_showHideLayers() { //v9.0
      var i,p,v,obj,args=MM_showHideLayers.arguments;
      for (i=0; i<(args.length-2); i+=3) 
      with (document) if (getElementById && ((obj=getElementById(args[i]))!=null)) { v=args[i+2];
        if (obj.style) { obj=obj.style; v=(v=='show')?'visible':(v=='hide')?'hidden':v; }
        obj.visibility=v; } 
    }
    function MM_swapImgRestore() { //v3.0
      var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
    }
    function MM_preloadImages() { //v3.0
      var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
        var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
        if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
    }
    
    function MM_findObj(n, d) { //v4.01
      var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
        d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
      if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
      for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
      if(!x && d.getElementById) x=d.getElementById(n); return x;
    }
    
    function MM_swapImage() { //v3.0
      var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
       if ((x=MM_findObj(a[i]))!=null)
	   	{
		document.MM_sr[j++]=x;
		if(!x.oSrc) x.oSrc=x.src;
		x.src=a[i+2];
		}
    }
    //-->
  </script>
  
  
<!-- End LegacyAppFragment name="Head" -->	

        

      </head>
<body onload="MM_preloadImages('/images/multimedia_gal_prev2.jpg','/images/multimedia_gal_next2.jpg','/images/multimedia_gal_forward2.gif','/images/multimedia_gal_back2.gif','/images/a_tool_email_2.jpg','/images/a_tool_print_2.jpg','/images/pagination_prev_hov.jpg','/images/pagination_next_hov.jpg'); naming();  ">
    <div class="top-ad-wrapper">
	
		      
                  
    
      
                
<div id="top_container" align="center">

    	  
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4350736|0|225|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4350736|0|225|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4350736|0|225|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      	
</div>













          
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4350739|0|16|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4350739|0|16|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4350739|0|16|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
          
        
        
                        <!-- BEGIN EFFECTIVE MEASURE CODE -->
<!-- COPYRIGHT EFFECTIVE MEASURE -->
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
<!--END EFFECTIVE MEASURE CODE -->
      
      
      
  
      		      
                  
    
      
        
<div id="top_container" align="center">

    
</div>












  <div class="sponsored_links">
    <div class="sponsored_links_head"><p class="sponsored_link_head_text">Sponsored Links:</p></div>
    <div class="sponsored_links_cont">  
      <ul class="sponsored_link_cont">
        		  <li>
			    <a href="http://www.ioldeals.co.za/"  target='_blank' style="margin: 0px 0px 0px 5px;">IOL Deals</a>
		  </li>
				  <li>
			    <a href="http://www.iolproperty.co.za/"  target='_blank' style="margin: 0px 0px 0px 5px;">IOL Property</a>
		  </li>
				  <li>
			    <a href="http://www.ioldating.co.za"  target='_blank' style="margin: 0px 0px 0px 5px;">IOL Dating</a>
		  </li>
				  <li>
			    <a href="http://www.wegotads.co.za"  target='_blank' style="margin: 0px 0px 0px 5px;">WeGotAds</a>
		  </li>
				  <li>
			    <a href="http://www.ioljobs.co.za/"  target='_blank' style="margin: 0px 0px 0px 5px;">IOL Jobs</a>
		  </li>
		      </ul>
    </div>
  </div>

      
  
      		
  </div>
		  <div id="wrapper">
			<div id="masthead" class="masthead">
	          
                  
    
      
        
        
		
				
<div class="images">
						   <img src="http://www.iol.co.za:80/polopoly_fs/isolezwe1-7.7574!/image/2550624056.png_gen/derivatives/default/2550624056.png" alt="isolezwe1" class="images"/>
			 </div>
      
      
          
        
        
		
				
<div class="images">
						   <img src="http://www.iol.co.za:80/polopoly_fs/isolezwe-2-7.7573!/image/2235133015.png_gen/derivatives/default/2235133015.png" alt="isolezwe-2" class="images"/>
			 </div>
      
      
          
        
        
		
				
<div class="images">
						   <img src="http://www.iol.co.za:80/polopoly_fs/isolezwe-3-7.7571!/image/3092858343.png_gen/derivatives/default/3092858343.png" alt="isolezwe-3" class="images"/>
			 </div>
      
      
          
        <div class="search_box">
<div id="cse-search-form" style="width: 300px;float: left">Loading</div>
<script src="http://www.google.com/jsapi" type="text/javascript"></script>
<script type="text/javascript"> 
  google.load('search', '1', {language : 'en', style : google.loader.themes.ESPRESSO});
  google.setOnLoadCallback(function() {
    var customSearchOptions = {};  var customSearchControl = new google.search.CustomSearchControl(
      'partner-pub-7576204233346138:2203392007', customSearchOptions);
    customSearchControl.setResultSetSize(google.search.Search.FILTERED_CSE_RESULTSET);
    var options = new google.search.DrawOptions();
    options.enableSearchboxOnly("http://www.iol.co.za/search-results-page");
    customSearchControl.draw('cse-search-form', options);
  }, true);
</script>
</div>

      
  
      	  	  <div class="clearing"></div>
    </div>

	
		<div id="navigation">
	          
                  
    
      
        


  	<div class="nav_home_sections">
      <div id="home_navigation">
        <p class="nav_home_text_sections">
		  <img src="/images/nav_logo.jpg" alt="IOL - logo" title="" class="nav_logo" />
		  <a href="/"  rel="nav_home_submenus">Home</a>
		</p>
      </div>
	  <div id="nav_home_submenus" class="tabcontent">
        <div class="nav_home_submenus">
	      	      <ul>
                	                                    	                                    	                             <li><a href="http://www.iol.co.za:80/news"  class=""  rel="navigation2226" >News</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/business"  class=""  rel="navigation2545" >Business</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/sport"  class=""  rel="navigation2228" >Sport</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/motoring"  class=""  rel="navigation2572" >Motoring</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/tonight"  class=""  rel="navigation2901" >Tonight</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/lifestyle"  class=""  rel="navigation2227" >Lifestyle</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/travel"  class=""  rel="navigation2835" >Travel</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/scitech"  class=""  rel="navigation2750" >SciTech</a></li>
                      	                                    	                             <li><a href="http://www.iol.co.za:80/blogs"  class=""  rel="navigation2230" >Blogs</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/newspapers"  class=""  rel="navigation2231" >Newspapers</a></li>
                      	                                                	                				        	                 <li><a href="http://www.wegotads.co.za"  class=""  rel="navigation1620826"  target='_blank'>Classifieds</a></li>
                                  	                				        	                 <li><a href="http://www.iolproperty.co.za"  class=""  rel="navigation1620809"  target='_blank'>Property</a></li>
                                  	                				        	                 <li><a href="http://ioljobs.co.za/"  class=""  rel="navigation11578664"  target='_blank'>Jobs</a></li>
                      	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                                    	                            </ul>
    	    </div>
      </div>
	</div>
		      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	      	            	      	      	      	      	      				<div class="nav_links_sections">
      <div id="ddtabs3" class="solidblockmenu">
        	      <ul>
                                          							                 <li><a href="http://www.iol.co.za:80/isolezwe"  class=""  rel="navigation1989096" >Isolezwe Home</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/isolezwe/izindaba"  class=""  rel="navigation21554" >Izindaba</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/isolezwe/ezokungcebeleka"  class=""  rel="navigation21553" >Ezokungcebeleka</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/isolezwe/ezemidlalo"  class=""  rel="navigation21552" >Ezemidlalo</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/isolezwe/intandokazi"  class=""  rel="navigation21551" >Intandokazi</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/isolezwe/ezemisakazo"  class=""  rel="navigation21550" >Ezemisakazo</a></li>
                      	                             <li><a href="http://www.iol.co.za:80/isolezwe/ezezimoto"  class=""  rel="navigation21549" >Ezezimoto</a></li>
                      	                                    	                            </ul>
    	  </div>	
	  	  	
                <div id="navigation1989096" class="tabcontent">
        <div class="second_level_menu">
		  						          </div>
      </div>
          <div id="navigation21554" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation21553" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation21552" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation21551" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation21550" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation21549" class="tabcontent">
        <div class="second_level_menu">
		              	    		          </div>
      </div>
          <div id="navigation21617" class="tabcontent">
        <div class="second_level_menu">
		              	      <ul>
                	                                    	                                    	                                    	                                    	                                    	                            </ul>
    		          </div>
      </div>
          <div id="navigation21616" class="tabcontent">
        <div class="second_level_menu">
		              	      <ul>
                	                                    	                                    	                                    	                                    	                                    	                            </ul>
    		          </div>
      </div>
            </div> 
			  		  		  		  		  		  		  		  		  		<div class="nav_add">
		        				      </div>
	<script type="text/javascript">
	  	    ddtabmenu.definemenu("ddtabs3")
	      </script>
	<script type="text/javascript">
      ddtabmenu.definemenu("home_navigation")
    </script>
  


      
  
      	  	</div>
	
								<div id="nav_devider"></div>
		        	
		  <div id="col_1_2_3_container_sections">
		
	  	    	    <div id="col_1_2">
		              


	<img src='http://www.iol.co.za/logger/p.gif?a=1.1667768&amp;d=/2.225/2.1495' alt='' />


          <div class="article-white">
      <h1 class="article_headers">EzikaMalema zethule abazo eKZN</h1>
      <p class="byline">
						  		          		    March 28 2014 at 11:57am <br/>
		                   By CELANI SIKHAKHANE noSIMPHIWE NGUBANE
	          </p>
              <p class="comment_call_to_action"><a class="lrc_btm_text" href="#comments_start">Comment on this story</a></p>
            <hr />
	 
	  <div class="ctx_content">
<!-- C-ON-TEXT_CONTENT_START --> 

      <div id="article_container">
        <div class="aticle_column">
                      <div class="aticle_video">
        	                                <!-- Main Editorial Image -->
                    			      			                                      <img src="/polopoly_fs/copy-of-no-no-moonsamyy0-1.1667766!/image/3851252182.jpg_gen/derivatives/box_300/3851252182.jpg" alt="Copy of NO_no moonsamyy0" title=""  class="pics"/>
				  <p class="captions_credit_article">INL SA</p>
                  <p class="captions">UNKSZ Magdalene Moonsamy, osuka kwi-ANC Youth League, ujutshwe yisigungu se-EFF kuzwelonke ukuthi eze KwaZulu-Natal</p>
                  <p class="captions"></p>
                                          </div>
                              
		  
		  
		  
		  
		  		  					  		  		    <!--PSTYLE=WT Web Text--><p class="arcticle_text"><strong>CELANI SIKHAKHANE noSIMPHIWE NGUBANE</strong> </p> 
					  		    <p/><p class="arcticle_text"><strong>I</strong>-Economic Freedom Fighters (EFF) KwaZulu-Natal ifolosa ngabesifazane nentsha ohlwini lwayo lwamagama okuqala ayishumi abaholi abazoyimela esiShayamthetho ngemva kokhetho lukazwelonke oluzoba ngoMeyi 7. </p> 
					  		    <p class="arcticle_text">Lokhu kugqame izolo ngenkathi i-EEF yethula abaholi bayo abasohlwini lokhetho esithangamini nabezindaba eThekwini. </p> 
					  		    <p class="arcticle_text">Inxusa leqembu nokubhekwe ukuthi libe ngundunankulu wase-KZN uma i-EFF inqoba, nguMnuz Vusi Khoza. UKhoza uke waba yikhansela le-ANC eThekwini nonobhala weNFP esifundazweni. </p> 
					  		    <p class="arcticle_text">UKhoza uthe uhla lwabo lumele lonke uhlobo lwabantu abakhona  e-KZN ngokobulili, ukuxuba intsha nabadala. </p> 
					  		    <p class="arcticle_text">UNksz Magdalene Moonsamy, obengumholi we-ANC Youth League nojutshwe ubuholi bukazwelonke esifundazweni, uthe iningi labaholi babo abazobamela eSishayamthetho banamakhono adingekayo futhi bayabethemba. </p> 
						  							                                                                  				    <div class="aticle_pic">
                      <img src="/polopoly_fs/copy-of-no-no-khoza0-1.1667767!/image/4259951999.jpg_gen/derivatives/box_300/4259951999.jpg" class="pics" alt="Copy of NO_no khoza0" title="" />
                      <p class="captions">UMNUZ Vusi Khoza, osuka kwi-ANC neNational Freedom Party, i-Economic Freedom Fighters imthwele ngeqoma ukuthi abe ngundunankulu eKZN</p>
					  <p class="captions"><span class="captions_credit">INLSA</span></p>
                    </div>
				    		          		        		    		  		    <p class="arcticle_text">&#8220;Abanye baholi bethu banomlando wokusebenzela abantu kusuka kwi-ANC nakwezinye izinhlaka njengoKhoza okunguye osimele njengondunankulu wesifundazwe,&#8221; kusho uNksz Moonsamy. </p> 
					  		    <p class="arcticle_text">Okufike kwagqama wukuthi ngesikhathi bebiza uKhoza abaholi bale nhlangano bebembiza ngondunankulu, yize kungakayiwa okhethweni. </p> 
					  		    <p class="arcticle_text">Phakathi kwamagama asohlwini lokuqala olubizwa nge-<em>Top 10</em> uKhoza,uNksz Thembi Msane, uMnuz Lwazi Ntombela, uNksz Londiwe Mkhwanazi, uMnuz Nhlanhla Buthelezi, uNksz Sbongile Khawula, uVerusca Fynn, uMnuz Reggie Ngcobo,uNksz Cebisile Shangase, uMnuz Nkosinathi Mthethwa. </p> 
					  		    <p class="arcticle_text">UNksz Moonsamy uthe abaholi babo bazimisele ukufunda okuningi njengoba beya eSishayamthetho. </p> 
					  		    <p class="arcticle_text">UKhoza uthe okubalulekile kubo wukuthi banqobe zonke izihlalo ezingu-80 eziseSishayamthetho. </p> 
					  		    <p class="arcticle_text">Ngaphandle kwamagama abaholi abayishumi abasohlwini , kuphinde kwethulwa nabanye abasohlwini lwesifundazwe abayingxenye yabantu abazoya eSishayamthetho. </p> 
						  				  		        		    		  		    <p class="arcticle_text">Kulesi sithangami kuphinde kwethulwa uMnuz Vukani Ndlovu ngokusemthethweni obedume ebuholini be-ANC Youth League ngenkathi ehola isigungu sesikhashana sesifundazwe esihlakazwe ngonyaka odlule. </p> 
					  		    <p class="arcticle_text">Abaholi baleli qembu bamile ekutheni bafuna ukusebenzisana nanoma yimuphi umbutho ozovumelana nabo ngemigomo ehambisana nokubuyiswa komhlaba ngaphandle kwesinxephezelo ukuthi uhlomulise bonke abantu bakuleli. </p> 
					  		    <p class="arcticle_text">UNksz Moonsamy uthe bangasebenzisana neFreedom Front Plus inqobo nje uma izimisele ukuvumelana nabo ngodaba lomhlaba, ivume ukuthi kumele ubesezandleni zabantu, hhayi zedlanzana. </p> 
					  		    <p class="arcticle_text">Abaholi baleli qembu abazange bacacise ukuthi banamalungu amangaki eKZN, bakhankasa nini nokuthi yiziphi izindlela abazisebenzisayo ukuxhumana nabantu njengoba bethi sebehlangane nabantu abaningi abampofu, abahola kancane, abasebenza ezindlini, abahlengikazi nabahlala emijondolo. </p> 
					  		    <p class="arcticle_text">Bathi iKZN sebeyiphendule yabomvu njengoba bexhumana nabantu kuzona zonke izingxenye zesifundazwe. </p> 
					  		    <p class="arcticle_text">UKhoza uthe abantu baseKZN basetshenziswa ngamaqembu ezepolitiki njengethuluzi lokuvota ukuze kucebe idlanzana eliphila ntofontofo. </p> 
						  				  		        		    		  		    <p class="arcticle_text">Uphinde wathi igama lesifundazwe selingcolile  ezweni isidume njengendawo eyisizinda senkohlakalo  ngenxa yomuzi kaMengameli  Jacob Zuma owakhiwe ngoR246 million . </p> 
					  		  		  
		  		  
		  
		  		    		  

        </div>
	  <!-- .aticle_column -->
        
        
	  </div>  
	  
	  
	  
	  
<!-- C-ON-TEXT_CONTENT_END -->
</div> 

  
	  


<div class="article-ad-cont">


<!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Articles // Page: ROS // Placement: IOL Article ROS-MPU Content-300 x 250 (4390488) // created at: Apr 16, 2013 2:56:37 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4390488|0|170|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4390488|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4390488|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="300" height="250"></a></noscript>
<!-- End of JavaScript Tag -->
	
</div>	

<div style="width:320px; float: left;">	  
	  <br />
      <a name="sharinganchor"></a>
	  		<table>
            	<tr>
            		<td>
                       <script src="http://connect.facebook.net/en_US/all.js#xfbml=1"></script><fb:like show_faces="true" width="450" action="recommend"></fb:like>
                    </td>
                </tr>
		</table>
		

        <div class="article_tool">
		            <!-- AddThis Button BEGIN -->
<div class="addthis_toolbox addthis_default_style addthis_32x32_style">
<a class="addthis_button_preferred_1"></a>
<a class="addthis_button_preferred_2"></a>
<a class="addthis_button_preferred_3"></a>
<a class="addthis_button_preferred_4"></a>
<a class="addthis_button_compact"></a>
<a class="addthis_counter addthis_bubble_style"></a>
</div>
<script type="text/javascript">var addthis_config = {"data_track_addressbar":true};</script>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#pubid=ra-4fc86a501732950d">
</script>
<script>
var addthis_share = {
    url_transforms: {
	clean: true, shorten: 
	{ twitter: "bitly"}
	},
    shorteners: {bitly : { login: "IOLDev",apiKey: "R_f3b73cf80cbc877f864aeeb27c9233a6"} }
};
</script>


<!-- AddThis Button END -->







        </div> <!--  .article_tool" -->
		
		


                                                                                                                                                                                                                                                                                                                                                                                                                      <span class="storify-this">
       <input type="image" src="/images/share_button.png" name="storify">
    </span>
	
    <div class="images">
    <a href="http://www.iol.co.za/newsletters" target="_blank"><img src="/images/sign-up.jpg" alt="sign up" class="storify-this"/></a>
    </div>
</div>  





<div class="comments_ad_space">&nbsp;</div>

  	    <!-- Render the Comments -->
                  


  <div class="comments_text">
	<a name="comments_start">&nbsp;</a>
<h3>Comment Guidelines</h3>
<hr />
<br />
<ol>
<li>Please read our <a href="http://www.iol.co.za/comment-guidelines" target="_blank" >comment guidelines</a>.</li>
<li>Login and register, if you haven&rsquo; t already.</li>
li>Write your comment in the block below and click (Post As)</li>
<li><strong>Has a comment offended you?</strong> Hover your mouse over the comment and wait until a small triangle appears on the right-hand side. Click triangle (<img src="/images/disqus-triangle.png" />) and select "Flag as inappropriate". Our moderators will take action if need be.</p>&nbsp;
</li>


</ol>
<p>

</div>



<div id="disqus_thread" style="margin: 20px 0px 20px 0px; padding: 20px 0px 0px 0px;"></div>
<script type="text/javascript">   
    /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
	var disqus_identifier = '1667768';
    var disqus_shortname = 'iol'; // required: replace example with your forum shortname
	var disqus_title = "EzikaMalema zethule abazo eKZN";

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
	





	    	  	  
	</div>
  
                    <div style="clear:both"></div>
	    </div>
	  
	    	    <div id="col_3">
		              
                  
    
      
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4350742|0|170|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4350742|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4350742|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
          
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4350737|0|632|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4350737|0|632|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4350737|0|632|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
          
        




<script type="text/javascript">
	<!--
		// Check that min & max are the right way round
		function checkAge (formElement) {
			var mAgeMin = formElement.form.mAgeMin.selectedIndex;
			var mAgeMax = formElement.form.mAgeMax.selectedIndex;
			if (mAgeMax < mAgeMin) {
				formElement.form.mAgeMin.options[mAgeMax].selected = true;
				formElement.form.mAgeMax.options[mAgeMin].selected = true;
			}
			return true;
		}
	//-->
	</script>


<div id="home_dating">
<div id="home_dating_head" class="menu_tab">
<ul class="menu_tab">
<li><a href="#" rel="home_dating_women">Women</a></li>
<li><a href="#" rel="home_dating_men">Men</a></li>
<li><a href="#" rel="home_dating_search">Search</a></li>
</ul>
</div>



<div id="home_dating_women" class="home_dating_tab1">
			                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3425473/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/su/t/f41~8p.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>HRHCPT</strong><br />
                           <span>I'm a 56 year old woman looking to meet men between the ages of 55 and 65.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3425473/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3294309/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/ob/t/lwl~sp.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Smashizo</strong><br />
                           <span>I'm a 29 year old woman looking to meet men between the ages of 32 and 37.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3294309/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3500258/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/vp/t/0te~in.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>kafze</strong><br />
                           <span>I'm a 29 year old woman looking to meet men between the ages of 29 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3500258/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3350649/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/q8/t/tdl~ad.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>joocypie</strong><br />
                           <span>I'm a 28 year old woman looking to meet men between the ages of 27 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3350649/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3189373/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/kh/t/cxp~fn.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>RealBlackPearl</strong><br />
                           <span>I'm a 22 year old woman looking to meet men between the ages of 25 and 35.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3189373/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3479264/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0j/t/km8~gn.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>bongrhultiy</strong><br />
                           <span>I'm a 45 year old woman looking to meet men between the ages of 44 and 55.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3479264/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3350701/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/q8/t/tf1~j7.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>simphy337</strong><br />
                           <span>I'm a 30 year old woman looking to meet men between the ages of 35 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3350701/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3496022/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/vk/t/xjq~9u.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>xoxohayleyxoxo</strong><br />
                           <span>I'm a 26 year old woman looking to meet men between the ages of 18 and 100.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3496022/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3286716/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/q9/t/g1o~b3.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Nelisa32</strong><br />
                           <span>I'm a 34 year old woman looking to meet men between the ages of 37 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3286716/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3189273/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/kr/t/cux~v5.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>gloml66</strong><br />
                           <span>I'm a 48 year old woman looking to meet men between the ages of 40 and 58.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3189273/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3448583/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/tt/t/wxz~ka.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>sassyfoxylady101</strong><br />
                           <span>I'm a 33 year old woman looking to meet men between the ages of 25 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3448583/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
															                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3463330/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/ud/t/8bm~fg.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Royalness</strong><br />
                           <span>I'm a 29 year old woman looking to meet men between the ages of 30 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3463330/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3478010/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/v3/t/jne~sb.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>sexy50</strong><br />
                           <span>I'm a 51 year old woman looking to meet men between the ages of 25 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3478010/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3446384/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1i/t/v8w~8n.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>AWELANI</strong><br />
                           <span>I'm a 29 year old woman looking to meet men between the ages of 33 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3446384/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3450964/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/tv/t/ys4~s2.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>MASESHIA</strong><br />
                           <span>I'm a 28 year old woman looking to meet men between the ages of 27 and 40.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3450964/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3359074/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/qn/t/zvm~cu.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>sweetnessmgm</strong><br />
                           <span>I'm a 26 year old woman looking to meet men between the ages of 40 and 63.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3359074/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3340907/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/pt/t/luz~fi.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Rivee</strong><br />
                           <span>I'm a 24 year old woman looking to meet men between the ages of 26 and 32.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3340907/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
																		                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/2898406/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/7v/t/4fa~0i.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Dudutuli246</strong><br />
                           <span>I'm a 34 year old woman looking to meet men between the ages of 35 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/2898406/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
															                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3364723/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/qp/t/48j~c0.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Foxy88</strong><br />
                           <span>I'm a 22 year old woman looking to meet men between the ages of 25 and 33.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3364723/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3058964/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/vi/t/kb8~nv.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>curvalicious</strong><br />
                           <span>I'm a 30 year old woman looking to meet men between the ages of 25 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3058964/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3330645/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/pg/t/dxx~lb.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>mitch09</strong><br />
                           <span>I'm a 29 year old woman looking to meet men between the ages of 35 and 40.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3330645/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/2940379/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/9p/t/0t7~al.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>lulubaby</strong><br />
                           <span>I'm a 33 year old woman looking to meet men between the ages of 30 and 70.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/2940379/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/2925386/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/ab/t/p8q~kn.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>mako_001</strong><br />
                           <span>I'm a 35 year old woman looking to meet men between the ages of 35 and 70.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/2925386/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3189201/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/m4/t/csx~lk.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>ProVoq</strong><br />
                           <span>I'm a 43 year old woman looking to meet men between the ages of 50 and 70.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3189201/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3406025/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/s5/t/03t~ur.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Thel_89_zzz</strong><br />
                           <span>I'm a 25 year old woman looking to meet men between the ages of 30 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3406025/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3117491/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/hg/t/tgz~i2.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>ntando_784</strong><br />
                           <span>I'm a 34 year old woman looking to meet men between the ages of 40 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3117491/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3336380/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/pn/t/id8~9e.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>LadyJimpster</strong><br />
                           <span>I'm a 23 year old woman looking to meet men between the ages of 22 and 28.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3336380/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3477510/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/v8/t/j9i~tk.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>fungi1971</strong><br />
                           <span>I'm a 43 year old woman looking to meet men between the ages of 40 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3477510/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3451016/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/u2/t/ytk~if.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>NiniEmma</strong><br />
                           <span>I'm a 63 year old woman looking to meet men between the ages of 60 and 70.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3451016/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3347059/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/q4/t/qlv~1k.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>samke_722</strong><br />
                           <span>I'm a 22 year old woman looking to meet men between the ages of 22 and 25.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3347059/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3314249/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/ou/t/1ah~qj.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Yahoo</strong><br />
                           <span>I'm a 42 year old woman looking to meet men between the ages of 41 and 60.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3314249/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/2761538/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/1s/t/6te~70.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Noxy727</strong><br />
                           <span>I'm a 27 year old woman looking to meet men between the ages of 30 and 36.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/2761538/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/2953757/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/ab/t/b4t~7k.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Jade_76</strong><br />
                           <span>I'm a 38 year old woman looking to meet men between the ages of 36 and 42.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/2953757/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3532845/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/17/t/pyl~g1.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Voicelady</strong><br />
                           <span>I'm a 40 year old woman looking to meet men between the ages of 35 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3532845/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/2946287/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/a1/t/5db~eg.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>fiksBee</strong><br />
                           <span>I'm a 25 year old woman looking to meet men between the ages of 26 and 40.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/2946287/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3180060/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/pi/t/5r0~31.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>smilyz</strong><br />
                           <span>I'm a 43 year old woman looking to meet men between the ages of 35 and 48.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3180060/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3128856/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0m/t/28o~tl.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>bontle212</strong><br />
                           <span>I'm a 42 year old woman looking to meet men between the ages of 45 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3128856/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3431023/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/t5/t/je7~e4.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>mcgoyer</strong><br />
                           <span>I'm a 26 year old woman looking to meet men between the ages of 27 and 35.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3431023/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3464364/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/uh/t/94c~co.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>SexLips</strong><br />
                           <span>I'm a 26 year old woman looking to meet men between the ages of 25 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3464364/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3548393/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1n/t/1yh~mo.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>honeybee_036</strong><br />
                           <span>I'm a 25 year old woman looking to meet men between the ages of 25 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3548393/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3463559/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0l/t/8hz~94.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Noks76</strong><br />
                           <span>I'm a 38 year old woman looking to meet men between the ages of 37 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3463559/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
																		                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3332937/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0j/t/fpl~l5.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>cuddles79</strong><br />
                           <span>I'm a 35 year old woman looking to meet men between the ages of 36 and 47.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3332937/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3542674/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1g/t/xjm~2a.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Leematt</strong><br />
                           <span>I'm a 25 year old woman looking to meet men between the ages of 25 and 29.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3542674/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3502725/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0v/t/2px~n1.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>kauwel</strong><br />
                           <span>I'm a 40 year old woman looking to meet men between the ages of 39 and 55.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3502725/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3527318/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0s/t/lp2~37.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>lala408</strong><br />
                           <span>I'm a 46 year old woman looking to meet men between the ages of 40 and 55.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3527318/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3163425/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/v9/t/swx~mq.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Butiful</strong><br />
                           <span>I'm a 44 year old woman looking to meet men between the ages of 44 and 63.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3163425/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3242486/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/m3/t/hx2~ur.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>kncyLuv</strong><br />
                           <span>I'm a 28 year old woman looking to meet men between the ages of 27 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3242486/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
															                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3522013/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0p/t/hlp~9u.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>ChocLatte</strong><br />
                           <span>I'm a 44 year old woman looking to meet men between the ages of 40 and 60.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3522013/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3492398/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/vg/t/ur2~8v.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Bathandwa83</strong><br />
                           <span>I'm a 31 year old woman looking to meet men between the ages of 31 and 47.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3492398/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3549910/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1p/t/34m~9c.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>PrincessEdelweiss</strong><br />
                           <span>I'm a 43 year old woman looking to meet men between the ages of 35 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3549910/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3309040/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/om/t/x9s~ti.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Leratomntande</strong><br />
                           <span>I'm a 23 year old woman looking to meet men between the ages of 25 and 30.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3309040/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3363124/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/r0/t/304~d1.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Nola_505</strong><br />
                           <span>I'm a 40 year old woman looking to meet men between the ages of 35 and 47.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3363124/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3323455/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/ph/t/8e7~lj.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>RareT0paz</strong><br />
                           <span>I'm a 35 year old woman looking to meet men between the ages of 38 and 60.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3323455/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3538460/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1a/t/uak~b5.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>zama1zn</strong><br />
                           <span>I'm a 37 year old woman looking to meet men between the ages of 38 and 47.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3538460/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3207181/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/l0/t/qod~9m.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Sthandwasakhesit</strong><br />
                           <span>I'm a 29 year old woman looking to meet men between the ages of 30 and 35.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3207181/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3525941/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0s/t/kmt~lr.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Monique_2014</strong><br />
                           <span>I'm a 31 year old woman looking to meet men between the ages of 29 and 39.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3525941/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3492787/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/vg/t/v1v~oi.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>marryme2014</strong><br />
                           <span>I'm a 34 year old woman looking to meet men between the ages of 37 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3492787/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
															                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3337304/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/po/t/j2w~fl.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>tkay011</strong><br />
                           <span>I'm a 23 year old woman looking to meet women between the ages of 25 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3337304/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3546488/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1k/t/0hk~rt.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>TennysonBeck</strong><br />
                           <span>I'm a 39 year old woman looking to meet men between the ages of 36 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3546488/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3524561/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0o/t/jkh~k2.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Cyndilouper</strong><br />
                           <span>I'm a 35 year old woman looking to meet men between the ages of 30 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3524561/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3373062/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/r2/t/ao6~9l.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>ally_charmy80</strong><br />
                           <span>I'm a 34 year old woman looking to meet men between the ages of 40 and 55.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3373062/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3039850/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/e2/t/5ka~7d.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Sweetlipsss627</strong><br />
                           <span>I'm a 21 year old woman looking to meet men between the ages of 25 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3039850/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3383736/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/tf/t/iwo~62.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>TABIEE</strong><br />
                           <span>I'm a 29 year old woman looking to meet men between the ages of 40 and 100.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3383736/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3324045/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/p8/t/8ul~s1.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>sbobo736</strong><br />
                           <span>I'm a 27 year old woman looking to meet men between the ages of 25 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3324045/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3547459/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1q/t/18j~n0.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>MissD123</strong><br />
                           <span>I'm a 39 year old woman looking to meet men between the ages of 36 and 47.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3547459/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
															                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3418427/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/sk/t/9ob~t4.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>blosoble</strong><br />
                           <span>I'm a 27 year old woman looking to meet men between the ages of 28 and 40.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3418427/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/2891074/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/7h/t/yrm~i7.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>TT200</strong><br />
                           <span>I'm a 25 year old woman looking to meet men between the ages of 25 and 35.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/2891074/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3182001/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0b/t/78x~o8.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>kgotlas</strong><br />
                           <span>I'm a 34 year old woman looking to meet men between the ages of 30 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3182001/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3515214/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0c/t/ccu~o3.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>maria8022</strong><br />
                           <span>I'm a 34 year old woman looking to meet men between the ages of 40 and 60.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3515214/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3466517/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/uh/t/as5~di.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Lindz4life1</strong><br />
                           <span>I'm a 39 year old woman looking to meet men between the ages of 35 and 65.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3466517/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
																		                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3538155/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/19/t/u23~ta.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Bizkit2808</strong><br />
                           <span>I'm a 38 year old woman looking to meet men between the ages of 30 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3538155/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3376239/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/r5/t/d4f~gb.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Melone</strong><br />
                           <span>I'm a 27 year old woman looking to meet men between the ages of 30 and 42.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3376239/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3419610/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/st/t/al6~bk.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>LolliCandy</strong><br />
                           <span>I'm a 20 year old woman looking to meet men between the ages of 21 and 35.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3419610/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3480898/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/v7/t/lvm~8b.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Casiopiea40</strong><br />
                           <span>I'm a 44 year old woman looking to meet men between the ages of 35 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3480898/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3395662/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/rp/t/s3y~i6.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>DDeeZA</strong><br />
                           <span>I'm a 45 year old woman looking to meet women between the ages of 19 and 50.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3395662/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3550113/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1p/t/3a9~ef.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Lola10</strong><br />
                           <span>I'm a 25 year old woman looking to meet men between the ages of 25 and 35.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3550113/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3508896/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1i/t/7hc~bk.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>danda100</strong><br />
                           <span>I'm a 47 year old woman looking to meet men between the ages of 37 and 52.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3508896/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3285454/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/no/t/f2m~m8.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>mello_185</strong><br />
                           <span>I'm a 26 year old woman looking to meet men between the ages of 25 and 60.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3285454/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3404018/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/s3/t/yk2~ff.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>leez83</strong><br />
                           <span>I'm a 31 year old woman looking to meet men between the ages of 25 and 42.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3404018/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/2936967/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/bb/t/y6f~hg.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Emjae</strong><br />
                           <span>I'm a 38 year old woman looking to meet men between the ages of 35 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/2936967/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3544911/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1j/t/z9r~33.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>briluu</strong><br />
                           <span>I'm a 24 year old woman looking to meet men between the ages of 27 and 30.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3544911/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3525640/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0t/t/keg~2p.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Dlodlolas75</strong><br />
                           <span>I'm a 39 year old woman looking to meet men between the ages of 43 and 49.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3525640/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3186083/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/k9/t/aeb~3c.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Roroe</strong><br />
                           <span>I'm a 26 year old woman looking to meet men and women between the ages of 22 and 30.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3186083/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/2886474/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/7b/t/v7u~50.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>spesy59</strong><br />
                           <span>I'm a 35 year old woman looking to meet men between the ages of 32 and 40.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/2886474/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3483443/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/v6/t/nub~re.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Switnesspopo</strong><br />
                           <span>I'm a 25 year old woman looking to meet men between the ages of 29 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3483443/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3219736/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0r/t/0d4~7o.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Rosey903</strong><br />
                           <span>I'm a 40 year old woman looking to meet men between the ages of 38 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3219736/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3470928/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/um/t/e6o~tp.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>BOTSHELOMAN</strong><br />
                           <span>I'm a 32 year old woman looking to meet men between the ages of 35 and 42.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3470928/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3508905/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/0a/t/7hl~k3.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Bods</strong><br />
                           <span>I'm a 53 year old woman looking to meet men between the ages of 45 and 60.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3508905/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3462666/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/ui/t/7t6~1v.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>hellena_596</strong><br />
                           <span>I'm a 37 year old woman looking to meet men between the ages of 37 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3462666/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3254947/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/mh/t/rj7~uo.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>lexy278</strong><br />
                           <span>I'm a 32 year old woman looking to meet men between the ages of 30 and 40.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3254947/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3316497/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/p0/t/30x~6a.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>FanceFace</strong><br />
                           <span>I'm a 27 year old woman looking to meet men between the ages of 28 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3316497/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3284223/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/us/t/e4f~i9.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>zaneli</strong><br />
                           <span>I'm a 34 year old woman looking to meet men between the ages of 35 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3284223/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3327250/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/pc/t/bbm~lr.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Bonwel</strong><br />
                           <span>I'm a 30 year old woman looking to meet men between the ages of 32 and 36.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3327250/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3334757/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/pl/t/h45~8g.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>LavishT</strong><br />
                           <span>I'm a 21 year old woman looking to meet men and women between the ages of 25 and 27.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3334757/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3431091/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/tq/t/jg3~om.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>nwaolisa</strong><br />
                           <span>I'm a 31 year old woman looking to meet men between the ages of 32 and 41.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3431091/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
						                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3187098/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/po/t/b6i~0l.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>vicky74</strong><br />
                           <span>I'm a 40 year old woman looking to meet men between the ages of 38 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3187098/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3546329/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1k/t/0d5~jo.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Phoenix1983</strong><br />
                           <span>I'm a 31 year old woman looking to meet men between the ages of 29 and 35.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3546329/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3063803/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/f4/t/o1n~fj.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Blaq_chic</strong><br />
                           <span>I'm a 26 year old woman looking to meet men between the ages of 25 and 45.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3063803/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
									                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3541155/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/4/1n/t/wdf~bl.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>armor2014</strong><br />
                           <span>I'm a 55 year old woman looking to meet men between the ages of 45 and 70.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3541155/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
												                	<div class="home_dating_content">
                    	<div class="home_dating_image">
                			<a href="http://www.ioldating.co.za/s/d/3238336/a/16405/" target="_blank" >
                              <img src="http://57.feed.datinglab.net/photos/3/m2/t/eps~53.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                            </a>
                        </div>
                        <div class="home_dating_text">
                        	<strong>Calmine</strong><br />
                           <span>I'm a 24 year old woman looking to meet men between the ages of 25 and 40.</span><br />
                           <a href="http://www.ioldating.co.za/s/d/3238336/a/16405/" target="_blank">View Profile</a>
                        </div>
                        <div style="clear:both"></div>
                    </div>
				</div>

<div id="home_dating_men" class="home_dating_tab2_3">
		   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3464442/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/uf/t/96i~9u.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Satisfactor99</strong><br />
                   <span>I'm a 37 year old man looking to meet women between the ages of 18 and 35.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3464442/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3545734/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/1j/t/zwm~tm.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>THOKZANHLA</strong><br />
                   <span>I'm a 44 year old man looking to meet women between the ages of 25 and 44.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3545734/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3202372/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/q0/t/mys~p7.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>RealEstate</strong><br />
                   <span>I'm a 53 year old man looking to meet women between the ages of 40 and 52.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3202372/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2624874/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/93/t/9d6~hc.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>IceTy</strong><br />
                   <span>I'm a 42 year old man looking to meet women between the ages of 18 and 42.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2624874/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2900211/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/7v/t/5tf~6b.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Bento1</strong><br />
                   <span>I'm a 52 year old man looking to meet women between the ages of 38 and 50.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2900211/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3399451/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/rt/t/v17~rd.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Lucky123nxt</strong><br />
                   <span>I'm a 36 year old man looking to meet women between the ages of 18 and 40.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3399451/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1474886/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/i3/t/m12~14.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>pianoman40</strong><br />
                   <span>I'm a 60 year old man looking to meet women between the ages of 44 and 65.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1474886/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3510043/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/06/t/8d7~7c.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Kelvin7777</strong><br />
                   <span>I'm a 50 year old man looking to meet women between the ages of 42 and 56.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3510043/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3139587/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/id/t/air~j5.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>charged</strong><br />
                   <span>I'm a 40 year old man looking to meet women between the ages of 25 and 35.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3139587/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3432934/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/t7/t/kva~nl.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Easylikesundaymornin</strong><br />
                   <span>I'm a 52 year old man looking to meet women between the ages of 25 and 51.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3432934/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3100139/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/pb/t/g2z~co.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>TSKgosiemang</strong><br />
                   <span>I'm a 52 year old man looking to meet women between the ages of 35 and 50.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3100139/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2146496/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/05/t/08w~h4.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>lonelylooking4lady</strong><br />
                   <span>I'm a 38 year old man looking to meet women between the ages of 24 and 30.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2146496/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3489732/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/02/t/sp0~cd.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>vululami2009</strong><br />
                   <span>I'm a 28 year old man looking to meet women between the ages of 18 and 26.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3489732/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1104166/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/1/46/t/nza~b5.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>WestPalm</strong><br />
                   <span>I'm a 55 year old man looking to meet women between the ages of 18 and 100.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1104166/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1700805/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/r8/t/gcl~pa.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Chacal</strong><br />
                   <span>I'm a 44 year old man looking to meet women between the ages of 30 and 40.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1700805/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3516212/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/0d/t/d4k~rr.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>ngla35</strong><br />
                   <span>I'm a 38 year old man looking to meet women between the ages of 18 and 100.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3516212/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3527596/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/0t/t/lws~7l.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Lawrence218</strong><br />
                   <span>I'm a 26 year old man looking to meet women between the ages of 25 and 39.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3527596/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3454062/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/va/t/166~41.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>MJ4life</strong><br />
                   <span>I'm a 40 year old man looking to meet women between the ages of 18 and 40.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3454062/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2123572/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/sr/t/ik4~e8.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>dlalo</strong><br />
                   <span>I'm a 44 year old man looking to meet women between the ages of 18 and 100.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2123572/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3360486/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/qj/t/0yu~t6.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Thamza_77</strong><br />
                   <span>I'm a 37 year old man looking to meet women between the ages of 18 and 35.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3360486/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2755405/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/1j/t/231~v4.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>oceanmoon</strong><br />
                   <span>I'm a 61 year old man looking to meet women between the ages of 41 and 55.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2755405/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3503941/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/01/t/3np~nc.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Mandevho</strong><br />
                   <span>I'm a 36 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3503941/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2832943/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/io/t/pwv~j3.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>kpl23</strong><br />
                   <span>I'm a 35 year old man looking to meet women between the ages of 26 and 34.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2832943/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1944455/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/1o/t/ocn~57.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>chumisto</strong><br />
                   <span>I'm a 34 year old man looking to meet women between the ages of 18 and 100.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1944455/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2915748/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/8n/t/ht0~qi.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>tonym</strong><br />
                   <span>I'm a 44 year old man looking to meet women between the ages of 24 and 35.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2915748/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3242783/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/vl/t/i5b~rf.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>bobbylava</strong><br />
                   <span>I'm a 35 year old man looking to meet women between the ages of 18 and 31.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3242783/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3428707/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/vs/t/hlv~i7.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>loner729</strong><br />
                   <span>I'm a 40 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3428707/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1263260/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/1/9f/t/2qk~8h.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>raffo</strong><br />
                   <span>I'm a 63 year old man looking to meet women between the ages of 40 and 50.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1263260/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3134638/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/ns/t/6pa~k2.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>liveforjoy</strong><br />
                   <span>I'm a 56 year old man looking to meet women between the ages of 43 and 53.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3134638/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3483070/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/v5/t/njy~lj.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>GastFR</strong><br />
                   <span>I'm a 39 year old man looking to meet women between the ages of 25 and 39.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3483070/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1941286/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/uf/t/lwm~2o.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>iko_103</strong><br />
                   <span>I'm a 37 year old man looking to meet women between the ages of 25 and 34.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1941286/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3271578/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/n7/t/4d6~1j.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Rendzo</strong><br />
                   <span>I'm a 47 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3271578/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2282173/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/1k/t/wxp~cs.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Qtip</strong><br />
                   <span>I'm a 30 year old man looking to meet women between the ages of 26 and 32.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2282173/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3495978/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/vq/t/xii~o7.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Tuzet</strong><br />
                   <span>I'm a 27 year old man looking to meet women between the ages of 25 and 33.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3495978/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3510391/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/06/t/8mv~k4.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Mokoka01</strong><br />
                   <span>I'm a 42 year old man looking to meet women between the ages of 28 and 35.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3510391/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3501446/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/vr/t/1qe~5u.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Cool_S</strong><br />
                   <span>I'm a 28 year old man looking to meet women between the ages of 18 and 27.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3501446/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1754205/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/2f/t/ljx~m4.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>GD1</strong><br />
                   <span>I'm a 70 year old man looking to meet women between the ages of 55 and 65.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1754205/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3489054/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/vc/t/s66~tg.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>marane</strong><br />
                   <span>I'm a 51 year old man looking to meet women between the ages of 40 and 60.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3489054/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3360671/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/qp/t/13z~09.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Kabili</strong><br />
                   <span>I'm a 41 year old man looking to meet women between the ages of 18 and 36.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3360671/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1984662/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/3b/t/jdi~v7.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Pappers</strong><br />
                   <span>I'm a 71 year old man looking to meet women between the ages of 50 and 65.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1984662/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3522092/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/0l/t/hnw~dc.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Dayo78</strong><br />
                   <span>I'm a 36 year old man looking to meet women between the ages of 20 and 50.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3522092/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3513072/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/0d/t/apc~l3.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Mpeks</strong><br />
                   <span>I'm a 22 year old man looking to meet women between the ages of 18 and 30.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3513072/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3155831/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/12/t/n1z~5h.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Thulani1234</strong><br />
                   <span>I'm a 42 year old man looking to meet women between the ages of 27 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3155831/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1904936/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/08/t/tuw~4m.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>jakobus</strong><br />
                   <span>I'm a 34 year old man looking to meet women between the ages of 18 and 100.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1904936/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3531211/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/10/t/op7~rh.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>myth909</strong><br />
                   <span>I'm a 34 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3531211/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3445320/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/tn/t/ufc~u7.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>mthamis456</strong><br />
                   <span>I'm a 29 year old man looking to meet women between the ages of 30 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3445320/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3298031/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/o8/t/orz~ds.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>bloodmoney370</strong><br />
                   <span>I'm a 43 year old man looking to meet women between the ages of 30 and 50.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3298031/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3543216/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/1g/t/xyo~m5.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>dev_xoxox52</strong><br />
                   <span>I'm a 53 year old man looking to meet women between the ages of 41 and 65.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3543216/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3470754/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/0e/t/e1u~fp.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Jabz_0</strong><br />
                   <span>I'm a 29 year old man looking to meet women between the ages of 25 and 36.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3470754/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3495754/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/vk/t/xca~31.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Ernie_Manyesa</strong><br />
                   <span>I'm a 32 year old man looking to meet women between the ages of 20 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3495754/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2544531/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/p5/t/jdf~dd.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>princepoqo</strong><br />
                   <span>I'm a 29 year old man looking to meet women between the ages of 18 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2544531/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/995000/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/ru/t/bqw~3b.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>mfhalim</strong><br />
                   <span>I'm a 42 year old man looking to meet women between the ages of 18 and 35.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/995000/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3505751/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/00/t/51z~pv.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Fanzonator</strong><br />
                   <span>I'm a 28 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3505751/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2718445/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/v4/t/9kd~qf.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>loverboy111_tvs</strong><br />
                   <span>I'm a 44 year old man looking to meet women between the ages of 26 and 40.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2718445/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3436299/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/tc/t/ngr~e0.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>loverman26</strong><br />
                   <span>I'm a 40 year old man looking to meet women between the ages of 18 and 30.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3436299/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2912065/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/ub/t/eyp~cd.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Pheman</strong><br />
                   <span>I'm a 26 year old man looking to meet women between the ages of 21 and 32.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2912065/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3426002/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/su/t/fiq~s8.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Sir_Frances</strong><br />
                   <span>I'm a 49 year old man looking to meet women between the ages of 22 and 40.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3426002/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3543334/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/1g/t/y1y~ro.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Terror000</strong><br />
                   <span>I'm a 28 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3543334/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3340288/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/q2/t/lds~d8.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>mattgeah</strong><br />
                   <span>I'm a 31 year old man looking to meet women between the ages of 25 and 40.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3340288/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3357392/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/qg/t/ykw~na.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>simt</strong><br />
                   <span>I'm a 36 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3357392/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3509622/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/0h/t/81i~gv.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>ntuthuko424</strong><br />
                   <span>I'm a 59 year old man looking to meet women between the ages of 25 and 50.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3509622/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2318983/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/g0/t/pc7~j7.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>STONE_228</strong><br />
                   <span>I'm a 42 year old man looking to meet women between the ages of 18 and 35.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2318983/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3392381/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/tc/t/pkt~ps.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>tsvoritsvoto</strong><br />
                   <span>I'm a 27 year old man looking to meet women between the ages of 18 and 25.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3392381/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1048551/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/1/ri/t/h2f~b8.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Deejay_homy</strong><br />
                   <span>I'm a 46 year old man looking to meet women between the ages of 18 and 42.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1048551/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2599314/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/vu/t/pn6~27.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>DreamingAwake</strong><br />
                   <span>I'm a 48 year old man looking to meet women between the ages of 28 and 44.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2599314/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1678861/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/4i/t/zf1~kt.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>shooter_949</strong><br />
                   <span>I'm a 51 year old man looking to meet women between the ages of 20 and 50.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1678861/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3523132/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/0m/t/igs~tt.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Ma1010n</strong><br />
                   <span>I'm a 26 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3523132/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3436861/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/un/t/nwd~gi.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Mash70</strong><br />
                   <span>I'm a 44 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3436861/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3485770/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/15/t/pmy~5s.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Phistos_Number_1</strong><br />
                   <span>I'm a 38 year old man looking to meet women between the ages of 33 and 40.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3485770/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3161495/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/je/t/rfb~4f.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>CoolnCalm</strong><br />
                   <span>I'm a 35 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3161495/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1856651/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/1/ug/t/sln~o8.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Mahlobo</strong><br />
                   <span>I'm a 46 year old man looking to meet women between the ages of 28 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1856651/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2545180/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/qd/t/jvg~9j.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>2282B</strong><br />
                   <span>I'm a 48 year old man looking to meet women between the ages of 26 and 37.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2545180/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/934714/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/1/0r/t/18a~io.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>shiva709</strong><br />
                   <span>I'm a 56 year old man looking to meet women between the ages of 45 and 56.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/934714/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3096816/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/hm/t/dio~8l.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Washe</strong><br />
                   <span>I'm a 37 year old man looking to meet women between the ages of 25 and 33.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3096816/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1907225/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/2/0f/t/vmh~ho.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>michaelangelo</strong><br />
                   <span>I'm a 27 year old man looking to meet women between the ages of 18 and 25.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1907225/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/1291124/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/dj/t/o8k~5h.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>tripplekkkk</strong><br />
                   <span>I'm a 37 year old man looking to meet women between the ages of 18 and 30.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/1291124/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3153762/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/j9/t/lgi~56.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Vbe2014</strong><br />
                   <span>I'm a 37 year old man looking to meet women between the ages of 25 and 30.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3153762/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		   		   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3485510/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/v8/t/pfq~mt.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>catcher182</strong><br />
                   <span>I'm a 22 year old man looking to meet men between the ages of 20 and 24.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3485510/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3061971/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/sg/t/mmr~os.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>bangstar</strong><br />
                   <span>I'm a 22 year old man looking to meet women between the ages of 19 and 23.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3061971/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3144992/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/pe/t/eow~kq.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Shadra143</strong><br />
                   <span>I'm a 22 year old man looking to meet women between the ages of 18 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3144992/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3393192/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/uh/t/q7c~d5.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Mxo87</strong><br />
                   <span>I'm a 27 year old man looking to meet women between the ages of 18 and 30.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3393192/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3315089/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/ou/t/1xt~jl.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Bheki_038</strong><br />
                   <span>I'm a 50 year old man looking to meet women between the ages of 29 and 43.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3315089/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3520010/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/4/0i/t/g22~i9.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>sbo123sss</strong><br />
                   <span>I'm a 30 year old man looking to meet women between the ages of 25 and 45.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3520010/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3400558/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/rv/t/vvy~mb.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>joseman200</strong><br />
                   <span>I'm a 60 year old man looking to meet women between the ages of 40 and 70.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3400558/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   		           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/2684083/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/1o/t/j1v~14.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>gothicD</strong><br />
                   <span>I'm a 44 year old man looking to meet women between the ages of 18 and 37.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/2684083/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				           	<div class="home_dating_content">
            	<div class="home_dating_image">
					<a href="http://www.ioldating.co.za/s/d/3076373/a/16405/" target="_blank" >
        			<img src="http://57.feed.datinglab.net/photos/3/fn/t/xqt~k6.jpg" alt="IOL - dating" title="" class="dating_teaseres_pic_restrictions" />
                    </a>
        		</div>
                <div class="home_dating_text">
                	<strong>Jb24golf</strong><br />
                   <span>I'm a 40 year old man looking to meet women between the ages of 32 and 38.</span><br />
                   <a href="http://www.ioldating.co.za/s/d/3076373/a/16405/" target="_blank">View Profile</a>
                </div>
                <div style="clear:both"></div>
            </div>
				   	</div>





<div id="home_dating_search" class="home_dating_tab2_3">

<div class="home_dating_search_cont">

<!-- Start Update graphic and text content as required -->


     <span class="home_dating_search_head">Find your perfect match now!</span>

<form action="http://www.ioldating.co.za/s/find/search.php" method="post" target="winMM" name="frmMM" id="frmMM">
	<input type="hidden" name="sub" id="sub" value="yes" />
	<input type="hidden" name="xqs" id="xqs"value="yes" />
	<input type="hidden" name="aID" id="aID" value="16783" />
	<table>
  <tr><td width="100">
I am a:
  </td><td>
<select name="gender" id="gender" class="home_dating_search_input">
	   <option value="1">Woman</option>
       <option value="2" selected="selected">Man</option>
  </select></td></tr>
  
  <tr><td>
	Looking for:</td><td><select name="mGender" id="mGender" class="home_dating_search_input">
				<option value="1" selected="selected">Women</option>
                <option value="2">Men</option>
                <option value="3">Men &amp; Women</option>
             </select>
			 <br /><br />
  </td></tr>		 
			 

  </table>			 
			 
	<table> <tr><td>&nbsp;</td></tr></table>		 
			 
			 
	Age Range: <br /><a name="c"></a>
	     <table><tr>
        <td width="120"> From</td><td>
	       <select name="mAgeMin" id="mAgeMin" class="home_dating_search_input2" onchange="checkAge(this);">
				<option>18</option><option>19</option><option>20</option><option>21</option>
                <option>22</option><option>23</option><option>24</option><option selected="selected">25</option>
				<option>26</option><option>27</option>
                <option>28</option><option>29</option><option>30</option><option>31</option><option>32</option><option>33</option>
<option>34</option><option>35</option><option>36</option><option>37</option><option>38</option><option>39</option>
<option>40</option><option>41</option><option>42</option><option>43</option><option>44</option><option>45</option>
<option>46</option><option>47</option><option>48</option><option>49</option><option>50</option><option>51</option>
<option>52</option><option>53</option><option>54</option><option>55</option><option>56</option><option>57</option>
<option>58</option><option>59</option><option>60</option><option>61</option><option>62</option><option>63</option>
<option>64</option><option>65</option><option>66</option><option>67</option><option>68</option><option>69</option>
<option>70</option><option>71</option><option>72</option><option>73</option><option>74</option><option>75</option>
<option>76</option><option>77</option><option>78</option><option>79</option><option>80</option><option>81</option>
<option>82</option><option>83</option><option>84</option><option>85</option><option>86</option><option>87</option>
<option>88</option><option>89</option><option>90</option><option>91</option><option>92</option><option>93</option>
<option>94</option><option>95</option><option>96</option><option>97</option><option>98</option><option>99</option>
<option>100</option></select></td>
<td></td>
		
<td>To </td><td> <select name="mAgeMax" id="mAgeMax" class="home_dating_search_input2" onchange="checkAge(this);"><option>18</option><option>19</option><option>20</option><option>21</option>
<option>22</option><option>23</option><option>24</option><option>25</option><option>26</option><option>27</option>
<option>28</option><option>29</option><option>30</option><option>31</option><option>32</option><option>33</option>
<option>34</option><option selected="selected">35</option><option>36</option><option>37</option><option>38</option><option>39</option>
<option>40</option><option>41</option><option>42</option><option>43</option><option>44</option><option>45</option>
<option>46</option><option>47</option><option>48</option><option>49</option><option>50</option><option>51</option>
<option>52</option><option>53</option><option>54</option><option>55</option><option>56</option><option>57</option>
<option>58</option><option>59</option><option>60</option><option>61</option><option>62</option><option>63</option>
<option>64</option><option>65</option><option>66</option><option>67</option><option>68</option><option>69</option>
<option>70</option><option>71</option><option>72</option><option>73</option><option>74</option><option>75</option>
<option>76</option><option>77</option><option>78</option><option>79</option><option>80</option><option>81</option>
<option>82</option><option>83</option><option>84</option><option>85</option><option>86</option><option>87</option>
<option>88</option><option>89</option><option>90</option><option>91</option><option>92</option><option>93</option>
<option>94</option><option>95</option><option>96</option><option>97</option><option>98</option><option>99</option>
<option>100</option></select>


<input type="hidden" name="mCountryID[]" id="mCountryID" value="za" />
<input type="hidden" name="mHasPhoto" id="mHasPhoto" value="1" />
         </td></tr>
		 <tr><td>&nbsp;</td></tr>	 
		 <tr><td>

<input type="image" name="quickSearch" id="quickSearch" src="/images/search_form.jpg" alt="Search" border="0" />
</td></tr></table></form>
</div>
</div>
</div>



<blockquote>

<script type="text/javascript">
ddtabmenu.definemenu("home_dating_head",0)
</script>

<script type="text/javascript">
	<!--
		// Check that min & max are the right way round
		function checkAge (formElement) {
			var mAgeMin = formElement.form.mAgeMin.selectedIndex;
			var mAgeMax = formElement.form.mAgeMax.selectedIndex;
			if (mAgeMax < mAgeMin) {
				formElement.form.mAgeMin.options[mAgeMax].selected = true;
				formElement.form.mAgeMax.options[mAgeMin].selected = true;
			}
			return true;
		}
	//-->
	</script>


</blockquote>


          
        		 
 



<div id="sp_links">
  <div id="sp_links_head"><p class="sp_links_headers">Services</p></div>
  <div id="sp_links_body">
    <div id="sp_links_text_left">
      <ul class="menu_tab_lists">
                                                      <li><a href="http://adserver.adtech.de/?adlink|3.0|567|1104792|1|16|AdId=9171969;BnId=1;link=http://ad.doubleclick.net/clk;259736234;99775611;z" rel="nofollow" class="menu_tab_lists" >Need cash quick? wonga.com</a></li>
                                                                                  <li><a href="http://adserver.adtech.de/?adlink|3.0|559|2122637|1|16|AdId=7297318;BnId=1;link=http://www.metropolitan.co.za/digital/iol/index.htm?febtxt001" rel="nofollow" class="menu_tab_lists" >Get R30 000 funeral cover</a></li>
                                                                                  <li><a href="http://adserver.adtech.de/?adlink%7C3.0%7C585%7C1102745%7C1%7C16%7CAdId=8129288;BnId=1;link=http://www.alloutlotto.com/?affiliateCode=8" rel="nofollow" class="menu_tab_lists" >Play UK Lottery - Go AllOut</a></li>
                                                                                  <li><a href="http://adserver.adtech.de/?adlink|3.0|585|1102745|1|16|AdId=5068811;BnId=1;link=http://www.ioltravel.co.za" rel="nofollow" class="menu_tab_lists" >Travel News</a></li>
                                          </ul>
    </div>
    <div id="sp_links_text_right">
      <ul class="menu_tab_lists">
                                                						                        <li><a href="http://bulksms.2way.co.za" rel="nofollow" class="menu_tab_lists"  target='_blank'>Buy SMS Bundles</a></li>
                                                          						                        <li><a href="http://adserver.adtech.de/?adlink|3.0|585|1102745|1|16|AdId=7548793;BnId=1;link=http://adserver.adtech.de/?adlink|3.0|559|2122637|1|16|AdId=7540407;BnId=1;link=http://www.oldmutual.co.za/personal/educ" rel="nofollow" class="menu_tab_lists"  target='_blank'>Education plan from R150/m</a></li>
                                                          						                        <li><a href="http://adserver.adtech.de/?adlink%7C3.0%7C567%7C1104792%7C1%7C16%7CAdId=9017502;BnId=1;link=http://www.dialdirect.co.za/express-claims?vdn=15962" rel="nofollow" class="menu_tab_lists"  target='_blank'>Save up to 25% on your insurance: Dial Direct</a></li>
                                                          						                        <li><a href="http://adserver.adtech.de/?adlink|3.0|585|1102745|1|16|AdId=8067860;BnId=1;link=http://www.1lifedirect.co.za/quick-quote/?vdn=21474" rel="nofollow" class="menu_tab_lists"  target='_blank'>Simple affordable life cover</a></li>
                        </ul>
    </div>
  </div>
</div>

          
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4350738|0|170|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4350738|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4350738|0|170|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
      
  
                                      
                  
    
      
        


 	
			    <script type="text/javascript">
        $(document).ready(function() {
           var voteuid = new Date().getTime();
           $.get('http://www.iol.co.za:80/isolezwe/7.12506?ot=inmsa.AjaxPageLayout.ot&r=http://www.iol.co.za:80/isolezwe/ezikamalema-zethule-abazo-ekzn-1.1667768&view=right&voteuid='+voteuid, loadPoll7_12506HTML);
        });
        function loadPoll7_12506HTML(pollHTML) {            $('div#poll7_12506').html(pollHTML);
        }
    </script>

    <div id="poll7_12506" class="poll_container">

    </div>
		
	<div>
			</div>
	
	
	
	
	
	
      
  
                                      
                  
    
      
        
        
                                  <div id="jobs_prop_class_motor"> 
              <div id="71741373356533" class="third_col_head">
                <ul class="menu_tab">
                                      <li>
                                              <a href="http://www.iolproperty.co.za" target="_blank" rel="menu_tab_171741373356533">
                                            Property</a>
                    </li>
                                     <li>
                                              <a href="http://www.wegotads.co.za" target="_blank" rel="menu_tab_271741373356533">
                                            Classifieds</a>
                    </li>
                                     <li>
                                              <a href="http://www.iolmotoring.co.za" target="_blank" rel="menu_tab_371741373356533">
                                            Motors</a>
                    </li>
                                </ul> 
             </div>
                            <div id="menu_tab_171741373356533" class="menu_tab_1">
							   <div style="width: 300px; height:140px; overflow:hidden; border: 0px; border:none;"> <iframe src="http://www.iolproperty.co.za/featured_property.jsp?type=new_home" style="width: 310px; height:150px; overflow:hidden;  border:none;"  frameborder="0"> </iframe>  </div>
               </div>
                            <div id="menu_tab_271741373356533" class="menu_tab_2">
							   <div style="width: 300px; height: 140px; background-image: url('/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/wegotads_bg.jpg'); position: absolute; top: 0px; float: left; z-index: 19px;">
<div style=" width:130px; height:111px; float:left; margin:0px 0px 0px 0px; padding:0px;">
 <a href="http://www.wegotads.co.za/"><img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/wegotads_pic.jpg" alt="" border="0"/>
</a>
 </div>
 
 <div style=" width: 162px; float:left; margin:11px 0px 0px 0px; padding:0px; height: 101px;">
<p style="margin-top: 0px; margin-left:0px; padding: 0 7px ; clear: inherit;">
Whether you are a buyer or seller, wegotads is your online marketplace.  <br /> 
<a href="http://www.wegotads.co.za/" class="teasers_right_read_more">Wegotads &raquo;</a><br /></p>
</div>

<div>
<div style="width:142px; float:left; margin: 0px 15px 0px 5px;"><a href="http://www.wegotads.co.za/"><img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/your_local_market_place.jpg" alt="" border="0"/>

</a></div>
<div style="float:left; margin: 0px 5px 0px 10px;" ><a href="http://www.wegotads.co.za/">
<img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/wegotads_logo.jpg" alt="" border="0"/>
</a></div>
</div>
</div>
               </div>
                            <div id="menu_tab_371741373356533" class="menu_tab_3">
							   <div style="width: 300px; height: 140px; background-image: url('/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/jobs_bg.png'); position: absolute; top: 0px; float: left; z-index: 19px;">
<div style=" width:130px; height:111px; float:left; margin:1px 0px 0px 0px; padding:0px;">
 <a href="http://www.motoring.co.za/"><img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/motors_car.jpg" alt="" border="0"/>
</a>
 </div>
 
 <div style=" width: 162px; float:left; margin:11px 0px 0px 0px; padding:0px; height: 101px;">
<p style="margin-top: 0px; margin-left:0px; padding: 0 7px ; clear: inherit;">
Buying a car has never been easy. Motoring.co.za contains a large database of car listings with a user friendly search. <br /> 
<a href="http://www.motoring.co.za/" class="teasers_right_read_more">Start searching today &raquo;</a><br /></p>
</div>

<div>
<div style=" width: 111px; float:left; margin: 0px 15px 0px 5px;"><a href="http://www.wegotads.co.za/bluefin.cmp?cPath=16001&cstr=Motors&sfid=1"><img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/cars_for_sale.jpg" alt="" border="0"/>

</a></div>
<div style="width: 148px; float:left;" ><a href="http://www.motoring.co.za/">
<img src="/polopoly_fs/tabbed-element-for-jobs-property-and-motors-7.174!/motoring_logo.jpg" alt="" border="0"/>
</a></div>
</div>
</div>
               </div>
                        </div>
           <script type="text/javascript">
             ddtabmenu.definemenu("71741373356533",0)
            </script>
      
      
      
  
                	    </div>
	  	  <div style="clear:both"></div>
      </div>
	
        <div id="footer">

	          
                  
    
      
        
        
        <div class='advert-container'>
        	        	        	            
          <!--JavaScript Tag // Tag for network 567: Dash Of Lime // Website: IOL Travel // Page: Bookings // Placement: Bookings-Leaderboard Bottom-728 x 90 (4291912) // created at: Feb 19, 2013 2:22:06 PM-->
<script language="javascript">
<!--
if (window.adgroupid == undefined) {
	window.adgroupid = Math.round(Math.random() * 1000);
}
document.write('<scr'+'ipt language="javascript1.1" src="http://adserver.adtech.de/addyn|3.0|567|4350741|0|225|ADTECH;loc=100;target=_blank;key=key1+key2+key3+key4;grp='+window.adgroupid+';misc='+new Date().getTime()+'"></scri'+'pt>');
//-->
</script><noscript><a href="http://adserver.adtech.de/adlink|3.0|567|4350741|0|225|ADTECH;loc=300;key=key1+key2+key3+key4" target="_blank"><img src="http://adserver.adtech.de/adserv|3.0|567|4350741|0|225|ADTECH;loc=300;key=key1+key2+key3+key4" border="0" width="728" height="90"></a></noscript>
<!-- End of JavaScript Tag -->
	</div> 

          <div style='clear:both;'></div>
		
      
          
        <div class="breadcrum_cont">
  <p class="breadcrum"><strong>You are here:</strong>
        	      <a href="http://www.iol.co.za:80/" class="breadcrum">IOL</a><span class="separator"> / </span> 
	  	      <a href="http://www.iol.co.za:80/isolezwe" class="breadcrum">Isolezwe</a><span class="separator"> / </span> 
	        EzikaMalema zethule abazo eKZN 
    </p>
</div>

          
        
  <div id="iol_services">
    <div id="iol_services_head">
      <p><img src="/images/iol-services-logo.gif" alt="IOL-Services" title=""/><br />
      <b>We like to make your life easier</b></p>
    </div>
    <div id="iol_services_cont">
      <div class="iol_services_cont_pic">
		<a href="http://www.iol.co.za:80/rss" target="_blank"><img src="/images/footer_rss_feeds.gif" alt="IOL - RSS Feeds" title="" class="pics" /></a>
	  </div>
      <div class="iol_services_cont_text">
		<p><strong><a href="http://www.iol.co.za:80/rss" class="highlights_head" target="_blank">RSS feeds</a></strong>
		<br />
		<a href="http://www.iol.co.za:80/rss" class="footer-links">Subscribe</a> to one of our feeds and receive instant news.</p>
	  </div>
      <div class="iol_services_cont_pic">
		<a href="http://m.iol.co.za/"><img src="/images/footer_mobile.gif" alt="IOL - Mobile" title="" class="pics" /></a>
	  </div>
      <div class="iol_services_cont_text2">
		<p><strong><a href="http://m.iol.co.za/" target="_blank" class="highlights_head">Mobile</a></strong>
		<br /> Browse IOL on your phone at <a href="http://m.iol.co.za/" target="_blank" class="footer-links">m.iol.co.za.</a></p>
	  </div>
      <div class="iol_services_cont_pic">
		<a href="http://www.iol.co.za/newsletters"  target='_blank'><img src="/images/footer_newsletters.gif" alt="IOL - Headlights" title="" class="pics" /></a>
	  </div>
      <div class="iol_services_cont_text">
		<p><strong><a href="http://www.iol.co.za/newsletters"  class="highlights_head"  target='_blank'>Newsletters</a></strong>
		<br />Subscribe to our <a href="http://www.iol.co.za/newsletters" class="footer-links"  target='_blank'> newsletters.</a> News delivered to your inbox!</p>
	  </div>
	  <div class="iol_services_cont_pic3"><a href="https://twitter.com/iol" target="_blank"><img src="/images/tweeter_top.gif" alt="IOL - Headlights" title="" class="pics" /></a></div>
      <div class="iol_services_cont_text3"><p><strong><a href="https://twitter.com/iol" target="_blank" class="highlights_head">Twitter</a></strong><br /><a href="https://twitter.com/iol" class="footer-links">Join us now</a></p></div>
	  <div class="iol_services_cont_pic3"><a href="http://www.facebook.com/IOLnews"><img src="/images/facebook_top.gif" target="_blank" alt="IOL - Headlights" title="" class="pics" /></a></div>
      <div class="iol_services_cont_text3"><p><strong><a href="http://www.facebook.com/IOLnews" target="_blank" class="highlights_head">Facebook</a></strong><br /><a href="http://www.facebook.com/IOLnews" class="footer-links">Join us now</a></p></div>

    </div>  
  </div>

          
        
<div>
 
                  
    
      
        		 
 



<div class="footer_sponsored_links">
<div class="footer_sponsored_links_head"><p class="sponsored_link_head_text">Isolezwe</p></div>

<div class="footer_sponsored_links_cont">	<ul class="footer_sponsored_link_cont">
                                             <li><a href="http://www.iol.co.za/isolezwe/sithinte-1.999376" class="menu_tab_lists" rel="nofollow" >Sithinte</a></li>
                                             <li><a href="http://www.iol.co.za/isolezwe/ukukhangisa-1.999401" class="menu_tab_lists" rel="nofollow" >Ukukhangisa</a></li>
                                             <li><a href="http://www.iol.co.za/isolezwe/abafundi-1.999414" class="menu_tab_lists" rel="nofollow" >Abafundi</a></li>
                                             <li><a href="http://www.iol.co.za/isolezwe/terms-conditions-1.999435" class="menu_tab_lists" rel="nofollow" >Terms & Conditions</a></li>
              </ul>
    </div>
</div>

























      
  
      </div>
 
 
 
<div id="foot_note">
  <div class="foot_note_text">
	      	  	        <p class="foot_note"><a href="http://www.iol.co.za/about-iol-1.458" class="foot_note" >About IOL</a></p>
	            	  	        <p class="foot_note"><a href="http://www.inlsubs.co.za/" class="foot_note" >Subscriptions</a></p>
	          </div>
        <div class="foot_note_text">
                	  	        <p class="foot_note"><a href="http://www.iol.co.za/about-iol-1.458" class="foot_note" >Feedback</a></p>
	            	  	        <p class="foot_note"><a href="http://www.iol.co.za/about-iol-1.458" class="foot_note" >Contact Us</a></p>
	          </div>
        <div class="foot_note_text">
                	  	        <p class="foot_note"><a href="http://www.iol.co.za/advertising-1.459" class="foot_note" >Advertising</a></p>
	            	  	        <p class="foot_note"><a href="http://www.iol.co.za/site-map" class="foot_note" >Sitemap</a></p>
	          </div>
        <div class="foot_note_text">
                	  	        <p class="foot_note"><a href="http://www.iol.co.za/terms-conditions-1.462" class="foot_note" >Terms & Conditions</a></p>
	            	  	        <p class="foot_note"><a href="http://www.iol.co.za/our-privacy-policy-1.599" class="foot_note" >Privacy Policy</a></p>
	        </div>

  <div id="online_publishers_etc">
	  	  	  </div>

  <div id="footer_copywrite">
    <p class="foot_note">Isolezwe © 1999 - 2010 Independent Online. All rights strictly reserved. Independent Online is a wholly owned subsidiary of Independent News and Media. Reliance on the information this site contains is at your own risk. Independent Newspapers subscribes to the South African Press Code that prescribes news that is truthful, accurate, fair and balanced. If we don't live up to the Code please contact the Press Ombudsman at 011 484 3612/8. </p>
  </div>


</div>






          
        
        
                        <!-- Kontera ContentLink(TM);-->
<script type='text/javascript'>
var dc_AdLinkColor = 'blue' ;
var dc_PublisherID = 203955 ;
 
</script>
<script type='text/javascript' src='http://kona.kontera.com/javascript/lib/KonaLibInline.js'>
</script>
<!-- Kontera ContentLink(TM) -->



      
      
          
        
        
                        <script type="text/javascript">

var _gaq = _gaq || [];
_gaq.push(
['_setAccount', 'UA-425302-32'],
['_trackPageview'],
['newSite._setAccount', 'UA-17710838-8'],
['newSite._trackPageview']
);

(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();

</script>
      
      
      
  
      	  	
    </div>	

  </div>
 </div>

<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
    var disqus_shortname = 'iol'; // required: replace example with your forum shortname
	var disqus_developer = 1;

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function () {
        var s = document.createElement('script'); s.async = true;
        s.type = 'text/javascript';
        s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';
        (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
    }());
</script>
 

<!-- C|ON|TEXT ad tag -->

<!-- Front:iolfront01.mhs.onsite.hosting.co.za -->
<!-- Timestamp:1396429893915 -->
      </body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.iol.co.za/isolezwe/ezikamalema-zethule-abazo-ekzn-1.1667768#.UzvUR62SxWv'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, 'EzikaMalema zethule abazo eKZN')
        self.assertEqual(doc.summary, None)
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '28 03 2014')
        self.assertEqual(doc.author.name, 'CELANI SIKHAKHANE noSIMPHIWE NGUBANE')
        self.assertEqual(doc.medium.name, 'Isolezwe')

        print repr(doc.text)

        self.assertEqual(doc.text, u'CELANI SIKHAKHANE noSIMPHIWE NGUBANE \n\nI-Economic Freedom Fighters (EFF) KwaZulu-Natal ifolosa ngabesifazane nentsha ohlwini lwayo lwamagama okuqala ayishumi abaholi abazoyimela esiShayamthetho ngemva kokhetho lukazwelonke oluzoba ngoMeyi 7. \n\nLokhu kugqame izolo ngenkathi i-EEF yethula abaholi bayo abasohlwini lokhetho esithangamini nabezindaba eThekwini. \n\nInxusa leqembu nokubhekwe ukuthi libe ngundunankulu wase-KZN uma i-EFF inqoba, nguMnuz Vusi Khoza. UKhoza uke waba yikhansela le-ANC eThekwini nonobhala weNFP esifundazweni. \n\nUKhoza uthe uhla lwabo lumele lonke uhlobo lwabantu abakhona  e-KZN ngokobulili, ukuxuba intsha nabadala. \n\nUNksz Magdalene Moonsamy, obengumholi we-ANC Youth League nojutshwe ubuholi bukazwelonke esifundazweni, uthe iningi labaholi babo abazobamela eSishayamthetho banamakhono adingekayo futhi bayabethemba. \n\n\u201cAbanye baholi bethu banomlando wokusebenzela abantu kusuka kwi-ANC nakwezinye izinhlaka njengoKhoza okunguye osimele njengondunankulu wesifundazwe,\u201d kusho uNksz Moonsamy. \n\nOkufike kwagqama wukuthi ngesikhathi bebiza uKhoza abaholi bale nhlangano bebembiza ngondunankulu, yize kungakayiwa okhethweni. \n\nPhakathi kwamagama asohlwini lokuqala olubizwa nge-Top 10 uKhoza,uNksz Thembi Msane, uMnuz Lwazi Ntombela, uNksz Londiwe Mkhwanazi, uMnuz Nhlanhla Buthelezi, uNksz Sbongile Khawula, uVerusca Fynn, uMnuz Reggie Ngcobo,uNksz Cebisile Shangase, uMnuz Nkosinathi Mthethwa. \n\nUNksz Moonsamy uthe abaholi babo bazimisele ukufunda okuningi njengoba beya eSishayamthetho. \n\nUKhoza uthe okubalulekile kubo wukuthi banqobe zonke izihlalo ezingu-80 eziseSishayamthetho. \n\nNgaphandle kwamagama abaholi abayishumi abasohlwini , kuphinde kwethulwa nabanye abasohlwini lwesifundazwe abayingxenye yabantu abazoya eSishayamthetho. \n\nKulesi sithangami kuphinde kwethulwa uMnuz Vukani Ndlovu ngokusemthethweni obedume ebuholini be-ANC Youth League ngenkathi ehola isigungu sesikhashana sesifundazwe esihlakazwe ngonyaka odlule. \n\nAbaholi baleli qembu bamile ekutheni bafuna ukusebenzisana nanoma yimuphi umbutho ozovumelana nabo ngemigomo ehambisana nokubuyiswa komhlaba ngaphandle kwesinxephezelo ukuthi uhlomulise bonke abantu bakuleli. \n\nUNksz Moonsamy uthe bangasebenzisana neFreedom Front Plus inqobo nje uma izimisele ukuvumelana nabo ngodaba lomhlaba, ivume ukuthi kumele ubesezandleni zabantu, hhayi zedlanzana. \n\nAbaholi baleli qembu abazange bacacise ukuthi banamalungu amangaki eKZN, bakhankasa nini nokuthi yiziphi izindlela abazisebenzisayo ukuxhumana nabantu njengoba bethi sebehlangane nabantu abaningi abampofu, abahola kancane, abasebenza ezindlini, abahlengikazi nabahlala emijondolo. \n\nBathi iKZN sebeyiphendule yabomvu njengoba bexhumana nabantu kuzona zonke izingxenye zesifundazwe. \n\nUKhoza uthe abantu baseKZN basetshenziswa ngamaqembu ezepolitiki njengethuluzi lokuvota ukuze kucebe idlanzana eliphila ntofontofo. \n\nUphinde wathi igama lesifundazwe selingcolile  ezweni isidume njengendawo eyisizinda senkohlakalo  ngenxa yomuzi kaMengameli  Jacob Zuma owakhiwe ngoR246 million . ')
        
