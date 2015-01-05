# -*- coding: utf-8 -*-

import unittest

from dexter.models import Document, Author
from dexter.models.support import db
from dexter.models.seeds import seed_db
from dexter.processing.crawlers.zambia import *

class TestZambiaDailyNationCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = ZambiaDailyNationCrawler()

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
<head profile="http://gmpg.org/xfn/11">

<title>Kalaba is Chipolopolo Captain - Daily Nation</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

    <link rel="stylesheet" type="text/css" href="http://zambiadailynation.com/wp-content/themes/gazette/style.css" media="screen" />
    <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="http://zambiadailynation.com/feed/" />
    <link rel="pingback" href="http://zambiadailynation.com/xmlrpc.php" />
       
    <!--[if IE 6]>
    <script type="text/javascript" src="http://zambiadailynation.com/wp-content/themes/gazette/includes/js/suckerfish.js"></script>
    <![endif]-->
            
<!-- This site is optimized with the Yoast WordPress SEO plugin v1.3.3 - http://yoast.com/wordpress/seo/ -->
<link rel="canonical" href="http://zambiadailynation.com/2015/01/04/kalaba-is-chipolopolo-captain/" />
<meta property='og:locale' content='en_US'/>
<meta property='og:title' content='Kalaba is Chipolopolo Captain - Daily Nation'/>
<meta property='og:url' content='http://zambiadailynation.com/2015/01/04/kalaba-is-chipolopolo-captain/'/>
<meta property='og:site_name' content='Daily Nation'/>
<meta property='og:type' content='article'/>
<!-- / Yoast WordPress SEO plugin. -->

<link rel="alternate" type="application/rss+xml" title="Daily Nation &raquo; Kalaba is Chipolopolo Captain Comments Feed" href="http://zambiadailynation.com/2015/01/04/kalaba-is-chipolopolo-captain/feed/" />
<script type='text/javascript' src='http://zambiadailynation.com/wp-includes/js/comment-reply.min.js?ver=3.7.4'></script>
<script type='text/javascript' src='http://zambiadailynation.com/wp-includes/js/jquery/jquery.js?ver=1.10.2'></script>
<script type='text/javascript' src='http://zambiadailynation.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.2.1'></script>
<script type='text/javascript' src='http://zambiadailynation.com/wp-content/themes/gazette/includes/js/scripts.js?ver=3.7.4'></script>
<script type='text/javascript' src='http://zambiadailynation.com/wp-content/themes/gazette/includes/js/superfish.js?ver=3.7.4'></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://zambiadailynation.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://zambiadailynation.com/wp-includes/wlwmanifest.xml" /> 
<meta name="generator" content="WordPress 3.7.4" />
<link rel='shortlink' href='http://zambiadailynation.com/?p=13103' />

<!-- Theme version -->
<meta name="generator" content="Gazette 2.9.14" />
<meta name="generator" content="WooFramework 5.3.12" />

<!-- Alt Stylesheet -->
<link href="http://zambiadailynation.com/wp-content/themes/gazette/styles/default.css" rel="stylesheet" type="text/css" />
<!-- Options Panel Custom CSS -->
<style type="text/css">
#archivebox {
background-color: transparent;
border: 1px solid white;
}
</style>


<!-- Woo Shortcodes CSS -->
<link href="http://zambiadailynation.com/wp-content/themes/gazette/functions/css/shortcodes.css" rel="stylesheet" type="text/css" />

<!-- Custom Stylesheet -->
<link href="http://zambiadailynation.com/wp-content/themes/gazette/custom.css" rel="stylesheet" type="text/css" />
<style type="text/css">

.wooslider .slider-container,.slider-container .slide  { height: 292px!important } 
.wooslider .slider-container .slide-content { top: 292px } }
</style>

	


</head>

<body class="single single-post postid-13103 single-format-standard chrome">

<!-- Set video category -->

<div id="page">

<div id="nav"> <!-- START TOP NAVIGATION BAR -->
	
		<div id="nav-left">
						<ul id="nav1">
			            
            					<li class="page_item"><a href="http://zambiadailynation.com/">Home</a></li>
								<li class="page_item page-item-19"><a href="http://zambiadailynation.com/about-daily-nation/">About Daily Nation</a></li>
<li class="page_item page-item-21"><a href="http://zambiadailynation.com/advertise-with-us/">Advertise With Us</a></li>
<li class="page_item page-item-28"><a href="http://zambiadailynation.com/terms/">Terms</a></li>
<li class="page_item page-item-30"><a href="http://zambiadailynation.com/contact/">Contact</a></li>
	
                
            	
			
			</ul>
					</div><!--/nav-left -->

		<div id="nav-right">		
		
			<form method="get" id="searchform" action="http://zambiadailynation.com/">
				
				<div id="search">
					<input type="text" value="Enter search keyword" onclick="this.value='';" name="s" id="s" />
					<input name="" type="image" src="http://zambiadailynation.com/wp-content/themes/gazette/images/search.gif" value="Go" class="btn" />
				</div><!--/search -->
				
			</form>
		
		</div><!--/nav-right -->
		
	</div><!--/nav-->
	
	<div class="fix"></div>
	
	<div id="header"><!-- START LOGO LEVEL WITH RSS FEED -->
		
		<div id="logo">
	       
		            <a href="http://zambiadailynation.com" title="The People&#039;s Paper">
                <img src="http://zambiadailynation.com/wp-content/uploads/2013/02/daily-nation-logo21.png" alt="Daily Nation" />
            </a>
         
        
                    <span class="site-title"><a href="http://zambiadailynation.com">Daily Nation</a></span>
                    <span class="site-description">The People&#039;s Paper</span>
	      	
		</div><!-- /#logo -->
		
		<!-- Top Ad Starts -->
			<div id="topbanner">

		
		<a href="http://www.tradecarview.com/"><img src="http://zambiadailynation.com/wp-content/uploads/2012/05/tradecarreview.jpg" width="468" height="60" alt="Advert" /></a>
		
		

</div>		<!-- Top Ad Ends -->
		
	</div><!--/header -->
    
    	
	
	<div id="suckerfish"><!-- START CATEGORY NAVIGATION (SUCKERFISH CSS) -->
			<ul id="nav2" class="menu"><li id="menu-item-35" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-35"><a href="http://zambiadailynation.com/category/home-news/">Home News</a></li>
<li id="menu-item-36" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-36"><a href="http://zambiadailynation.com/category/africa-news/">Africa News</a></li>
<li id="menu-item-39" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-39"><a href="http://zambiadailynation.com/category/international-news/">International News</a></li>
<li id="menu-item-37" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-37"><a href="http://zambiadailynation.com/category/sport/">Sport</a></li>
<li id="menu-item-38" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-38"><a href="http://zambiadailynation.com/category/editorial/">Editorial</a></li>
</ul>		
	</div><!--/nav2-->
	
    <div id="columns"><!-- START MAIN CONTENT COLUMNS -->
		<div class="col1">

			
					

				<div class="post-alt blog" id="post-13103">
				
					<h2><a title="Permanent Link to Kalaba is Chipolopolo Captain" href="http://zambiadailynation.com/2015/01/04/kalaba-is-chipolopolo-captain/" rel="bookmark">Kalaba is Chipolopolo Captain</a></h2>
					<p class="post_date">Posted on 04 January 2015. <span class="singletags"></span></p>
                    
                    					<div class="entry">
												<p align="right">
<p><b> </b></p>
<p><b> </b></p>
<p><b>CHIPOLOPOLO striker Rainsford Kalaba has been appointed captain of the team barely three weeks before the Africa Cup of Nations (AfCON) tournament kicks off in Equatorial Guinea after defender Stoppila Sunzu relinquished the role.</b></p>
<p>The first task of the young captain begins today when he will lead the boys in an international friendly encounter with South Africa’s Bafana Bafana.</p>
<p>Sunzu voluntarily quit and anointed Kalaba to take over from him after he was consulted on who should be his replacement and the technical bench approved his suggestion and congratulated him.</p>
<p>Football Association of Zambia (FAZ) spokesperson Nkweto Tembwe confirmed the development from South Africa yesterday.</p>
<p>Tembwe said Sunzu decided to voluntarily relinquish his captaincy so that he could concentrate on his role as defender.</p>
<p>When handing over the arm band to Kalaba, Sunzu thanked the football authorities in Zambia for giving him an opportunity to serve as Chipolopolo captain at a time the Chipolopolo were campaigning for the 2015 AfCON.</p>
<p>“Coach Honour Janza informed us that Stoppila Sunzu, who until this morning was the captain for Chipolopolo, has asked that he relinquish his position so that he can concentrate on his core role in the team which is being a defender,” he said.</p>
<p>“He (Sunzu) was asked on his opinion who should be given the arm band. Stophila suggested Rainsford Kalaba. As at now, the new captain for Chipolopolo is Rainsford Kalaba.”</p>
<p>Tembwe said Sunzu’s decision was first communicated to the senior players namely James Kamanga, Kennedy Mweene, Davies Nkausu, Nathan Sinkala and officials yesterday morning by Janza and they congratulated Kalaba.</p>
<p>“At the time he (Sunzu) was landing in South Africa he was a captain of Chipolopolo side and it is important to consult him in such a situation especially that he was not stripped of the captaincy. He has voluntarily relinquished saying he wants to concentrate on one role rather than having the control of leadership on the pitch,” he said.</p>
<p>Tembwe said by giving up the captaincy and anointing Kalaba, Sunzu had put the interest of the team above his own, adding that he was happy because he was handing over to somebody who he considers to be a leader.  He said if Sunzu was troubled with public criticism to have made such a decision to step aside, he had not shown it to anyone because he appeared very happy during training session at University of Johannesburg yesterday.</p>
<p>He, however, said he did not believe that Sunzu was troubled with anything but indicated that he was sure that the defender meditated over the decision before making the announcement.</p>
<p>Tembwe said Kalaba was happy to be appointed as captain for Chipolopolo and that he would work with other players.</p>
<p>“Rainsford Kalaba said he was happy about having been considered,” he said. “He also said other senior players are also captains. ‘We are all captains, even if it will be me wearing the band. Everyone remains a captain in his own right’.” And Chipolopolo team doctor Joseph Kabungo said apart from Patrick Ngoma, all the players were physically and mentally fit for the AfCON encounter this month. The team doctor said Ngoma was responding well to treatment and he would be ready for training on Monday.</p>
<p>“He (Ngoma) has done pretty well but we are still keeping a closer eye on him. He has been doing light training. He should be okay the remaining few days,” he said. “I am happy with his response to treatment,   he will be back in training on Monday. Apart from Patrick everyone is in good shape, all the guys are doing pretty well, physically, mentally. Everyone is okay.  We are hoping for a better performance in tomorrow’s game.”</p>
<div style=""><div style="display:inline;"><iframe src="http://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fzambiadailynation.com%2F2015%2F01%2F04%2Fkalaba-is-chipolopolo-captain%2F&amp;send=false&amp;layout=button_count&amp;width=120&amp;show_faces=false&amp;action=like&amp;colorscheme=light&amp;font&amp;height=21" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:120px; height:21px;" allowTransparency="true"></iframe></div><div style="display:inline;"><a href="http://twitter.com/share?url=http%3A%2F%2Fzambiadailynation.com%2F2015%2F01%2F04%2Fkalaba-is-chipolopolo-captain%2F" class="twitter-share-button" data-count="horizontal">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script></div><div style="display:inline;"><g:plusone size="medium" href="http://zambiadailynation.com/2015/01/04/kalaba-is-chipolopolo-captain/"></g:plusone><script type="text/javascript">(function() { var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true; po.src = 'https://apis.google.com/js/plusone.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s); })();</script></div></div>					</div>
				
				</div><!--/post-->

<div id="archivebox">
					
						<h3><em>Categorized |</em> <a href="http://zambiadailynation.com/category/sport/" title="View all posts in Sport" rel="category tag">Sport</a></h3>     
				
				</div><!--/archivebox-->
				
               	
                <div class="navigation">
    				<div class="alignleft"><a href="http://zambiadailynation.com/2015/01/04/its-time-to-judge-pf-mbulakulima/" rel="prev"><span class="meta-nav">&larr;</span> It’s time to judge PF-Mbulakulima</a></div>
    				<div class="alignright"><a href="http://zambiadailynation.com/2015/01/04/rebel-mmd-mps-face-expulsion/" rel="next">Rebel MMD MPs face expulsion <span class="meta-nav">&rarr;</span></a></div>
    	<br class="fix" />
				</div>

				<div id="comment">
					
<!-- You can start editing here. -->

<div id="comments">


			<!-- If comments are open, but there are no comments. -->

	 

</div> <!-- end #comments_wrap -->


<div id="respond">

<h3>Leave a Reply</h3>
<div class="cancel-comment-reply">
	<p><small><a rel="nofollow" id="cancel-comment-reply-link" href="/2015/01/04/kalaba-is-chipolopolo-captain/#respond" style="display:none;">Click here to cancel reply.</a></small></p>
</div>

<form action="http://zambiadailynation.com/wp-comments-post.php" method="post" id="commentform">


<p><input type="text" name="author" id="author" value="" size="22" tabindex="1" />
<label for="author"><small>Name (required)</small></label></p>

<p><input type="text" name="email" id="email" value="" size="22" tabindex="2" />
<label for="email"><small>Mail (will not be published) (required)</small></label></p>

<p><input type="text" name="url" id="url" value="" size="22" tabindex="3" />
<label for="url"><small>Website</small></label></p>


<!--<p><small><strong>XHTML:</strong> You can use these tags: &lt;a href=&quot;&quot; title=&quot;&quot;&gt; &lt;abbr title=&quot;&quot;&gt; &lt;acronym title=&quot;&quot;&gt; &lt;b&gt; &lt;blockquote cite=&quot;&quot;&gt; &lt;cite&gt; &lt;code&gt; &lt;del datetime=&quot;&quot;&gt; &lt;em&gt; &lt;i&gt; &lt;q cite=&quot;&quot;&gt; &lt;strike&gt; &lt;strong&gt; </small></p>-->

<p><textarea name="comment" id="comment" rows="10" tabindex="4" style="width:85%"></textarea></p>

<p><input name="submit" type="submit" id="submit" tabindex="5" value="Submit Comment" />
<input type="hidden" name="comment_post_ID" value="13103" />
</p>
<input type='hidden' name='comment_post_ID' value='13103' id='comment_post_ID' />
<input type='hidden' name='comment_parent' id='comment_parent' value='0' />
<p style="display: none;"><input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="c74af1b282" /></p>
</form>


<div class="fix"></div>
</div> <!-- end #respond -->

				</div>

					
								

		</div><!--/col1-->

<div class="col2">
	
	<div class="adspace-widget widget"><h3>Our Sponsor</h3>		
			<a href="http://jevic.co.jp/en/activities/regulatory-inspections/zambia/"><img src="http://zambiadailynation.com/wp-content/uploads/2013/04/Hellens-advert.png" alt="Jevic Japanese Auto Inspections" /></a>
	
		</div>  

 		<div id="tabs">
           
            <ul class="wooTabs">
                <li class="latest"><a href="#tab-latest">Latest</a></li>
                                <li class="popular"><a href="#tab-pop">Popular</a></li>                                <li class="comm"><a href="#tab-comm">Comments</a></li>                <li class="tags"><a href="#tab-tags">Tags</a></li>            	<li class="sub"><a href="#sub">Subscribe </a></li>            </ul>
            
            <div class="clear"></div>
            
            <div class="boxes box inside">
                        
	                            <ul id="tab-latest" class="list">
                    	<li>
				<a title="Poll credibility" href="http://zambiadailynation.com/2015/01/04/poll-credibility/">Poll credibility</a>
		<span class="meta">January 4, 2015</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="Rebel MMD MPs face expulsion" href="http://zambiadailynation.com/2015/01/04/rebel-mmd-mps-face-expulsion/">Rebel MMD MPs face expulsion</a>
		<span class="meta">January 4, 2015</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="Kalaba is Chipolopolo Captain" href="http://zambiadailynation.com/2015/01/04/kalaba-is-chipolopolo-captain/">Kalaba is Chipolopolo Captain</a>
		<span class="meta">January 4, 2015</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="It’s time to judge PF-Mbulakulima" href="http://zambiadailynation.com/2015/01/04/its-time-to-judge-pf-mbulakulima/">It’s time to judge PF-Mbulakulima</a>
		<span class="meta">January 4, 2015</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="PF has committed no crime-Scott" href="http://zambiadailynation.com/2015/01/04/pf-has-committed-no-crime-scott/">PF has committed no crime-Scott</a>
		<span class="meta">January 4, 2015</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="UPND govt won’t interfere in chiefs’ matters – HH" href="http://zambiadailynation.com/2015/01/04/upnd-govt-wont-interfere-in-chiefs-matters-hh/">UPND govt won’t interfere in chiefs’ matters – HH</a>
		<span class="meta">January 4, 2015</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="ECZ  to summon UPND veep" href="http://zambiadailynation.com/2015/01/04/ecz-to-summon-upnd-veep/">ECZ  to summon UPND veep</a>
		<span class="meta">January 4, 2015</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="MPs must live with electorate-FDD" href="http://zambiadailynation.com/2015/01/04/mps-must-live-with-electorate-fdd/">MPs must live with electorate-FDD</a>
		<span class="meta">January 4, 2015</span>
		<div class="fix"></div>
	</li>
	                    
                </ul>
	                            
                                <ul id="tab-pop" class="list">            
                    	<li>
				<a title="Harrington disagrees with possibility of national airline" href="http://zambiadailynation.com/2013/01/09/harrington-disagrees-with-possibility-of-national-airline/">Harrington disagrees with possibility of national airline</a>
		<span class="meta">January 9, 2013</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="Nigerian witness “clears” RB" href="http://zambiadailynation.com/2013/08/13/nigerian-witness-clears-rb/">Nigerian witness “clears” RB</a>
		<span class="meta">August 13, 2013</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="Kabimba warns of genocide" href="http://zambiadailynation.com/2013/02/27/kabimba-warns-of-genocide/">Kabimba warns of genocide</a>
		<span class="meta">February 27, 2013</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="Treat unemployment as a matter of urgency" href="http://zambiadailynation.com/2013/04/13/treat-unemployment-as-a-matter-of-urgency/">Treat unemployment as a matter of urgency</a>
		<span class="meta">April 13, 2013</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="M’membe choked  with DBZ debt &#8211; GBM" href="http://zambiadailynation.com/2013/09/02/mmembe-choked-with-dbz-debt-gbm/">M’membe choked  with DBZ debt &#8211; GBM</a>
		<span class="meta">September 2, 2013</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="Ilunda Chalo not for PF" href="http://zambiadailynation.com/2012/12/21/ilunda-chalo-not-for-pf/">Ilunda Chalo not for PF</a>
		<span class="meta">December 21, 2012</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="Secret arrests exposed" href="http://zambiadailynation.com/2013/01/11/secret-arrests-exposed/">Secret arrests exposed</a>
		<span class="meta">January 11, 2013</span>
		<div class="fix"></div>
	</li>
		<li>
				<a title="Pay KK’s K3.5bn debt" href="http://zambiadailynation.com/2013/04/02/pay-kks-k3-5bn-debt/">Pay KK’s K3.5bn debt</a>
		<span class="meta">April 2, 2013</span>
		<div class="fix"></div>
	</li>
	                    
                </ul>
                                                				<ul id="tab-comm" class="list">
                    				<li class="recentcomments">
					<img alt='' src='http://0.gravatar.com/avatar/a6ec97a36394de4ed69e805cfefaf2df?s=0&amp;d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D0&amp;r=G' class='avatar avatar-0 photo' height='0' width='0' />					<a href="http://zambiadailynation.com/2014/12/29/kambwili-threatens-to-ban-matete-for-life/#comment-46551" title="fort Jameson nzika on Kambwili threatens to ban Matete for life">fort Jameson nzika: at the recent pf 'convention' edgar was elected ...</a>
					<div class="fix"></div>
				</li>
							<li class="recentcomments">
					<img alt='' src='http://0.gravatar.com/avatar/21e810ea8d88ef57392581577a778735?s=0&amp;d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D0&amp;r=G' class='avatar avatar-0 photo' height='0' width='0' />					<a href="http://zambiadailynation.com/2014/12/29/nawakwi-invites-more-women-into-politics/#comment-46535" title="*Olemekezeka on Nawakwi invites more women into politics">*Olemekezeka: Sponsor their campaigns...</a>
					<div class="fix"></div>
				</li>
							<li class="recentcomments">
					<img alt='' src='http://1.gravatar.com/avatar/b040dfeb4f1d789f167a0bbd6437e50b?s=0&amp;d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D0&amp;r=G' class='avatar avatar-0 photo' height='0' width='0' />					<a href="http://zambiadailynation.com/2014/12/29/kaingu-faction-backs-edgar/#comment-46525" title="sate on Kaingu faction  backs Edgar">sate: PF welcomes the endorsements from the two MMD fact...</a>
					<div class="fix"></div>
				</li>
							<li class="recentcomments">
					<img alt='' src='http://1.gravatar.com/avatar/3ce376fc86cbaa4baf87c485b7ef916e?s=0&amp;d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D0&amp;r=G' class='avatar avatar-0 photo' height='0' width='0' />					<a href="http://zambiadailynation.com/2014/12/28/candidates-lying/#comment-46506" title="SIWALE GODFREY on Candidates lying">SIWALE GODFREY: That Makes Sense...</a>
					<div class="fix"></div>
				</li>
							<li class="recentcomments">
					<img alt='' src='http://1.gravatar.com/avatar/15bfa3857290dfccfc02fe35d384efe8?s=0&amp;d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D0&amp;r=G' class='avatar avatar-0 photo' height='0' width='0' />					<a href="http://zambiadailynation.com/2014/12/22/esther-back-with-victory/#comment-46505" title="FTJ on Esther back with victory">FTJ: Esther chikali...</a>
					<div class="fix"></div>
				</li>
							<li class="recentcomments">
					<img alt='' src='http://0.gravatar.com/avatar/82820788700726367fa023989b44958e?s=0&amp;d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D0&amp;r=G' class='avatar avatar-0 photo' height='0' width='0' />					<a href="http://zambiadailynation.com/2014/12/26/political-tribalism/#comment-46481" title="UPND on Political tribalism">UPND: Well written article - well done. Please do an ana...</a>
					<div class="fix"></div>
				</li>
							<li class="recentcomments">
					<img alt='' src='http://0.gravatar.com/avatar/c5d1104ca82e278e9aee23e9f8822ec2?s=0&amp;d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D0&amp;r=G' class='avatar avatar-0 photo' height='0' width='0' />					<a href="http://zambiadailynation.com/2014/12/26/political-tribalism/#comment-46480" title="scorescore on Political tribalism">scorescore: Tribalism is unproductive and as zambians we shoul...</a>
					<div class="fix"></div>
				</li>
							<li class="recentcomments">
					<img alt='' src='http://1.gravatar.com/avatar/7dedcad2c4c8b8d12cae7b7e46909d47?s=0&amp;d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D0&amp;r=G' class='avatar avatar-0 photo' height='0' width='0' />					<a href="http://zambiadailynation.com/2014/12/24/the-dismal-end-of-the-chikopa-tribunal-was-inevitable/#comment-46457" title="Winter Kabimba on The dismal end of the Chikopa tribunal was inevitable.">Winter Kabimba: Although I am not for retribution, i think a truth...</a>
					<div class="fix"></div>
				</li>
			                    
                </ul>                
                                                <div id="tab-tags" class="list">
                    <a href='http://zambiadailynation.com/tag/africa/' class='tag-link-28' title='1 topic' style='font-size: 12pt;'>Africa</a>
<a href='http://zambiadailynation.com/tag/chipolopolo/' class='tag-link-13' title='2 topics' style='font-size: 15.6pt;'>Chipolopolo</a>
<a href='http://zambiadailynation.com/tag/corruption/' class='tag-link-29' title='1 topic' style='font-size: 12pt;'>corruption</a>
<a href='http://zambiadailynation.com/tag/elections/' class='tag-link-18' title='2 topics' style='font-size: 15.6pt;'>Elections</a>
<a href='http://zambiadailynation.com/tag/eu/' class='tag-link-21' title='1 topic' style='font-size: 12pt;'>EU</a>
<a href='http://zambiadailynation.com/tag/euro-crisis/' class='tag-link-23' title='1 topic' style='font-size: 12pt;'>Euro Crisis</a>
<a href='http://zambiadailynation.com/tag/football/' class='tag-link-15' title='2 topics' style='font-size: 15.6pt;'>Football</a>
<a href='http://zambiadailynation.com/tag/greece/' class='tag-link-22' title='1 topic' style='font-size: 12pt;'>Greece</a>
<a href='http://zambiadailynation.com/tag/guy-scott/' class='tag-link-26' title='1 topic' style='font-size: 12pt;'>Guy Scott</a>
<a href='http://zambiadailynation.com/tag/ilunda-chalo/' class='tag-link-31' title='1 topic' style='font-size: 12pt;'>Ilunda Chalo</a>
<a href='http://zambiadailynation.com/tag/jacob-mulenga/' class='tag-link-24' title='1 topic' style='font-size: 12pt;'>Jacob Mulenga</a>
<a href='http://zambiadailynation.com/tag/john-boehner/' class='tag-link-10' title='1 topic' style='font-size: 12pt;'>John Boehner</a>
<a href='http://zambiadailynation.com/tag/judicial-corruption/' class='tag-link-20' title='2 topics' style='font-size: 15.6pt;'>judicial corruption</a>
<a href='http://zambiadailynation.com/tag/michael-sata/' class='tag-link-16' title='4 topics' style='font-size: 20pt;'>Michael Sata</a>
<a href='http://zambiadailynation.com/tag/mmd/' class='tag-link-12' title='1 topic' style='font-size: 12pt;'>MMD</a>
<a href='http://zambiadailynation.com/tag/nevers-mumba/' class='tag-link-11' title='1 topic' style='font-size: 12pt;'>Nevers Mumba</a>
<a href='http://zambiadailynation.com/tag/patriotic-front/' class='tag-link-17' title='4 topics' style='font-size: 20pt;'>Patriotic Front</a>
<a href='http://zambiadailynation.com/tag/pf/' class='tag-link-30' title='2 topics' style='font-size: 15.6pt;'>PF</a>
<a href='http://zambiadailynation.com/tag/robert-amsterdam/' class='tag-link-33' title='1 topic' style='font-size: 12pt;'>Robert Amsterdam</a>
<a href='http://zambiadailynation.com/tag/rule-of-law/' class='tag-link-19' title='2 topics' style='font-size: 15.6pt;'>rule of law</a>
<a href='http://zambiadailynation.com/tag/u-s-a/' class='tag-link-9' title='1 topic' style='font-size: 12pt;'>U.S.A.</a>
<a href='http://zambiadailynation.com/tag/world-cup/' class='tag-link-14' title='1 topic' style='font-size: 12pt;'>World Cup</a>
<a href='http://zambiadailynation.com/tag/wynter-kabimba/' class='tag-link-32' title='2 topics' style='font-size: 15.6pt;'>Wynter Kabimba</a>
<a href='http://zambiadailynation.com/tag/zambia/' class='tag-link-27' title='2 topics' style='font-size: 15.6pt;'>Zambia</a>                </div>                
                                
                    		    <div id="sub">
			        <ul>
						<li><h3>Stay up to date</h3><a href="http://zambiadailynation.com/feed/"><img src="http://zambiadailynation.com/wp-content/themes/gazette/images/ico-rss.gif" alt="" /></a></li>
						<li><a href="http://zambiadailynation.com/feed/">Subscribe to the RSS feed</a></li>
						<li><a href="" target="_blank">Subscribe to the feed via email</a></li>
					</ul>            
    		    </div>
                                

            </div><!-- /.boxes -->
			
        </div><!-- /wooTabs -->
    
         		<div id="recent-posts-2" class="block widget widget_recent_entries">		<h3>Recent Posts</h3>		<ul>
					<li>
				<a href="http://zambiadailynation.com/2015/01/04/poll-credibility/">Poll credibility</a>
						</li>
					<li>
				<a href="http://zambiadailynation.com/2015/01/04/rebel-mmd-mps-face-expulsion/">Rebel MMD MPs face expulsion</a>
						</li>
					<li>
				<a href="http://zambiadailynation.com/2015/01/04/kalaba-is-chipolopolo-captain/">Kalaba is Chipolopolo Captain</a>
						</li>
					<li>
				<a href="http://zambiadailynation.com/2015/01/04/its-time-to-judge-pf-mbulakulima/">It’s time to judge PF-Mbulakulima</a>
						</li>
					<li>
				<a href="http://zambiadailynation.com/2015/01/04/pf-has-committed-no-crime-scott/">PF has committed no crime-Scott</a>
						</li>
				</ul>
		</div><div id="archives-2" class="block widget widget_archive"><h3>Archives</h3>		<ul>
			<li><a href='http://zambiadailynation.com/2015/01/'>January 2015</a></li>
	<li><a href='http://zambiadailynation.com/2014/12/'>December 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/11/'>November 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/10/'>October 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/09/'>September 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/08/'>August 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/07/'>July 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/06/'>June 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/05/'>May 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/04/'>April 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/03/'>March 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/02/'>February 2014</a></li>
	<li><a href='http://zambiadailynation.com/2014/01/'>January 2014</a></li>
	<li><a href='http://zambiadailynation.com/2013/12/'>December 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/11/'>November 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/10/'>October 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/09/'>September 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/08/'>August 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/07/'>July 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/06/'>June 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/05/'>May 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/04/'>April 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/03/'>March 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/02/'>February 2013</a></li>
	<li><a href='http://zambiadailynation.com/2013/01/'>January 2013</a></li>
	<li><a href='http://zambiadailynation.com/2012/12/'>December 2012</a></li>
	<li><a href='http://zambiadailynation.com/2012/11/'>November 2012</a></li>
	<li><a href='http://zambiadailynation.com/2012/10/'>October 2012</a></li>
	<li><a href='http://zambiadailynation.com/2012/09/'>September 2012</a></li>
	<li><a href='http://zambiadailynation.com/2012/08/'>August 2012</a></li>
	<li><a href='http://zambiadailynation.com/2012/07/'>July 2012</a></li>
	<li><a href='http://zambiadailynation.com/2012/05/'>May 2012</a></li>
		</ul>
</div><div id="categories-2" class="block widget widget_categories"><h3>Categories</h3>		<ul>
	<li class="cat-item cat-item-25"><a href="http://zambiadailynation.com/category/add-to-homepage-slideshow/" title="View all posts filed under Add to Homepage Slideshow">Add to Homepage Slideshow</a>
</li>
	<li class="cat-item cat-item-4"><a href="http://zambiadailynation.com/category/africa-news/" title="View all posts filed under Africa News">Africa News</a>
</li>
	<li class="cat-item cat-item-6"><a href="http://zambiadailynation.com/category/editorial/" title="View all posts filed under Editorial">Editorial</a>
</li>
	<li class="cat-item cat-item-3"><a href="http://zambiadailynation.com/category/home-news/" title="View all posts filed under Home News">Home News</a>
</li>
	<li class="cat-item cat-item-7"><a href="http://zambiadailynation.com/category/international-news/" title="View all posts filed under International News">International News</a>
</li>
	<li class="cat-item cat-item-5"><a href="http://zambiadailynation.com/category/sport/" title="View all posts filed under Sport">Sport</a>
</li>
	<li class="cat-item cat-item-1"><a href="http://zambiadailynation.com/category/uncategorized/" title="View all posts filed under Uncategorized">Uncategorized</a>
</li>
		</ul>
</div> 
	
	<div class="fix"></div>
    
    <div class="subcol fl">

	 
                   
    </div><!--/subcol-->
	
	<div class="subcol fr">
	
	 
			
	</div><!--/subcol-->
		
<div class="fix"></div>
	
</div><!--/col2-->

		<div class="fix"></div>

	</div><!--/columns -->
	
	<div id="footer">
		 <p class="fl">&copy; 2015 Daily Nation. Powered by <a href="#">WordPress</a>.</p>
            <p class="fr"><a href="http://www.woothemes.com">Gazette Theme</a> by <a href="http://www.woothemes.com" title="WooThemes - Premium WordPress Themes"><img src="http://zambiadailynation.com/wp-content/themes/gazette/images/woothemes.gif" width="85" height="24" alt="WooThemes - Premium WordPress Themes" /></a></p>
	</div><!--/footer -->

</div><!--/page -->

<p style="text-align:center;font-size:x-small;color:#808080;"><a style="font-weight:normal;color:#808080" href="http://www.ab-weblog.com/en/wordpress-plug-ins/social-widgets/" title="Facebook, Twitter &amp; Google+ Social Widgets" target="_blank">Social Widgets</a> powered by <a style="font-weight:normal;color:#808080" href="http://www.ab-weblog.com/en/" title="Software Developer Blog" target="_blank">AB-WebLog.com</a>.</p><script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-34409587-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
<!-- Woo Tabs Widget -->
<script type="text/javascript">
jQuery(document).ready(function(){
	// UL = .wooTabs
	// Tab contents = .inside
	
	var tag_cloud_class = '#tagcloud'; 
	
	//Fix for tag clouds - unexpected height before .hide() 
	var tag_cloud_height = jQuery('#tagcloud').height();
	
	jQuery('.inside ul li:last-child').css('border-bottom','0px'); // remove last border-bottom from list in tab content
	jQuery('.wooTabs').each(function(){
		jQuery(this).children('li').children('a:first').addClass('selected'); // Add .selected class to first tab on load
	});
	jQuery('.inside > *').hide();
	jQuery('.inside > *:first-child').show();
	
	jQuery('.wooTabs li a').click(function(evt){ // Init Click funtion on Tabs
	
		var clicked_tab_ref = jQuery(this).attr('href'); // Strore Href value
		
		jQuery(this).parent().parent().children('li').children('a').removeClass('selected'); //Remove selected from all tabs
		jQuery(this).addClass('selected');
		jQuery(this).parent().parent().parent().children('.inside').children('*').hide();
		
		jQuery('.inside ' + clicked_tab_ref).fadeIn(500);
		 
		 evt.preventDefault();
	
	})
})
</script>



</body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://zambiadailynation.com/2015/01/04/kalaba-is-chipolopolo-captain/'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, 'Kalaba is Chipolopolo Captain')
        self.assertIsNone(doc.summary)
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '04 01 2015')
        self.assertEqual(doc.author, Author.unknown())
        self.assertEqual(doc.medium.name, 'Daily Nation')

        self.assertEqual(doc.text, u'\n\n\n\n\n\nCHIPOLOPOLO striker Rainsford Kalaba has been appointed captain of the team barely three weeks before the Africa Cup of Nations (AfCON) tournament kicks off in Equatorial Guinea after defender Stoppila Sunzu relinquished the role.\n\nThe first task of the young captain begins today when he will lead the boys in an international friendly encounter with South Africa\u2019s Bafana Bafana.\n\nSunzu voluntarily quit and anointed Kalaba to take over from him after he was consulted on who should be his replacement and the technical bench approved his suggestion and congratulated him.\n\nFootball Association of Zambia (FAZ) spokesperson Nkweto Tembwe confirmed the development from South Africa yesterday.\n\nTembwe said Sunzu decided to voluntarily relinquish his captaincy so that he could concentrate on his role as defender.\n\nWhen handing over the arm band to Kalaba, Sunzu thanked the football authorities in Zambia for giving him an opportunity to serve as Chipolopolo captain at a time the Chipolopolo were campaigning for the 2015 AfCON.\n\n\u201cCoach Honour Janza informed us that Stoppila Sunzu, who until this morning was the captain for Chipolopolo, has asked that he relinquish his position so that he can concentrate on his core role in the team which is being a defender,\u201d he said.\n\n\u201cHe (Sunzu) was asked on his opinion who should be given the arm band. Stophila suggested Rainsford Kalaba. As at now, the new captain for Chipolopolo is Rainsford Kalaba.\u201d\n\nTembwe said Sunzu\u2019s decision was first communicated to the senior players namely James Kamanga, Kennedy Mweene, Davies Nkausu, Nathan Sinkala and officials yesterday morning by Janza and they congratulated Kalaba.\n\n\u201cAt the time he (Sunzu) was landing in South Africa he was a captain of Chipolopolo side and it is important to consult him in such a situation especially that he was not stripped of the captaincy. He has voluntarily relinquished saying he wants to concentrate on one role rather than having the control of leadership on the pitch,\u201d he said.\n\nTembwe said by giving up the captaincy and anointing Kalaba, Sunzu had put the interest of the team above his own, adding that he was happy because he was handing over to somebody who he considers to be a leader.  He said if Sunzu was troubled with public criticism to have made such a decision to step aside, he had not shown it to anyone because he appeared very happy during training session at University of Johannesburg yesterday.\n\nHe, however, said he did not believe that Sunzu was troubled with anything but indicated that he was sure that the defender meditated over the decision before making the announcement.\n\nTembwe said Kalaba was happy to be appointed as captain for Chipolopolo and that he would work with other players.\n\n\u201cRainsford Kalaba said he was happy about having been considered,\u201d he said. \u201cHe also said other senior players are also captains. \u2018We are all captains, even if it will be me wearing the band. Everyone remains a captain in his own right\u2019.\u201d And Chipolopolo team doctor Joseph Kabungo said apart from Patrick Ngoma, all the players were physically and mentally fit for the AfCON encounter this month. The team doctor said Ngoma was responding well to treatment and he would be ready for training on Monday.\n\n\u201cHe (Ngoma) has done pretty well but we are still keeping a closer eye on him. He has been doing light training. He should be okay the remaining few days,\u201d he said. \u201cI am happy with his response to treatment,   he will be back in training on Monday. Apart from Patrick everyone is in good shape, all the guys are doing pretty well, physically, mentally. Everyone is okay.  We are hoping for a better performance in tomorrow\u2019s game.\u201d')
        

class TestLusakaTimesCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = LusakaTimesCrawler()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_extract(self):
        html = """

<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8"/>
<title>Zambia : UPND intensifies campaign in Western province</title>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="template" content="Lusakatimes 1.2.1"/>
<meta name="generator" content="WordPress 4.1"/>
 
<link rel="original-source" href=""/>
<meta name="description" content="Lusaka - Zambia: UPND Mongu rally The United Party for National Development (UPND) has intensified its Presidential campaigns and its candidate, Hakainde Hichilema, is now"/>
<link rel="canonical" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/"/>
 
<link rel="alternate" type="application/rss+xml" title="LusakaTimes.com &raquo; Feed" href="http://www.lusakatimes.com/feed/"/>
<link rel="alternate" type="application/rss+xml" title="LusakaTimes.com &raquo; Comments Feed" href="http://www.lusakatimes.com/comments/feed/"/>
<link rel="alternate" type="application/rss+xml" title="LusakaTimes.com &raquo; UPND intensifies campaign in Western province Comments Feed" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/feed/"/>
<style type='text/css'>table.leaguemanager th{background-color:#69AEE7}table.standingstable tr.ascend,table.standingstable tr.ascend.alternate{background-color:#00FF66}table.standingstable tr.descend,table.standingstable tr.descend.alternate{background-color:#FFFFFF}table.standingstable tr.relegation,table.standingstable tr.relegation.alternate{background-color:#FFB6C1}</style><link rel='stylesheet' id='yarppWidgetCss-css' href='http://www.lusakatimes.com/wp-content/plugins/yet-another-related-posts-plugin/style/widget.css?ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='updownupdown-css' href='http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/style/updownupdown.css?ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='twitter-follow-widget-style-css' href='http://www.lusakatimes.com/wp-content/plugins/wp-twitter-mega-fan-box/followbox/followbox.css?ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='twitter-follow-color-style-css' href='http://www.lusakatimes.com/wp-content/plugins/wp-twitter-mega-fan-box/color-picker/css/colorpicker.css?ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='stargazer-fonts-css' href='//fonts.googleapis.com/css?family=Droid+Serif%3A400%2C700%2C400italic%2C700italic%7COpen+Sans%3A300%2C400%2C600%2C700&#038;ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='one-five-css' href='http://www.lusakatimes.com/wp-content/themes/lusaskatimes/library/css/one-five.min.css?ver=20131105' type='text/css' media='all'/>
<link rel='stylesheet' id='gallery-css' href='http://www.lusakatimes.com/wp-content/themes/lusaskatimes/library/css/gallery.min.css?ver=20130526' type='text/css' media='all'/>
<link rel='stylesheet' id='stargazer-mediaelement-css' href='http://www.lusakatimes.com/wp-content/themes/lusaskatimes/css/mediaelement/mediaelement.min.css?ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='style-css' href='http://www.lusakatimes.com/wp-content/themes/lusaskatimes/style.css?ver=1.2.1' type='text/css' media='all'/>
<link rel='stylesheet' id='cwpcss-css' href='http://www.lusakatimes.com/wp-content/plugins/cardoza-wordpress-poll/public/css/CWPPoll.css?ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='cwpcssjqui-css' href='http://www.lusakatimes.com/wp-content/plugins/cardoza-wordpress-poll/public/css/JqueryUi.css?ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='wp-email-css' href='http://www.lusakatimes.com/wp-content/plugins/wp-email/email-css.css?ver=2.60' type='text/css' media='all'/>
<link rel='stylesheet' id='jetpack_css-css' href='http://www.lusakatimes.com/wp-content/plugins/jetpack/css/jetpack.css?ver=3.3' type='text/css' media='all'/>
<link rel='stylesheet' id='dashicons-css' href='http://www.lusakatimes.com/wp-includes/css/dashicons.min.css?ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='thickbox-css' href='http://www.lusakatimes.com/wp-includes/js/thickbox/thickbox.css?ver=4.1' type='text/css' media='all'/>
<link rel='stylesheet' id='leaguemanager-css' href='http://www.lusakatimes.com/wp-content/plugins/leaguemanager/style.css?ver=1.0' type='text/css' media='screen'/>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-includes/js/jquery/jquery.js?ver=1.11.1'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.2.1'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/js/updownupdown.js?ver=1.0'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/wp-twitter-mega-fan-box/followbox/jquery.followbox.js?ver=4.1'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/wp-twitter-mega-fan-box/color-picker/js/colorpicker.js?ver=4.1'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/wp-twitter-mega-fan-box/color-picker/js/colorpicker.js?ver=4.1'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/wp-twitter-mega-fan-box/color-picker/js/colorpicker.js?ver=4.1'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/wp-twitter-mega-fan-box/color-picker/js/colorpicker.js?ver=4.1'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-includes/js/jquery/ui/core.min.js?ver=1.11.2'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/cardoza-wordpress-poll/public/js/CWPPoll.js?ver=4.1'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/cardoza-wordpress-poll/public/js/jquery.ui.datepicker.min.js?ver=4.1'></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://www.lusakatimes.com/xmlrpc.php?rsd"/>
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://www.lusakatimes.com/wp-includes/wlwmanifest.xml"/>
<link rel='shortlink' href='http://wp.me/pjJcM-miQ'/>
<script type='text/javascript'>
 var CwppPlgSettings = {
   ajaxurl : 'http://www.lusakatimes.com/wp-admin/admin-ajax.php',
   nonce : '995a301640'
 };
</script>
<link type="text/css" rel="stylesheet" href="http://www.lusakatimes.com/wp-content/plugins/simple-pull-quote/css/simple-pull-quote.css"/>
<script type="text/javascript">var UpDownUpDown = { ajaxurl: "http://www.lusakatimes.com/wp-admin/admin-ajax.php" };</script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/wp-spamshield/js/jscripts.php'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-includes/js/tw-sack.min.js?ver=1.6.1'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var thickboxL10n = {"next":"Next >","prev":"< Prev","image":"Image","of":"of","close":"Close","noiframes":"This feature requires inline frames. You have iframes disabled or your browser does not support them.","loadingAnimation":"http:\/\/www.lusakatimes.com\/wp-includes\/js\/thickbox\/loadingAnimation.gif"};
/* ]]> */
</script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-includes/js/thickbox/thickbox.js?ver=3.1-20121105'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/leaguemanager/leaguemanager.js?ver=3.8.9'></script>
<script type="text/javascript">
		//<![CDATA[
		LeagueManagerAjaxL10n = {
			blogUrl: "http://www.lusakatimes.com", pluginPath: "/var/www/lusakatimes.com/htdocs/wp-content/plugins/leaguemanager", pluginUrl: "http://www.lusakatimes.com/wp-content/plugins/leaguemanager", requestUrl: "http://www.lusakatimes.com/wp-content/plugins/leaguemanager/ajax.php", Edit: "Edit", Post: "Post", Save: "Save", Cancel: "Cancel", pleaseWait: "Please wait...", Revisions: "Page Revisions", Time: "Insert time", Options: "Options", Delete: "Delete"
	 	}
		//]]>
		</script>
<style type="text/css" id="custom-colors-css">a,.wp-playlist-light .wp-playlist-playing{color:rgba(2,98,126,0.75);}a:hover,a:focus,legend,mark,.comment-respond .required,pre,.form-allowed-tags code,pre code,.wp-playlist-light .wp-playlist-item:hover,.wp-playlist-light .wp-playlist-item:focus,.mejs-button button:hover::after,.mejs-button button:focus::after,.mejs-overlay-button:hover::after,.mejs-overlay-button:focus::after{color:#02627e;}input[type='submit'],input[type='reset'],input[type='button'],button,.page-links a,.comment-reply-link,.comment-reply-login,.wp-calendar td.has-posts a,#menu-sub-terms li a{background-color:rgba(2,98,126,0.8);}legend,mark,pre,.form-allowed-tags code{background-color:rgba(2,98,126,0.1);}input[type='submit']:hover,input[type='submit']:focus,input[type='reset']:hover,input[type='reset']:focus,input[type='button']:hover,input[type='button']:focus,button:hover,button:focus,.page-links a:hover,.page-links a:focus,.wp-calendar td.has-posts a:hover,.wp-calendar td.has-posts a:focus,.widget-title>.wrap,#comments-number>.wrap,#reply-title>.wrap,.attachment-meta-title>.wrap,.widget_search>.search-form,#menu-sub-terms li a:hover,#menu-sub-terms li a:focus,.comment-reply-link:hover,.comment-reply-link:focus,.comment-reply-login:hover,.comment-reply-login:focus,.mejs-time-rail .mejs-time-loaded,.skip-link .screen-reader-text{background-color:#02627e;}::selection{background-color:#02627e;}legend{border-color:rgba(2,98,126,0.15);}body{border-top-color:#02627e;}.entry-content a,.entry-summary a,.comment-content a{border-bottom-color:rgba(2,98,126,0.15);}.entry-content a:hover,.entry-content a:focus,.entry-summary a:hover,.entry-summary a:focus,.comment-content a:hover,.comment-content a:focus{border-bottom-color:rgba(2,98,126,0.75);}body,.widget-title,#comments-number,#reply-title,.attachment-meta-title{border-bottom-color:#02627e;}blockquote{background-color:rgba(2,98,126,0.85);}blockquote blockquote{background-color:rgba(2,98,126,0.9);}blockquote{outline-color:rgba(2,98,126,0.85);}</style>
<style type="text/css" id="custom-background-css">body.custom-background{background:#dddddd;}</style>
 
<meta property="og:type" content="article"/>
<meta property="og:title" content="UPND intensifies campaign in Western province"/>
<meta property="og:url" content="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/"/>
<meta property="og:description" content="The United Party for National Development (UPND) has intensified its Presidential campaigns and its candidate, Hakainde Hichilema, is now in the Western Province for a series of rallies ahead of th..."/>
<meta property="article:published_time" content="2015-01-05T12:09:29+00:00"/>
<meta property="article:modified_time" content="2015-01-05T12:10:32+00:00"/>
<meta property="article:author" content="https://www.facebook.com/lusakatimes"/>
<meta property="og:site_name" content="LusakaTimes.com"/>
<meta property="og:image" content="http://www.lusakatimes.com/wp-content/uploads/2015/01/Mongu-Crowds-1.jpg"/>
<meta property="og:image" content="http://www.lusakatimes.com/wp-content/uploads/2015/01/Mongu-Crowd.jpg"/>
<meta property="og:image" content="http://www.lusakatimes.com/wp-content/uploads/2015/01/HH-William-Harrington.jpg"/>
<meta property="og:image" content="http://www.lusakatimes.com/wp-content/uploads/2015/01/HH-Mongu.jpg"/>
<meta property="og:image" content="http://www.lusakatimes.com/wp-content/uploads/2015/01/HH-Induna-Inete.jpg"/>
<meta property="og:image" content="http://www.lusakatimes.com/wp-content/uploads/2015/01/HH-1.jpg"/>
<meta name="twitter:site" content="@lusakatimes"/>
<meta name="twitter:image" content="http://www.lusakatimes.com/wp-content/uploads/2015/01/Mongu-Crowds-1.jpg?w=240"/>
<meta name="twitter:card" content="summary"/>
<meta name="twitter:creator" content="@lusakatimes"/>
<link rel="stylesheet" href="http://www.lusakatimes.com/wp-content/plugins/oiopub-direct/images/style/output.css" type="text/css"/>
<script type="text/javascript">
  window._taboola = window._taboola || [];
  _taboola.push({article:'auto'});
  !function (e, f, u) {
    e.async = 1;
    e.src = u;
    f.parentNode.insertBefore(e, f);
  }(document.createElement('script'),
  document.getElementsByTagName('script')[0],
  'http://cdn.taboola.com/libtrc/lusakatimes/loader.js');
</script>
</head>
<body class="wordpress ltr en en-us parent-theme y2015 m01 d05 h15 monday logged-out custom-background singular singular-post singular-post-85736 post-format-standard custom-colors layout-2c-l" dir="ltr" itemscope="itemscope" itemtype="http://schema.org/WebPage">
<div id="container">
<div class="skip-link">
<a href="#content" class="screen-reader-text">Skip to content</a>
</div>
 
<div class="top-banner">
<div id="oio-banner-1" style="width:100%; max-width:1000px; margin:0 auto;">
<a rel="nofollow" target="_blank" href="http://www.lusakatimes.com/wp-content/plugins/oiopub-direct/modules/tracker/go.php?id=80" title="AUTOREC ENTERPRISE, LTD. JAPAN"><img src="http://www.lusakatimes.com/wp-content/plugins/oiopub-direct/uploads/SRpt9n_140716autorec_LusakaTimes.gif" width="1000" height="70" border="0" alt="AUTOREC ENTERPRISE, LTD. JAPAN" style="width:100%; height:auto;"/></a>
</div>
</div>
<nav id="menu-primary" class="menu" role="navigation" aria-label="Primary Menu" itemscope="itemscope" itemtype="http://schema.org/SiteNavigationElement">
<h3 id="menu-primary-title" class="menu-toggle">
<button class="screen-reader-text">Primary Menu</button>
</h3> 
<div class="wrap"><ul id="menu-primary-items" class="menu-items"><li id="menu-item-81733" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-81733"><a href="http://www.lusakatimes.com">Home</a></li>
<li id="menu-item-81738" class="menu-item menu-item-type-post_type menu-item-object-page current-post-parent menu-item-has-children menu-item-81738"><a href="http://www.lusakatimes.com/about/">About Us</a>
<ul class="sub-menu">
<li id="menu-item-81739" class="menu-item menu-item-type-post_type menu-item-object-page current-post-parent menu-item-81739"><a href="http://www.lusakatimes.com/about/">About Us</a></li>
<li id="menu-item-81737" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-81737"><a href="http://www.lusakatimes.com/contact/">Contact Us</a></li>
<li id="menu-item-81734" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-81734"><a href="http://www.lusakatimes.com/send-in-your-articlespictures/">Send Pictures</a></li>
<li id="menu-item-81735" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-81735"><a href="http://www.lusakatimes.com/advertise-with-us/">To Advertise</a></li>
<li id="menu-item-81736" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-81736"><a href="http://www.lusakatimes.com/comments-policy/">Comments Policy</a></li>
</ul>
</li>
<li id="menu-item-81740" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-has-children menu-item-81740"><a href="http://www.lusakatimes.com">News Categories</a>
<ul class="sub-menu">
<li id="menu-item-81742" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81742"><a href="http://www.lusakatimes.com/headlines/">Headlines</a></li>
<li id="menu-item-81741" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81741"><a href="http://www.lusakatimes.com/other-news/">General News</a></li>
<li id="menu-item-81743" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81743"><a href="http://www.lusakatimes.com/economy/">Economy</a></li>
<li id="menu-item-81744" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-81744"><a href="http://www.lusakatimes.com/politics/">Politics</a></li>
<li id="menu-item-81745" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81745"><a href="http://www.lusakatimes.com/ruralnews/">Rural News</a></li>
<li id="menu-item-81746" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81746"><a href="http://www.lusakatimes.com/health/">Health</a></li>
<li id="menu-item-81747" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81747"><a href="http://www.lusakatimes.com/lifestyle/">Lifestyle</a></li>
</ul>
</li>
<li id="menu-item-81748" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81748"><a href="http://www.lusakatimes.com/sports/">Sports</a></li>
<li id="menu-item-81749" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81749"><a href="http://www.lusakatimes.com/lifestyle/photo-gallery/">Photo Gallery</a></li>
<li id="menu-item-81750" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81750"><a href="http://www.lusakatimes.com/entertainment/">Entertainment</a></li>
<li id="menu-item-81759" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-81759"><a href="http://www.lusakatimes.com/zambiancolumn/">Columns</a></li>
<li id="menu-item-81758" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-81758"><a href="http://www.lusakatimes.com/archives/">Archives</a></li>
</ul><form role="search" method="get" class="search-form" action="http://www.lusakatimes.com/">
<label>
<span class="screen-reader-text">Search for:</span>
<input type="search" class="search-field" placeholder="Search &hellip;" value="" name="s" title="Search for:"/>
</label>
<input type="submit" class="search-submit" value="Search"/>
</form></div>
</nav> 
<div class="wrap">
<div class="header-banner">
<img src="http://www.lusakatimes.com/wp-content/themes/lusaskatimes/images/logo.png" title="lusakatimes.com" alt="www.lusakatimes.com"/>
<script type="text/javascript"><!--
                google_ad_client = "ca-pub-5698567159910228";
                /* 728x90, created 12/15/07 */
                google_ad_slot = "0967911373";
                google_ad_width = 728;
                google_ad_height = 90;
                //-->
            </script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
            </script>
</div>
</div>
<div class="wrap">
<header id="header" role="banner" itemscope="itemscope" itemtype="http://schema.org/WPHeader">
<div id="oio-banner-15" style="width:100%; max-width:729px; margin:0 auto;">
<a rel="nofollow" target="_blank" href="http://www.lusakatimes.com/wp-content/plugins/oiopub-direct/modules/tracker/go.php?id=76" title="Beforward Japan"><img src="http://www.lusakatimes.com/wp-content/plugins/oiopub-direct/uploads/ICKWQN_Lusaka Times_728x90_Quality.jpg" width="729" height="91" border="0" alt="Beforward Japan" style="width:100%; height:auto;"/></a>
</div>
<script type="text/javascript"><!--
                google_ad_client = "ca-pub-5698567159910228";
                /* 728x15, created 3/30/11 */
                google_ad_slot = "7184390668";
                google_ad_width = 728;
                google_ad_height = 15;
                //-->
            </script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
            </script>
</header>
 
<div id="main" class="main">
<nav class="breadcrumb-trail breadcrumbs" itemprop="breadcrumb"><span class="trail-begin"><a href="http://www.lusakatimes.com" title="LusakaTimes.com" rel="home">Home</a></span>
<span class="sep">></span> <a href="http://www.lusakatimes.com/2015/">2015</a>
<span class="sep">></span> <a href="http://www.lusakatimes.com/2015/01/">January</a>
<span class="sep">></span> <a href="http://www.lusakatimes.com/2015/01/05/">5</a>
<span class="sep">></span> <span class="trail-end">UPND intensifies campaign in Western province</span>
</nav>
<main id="content" class="content" role="main" itemprop="mainContentOfPage" itemscope itemtype="http://schema.org/Blog">
<article id="post-85736" class="entry post publish author-admin post-85736 format-standard category-politics" itemscope="itemscope" itemtype="http://schema.org/BlogPosting" itemprop="blogPost">
<header class="entry-header">
<h1 class="entry-title" itemprop="headline">UPND intensifies campaign in Western province</h1>
<div class="entry-byline">
 
<time class="entry-published updated" datetime="2015-01-05T14:09:29+00:00" title="Monday, January 5, 2015, 2:09 pm">Jan 5, 2015 2:09 pm </time>
<a href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comments" class="comments-link" itemprop="discussionURL" title="Comment on UPND intensifies campaign in Western province">9</a> 120 views <a href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/email/" title="Email This Post" rel="nofollow"><img class="WP-EmailIcon" src="http://www.lusakatimes.com/wp-content/plugins/wp-email/images/email.gif" alt="Email This Post" title="Email This Post" style="border: 0px;"/></a>&nbsp;<a href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/email/" title="Email This Post" rel="nofollow">Email This Post</a>
|<a href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/print/" title="Print This Post" rel="nofollow"><img class="WP-PrintIcon" src="http://www.lusakatimes.com/wp-content/plugins/wp-print/images/printer_famfamfam.gif" alt="Print This Post" title="Print This Post" style="border: 0px;"/></a>&nbsp;<a href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/print/" title="Print This Post" rel="nofollow">Print This Post</a>
</div> 
</header> 
<div class="entry-content" itemprop="articleBody">
<figure id="attachment_85688" class="wp-caption aligncenter" style="max-width: 650px"><a href="http://i1.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/Mongu-Crowds-1.jpg"><img class="size-full wp-image-85688" src="http://i1.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/Mongu-Crowds-1.jpg?resize=650%2C390" alt="UPND Mongu rally" data-recalc-dims="1"/></a><figcaption class="wp-caption-text">UPND Mongu rally</figcaption></figure>
<p>The United Party for National Development (UPND) has intensified its Presidential campaigns and its candidate, Hakainde Hichilema, is now in the Western Province for a series of rallies ahead of the elections slated for January 20, 2015.</p>
<p>Mr Hichilema arrived at Mongu Airport in Mongu district yesterday around 17:30 hours and proceeded to Mulambwa Basic School ground where he held a mammoth public rally.</p>
<p>Mr Hichilema promised the people of Western province to reduce the price of fertilizer for them to grow more maize resulting into reduced mealie meal prices once voted into power.</p>
<p>He also promised to improve the health, education, and livestock sectors among others and create decent and permanent jobs for the citizenry.</p>
<p>The UPND leader added that he would strike a balance when forming his cabinet rather than having it dominated by people from specific regions and thanked his entourage from various political parties for deciding to re-unite and campaign for him.</p>
<p>Mr Hichilema was accompanied by Alliance for Democracy and Development (ADD) President, Charles Milupi with his Luena Member of Parliament (MP), Getrude Imenda, Movement for Multi-party Democracy (MMD) MP for Nalikwanda, Geoffrey Lungwangwa, for Liuwa, Situmbeko Musokotwane, and Likando Mufalali, for Senanga.</p>
<p>Others were former MMD National Chairman and Mulobezi MP, Michael Mabenga, former Western province Minister and Mongu MMD MP, Joseph Mulyata, and former Communications and Transport Minister and MMD Senanga MP, William Harringtone.</p>
<p>At the same rally Kenneth Namutulo, who was Patriotic Front Provincial Chairman and his Vice Treasurer, Sitali Simushi, defected from the ruling party, the PF, to the UPND.</p>
<p>Meanwhile, activities in Mongu Town came to a standstill yesterday afternoon as thousands of UPND supporters flocked to Mulambwa Primary School ground for UPND President Hakainde Hichilema’s rally that took place late in the evening.</p>
<figure id="attachment_85687" class="wp-caption aligncenter" style="max-width: 650px"><a href="http://i1.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/Mongu-Crowd.jpg"><img class="size-full wp-image-85687" src="http://i1.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/Mongu-Crowd.jpg?resize=650%2C390" alt="UPND Mongu rally" data-recalc-dims="1"/></a><figcaption class="wp-caption-text">UPND Mongu rally</figcaption></figure>
<figure id="attachment_85686" class="wp-caption aligncenter" style="max-width: 650px"><a href="http://i1.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/HH-William-Harrington.jpg"><img class="size-full wp-image-85686" src="http://i1.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/HH-William-Harrington.jpg?resize=650%2C390" alt="UPND leader Hakainde Hichilema talks to William Harrington" data-recalc-dims="1"/></a><figcaption class="wp-caption-text">UPND leader Hakainde Hichilema talks to William Harrington</figcaption></figure>
<figure id="attachment_85685" class="wp-caption aligncenter" style="max-width: 650px"><a href="http://i0.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/HH-Mongu.jpg"><img class="size-full wp-image-85685" src="http://i0.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/HH-Mongu.jpg?resize=650%2C390" alt="UPND Mongu rally" data-recalc-dims="1"/></a><figcaption class="wp-caption-text">UPND Mongu rally</figcaption></figure>
<figure id="attachment_85684" class="wp-caption aligncenter" style="max-width: 650px"><a href="http://i0.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/HH-Induna-Inete.jpg"><img class="size-full wp-image-85684" src="http://i0.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/HH-Induna-Inete.jpg?resize=650%2C390" alt="UPND leader Hakainde Hichilema with Induna Inete" data-recalc-dims="1"/></a><figcaption class="wp-caption-text">UPND leader Hakainde Hichilema with Induna Inete</figcaption></figure>
<figure id="attachment_85683" class="wp-caption aligncenter" style="max-width: 650px"><a href="http://i2.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/HH-1.jpg"><img class="size-full wp-image-85683" src="http://i2.wp.com/www.lusakatimes.com/wp-content/uploads/2015/01/HH-1.jpg?resize=650%2C390" alt="UPND leader Hakainde Hichilema during the Mongu rally" data-recalc-dims="1"/></a><figcaption class="wp-caption-text">UPND leader Hakainde Hichilema during the Mongu rally</figcaption></figure>
<div class='yarpp-related'>
<p>Related News:<ol>
<li><a href="http://www.lusakatimes.com/2011/02/15/upnd-intensifies-campaigns-hh/" rel="bookmark" title="UPND intensifies campaigns for HH">UPND intensifies campaigns for HH </a></li>
<li><a href="http://www.lusakatimes.com/2014/12/18/upnd-sending-false-information-media-northern-province-rallies-sikazwe/" rel="bookmark" title="UPND sending false information to the media about their Northern province rallies-Sikazwe">UPND sending false information to the media about their Northern province rallies-Sikazwe </a></li>
<li><a href="http://www.lusakatimes.com/2012/08/13/upnd-leader-hakainde-hichilema-arrested/" rel="bookmark" title="UPND leader Hakainde Hichilema has been arrested">UPND leader Hakainde Hichilema has been arrested </a></li>
<li><a href="http://www.lusakatimes.com/2014/02/12/zaf-helicopters-hover-upnd-leader-hakainde-hichilemas-ranch/" rel="bookmark" title="ZAF helicopters hover over UPND leader Hakainde Hichilema&#8217;s ranch">ZAF helicopters hover over UPND leader Hakainde Hichilema&#8217;s ranch </a></li>
<li><a href="http://www.lusakatimes.com/2014/12/14/hh-conduct-campaign-defining-rally-kasama-upnd/" rel="bookmark" title="HH to conduct a campaign-defining rally in Kasama-UPND">HH to conduct a campaign-defining rally in Kasama-UPND </a></li>
<li><a href="http://www.lusakatimes.com/2014/12/23/upnd-campaign-pictures/" rel="bookmark" title="UPND Campaign in Pictures">UPND Campaign in Pictures </a></li>
<li><a href="http://www.lusakatimes.com/2011/03/25/southern-province-shifts-support-upnd-mmd/" rel="bookmark" title="Southern province shifts support from UPND to MMD">Southern province shifts support from UPND to MMD </a></li>
</ol></p>
</div>
<div id="taboola-below-article-thumbnails"></div>
<script type="text/javascript">
  window._taboola = window._taboola || [];
  _taboola.push({
    mode: 'thumbnails-a',
    container: 'taboola-below-article-thumbnails',
    placement: 'Below Article Thumbnails',
    target_type: 'mix'
  });
</script>
</div> 
<footer class="entry-footer">
<span class="entry-terms category" itemprop="articleSection">Posted in <a href="http://www.lusakatimes.com/politics/" rel="tag">Politics</a></span> </footer> 
</article> 
<section id="comments-template">
<div id="comments">
<h3 id="comments-number">9 Comments</h3>
<ol class="comment-list">
<li id="comment-1801286" class="comment even thread-even depth-1 has-avatar" itemprop="comment" itemscope="itemscope" itemtype="http://schema.org/UserComments">
<article>
<header class="commentor-header">
<img alt='' src='http://0.gravatar.com/avatar/477fb132203e635371d4b69536cce48f?s=96&amp;d=&amp;r=G' class='avatar avatar-96 photo' height='96' width='96' itemprop="image"/> <span style="font-size:25px"> 1 <img alt="flag" src="/wp-content/themes/options/images/flag_us.gif"> <cite class="comment-author" itemprop="creator" itemscope="itemscope" itemtype="http://schema.org/Person">ine wine</cite><br/> </span>
<time class="comment-published" datetime="2015-01-05T14:36:26+00:00" title="Monday, January 5, 2015, 2:36 pm" itemprop="commentTime">45 mins ago</time>
<a class="comment-permalink" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comment-1801286" itemprop="url">Permalink</a>
</header> 
<div class="centered">
<div class="leftblock">
<div class="commentsblock">
<p>The only thing PF has done in WP for the last three years is 12km of Mongu township roads and declaring 9 districts without infrastructure. Whilst I support creation of districts, I don&#8217;t think the manner they were done is health.</p>
<a itemprop="replyToUrl"class='comment-reply-link' href='/2015/01/05/upnd-intensifies-campaign-western-province/?replytocom=1801286#respond' onclick='return addComment.moveForm( "comment-1801286", "1801286", "respond", "85736" )' aria-label='Reply to ine wine'>Reply</a>                </div>
                <div class="votes">            <div class="updown-vote-box updown-comments" id="updown-comment-1801286" comment-id="1801286"><div><img class="updown-button updown-up-button" vote-direction="1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-up.png"></div><div class="updown-up-count updown-active">+4</div><div class="updown-down-count updown-active">-1</div><div><img class="updown-button updown-down-button" vote-direction="-1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-down.png"></div><div class="updown-label">vote</div></div></div>
            </div>
            <div class="clear"></div>
        </div>






	</article>



<ol class="children">
<li id="comment-1801292" class="comment odd alt depth-2 has-avatar" itemprop="comment" itemscope="itemscope" itemtype="http://schema.org/UserComments">

	<article>
		<header class="commentor-header">

			<img alt='' src='http://1.gravatar.com/avatar/b06cb00c043ffce74d3da4c0cb42c249?s=96&amp;d=&amp;r=G' class='avatar avatar-96 photo' height='96' width='96' itemprop="image" />            <span style="font-size:25px"> 1.1             <img alt="flag" src="/wp-content/themes/options/images/flag_gb.gif"> 			<cite class="comment-author" itemprop="creator" itemscope="itemscope" itemtype="http://schema.org/Person">Gen</cite><br /> </span>

			<time class="comment-published" datetime="2015-01-05T14:45:54+00:00" title="Monday, January 5, 2015, 2:45 pm" itemprop="commentTime">35 mins ago</time>
			<a class="comment-permalink" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comment-1801292" itemprop="url">Permalink</a>
			

		</header><!-- .comment-meta -->

        <div class="centered">
            <div class="leftblock">
                <div class="commentsblock" >
                    <p>Edgar is he man the Zambian people deserve for continued peace, stability and prosperity.</p>
<p>January 20, 2015, vote Edgar C. Lungu</p>
<p>The other one Halelusa Hagain</p>

                                    </div>
                <div class="votes">            <div class="updown-vote-box updown-comments" id="updown-comment-1801292" comment-id="1801292"><div><img class="updown-button updown-up-button" vote-direction="1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-up.png"></div><div class="updown-up-count">0</div><div class="updown-down-count updown-active">-5</div><div><img class="updown-button updown-down-button" vote-direction="-1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-down.png"></div><div class="updown-label">vote</div></div></div>
            </div>
            <div class="clear"></div>
        </div>






	</article>



</li><!-- .comment --><li id="comment-1801304" class="comment even depth-2 has-avatar" itemprop="comment" itemscope="itemscope" itemtype="http://schema.org/UserComments">

	<article>
		<header class="commentor-header">

			<img alt='' src='http://1.gravatar.com/avatar/5aff5492428679a8174ae2801fc4f718?s=96&amp;d=&amp;r=G' class='avatar avatar-96 photo' height='96' width='96' itemprop="image" />            <span style="font-size:25px"> 1.2             <img alt="flag" src="/wp-content/themes/options/images/flag_gb.gif"> 			<cite class="comment-author" itemprop="creator" itemscope="itemscope" itemtype="http://schema.org/Person">Wanzelu</cite><br /> </span>

			<time class="comment-published" datetime="2015-01-05T15:03:16+00:00" title="Monday, January 5, 2015, 3:03 pm" itemprop="commentTime">18 mins ago</time>
			<a class="comment-permalink" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comment-1801304" itemprop="url">Permalink</a>
			

		</header><!-- .comment-meta -->

        <div class="centered">
            <div class="leftblock">
                <div class="commentsblock" >
                    <p>Ba LT you are late again why? This is from the archives of other papers.   Next please.</p>
<p>Flight HH is now smaller towns in Western province.</p>

                                    </div>
                <div class="votes">            <div class="updown-vote-box updown-comments" id="updown-comment-1801304" comment-id="1801304"><div><img class="updown-button updown-up-button" vote-direction="1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-up.png"></div><div class="updown-up-count"></div><div class="updown-down-count"></div><div><img class="updown-button updown-down-button" vote-direction="-1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-down.png"></div><div class="updown-label">vote</div></div></div>
            </div>
            <div class="clear"></div>
        </div>






	</article>



</li><!-- .comment --><li id="comment-1801319" class="comment odd alt depth-2 has-avatar" itemprop="comment" itemscope="itemscope" itemtype="http://schema.org/UserComments">

	<article>
		<header class="commentor-header">

			<img alt='' src='http://1.gravatar.com/avatar/367fb8590ff0b95c83ea550067ab2228?s=96&amp;d=&amp;r=G' class='avatar avatar-96 photo' height='96' width='96' itemprop="image" />            <span style="font-size:25px"> 1.3             <img alt="flag" src="/wp-content/themes/options/images/flag_us.gif"> 			<cite class="comment-author" itemprop="creator" itemscope="itemscope" itemtype="http://schema.org/Person">The Bricklayer</cite><br /> </span>

			<time class="comment-published" datetime="2015-01-05T15:19:57+00:00" title="Monday, January 5, 2015, 3:19 pm" itemprop="commentTime">1 min ago</time>
			<a class="comment-permalink" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comment-1801319" itemprop="url">Permalink</a>
			

		</header><!-- .comment-meta -->

        <div class="centered">
            <div class="leftblock">
                <div class="commentsblock" >
                    <p>The Mungu Rally was mammoth and these pictures cannot do it justice. The Podium was in the center and the people surrounded it in all directions as far as the eye could see. But I think we need to spend these last two weeks in Lusaka and on the Copperbelt. I think we can take the copperbelt. Chingola is already in the books, so is Luanshya, Ndola and Kitwe are very close and so is Mufulira and Kalulushi. CB is a very important voting block and if take it or loose by a close margin, then it is over, no matter what happens in Eastern and Northern. Lets Go HH, let us retire the Panga Family and Judge Ngoma, Bowman Lunsambo and Skopion Kadobi.</p>

                                    </div>
                <div class="votes">            <div class="updown-vote-box updown-comments" id="updown-comment-1801319" comment-id="1801319"><div><img class="updown-button updown-up-button" vote-direction="1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-up.png"></div><div class="updown-up-count"></div><div class="updown-down-count"></div><div><img class="updown-button updown-down-button" vote-direction="-1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-down.png"></div><div class="updown-label">vote</div></div></div>
            </div>
            <div class="clear"></div>
        </div>






	</article>



</li><!-- .comment --></ol><!-- .children -->
</li><!-- .comment --><li id="comment-1801289" class="comment even thread-odd thread-alt depth-1 has-avatar" itemprop="comment" itemscope="itemscope" itemtype="http://schema.org/UserComments">

	<article>
		<header class="commentor-header">

			<img alt='' src='http://0.gravatar.com/avatar/806a94561c8dc23956fa5150e8633d86?s=96&amp;d=&amp;r=G' class='avatar avatar-96 photo' height='96' width='96' itemprop="image" />            <span style="font-size:25px"> 2             <img alt="flag" src="/wp-content/themes/options/images/flag_mu.gif"> 			<cite class="comment-author" itemprop="creator" itemscope="itemscope" itemtype="http://schema.org/Person">Mwaba-Jr</cite><br /> </span>

			<time class="comment-published" datetime="2015-01-05T14:38:07+00:00" title="Monday, January 5, 2015, 2:38 pm" itemprop="commentTime">43 mins ago</time>
			<a class="comment-permalink" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comment-1801289" itemprop="url">Permalink</a>
			

		</header><!-- .comment-meta -->

        <div class="centered">
            <div class="leftblock">
                <div class="commentsblock" >
                    <p>HH is the man!  our incoming president.</p>

                    <a itemprop="replyToUrl"class='comment-reply-link' href='/2015/01/05/upnd-intensifies-campaign-western-province/?replytocom=1801289#respond' onclick='return addComment.moveForm( "comment-1801289", "1801289", "respond", "85736" )' aria-label='Reply to Mwaba-Jr'>Reply</a>                </div>
                <div class="votes">            <div class="updown-vote-box updown-comments" id="updown-comment-1801289" comment-id="1801289"><div><img class="updown-button updown-up-button" vote-direction="1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-up.png"></div><div class="updown-up-count updown-active">+5</div><div class="updown-down-count updown-active">-1</div><div><img class="updown-button updown-down-button" vote-direction="-1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-down.png"></div><div class="updown-label">vote</div></div></div>
            </div>
            <div class="clear"></div>
        </div>






	</article>



</li><!-- .comment --><li id="comment-1801297" class="comment odd alt thread-even depth-1 has-avatar" itemprop="comment" itemscope="itemscope" itemtype="http://schema.org/UserComments">

	<article>
		<header class="commentor-header">

			<img alt='' src='http://0.gravatar.com/avatar/8ea0c43ef19cfdabb6a829303778fb6e?s=96&amp;d=&amp;r=G' class='avatar avatar-96 photo' height='96' width='96' itemprop="image" />            <span style="font-size:25px"> 3             <img alt="flag" src="/wp-content/themes/options/images/flag_us.gif"> 			<cite class="comment-author" itemprop="creator" itemscope="itemscope" itemtype="http://schema.org/Person">Insp</cite><br /> </span>

			<time class="comment-published" datetime="2015-01-05T14:50:44+00:00" title="Monday, January 5, 2015, 2:50 pm" itemprop="commentTime">30 mins ago</time>
			<a class="comment-permalink" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comment-1801297" itemprop="url">Permalink</a>
			

		</header><!-- .comment-meta -->

        <div class="centered">
            <div class="leftblock">
                <div class="commentsblock" >
                    <p>HH just ,,Zambia 4x4ward.</p>

                    <a itemprop="replyToUrl"class='comment-reply-link' href='/2015/01/05/upnd-intensifies-campaign-western-province/?replytocom=1801297#respond' onclick='return addComment.moveForm( "comment-1801297", "1801297", "respond", "85736" )' aria-label='Reply to Insp'>Reply</a>                </div>
                <div class="votes">            <div class="updown-vote-box updown-comments" id="updown-comment-1801297" comment-id="1801297"><div><img class="updown-button updown-up-button" vote-direction="1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-up.png"></div><div class="updown-up-count updown-active">+3</div><div class="updown-down-count">0</div><div><img class="updown-button updown-down-button" vote-direction="-1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-down.png"></div><div class="updown-label">vote</div></div></div>
            </div>
            <div class="clear"></div>
        </div>






	</article>



</li><!-- .comment --><li id="comment-1801311" class="comment even thread-odd thread-alt depth-1 has-avatar" itemprop="comment" itemscope="itemscope" itemtype="http://schema.org/UserComments">

	<article>
		<header class="commentor-header">

			<img alt='' src='http://1.gravatar.com/avatar/b6fef04108438e51f22d55810d952229?s=96&amp;d=&amp;r=G' class='avatar avatar-96 photo' height='96' width='96' itemprop="image" />            <span style="font-size:25px"> 4             <img alt="flag" src="/wp-content/themes/options/images/flag_za.gif"> 			<cite class="comment-author" itemprop="creator" itemscope="itemscope" itemtype="http://schema.org/Person">What a life!!</cite><br /> </span>

			<time class="comment-published" datetime="2015-01-05T15:08:59+00:00" title="Monday, January 5, 2015, 3:08 pm" itemprop="commentTime">12 mins ago</time>
			<a class="comment-permalink" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comment-1801311" itemprop="url">Permalink</a>
			

		</header><!-- .comment-meta -->

        <div class="centered">
            <div class="leftblock">
                <div class="commentsblock" >
                    <p>I cant wait to hear the results of the elections.HH should not be confident that he is going to win because of the number of people that attend his rallies in UPND strong holds because it is normal and it is expected that any political party that holds a rally in their strong hold a lot of people will attend the rally.The numbers at the rally do not translate into the number of votes. Some people go to rallies for curiosity purposes and it is unfortunate that UPND supporters think that the number of people at rallies is an expression of support for HH.By the way how is HH going to solve the outstanding Barotseland agreement problem?What is HH&#8217;s possition on this issue</p>

                    <a itemprop="replyToUrl"class='comment-reply-link' href='/2015/01/05/upnd-intensifies-campaign-western-province/?replytocom=1801311#respond' onclick='return addComment.moveForm( "comment-1801311", "1801311", "respond", "85736" )' aria-label='Reply to What a life!!'>Reply</a>                </div>
                <div class="votes">            <div class="updown-vote-box updown-comments" id="updown-comment-1801311" comment-id="1801311"><div><img class="updown-button updown-up-button" vote-direction="1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-up.png"></div><div class="updown-up-count">0</div><div class="updown-down-count updown-active">-1</div><div><img class="updown-button updown-down-button" vote-direction="-1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-down.png"></div><div class="updown-label">vote</div></div></div>
            </div>
            <div class="clear"></div>
        </div>






	</article>



<ol class="children">
<li id="comment-1801320" class="comment odd alt depth-2 has-avatar" itemprop="comment" itemscope="itemscope" itemtype="http://schema.org/UserComments">

	<article>
		<header class="commentor-header">

			<img alt='' src='http://1.gravatar.com/avatar/d5bff20135efbffe9721ec91040bbf51?s=96&amp;d=&amp;r=G' class='avatar avatar-96 photo' height='96' width='96' itemprop="image" />            <span style="font-size:25px"> 4.1             <img alt="flag" src="/wp-content/themes/options/images/flag_zm.gif"> 			<cite class="comment-author" itemprop="creator" itemscope="itemscope" itemtype="http://schema.org/Person">DIVA</cite><br /> </span>

			<time class="comment-published" datetime="2015-01-05T15:20:39+00:00" title="Monday, January 5, 2015, 3:20 pm" itemprop="commentTime">1 min ago</time>
			<a class="comment-permalink" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comment-1801320" itemprop="url">Permalink</a>
			

		</header><!-- .comment-meta -->

        <div class="centered">
            <div class="leftblock">
                <div class="commentsblock" >
                    <p>He has no clue my brother.</p>

                                    </div>
                <div class="votes">            <div class="updown-vote-box updown-comments" id="updown-comment-1801320" comment-id="1801320"><div><img class="updown-button updown-up-button" vote-direction="1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-up.png"></div><div class="updown-up-count"></div><div class="updown-down-count"></div><div><img class="updown-button updown-down-button" vote-direction="-1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-down.png"></div><div class="updown-label">vote</div></div></div>
            </div>
            <div class="clear"></div>
        </div>






	</article>



</li><!-- .comment --></ol><!-- .children -->
</li><!-- .comment --><li id="comment-1801318" class="comment even thread-even depth-1 has-avatar" itemprop="comment" itemscope="itemscope" itemtype="http://schema.org/UserComments">

	<article>
		<header class="commentor-header">

			<img alt='' src='http://1.gravatar.com/avatar/d5bff20135efbffe9721ec91040bbf51?s=96&amp;d=&amp;r=G' class='avatar avatar-96 photo' height='96' width='96' itemprop="image" />            <span style="font-size:25px"> 5             <img alt="flag" src="/wp-content/themes/options/images/flag_zm.gif"> 			<cite class="comment-author" itemprop="creator" itemscope="itemscope" itemtype="http://schema.org/Person">salaula</cite><br /> </span>

			<time class="comment-published" datetime="2015-01-05T15:19:34+00:00" title="Monday, January 5, 2015, 3:19 pm" itemprop="commentTime">1 min ago</time>
			<a class="comment-permalink" href="http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/#comment-1801318" itemprop="url">Permalink</a>
			

		</header><!-- .comment-meta -->

        <div class="centered">
            <div class="leftblock">
                <div class="commentsblock" >
                    <p>HH ayonda nicani, kapena adwala? Please a Dr Caniscious Banda tiozeni ngati niconco kaili ndimwe mule nama documents ya health on presidential candidates.</p>

                    <a itemprop="replyToUrl"class='comment-reply-link' href='/2015/01/05/upnd-intensifies-campaign-western-province/?replytocom=1801318#respond' onclick='return addComment.moveForm( "comment-1801318", "1801318", "respond", "85736" )' aria-label='Reply to salaula'>Reply</a>                </div>
                <div class="votes">            <div class="updown-vote-box updown-comments" id="updown-comment-1801318" comment-id="1801318"><div><img class="updown-button updown-up-button" vote-direction="1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-up.png"></div><div class="updown-up-count"></div><div class="updown-down-count"></div><div><img class="updown-button updown-down-button" vote-direction="-1" src="http://www.lusakatimes.com/wp-content/plugins/updownupdown-postcomment-voting/images/arrow-down.png"></div><div class="updown-label">vote</div></div></div>
            </div>
            <div class="clear"></div>
        </div>






	</article>



</li><!-- .comment -->			</ol><!-- .comment-list -->

			
		</div><!-- #comments-->

	
	
									<div id="respond" class="comment-respond">
				<h3 id="reply-title" class="comment-reply-title">Leave a Reply <small><a rel="nofollow" id="cancel-comment-reply-link" href="/2015/01/05/upnd-intensifies-campaign-western-province/#respond" style="display:none;">Cancel reply</a></small></h3>
									<form action="http://www.lusakatimes.com/wp-comments-post.php" method="post" id="commentform" class="comment-form" novalidate>
																			<p class="comment-notes"><span id="email-notes">Your email address will not be published.</span> Required fields are marked <span class="required">*</span></p>							<p class="comment-form-author"><label for="author">Name <span class="required">*</span></label> <input id="author" name="author" type="text" value="" size="30" aria-required='true' /></p>
<p class="comment-form-email"><label for="email">Email <span class="required">*</span></label> <input id="email" name="email" type="email" value="" size="30" aria-describedby="email-notes" aria-required='true' /></p>

												<p class="comment-form-comment"><label for="comment">Comment</label> <textarea  onkeydown="gcllCounter(this)" onkeyup="gcllCounter(this)"  id="comment" name="comment" cols="45" rows="8" aria-describedby="form-allowed-tags" aria-required="true"></textarea></p><span class="countdownbox">
<input readonly="readonly" type="text" id="commentlen" size="3" maxlength="3" value="800" style="width:auto;text-indent:0;" />
&nbsp;characters available
</span>						<p class="form-allowed-tags" id="form-allowed-tags">You may use these <abbr title="HyperText Markup Language">HTML</abbr> tags and attributes:  <code>&lt;a href=&quot;&quot; title=&quot;&quot;&gt; &lt;abbr title=&quot;&quot;&gt; &lt;acronym title=&quot;&quot;&gt; &lt;b&gt; &lt;blockquote cite=&quot;&quot;&gt; &lt;cite&gt; &lt;code&gt; &lt;del datetime=&quot;&quot;&gt; &lt;em&gt; &lt;i&gt; &lt;q cite=&quot;&quot;&gt; &lt;strike&gt; &lt;strong&gt; </code></p>						<p class="form-submit">
							<input name="submit" type="submit" id="submit" class="submit" value="Post Comment" />
							<input type='hidden' name='comment_post_ID' value='85736' id='comment_post_ID' />
<input type='hidden' name='comment_parent' id='comment_parent' value='0' />
						</p>
						<p style="display: none;"><input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="640f8dbe33" /></p>
<script type='text/javascript'>
// <![CDATA[
ref2xJS=escape(document['referrer']);
hf1N='3ae56a28c294999059300efb6b89ea1a';
hf1V='aad18b4794fd8ab17ec68350f43e3e49';
document.write("<input type='hidden' name='ref2xJS' value='"+ref2xJS+"'><input type='hidden' name='"+hf1N+"' value='"+hf1V+"'>");
// ]]>
</script><noscript><input type="hidden" name="JSONST" value="NS1"></noscript>
<noscript><p><strong>Currently you have JavaScript disabled. In order to post comments, please make sure JavaScript and Cookies are enabled, and reload the page.</strong> <a href="http://enable-javascript.com/" rel="nofollow external" >Click here for instructions on how to enable JavaScript in your browser.</a></p></noscript>
<p class="comment-subscription-form"><input type="checkbox" name="subscribe_comments" id="subscribe_comments" value="subscribe" style="width: auto; -moz-appearance: checkbox; -webkit-appearance: checkbox;" /> <label class="subscribe-label" id="subscribe-label" for="subscribe_comments">Notify me of follow-up comments by email.</label></p><p class="comment-subscription-form"><input type="checkbox" name="subscribe_blog" id="subscribe_blog" value="subscribe" style="width: auto; -moz-appearance: checkbox; -webkit-appearance: checkbox;" /> <label class="subscribe-label" id="subscribe-blog-label" for="subscribe_blog">Notify me of new posts by email.</label></p><p style="display: none;"><input type="hidden" id="ak_js" name="ak_js" value="150"/></p>					</form>
							</div><!-- #respond -->
			
</section><!-- #comments-template -->
			
		
		
	<div class="loop-nav">
		<div class="prev">Previous Post: <a href="http://www.lusakatimes.com/2015/01/05/nkandu-luo-pf-government-destroyed-bembaland-bashilubemba/" rel="prev">Nkandu Luo and her PF government destroyed bembaland &#8211; Bashilubemba</a></div>			</div><!-- .loop-nav -->


	
</main><!-- #content -->

				
	<aside id="sidebar-primary" class="sidebar" role="complementary" aria-label="Primary Sidebar" itemscope="itemscope" itemtype="http://schema.org/WPSideBar">

		<h3 id="sidebar-primary-title" class="screen-reader-text">Primary Sidebar</h3>

		
			<section id="text-465810719" class="widget widget_text">			<div class="textwidget"><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 336x280, created 12/5/08 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:336px;height:280px"
     data-ad-client="ca-pub-5698567159910228"
     data-ad-slot="2604067005"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
		</section><section id="text-465810726" class="widget widget_text">			<div class="textwidget"><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 160x600, created 6/10/10 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:160px;height:600px"
     data-ad-client="ca-pub-5698567159910228"
     data-ad-slot="7598468158"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
		</section><section id="text-465810721" class="widget widget_text">			<div class="textwidget"><script id="mNCC" language="javascript">  medianet_width='300';  medianet_height= '600';  medianet_crid='373405668';  </script>  <script id="mNSC" src="http://contextual.media.net/nmedianet.js?cid=8CU67CVLK" language="javascript"></script> </div>
		</section><section id="text-465810725" class="widget widget_text">			<div class="textwidget"><script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/oiopub-direct/js.php?type=banner&align=center&zone=8'></script></div>
		</section><section id="text-465810722" class="widget widget_text">			<div class="textwidget"><script type="text/javascript" src="http://ap.lijit.com///www/delivery/fpi.js?z=244171&u=LusakaTimes&width=300&height=600"></script></div>
		</section><section id="text-465810724" class="widget widget_text">			<div class="textwidget"></div>
		</section><section id="text-465810720" class="widget widget_text">			<div class="textwidget"><iframe src="//www.facebook.com/plugins/likebox.php?href=http%3A%2F%2Fwww.facebook.com%2Flusakatimes&amp;width=300&amp;height=650&amp;show_faces=true&amp;colorscheme=light&amp;stream=false&amp;border_color&amp;header=true&amp;appId=204116279606603" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:300px; height:650px;" allowTransparency="true"></iframe></div>
		</section>
		
	</aside><!-- #sidebar-primary -->


			</div><!-- #main -->

			
		</div><!-- .wrap -->

		<footer id="footer" role="contentinfo" itemscope="itemscope" itemtype="http://schema.org/WPFooter">

			<div class="wrap">

				
				<p class="credit">
					Copyright &#169; 2015 <a class="site-link" href="http://www.lusakatimes.com" rel="home">LusakaTimes.com</a>. Powered by <a class="wp-link" href="http://wordpress.org" title="State-of-the-art semantic personal publishing platform">WordPress</a>
				</p><!-- .credit -->

			</div><!-- .wrap -->

		</footer><!-- #footer -->

	</div><!-- #container -->


<script type="text/javascript">
   var infolink_pid = 56876;
   var infolink_wsid = 0;
</script>
<script type="text/javascript" src="http://resources.infolinks.com/js/infolinks_main.js"></script>



<script type="text/javascript">

var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");

document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));

</script>

<script type="text/javascript">

try {

var pageTracker = _gat._getTracker("UA-4363037-1");

pageTracker._trackPageview();

} catch(err) {}</script>


<script type="text/javascript" id="wau_scr_02b07926">
    var wau_p = wau_p || []; wau_p.push(["ldnw", "02b07926", false]);
    (function() {
        var s=document.createElement("script"); s.type="text/javascript";
        s.async=true; s.src="http://widgets.amung.us/a_pro.js";
        document.getElementsByTagName("head")[0].appendChild(s);
    })();
</script>

	<img id="oio-pixel" src="http://www.lusakatimes.com/wp-content/plugins/oiopub-direct/modules/tracker/tracker.php?pids=80|76|0" alt="" />
		<!-- Ajax_the_views disabled: Cache not detected -->
		<style type="text/css"></style><!-- Start Of Script Generated By Greg's Comment Length Limiter Plugin 1.6.2 -->
<script type="text/javascript">
<!--
function gcllCounter(textarea) {
if (textarea.value.length > 800)
textarea.value = textarea.value.substring(0, 800);
else
document.getElementById('commentlen').value = 800 - textarea.value.length;
}
//-->
</script>
<!-- End of Script Generated By Greg's Comment Length Limiter Plugin 1.6.2 -->	<div style="display:none">
	<div class="grofile-hash-map-477fb132203e635371d4b69536cce48f">
	</div>
	<div class="grofile-hash-map-b06cb00c043ffce74d3da4c0cb42c249">
	</div>
	<div class="grofile-hash-map-5aff5492428679a8174ae2801fc4f718">
	</div>
	<div class="grofile-hash-map-367fb8590ff0b95c83ea550067ab2228">
	</div>
	<div class="grofile-hash-map-806a94561c8dc23956fa5150e8633d86">
	</div>
	<div class="grofile-hash-map-8ea0c43ef19cfdabb6a829303778fb6e">
	</div>
	<div class="grofile-hash-map-b6fef04108438e51f22d55810d952229">
	</div>
	<div class="grofile-hash-map-d5bff20135efbffe9721ec91040bbf51">
	</div>
	</div>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/akismet/_inc/form.js?ver=3.0.4'></script>
<link rel='stylesheet' id='yarppRelatedCss-css'  href='http://www.lusakatimes.com/wp-content/plugins/yet-another-related-posts-plugin/style/related.css?ver=4.1' type='text/css' media='all' />
<script type='text/javascript' src='http://www.lusakatimes.com/wp-includes/js/comment-reply.min.js?ver=4.1'></script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/jetpack/modules/photon/photon.js?ver=20130122'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var emailL10n = {"ajax_url":"http:\/\/www.lusakatimes.com\/wp-admin\/admin-ajax.php","max_allowed":"5","text_error":"The Following Error Occurs:","text_name_invalid":"- Your Name is empty\/invalid","text_email_invalid":"- Your Email is empty\/invalid","text_remarks_invalid":"- Your Remarks is invalid","text_friend_names_empty":"- Friend Name(s) is empty","text_friend_name_invalid":"- Friend Name is empty\/invalid: ","text_max_friend_names_allowed":"- Maximum 5 Friend Names allowed","text_friend_emails_empty":"- Friend Email(s) is empty","text_friend_email_invalid":"- Friend Email is invalid: ","text_max_friend_emails_allowed":"- Maximum 5 Friend Emails allowed","text_friends_tally":"- Friend Name(s) count does not tally with Friend Email(s) count","text_image_verify_empty":"- Image Verification is empty"};
/* ]]> */
</script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/wp-email/email-js.js?ver=2.63'></script>
<script type='text/javascript' src='http://s0.wp.com/wp-content/js/devicepx-jetpack.js?ver=201502'></script>
<script type='text/javascript' src='http://s.gravatar.com/js/gprofiles.js?ver=2015Janaa'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var WPGroHo = {"my_hash":""};
/* ]]> */
</script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/plugins/jetpack/modules/wpgroho.js?ver=4.1'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var stargazer_i18n = {"search_toggle":"Expand Search Form"};
/* ]]> */
</script>
<script type='text/javascript' src='http://www.lusakatimes.com/wp-content/themes/lusaskatimes/js/stargazer.min.js'></script>
<script type="text/javascript">
/* <![CDATA[ */
jQuery(document).ready( function($) {
	$("ul.menu").not(":has(li)").closest('div').prev('h3.widget-title').hide();
});
/* ]]> */
</script>
	<script src="http://stats.wp.com/e-201502.js" type="text/javascript"></script>
	<script type="text/javascript">
	st_go({v:'ext',j:'1:3.3',blog:'4702004',post:'85736',tz:'2'});
	var load_cmc = function(){linktracker_init(4702004,85736,2);};
	if ( typeof addLoadEvent != 'undefined' ) addLoadEvent(load_cmc);
	else load_cmc();
	</script><!-- Generated in 1.610 seconds. Made 65 queries to database and 68 cached queries. Memory used - 8.92MB -->
<!-- Cached by DB Cache Reloaded Fix -->
<script type="text/javascript">
  window._taboola = window._taboola || [];
  _taboola.push({flush: true});
</script>

</body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.lusakatimes.com/2015/01/05/upnd-intensifies-campaign-western-province/'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, 'UPND intensifies campaign in Western province')
        self.assertIsNone(doc.summary)
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '05 01 2015')
        self.assertEqual(doc.author, Author.unknown())
        self.assertEqual(doc.medium.name, 'Lusaka Times')

        self.assertEqual(doc.text, u'The United Party for National Development (UPND) has intensified its Presidential campaigns and its candidate, Hakainde Hichilema, is now in the Western Province for a series of rallies ahead of the elections slated for January 20, 2015.\n\nMr Hichilema arrived at Mongu Airport in Mongu district yesterday around 17:30 hours and proceeded to Mulambwa Basic School ground where he held a mammoth public rally.\n\nMr Hichilema promised the people of Western province to reduce the price of fertilizer for them to grow more maize resulting into reduced mealie meal prices once voted into power.\n\nHe also promised to improve the health, education, and livestock sectors among others and create decent and permanent jobs for the citizenry.\n\nThe UPND leader added that he would strike a balance when forming his cabinet rather than having it dominated by people from specific regions and thanked his entourage from various political parties for deciding to re-unite and campaign for him.\n\nMr Hichilema was accompanied by Alliance for Democracy and Development (ADD) President, Charles Milupi with his Luena Member of Parliament (MP), Getrude Imenda, Movement for Multi-party Democracy (MMD) MP for Nalikwanda, Geoffrey Lungwangwa, for Liuwa, Situmbeko Musokotwane, and Likando Mufalali, for Senanga.\n\nOthers were former MMD National Chairman and Mulobezi MP, Michael Mabenga, former Western province Minister and Mongu MMD MP, Joseph Mulyata, and former Communications and Transport Minister and MMD Senanga MP, William Harringtone.\n\nAt the same rally Kenneth Namutulo, who was Patriotic Front Provincial Chairman and his Vice Treasurer, Sitali Simushi, defected from the ruling party, the PF, to the UPND.\n\nMeanwhile, activities in Mongu Town came to a standstill yesterday afternoon as thousands of UPND supporters flocked to Mulambwa Primary School ground for UPND President Hakainde Hichilema\u2019s rally that took place late in the evening.\n\nRelated News:')
        

class TestZambianWatchdogCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = ZambianWatchdogCrawler()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_extract(self):
        html = """

<!DOCTYPE html>
<!--[if IE 7]>
<html class="ie ie7" lang="en-US"
 xmlns:og="http://opengraphprotocol.org/schema/"
 xmlns:fb="http://www.facebook.com/2008/fbml">
<![endif]-->
<!--[if IE 8]>
<html class="ie ie8" lang="en-US"
 xmlns:og="http://opengraphprotocol.org/schema/"
 xmlns:fb="http://www.facebook.com/2008/fbml">
<![endif]-->
<!--[if !(IE 7) | !(IE 8) ]><!-->
<html lang="en-US" xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://www.facebook.com/2008/fbml">
<!--<![endif]-->
<head><link rel="dns-prefetch" href="//ajax.googleapis.com"><link rel="dns-prefetch" href="//adscaspion.appspot.com"><link rel="dns-prefetch" href="//www.facebook.com"><link rel="dns-prefetch" href="//connect.facebook.net"><link rel="dns-prefetch" href="//platform.twitter.com"><link rel="dns-prefetch" href="//apis.google.com"><link rel="dns-prefetch" href="//s0.wp.com"><link rel="dns-prefetch" href="//stats.wp.com"><link rel="stylesheet" href="http://www.zambianwatchdog.com/wp-content/plugins/adsight/articlead.css"/>
<script type="text/javascript">var links = document.getElementsByTagName('link');for (var i = 0; i < links.length; ++i) {  if (links[i].getAttribute('rel') == 'stylesheet') {    links[i].disabled=true;  }}</script><script type='text/javascript'>window.mod_pagespeed_prefetch_start = Number(new Date());window.mod_pagespeed_num_resources_prefetched = 1</script>




	<meta charset="UTF-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
	<title>UPND warns PF against attempts to rig polls &raquo; Zambian Watchdog</title>
	<script type='text/javascript'>window.mod_pagespeed_start = Number(new Date());</script><link rel="profile" href="http://gmpg.org/xfn/11">
	<link rel="pingback" href="http://www.zambianwatchdog.com/xmlrpc.php">
	<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="http://www.zambianwatchdog.com/feed/"/>	
	<link rel="pingback" href="http://www.zambianwatchdog.com/xmlrpc.php"/>	
	





	<link rel="alternate" type="application/rss+xml" title="Zambian Watchdog &raquo; Feed" href="http://www.zambianwatchdog.com/feed/"/>
<link rel="alternate" type="application/rss+xml" title="Zambian Watchdog &raquo; Comments Feed" href="http://www.zambianwatchdog.com/comments/feed/"/>
<link rel="alternate" type="application/rss+xml" title="Zambian Watchdog &raquo; UPND warns PF against attempts to rig polls Comments Feed" href="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/feed/"/>
<link rel='stylesheet' id='fb-like-responsive-css' href='http://www.zambianwatchdog.com/wp-content/plugins/facebook-like-box-responsive/facebook-like-responsive.css?ver=4.0.1' type='text/css' media='all'/>
<link rel='stylesheet' id='tfg_style-css' href='http://www.zambianwatchdog.com/wp-content/plugins/twitter-facebook-google-plusone-share/tfg_style.css?ver=4.0.1' type='text/css' media='all'/>
<link rel='stylesheet' id='wp-polls-css' href='http://www.zambianwatchdog.com/wp-content/plugins/wp-polls/polls-css.css?ver=2.67' type='text/css' media='all'/>
<link rel='stylesheet' id='wp-post-navigation-style-css' href='http://www.zambianwatchdog.com/wp-content/plugins/wp-post-navigation/style.css?ver=4.0.1' type='text/css' media='all'/>
<link rel='stylesheet' id='bootstrap-css' href='http://www.zambianwatchdog.com/wp-content/themes/sharp/framework/bootstrap/css/bootstrap.min.css?ver=4.0.1' type='text/css' media='all'/>
<link rel='stylesheet' id='font-awesome-css' href='http://www.zambianwatchdog.com/wp-content/themes/sharp/framework/font-awesome/css/font-awesome.min.css?ver=4.0.1' type='text/css' media='all'/>
<link rel='stylesheet' id='gabfire-style-css' href='http://www.zambianwatchdog.com/wp-content/themes/sharp-child/style.css?ver=4.0.1' type='text/css' media='all'/>
<link rel='stylesheet' id='jetpack_css-css' href='http://www.zambianwatchdog.com/wp-content/plugins/jetpack/css/jetpack.css?ver=3.2' type='text/css' media='all'/>
<script type='text/javascript' src='http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js?ver=4.0.1'></script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/plugins/jetpack/modules/related-posts/related-posts.js?ver=20140611'></script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/themes/sharp/inc/js/jquery.cycle2.min.js?ver=4.0.1'></script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/themes/sharp/inc/js/jquery.easing.min.js?ver=4.0.1'></script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/themes/sharp/framework/bootstrap/js/bootstrap.min.js?ver=4.0.1'></script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/themes/sharp/inc/js/flowplayer/flowplayer.min.js?ver=4.0.1'></script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/themes/sharp/inc/js/jquery.tools.min.js?ver=4.0.1'></script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/themes/sharp/inc/js/responsive-menu.js?ver=4.0.1'></script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/themes/sharp/inc/js/slides.min.jquery.js?ver=4.0.1'></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://www.zambianwatchdog.com/xmlrpc.php?rsd"/>
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://www.zambianwatchdog.com/wp-includes/wlwmanifest.xml"/> 
<link rel='prev' title='PF members feel betrayed by Lungu&#8217;s auctioning of the party to RB' href='http://www.zambianwatchdog.com/pf-members-feel-betrayed-by-lungus-auctioning-of-the-party-to-rb/'/>
<link rel='next' title='GBM says campaigns going well' href='http://www.zambianwatchdog.com/gbm-says-campains-going-well/'/>
<meta name="generator" content="WordPress 4.0.1"/>
<link rel='canonical' href='http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/'/>
<link rel='shortlink' href='http://wp.me/p3hKsL-kFh'/>
<script type="text/javascript" src="http://www.zambianwatchdog.com/wp-content/plugins/audio-player/assets/audio-player.js?ver=2.0.4.6"></script>
<script type="text/javascript">AudioPlayer.setup("http://www.zambianwatchdog.com/wp-content/plugins/audio-player/assets/player.swf?ver=2.0.4.6", {width:"290",animation:"yes",encode:"yes",initialvolume:"60",remaining:"no",noinfo:"no",buffer:"5",checkpolicy:"no",rtl:"no",bg:"6299c5",text:"333333",leftbg:"CCCCCC",lefticon:"333333",volslider:"666666",voltrack:"FFFFFF",rightbg:"B4B4B4",rightbghover:"999999",righticon:"333333",righticonhover:"FFFFFF",track:"FFFFFF",loader:"009900",border:"CCCCCC",tracker:"DDDDDD",skip:"666666",pagebg:"FFFFFF",transparentpagebg:"yes"});</script>
<meta property="og:site_name" content="Zambian Watchdog"/>
<meta property="og:title" content="UPND warns PF against attempts to rig polls"/>
<meta property="og:url" content="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/"/>
<meta property="og:description" content="PF members feel betrayed by Lungu's auctioning of the party to RB GBM says campaigns going well Related"/>
<meta property="og:type" content="article"/>
<style type="text/css">
.wp-polls .pollbar {
	margin: 1px;
	font-size: 6px;
	line-height: 8px;
	height: 8px;
	background-image: url('http://www.zambianwatchdog.com/wp-content/plugins/wp-polls/images/default/pollbg.gif');
	border: 1px solid #c8c8c8;
}
</style>
<style type="text/css">
					.wp-post-navigation a{
					text-decoration: none;
font:normal 12px arial;
					}
				 </style><style type='text/css'>img#wpstats{display:none}</style><link rel="shortcut icon" href="/wp-content/uploads/favicon.ico"/>
		
			<script type='text/javascript'>
			<!--	
			(function($) {
				$.noConflict();
				$(document).ready(function() {
					$(".children").parent("li").addClass("has-child-menu");
					$(".sub-menu").parent("li").addClass("has-child-menu");
					$(".drop").parent("li").addClass("has-child-menu");
					
					$('.fadeimage').hover(
						function() {$(this).stop().animate({ opacity: 0.5 }, 800);},
						function() {$(this).stop().animate({ opacity: 1.0 }, 800);}
					);
					
					$('.mastheadnav li ul').hide().removeClass('fallback');
					$('.mastheadnav > li').hover(
						function () {
							$('ul', this).stop().slideDown(250);
						},
						function () {
							$('ul', this).stop().slideUp(250);
						}
					);			
					
					$('.mainnav li ul').hide().removeClass('fallback');
					$('.mainnav > li').hover(
						function () {
							$('ul', this).stop().slideDown(250);
						},
						function () {
							$('ul', this).stop().slideUp(250);
						}
					);

					$('.secondnav li ul').hide().removeClass('fallback');
					$('.secondnav > li').hover(
						function () {
							$('ul', this).stop().slideDown(250);
						},
						function () {
							$('ul', this).stop().slideUp(250);
						}
					);	
					
					$('#tabs-left').tab();
					$('#tabs > li > a').hover( function(){$(this).tab('show');});
				
					$('a[href=#top]').click(function(){	$('html, body').animate({scrollTop:0}, 'slow');	return false; });		
					// Responsive Menu (TinyNav)
					$(".responsive_menu").tinyNav({
						active: 'current_page_item', // Set the "active" class for default menu
						label: ''
					});
					$(".tinynav").selectbox();
					$("ul.tabs").tabs("div.panes > div");
					$("ul.sc_tabs").tabs("div.sc_tabs-content > div");
					$('.tooltip-link').tooltip({ placement: 'top'});

					//portfolio - show link
					$('.gallery-background').hover(
						function () {
							$(this).animate({opacity:'1'});
						},
						function () {
							$(this).animate({opacity:'0'});
						}
					);
					
				});
			})(jQuery);
			// -->
			</script>
			
				<style type="text/css">.recentcomments a{display:inline !important;padding:0 !important;margin:0 !important;}</style>

<!-- Jetpack Open Graph Tags -->
<meta property="og:type" content="article"/>
<meta property="og:title" content="UPND warns PF against attempts to rig polls"/>
<meta property="og:url" content="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/"/>
<meta property="og:description" content="The United Party for National Development (UPND) have warned the PF that they are aware of attempts to rig the elections but have warned that they will soon be caught one by one. And the party has ..."/>
<meta property="article:published_time" content="2015-01-05T12:13:22+00:00"/>
<meta property="article:modified_time" content="2015-01-05T12:21:34+00:00"/>
<meta property="article:author" content="http://www.zambianwatchdog.com/author/jabulani/"/>
<meta property="og:site_name" content="Zambian Watchdog"/>
<meta property="og:image" content="https://s0.wp.com/i/blank.jpg"/>
<meta name="twitter:site" content="@jetpack"/>
<meta name="twitter:card" content="summary"/>

	


<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>

	<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
	<script src="http://www.zambianwatchdog.com/wp-content/themes/sharp/framework/bootstrap/assets/js/respond.min.js"></script>
<![endif]-->








<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-8423487-1', 'auto');
  ga('require', 'displayfeatures');
  ga('send', 'pageview');

</script>
<!-- Start taboola -->
<script type="text/javascript">
  window._taboola = window._taboola || [];
  _taboola.push({article:'auto'});
  !function (e, f, u) {
    e.async = 1;
    e.src = u;
    f.parentNode.insertBefore(e, f);
  }(document.createElement('script'),
  document.getElementsByTagName('script')[0],
  'https://cdn.taboola.com/libtrc/diversityad-zambianwatchdog/loader.js');
</script>






<script type='text/javascript'>
var googletag = googletag || {};
googletag.cmd = googletag.cmd || [];
(function() {
var gads = document.createElement('script');
gads.async = true;
gads.type = 'text/javascript';
var useSSL = 'https:' == document.location.protocol;
gads.src = (useSSL ? 'https:' : 'http:') + 
'//www.googletagservices.com/tag/js/gpt.js';
var node = document.getElementsByTagName('script')[0];
node.parentNode.insertBefore(gads, node);
})();
</script>



<script type='text/javascript'>



var gptAdSlots = [];


googletag.cmd.push(function() {

	var mappingHeaderAd = googletag.sizeMapping().
	
	addSize([200, 200], [320, 50]).
	addSize([539, 200], [468, 60]).
	addSize([767, 200], [728, 90]).
	addSize([992, 200], [[728, 90], [970, 90]]). 
	addSize([1201, 200],[728, 90]).build();


	var mappingRightHandFSatf = googletag.sizeMapping().
	
	addSize([0, 0], [88, 88]).
	addSize([992, 200],[300, 250]).
	addSize([1201, 200], [[336, 28], [300, 250]]).build(); 


	var mappingRightHandFSbtf = googletag.sizeMapping().
	
	addSize([200, 50], [300, 250]).
	addSize([539, 200],[[336, 280], [300, 250]]).
	addSize([992, 200], [88, 88]).build(); 


	var mappingHompageBottomLeft = googletag.sizeMapping().
	
	addSize([200, 50], [300, 250]).
	addSize([539, 200],[[336, 280], [300, 250]]).
	addSize([767, 200], [728, 90]).build(); 


	var mappingSidebar2 = googletag.sizeMapping().
	
	addSize([0, 0],[88, 88]).
	addSize([992, 200], [300, 600]).build(); 


	var mappingBelowFeaturedSlider = googletag.sizeMapping().
	addSize([200, 200],[[300, 250],[336, 280]]).
	addSize([539, 200],[[300, 250],[336, 280]]).
	addSize([767, 200], [336, 280]).build(); 


	var mappingCategoryInLoop = googletag.sizeMapping().
	addSize([200, 200],[[336, 280],[300, 250]]).
	addSize([767, 200],[728, 90]).
	addSize([992, 200],[[336, 280],[300, 250]]).
	addSize([1201, 200], [728, 90]).build(); 
	

	var mappingArticleThirdP = googletag.sizeMapping().
	addSize([50, 50], [[336, 280], [300, 250]]).build(); 





/*ADS START*/	


	gptAdSlots[0] = googletag.defineSlot('/6379308/da-zwd-a', [728, 90], 'zwd001').addService(googletag.pubads())
		.defineSizeMapping(mappingHeaderAd)
		.setTargeting("url", "zambianwatchdog.com")
		.setTargeting("fold", "atf")
		.setTargeting("lang", "english")
		.setTargeting("page", "ros");

	gptAdSlots[1] = googletag.defineSlot('/6379308/da-zwd-a', [336, 280], 'zwd002').addService(googletag.pubads())
		.defineSizeMapping(mappingRightHandFSatf)
		.setTargeting("url", "zambianwatchdog.com")
		.setTargeting("fold", "atf")
		.setTargeting("lang", "english")
		.setTargeting("page", "ros");


	gptAdSlots[4] = googletag.defineSlot('/6379308/da-zwd-b', [300, 600], 'zwd003').addService(googletag.pubads())
		.defineSizeMapping(mappingSidebar2)
		.setTargeting("url", "zambianwatchdog.com")
		.setTargeting("fold", "btf")
		.setTargeting("lang", "english")
		.setTargeting("page", "ros");


	gptAdSlots[2] = googletag.defineSlot('/6379308/da-zwd-b', [300, 250], 'zwd004').addService(googletag.pubads())
		.defineSizeMapping(mappingRightHandFSbtf)
		.setTargeting("url", "zambianwatchdog.com")
		.setTargeting("fold", "btf")
		.setTargeting("lang", "english")
		.setTargeting("page", "ros");


	gptAdSlots[5] = googletag.defineSlot('/6379308/da-zwd-b', [[336, 280],[300, 250]], 'zwd005').addService(googletag.pubads())
		.defineSizeMapping(mappingBelowFeaturedSlider)
		.setTargeting("url", "zambianwatchdog.com")
		.setTargeting("fold", "btf")
		.setTargeting("lang", "english")
		.setTargeting("page", "home");


	gptAdSlots[3] = googletag.defineSlot('/6379308/da-zwd-b', [728, 90], 'zwd006').addService(googletag.pubads())
		.defineSizeMapping(mappingHompageBottomLeft)
		.setTargeting("url", "zambianwatchdog.com")
		.setTargeting("fold", "btf")
		.setTargeting("lang", "english")
		.setTargeting("page", "ros");


	gptAdSlots[7] =googletag.defineSlot('/6379308/da-zwd-b', [336, 280], 'zwd007').addService(googletag.pubads())
	.defineSizeMapping(mappingArticleThirdP)
	.setTargeting("url", "zambianwatchdog.com")
	.setTargeting("fold", "btf")
	.setTargeting("lang", "english")
	.setTargeting("page", "article");


gptAdSlots[6] = googletag.defineSlot('/6379308/da-zwd-b', [336, 280], 'zwd008').addService(googletag.pubads())
	.defineSizeMapping(mappingCategoryInLoop)
	.setTargeting("url", "zambianwatchdog.com")
	.setTargeting("fold", "btf")
	.setTargeting("lang", "english")
	.setTargeting("page", "section");





/*ADS END*/

googletag.pubads().enableSingleRequest();
googletag.enableServices();



/*
window.onresize = adResize;

function adResize(){
	googletag.pubads().refresh( [gptAdSlots[0], gptAdSlots[1], gptAdSlots[2], gptAdSlots[3], gptAdSlots[4], gptAdSlots[5], gptAdSlots[6], gptAdSlots[7]]);
};
	
*/


	
}); 




</script>









<link rel='stylesheet' href='/wp-content/uploads/custom-style.css' type='text/css' media='all'/>

<link rel="stylesheet" type="text/css" href="/wp-content/plugins/adsight/articlead.css"></head>


<body class="single single-post postid-79439 single-format-standard"><noscript><meta HTTP-EQUIV="refresh" content="0;url='http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/?PageSpeed=noscript'" /><style><!--table,div,span,font,p{display:none} --></style><div style="display:block">Please click <a href="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/?PageSpeed=noscript">here</a> if you are not redirected within a few seconds.</div></noscript>
<div class="container">
<script type="text/javascript"> Caspion = { 'cfg': { 'id': 'zambianwatchdogcom', 'url': '//adscaspion.appspot.com/r/' } };</script>
<script type="text/javascript" src="//adscaspion.appspot.com/cas.js"></script>
	<header class="row">
		<div class="col-sm-12 col-md-12 col-lg-4">
			<div class="sitelogo" style="padding:15px 0px 10px 0px;">		
									<h1>
						<a href="http://www.zambianwatchdog.com/" title="Breaking and investigative news on Zambia">
							<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAAA+CAMAAAB3CIU6AAABJlBMVEUAAAD///8AJ0oALEsAJ0oALEsAJ0oALEsAJ0oAJ0oALEsAJ0oAJ0oALEsAJ0oAJ0oALEsAJ0oALEsAJ0oAJ0oALEsAJ0oAJ0oALEsAJ0oAJ0oALEsAJ0oAJ0oALEsAJ0oAJ0oALEsAJ0oAJ0oALEsAJ0oAJ0oALEsAJ0oAJ0oALEsAJ0oALEsAXWoQNVUQZ3MfcXwgQmEgcX0ve4UwUGwwe4Y/XHc/hY9AXXdAho9Pj5hQa4NQkJlfd41fmaJgeI5gmqJvpKtwhplwpKt/k6R/rrSAk6WArrWPoK+PuL6QobCQuL6fwsegr7ygw8evu8avzNCwvMewzdG/ydK/1trAytLD2dzP1t3P4ePQ197c6erf6+zg5eng6+3v8fTv9fbw8vT///8nZqWxAAAAK3RSTlMAABAQICAwMD9AQE9QUF9gYHBwf4CAj5CQn6Cgr7Cwv8DAz9DQ3+Dg7/Dwy26xPgAACElJREFUaN7tm3t70zYUh52orhdRUxMi8Oo1rTt3pm5SKPfCBgPWMRi3sW6UXZrq+3+J+SIdHclK4gR4uvCgf+rItqzXks7lJ9dpTS7OQpcvcF/gvsA1KGFclrOEG9QKnePpcXXr1LqPCddZ7a1tbm5e7q0sjwNeTLj26vrOrio7ayufDdzS2m6t7PTanwNc24JW4TWA8z4S3CcyKCs7u+PKd8sGHJMlEWyhbJGWpf6kvNItDwgcKbiijlg7SMrmPGu91xhu3LCJcsFuQT3BlgiCvhzIJKgqyh+xw7Lib0QcEg3EEYILq/dDaqMZyHc36Ffvi2ntpX4zuPa3u5PLmg2OZNWjs3IoSB/P04QouFDWuQk+K0AiS1355hLcXoTg5B2DoAncVDZFZ1k0A1/7JV82wGVQp45Y/YZybis4kulnuwCH2msA14AN6NDdTFtwgXheLPvsSjhbiS1wxR0KTgxPGosBTNETG9kxAbe+26RcMOB8fcFVfYgJnKAAlzE5MbMwVO9cTku5EovBUUZGvbgQgAVcFvjpdA9UsV3QIfYf/3bK8/L++X39xLIG52oLrjRgAWPFDwKTlUKnQ1gkamzEUf46XJjJ6qxLaZcx9BYJwIVw5E+DW9LRXnJV/nmoeQQNLhnU2yc+68eZWlYU3i+DDtbglONMTd/nBgxmOWpFHbFpcJsY4HnBdPzs8MHh4ZtRMXw30ckegotMD4c9wVg4ZwxcIg8xXJCYQdDMcB3U+733nI9eXBuK8uDvHA8N3k4b4AJ9wTmW1T4LXFyH0z3LnHCbOtsRoBXl0Uij60k4z1hweelKFxDQjwIn2LLI784Nt4wG7g/OXwz1ciOnu6uGTsCR+oITbinzwKDMAgfTAOqo8uz+3HCXFdvPdbaS7nQPLlltaQsuprK4vgokZh85UreWyrzWkRrDqXB5/5QfD+vlHufP4Zr1Fp6BeIExBdefDS6ABoP6/MyrSDovHJqVuQ+4YYEbvuF8X81LxxZa5E+RwUjE4hkNykBa+ww7CumvQ5bObVCQAz+1TMqiXOP8sXLk4+CcbDCntbTFmyrh+BBrqTKd+5zfscINj/l7tejGwvkqboybw8XKgSR6yhOqtueF20Tue2RnGz7iHExKbyycE2TSrfeleZgOF6jbzHxORqGBmBTdmeF2kB84soBdPXjy6i/kDTZLL0drpYwp89iSdd0yLKzy8SqRLrJsqJI3iyMibguEw/RQKu92ixNEVnrQimrPnQiHndwzk+vp239FkKnDLYrirOA4P8RoB69QAK2ilAWFq43c8Na9w6ORbeRSyDdlcBGj1LxvfZQ/WdYa4GZmPt0AzrbmhlfvHP5pwkUodKeQy8g+dK2PYpMFyU8CtzWjtbyMUgKKOu0rUPds4fxEWFGsMDzk/JYd7g1/t6u5AhfZ4RildUxqHWcIR6FrrVZP5Tt8TIRyHQeXHayXIPFZeeDobOESBNfRYsvrNrgXKLbcbTuOJtlAlERkFwK79lyHc/F56D3RvZeX+zq/DmfRoSufiiZVC1uUfW41KQecv4RrtlpY+KIoQQA5iNi0ZzOEzNdtKnJRV4OrtORYiOsiG088DY5CHgtvgUB4XVwex14Ft67pJ4f1STniJ3tI3qvagm72kaLalfOzrj2bcETJI5mP4GRglxItJ84QHIkMpRYJA5qYmcOtokz8HedPTLZjzpHCt9TCWnPu0TIU9vYN2RhpzwYcScztL0usqnJirOQ6SU2lBpVxoFInoaFsIw3lJDcqVzHb9yOc7+S5aguvoEzazWo6ZmJ6WrRno9+69pNa4FJllAdpiuBC40If6jLquCkazwKuh0XLfOxGTwHv4EhXv3Y7Ek64bi9Qk8b3pMWwaM9MprB5KExBH/FFRhAoo9uVnVccfVjZMRiwfNp66i3EIAIwtDbLjYJtrO29LoKtt08PDg5+/LUQ9k6w6ryhdEsx5SOVb0Vd2a5Ne9asZQRrg+nztphQqZkcUWgnhlu7Ss3w5YWhBa61oinOd39H8fLJT3v43JKCEylbWvaoeoV9nGCZ2rMGlynNvDBtYYBtvcroBqY6FsOt1MHaeghGKEZCcbVX8I2+JXDzl3cV2esfNLRScG5pKmVWvfdE/aBjtGcNzuKSm8Ihr8qgUhiULNa2R8QO1nZtR+fm7dt7Zt0G3uXxcNdDY8PMoj1jOG9+OA/VKThjnzLQtrCWrzTYwdpqa1tYGbLkvrbjaNWeMRz58JEz4ZDz6XvGzmpnOtuVJX3zUfkg6K1Y6Fbt2TIty1GOwtx80pnXnKdajITvyZifR2rUsifemTZ2W8vGtnGAPWuCgwOr9oz2sKD/rnRliR0uhjZdOK1MpDwMxNtMyNivGabMzK22ueHv4gUVItfrWLVnmESMBfLFJJQm0rrZ4JSf68NpCo3LCULQ5nRWJPvMq32H0t6YwHbJ8rEbEoJh0UXIwevaM5LgGQjkaC/cBudN2Ejvy0i5a9l5D+tfEJ0fN3hbHduXfCiUgOURGLYGwbn4l1c7bYOr6aNx/SOHqB5uSjrjq7aLNrzt8/bPFH28+6hWERpHrD2joLD45WdG/6xwAJKh7Fgz+5FjCZxFR2of7Z03J+fX58Z9g0nwFGDaNqtFe0Z0JaorrW0ajHUF+VXVj1SY+ljkbpIlqbYHaY2ttNqW7ynb5y5tVE59a+PiV5M+MMWar/GNVl17ri4qFGT5lZdbXMOo1phnaM55fXEL0pzFrClu7XrY5fZJ1QssM8xc/n/iK9U+PGBN4BZHWfak/Qwo9cNs7JpbzC/T65tOofPZwJF4up9b4P8poJHyD3HoOp8VnDLYzf6vwFn08h/DnyyE2h+GBQAAAABJRU5ErkJggg==" alt="Zambian Watchdog" title="Zambian Watchdog"/>
						</a>
					</h1>
								<div class="clearfix"></div>
			</div><!-- .logo -->
		</div>
		
		<div class="headerbanner col-sm-12 col-md-12 col-lg-8 pull-right hidden-xs" style="padding-top:0px"><div class="innerad"><div id='zwd001'>
<script type='text/javascript'>
googletag.cmd.push(function() { googletag.display('zwd001'); });
</script>
</div></div></div>	</header>
	
	<section class="row site-nav">
		<div class="col-md-12">
			<nav class="main-navigation">
				<ul class="mainnav responsive_menu">
					<li id="menu-item-29731" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-29731"><a href="https://www.zambianwatchdog.com/">Home</a></li>
<li id="menu-item-29739" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-29739"><a href="http://www.zambianwatchdog.com/category/main/">Main News</a></li>
<li id="menu-item-29733" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-29733"><a href="http://www.zambianwatchdog.com/category/editors-choice/">Editor&#8217;s Choice</a></li>
<li id="menu-item-29732" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-29732"><a href="http://www.zambianwatchdog.com/category/latestnews/">Latest</a></li>
<li id="menu-item-29734" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-29734"><a href="http://www.zambianwatchdog.com/category/more-news/">More News</a></li>
<li id="menu-item-29738" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-29738"><a href="http://www.zambianwatchdog.com/category/verbatim-statements/">Statements</a></li>
<li id="menu-item-77176" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-77176"><a href="http://www.zambianwatchdog.com/category/football/">Football</a></li>
				</ul>
			</nav>
		</div>
	</section>		
		<section class="row">
		<div class="col-md-12">
			<div class="post-lead">
				<p class="post-category"><a href="http://www.zambianwatchdog.com/category/latestnews/" rel="category tag">Latest</a></p>
				<h1 class="post-title">UPND warns PF against attempts to rig polls</h1>
				<p class="post-datecomment">
					January 5, 2015					
					<span class="commentnr">4 Comments</span>				</p>
				
							</div>
		</div>
	</section>
	
	<section class="row">
	<div class="col-xs-12 col-md-8">		
				
		<article class="post-79439 post type-post status-publish format-standard hentry category-latestnews entry last_archivepost">		
				<div class="bottomcontainerBox" style="background-color:#FFFFFF;">
			<div style="float:left; width:85px;padding-right:10px; margin:4px 4px 4px 4px;height:30px;">
			<iframe src="http://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.zambianwatchdog.com%2Fupnd-warns-pf-against-attempts-to-rig-polls%2F&amp;layout=button_count&amp;show_faces=false&amp;width=85&amp;action=like&amp;font=verdana&amp;colorscheme=light&amp;height=21" scrolling="no" frameborder="0" allowTransparency="true" style="border:none; overflow:hidden; width:85px; height:21px;"></iframe></div>
			<div style="float:left; width:85px;padding-right:10px; margin:4px 4px 4px 4px;height:30px;">
			<g:plusone size="medium" href="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/"></g:plusone>
			</div>
			<div style="float:left; width:85px;padding-right:10px; margin:4px 4px 4px 4px;height:30px;">
			<a href="http://twitter.com/share" class="twitter-share-button" data-url="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/" data-text="UPND warns PF against attempts to rig polls" data-count="horizontal"></a>
			</div>			
			</div><div style="clear:both"></div><div style="padding-bottom:4px;"></div>
<!-- Facebook Like Button v1.9.6 BEGIN [http://blog.bottomlessinc.com] -->
<iframe src="http://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.zambianwatchdog.com%2Fupnd-warns-pf-against-attempts-to-rig-polls%2F&amp;layout=standard&amp;show_faces=false&amp;width=450&amp;action=like&amp;colorscheme=light" scrolling="no" frameborder="0" allowTransparency="true" style="border:none; overflow:hidden; width:450px; height: 30px; align: left; margin: 2px 0px 2px 0px"></iframe>
<!-- Facebook Like Button END -->
<p>The United Party for National Development (UPND) have warned the PF that they are aware of attempts to rig the elections but have warned that they will soon be caught one by one.<br/>
And the party has advised the Electoral Commission of Zambia (ECZ) to find out whether they have been infiltrated by other elements instead of accusing the party of making alarming statements.<br/>
UPND Adviser to the president Douglas Siakalima said when he featured on UNZA Radio’s Lusaka Star programme Monday morning that his party was on top of things and was closely monitoring PF attempts to fidget with the election results.<br/>
Siakalima warned that those who are attempting to tamper with the election results will soon be ashamed when the UPND starts catching them one by one.<br/>
‘There are various players in this election but we shall catch them one by one because we know exactly what they are trying to do, we will get them before elections and even on the actual day of voting and they will be ashamed,’ Siakalima warned.<br/>
And Siakalima has advised the Electoral Commission of Zambia (ECZ) to find out whether they have been infiltrated by other elements instead of accusing the party of making alarming statements.<br/>
He said the ECZ should make sure they avoid vote rigging in order to avoid the chaos that follows a rigged election.<br/>
He said tampering with results caused problems in Zimbabwe, Kenya and Ivory Coast because most African leaders did not want to lose power adding that the ECZ’s biggest obligation was to provide fair elections to avoid the ugly face of chaos.<br/>
Siakalima was however quick to mention that the UPND has great respect for the Electoral Commission of Zambia (ECZ) Chairperson Judge Ireen Mambilima and stressed that she may not be aware of what some people are trying to do.<br/>
Siakalima said even the ECZ itself may not be directly involved in the alleged manoeuvres to rig the elections.<br/>
Siakalima said late President Michael Sata continuously talked about rigging prior to the 2011 elections and demanded for Parallel Voter Tabulation (PVT) because they (PF) were on top of things and no one accused them of alarming the nation.</p>

<!-- Facebook Like Button v1.9.6 BEGIN [http://blog.bottomlessinc.com] -->
<iframe src="http://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.zambianwatchdog.com%2Fupnd-warns-pf-against-attempts-to-rig-polls%2F&amp;layout=standard&amp;show_faces=false&amp;width=450&amp;action=like&amp;colorscheme=light" scrolling="no" frameborder="0" allowTransparency="true" style="border:none; overflow:hidden; width:450px; height: 30px; align: left; margin: 2px 0px 2px 0px"></iframe>
<!-- Facebook Like Button END -->
<div class="wp-post-navigation">
									   <div class="wp-post-navigation-pre">
									   <a href="http://www.zambianwatchdog.com/pf-members-feel-betrayed-by-lungus-auctioning-of-the-party-to-rb/">PF members feel betrayed by Lungu's auctioning of the party to RB</a>
									   </div>
									   <div class="wp-post-navigation-next">
									   <a href="http://www.zambianwatchdog.com/gbm-says-campains-going-well/">GBM says campaigns going well</a>
									   </div>
									</div>
<div id='jp-relatedposts' class='jp-relatedposts'>
	<h3 class="jp-relatedposts-headline"><em>Related</em></h3>
</div><section id="text-10" class="widget widget_text"><div class="widgetinner">			<div class="textwidget"><div id="taboola-below-article-thumbnails"></div>
<script type="text/javascript">
  window._taboola = window._taboola || [];
  _taboola.push({
    mode: 'thumbnails-a',
    container: 'taboola-below-article-thumbnails',
    placement: 'Below Article Thumbnails',
    target_type: 'mix'
  });
</script></div>
		</div></section>
				
				
<div id="comments">
	
			<h3 id="comments-title">
			4 Responses to &#34;<span>UPND warns PF against attempts to rig polls</span>&#34;		</h3>

	
	<ol class="commentlist">
					<li class="comment even thread-even depth-1" id="li-comment-1227193">

				<div class="comment-inner" id="comment-1227193">
				
					<div class="comment-top">
						<div class="comment-avatar">
													</div> 
						<span class="comment-author">
							<i class="icon-user"></i> 
							<cite class="fn"><a href='http://www.missionpress.org' rel='external nofollow' class='url'>Mich</a></cite> 						</span>
						<span class="comment-date-link">
							<i class="icon-calendar-empty"></i>&nbsp;January 5, 2015 at 13:44						</span>
					</div>				
					
										
					<p>Mwasokwa bamambala!!!!!!!</p>
					
					<a class='comment-reply-link' href='/upnd-warns-pf-against-attempts-to-rig-polls/?replytocom=1227193#respond' onclick='return addComment.moveForm("comment-1227193", "1227193", "respond", "79439")'>Reply</a>					
				</div><!-- comment-inner  -->

			</li><!-- #comment-## -->
			<li class="comment odd alt thread-odd thread-alt depth-1" id="li-comment-1227188">

				<div class="comment-inner" id="comment-1227188">
				
					<div class="comment-top">
						<div class="comment-avatar">
													</div> 
						<span class="comment-author">
							<i class="icon-user"></i> 
							<cite class="fn">VAMPIRO</cite> 						</span>
						<span class="comment-date-link">
							<i class="icon-calendar-empty"></i>&nbsp;January 5, 2015 at 13:33						</span>
					</div>				
					
										
					<p>Whether pf riggs or not its winning and no amount of violence will be tolerated by minions like upnd.</p>
					
					<a class='comment-reply-link' href='/upnd-warns-pf-against-attempts-to-rig-polls/?replytocom=1227188#respond' onclick='return addComment.moveForm("comment-1227188", "1227188", "respond", "79439")'>Reply</a>					
				</div><!-- comment-inner  -->

			</li><!-- #comment-## -->
			<li class="comment even thread-even depth-1" id="li-comment-1227185">

				<div class="comment-inner" id="comment-1227185">
				
					<div class="comment-top">
						<div class="comment-avatar">
													</div> 
						<span class="comment-author">
							<i class="icon-user"></i> 
							<cite class="fn">Red Square</cite> 						</span>
						<span class="comment-date-link">
							<i class="icon-calendar-empty"></i>&nbsp;January 5, 2015 at 13:29						</span>
					</div>				
					
										
					<p>UPND,MY ADVICE IS THAT LET THEM PROVIDE YOU WITH ALL POLLING STATIONS THAT BALLOT BOXES WILL BE PICKED USING ZAF HELICOPTERS.LET THE BALLOT BOXES VERIFIED,SEALED AND  BE ACCOMPANIED BY SADC ELECTIONS OBSERVERS BECAUSE THE LOCAL ONES WILL SCCUMB TO TEMPTATION FROM BOKO HARAM DOLLARS.</p>
					
					<a class='comment-reply-link' href='/upnd-warns-pf-against-attempts-to-rig-polls/?replytocom=1227185#respond' onclick='return addComment.moveForm("comment-1227185", "1227185", "respond", "79439")'>Reply</a>					
				</div><!-- comment-inner  -->

			</li><!-- #comment-## -->
			<li class="comment odd alt thread-odd thread-alt depth-1" id="li-comment-1227176">

				<div class="comment-inner" id="comment-1227176">
				
					<div class="comment-top">
						<div class="comment-avatar">
													</div> 
						<span class="comment-author">
							<i class="icon-user"></i> 
							<cite class="fn">scorpion</cite> 						</span>
						<span class="comment-date-link">
							<i class="icon-calendar-empty"></i>&nbsp;January 5, 2015 at 13:18						</span>
					</div>				
					
										
					<p>FEELING THE HEAT AND ALREADY WORKING ON LOSS STRATEGIES.</p>
					
					<a class='comment-reply-link' href='/upnd-warns-pf-against-attempts-to-rig-polls/?replytocom=1227176#respond' onclick='return addComment.moveForm("comment-1227176", "1227176", "respond", "79439")'>Reply</a>					
				</div><!-- comment-inner  -->

			</li><!-- #comment-## -->
	</ol>


<div class="wp-post-navigation">
<div class="wp-post-navigation-next wp-post-navigation-next-custom">
<a href="http://www.zambianwatchdog.com/gbm-says-campains-going-well/" rel="next">GBM says campaigns going well</a> 
</div>
<div class="wp-post-navigation-pre wp-post-navigation-pre-custom">
<a href="http://www.zambianwatchdog.com/pf-members-feel-betrayed-by-lungus-auctioning-of-the-party-to-rb/" rel="prev">PF members feel betrayed by Lungu&#8217;s auctioning of the party to RB</a> 
</div>
<div class="clear"></div>

</div>



	
	
	
		
	
									<div id="respond" class="comment-respond">
				<h3 id="reply-title" class="comment-reply-title">Leave a Reply <small><a rel="nofollow" id="cancel-comment-reply-link" href="/upnd-warns-pf-against-attempts-to-rig-polls/#respond" style="display:none;">Cancel Reply</a></small></h3>
									<form action="http://www.zambianwatchdog.com/wp-comments-post.php" method="post" id="commentform" class="comment-form">
																			<p class="comment-notes">Your email address will not be published.</p>							<div class="form-field-wrapper"><div class="input-group"><span class="input-group-addon"><i class="fa fa-user"></i></span><input class="form-control" id="author" name="author" type="text" placeholder="Name" value=""/></div></div>
<div class="form-field-wrapper mid-input-item"><div class="input-group"><span class="input-group-addon"><i class="fa fa-envelope"></i></span><input class="form-control" id="email" name="email" type="text" placeholder="Email" value=""/></div></div>
<div class="form-field-wrapper"><div class="input-group"><span class="input-group-addon"><i class="fa fa-home"></i></span><input class="form-control" placeholder="Website" id="url" name="url" type="text" value="" size="30"/></div></div>
												<p class="comment-form-comment"><textarea id="comment" placeholder="Add your comment" name="comment" cols="45" rows="8" aria-required="true"></textarea></p>												<p class="form-submit">
							<input name="submit" type="submit" id="submit" value="Post Comment"/>
							<input type='hidden' name='comment_post_ID' value='79439' id='comment_post_ID'/>
<input type='hidden' name='comment_parent' id='comment_parent' value='0'/>
						</p>
						<p style="display: none;"><input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="b9bac4312f"/></p><p class="comment-subscription-form"><input type="checkbox" name="subscribe_comments" id="subscribe_comments" value="subscribe" style="width: auto; -moz-appearance: checkbox; -webkit-appearance: checkbox;"/> <label class="subscribe-label" id="subscribe-label" for="subscribe_comments">Notify me of follow-up comments by email.</label></p><p class="comment-subscription-form"><input type="checkbox" name="subscribe_blog" id="subscribe_blog" value="subscribe" style="width: auto; -moz-appearance: checkbox; -webkit-appearance: checkbox;"/> <label class="subscribe-label" id="subscribe-blog-label" for="subscribe_blog">Notify me of new posts by email.</label></p><p style="display: none;"><input type="hidden" id="ak_js" name="ak_js" value="57"/></p>					</form>
							</div><!-- #respond -->
			
	
</div><!-- #comments -->		</article>					
	</div><!-- col-md-8 --><div class="clearfix hidden-lg hidden-md"></div>

			<aside class="col-md-4 sidebar">
			<section id="facebooklikebox-4" class="widget widget_FacebookLikeBox"><div class="widgetinner"><script src="https://connect.facebook.net/en_US/all.js#xfbml=1"></script><fb:like-box href="https://www.facebook.com/ZambianWatchdog" width="292" show_faces="true" border_color="dddddd" stream="false" header="false"></fb:like-box></div></section>
		
			<div class="widget sidebarad">
	<div id='zwd002'>
<script type='text/javascript'>
googletag.cmd.push(function() { googletag.display('zwd002'); });
</script>
</div>


<div id='zwd004'>
<script type='text/javascript'>
googletag.cmd.push(function() { googletag.display('zwd004'); });
</script>
</div>

<div class="intrestedInAdvertising">
<a style="text-align:center" href="/advertise/">Interested in advertising?</a>
</div></div>			
			
			<div class="search-wrapper">
	<div class="search-inner">
		<form class="form-wrapper cf" action="http://www.zambianwatchdog.com/">
			<input type="text" name="s" placeholder="Search in site..." required>
			<button type="submit">Search</button>
		</form>
	</div>
</div>

<div class="clearfix visible-sm"></div>			
			<section id="recent-comments-5" class="widget widget_recent_comments"><div class="widgetinner"><h3 class="widgettitle">Latest Comments</h3>
<ul id="recentcomments"><li class="recentcomments"><span class="comment-author-link">Pastor leyad</span> on <a href="http://www.zambianwatchdog.com/gbm-says-campains-going-well/comment-page-1/#comment-1227211">GBM says campaigns going well</a></li><li class="recentcomments"><span class="comment-author-link"><a href='http://yahoo' rel='external nofollow' class='url'>chick</a></span> on <a href="http://www.zambianwatchdog.com/upnd-should-get-clearance-from-me-before-they-go-back-to-shiwangandu-kampyongo/comment-page-1/#comment-1227210">UPND should get clearance from me before they go back to Shiwang’andu-Kampyongo</a></li><li class="recentcomments"><span class="comment-author-link">Pastor Leyad</span> on <a href="http://www.zambianwatchdog.com/photos-of-the-day-pf-ferrying-villagers-to-boost-numbers-at-nakonde-rally/comment-page-1/#comment-1227208">Photos of the day: PF ferrying villagers to boost numbers at Nakonde rally</a></li><li class="recentcomments"><span class="comment-author-link">Precious</span> on <a href="http://www.zambianwatchdog.com/gbm-says-campains-going-well/comment-page-1/#comment-1227198">GBM says campaigns going well</a></li><li class="recentcomments"><span class="comment-author-link">Sara</span> on <a href="http://www.zambianwatchdog.com/pf-members-feel-betrayed-by-lungus-auctioning-of-the-party-to-rb/comment-page-1/#comment-1227196">PF members feel betrayed by Lungu&#8217;s auctioning of the party to RB</a></li><li class="recentcomments"><span class="comment-author-link">Blago</span> on <a href="http://www.zambianwatchdog.com/pf-hypocrisy-on-muvi-tv-exposed/comment-page-1/#comment-1227194">PF hypocrisy on Muvi TV exposed</a></li><li class="recentcomments"><span class="comment-author-link"><a href='http://www.missionpress.org' rel='external nofollow' class='url'>Mich</a></span> on <a href="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/comment-page-1/#comment-1227193">UPND warns PF against attempts to rig polls</a></li><li class="recentcomments"><span class="comment-author-link">VAMPIRO</span> on <a href="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/comment-page-1/#comment-1227188">UPND warns PF against attempts to rig polls</a></li><li class="recentcomments"><span class="comment-author-link">Red Square</span> on <a href="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/comment-page-1/#comment-1227185">UPND warns PF against attempts to rig polls</a></li><li class="recentcomments"><span class="comment-author-link">shambala</span> on <a href="http://www.zambianwatchdog.com/pf-hypocrisy-on-muvi-tv-exposed/comment-page-1/#comment-1227183">PF hypocrisy on Muvi TV exposed</a></li><li class="recentcomments"><span class="comment-author-link">Mule</span> on <a href="http://www.zambianwatchdog.com/pf-members-feel-betrayed-by-lungus-auctioning-of-the-party-to-rb/comment-page-1/#comment-1227181">PF members feel betrayed by Lungu&#8217;s auctioning of the party to RB</a></li><li class="recentcomments"><span class="comment-author-link"><a href='http://www.missionpress.org' rel='external nofollow' class='url'>Mich</a></span> on <a href="http://www.zambianwatchdog.com/pf-members-feel-betrayed-by-lungus-auctioning-of-the-party-to-rb/comment-page-1/#comment-1227179">PF members feel betrayed by Lungu&#8217;s auctioning of the party to RB</a></li><li class="recentcomments"><span class="comment-author-link">scorpion</span> on <a href="http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/comment-page-1/#comment-1227176">UPND warns PF against attempts to rig polls</a></li><li class="recentcomments"><span class="comment-author-link">Frank</span> on <a href="http://www.zambianwatchdog.com/pf-members-feel-betrayed-by-lungus-auctioning-of-the-party-to-rb/comment-page-1/#comment-1227174">PF members feel betrayed by Lungu&#8217;s auctioning of the party to RB</a></li></ul></div></section>
<section id="text-8" class="widget widget_text"><div class="widgetinner">			<div class="textwidget"><div id='zwd003'>
<script type='text/javascript'>
googletag.cmd.push(function() { googletag.display('zwd003'); });
</script>
</div></div>
		</div></section>
<section id="text-9" class="widget widget_text"><div class="widgetinner"><h3 class="widgettitle">About Us</h3>
			<div class="textwidget"><p><strong>Who we are</strong><br/>
The Zambian Watchdog is owned by private Zambian journalists.</p>
<p><strong>What we do</strong><br/>
We publish breaking news on Zambia and about Zambia on a 24 hour basis. We also publish investigative special reports. At times we aggregate news carried by local media.</p>
<p><strong>Our guiding principle</strong><br/>
We write news regardless of who or what the subject is. We fear no one. We favour no one.</p>
</div>
		</div></section>
<section id="text-11" class="widget widget_text"><div class="widgetinner"><h3 class="widgettitle">Sponsored Posts</h3>
			<div class="textwidget"><a href="http://www.zambianwatchdog.com/things-to-know-before-importing-used-cars-from-japan/">Things to know before importing used cars from Japan</a></div>
		</div></section>
						
						
					</aside>
</section>	
		
		<section class="row bottomads">
		<div class="col-md-12">
			<div class="bottomads-innerdiv">
									<div class="col pull-left">
						<div id='zwd006'>
<script type='text/javascript'>
googletag.cmd.push(function() { googletag.display('zwd006'); });
</script>
</div>					</div>
								
									<div class="col pull-right">
						<div id="HPBottom">
</div>					</div>
							</div>
		</div>
	</section>	
		
	<section class="row footer-nav hidden-xs">
		<div class="col-md-12">	
			<div class="footernav-innerdiv">
			
								
				<nav>		
									</nav>
				<div class="clearfix"></div>
			</div>
		</div>
	</section>
	
	<footer>
		<div class="row">
			<div class="col-xs-12 col-sm-7 col-md-4">
							</div>
			
			<div class="col-xs-12 col-sm-5 col-md-3">
							</div>
			
			<div class="clearfix visible-sm"></div>
			
			<div class="col-xs-12 col-sm-3 col-md-2">
							</div>
			
			<div class="col-xs-12 col-sm-9 col-md-3 footerlast">
							</div>
		</div>
		
		<div class="row">
			<div class="col-md-12">
				
			</div>
		</div>
		
		<div class="row">
			<div class="col-md-12">

<div class="menu-footermenu-container"><ul id="menu-footermenu" class="menu"><li id="menu-item-77177" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-77177"><a>Home</a></li>
<li id="menu-item-77179" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-77179"><a href="http://www.zambianwatchdog.com/contact-us/">Contact us</a></li>
<li id="menu-item-77178" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-77178"><a href="http://www.zambianwatchdog.com/advertise/">Advertise</a></li>
<li id="menu-item-77180" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-77180"><a href="https://www.zambianwatchdog.com/feed/">RSS</a></li>
</ul></div>

				<div class="footer-meta">
				
					<p class="footer-metaleft pull-left">
						Copyright © 2003 - 2014 Zambian Watchdog.<br/>All rights reserved.					</p><!-- #site-info -->
								
					<p class="footer-metaleft pull-right">
						Zambia's Leading Investigative, 24-hour Breaking News Newspaper.



						
							<div style="display:none">
	</div>
					<div id="fb-root"></div>
					<script type='text/javascript'>
					<!--
					(function(d, s, id) {
					  var js, fjs = d.getElementsByTagName(s)[0];
					  if (d.getElementById(id)) return;
					  js = d.createElement(s); js.id = id;
					  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
					  fjs.parentNode.insertBefore(js, fjs);
					}(document, 'script', 'facebook-jssdk'));
					// -->
					</script>
				<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/plugins/akismet/_inc/form.js?ver=3.0.2'></script>
<script type='text/javascript' src='http://platform.twitter.com/widgets.js?ver=4.0.1'></script>
<script type='text/javascript' src='http://apis.google.com/js/plusone.js?ver=4.0.1'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var pollsL10n = {"ajax_url":"http:\/\/www.zambianwatchdog.com\/wp-admin\/admin-ajax.php","text_wait":"Your last request is still being processed. Please wait a while ...","text_valid":"Please choose a valid poll answer.","text_multiple":"Maximum number of choices allowed: ","show_loading":"1","show_fading":"1"};
/* ]]> */
</script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-content/plugins/wp-polls/polls-js.js?ver=2.67'></script>
<script type='text/javascript' src='http://s0.wp.com/wp-content/js/devicepx-jetpack.js?ver=201502'></script>
<script type='text/javascript' src='http://www.zambianwatchdog.com/wp-includes/js/comment-reply.min.js?ver=4.0.1'></script>

	<script src="http://stats.wp.com/e-201502.js" type="text/javascript"></script>
	<script type="text/javascript">
	st_go({v:'ext',j:'1:3.2',blog:'48559191',post:'79439',tz:'1'});
	var load_cmc = function(){linktracker_init(48559191,79439,2);};
	if ( typeof addLoadEvent != 'undefined' ) addLoadEvent(load_cmc);
	else load_cmc();
	</script>

					</p> <!-- #footer-right-side -->
				</div>
			</div>
		</div>
	</footer>
</div>







<!-- container -->

<!-- Start taboola -->
<script type="text/javascript">
  window._taboola = window._taboola || [];
  _taboola.push({flush: true});
</script>
<!-- End taboola -->



<script pagespeed_no_defer="">(function(){window.pagespeed=window.pagespeed||{};var l=window.pagespeed;
l.getResourceTimingData=function(){if(window.performance&&(window.performance.getEntries||window.performance.webkitGetEntries)){for(var m=0,n=0,e=0,p=0,f=0,q=0,g=0,r=0,h=0,t=0,k=0,c={},d=window.performance.getEntries?window.performance.getEntries():window.performance.webkitGetEntries(),b=0;b<d.length;b++){var a=d[b].duration;0<a&&(m+=a,++e,n=Math.max(n,a));a=d[b].connectEnd-d[b].connectStart;0<a&&(q+=a,++g);a=d[b].domainLookupEnd-d[b].domainLookupStart;0<a&&(p+=a,++f);a=d[b].initiatorType;c[a]?++c[a]:
c[a]=1;a=d[b].requestStart-d[b].fetchStart;0<a&&(t+=a,++k);a=d[b].responseStart-d[b].requestStart;0<a&&(r+=a,++h)}return"&afd="+(e?Math.round(m/e):0)+"&nfd="+e+"&mfd="+Math.round(n)+"&act="+(g?Math.round(q/g):0)+"&nct="+g+"&adt="+(f?Math.round(p/f):0)+"&ndt="+f+"&abt="+(k?Math.round(t/k):0)+"&nbt="+k+"&attfb="+(h?Math.round(r/h):0)+"&nttfb="+h+(c.css?"&rit_css="+c.css:"")+(c.link?"&rit_link="+c.link:"")+(c.script?"&rit_script="+c.script:"")+(c.img?"&rit_img="+c.img:"")}return""};
l.getResourceTimingData=l.getResourceTimingData;})();
(function(){window.pagespeed=window.pagespeed||{};var e=window.pagespeed;function g(a,c,b,d){this.c=a;this.a=c;this.b=b;this.d=d}e.beaconUrl="";
g.prototype.sendBeacon=function(){var a=this.c,c=window.mod_pagespeed_start,b=Number(new Date)-c,a=a+(-1==a.indexOf("?")?"?":"&"),a=a+"ets="+("load"==this.a?"load:":"unload:"),a=a+b;if("beforeunload"!=this.a||!window.mod_pagespeed_loaded){a+="&r"+this.a+"=";if(window.performance){var b=window.performance.timing,d=b.navigationStart,f=b.requestStart,a=a+(b[this.a+"EventStart"]-d),a=a+("&nav="+(b.fetchStart-d)),a=a+("&dns="+(b.domainLookupEnd-b.domainLookupStart)),a=a+("&connect="+(b.connectEnd-b.connectStart)),
a=a+("&req_start="+(f-d)),a=a+("&ttfb="+(b.responseStart-f)),a=a+("&dwld="+(b.responseEnd-b.responseStart)),a=a+("&dom_c="+(b.domContentLoadedEventStart-d));window.performance.navigation&&(a+="&nt="+window.performance.navigation.type);d=-1;b.msFirstPaint?d=b.msFirstPaint:window.chrome&&window.chrome.loadTimes&&(d=Math.floor(1E3*window.chrome.loadTimes().firstPaintTime));d-=f;0<=d&&(a+="&fp="+d)}else a+=b;e.getResourceTimingData&&window.parent==window&&(a+=e.getResourceTimingData());a+=window.parent!=
window?"&ifr=1":"&ifr=0";"load"==this.a&&(window.mod_pagespeed_loaded=!0,(b=window.mod_pagespeed_num_resources_prefetched)&&(a+="&nrp="+b),(b=window.mod_pagespeed_prefetch_start)&&(a+="&htmlAt="+(c-b)));e.panelLoader&&(c=e.panelLoader.getCsiTimingsString(),""!=c&&(a+="&b_csi="+c));e.criticalCss&&(c=e.criticalCss,a+="&ccis="+c.total_critical_inlined_size+"&cces="+c.total_original_external_size+"&ccos="+c.total_overhead_size+"&ccrl="+c.num_replaced_links+"&ccul="+c.num_unreplaced_links);""!=this.b&&
(a+=this.b);document.referrer&&(a+="&ref="+encodeURIComponent(document.referrer));a+="&url="+encodeURIComponent(this.d);e.beaconUrl=a;(new Image).src=a}};e.e=function(a,c,b,d){var f=new g(a,c,b,d);window.addEventListener?window.addEventListener(c,function(){f.sendBeacon()},!1):window.attachEvent("on"+c,function(){f.sendBeacon()})};e.addInstrumentationInit=e.e;})();

pagespeed.addInstrumentationInit('http://1-ps.googleusercontent.com/beacon?org=125_1_jt', 'load', '&s_ttfb=5&id=1420465143377952', 'http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/');</script></body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.zambianwatchdog.com/upnd-warns-pf-against-attempts-to-rig-polls/'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, 'UPND warns PF against attempts to rig polls')
        self.assertIsNone(doc.summary)
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '05 01 2015')
        self.assertEqual(doc.author, Author.unknown())
        self.assertEqual(doc.medium.name, 'Zambian Watchdog')

        self.assertEqual(doc.text, u'The United Party for National Development (UPND) have warned the PF that they are aware of attempts to rig the elections but have warned that they will soon be caught one by one.\nAnd the party has advised the Electoral Commission of Zambia (ECZ) to find out whether they have been infiltrated by other elements instead of accusing the party of making alarming statements.\nUPND Adviser to the president Douglas Siakalima said when he featured on UNZA Radio\u2019s Lusaka Star programme Monday morning that his party was on top of things and was closely monitoring PF attempts to fidget with the election results.\nSiakalima warned that those who are attempting to tamper with the election results will soon be ashamed when the UPND starts catching them one by one.\n\u2018There are various players in this election but we shall catch them one by one because we know exactly what they are trying to do, we will get them before elections and even on the actual day of voting and they will be ashamed,\u2019 Siakalima warned.\nAnd Siakalima has advised the Electoral Commission of Zambia (ECZ) to find out whether they have been infiltrated by other elements instead of accusing the party of making alarming statements.\nHe said the ECZ should make sure they avoid vote rigging in order to avoid the chaos that follows a rigged election.\nHe said tampering with results caused problems in Zimbabwe, Kenya and Ivory Coast because most African leaders did not want to lose power adding that the ECZ\u2019s biggest obligation was to provide fair elections to avoid the ugly face of chaos.\nSiakalima was however quick to mention that the UPND has great respect for the Electoral Commission of Zambia (ECZ) Chairperson Judge Ireen Mambilima and stressed that she may not be aware of what some people are trying to do.\nSiakalima said even the ECZ itself may not be directly involved in the alleged manoeuvres to rig the elections.\nSiakalima said late President Michael Sata continuously talked about rigging prior to the 2011 elections and demanded for Parallel Voter Tabulation (PVT) because they (PF) were on top of things and no one accused them of alarming the nation.')
        
