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
        
