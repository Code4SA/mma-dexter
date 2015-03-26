# -*- coding: utf-8 -*-

import unittest

from dexter.models import Document, db
from dexter.models.seeds import seed_db
from dexter.processing.crawlers import CitizenCrawler

class TestTimesliveCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = CitizenCrawler()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_canonicalise_url(self):
        self.assertEqual(self.crawler.canonicalise_url(
            'https://www.citizen.co.za/153078/outa-claims-proof-e-toll-mismanagement'),
            'http://citizen.co.za/153078/outa-claims-proof-e-toll-mismanagement/')

    def test_offer(self):
        self.assertEqual(self.crawler.offer('http://citizen.co.za/153078/outa-claims-proof-e-toll-mismanagement/'), True)
        # ignore non-citizen
        self.assertEqual(self.crawler.offer('http://www.iol.co.za/news/crime-courts/justice-system-not-equipped-for-cable-theft-1.1760799'), False)

    def test_extract(self):
        html = """

<!DOCTYPE html>
<head>
                <title>
                Outa claims proof of e-toll mismanagement | The Citizen            </title>
            <link href="http://citizen.co.za/wp-content/themes/citizen-v5-1/ticker-style.css" rel="stylesheet" type="text/css" />
    <link rel="stylesheet" type="text/css" href="http://citizen.co.za/wp-content/themes/citizen-v5-1/style.css" />
    <link rel="stylesheet" type="text/css" href="http://citizen.co.za/wp-content/themes/citizen-v5-1/mod_style.css" />
    <link rel="icon" type="image/png" href="http://citizen.co.za/wp-content/themes/citizen-v5-1/favicon.png">
    <meta name="msapplication-TileColor" content="#DE070F">
    <meta name="msapplication-TileImage" content="http://citizen.co.za/wp-content/themes/citizen-v5-1/tileicon.png">
         <meta property="og:image" content="http://citizen.co.za/wp-content/uploads/sites/18/2014/01/et13-300x199.jpg " />
    <meta property="og:title" content="Outa claims proof of e-toll mismanagement"/>
    <meta property="og:url" content="http://citizen.co.za/153078/outa-claims-proof-e-toll-mismanagement/"/>
    <meta property="og:site_name" content="The Citizen"/>
    <meta property="og:type" content="news"/>
        <link rel="apple-touch-icon" href="http://citizen.co.za/wp-content/themes/citizen-v5-1/touchicon.png">
    
    
    
<!-- This site is optimized with the Yoast WordPress SEO plugin v1.5.2.5 - http://yoast.com/wordpress/seo/ -->
<meta name="robots" content="noodp,noydir"/>
<meta name="description" content="The Opposition to Urban Tolling Alliance (Outa) has once again pleaded with government to listen to “critics” against e-tolling, in light of new information provided by a whistle blower on the user payment system."/>
<link rel="canonical" href="http://citizen.co.za/153078/outa-claims-proof-e-toll-mismanagement/" />
<!-- / Yoast WordPress SEO plugin. -->

<link rel='stylesheet' id='slideshow-style-css'  href='http://citizen.co.za/wp-content/plugins/caxton-citizen-flexslider-wp-gallery/flexslider.css?ver=3.8.1' type='text/css' media='all' />
<link rel='stylesheet' id='ubermenu-basic-css'  href='http://citizen.co.za/wp-content/plugins/ubermenu/standard/styles/basic.css?ver=2.3.2.2' type='text/css' media='all' />
<script type='text/javascript' src='http://citizen.co.za/wp-includes/js/jquery/jquery.js?ver=1.10.2'></script>
<script type='text/javascript' src='http://citizen.co.za/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.2.1'></script>
<script type='text/javascript' src='http://citizen.co.za/wp-content/plugins/caxton-citizen-flexslider-wp-gallery/jquery.flexslider.js?ver=3.8.1'></script>
<script type='text/javascript' src='http://citizen.co.za/wp-content/plugins/caxton-citizen-flexslider-wp-gallery/load-slider.js?ver=3.8.1'></script>
<script type='text/javascript' src='http://ox-d.caxton.co.za/w/1.0/jstag'></script>

		<!--[if lt IE 8]>
		<script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE8.js"></script>
		<![endif]-->
		
<!-- UberMenu CSS - Controlled through UberMenu Options Panel 
================================================================ -->
<style type="text/css" id="ubermenu-style-generator-css">
/* Menu Width - UberMenu Advanced Settings */
#megaMenu{ width: 960px; max-width:100%; }

/* Inner Menu Width - used for centering - UberMenu Advanced Settings */
#megaMenu ul.megaMenu{ max-width: 960px; }
/* Image Text Padding */
#megaMenu .ss-nav-menu-with-img > a > .wpmega-link-title, #megaMenu .ss-nav-menu-with-img > a > .wpmega-link-description, #megaMenu .ss-nav-menu-with-img > a > .wpmega-item-description, #megaMenu .ss-nav-menu-with-img > span.um-anchoremulator > .wpmega-link-title, #megaMenu .ss-nav-menu-with-img > span.um-anchoremulator > .wpmega-link-description, #megaMenu .ss-nav-menu-with-img > span.um-anchoremulator > .wpmega-item-description{
  padding-left: 23px;
}	
</style>
<!-- end UberMenu CSS -->
		
			<script type="text/javascript">
 var OX_12345cxt = OX();   
         OX_12345cxt.addAdUnit("537079555");//halfpage - news section
        OX_12345cxt.addAdUnit("459167");//leaderboard - news section
        OX_12345cxt.addAdUnit("459170");//MPU - news section
                OX_12345cxt.addAdUnit("537079558");//136X130 Top left
        OX_12345cxt.addAdUnit("537079559");//136X130 Top right
        OX_12345cxt.addAdUnit("537079560");//136X130 Bottom left
        OX_12345cxt.addAdUnit("537079561");//136X130 Bottom right
        OX_12345cxt.addAdUnit("537084166");//266X185
        OX_12345cxt.fetchAds(); 
 
</script>


</head>
<body>
<div class="wrapperwallpaper"><!--<div class="wrapperwallpaper-no-bg">-->
    <div class="page-content-wrapper">
                   
        <div class="header-wrapper">
            <div class="header-superleaderboard">
                <div class="superleaderboard-container">
                    <div id="leaderboard"> 
                        <script type="text/javascript">
                                                                OX_12345cxt.showAdUnit("459167");//leaderboard/superleaderboard - news section
                                                        </script>               
                    </div>
                </div>
            </div>
            <div class="header">
                <div class="container">
                    <div class="header-logo">
                        <a href="http://citizen.co.za" title="The Citizen">
                            <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/02/copy-citizen-logo22.png" alt="The Citizen" />
                        </a>
                    </div>
                    <div class="header-utilities">
                        <div class="header-dateline">
                            Tuesday 1 April 2014                        </div>
                        <div class="header-tagline">
                            <img src="http://citizen.co.za/wp-content/themes/citizen-v5-1/images/tagline.png" alt="Citizen" />
                        </div>
                        <div class="header-search">
                            <form role="search" method="get" id="searchform" class="searchform" action="http://citizen.co.za/">
				<div>
					<label class="screen-reader-text" for="s">Search for:</label>
					<input type="text" value="" name="s" id="s" />
					<input type="submit" id="searchsubmit" value="Search" />
				</div>
			</form>                        </div> 
                    </div> 
                </div>
            </div>
            <div class="header-navigation">
                <div class="navigation last">
                    <!-- mfunc -->
                    <nav id="megaMenu" class="megaMenuContainer megaMenu-nojs megaResponsive megaResponsiveToggle wpmega-withjs megaMenuOnHover megaFullWidthSubs megaFullWidth megaMenuHorizontal wpmega-noconflict megaMinimizeResiduals megaResetStyles"><div id="megaMenuToggle" class="megaMenuToggle">Menu&nbsp; <span class="megaMenuToggle-icon"></span></div><ul id="megaUber" class="megaMenu"><li id="menu-item-22097" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home ss-nav-menu-item-0 ss-nav-menu-item-depth-0 ss-nav-menu-reg um-flyout-align-center ss-nav-menu-with-img ss-nav-menu-notext"><a href="http://citizen.co.za/"><img class="um-img um-img-resize" height="16" width="16" src="http://citizen.co.za/wp-content/uploads/sites/18/2013/08/home.png" alt="home" title="home" /></a></li><li id="menu-item-3536" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor menu-item-has-children mega-with-sub ss-nav-menu-item-1 ss-nav-menu-item-depth-0 ss-nav-menu-mega ss-nav-menu-mega-alignCenter"><a href="http://citizen.co.za/category/news/"><span class="wpmega-link-title">NEWS</span></a>
<ul class="sub-menu sub-menu-1">
<li id="menu-item-1827" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-1789" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/news/news-national/"><span class="wpmega-link-title">National</span></a></li><li id="menu-item-1788" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/news/news-business/"><span class="wpmega-link-title">Business</span></a></li><li id="menu-item-1787" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/news/news-africa/"><span class="wpmega-link-title">Africa</span></a></li><li id="menu-item-1790" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/news/news-world/"><span class="wpmega-link-title">World</span></a></li><li id="menu-item-4953" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/news/news-eish/"><span class="wpmega-link-title">Eish!</span></a></li><li id="menu-item-136525" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/news/oscar-trial/"><span class="wpmega-link-title">Oscar Trial</span></a></li>	</ul>
</li><li id="menu-item-1828" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-1835" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar">				<div class="menu-widget">
            	<div class="menu-widget-headlines">
    				<div class="menu-widget-body">
						                    	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/153147/arms-inquiry-adjourned-4/" title="Arms Inquiry adjourned">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/08/seriti-130x86.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category news-national-category-color">
                                        National                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/153147/arms-inquiry-adjourned-4/" title="Arms Inquiry adjourned" >
                                        Arms Inquiry adjourned                                    </a>
                                </div>
                        </div>
                                            	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/153140/free-state-woman-found-dead/" title="Free State woman found dead">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/12/crime-scene-130x86.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category news-national-category-color">
                                        National                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/153140/free-state-woman-found-dead/" title="Free State woman found dead" >
                                        Free State woman found dead                                    </a>
                                </div>
                        </div>
                                             </div>
		</ul></div></li>	</ul>
</li><li id="menu-item-1829" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-1836" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-2">        	<div class="menu-weather">
            	<div class="menu-widget-header ">
    				<span class="page-lead-category news-category-color">
                           WEATHER
                	</span>
    			</div>
                <div class="menu-weather-body">
                	                        <div class="widget-item">
                        	<div class="todays-weather-report">
                                    <h3 class="weather-day">
                                        Johannesburg
											                                            &nbsp;tomorrow                                    </h3>
                                    <div class="weather-icon">
										<img src="http://citizen.co.za/wp-content/themes/citizen-v5-1/images/weather/sunny.png" alt=" " />
                                	</div>
                                    <h3 class="weather-temps">
                                        14&nbsp;/&nbsp;25&deg;C
                                    </h3>
                                    <div class="weather-description">
                                    	Sunny                                    </div>
                                    <div class="weather-sunriseset">
                                    	<strong>Sunrise:&nbsp;</strong>
                                        	06:16                                    </div>
                                    <div class="weather-sunriseset">
                                         <strong>Sunset:&nbsp;</strong>
                                        	18:03									</div>
                            </div>
        				</div>
                                        </div>
            </div>
        </ul></div></li>	</ul>
</li><li id="menu-item-1830" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-1840" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-3">		
	            
			<div class="menu-widget">
            	<div class="menu-widget-headlines">
					<div class="menu-widget-header ">
    					<span class="page-lead-category news-category-color">
                            MORE HEADLINES
                		</span>
    				</div>
    				<div class="menu-widget-body">
						                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/153133/sars-surpasses-tax-collection-target/" title="Sars surpasses tax collection target" >
                            		Sars surpasses tax collection target                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/153134/petrol-price-midnight-tonight/" title="Petrol price up at midnight tonight" >
                            		Petrol price up at midnight tonight                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/153126/charges-itumeleng-khune-dropped/" title="Charges against Itumeleng Khune dropped" >
                            		Charges against Itumeleng Khune dropped                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/153078/outa-claims-proof-e-toll-mismanagement/" title="Outa claims proof of e-toll mismanagement" >
                            		Outa claims proof of e-toll mismanagement                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/153124/sadtu-welcomes-soobrayans-move/" title="Sadtu welcomes Soobrayan&#8217;s move" >
                            		Sadtu welcomes Soobrayan&#8217;s move                                </a>
                            </div>
    					    				</div>
    				<div class="menu-widget-footer">
    				</div>
				</div>
             </div>
	</ul></div></li>	</ul>
</li></ul>
</li><li id="menu-item-1791" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children mega-with-sub ss-nav-menu-item-2 ss-nav-menu-item-depth-0 ss-nav-menu-mega ss-nav-menu-mega-alignCenter"><a href="http://citizen.co.za/category/opinion/"><span class="wpmega-link-title">OPINION</span></a>
<ul class="sub-menu sub-menu-1">
<li id="menu-item-1831" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-1793" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/opinion/opinion-columns/"><span class="wpmega-link-title">Columns</span></a></li><li id="menu-item-1794" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/opinion/opinion-editorials/"><span class="wpmega-link-title">Editorials</span></a></li>	</ul>
</li><li id="menu-item-1832" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2264" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-4">				<div class="menu-widget">
            	<div class="menu-widget-headlines">
    				<div class="menu-widget-body">
						                    	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/152790/law-keeps-poor-work/" title="Law keeps the poor out of work">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/08/andrewcol-e1376379423945-130x63.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category opinion-columns-category-color">
                                        Columns                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/152790/law-keeps-poor-work/" title="Law keeps the poor out of work" >
                                        Law keeps the poor out of work                                    </a>
                                </div>
                        </div>
                                            	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-portrait">
                                            <a href="http://citizen.co.za/152786/good-story-pupils/" title="No good story for pupils">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/07/block_opinion-130x130.png" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category opinion-editorials-category-color">
                                        Editorials                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/152786/good-story-pupils/" title="No good story for pupils" >
                                        No good story for pupils                                    </a>
                                </div>
                        </div>
                                             </div>
		</ul></div></li>	</ul>
</li><li id="menu-item-1833" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2265" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-5">        	<div class="menu-weather">
            	<div class="menu-widget-header ">
    				<span class="page-lead-category opinion-category-color">
                          EDITORIAL
                	</span>
    			</div>
                <div class="menu-weather-body">
                	                        
                        <div class="menu-more-headline">
                        	<a href="http://citizen.co.za/152786/good-story-pupils/" title="No good story for pupils" >
                            	No good story for pupils                        	</a>
                        </div>
                        <div class="menu-widget-excerpt">
                        	Despite all assurances from education officials that learning material would be delivered to all schools on time, another textbook scandal has surfaced in Limpopo.                        </div>
    				 
                </div>
            </div>
        </ul></div></li>	</ul>
</li><li id="menu-item-1834" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2266" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-6">		
	            
			<div class="menu-widget">
            	<div class="menu-widget-headlines">
					<div class="menu-widget-header ">
    					<span class="page-lead-category opinion-category-color">
                            COLUMNISTS
                		</span>
    				</div>
    				<div class="menu-widget-body">
						                        	<div class="view-count">
                            	Andrew Kenny                        	</div>
                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152790/law-keeps-poor-work/" title="Law keeps the poor out of work" >
                            		Law keeps the poor out of work                                </a>
                            </div>
    					                        	<div class="view-count">
                            	Kay Sexwale                        	</div>
                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152788/guide-gold-digers/" title="A guide for gold diggers" >
                            		A guide for gold diggers                                </a>
                            </div>
    					                        	<div class="view-count">
                            	Hendri Pelser                        	</div>
                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152336/bread-butter-politics/" title="Bread and butter politics" >
                            		Bread and butter politics                                </a>
                            </div>
    					    				</div>
    				<div class="menu-widget-footer">
    				</div>
				</div>
             </div>
	</ul></div></li>	</ul>
</li></ul>
</li><li id="menu-item-3675" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children mega-with-sub ss-nav-menu-item-3 ss-nav-menu-item-depth-0 ss-nav-menu-mega ss-nav-menu-mega-alignCenter"><a href="http://citizen.co.za/category/sport/"><span class="wpmega-link-title">SPORT</span></a>
<ul class="sub-menu sub-menu-1">
<li id="menu-item-1841" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-1800" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/sport/sport-soccer/"><span class="wpmega-link-title">Soccer</span></a></li><li id="menu-item-1798" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/sport/sport-cricket/"><span class="wpmega-link-title">Cricket</span></a></li><li id="menu-item-4947" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/sport/sport-rugby/"><span class="wpmega-link-title">Rugby</span></a></li><li id="menu-item-4952" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/motoring/motoring-motorsport/"><span class="wpmega-link-title">Motorsport</span></a></li><li id="menu-item-1799" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/sport/sport-other-sport/"><span class="wpmega-link-title">Other sport</span></a></li><li id="menu-item-1797" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/sport/sport-columnists/"><span class="wpmega-link-title">Columnists</span></a></li>	</ul>
</li><li id="menu-item-1842" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2261" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-7">				<div class="menu-widget">
            	<div class="menu-widget-headlines">
    				<div class="menu-widget-body">
						                    	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/153104/153104/" title="Du Preez signs with WP">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/04/TL_1116733-130x94.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category sport-rugby-category-color">
                                        Rugby                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/153104/153104/" title="Du Preez signs with WP" >
                                        Du Preez signs with WP                                    </a>
                                </div>
                        </div>
                                            	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/153067/csa-commends-western-province-2/" title="CSA commends Western Province">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/04/TL_1115689-130x94.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category sport-cricket-category-color">
                                        Cricket                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/153067/csa-commends-western-province-2/" title="CSA commends Western Province" >
                                        CSA commends Western Province                                    </a>
                                </div>
                        </div>
                                             </div>
		</ul></div></li>	</ul>
</li><li id="menu-item-1844" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2262" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-8">        	<div class="menu-weather">
            	<div class="menu-widget-header ">
    				<span class="page-lead-category sport-category-color">
                          COLUMNISTS
                	</span>
    			</div>
                <div class="menu-weather-body">
                	                        	
                        <div class="view-count">
                            	Jon Swift                        </div>
                        
                        <div class="menu-more-headline">
                        	<a href="http://citizen.co.za/152711/ab-victor-whats-fuss/" title="AB and Victor: so what’s the fuss?" >
                            	AB and Victor: so what’s the fuss?                        	</a>
                        </div>
                        <div class="menu-widget-excerpt">
                        	It has taken Dave the Silent a reasonably full working lifetime to develop the delicate balance between a healthy cynicism about his fellow man and the carapace of accepting that while his inherent doubts about those around him are probably justified, the sun will doubtless come up tomorrow.                        </div>
    				 
                </div>
            </div>
        </ul></div></li>	</ul>
</li><li id="menu-item-1843" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2263" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-9">		
	            
			<div class="menu-widget">
            	<div class="menu-widget-headlines">
					<div class="menu-widget-header ">
    					<span class="page-lead-category sport-category-color">
                            MORE HEADLINES
                		</span>
    				</div>
    				<div class="menu-widget-body">
						                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152770/parnell-adds-cause-extra/" title="Parnell adds to the cause extra" >
                            		Parnell adds to the cause extra                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152761/dauda-hopes-prove-world-cup-worth/" title="Dauda hopes to prove World Cup worth" >
                            		Dauda hopes to prove World Cup worth                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152738/bulls-vow-bounce-back-canes-clash/" title="Bulls vow to bounce back in Canes clash" >
                            		Bulls vow to bounce back in Canes clash                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152711/ab-victor-whats-fuss/" title="AB and Victor: so what’s the fuss?" >
                            		AB and Victor: so what’s the fuss?                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152713/big-easy-miss-trick/" title="Big Easy does not miss a trick" >
                            		Big Easy does not miss a trick                                </a>
                            </div>
    					    				</div>
    				<div class="menu-widget-footer">
    				</div>
				</div>
             </div>
	</ul></div></li>	</ul>
</li></ul>
</li><li id="menu-item-1775" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children mega-with-sub ss-nav-menu-item-4 ss-nav-menu-item-depth-0 ss-nav-menu-mega ss-nav-menu-mega-alignCenter"><a href="http://citizen.co.za/category/horses/"><span class="wpmega-link-title">HORSES</span></a>
<ul class="sub-menu sub-menu-1">
<li id="menu-item-1853" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-1779" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/horses/horses-news/"><span class="wpmega-link-title">Racing News</span></a></li><li id="menu-item-1776" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/horses/horses-columnists/"><span class="wpmega-link-title">Columnists</span></a></li>	</ul>
</li><li id="menu-item-1854" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2267" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-10">				<div class="menu-widget">
            	<div class="menu-widget-headlines">
    				<div class="menu-widget-body">
						                    	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/152978/triple-crown-continues-conquer/" title="Triple Crown continues to conquer">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/04/DSC_1173-130x84.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category horses-news-category-color">
                                        Racing News                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/152978/triple-crown-continues-conquer/" title="Triple Crown continues to conquer" >
                                        Triple Crown continues to conquer                                    </a>
                                </div>
                        </div>
                                            	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/151562/horseys/" title="SA horses can clinch world’s richest race">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/dubai_538656348.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category horses-news-category-color">
                                        Racing News                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/151562/horseys/" title="SA horses can clinch world’s richest race" >
                                        SA horses can clinch world’s richest race                                    </a>
                                </div>
                        </div>
                                             </div>
		</ul></div></li>	</ul>
</li><li id="menu-item-1855" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2268" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-11">        	<div class="menu-weather">
            	<div class="menu-widget-header ">
    				<span class="page-lead-category horses-category-color">
                          COLUMNISTS
                	</span>
    			</div>
                <div class="menu-weather-body">
                	                        	
                        <div class="view-count">
                            	Piere Strydom                        </div>
                        
                        <div class="menu-more-headline">
                        	<a href="http://citizen.co.za/128357/column-outlet/" title="Column is the only outlet" >
                            	Column is the only outlet                        	</a>
                        </div>
                        <div class="menu-widget-excerpt">
                        	Sometimes I can get so frustrated by punters who always ask for information and often feel aggrieved when they’ve had a bet and it hasn’t gone their way.                        </div>
    				 
                </div>
            </div>
        </ul></div></li>	</ul>
</li><li id="menu-item-1856" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2269" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-12">		
	            
			<div class="menu-widget">
            	<div class="menu-widget-headlines">
					<div class="menu-widget-header ">
    					<span class="page-lead-category horses-category-color">
                            MORE HEADLINES
                		</span>
    				</div>
    				<div class="menu-widget-body">
						                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/151347/disappointments-still-haunt-laird/" title="Disappointments still haunt Laird" >
                            		Disappointments still haunt Laird                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/141842/horse-containment-zone-established/" title="Horse containment zone established" >
                            		Horse containment zone established                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/135763/wcape-horse-movement-restricted/" title="WCape horse movement restricted" >
                            		WCape horse movement restricted                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/135411/a-lot-at-stake-for-guineas-runners/" title="A lot at stake for Guineas runners" >
                            		A lot at stake for Guineas runners                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/130907/triple-crown-fever-hits-city/" title="Triple Crown fever hits the city!" >
                            		Triple Crown fever hits the city!                                </a>
                            </div>
    					    				</div>
    				<div class="menu-widget-footer">
    				</div>
				</div>
             </div>
	</ul></div></li>	</ul>
</li></ul>
</li><li id="menu-item-1806" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children mega-with-sub ss-nav-menu-item-5 ss-nav-menu-item-depth-0 ss-nav-menu-mega ss-nav-menu-mega-alignCenter"><a href="http://citizen.co.za/category/your-life/"><span class="wpmega-link-title">YOUR LIFE</span></a>
<ul class="sub-menu sub-menu-1">
<li id="menu-item-1845" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-1807" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/your-life/your-life-entertainment/"><span class="wpmega-link-title">Entertainment</span></a></li><li id="menu-item-1809" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/your-life/your-life-home-life/"><span class="wpmega-link-title">Home LIfe</span></a></li><li id="menu-item-1813" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/your-life/your-life-technology/"><span class="wpmega-link-title">Digital Life</span></a></li><li id="menu-item-1814" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/your-life/your-life-things-to-do/"><span class="wpmega-link-title">Things to do</span></a></li>	</ul>
</li><li id="menu-item-1846" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2273" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-13">				<div class="menu-widget">
            	<div class="menu-widget-headlines">
    				<div class="menu-widget-body">
						                    	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/152722/miss-sa-journey-continues/" title="Miss SA: the journey continues">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/City_1A-5-130x86.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category your-life-entertainment-category-color">
                                        Entertainment                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/152722/miss-sa-journey-continues/" title="Miss SA: the journey continues" >
                                        Miss SA: the journey continues                                    </a>
                                </div>
                        </div>
                                            	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/152675/queen-show-presents-ballet-twist/" title="Queen show presents ballet with a twist">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/City4_1-130x86.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category entertainment-theatre-category-color">
                                        Theatre                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/152675/queen-show-presents-ballet-twist/" title="Queen show presents ballet with a twist" >
                                        Queen show presents ballet with a twist                                    </a>
                                </div>
                        </div>
                                             </div>
		</ul></div></li>	</ul>
</li><li id="menu-item-1847" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2274" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-14">        	                
        	<div class="menu-weather">
            	<div class="menu-widget-header ">
    				<span class="page-lead-category your-life-category-color">
                         THINGS TO DO
                	</span>
    			</div>
                <div class="menu-weather-body">
                        	
                            	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/152532/cape-town-jazz-festival-magical-mesmerising/" title="Cape Town Jazz festival ‘magical and mesmerising’">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/09/cape-town-130x97.jpg" alt="" />
                                            </a>
                                        </div>
                                                        
                        <div class="menu-more-headline">
                        	<a href="http://citizen.co.za/152532/cape-town-jazz-festival-magical-mesmerising/" title="Cape Town Jazz festival ‘magical and mesmerising’" >
                            	Cape Town Jazz festival ‘magical and mesmerising’                        	</a>
                        </div>
    				
                </div>
            </div>
			 
        </ul></div></li>	</ul>
</li><li id="menu-item-1848" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2275" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-15">		
	            
			<div class="menu-widget">
            	<div class="menu-widget-headlines">
					<div class="menu-widget-header ">
    					<span class="page-lead-category your-life-category-color">
                            MORE HEADLINES
                		</span>
    				</div>
    				<div class="menu-widget-body">
						                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152689/152689/" title="A lifetime in the music industry and still learning" >
                            		A lifetime in the music industry and still learning                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152550/gareth-cliff-leaves-5fm/" title="Gareth Cliff leaves 5FM" >
                            		Gareth Cliff leaves 5FM                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152532/cape-town-jazz-festival-magical-mesmerising/" title="Cape Town Jazz festival ‘magical and mesmerising’" >
                            		Cape Town Jazz festival ‘magical and mesmerising’                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152480/sweet-sensations/" title="Sweet sensations" >
                            		Sweet sensations                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/152470/discover-new-appreciation-ants/" title="Discover a new appreciation for ants" >
                            		Discover a new appreciation for ants                                </a>
                            </div>
    					    				</div>
    				<div class="menu-widget-footer">
    				</div>
				</div>
             </div>
	</ul></div></li>	</ul>
</li></ul>
</li><li id="menu-item-1781" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children mega-with-sub ss-nav-menu-item-6 ss-nav-menu-item-depth-0 ss-nav-menu-mega ss-nav-menu-mega-alignCenter"><a href="http://citizen.co.za/category/motoring/"><span class="wpmega-link-title">MOTORING</span></a>
<ul class="sub-menu sub-menu-1">
<li id="menu-item-1849" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-4951" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/motoring/motoring-news/"><span class="wpmega-link-title">News</span></a></li><li id="menu-item-1782" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/motoring/motoring-car-tests-and-new-models/"><span class="wpmega-link-title">Car Tests &#038; New Models</span></a></li><li id="menu-item-1783" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/category/motoring/motoring-motorsport/"><span class="wpmega-link-title">Motorsport</span></a></li><li id="menu-item-137168" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2"><a href="http://citizen.co.za/146069/new-car-price-guide-2/"><span class="wpmega-link-title">New Car Price Guide</span></a></li>	</ul>
</li><li id="menu-item-1850" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2270" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-16">				<div class="menu-widget">
            	<div class="menu-widget-headlines">
    				<div class="menu-widget-body">
						                    	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/152367/152367/" title="Varied winners in Western Cape production car races">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/race-130x70.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category motoring-motorsport-category-color">
                                        Motorsport                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/152367/152367/" title="Varied winners in Western Cape production car races" >
                                        Varied winners in Western Cape production car races                                    </a>
                                </div>
                        </div>
                                            	
                        <div class="menu-widget-main-item">
                        	                                        
                                        <div class="menu-widget-thumbnail thumbnail-landscape">
                                            <a href="http://citizen.co.za/151655/new-bmw-offeringsare-set-to-thrill/" title="New BMW offerings are set to thrill">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/OHP_9860-130x86.jpg" alt="" />
                                            </a>
                                        </div>
                                                                <div class="menu-widget-category">
                                    <span class="page-lead-category motoring-car-tests-and-new-models-category-color">
                                        Car Tests &amp; New Models                                    </span>
                            	</div>
                                <div class="menu-widget-headline">
                                    <a href="http://citizen.co.za/151655/new-bmw-offeringsare-set-to-thrill/" title="New BMW offerings are set to thrill" >
                                        New BMW offerings are set to thrill                                    </a>
                                </div>
                        </div>
                                             </div>
		</ul></div></li>	</ul>
</li><li id="menu-item-1851" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2271" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-17">        	<div class="menu-weather">
            	<div class="menu-widget-header ">
    				<span class="page-lead-category motoring-category-color">
                          TESTS & NEW MODELS
                	</span>
    			</div>
                <div class="menu-weather-body">
                	
                        <div class="menu-more-headline">
                        	<a href="http://citizen.co.za/151655/new-bmw-offeringsare-set-to-thrill/" title="New BMW offerings are set to thrill" >
                            	New BMW offerings are set to thrill                        	</a>
                        </div>
                        <div class="menu-widget-excerpt">
                        	The BMW model family celebrates the premiere of another new model series, the 2 Series Coupe. This car raises the bar in the premium compact segment in terms of dynamic ability, aesthetic appeal and emotional allure.                        </div>
    				 
                </div>
            </div>
        </ul></div></li>	</ul>
</li><li id="menu-item-1852" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children ss-nav-menu-item-depth-1 ss-nav-menu-notext ss-nav-menu-nolink">
	<ul class="sub-menu sub-menu-2">
<li id="menu-item-2272" class="menu-item menu-item-type-custom menu-item-object-custom ss-nav-menu-item-depth-2 ss-nav-menu-notext ss-nav-menu-nolink ss-sidebar"><div class="wpmega-nonlink wpmega-widgetarea ss-colgroup-1 uberClearfix"><ul class="um-sidebar" id="wpmega-wpmega-sidebar-18">		
	            
			<div class="menu-widget">
            	<div class="menu-widget-headlines">
					<div class="menu-widget-header ">
    					<span class="page-lead-category motoring-category-color">
                            MORE HEADLINES
                		</span>
    				</div>
    				<div class="menu-widget-body">
						                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/149454/floydw-2/" title="Confusing situation after just one F1 race" >
                            		Confusing situation after just one F1 race                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/149450/super-series-visits-w-cape/" title="Super Series visits Western Cape" >
                            		Super Series visits Western Cape                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/149447/new-terrain-to-test-off-road-racing-crews-to-the-full/" title="New terrain to test off-road racing crews to the full" >
                            		New terrain to test off-road racing crews to the full                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/149443/suzuki-veteran-of-the-nurburgring/" title="Suzuki veteran of the Nurburgring" >
                            		Suzuki veteran of the Nurburgring                                </a>
                            </div>
    					                        	<div class="menu-more-headline">
                            	<a href="http://citizen.co.za/149418/michelin-latitude-sport-3s-rock/" title="Michelin Latitude Sport 3s rock" >
                            		Michelin Latitude Sport 3s rock                                </a>
                            </div>
    					    				</div>
    				<div class="menu-widget-footer">
    				</div>
				</div>
             </div>
	</ul></div></li>	</ul>
</li></ul>
</li><li id="menu-item-1773" class="menu-item menu-item-type-taxonomy menu-item-object-category ss-nav-menu-item-7 ss-nav-menu-item-depth-0 ss-nav-menu-mega ss-nav-menu-mega-alignCenter"><a href="http://citizen.co.za/category/auctions/"><span class="wpmega-link-title">Auctions</span></a></li></ul></nav>                    <!-- /mfunc -->
                </div>
            </div>
        </div> 

<div id="page-content" class="container">
    <div class="row">
        		     
            <div class="eightcol">
                <div class="twelvecol">
                    <div class="article-header">
                                        
                        <div>
                            <span class="page-lead-category news-national-category-color">
                                <a href="http://citizen.co.za/category/news/news-national/" title="National">
                                    National                                </a>
                            </span>
                            <span class="page-lead-datetime">
                                1.4.2014 01.50 pm                            </span>
                        </div>
                    
                        <h1 class="article-headline">
                            <a href="http://citizen.co.za/153078/outa-claims-proof-e-toll-mismanagement/" title="Link to Outa claims proof of e-toll mismanagement" >
                                Outa claims proof of e-toll mismanagement                            </a>
                        </h1>
                                                            <div class="article-byline">
                                        Yadhana Jadoo & Alex Mitchley                                     </div>
                                                                    
                                        <div class="lead-story-single">
                                            <div class="article-main-image">
                                                <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/01/et13-602x400.jpg" alt="" />  
                                            </div>
                                            <div class="afp-article-caption">
                                                FILE PICTURE: E-toll objectors gather, 25 January 2014, at the Portuguese Hall in Joburg South, before taking part in a mass protest drive along the tolled highways. Picture: Michel Bega                                            </div>
                                        </div>
                                                    
                        <div class="article-excerpt">
                            The Opposition to Urban Tolling Alliance (Outa) has once again pleaded with government to listen to “critics” against e-tolling, in light of new information provided by a whistle blower on the user payment system.
                        </div>
                    </div> 
                </div>                   
                <div class="clear"></div>
                <div>    
                    <div class="leftcol no-mobile">
                        <div class="sidebar-wrapper">
    
	    
 
                        
 <div class="article-widget no-mobile">
 <!-- TABS -->
	<div class="article-tabbed-widget">
		<ul class="article-tabbed-widget-list">
			<li>
        		Share & Rate this article
			</li>
		</ul>
    	<div class="article-widget-panel">
    		<div class="article-widget-panel-content"> 
            	<div class="article-widget-body">
                	<!-- AddThis Button BEGIN -->
                    	
						<div class="addthis_toolbox"
                            addthis:title="Outa claims proof of e-toll mismanagement | The Citizen"
                            addthis:description="The Opposition to Urban Tolling Alliance (Outa) has once again pleaded with government to listen to “critics” against e-tolling, in light of new information provided by a whistle blower on the user payment system.
" >
                            <div class="custom_images">
                        	<div class="facebook-share">
							<a class="addthis_button_facebook_like" fb:like:layout="button_count"></a>
                            </div>
                            <div class="twitter-share">
								<a class="addthis_button_tweet"></a>
                            </div>
                            <div class="google-share">
								<a class="addthis_button_google_plusone" g:plusone:size="medium"></a>
                            </div>
                            <div class="email-share">
                            	<a class="addthis_button_email"><img src="http://citizen.co.za/wp-content/themes/citizen-v5-1/images/mail.png" width="20" height="20" border="0" alt="Share on email" /> Email</a>
                            </div>
                            </div>
						</div>
						<script type="text/javascript">var addthis_config = {"data_track_addressbar":false};</script>
						<script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=clickatcaxton" async></script>
					<!-- AddThis Button END -->
                    </div>
                </div>
			</div>
		</div>
	</div>
	<!-- end of widget-->
<div class="clear"></div>

	    
 
                                                
                            <div class="article-widget">
                            <!-- TABS -->
                                <div class="article-tabbed-widget">
                                    <ul class="article-tabbed-widget-list">
                                       <li>Multimedia</li>
                                    </ul>
                                    <div class="article-widget-panel">
                                        <div class="article-widget-panel-content"> 
                                            <div class="article-widget-body">
                                                                                                    <div class="multimedia-widget-item">
                                                       <div class="page-home-multimedia-thumbnail-3bar  multimedia-img-holder">
                                                                <a href="http://citizen.co.za?page_id=89343&cxtpname=nkandla-style-video-goes-viral" title="‘Nkandla Style’ video goes viral">
                                        
                                                                        <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/Nkandla-style-150x150.jpg" alt="" />
                                                                        <span class="multimedia-home-play"></span>
                                            
                                                                </a>
                                                        </div>

                                                        
                                                        <span class="article-widget-related-link">
                                                            <a href="http://citizen.co.za?page_id=89343&cxtpname=nkandla-style-video-goes-viral" title="‘Nkandla Style’ video goes viral">
                                                                ‘Nkandla Style’ video goes viral                                   
                                                            </a>
                                                        </span>
                                                        
                                                    </div>
                                                                                               
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- end of widget-->

                            <div class="clear"></div>
                            
 
                        
 
                                            <div class="article-widget">
                            <!-- TABS -->
                                <div class="article-tabbed-widget">
                                    <ul class="article-tabbed-widget-list">
                                        <li>Related Stories</li>
                                    </ul>
                                    <div class="article-widget-panel">
                                        <div class="article-widget-panel-content"> 
                                            <div class="article-widget-body">
                                                
                                                                                             <div class="widget-item">
                                                   <span class="article-widget-related-link">
                                                      <a href="http://citizen.co.za/150033/hands-public-protector-campaign-launches/" rel="bookmark" title="Link to &#8220;Hands Off our Public Protector&#8221; campaign launches">
                                                          &#8220;Hands Off our Public Protector&#8221; campaign launches                                 
                                                      </a>
                                                   </span>
                                                   <span class="page-lead-datetime">
                                                       26.3.2014                                                    </span>
                                                 </div>
                                                                                            <div class="widget-item">
                                                   <span class="article-widget-related-link">
                                                      <a href="http://citizen.co.za/146523/sanral-collected-r250m-e-tolls/" rel="bookmark" title="Link to Sanral collected R250m from e-tolls">
                                                          Sanral collected R250m from e-tolls                                 
                                                      </a>
                                                   </span>
                                                   <span class="page-lead-datetime">
                                                       19.3.2014                                                    </span>
                                                 </div>
                                                                                            <div class="widget-item">
                                                   <span class="article-widget-related-link">
                                                      <a href="http://citizen.co.za/145173/e-toll-court-action-yet-outa/" rel="bookmark" title="Link to No e-toll court action for non-payment &#8211; Outa">
                                                          No e-toll court action for non-payment &#8211; Outa                                 
                                                      </a>
                                                   </span>
                                                   <span class="page-lead-datetime">
                                                       17.3.2014                                                    </span>
                                                 </div>
                                                                                            <div class="widget-item">
                                                   <span class="article-widget-related-link">
                                                      <a href="http://citizen.co.za/138753/da-continues-to-fight-unjust-e-tolling-system/" rel="bookmark" title="Link to DA continues to fight &#8216;unjust&#8217; e-tolling system">
                                                          DA continues to fight &#8216;unjust&#8217; e-tolling system                                 
                                                      </a>
                                                   </span>
                                                   <span class="page-lead-datetime">
                                                       6.3.2014                                                    </span>
                                                 </div>
                                                                                            <div class="widget-item">
                                                   <span class="article-widget-related-link">
                                                      <a href="http://citizen.co.za/138523/amendment-act-vital-sanral/" rel="bookmark" title="Link to Amendment act not vital &#8211; Sanral">
                                                          Amendment act not vital &#8211; Sanral                                 
                                                      </a>
                                                   </span>
                                                   <span class="page-lead-datetime">
                                                       5.3.2014                                                    </span>
                                                 </div>
                                                                                           
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- end of widget-->

                            <div class="clear"></div>
                        	
					

	    
    <div class="clear"></div>
    
</div>                    </div>
                </div>
                <div class="middlecol article-content">
                        <p><span style="line-height: 1.5em">This, as Outa awaits feedback from the Public Protector’s office on a complaint it laid, following “damning” information it received from a source within the system.</span></p>
<p>The City Press reported on Sunday that an employee of Austrian Company Kapsch &#8211; used to design the e-toll system &#8211; had warned the SA National Roads Agency Ltd (Sanral) of the high risk in the implementation of a national roll-out.</p>
<p>He said the e-tolling system was designed to monitor 7 000 km of national roads, with tolls being planned for Durban and Cape Town, it reported.</p>
<p>The source further stated that there were design flaws within the system and Sanral’s control centre in Midrand had been created to monitor all roads in South Africa.</p>
<p>If the claims are true, it suggests that Sanral saw the Gauteng highway tolling project as either a starting point for national e-tolling, or it significantly over-invested in a system it did not need.</p>
<p>Sanral spokesman Vusi Mona, in rejecting the allegations by the &#8220;so-called informant&#8221;, said the Public Protector Thuli Madonsela had not yet contacted the entity.</p>
<p>It would however &#8220;co-operate&#8221;, should her office conduct an investigation, he added.</p>
<p>Mona said Sanral and its concessionaires were in the process of installing the &#8220;electronic toll collection equipment&#8221; needed at conventional toll plazas across the country.</p>
<p>It would make the exact details as to which toll plazas and  when this payment method will be available, at an &#8220;opportune time&#8221;.</p>
<p>&#8220;Electronic toll collection &#8211; the use of e-tags &#8211; is a method of payment for one’s toll fees. Electronic toll collection does not replace existing toll plazas. It is a tool that toll plazas will use in addition to current methods of payment.</p>
<p>&#8220;By obtaining and e-tag and registering it, e-tolling allows an account holder to use the same e-tag and e-toll account to pay toll fees at any toll plaza equipped to accept e-tags.&#8221;</p>
<p>Deputy Public Protector Kevin Malunga, who was handling the complaint, according to Outa, was not immediately available for comment.</p>
<p>Outa chairman Wayne Duvenage told <em>The Citizen</em> that the alliance had always provided an open door for Parliament’s Portfolio Committee on Transport and Government’s Inter-Ministerial Committee (IMC), which previously engaged with stakeholders against e-tolling, prior to its implementation.</p>
<p>It was important for government to learn from its critics, said Duvenage.</p>
<p>“… And they are not learning from their critics. We are happy to present to anybody.”</p>
<p>He described previous IMC engagements as being unfruitful with government unwilling to unpack and explore the rationality of arguments.</p>
<p>The insider has described “them as arrogant and dangerous people who steam-roll public opinion … bully politicians, and business people and do not act in the interests of the country”, according to Outa.</p>
<p>Duvenage hailed the disclosures as a breakthrough which he hoped would start laying the table for “meaningful multi-lateral engagement with all stakeholders to transcend the mess”.</p>
<p>“The whistle blower shows the sheer arrogance of the system.”</p>
<p>He further asked motorists not the “fall” for a system which was not working.</p>
<p>“The compliance levels are far too low. Don’t be hoodwinked by the propaganda. Now the chickens are coming out to roost.”</p>
<p>Justice Project South Africa (JPSA) chairperson Howard Dembovsky said it was only a matter of time until someone with a “paining conscious” came forward.</p>
<p>“This is a very good thing, we need more people to tell the truth behind what has happened and what is happening with the e-tolls,” said Dembovsky.</p>
<p>The JPSA is convinced that there is corruption behind the controversial system: “It will come out in the dirty washing, a system rolled out veiled in shrouds of secrecy is a dead giveaway.”</p>
<p>Dembovsky echoed Duvenage’s comments, indicating that further IMC engagements would be “a waste of time”.</p>
<p>“The last round of engagements was just Sanral telling people what was going to happen. Do not waste more time and our money,” he said.</p>
<p>“Take the money and lets have a referendum, this is after all a democracy and we have not held a single referendum on the matter,” said Dembovsky.</p>
<p>“Let’s do it, let’s show what democracy is all about,” he added.</p>
<p>&nbsp;</p>
                    <div class="clear"></div>
                                        <a href ="#commects-section">Comment here >></a>
                                        <div class="article-inthis-section">
                        	<div class="list-header news-world-category-header">
        <div class="list-category">
            <div class="list-tag-cat news-world-category-color">           
                You might also like
            </div>
        </div>
    </div>
                <div class="page-lead-list-item">
                <div class="page-lead-list-item-3bar-article">
                            <div class="page-lead-list-item-3bar-single-article">
                                
                                                                        
                            <div class="page-lead-list-thumbnail-3bar thumbnail-portrait">
                                <a href="http://citizen.co.za/153147/arms-inquiry-adjourned-4/" title="Arms Inquiry adjourned">
                                    <img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/08/seriti-150x150.jpg" alt="" />
                                </a>
                            </div>
                                                            
                        <span class="page-lead-list-headline-3bar">
                            <a href="http://citizen.co.za/153147/arms-inquiry-adjourned-4/" title="Arms Inquiry adjourned">
                                Arms Inquiry adjourned                            </a>
                        </span>
                    </div>
                                
                        <div class="page-lead-list-item-separator"></div>                    <div class="page-lead-list-item-3bar-single-article">
                                
                                                                        
                            <div class="page-lead-list-thumbnail-3bar thumbnail-portrait">
                                <a href="http://citizen.co.za/153140/free-state-woman-found-dead/" title="Free State woman found dead">
                                    <img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/12/crime-scene-150x150.jpg" alt="" />
                                </a>
                            </div>
                                                            
                        <span class="page-lead-list-headline-3bar">
                            <a href="http://citizen.co.za/153140/free-state-woman-found-dead/" title="Free State woman found dead">
                                Free State woman found dead                            </a>
                        </span>
                    </div>
                                
                        <div class="page-lead-list-item-separator"></div>                    <div class="page-lead-list-item-3bar-single-article">
                                
                                                                        
                            <div class="page-lead-list-thumbnail-3bar thumbnail-portrait">
                                <a href="http://citizen.co.za/153133/sars-surpasses-tax-collection-target/" title="Sars surpasses tax collection target">
                                    <img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/11/tax-sars-150x150.jpg" alt="" />
                                </a>
                            </div>
                                                            
                        <span class="page-lead-list-headline-3bar">
                            <a href="http://citizen.co.za/153133/sars-surpasses-tax-collection-target/" title="Sars surpasses tax collection target">
                                Sars surpasses tax collection target                            </a>
                        </span>
                    </div>
                                
                    	</div>
            </div>
                    <div class="page-lead-list-item">
                <div class="page-lead-list-item-3bar-article">
                            <div class="page-lead-list-item-3bar-single-article">
                                
                                                                        
                            <div class="page-lead-list-thumbnail-3bar thumbnail-portrait">
                                <a href="http://citizen.co.za/afp_feed_article/japan-lifts-self-imposed-arms-export-ban/" title="Japan lifts self-imposed arms export ban">
                                    <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/04/f31cc7fc0a8273a64dedd828ff89ccba50709597-150x150.jpg" alt="" />
                                </a>
                            </div>
                                                            
                        <span class="page-lead-list-headline-3bar">
                            <a href="http://citizen.co.za/afp_feed_article/japan-lifts-self-imposed-arms-export-ban/" title="Japan lifts self-imposed arms export ban">
                                Japan lifts self-imposed arms export ban                            </a>
                        </span>
                    </div>
                                
                        <div class="page-lead-list-item-separator"></div>                    <div class="page-lead-list-item-3bar-single-article">
                                
                                                                        
                            <div class="page-lead-list-thumbnail-3bar thumbnail-portrait">
                                <a href="http://citizen.co.za/153134/petrol-price-midnight-tonight/" title="Petrol price up at midnight tonight">
                                    <img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/09/photo_17162_20100314-150x150.jpg" alt="" />
                                </a>
                            </div>
                                                            
                        <span class="page-lead-list-headline-3bar">
                            <a href="http://citizen.co.za/153134/petrol-price-midnight-tonight/" title="Petrol price up at midnight tonight">
                                Petrol price up at midnight tonight                            </a>
                        </span>
                    </div>
                                
                        <div class="page-lead-list-item-separator"></div>                    <div class="page-lead-list-item-3bar-single-article">
                                
                                                                        
                            <div class="page-lead-list-thumbnail-3bar thumbnail-portrait">
                                <a href="http://citizen.co.za/153126/charges-itumeleng-khune-dropped/" title="Charges against Itumeleng Khune dropped">
                                    <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/Itumeleng-Khune-150x150.jpg" alt="" />
                                </a>
                            </div>
                                                            
                        <span class="page-lead-list-headline-3bar">
                            <a href="http://citizen.co.za/153126/charges-itumeleng-khune-dropped/" title="Charges against Itumeleng Khune dropped">
                                Charges against Itumeleng Khune dropped                            </a>
                        </span>
                    </div>
                                
                    	</div>
            </div>
                            </div>

                    <div class="clear"></div>
                    <div class="article-comment">
                                                    <a id="comments" NAME="commects-section"></a> 
                            <div class="article-comment-form">
                                								<div id="respond" class="comment-respond">
				<h3 id="reply-title" class="comment-reply-title">Comment <small><a rel="nofollow" id="cancel-comment-reply-link" href="/153078/outa-claims-proof-e-toll-mismanagement/#respond" style="display:none;">Cancel reply</a></small></h3>
									<form action="http://citizen.co.za/wp-comments-post.php" method="post" id="commentform" class="comment-form">
																			<p class="comment-notes">Your email address will not be published. Required fields are marked <span class="required">*</span></p>							<p class="comment-form-author"><label for="author">Name <span class="required">*</span></label> <input id="author" name="author" type="text" value="" size="30" aria-required='true' /></p>
<p class="comment-form-email"><label for="email">Email <span class="required">*</span></label> <input id="email" name="email" type="text" value="" size="30" aria-required='true' /></p>

												<p class="comment-form-comment"><label for="comment">Comment</label> <textarea id="comment" name="comment" cols="45" rows="8" aria-required="true"></textarea></p>						<div class="comment-mandatory">* Mandatory field</div>						<p class="form-submit">
							<input name="submit" type="submit" id="submit" value="Submit" />
							<input type='hidden' name='comment_post_ID' value='153078' id='comment_post_ID' />
<input type='hidden' name='comment_parent' id='comment_parent' value='0' />
						</p>
						<p style="display: none;"><input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="10a27b3b5a" /></p>					</form>
							</div><!-- #respond -->
			 
                            </div>
                    
                            <div class="clear"></div>
                    
                            <div class="comments-list">
                                                            </div>
                                      </div>
                </div>
            </div>
       
        <div class="fourcol last sidebar">
            <div class="sidebar-wrapper">
    
	
	                        
    <div class="textwidget">
        <div id="mpu-container" class="mpu-container">
            
                <script type="text/javascript">
                                                                OX_12345cxt.showAdUnit("459170");//MPU - news
                                                        </script>
            </div>
        </div>
    
    <div class="clear"></div>
	                    <div class="widget-special-events">
                    <!-- TABS -->
                        <div class="widget-special-events-header">
                        <!--PROUDLY BROUGHT TO YOU BY-->
                        </div>
                        <div class="widget-special-events-inner">
                            <div class="widget-special-events-header2">
                                <a href="http://citizen.co.za/category/news/oscar-trial/" title="">
                                    Oscar Trial                                </a>
                            </div>
                            <div class="widget-special-events-pic">
                                <a href="http://citizen.co.za/category/news/oscar-trial/" title="">
                                    <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/oscar_pistorious_spec_w.jpg">
                                </a>
                            </div>
                            <div class="widget-special-events-ticker">
                                <script type="text/javascript">
                                    jQuery(function () {
                                        jQuery('#js-news').ticker();
                                    });
                                </script>
                                <ul id="js-news" class="js-hidden">
                                                                        <li class="news-item">
                                            <a href="http://citizen.co.za/151337/pistorius-trial-adjourned-10-days/" title="Pistorius trial adjourned for 10 days">
                                                Pistorius trial adjourned for 10 days                                            </a>
                                        </li>
                                                                                <li class="news-item">
                                            <a href="http://citizen.co.za/151309/murdered-teens-parents-console-reevas-mom/" title="Murdered teen&#8217;s parents console Reeva&#8217;s mom">
                                                Murdered teen&#8217;s parents console<span class="special_cutoff"> ...</span>                                            </a>
                                        </li>
                                                                                <li class="news-item">
                                            <a href="http://citizen.co.za/151215/oscar-pistorius-trial-postponed/" title="Oscar Pistorius trial postponed">
                                                Oscar Pistorius trial postponed                                            </a>
                                        </li>
                                                                                <li class="news-item">
                                            <a href="http://citizen.co.za/151196/large-media-turnout-oscar-trial/" title="Large media turnout for Oscar trial">
                                                Large media turnout for Oscar trial                                            </a>
                                        </li>
                                                                                <li class="news-item">
                                            <a href="http://citizen.co.za/151016/the-case-oscar-has-to-answer/" title="The case Oscar has to answer">
                                                The case Oscar has to answer                                            </a>
                                        </li>
                                                                                <li class="news-item">
                                            <a href="http://citizen.co.za/149777/loving-relationship-resovled-fights-quickly/" title="Oscar and Reeva had a &#8220;loving relationship&#8221;">
                                                Oscar and Reeva had a &#8220;loving<span class="special_cutoff"> ...</span>                                            </a>
                                        </li>
                                                                                <li class="news-item">
                                            <a href="http://citizen.co.za/149754/ball-in-oscars-court/" title="Ball in Oscar&#8217;s court">
                                                Ball in Oscar&#8217;s court                                            </a>
                                        </li>
                                                                                <li class="news-item">
                                            <a href="http://citizen.co.za/149758/opening-chatline-pandoras-box/" title="Oscar trial: How to delete your WhatsApp messages">
                                                Oscar trial: How to delete your<span class="special_cutoff"> ...</span>                                            </a>
                                        </li>
                                                                                <li class="news-item">
                                            <a href="http://citizen.co.za/149537/oscar-testify-defence/" title="Oscar to testify &#8211; defence">
                                                Oscar to testify &#8211; defence                                            </a>
                                        </li>
                                                                                <li class="news-item">
                                            <a href="http://citizen.co.za/149529/state-closes-case-oscar-trial/" title="State closes its case in Oscar trial">
                                                State closes its case in Oscar trial                                            </a>
                                        </li>
                                                                        </ul>
                            </div>
                        </div>
                    </div>
                    <div class="clear"></div>
                          <div class="widget">
         
 
 <!-- TABS -->
	<div id="cxt-latest-most-read" class="tabbed-widget">
		<ul id="tabnav-cxt-latest-most-read" class="tabbed-widget-list">
			<li>
        		<a href="#cxt-top-read-1" title="Top read">
            		Top Read
				</a>
			</li>
			<li>
        		<a href="#cxt-talked-about-1" title="Talked about">
            		Talked About
				</a>
			</li>
            <li>
        		<a href="#cxt-latest-1" title="Latest">
            		Latest
				</a>
			</li>
		</ul>
    	
		<div id="cxt-top-read-1" class="panel">
			<div class="panel-content">
            	<div class="widget-body">
                
                                </div>
            </div>
        </div>  
        
        <div id="cxt-talked-about-1" class="panel">
        <div class="panel-content"> 
              <div class="widget-body">
        
                          
                            <div class="widget-item">
                              <div class="widget-item-counter">
                                  1                                </div>
                                <div class="widget-content-wrapper">
                                                        
                                          <div class="widget-full-thumbnail">
                                            <a href="http://citizen.co.za/152349/anc-bigwigs-odds-nkandla-fiasco/" title="Link to ANC bigwigs at odds over Nkandla fiasco">
                                              <img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/a1c065ac7f0209b7bd49fa914b1799ec1d92c1f8.jpg" alt="" />
                                            </a>
                                          </div>
                                                                        <h3>
                                        <a href="http://citizen.co.za/152349/anc-bigwigs-odds-nkandla-fiasco/" rel="bookmark" title="Link to ANC bigwigs at odds over Nkandla fiasco">
                                          <span class="widget-category-span news-national-category-color">
                                            National&nbsp;
                                          </span>
                                          <span class="widget-headline-span">
                                            ANC bigwigs at odds over Nkandla fiasco                                          </span>
                                        </a>
                                      </h3>
                                      <!--<span class="view-count"></span>-->
                                </div>
                            </div>
                   
                                    
                            <div class="widget-item">
                              <div class="widget-item-counter">
                                  2                                </div>
                                <div class="widget-content-wrapper">
                                                                      <h3>
                                        <a href="http://citizen.co.za/152479/dark-cloud-hangs-suraoure/" rel="bookmark" title="Link to Dark cloud hangs over SuraPure">
                                          <span class="widget-category-span news-business-category-color">
                                            Business&nbsp;
                                          </span>
                                          <span class="widget-headline-span">
                                            Dark cloud hangs over SuraPure                                          </span>
                                        </a>
                                      </h3>
                                      <!--<span class="view-count"></span>-->
                                </div>
                            </div>
                   
                                    
                            <div class="widget-item">
                              <div class="widget-item-counter">
                                  3                                </div>
                                <div class="widget-content-wrapper">
                                                                      <h3>
                                        <a href="http://citizen.co.za/152853/focus-corruption-zuma-says-blade/" rel="bookmark" title="Link to Focus on the corruption, not Zuma says Blade">
                                          <span class="widget-category-span news-national-category-color">
                                            National&nbsp;
                                          </span>
                                          <span class="widget-headline-span">
                                            Focus on the corruption, not Zuma says Blade                                          </span>
                                        </a>
                                      </h3>
                                      <!--<span class="view-count"></span>-->
                                </div>
                            </div>
                   
                                    
                            <div class="widget-item">
                              <div class="widget-item-counter">
                                  4                                </div>
                                <div class="widget-content-wrapper">
                                                                      <h3>
                                        <a href="http://citizen.co.za/152644/nkandla-zuma-micro-manager/" rel="bookmark" title="Link to Nkandla: Zuma not a &#8216;micro manager&#8217;">
                                          <span class="widget-category-span news-national-category-color">
                                            National&nbsp;
                                          </span>
                                          <span class="widget-headline-span">
                                            Nkandla: Zuma not a &#8216;micro manager&#8217;                                          </span>
                                        </a>
                                      </h3>
                                      <!--<span class="view-count"></span>-->
                                </div>
                            </div>
                   
                                    
                            <div class="widget-item">
                              <div class="widget-item-counter">
                                  5                                </div>
                                <div class="widget-content-wrapper">
                                                                      <h3>
                                        <a href="http://citizen.co.za/147375/ill-stand-president/" rel="bookmark" title="Link to I’ll stand  up for the  president">
                                          <span class="widget-category-span opinion-columns-category-color">
                                            Columns&nbsp;
                                          </span>
                                          <span class="widget-headline-span">
                                            I’ll stand  up for the  president                                          </span>
                                        </a>
                                      </h3>
                                      <!--<span class="view-count"></span>-->
                                </div>
                            </div>
                   
                  
                </div>
      </div>
    </div>
        
        <div id="cxt-latest-1" class="panel">
    		<div class="panel-content"> 
            	<div class="widget-body">
				
				                	
                    <div class="widget-item">
                            	<div class="widget-item-counter">
                                	1                                </div>
                                <div class="widget-content-wrapper">
                                												
													<div class="widget-full-thumbnail">
														<a href="http://citizen.co.za/153147/arms-inquiry-adjourned-4/" title="Link to Arms Inquiry adjourned">
															<img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/08/seriti.jpg" alt="" />
														</a>
													</div>
										                          		<h3>
                                	<a href="http://citizen.co.za/153147/arms-inquiry-adjourned-4/" rel="bookmark" title="Link to Arms Inquiry adjourned">
											<span class="widget-category-span news-national-category-color">
												National&nbsp;
                                           </span>
                                           <span class="widget-headline-span">
                                				Arms Inquiry adjourned                                           </span>
                            		</a>
                                    </h3>
                            		<span class="view-count">1.4.2014 02.35 pm</span>
                                </div>
                                </div>
                    
                                 	
                    <div class="widget-item">
                            	<div class="widget-item-counter">
                                	2                                </div>
                                <div class="widget-content-wrapper">
                                                        		<h3>
                                	<a href="http://citizen.co.za/153140/free-state-woman-found-dead/" rel="bookmark" title="Link to Free State woman found dead">
											<span class="widget-category-span news-national-category-color">
												National&nbsp;
                                           </span>
                                           <span class="widget-headline-span">
                                				Free State woman found dead                                           </span>
                            		</a>
                                    </h3>
                            		<span class="view-count">1.4.2014 02.27 pm</span>
                                </div>
                                </div>
                    
                                 	
                    <div class="widget-item">
                            	<div class="widget-item-counter">
                                	3                                </div>
                                <div class="widget-content-wrapper">
                                                        		<h3>
                                	<a href="http://citizen.co.za/153133/sars-surpasses-tax-collection-target/" rel="bookmark" title="Link to Sars surpasses tax collection target">
											<span class="widget-category-span news-business-category-color">
												Business&nbsp;
                                           </span>
                                           <span class="widget-headline-span">
                                				Sars surpasses tax collection target                                           </span>
                            		</a>
                                    </h3>
                            		<span class="view-count">1.4.2014 02.05 pm</span>
                                </div>
                                </div>
                    
                                 	
                    <div class="widget-item">
                            	<div class="widget-item-counter">
                                	4                                </div>
                                <div class="widget-content-wrapper">
                                                        		<h3>
                                	<a href="http://citizen.co.za/afp_feed_article/japan-lifts-self-imposed-arms-export-ban/" rel="bookmark" title="Link to Japan lifts self-imposed arms export ban">
											<span class="widget-category-span news-world-category-color">
												World&nbsp;
                                           </span>
                                           <span class="widget-headline-span">
                                				Japan lifts self-imposed arms export ban                                           </span>
                            		</a>
                                    </h3>
                            		<span class="view-count">1.4.2014 02.01 pm</span>
                                </div>
                                </div>
                    
                                 	
                    <div class="widget-item">
                            	<div class="widget-item-counter">
                                	5                                </div>
                                <div class="widget-content-wrapper">
                                                        		<h3>
                                	<a href="http://citizen.co.za/153134/petrol-price-midnight-tonight/" rel="bookmark" title="Link to Petrol price up at midnight tonight">
											<span class="widget-category-span news-national-category-color">
												National&nbsp;
                                           </span>
                                           <span class="widget-headline-span">
                                				Petrol price up at midnight tonight                                           </span>
                            		</a>
                                    </h3>
                            		<span class="view-count">1.4.2014 01.54 pm</span>
                                </div>
                                </div>
                    
                 
                </div>
			</div>
		</div>
	</div>
	<!-- end of widget-->
</div>
<div class="clear"></div>

	    
 <div class="widget">
 <!-- TABS -->
	<div id="cxt-daily-cartoon" class="tabbed-widget">
		<ul class="tabbed-widget-list">
			<li>
        		<a href="#cxt-daily-cartoon-1" title="Top read">
            		Daily Cartoon
				</a>
			</li>
			<li>
        		<a href="#cxt-opinion-1" title="Talked about">
            		Opinion
				</a>
			</li>
		</ul>
    	<div id="cxt-daily-cartoon-1" class="panel">
    		<div class="panel-content"> 
            	<div class="widget-body">
				
					                                <div class="widget-full-thumbnail">
                                                                        <a href="http://citizen.co.za?page_id=89343&ctype=cartoon-of-the-day" title="Cartoon of the day April 2014">
                                    	<img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/03/CARTOON14-300x212.jpg" alt="Cartoon of the day April 2014" /> 
                                    </a>
                                </div>                       
                                            
                    </div>
				</div>
			</div>
            <div id="cxt-opinion-1" class="panel">
    			<div class="panel-content"> 
            		<div class="widget-body">
                    
                    								
                            <div class="widget-item">
                            													
											<div class="widget-small-thumbnail">
												<a href="http://citizen.co.za/152790/law-keeps-poor-work/" title="Link to Law keeps the poor out of work">
													<img src="http://citizen.co.za/wp-content/uploads/sites/18/2013/08/andrewcol-e1376379423945.jpg" alt="" />
												</a>
											</div>
										                                    <div class="widget-small-wrapper">
                                        <div class="view-count opinion">
                                            Andrew Kenny                                        </div>
                                        <div class="widget-small-headline">
                                            <a href="http://citizen.co.za/152790/law-keeps-poor-work/" title="Law keeps the poor out of work" >
                                                Law keeps the poor out of work                                            </a>
                                        </div>
                                        <div class="widget-small-excerpt">
                                            By law, poor people are not allowed to get jobs in South Africa. &nbsp;...
                                        </div>
                                    </div>
                        	</div>
                            
														
                            <div class="widget-item">
                            													
											<div class="widget-small-thumbnail">
												<a href="http://citizen.co.za/152788/guide-gold-digers/" title="Link to A guide for gold diggers">
													<img src="http://citizen.co.za/wp-content/uploads/sites/18/2014/02/sexwale.jpg" alt="" />
												</a>
											</div>
										                                    <div class="widget-small-wrapper">
                                        <div class="view-count opinion">
                                            Kay Sexwale                                        </div>
                                        <div class="widget-small-headline">
                                            <a href="http://citizen.co.za/152788/guide-gold-digers/" title="A guide for gold diggers" >
                                                A guide for gold diggers                                            </a>
                                        </div>
                                        <div class="widget-small-excerpt">
                                            Reading the tabloids this weekend had me thinking about a seemingly easy way of making a living. &nbsp;...
                                        </div>
                                    </div>
                        	</div>
                            
							                    </div>
                </div>
            </div>

                    
                	

    </div>

	<!-- end of widget-->
</div>
<div class="clear"></div>

	    
 <div class="widget">
 <!-- TABS -->
	<div class="tabbed-widget">
		<ul class="tabbed-widget-list">
			<li>
        		Follow The Citizen
			</li>
		</ul>
    	<div class="panel">
    		<div class="panel-content"> 
            	<div class="widget-body">
                	<div class="social-media-links" style="float:left;">
					<a href="http://twitter.com/TheCitizen_News" target="_blank"><img src="http://citizen.co.za/wp-content/themes/citizen-v5-1/images/twitter.png" alt="Citizen twitter" /></a>
                    <a href="https://www.facebook.com/TheCitizenNewsaperSouthAfrica" target="_blank"><img src="http://citizen.co.za/wp-content/themes/citizen-v5-1/images/facebook.png" alt="Citizen Facebook" /></a>
                    <a href="https://plus.google.com/113672304772993300897/about" target="_blank"><img src="http://citizen.co.za/wp-content/themes/citizen-v5-1/images/googleplus.png" alt="Citizen Google+" /></a>
                    <a href="http://citizen.co.za/rss" target="_blank"><img src="http://citizen.co.za/wp-content/themes/citizen-v5-1/images/rss.png" alt="Citizen RSS Feed" /></a>
                    </div>
                </div>
			</div>
		</div>
	</div>
	<!-- end of widget-->
</div>
<div class="clear"></div>

	                            
    <div class="widget">
     <!-- TABS -->
        <div class="tabbed-widget">
            <ul class="tabbed-widget-list">
                <li>
                    Poll
                </li>
            </ul>
            <div class="panel">
                <div class="panel-content"> 
                    <div class="widget-body">
                    
                        
                            
                            <div class="widget-item">
                                
                                
                <div class='gf_browser_chrome gform_wrapper gpoll_enabled gpoll_show_results_link gpoll_wrapper' id='gform_wrapper_133' ><form method='post' enctype='multipart/form-data'  id='gform_133' class='gpoll_enabled gpoll_show_results_link gpoll' action='/153078/outa-claims-proof-e-toll-mismanagement/'>
                        <div class='gform_body'>
                            <ul id='gform_fields_133' class='gform_fields top_label description_below'><li id='field_133_1' class='gfield gpoll_field' ><label class='gfield_label'>The sick state of Government hospitals</label><div class='ginput_container'><ul class='gfield_radio' id='input_133_1'><li class='gchoice_1_0'><input name='input_1' type='radio' value='gpoll166b926cd'  id='choice_1_0' tabindex='1'    /><label for='choice_1_0'>Is the government's biggest failure</label></li><li class='gchoice_1_1'><input name='input_1' type='radio' value='gpoll134e020cd'  id='choice_1_1' tabindex='2'    /><label for='choice_1_1'>Is proof of wasted tax money</label></li><li class='gchoice_1_2'><input name='input_1' type='radio' value='gpoll1374a2553'  id='choice_1_2' tabindex='3'    /><label for='choice_1_2'>Is not true - they function well</label></li></ul></div></li>
                            </ul></div>
        <div class='gform_footer top_label'> <input type='submit' id='gform_submit_button_133' class='button gform_button' value='Submit' tabindex='4' onclick='if(window["gf_submitting_133"]){return false;}  window["gf_submitting_133"]=true; '/>
            <input type='hidden' class='gform_hidden' name='is_submit_133' value='1' />
            <input type='hidden' class='gform_hidden' name='gform_submit' value='133' />
            <input type='hidden' class='gform_hidden' name='gform_unique_id' value='' />
            <input type='hidden' class='gform_hidden' name='state_133' value='WyJhOjA6e30iLCJhZmU2MzI1NGZkOGZjYjBlZTkyYTE1MjVhZjliMjRjNyJd' />
            <input type='hidden' class='gform_hidden' name='gform_target_page_number_133' id='gform_target_page_number_133' value='0' />
            <input type='hidden' class='gform_hidden' name='gform_source_page_number_133' id='gform_source_page_number_133' value='1' />
            <input type='hidden' name='gform_field_values' value='' />
            
        </div>
                        </form>
                        </div><script type='text/javascript'> jQuery(document).ready(function(){jQuery(document).trigger('gform_post_render', [133, 1]) } ); </script>
                             
                            </div>
                   
                     	
               		</div>
            	</div>
        	</div>
     	</div>
    </div>
    <div class="clear"></div>
	
	                        
    <div class="widget">
     <!-- TABS -->
        <div class="tabbed-widget">
            <ul class="tabbed-widget-list">
                <li>
                    Today in Print
                </li>
            </ul>
            <div class="panel">
                <div class="panel-content"> 
                    <div class="widget-body">
                            <div class="widget-item">
                            	<div style="float:left; width: 130px; text-align:left;">
                                <a href="http://e-edition.citizen.co.za" title="The Citizen Today in Print" target="_blank">
                                	<img src="http://www.pressdisplay.com/advertising/showimage.aspx?cid=1457&type=thumb120"
                                    	title="Read today's edition"
                                        alt="Read Today's edition"
                                        target="_blank" />
                                </a>
                                </div>
                                <div style="font-size:1.1em">
                                	<strong>Subscribe now:</strong><br />
                                    Have The Citizen<br />
                                    delivered directly<br />
                                    to your desktop<br />
                                    hassle-free.<br />
                                    Stay connected<br />
                                    wherever you are.
                                </div>
                            </div>
                   			<div class="today-in-print-footer">
                            	<a href="http://e-edition.citizen.co.za" target="_blank"
                                    title="Subcribe to the electronic edition" >
                            			Subscribe to our e-edition
                                </a>
                     		</div>
               		</div>
            	</div>
        	</div>
     	</div>
    </div>
    <div class="clear"></div>
	    
    <div class="widget">
     <!-- TABS -->
        <div class="tabbed-widget">
            <ul class="tabbed-widget-list">
                <li>
                    Network News
                </li>
            </ul>
            <div class="panel">
                <div class="panel-content"> 
                    <div class="widget-body">
                    
                                                    
                            <div class="widget-item">
                                
                                <div class="view-count">
                                    looklocal Emalahleni Witbank                                </div>
                                
                                <h3>
                                	<span class="widget-headline-span">
                                        <a href="http://www.looklocal.co.za/looklocal/content/en/emalahleni-witbank/emalahleni-witbank-news-crime?oid=8248552&sn=Detail&pid=4730343&Break-in-at-a-church-" rel="bookmark" title="Break-in at a church" target="_blank">
                                            Break-in at a church                                        </a>
                                    </span>
                                </h3>
                             
                            </div>
                   
                     	                            
                            <div class="widget-item">
                                
                                <div class="view-count">
                                    looklocal North East Joburg                                </div>
                                
                                <h3>
                                	<span class="widget-headline-span">
                                        <a href="http://www.looklocal.co.za/looklocal/content/en/north-east-joburg/north-east-joburg-news-crime?oid=8241153&sn=Detail&pid=490266&Woman-dragged-out-of-taxi-and-beaten-by-gang-of-women" rel="bookmark" title="Woman dragged out of taxi and beaten by gang of women" target="_blank">
                                            Woman dragged out of taxi and beaten by gang of women                                        </a>
                                    </span>
                                </h3>
                             
                            </div>
                   
                     	                            
                            <div class="widget-item">
                                
                                <div class="view-count">
                                    looklocal Roodepoort                                </div>
                                
                                <h3>
                                	<span class="widget-headline-span">
                                        <a href="http://www.looklocal.co.za/looklocal/content/en/roodepoort/roodepoort-news-general?oid=8248432&sn=Detail&pid=489964&Partner-in-crime-shot-dead-during-house-robbery" rel="bookmark" title="Partner in crime shot dead during house robbery" target="_blank">
                                            Partner in crime shot dead during house robbery                                        </a>
                                    </span>
                                </h3>
                             
                            </div>
                   
                     	                            
                            <div class="widget-item">
                                
                                <div class="view-count">
                                    looklocal Centurion                                </div>
                                
                                <h3>
                                	<span class="widget-headline-span">
                                        <a href="http://www.looklocal.co.za/looklocal/content/en/centurion/centurion-news-general?oid=8248071&sn=Detail&pid=1345596&Fuel-prices-to-increase-again-" rel="bookmark" title="Fuel prices to increase again" target="_blank">
                                            Fuel prices to increase again                                        </a>
                                    </span>
                                </h3>
                             
                            </div>
                   
                     	                            
                            <div class="widget-item">
                                
                                <div class="view-count">
                                    looklocal Krugersdorp                                </div>
                                
                                <h3>
                                	<span class="widget-headline-span">
                                        <a href="http://www.looklocal.co.za/looklocal/content/en/krugersdorp/krugersdorp-news-crime?oid=8248491&sn=Detail&pid=489864&Ex-lover-arrested-for-rape" rel="bookmark" title="Ex-lover arrested for rape" target="_blank">
                                            Ex-lover arrested for rape                                        </a>
                                    </span>
                                </h3>
                             
                            </div>
                   
                     	               		</div>
            	</div>
        	</div>
     	</div>
    </div>
    <div class="clear"></div>

	
                            
    <div class="textwidget">
        <div id="halfpage-container" class="halfpage-container">
            
                <script type="text/javascript">
                                                                OX_12345cxt.showAdUnit("537079555");//halfpage - news section
                                                        </script>
           
        </div>
    </div>
    <div class="clear"></div>
        
    <div class="clear"></div>
    
</div>        </div>
    </div>

</div>
<script type="text/javascript">
            //var counter_url = null;
            //jQuery.get( counter_url );
        </script>
    <footer>
        <div class="row">
        
       		<div class="footer-wrapper">
          		<div class="twelvecol">
                <div class="footer-container">
            		<div class="footer-top">
                    	<div class="footer-utility-links">
                        <div class="menu-footer-utilities-container"><ul id="menu-footer-utilities" class="menu"><li id="menu-item-3929" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3929"><a href="http://citizen.co.za/contact-us/">Contact us</a></li>
<li id="menu-item-4284" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4284"><a href="http://citizen.co.za/about-us/">About us</a></li>
<li id="menu-item-3928" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3928"><a href="http://citizen.co.za/code-of-conduct/">Code of Conduct</a></li>
<li id="menu-item-3930" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3930"><a href="http://citizen.co.za/terms-of-use/">Terms of use</a></li>
</ul></div>                        </div>
                        <div class="footer-search">
                        <form role="search" method="get" id="searchform" class="searchform" action="http://citizen.co.za/">
				<div>
					<label class="screen-reader-text" for="s">Search for:</label>
					<input type="text" value="" name="s" id="s" />
					<input type="submit" id="searchsubmit" value="Search" />
				</div>
			</form>                        </div>
                    </div>
                    <div class="footer-middle">
                    	<div class="footer-emblem">
                        <img src="http://citizen.co.za/wp-content/themes/citizen-v5-1/images/citizen_footer_emblem.png" alt="Citizen" />
                   		</div>
                        <div class="footer-sitemap">
                                                
                        	<div class="footer-column-news">
                            NEWS
            <div class="menu-news-footer-container"><ul id="menu-news-footer" class="menu"><li id="menu-item-3693" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-3693"><a href="http://citizen.co.za/category/news/news-national/">National</a></li>
<li id="menu-item-3692" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3692"><a href="http://citizen.co.za/category/news/news-world/">World</a></li>
<li id="menu-item-3695" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3695"><a href="http://citizen.co.za/category/news/news-africa/">Africa</a></li>
<li id="menu-item-3694" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3694"><a href="http://citizen.co.za/category/news/news-business/">Business</a></li>
</ul></div>            				</div>
           					<div class="footer-column-opinion">
                            OPINION
            <div class="menu-opinion-footer-container"><ul id="menu-opinion-footer" class="menu"><li id="menu-item-3698" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3698"><a href="http://citizen.co.za/category/opinion/opinion-columns/">Columns</a></li>
<li id="menu-item-3699" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3699"><a href="http://citizen.co.za/category/opinion/opinion-editorials/">Editorials</a></li>
</ul></div>            				</div>
            
           					<div class="footer-column-sport">
                            SPORT
            <div class="menu-sport-footer-container"><ul id="menu-sport-footer" class="menu"><li id="menu-item-3713" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3713"><a href="http://citizen.co.za/category/sport/sport-columnists/">Columnists</a></li>
<li id="menu-item-3714" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3714"><a href="http://citizen.co.za/category/sport/sport-cricket/">Cricket</a></li>
<li id="menu-item-3715" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3715"><a href="http://citizen.co.za/category/sport/sport-other-sport/">Other sport</a></li>
<li id="menu-item-3716" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3716"><a href="http://citizen.co.za/category/sport/sport-rugby/">Rugby</a></li>
<li id="menu-item-3717" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3717"><a href="http://citizen.co.za/category/sport/sport-soccer/">Soccer</a></li>
<li id="menu-item-3718" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3718"><a href="http://citizen.co.za/category/sport/sport-soccer/soccer-bafana/">Bafana</a></li>
</ul></div>            				</div>
            
            				<div class="footer-column-horses">
                            HORSES
            <div class="menu-horses-footer-container"><ul id="menu-horses-footer" class="menu"><li id="menu-item-3706" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3706"><a href="http://citizen.co.za/category/horses/horses-columnists/">Columnists</a></li>
<li id="menu-item-3709" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3709"><a href="http://citizen.co.za/category/horses/horses-news/">Racing News</a></li>
</ul></div>            				</div>
            
            				<div class="footer-column-your-life">
                            YOUR LIFE
            <div class="menu-your-life-footer-container"><ul id="menu-your-life-footer" class="menu"><li id="menu-item-3723" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3723"><a href="http://citizen.co.za/category/your-life/your-life-entertainment/">Entertainment</a></li>
<li id="menu-item-3725" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3725"><a href="http://citizen.co.za/category/your-life/your-life-home-life/">Home LIfe</a></li>
<li id="menu-item-3726" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3726"><a href="http://citizen.co.za/category/your-life/your-life-things-to-do/your-life-food-and-drinks/">Food &#038; Drinks</a></li>
<li id="menu-item-3729" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3729"><a href="http://citizen.co.za/category/your-life/your-life-technology/">Digital Life</a></li>
<li id="menu-item-3730" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3730"><a href="http://citizen.co.za/category/your-life/your-life-things-to-do/">Things to do</a></li>
<li id="menu-item-3732" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3732"><a href="http://citizen.co.za/category/your-life/your-life-things-to-do/things-to-do-on-in-the-city/">On in the City</a></li>
<li id="menu-item-3734" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3734"><a href="http://citizen.co.za/category/your-life/your-life-things-to-do/things-to-do-travel/">Travel</a></li>
</ul></div>            				</div>            
                        
            				<div class="footer-column-motoring">
                            MOTORING
            <div class="menu-motoring-container"><ul id="menu-motoring" class="menu"><li id="menu-item-3702" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3702"><a href="http://citizen.co.za/category/motoring/motoring-car-tests-and-new-models/">Car Tests &amp; New Models</a></li>
<li id="menu-item-3703" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3703"><a href="http://citizen.co.za/category/motoring/motoring-motorsport/">Motorsport</a></li>
<li id="menu-item-3705" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3705"><a href="http://citizen.co.za/category/motoring/motoring-news/">Motoring News</a></li>
</ul></div>            				</div>   
            
            				<div class="footer-column-other">
                            OTHER
            <div class="menu-other-footer-container"><ul id="menu-other-footer" class="menu"><li id="menu-item-4961" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-4961"><a href="http://citizen.co.za/category/auctions/">Auctions</a></li>
<li id="menu-item-4962" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-4962"><a href="http://citizen.co.za/category/classifieds/">Classifieds</a></li>
<li id="menu-item-4957" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4957"><a href="http://citizen.co.za/about-us/">About us</a></li>
<li id="menu-item-4958" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4958"><a href="http://citizen.co.za/code-of-conduct/">Code of Conduct</a></li>
<li id="menu-item-4959" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4959"><a href="http://citizen.co.za/contact-us/">Contact us</a></li>
<li id="menu-item-4960" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4960"><a href="http://citizen.co.za/terms-of-use/">Terms of use</a></li>
<li id="menu-item-17482" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-17482"><a href="http://citizen.co.za/category/competitions/">Competitions</a></li>
<li id="menu-item-30973" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-30973"><a href="http://citizen.co.za/jobs-at-the-citizen/">Jobs at The Citizen</a></li>
</ul></div>            				</div>
            
            
                     
                        </div>
                    </div>
                	
                    <div class="footer-bottom">
                    <div class="footer-mobile">
                            
            <div class="menu-mobile-footer-menu-container"><ul id="menu-mobile-footer-menu" class="menu"><li id="menu-item-6501" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor menu-item-6501"><a href="http://citizen.co.za/category/news/">News</a></li>
<li id="menu-item-6502" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6502"><a href="http://citizen.co.za/category/opinion/">Opinion</a></li>
<li id="menu-item-6503" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6503"><a href="http://citizen.co.za/category/sport/">Sport</a></li>
<li id="menu-item-6504" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6504"><a href="http://citizen.co.za/category/your-life/">Your life</a></li>
<li id="menu-item-6499" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6499"><a href="http://citizen.co.za/category/horses/">Horses</a></li>
<li id="menu-item-6500" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6500"><a href="http://citizen.co.za/category/motoring/">Motoring</a></li>
<li id="menu-item-6497" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6497"><a href="http://citizen.co.za/category/auctions/">Auctions</a></li>
<li id="menu-item-6498" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6498"><a href="http://citizen.co.za/category/classifieds/">Classifieds</a></li>
<li id="menu-item-6493" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6493"><a href="http://citizen.co.za/about-us/">About us</a></li>
<li id="menu-item-6494" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6494"><a href="http://citizen.co.za/code-of-conduct/">Code of Conduct</a></li>
<li id="menu-item-6495" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6495"><a href="http://citizen.co.za/contact-us/">Contact us</a></li>
<li id="menu-item-6496" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6496"><a href="http://citizen.co.za/terms-of-use/">Terms of use</a></li>
</ul></div>            				</div>
                    	<div class="footer-logo">
                         <img src="http://citizen.co.za/wp-content/themes/citizen-v5-1/images/citizen_footer.png" alt="Citizen" /></div>
                        <div class="footer-rights">
                        © 2013 The Citizen. All rights reserved.
                        </div>
                    </div>
                
                
                </div>
           		</div>
       		</div>
        
        </div>
     </footer>
 </div>
  </div>  


                 
<!-- BEGIN GOOGLE ANALYTICS CODE -->
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount','UA-1099200-1'],
		['_trackPageview'],
		['server._setAccount', 'UA-1099200-10'],
		['server._trackPageview'],
		['server._setAccount', 'UA-27087662-4'],
		['server._trackPageview']);
    (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
</script>
<!-- END GOOGLE ANALYTICS CODE -->
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

<link rel='stylesheet' id='gforms_reset_css-css'  href='http://citizen.co.za/wp-content/plugins/gravityforms/css/formreset.css?ver=1.8.5' type='text/css' media='all' />
<link rel='stylesheet' id='gforms_datepicker_css-css'  href='http://citizen.co.za/wp-content/plugins/gravityforms/css/datepicker.css?ver=1.8.5' type='text/css' media='all' />
<link rel='stylesheet' id='gforms_formsmain_css-css'  href='http://citizen.co.za/wp-content/plugins/gravityforms/css/formsmain.css?ver=1.8.5' type='text/css' media='all' />
<link rel='stylesheet' id='gforms_ready_class_css-css'  href='http://citizen.co.za/wp-content/plugins/gravityforms/css/readyclass.css?ver=1.8.5' type='text/css' media='all' />
<link rel='stylesheet' id='gforms_browsers_css-css'  href='http://citizen.co.za/wp-content/plugins/gravityforms/css/browsers.css?ver=1.8.5' type='text/css' media='all' />
<link rel='stylesheet' id='gpoll_css-css'  href='http://citizen.co.za/wp-content/plugins/gravityformspolls/css/gpoll.css?ver=2.0' type='text/css' media='all' />
<script type='text/javascript' src='http://citizen.co.za/wp-content/plugins/ubermenu/core/js/hoverIntent.js?ver=3.8.1'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var uberMenuSettings = {"speed":"300","trigger":"hoverIntent","orientation":"horizontal","transition":"slide","hoverInterval":"20","hoverTimeout":"400","removeConflicts":"on","autoAlign":"off","noconflict":"on","fullWidthSubs":"on","androidClick":"off","iOScloseButton":"on","loadGoogleMaps":"off","repositionOnLoad":"on"};
/* ]]> */
</script>
<script type='text/javascript' src='http://citizen.co.za/wp-content/plugins/ubermenu/core/js/ubermenu.min.js?ver=3.8.1'></script>
<script type='text/javascript' src='http://citizen.co.za/wp-content/plugins/caxton-citizen-flexslider-wp-gallery/jquery-ui-1.9.2.custom.min.js?ver=3.8.1'></script>
<script type='text/javascript' src='http://citizen.co.za/wp-content/themes/citizen-v5-1/js/onload.scripts.js'></script>
<script type='text/javascript' src='http://citizen.co.za/wp-content/themes/citizen-v5-1/js/report-comments.scripts.js'></script>
<script type='text/javascript' src='http://citizen.co.za/wp-content/themes/citizen-v5-1/js/jquery.ticker.js'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var gpollVars = {"ajaxurl":"http:\/\/citizen.co.za\/wp-admin\/admin-ajax.php","imagesUrl":"http:\/\/citizen.co.za\/wp-content\/plugins\/gravityformspolls\/images"};
var gpoll_strings = {"viewResults":"View results","backToThePoll":"Back to the poll"};
/* ]]> */
</script>
<script type='text/javascript' src='http://citizen.co.za/wp-content/plugins/gravityformspolls/js/gpoll.js?ver=2.0'></script>


</body>
</html>
<!-- Performance optimized by W3 Total Cache. Learn more: http://www.w3-edge.com/wordpress-plugins/

Object Caching 6354/6414 objects using memcached

 Served from: citizen.co.za @ 2014-04-01 14:44:20 by W3 Total Cache -->
"""
        
        doc = Document()
        doc.url = 'http://citizen.co.za/153078/outa-claims-proof-e-toll-mismanagement/'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, 'Outa claims proof of e-toll mismanagement')
        self.assertEqual(doc.summary, u'The Opposition to Urban Tolling Alliance (Outa) has once again pleaded with government to listen to \u201ccritics\u201d against e-tolling, in light of new information provided by a whistle blower on the user payment system.')
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '01 04 2014')
        self.assertEqual(doc.author.name, "Yadhana Jadoo & Alex Mitchley")
        self.assertEqual(doc.medium.name, 'Citizen')

        self.assertEqual(doc.text, u'The Opposition to Urban Tolling Alliance (Outa) has once again pleaded with government to listen to \u201ccritics\u201d against e-tolling, in light of new information provided by a whistle blower on the user payment system.\n\nThis, as Outa awaits feedback from the Public Protector\u2019s office on a complaint it laid, following \u201cdamning\u201d information it received from a source within the system.\n\nThe City Press reported on Sunday that an employee of Austrian Company Kapsch \u2013 used to design the e-toll system \u2013 had warned the SA National Roads Agency Ltd (Sanral) of the high risk in the implementation of a national roll-out.\n\nHe said the e-tolling system was designed to monitor 7 000 km of national roads, with tolls being planned for Durban and Cape Town, it reported.\n\nThe source further stated that there were design flaws within the system and Sanral\u2019s control centre in Midrand had been created to monitor all roads in South Africa.\n\nIf the claims are true, it suggests that Sanral saw the Gauteng highway tolling project as either a starting point for national e-tolling, or it significantly over-invested in a system it did not need.\n\nSanral spokesman Vusi Mona, in rejecting the allegations by the \u201cso-called informant\u201d, said the Public Protector Thuli Madonsela had not yet contacted the entity.\n\nIt would however \u201cco-operate\u201d, should her office conduct an investigation, he added.\n\nMona said Sanral and its concessionaires were in the process of installing the \u201celectronic toll collection equipment\u201d needed at conventional toll plazas across the country.\n\nIt would make the exact details as to which toll plazas and  when this payment method will be available, at an \u201copportune time\u201d.\n\n\u201cElectronic toll collection \u2013 the use of e-tags \u2013 is a method of payment for one\u2019s toll fees. Electronic toll collection does not replace existing toll plazas. It is a tool that toll plazas will use in addition to current methods of payment.\n\n\u201cBy obtaining and e-tag and registering it, e-tolling allows an account holder to use the same e-tag and e-toll account to pay toll fees at any toll plaza equipped to accept e-tags.\u201d\n\nDeputy Public Protector Kevin Malunga, who was handling the complaint, according to Outa, was not immediately available for comment.\n\nOuta chairman Wayne Duvenage told The Citizen that the alliance had always provided an open door for Parliament\u2019s Portfolio Committee on Transport and Government\u2019s Inter-Ministerial Committee (IMC), which previously engaged with stakeholders against e-tolling, prior to its implementation.\n\nIt was important for government to learn from its critics, said Duvenage.\n\n\u201c\u2026 And they are not learning from their critics. We are happy to present to anybody.\u201d\n\nHe described previous IMC engagements as being unfruitful with government unwilling to unpack and explore the rationality of arguments.\n\nThe insider has described \u201cthem as arrogant and dangerous people who steam-roll public opinion \u2026 bully politicians, and business people and do not act in the interests of the country\u201d, according to Outa.\n\nDuvenage hailed the disclosures as a breakthrough which he hoped would start laying the table for \u201cmeaningful multi-lateral engagement with all stakeholders to transcend the mess\u201d.\n\n\u201cThe whistle blower shows the sheer arrogance of the system.\u201d\n\nHe further asked motorists not the \u201cfall\u201d for a system which was not working.\n\n\u201cThe compliance levels are far too low. Don\u2019t be hoodwinked by the propaganda. Now the chickens are coming out to roost.\u201d\n\nJustice Project South Africa (JPSA) chairperson Howard Dembovsky said it was only a matter of time until someone with a \u201cpaining conscious\u201d came forward.\n\n\u201cThis is a very good thing, we need more people to tell the truth behind what has happened and what is happening with the e-tolls,\u201d said Dembovsky.\n\nThe JPSA is convinced that there is corruption behind the controversial system: \u201cIt will come out in the dirty washing, a system rolled out veiled in shrouds of secrecy is a dead giveaway.\u201d\n\nDembovsky echoed Duvenage\u2019s comments, indicating that further IMC engagements would be \u201ca waste of time\u201d.\n\n\u201cThe last round of engagements was just Sanral telling people what was going to happen. Do not waste more time and our money,\u201d he said.\n\n\u201cTake the money and lets have a referendum, this is after all a democracy and we have not held a single referendum on the matter,\u201d said Dembovsky.\n\n\u201cLet\u2019s do it, let\u2019s show what democracy is all about,\u201d he added.\n\n\xa0')
        
