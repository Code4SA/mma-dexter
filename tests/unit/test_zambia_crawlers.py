# -*- coding: utf-8 -*-

import unittest

from dexter.models import Document, Author, db
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
        

class TestZambiaDailyMailCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = ZambiaDailyMailCrawler()

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
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"  lang="en-EN" prefix="og: http://ogp.me/ns#"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"  lang="en-EN" prefix="og: http://ogp.me/ns#"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"  lang="en-EN" prefix="og: http://ogp.me/ns#"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en-EN" prefix="og: http://ogp.me/ns#"> <!--<![endif]-->

<head>
    <link rel="profile" href="http://gmpg.org/xfn/11" />
    <link rel="pingback" href="http://www.daily-mail.co.zm/xmlrpc.php" />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>RB weighs in for Lungu - Zambia Daily MailZambia Daily Mail</title>
    
<!-- This site is optimized with the Yoast WordPress SEO plugin v1.6 - https://yoast.com/wordpress/plugins/seo/ -->
<link rel="canonical" href="https://www.daily-mail.co.zm/?p=16082" />
<meta property="og:locale" content="en_US" />
<meta property="og:type" content="article" />
<meta property="og:title" content="RB weighs in for Lungu - Zambia Daily Mail" />
<meta property="og:description" content="DARLINGTON MWENDABAI &amp; HOPE NYOKA, Chipata FORMER President Rupiah Banda has endorsed Patriotic Front presidential candidate Edgar Lungu for the January 20 presidential election. Mr Banda described this year as a dawn of new hope where all Zambians should turn up in numbers to vote for Mr Lungu for continuity and stability. The former head &hellip;" />
<meta property="og:url" content="https://www.daily-mail.co.zm/?p=16082" />
<meta property="og:site_name" content="Zambia Daily Mail" />
<meta property="article:publisher" content="https://www.facebook.com/ZAMBIA.DAILY.MAIL" />
<meta property="article:tag" content="Edgar Lungu" />
<meta property="article:tag" content="presidential election" />
<meta property="article:tag" content="Rupiah Banda" />
<meta property="article:section" content="News" />
<meta property="article:published_time" content="2015-01-05T00:10:03+00:00" />
<meta property="article:modified_time" content="2015-01-05T03:49:22+00:00" />
<meta property="og:updated_time" content="2015-01-05T03:49:22+00:00" />
<meta property="og:image" content="http://www.daily-mail.co.zm/wp-content/uploads/2015/01/Rupiah-Banda-EDGAR-LUNGU.jpg" />
<meta name="twitter:card" content="summary"/>
<meta name="twitter:site" content="@zadama24"/>
<meta name="twitter:domain" content="Zambia Daily Mail"/>
<meta name="twitter:creator" content="@zadama24"/>
<!-- / Yoast WordPress SEO plugin. -->

<link rel="alternate" type="application/rss+xml" title="Zambia Daily Mail &raquo; RB weighs in for Lungu Comments Feed" href="https://www.daily-mail.co.zm/?feed=rss2&#038;p=16082" />
<link rel='stylesheet' id='tcvn-recentpost-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='tcvn-recentpost-admin-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/admin/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='vina-breaking-admin-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/vina-breaking-news/includes/admin/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='vina-breaking-stile-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/vina-breaking-news/includes/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='vina-admin-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/vina-cslider-widget/includes/admin/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='vina-cslider-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/vina-cslider-widget/includes/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='vina_newstab-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/vina_news_tab/includes/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='vina_newstab-admin-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/vina_news_tab/includes/admin/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='vina-weather-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/vina_weather_widget/includes/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='tcvn-weather-tabs-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/vina_weather_widget/includes/css/style_tab.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='tcvn-weather-admin-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/vina_weather_widget/includes/admin/css/style.css?ver=1.0' type='text/css' media='screen' />
<link rel='stylesheet' id='bootstrap.min.css-css'  href='https://www.daily-mail.co.zm/wp-content/themes/vina_news/css/bootstrap.min.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='font-awesome.css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/helix/css/font-awesome.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='bootstrap-responsive.min.css-css'  href='https://www.daily-mail.co.zm/wp-content/themes/vina_news/css/bootstrap-responsive.min.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='theme.css-css'  href='https://www.daily-mail.co.zm/wp-content/themes/vina_news/css/theme.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='presets/preset3.css-css'  href='https://www.daily-mail.co.zm/wp-content/themes/vina_news/css/presets/preset3.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='jqueri_ui-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/player/js/jquery-ui.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='wpic-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/wp-image-carousel/css/style.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='flowplayer-css-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/easy-video-player/lib/minimalist.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='bwg_frontend-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/photo-gallery/css/bwg_frontend.css?ver=1.2.2' type='text/css' media='all' />
<link rel='stylesheet' id='bwg_font-awesome-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/photo-gallery/css/font-awesome-4.0.1/font-awesome.css?ver=4.0.1' type='text/css' media='all' />
<link rel='stylesheet' id='bwg_mCustomScrollbar-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/photo-gallery/css/jquery.mCustomScrollbar.css?ver=1.2.2' type='text/css' media='all' />
<link rel='stylesheet' id='rsss_front_style-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/responsive-social-sidebar-share/css/rsss_front.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='chosen-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/wp-job-manager/assets/css/chosen.css?ver=3.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='wp-job-manager-frontend-css'  href='https://www.daily-mail.co.zm/wp-content/plugins/wp-job-manager/assets/css/frontend.css?ver=3.6.1' type='text/css' media='all' />
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-includes/js/jquery/jquery.js?ver=1.10.2'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.2.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/helix/js/bootstrap.min.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/themes/vina_news/js/helix.core.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/helix/js/modernizr-2.6.2.min.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/helix/js/menu.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/themes/vina_news/js/bootstrap-tab.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-includes/js/comment-reply.min.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/player/js/jquery-ui.min.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/player/js/jquery.transit.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/player/js/flash_detect.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/wp-image-carousel/js/jcarousellite_1.0.1.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/easy-video-player/lib/flowplayer.js?ver=3.6.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/jquery-image-lazy-loading/js/jquery.lazyload.min.js?ver=1.7.1'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/photo-gallery/js/bwg_frontend.js?ver=1.2.2'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/photo-gallery/js/jquery.mobile.js?ver=1.2.2'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/photo-gallery/js/jquery.mCustomScrollbar.concat.min.js?ver=1.2.2'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/photo-gallery/js/jquery.fullscreen-0.4.1.js?ver=0.4.1'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var bwg_objectL10n = {"bwg_field_required":"field is required.","bwg_mail_validation":"This is not a valid email address.","bwg_search_result":"There are no images matching your search."};
/* ]]> */
</script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/photo-gallery/js/bwg_gallery_box.js?ver=1.2.2'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/responsive-social-sidebar-share/js/rsss_front.js?ver=3.6.1'></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.daily-mail.co.zm/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://www.daily-mail.co.zm/wp-includes/wlwmanifest.xml" /> 

			<style type='text/css'>
				#wpadminbar .quicklinks li#wp-admin-bar-clickystats {
					height: 28px
				}

				#wpadminbar .quicklinks li#wp-admin-bar-clickystats a {
					height: 28px;
					padding: 0
				}

				#wpadminbar .quicklinks li#wp-admin-bar-clickystats a img {
					padding: 4px 5px;
					height: 20px;
					width: 99px;
				}
			</style>
		
<script type='text/javascript'>
var g_hanaFlash = false;
try {
  var fo = new ActiveXObject('ShockwaveFlash.ShockwaveFlash');
  if(fo) g_hanaFlash = true;
}catch(e){
  if(navigator.mimeTypes ['application/x-shockwave-flash'] != undefined) g_hanaFlash = true;
}
function hanaTrackEvents(arg1,arg2,arg3,arg4) { if ( typeof( pageTracker ) !=='undefined') { pageTracker._trackEvent(arg1, arg2, arg3, arg4);} else if ( typeof(_gaq) !=='undefined'){  _gaq.push(['_trackEvent', arg1, arg2, arg3, arg4]);}}
function hana_check_mobile_device(){ if(navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPod/i) || navigator.userAgent.match(/iPad/i)  || navigator.userAgent.match(/Android/i)) { return true; }else return false; }
</script>
<style type='text/css'>
img.lazy { display: none; }
</style>
<style tyle="text/css">.container {max-width: 1170px;}</style></head>
<body id="sp-wrapper" class="single single-post postid-16082 single-format-standard preset3 ltr responsive hfeed bg vina-news">

<!-- Top Block -->
	<section id="sp-top-wrapper">
		<div class="container">

<a href="http://www.zesco.co.zm" target="_blank"><img src="wp-content/uploads/top_1170x120.fw.png" /></a>

			<div id="sp-top">
				<div class="row-fluid">
					<div id="sp-menu" class="span9">
						
<div class="mobile-menu pull-right btn hidden-desktop" id="sp-moble-menu">
	<i class="icon-align-justify"></i>
</div>

<nav id="sp-main-menu" class="visible-desktop pull-left" role="navigation"><div class="main-navigation"><ul id="menu-main-menu" class="sp-menu level-0"><li id="menu-item-357" class="menu-item menu-item-type-post_type menu-item-object-page" ><a class="menu-item" href="https://www.daily-mail.co.zm/">Home</a></li>
<li id="menu-item-1337" class="menu-item menu-item-type-custom menu-item-object-custom" ><a class="menu-item" href="https://mailhost.daily-mail.co.zm/owa">Staff Mail</a></li>
<li id="menu-item-12562" class="menu-item menu-item-type-post_type menu-item-object-page" ><a class="menu-item" href="https://www.daily-mail.co.zm/?page_id=12560">Jobs @ Zambia Daily Mail</a></li>
</ul></div></nav>

<script type="text/javascript">
	jQuery(function($){
		mainmenu();
		
		$(window).on('resize',function(){
			mainmenu();
		});
		
		function mainmenu() {
			$('.sp-menu').spmenu({
				startLevel: 0,
				direction:'ltr',
				initOffset: {
					x:0,
					y:0				},
				subOffset: {
					x:0,
					y:0				},
				center:0			});
		}
		
		//Mobile Menu
		$('#sp-main-menu > > ul').mobileMenu({
			defaultText:'--Select Menu--',
			appendTo: '#sp-moble-menu'
		});
		
	});
	
</script>					</div>
					<div class="span3">
						<div class="search-form pull-right">
	<form method="get" id="searchform" class="form-inline" action="https://www.daily-mail.co.zm/">
		<div class="input-append">
		  <input type="text" name="s" class="input-medium" id="s" placeholder="Search" />
		  <span class="border"></span>
		  <button class="btn btn-primary" type="submit"><i class="icon-search"></i></button>
		</div>
	</form>
</div>
					</div>
				</div>
			</div>
		</div>
	</section>

<!-- Header Block -->
	<header id="sp-header-wrapper" role="banner">
		<div class="container">
			<div id="sp-header">
				<div class="row-fluid">
					<div class="span5">
						
	
	<a id="logo" style="width:422px; height:100px" class="pull-left" href="https://www.daily-mail.co.zm/" title="Zambia Daily Mail" rel="home"></a>

					</div>
					<div class="span7">
						                <div id="sp-position-top2">
                    <div id="text-11" class=" sp-widget widget_text">			<div class="textwidget"><a href="http://www.henanguojizambia.com"  target="_blank"><img src="wp-content/uploads/top_banner.gif" /></a></div>
		</div>                </div>
                					</div>
				</div>
			</div>
		</div>
	</header>

<!-- Category Block -->
	<section id="sp-category-wrapper">
		<div class="container">
			<div id="sp-category-inner">
				<div class="row-fluid">
					<div id="sp-category">
						
<div class="mobile-menu pull-right btn hidden-desktop" id="sp-moble-categories">
	Category Menu &nbsp;
	<i class="icon-align-justify"></i>
</div>

<nav id="sp-main-categories" class="visible-desktop pull-left" role="navigation"><div class="main-navigation"><ul id="menu-menu-category" class="sp-menu level-0"><li id="menu-item-603" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent" ><a class="menu-item" href="https://www.daily-mail.co.zm/?cat=91">News</a></li>
<li id="menu-item-567" class="menu-item menu-item-type-taxonomy menu-item-object-category" ><a class="menu-item" href="https://www.daily-mail.co.zm/?cat=77">Business</a></li>
<li id="menu-item-1309" class="menu-item menu-item-type-taxonomy menu-item-object-category" ><a class="menu-item" href="https://www.daily-mail.co.zm/?cat=112">Court News</a></li>
<li id="menu-item-553" class="menu-item menu-item-type-taxonomy menu-item-object-category" ><a class="menu-item" href="https://www.daily-mail.co.zm/?cat=63">Features</a></li>
<li id="menu-item-6623" class="menu-item menu-item-type-taxonomy menu-item-object-category" ><a class="menu-item" href="https://www.daily-mail.co.zm/?cat=75">Gender</a></li>
<li id="menu-item-309" class="menu-item menu-item-type-taxonomy menu-item-object-category" ><a class="menu-item" href="https://www.daily-mail.co.zm/?cat=28">Sport</a></li>
<li id="menu-item-560" class="menu-item menu-item-type-taxonomy menu-item-object-category" ><a class="menu-item" href="https://www.daily-mail.co.zm/?cat=84">Entertainment</a></li>
<li id="menu-item-587" class="menu-item menu-item-type-taxonomy menu-item-object-category" ><a class="menu-item" href="https://www.daily-mail.co.zm/?cat=98">Technology</a></li>
</ul></div></nav>

<script type="text/javascript">
	jQuery(function($){
		
		//Mobile Menu
		$('#sp-main-categories > > ul').mobileMenu({
			defaultText:'--Select Menu--',
			appendTo: '#sp-moble-categories'
		});
		
	});
	
</script>					</div>&nbsp;<a href="http://www.daily-mail.co.zm/classifieds" target="_blank"><img src="wp-content/uploads/buttons/b_classy.jpg"/></a>&nbsp;<a href="http://www.daily-mail.co.zm/tourism" target="_blank"><img src="wp-content/uploads/buttons/b_tourism.jpg"/></a>
				</div>
			</div>
		</div>
	</section>

<!-- Breaknew Block -->
	<section id="sp-breaknew-wrapper">
		<div class="container">
			<div id="sp-breaknew-inner">
				                <div id="sp-position-breakingnews">
                    <div id="breaking_widget-4" class=" sp-widget Breaking_Widget"><div class="vina-header-top-marquee" style="width:100%; height:auto">
        <div class="vina-marquee-head" style="margin-top:0px;">BREAKING NEWS</div>
        <div class="vina-marquee-wrapper">
        <div id="vina-marquee-breaking_widget-4" class="vina-marquee">
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16082">RB weighs in for Lungu</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16083">Vote for Lungu, Scott tells Luanshya</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16102">Urban population explosion worries Chenda</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16093">State warns illegal bus station ‘tax’ collectors</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16097">Quality jobs coming, says HH </a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16087">Sondashi hails Sata formula</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16098">Chongwe PF gives Masebo vote of no confidence</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16090">Nawakwi pledges to cut presidential powers </a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=15979">Campaign violence: 4 nabbed</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=15986">Campaign for Lungu, Scott prods PF members</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=15985">Man finds ex-wife at Cockpit, commits suicide </a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=15998">Zesco ‘shuts’ 6 towns to improve power</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16002">Agriculture needs mechanisation, says Nawakwi</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16007">ECZ to summon UPND boss over rigging claim</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16006">MMD only party without violence tag - Nakacinda</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=15989">PF condemns attacks on Lungu’s health</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=16001">Bad Chinsali, Isoka roads irk Sondashi</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=15996">Ballot printing completed</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=15992">50 South youths in K233,000</a>
                                            </div>
                        <div>
                <a href="http://www.daily-mail.co.zm/?p=15928">Scott drums for Edgar Lungu </a>
                                            </div>
                    </div>
    </div>
    <div class="vina-clear"></div>
</div>

<script type="text/javascript">
    jQuery(document).ready(function(){
        var marquee = jQuery("#vina-marquee-breaking_widget-4"); 
        var time_multiplier = 20;
        var current;
                marquee.hover(function(){
           current.pause();
        }, function(){
           current.resume();
        })
        
        var reset = function() {
            current = jQuery(this);
            var item_width = jQuery(this).outerWidth();

            var time = time_multiplier * jQuery(this).outerWidth(); 
            jQuery(this).animate({ 'margin-left': -item_width }, time, 'linear', function(){
                var clone_item = jQuery(this).clone();
                clone_item.css({ 'margin-left': '0' });
                marquee.append(clone_item);
                jQuery(this).remove();
                reset.call(marquee.children().filter(':first'));
            });	
        };
        reset.call(marquee.children().filter(':first'));
    });
</script>
</div>                </div>
                			</div>
		</div>
	</section>

<!-- Feature Block -->

<!-- Promotion Block -->


<section id="sp-main" role="main">
<div class="container">
<div id="sp-main-body-wrapper">	
	<div class="container" id="content">
		
		
	
		<div class="row-fluid">
		
						
							<div class="span5 main-post">		
					
<ul class="breadcrumb">
	<li>You are here:</li>
  <li>
	<a href="https://www.daily-mail.co.zm" class="breadcrumb_home">Home</a> <span class="divider">/</span>
  </li>
  <li class="active">
  
					<a href="https://www.daily-mail.co.zm/?cat=91">News</a> <span class="raquo">&raquo;</span> RB weighs in for Lungu		  
  </li>
</ul>
	<article id="post-16082" class="post-16082 post type-post status-publish format-standard hentry category-news tag-edgar-lungu tag-presidential-election tag-rupiah-banda">
		<header class="entry-header">
			<h1 class="entry-title page-header">RB weighs in for Lungu<div id="rsss_sidebar"><div class="ss_sidebar_button">
			<a href="http://twitter.com/share" class="twitter-share-button" data-count="vertical">Tweet</a>
			<script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
			</div>
			<div class="clear"></div><div class="ss_sidebar_button facebook_ss_sidebar">
			<a href="http://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.daily-mail.co.zm%2F%3Fp%3D16082&t=" target="blank"><img src="https://www.daily-mail.co.zm/wp-content/plugins/responsive-social-sidebar-share/images/fbshare.gif" /></a>
			</div>
			<div class="clear"></div><div class="ss_sidebar_button">
			<iframe src="http://www.facebook.com/plugins/like.php?href=https%3A%2F%2Fwww.daily-mail.co.zm%2F%3Fp%3D16082&amp;layout=box_count&amp;show_faces=true&amp;width=52&amp;action=like&amp;font=segoe+ui&amp;colorscheme=light" scrolling="no" frameborder="0" style="border:none; overflow:hidden;width:52px;height:62px;" allowTransparency="true">
			</iframe></div>
			<div class="clear"></div><div class="ss_sidebar_button">
			<script type="text/javascript">(function() { 
			var s = document.createElement("SCRIPT"), s1 = document.getElementsByTagName("SCRIPT")[0]; 
			s.type = "text/javascript"; 
			s.async = true; 
			s.src = "http://widgets.digg.com/buttons.js"; 
			s1.parentNode.insertBefore(s, s1); })(); 
			</script><a class="DiggThisButton DiggMedium"></a>
			</div>
			<div class="clear"></div><div class="ss_sidebar_button"><a target="_blank"><script src="http://www.stumbleupon.com/hostedbadge.php?s=5"></script></a></div>
			<div class="clear"></div><div class="ss_sidebar_button ss_share_button"><a href="mailto:?subject=https://www.daily-mail.co.zm/?p=16082" >Email</a></div>
			<div class="clear"></div><a style="display:block !important;" target="_blank" class="rsss_ficon" href="http://www.wpfruits.com/downloads/wp-plugins/wp-sidebar-social-share/?rsss_refs=www.daily-mail.co.zm">RSSS</a>
		<div class="clear"></div></div><div id="rsss_sidebar_hid" style="display:none;"><span class="ss_sidebar_button ss_sidebar_twitter">
		<a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal">Tweet</a>
		<script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
		</span><span class="ss_sidebar_button">
		<a href="http://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.daily-mail.co.zm%2F%3Fp%3D16082&t=" target="blank"><img src="https://www.daily-mail.co.zm/wp-content/plugins/responsive-social-sidebar-share/images/fbshare.gif" /></a>
		</span><span class="ss_sidebar_button ss_sidebar_facebooklike">
		<iframe src="http://www.facebook.com/plugins/like.php?href=https%3A%2F%2Fwww.daily-mail.co.zm%2F%3Fp%3D16082&amp;layout=button_count&amp;show_faces=false&amp;width=60&amp;action=like&amp;font=segoe+ui&amp;colorscheme=light&amp;height=21" scrolling="no" frameborder="0" style="border:none; overflow:hidden;width:85px;height:21px;" allowTransparency="true">
		</iframe></span><span class="ss_sidebar_button">
		<script type="text/javascript">(function() {
		var s = document.createElement("SCRIPT"), s1 = document.getElementsByTagName("SCRIPT")[0]; 
		s.type = "text/javascript";
		s.async = true;
		s.src = "http://widgets.digg.com/buttons.js";
		s1.parentNode.insertBefore(s, s1); })(); 
		</script>
		<a class="DiggThisButton DiggCompact"></a>
		</span><span class="ss_sidebar_button">
		<script src="http://www.stumbleupon.com/hostedbadge.php?s=1"></script>
		</span><span class="ss_sidebar_button ss_share_button"><a href="mailto:?subject=https://www.daily-mail.co.zm/?p=16082" >Email</a></span><div class="clear"></div>
	</div></h1>
								</header>
		<div class="entry-meta muted " role="contentinfo">Posted in <a href="https://www.daily-mail.co.zm/?cat=91" title="View all posts in News" rel="category">News</a> on <time datetime="2015-01-05T00:10:03+00:00">January 05, 2015</time> by <span class="author vcard"><a class="url fn n" href="https://www.daily-mail.co.zm/?author=2" title="View all posts by Online Editor" role="author">Online Editor</a></span></div>		
				<div class="entry-content clearfix">
		
							<div class="post-thumbnail">
					<img width="624" height="499" src="http://www.daily-mail.co.zm/wp-content/uploads/2015/01/Rupiah-Banda-EDGAR-LUNGU-624x499.jpg" class="attachment-post-thumbnail wp-post-image" alt="FORMER President Rupiah Banda with PF president Edgar Lungu(right) and PF National Chairperson Inonge Wina at Amalula Lodge before they held a meeting at Protea Hotel yesterday:PICTURE:COLLINS PHIRI." />				</div>
						
			<p>DARLINGTON MWENDABAI &amp; HOPE NYOKA, Chipata<br />
FORMER President Rupiah Banda has endorsed Patriotic Front presidential candidate Edgar Lungu for the January 20 presidential election.<br />
<span id="more-16082"></span>Mr Banda described this year as a dawn of new hope where all Zambians should turn up in numbers to vote for Mr Lungu for continuity and stability.<br />
The former head of state, who was in a jovial mood, delivered his endorsement speech dubbed “Peace and Unity will deliver Zambia” in Chipata yesterday.<br />
He said the country needs stability and continuity, and not a revolution, hence Zambians should elect a leader who has shown the qualities of humility, commitment and unity.<br />
“For these reasons, I am appearing before you today to announce my endorsement of Minister of Justice and Defence Edgar Lungu of the PF for president on January 20, 2015,” he said.<br />
Mr Banda said after meeting Mr Lungu to understand his intentions and identify the problems which must be addressed, that he is confident that the PF candidate has qualities the Zambian people need.<br />
He said unlike the United Party for National Development (UPND) which is only interested in buying MMD members and asking his son Andrew to insult him on political podiums, Mr Lungu has shown interest to allow peace and unity to prevail in the county.<br />
“After much deliberation, I came to the conclusion that I could not support any candidate that would seek to eliminate or weaken the MMD.  I count many friends among those in the UPND, however, I cannot agree with the approach of poaching individual MMD members to defect to their camp instead of negotiating openly with the whole party,” Mr Banda said.<br />
He accused the UPND of trying to drag the country to a one party fiasco and not promoting peace and unity among Zambians.<br />
Mr Banda said he had had many meetings with UPND leaders where they suggested that he should deputise Hakainde Hichilema who had no experience of being republican president.<br />
Mr Banda  urged Mr Lungu if elected to ensure  the costs of basic goods such as mealie meal, fertilizer, fuel and cement are lowered and  the economy is stabilised while a genuine people driven constitution is delivered  and Zambians united.<br />
He said the past year had its own challenges where the country witnessed delayed payments for farmers and social divisions but this year, Zambians should vote for Mr Lungu to guide the country for the next 18 months.<br />
In accepting the endorsement, Mr Lungu said he was humbled by the gesture and promised the former head of state and Zambians that he will not let them down.<br />
“Our Late President Sata taught us to embrace all Zambians and we as PF, we do just that. We will work with the MMD who are supporting us and we are going to win the forth coming presidential election because of your support,” he said.<br />
Mr Lungu said he will not sign any social contract with the clergy or anybody but Zambians adding that he delivered as Minister of Justice a final draft constitution without any signed social contracts.<br />
He said it does not pay in a multiparty democracy to swallow opposition parties and the PF will instead co-exist with other political parties.<br />
Mr Lungu said the media enjoy press freedom and if elected, he will study the Access to Information Bill.<br />
Earlier, PF national chairperson Inonge Wina thanked Mr Banda and MMD National Executive Committee members for endorsing Mr Lungu, a gesture she described as rare from a former head of state.<br />
Former MMD national secretary Muhabi Lungu said all party structures will support Mr Lungu.</p>
		</div>
		
						
		
		<nav class="nav-single clearfix">
			<ul class="pager">
				<li class="previous"><a href="https://www.daily-mail.co.zm/?p=16110" rel="prev"><span class="meta-nav">&larr;</span> Kenya defender to ‘light up’ Zesco</a></li>
				<li class="next"><a href="https://www.daily-mail.co.zm/?p=16129" rel="next">Chinese firm ‘finds’ diamonds in Mbala <span class="meta-nav">&rarr;</span></a></li>
			</ul>
		</nav><!-- .nav-single -->		
		
		<footer>
			<ul class="entry-tags"><li><a href="https://www.daily-mail.co.zm/?tag=edgar-lungu" rel="tag">Edgar Lungu</a></li><li><a href="https://www.daily-mail.co.zm/?tag=presidential-election" rel="tag">presidential election</a></li><li><a href="https://www.daily-mail.co.zm/?tag=rupiah-banda" rel="tag">Rupiah Banda</a></li></ul>					</footer>
		
		
<div id="comments" class="comments-area">
		
	
									<div id="respond" class="comment-respond">
				<h3 id="reply-title" class="comment-reply-title">Leave a Reply <small><a rel="nofollow" id="cancel-comment-reply-link" href="/?p=16082#respond" style="display:none;">Cancel reply</a></small></h3>
									<form action="https://www.daily-mail.co.zm/wp-comments-post.php" method="post" id="commentform" class="comment-form">
																			<p class="comment-notes">Your email address will not be published. Required fields are marked <span class="required">*</span></p>							<p class="comment-form-author"><label for="author">Name <span class="required">*</span></label> <input id="author" name="author" type="text" value="" size="30" aria-required='true' /></p>
<p class="comment-form-email"><label for="email">Email <span class="required">*</span></label> <input id="email" name="email" type="text" value="" size="30" aria-required='true' /></p>
<p class="comment-form-url"><label for="url">Website</label> <input id="url" name="url" type="text" value="" size="30" /></p>
												<p class="comment-form-comment"><label for="comment">Comment</label> <textarea id="comment" name="comment" cols="45" rows="8" aria-required="true"></textarea></p>						<p class="form-allowed-tags">You may use these <abbr title="HyperText Markup Language">HTML</abbr> tags and attributes:  <code>&lt;a href=&quot;&quot; title=&quot;&quot;&gt; &lt;abbr title=&quot;&quot;&gt; &lt;acronym title=&quot;&quot;&gt; &lt;b&gt; &lt;blockquote cite=&quot;&quot;&gt; &lt;cite&gt; &lt;code&gt; &lt;del datetime=&quot;&quot;&gt; &lt;em&gt; &lt;i&gt; &lt;q cite=&quot;&quot;&gt; &lt;strike&gt; &lt;strong&gt; </code></p>						<p class="form-submit">
							<input name="submit" type="submit" id="submit" value="Post Comment" />
							<input type='hidden' name='comment_post_ID' value='16082' id='comment_post_ID' />
<input type='hidden' name='comment_parent' id='comment_parent' value='0' />
						</p>
						<p style="display: none;"><input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="70abd7f95b" /></p>					</form>
							</div><!-- #respond -->
						
</div><!-- #comments -->					
	</article>
				
				
				
				</div><!--End Main-->		
				
											<aside id="centersidebar" class="span4">
							                <div id="sp-position-center">
                    <div id="recentpost_widget-2" class="center-hotnews sp-widget recentpost_widget"><h3>Editor&#8217;s Comment</h3>
<div id="tcvn-post-widget-recentpost_widget-2" class="tcvn-post-widget">
<ul class="tcvn-menu">
    <li class="event" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=16079">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=260&h=150&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2015/01/Clever-Making-a-door-frame1.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=16079"> 
                       Youth fund set to reduce unemployment 
                    </a>
                </h3>
				<!-- show date -->
			   				<!-- show comment -->
								<span class="comment">
					0 <i class="icon-comment"></i>				</span>
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
                <div class="vina-post-extra">
            <!-- show readmore -->
                    </div>
            </li>
    </ul>
<div style="clear:both; width:100%; height:2px;"></div>
<div class="tcvn-link-item-post">
        <ul class="tcvn-menu-post" style="position: static">
                <li class="tcvn-menu-item-post" style="width:100%;">
			<a href="https://www.daily-mail.co.zm/?p=15980">Buseko market needs proper sanitation facilities</a>				
					</li>
                <li class="tcvn-menu-item-post" style="width:100%;">
			<a href="https://www.daily-mail.co.zm/?p=15910">Farming critical to development</a>				
					</li>
                <li class="tcvn-menu-item-post" style="width:100%;">
			<a href="https://www.daily-mail.co.zm/?p=15886">Wage Freeze, retirement age review important</a>				
					</li>
                <li class="tcvn-menu-item-post" style="width:100%;">
			<a href="https://www.daily-mail.co.zm/?p=15861">Let’s maintain economic growth</a>				
					</li>
            </ul>
</div>
        <div style="clear:both"></div>
</div>
</div><div id="text-45" class=" sp-widget widget_text"><h3>Silverest Gardens</h3>			<div class="textwidget"><hana-ampersand><script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/hana-flv-player/flowplayer3/example/flowplayer-3.2.6.min.js'></script></hana-ampersand><hana-ampersand><div ><div id='hana_flv_flow3_1' style='display:block;width:360px;height:250px;background-color:#555555;color:#ffffff;padding:0' title="*Video:silverest gardens"></div></div>
<script  type='text/javascript'>
if (typeof g_hanaFlash !== 'undefined' && !g_hanaFlash){
    jQuery('#hana_flv_flow3_1').css( 'padding', '5px' );
	jQuery('#hana_flv_flow3_1').html("<span class='inactive_message' style='display:block'>Sorry, your browser does not support Flash Video Player</span> *Video:silverest gardens");
}else{			
		flowplayer('hana_flv_flow3_1', { src: 'https://www.daily-mail.co.zm/wp-content/plugins/hana-flv-player/flowplayer3/flowplayer-3.2.7.swf', wmode: 'transparent' }, { 
		
			canvas: { backgroundColor: '#000000', backgroundGradient: 'none',},
    		clip:  { 
    			url: 'https://www.daily-mail.co.zm/wp-content/uploads/videos/zdahenan.flv',
        		scaling: 'scale', autoPlay: false, autoBuffering: true 
				,linkUrl: 'http://www.henanguojizambia.com' ,linkWindow: '_blank'  , onFinish : function () { this.seek(0); }  

				
				
			
	        }
	        
	        
		});
}
</script></hana-ampersand></div>
		</div><div id="text-36" class="tab-post sp-widget widget_text">			<div class="textwidget"><ul class="nav nav-tabs" id="myTab">
<li class="active"><a href="#home" data-toggle="tab">LATEST POST</a></li>
<li><a href="#profile" data-toggle="tab">MOST READ</a></li>
</ul>
<div class="tab-content">
<div class="tab-pane active" id="home">

<div id="tcvn-post-widget-recentpost_widget-9" class="tcvn-post-widget">
<ul class="tcvn-menu">
    <li class="event" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=16164">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2015/01/uth-heart.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=16164"> 
                       UTH gets to ‘heart’ of matter 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">January 5, 2015</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
        <li class="odd" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=16161">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2015/01/muwana-wamunyima.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=16161"> 
                       Rufunsa poised for speedy development 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">January 5, 2015</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
        <li class="event" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=16158">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2014/09/media-mic.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=16158"> 
                       Media can perpetuate stereotypes 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">January 5, 2015</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
        <li class="odd" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=16156">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2014/11/ANTHONY-MWENDA-WRITING.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=16156"> 
                       Connecting the dots, check your steps (Part 2) 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">January 5, 2015</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
        <li class="event" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=16154">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2014/10/Readers-Forum-Logo1-2.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=16154"> 
                       Challenges of developing agriculture 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">January 5, 2015</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
    </ul>
<div style="clear:both; width:100%; height:2px;"></div>
    <div style="clear:both"></div>
</div>

</div>
<div class="tab-pane" id="profile">

<div id="tcvn-post-widget-recentpost_widget-2" class="tcvn-post-widget">
<ul class="tcvn-menu">
    <li class="event" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=6193">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2014/10/HOT-SHOTS-MACKY-II-RESA.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=6193"> 
                       Big Brother Africa Hotshots: Macky II, Resa in house 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">October 4, 2014</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
        <li class="odd" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=9313">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2014/09/SATA-CABINET.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=9313"> 
                       President Sata dies 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">October 29, 2014</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
        <li class="event" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=15067">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2014/12/Pjay-Brian-Cheengwa.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=15067"> 
                       P-Jay dies 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">December 22, 2014</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
        <li class="odd" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=11001">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2014/11/INONGE-WINA-EDGAR-LUNGU-BRIDGET-ATANGA-GUY-SCOTT.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=11001"> 
                       Patriotic Front picks Edgar Lungu 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">November 14, 2014</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
        <li class="event" style="width:100%;">   
        <div class="vina-post-introtext">
			            <div class="vina-post-image">
                                <a class="img-box1" href="https://www.daily-mail.co.zm/?p=11780">
                    <img src="https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/timthumb.php?w=80&h=50&a=c&q=99&z=0&src=http://www.daily-mail.co.zm/wp-content/uploads/2014/11/PF-Central-Committee-Guy-Scott.jpg" alt=""/>                </a>
                				
				
				
				<h3 class="vina-title">
                    <a class="vina-title" href="https://www.daily-mail.co.zm/?p=11780"> 
                       PF goes to conference 
                    </a>
                </h3>
				<!-- show date -->
			   			   <i class="icon-calendar"></i> 
			   <span class="vina-date">November 21, 2014</span>
			   				<!-- show comment -->
				            </div>
			
			 <!-- show introtext-->
			         </div>
        <div style="clear:both"></div>
            </li>
    </ul>
<div style="clear:both; width:100%; height:2px;"></div>
    <div style="clear:both"></div>
</div>

</div>
</div></div>
		</div><div id="youtube_responsive-2" class=" sp-widget widget_youtube_responsive"><h3>Zambia &#8211; The Road to Independence with ZAMTEL</h3><iframe id='1' class='StefanoAI-youtube-responsive ' width='160' height='90' src='//www.youtube.com/embed/JKuywBjBKCE?&amp;autohide=2&amp;color=red&amp;controls=1&amp;disablekb=0&amp;fs=1&amp;iv_load_policy=1&amp;loop=0&amp;modestbranding=1&amp;rel=0&amp;showinfo=0&amp;theme=dark&amp;vq=default' frameborder='0' allowfullscreen="true" style=''></iframe></div><div id="text-28" class="center-likebox sp-widget widget_text"><h3>Like box</h3>			<div class="textwidget"><iframe src="//www.facebook.com/plugins/likebox.php?href=https://www.facebook.com/ZAMBIA.DAILY.MAIL&amp;width=300&amp;height=258&amp;colorscheme=light&amp;show_faces=true&amp;header=false&amp;stream=false&amp;show_border=false" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:300px; height:258px;" allowTransparency="true"></iframe>

</div>
		</div><div id="text-44" class=" sp-widget widget_text"><h3>ePaper  App</h3>			<div class="textwidget"><center><img src="wp-content/uploads/jubileee.fw.png" /></center></div>
		</div>                </div>
                						</aside>
											
											<aside id="rightsidebar" class="span3">
							                <div id="sp-position-right">
                    <div id="text-33" class=" sp-widget widget_text">			<div class="textwidget"><br />
<a href="http://www.sbtjapan.com" target="_blank" /><img src="wp-content/uploads/sbt.gif" /></a></div>
		</div><div id="text-14" class=" sp-widget widget_text">			<div class="textwidget"><br />
<a href="http://www.investrustbank.com/" target="_blank"><img src="wp-content/uploads/investrust.fw.png" /></a></div>
		</div><div id="text-34" class="banner right-banner2 hidden-mobile sp-widget widget_text">			<div class="textwidget"><br />
<a href="http://www.moh.gov.zm" target="_blank"/><img src="wp-content/uploads/ebola_270x312.fw.png" /></a></div>
		</div><div id="text-42" class=" sp-widget widget_text">			<div class="textwidget"><br />
<br />
<img src="wp-content/uploads/football_corner.fw.png" /></div>
		</div><div id="archives-2" class=" sp-widget widget_archive"><h3>Archives</h3>		<select name="archive-dropdown" onchange='document.location.href=this.options[this.selectedIndex].value;'> <option value="">Select Month</option> 	<option value='https://www.daily-mail.co.zm/?m=201501'> January 2015 &nbsp;(109)</option>
	<option value='https://www.daily-mail.co.zm/?m=201412'> December 2014 &nbsp;(1224)</option>
	<option value='https://www.daily-mail.co.zm/?m=201411'> November 2014 &nbsp;(1150)</option>
	<option value='https://www.daily-mail.co.zm/?m=201410'> October 2014 &nbsp;(1206)</option>
	<option value='https://www.daily-mail.co.zm/?m=201409'> September 2014 &nbsp;(1227)</option>
	<option value='https://www.daily-mail.co.zm/?m=201408'> August 2014 &nbsp;(724)</option>
	<option value='https://www.daily-mail.co.zm/?m=201407'> July 2014 &nbsp;(2)</option>
	<option value='https://www.daily-mail.co.zm/?m=201406'> June 2014 &nbsp;(5)</option>
	<option value='https://www.daily-mail.co.zm/?m=201405'> May 2014 &nbsp;(2)</option>
	<option value='https://www.daily-mail.co.zm/?m=201403'> March 2014 &nbsp;(1)</option>
	<option value='https://www.daily-mail.co.zm/?m=201309'> September 2013 &nbsp;(168)</option>
	<option value='https://www.daily-mail.co.zm/?m=201308'> August 2013 &nbsp;(36)</option>
	<option value='https://www.daily-mail.co.zm/?m=201306'> June 2013 &nbsp;(1)</option>
	<option value='https://www.daily-mail.co.zm/?m=201302'> February 2013 &nbsp;(3)</option>
 </select>
</div><div id="text-32" class=" sp-widget widget_text">			<div class="textwidget"><br />
<br />
<table>
<tr height="600px">
<td>
<a href="http://www.singaporeautos.net/" target="_blank"/><img src="wp-content/uploads/singapore_auto.fw.png" /></a></td>
<td><img src="wp-content/uploads/side_strip.fw.png" height="600px" width="130px" /></td>
</tr>
</table></div>
		</div>                </div>
                						</aside>
										
				</div>
		</div><!-- #content -->
	</div>
	<img src="wp-content/uploads/bottom_1170x120.fw.png" />
	<!--banner-->
			<section id="sp-banner-wrapper">
			<div class="container">
				<div class="row-fluid">
					                <div id="sp-position-banner">
                    <div id="nav_menu-3" class="menu-category-footer sp-widget widget_nav_menu"><div class="menu-menu-category-footer-container"><ul id="menu-menu-category-footer" class="menu"><li id="menu-item-512" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-512"><a href="https://www.daily-mail.co.zm/?cat=28">Sport</a>
<ul class="sub-menu">
	<li id="menu-item-513" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-513"><a href="https://www.daily-mail.co.zm/?cat=38">Football</a></li>
	<li id="menu-item-514" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-514"><a href="https://www.daily-mail.co.zm/?cat=40">Basketball</a></li>
	<li id="menu-item-515" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-515"><a href="https://www.daily-mail.co.zm/?cat=39">Boxing</a></li>
	<li id="menu-item-516" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-516"><a href="https://www.daily-mail.co.zm/?cat=41">Golf</a></li>
</ul>
</li>
<li id="menu-item-633" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-633"><a href="https://www.daily-mail.co.zm/?cat=63">Features</a>
<ul class="sub-menu">
	<li id="menu-item-634" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-634"><a href="https://www.daily-mail.co.zm/?cat=69">Development</a></li>
	<li id="menu-item-635" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-635"><a href="https://www.daily-mail.co.zm/?cat=67">Columnists</a></li>
	<li id="menu-item-636" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-636"><a href="https://www.daily-mail.co.zm/?cat=64">@50 Jubilee</a></li>
	<li id="menu-item-637" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-637"><a href="https://www.daily-mail.co.zm/?cat=65">Health</a></li>
	<li id="menu-item-638" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-638"><a href="https://www.daily-mail.co.zm/?cat=66">In focus</a></li>
	<li id="menu-item-639" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-639"><a href="https://www.daily-mail.co.zm/?cat=68">Letter to the Editor</a></li>
</ul>
</li>
<li id="menu-item-640" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-640"><a href="https://www.daily-mail.co.zm/?cat=84">Entertainment</a>
<ul class="sub-menu">
	<li id="menu-item-641" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-641"><a href="https://www.daily-mail.co.zm/?cat=89">Books</a></li>
	<li id="menu-item-642" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-642"><a href="https://www.daily-mail.co.zm/?cat=87">Gender</a></li>
	<li id="menu-item-643" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-643"><a href="https://www.daily-mail.co.zm/?cat=85">Movies</a></li>
	<li id="menu-item-644" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-644"><a href="https://www.daily-mail.co.zm/?cat=86">Music</a></li>
	<li id="menu-item-645" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-645"><a href="https://www.daily-mail.co.zm/?cat=90">Theatre</a></li>
	<li id="menu-item-646" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-646"><a href="https://www.daily-mail.co.zm/?cat=88">TV</a></li>
</ul>
</li>
<li id="menu-item-647" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-647"><a href="https://www.daily-mail.co.zm/?cat=77">Business</a>
<ul class="sub-menu">
	<li id="menu-item-648" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-648"><a href="https://www.daily-mail.co.zm/?cat=81">Headlines</a></li>
	<li id="menu-item-650" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-650"><a href="https://www.daily-mail.co.zm/?cat=82">Agri-business</a></li>
	<li id="menu-item-651" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-651"><a href="https://www.daily-mail.co.zm/?cat=83">Local Business</a></li>
	<li id="menu-item-652" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-652"><a href="https://www.daily-mail.co.zm/?cat=78">Editor&#8217;s Choice</a></li>
</ul>
</li>
<li id="menu-item-653" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-653"><a href="https://www.daily-mail.co.zm/?cat=70">Life and Style</a>
<ul class="sub-menu">
	<li id="menu-item-654" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-654"><a href="https://www.daily-mail.co.zm/?cat=71">Fashion and Beauty</a></li>
	<li id="menu-item-655" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-655"><a href="https://www.daily-mail.co.zm/?cat=74">Men&#8217;s Fashion</a></li>
	<li id="menu-item-657" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-657"><a href="https://www.daily-mail.co.zm/?cat=73">Couples</a></li>
	<li id="menu-item-658" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-658"><a href="https://www.daily-mail.co.zm/?cat=75">Gender</a></li>
	<li id="menu-item-659" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-659"><a href="https://www.daily-mail.co.zm/?cat=76">Kid&#8217;s Corner</a></li>
</ul>
</li>
<li id="menu-item-667" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-667"><a href="https://www.daily-mail.co.zm/?cat=98">Technology</a>
<ul class="sub-menu">
	<li id="menu-item-668" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-668"><a href="https://www.daily-mail.co.zm/?cat=102">Business Tech</a></li>
	<li id="menu-item-669" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-669"><a href="https://www.daily-mail.co.zm/?cat=101">Green Tech</a></li>
	<li id="menu-item-670" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-670"><a href="https://www.daily-mail.co.zm/?cat=99">Personal Tech</a></li>
	<li id="menu-item-671" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-671"><a href="https://www.daily-mail.co.zm/?cat=103">Science</a></li>
	<li id="menu-item-672" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-672"><a href="https://www.daily-mail.co.zm/?cat=104">Security</a></li>
	<li id="menu-item-673" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-673"><a href="https://www.daily-mail.co.zm/?cat=100">Space</a></li>
</ul>
</li>
<li id="menu-item-677" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-677"><a href="https://www.daily-mail.co.zm/?cat=96">World</a>
<ul class="sub-menu">
	<li id="menu-item-678" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-678"><a href="https://www.daily-mail.co.zm/?cat=92">Europe</a></li>
	<li id="menu-item-679" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-679"><a href="https://www.daily-mail.co.zm/?cat=93">Middle East</a></li>
	<li id="menu-item-680" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-680"><a href="https://www.daily-mail.co.zm/?cat=97">Pacific</a></li>
	<li id="menu-item-681" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-681"><a href="https://www.daily-mail.co.zm/?cat=94">Science</a></li>
	<li id="menu-item-682" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-682"><a href="https://www.daily-mail.co.zm/?cat=95">U.S. Politics</a></li>
	<li id="menu-item-684" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-684"><a href="https://www.daily-mail.co.zm/?cat=91">News</a></li>
</ul>
</li>
</ul></div></div>                </div>
                				</div>
			</div>
		</section>
	
	<!--bottom-->
	</div>
</section><!-- #sp-main -->

<footer id="sp-footer-wrapper" role="contentinfo">
	<div class="container">
		<div id="sp-footer">
			<div class="row-fluid">
				<div class="span7">
					

<span class="copyright">© 2014 Zambia Daily Mail News . All Rights Reserved.</span>				</div>		
				<div class="span5">
					
	<a class="sp-totop pull-right" href="#" rel="nofollow"><small>Goto top </small>
		<i class="icon-caret-up"></i>
	</a>
					                <div id="sp-position-footer">
                    <div id="nav_menu-2" class=" sp-widget widget_nav_menu"><div class="menu-footer-menu-container"><ul id="menu-footer-menu" class="menu"><li id="menu-item-196" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-196"><a href="#">Privacy Policy</a></li>
<li id="menu-item-197" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-197"><a href="#">Advertise With Us</a></li>
<li id="menu-item-198" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-198"><a href="#">Contact Us</a></li>
</ul></div></div>                </div>
                				</div>
			</div>
		</div>
	</div>
</footer>


<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/tcvn-recentpost-widget/includes/admin/js/jquery.simpletip-1.3.1.js?ver=1.0'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/vina-breaking-news/includes/js/pause.jQuery.js?ver=1.0'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/vina-cslider-widget/includes/admin/js/jquery.simpletip-1.3.1.js?ver=1.0'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-includes/js/jquery/ui/jquery.ui.core.min.js?ver=1.10.3'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-includes/js/jquery/ui/jquery.ui.widget.min.js?ver=1.10.3'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-includes/js/jquery/ui/jquery.ui.tabs.min.js?ver=1.10.3'></script>
<script type='text/javascript' src='https://www.daily-mail.co.zm/wp-content/plugins/vina-cslider-widget/includes/js/jquery-ui-tabs-rotate.js?ver=1.0'></script>
<script type='text/javascript' src='http://code.jquery.com/ui/1.10.3/jquery-ui.js?ver=1.0'></script>
	<!-- Clicky Web Analytics - http://clicky.com, WordPress Plugin by Yoast - https://yoast.com/wordpress/plugins/clicky/ -->
			<script type='text/javascript'>
			function clicky_gc(name) {
				var ca = document.cookie.split(';');
				for (var i in ca) {
					if (ca[i].indexOf(name + '=') != -1) {
						return decodeURIComponent(ca[i].split('=')[1]);
					}
				}
				return '';
			}
			var username_check = clicky_gc('comment_author_3919c1c371de7de5a8aec7bdf9e99be3');
			if (username_check) var clicky_custom_session = {username: username_check};
		</script>
		<script type="text/javascript">
				var clicky = { log : function () { return true;	}, goal: function () { return true;	} };
		var clicky_site_id = 100775605;
		(function () {
			var s = document.createElement('script');s.type = 'text/javascript';s.async = true;s.src = '//static.getclicky.com/js';
			( document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0] ).appendChild(s);
		})();
	</script>
	<noscript><p><img alt="Clicky" width="1" height="1" src="//in.getclicky.com/100775605ns.gif" /></p></noscript>
	<script type="text/javascript">function AI_responsive_widget() {
                        jQuery('iframe.StefanoAI-youtube-responsive').each(function() {
                            var width = jQuery(this).parent().innerWidth();
                            var maxwidth = jQuery(this).css('max-width').replace(/px/, '');
                            var pl = parseInt(jQuery(this).parent().css('padding-left').replace(/px/, ''));
                            var pr = parseInt(jQuery(this).parent().css('padding-right').replace(/px/, ''));
                            width = width - pl - pr;
                            if (maxwidth < width) {
                                width = maxwidth;
                            }
                            jQuery(this).css('width', width + "px");
                            jQuery(this).css('height', width / (16 / 9) + "px");
                        });
                    }
                    if (typeof jQuery !== 'undefined') {
                        jQuery(document).ready(function() {
                            AI_responsive_widget();
                        });
                        jQuery(window).resize(function() {
                            AI_responsive_widget();
                        });
                    }</script><p align="center"><a href="http://www.abc.org.za/" target="_blank"><img src="wp-content/uploads/member-abc.jpg" /></p></a>
<script type="text/javascript">  var _gaq = _gaq || [];  _gaq.push(['_setAccount', 'UA-55210547-1']);  _gaq.push(['_trackPageview']);  (function() {	var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;	ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';	var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);  })();</script>
</body>
</html>
<!-- Performance optimized by W3 Total Cache. Learn more: http://www.w3-edge.com/wordpress-plugins/

Object Caching 5351/5366 objects using disk

 Served from: www.daily-mail.co.zm @ 2015-01-05 16:02:06 by W3 Total Cache -->
"""
        
        doc = Document()
        doc.url = 'https://www.daily-mail.co.zm/?p=16082'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, 'RB weighs in for Lungu')
        self.assertIsNone(doc.summary)
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '05 01 2015')
        self.assertEqual(doc.author, Author.unknown())
        self.assertEqual(doc.medium.name, 'Zambia Daily Mail')

        self.assertEqual(doc.text, u'DARLINGTON MWENDABAI & HOPE NYOKA, Chipata\nFORMER President Rupiah Banda has endorsed Patriotic Front presidential candidate Edgar Lungu for the January 20 presidential election.\nMr Banda described this year as a dawn of new hope where all Zambians should turn up in numbers to vote for Mr Lungu for continuity and stability.\nThe former head of state, who was in a jovial mood, delivered his endorsement speech dubbed \u201cPeace and Unity will deliver Zambia\u201d in Chipata yesterday.\nHe said the country needs stability and continuity, and not a revolution, hence Zambians should elect a leader who has shown the qualities of humility, commitment and unity.\n\u201cFor these reasons, I am appearing before you today to announce my endorsement of Minister of Justice and Defence Edgar Lungu of the PF for president on January 20, 2015,\u201d he said.\nMr Banda said after meeting Mr Lungu to understand his intentions and identify the problems which must be addressed, that he is confident that the PF candidate has qualities the Zambian people need.\nHe said unlike the United Party for National Development (UPND) which is only interested in buying MMD members and asking his son Andrew to insult him on political podiums, Mr Lungu has shown interest to allow peace and unity to prevail in the county.\n\u201cAfter much deliberation, I came to the conclusion that I could not support any candidate that would seek to eliminate or weaken the MMD.  I count many friends among those in the UPND, however, I cannot agree with the approach of poaching individual MMD members to defect to their camp instead of negotiating openly with the whole party,\u201d Mr Banda said.\nHe accused the UPND of trying to drag the country to a one party fiasco and not promoting peace and unity among Zambians.\nMr Banda said he had had many meetings with UPND leaders where they suggested that he should deputise Hakainde Hichilema who had no experience of being republican president.\nMr Banda  urged Mr Lungu if elected to ensure  the costs of basic goods such as mealie meal, fertilizer, fuel and cement are lowered and  the economy is stabilised while a genuine people driven constitution is delivered  and Zambians united.\nHe said the past year had its own challenges where the country witnessed delayed payments for farmers and social divisions but this year, Zambians should vote for Mr Lungu to guide the country for the next 18 months.\nIn accepting the endorsement, Mr Lungu said he was humbled by the gesture and promised the former head of state and Zambians that he will not let them down.\n\u201cOur Late President Sata taught us to embrace all Zambians and we as PF, we do just that. We will work with the MMD who are supporting us and we are going to win the forth coming presidential election because of your support,\u201d he said.\nMr Lungu said he will not sign any social contract with the clergy or anybody but Zambians adding that he delivered as Minister of Justice a final draft constitution without any signed social contracts.\nHe said it does not pay in a multiparty democracy to swallow opposition parties and the PF will instead co-exist with other political parties.\nMr Lungu said the media enjoy press freedom and if elected, he will study the Access to Information Bill.\nEarlier, PF national chairperson Inonge Wina thanked Mr Banda and MMD National Executive Committee members for endorsing Mr Lungu, a gesture she described as rare from a former head of state.\nFormer MMD national secretary Muhabi Lungu said all party structures will support Mr Lungu.')
        

class TestPostZambiaCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = PostZambiaCrawler()

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
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" />
<title>The Post</title>
<style type="text/css">
<!--
body {
	margin-top: 0px;
	margin-bottom: 0px;
	font-family:Arial, Helvetica, sans-serif;
	font-size:12px;
}
.hdln
{
color:#CC0000;
font-family:Arial, Helvetica, sans-serif;
font-size:12px;
font-weight:bold;
}
.blueln
{
color:#006699;
}
.subhead
{
font-family: Arial, Helvetica, sans-serif;
font-size:14px;
color:#000;
}

.subhead-head
{
font-family:Arial, Helvetica, sans-serif;
font-size:14px;
color: #666666;
text-decoration:none;

}
.subhead-head:hover
{
text-decoration:underline;
}

.news-title
{
font-family: Georgia, "Times New Roman", Times, serif;
font-size:16px;
font-weight:500;
color:#003366;
text-decoration:none;
 }
.news-title:hover
{
text-decoration:underline;
}

.news-body
{
font-family: Verdana, Arial, Helvetica, sans-serif;
font-size:11px;
color:#333333

text-decoration:none;
}
 .news-date
{
margin-top:10px;
font-family: Verdana, Arial, Helvetica, sans-serif;
font-size:10px;
color: #999999;

text-decoration:none;
}

.subhead-body
{
font-family:Arial, Helvetica, sans-serif;
font-size:12px;
color: #999999;
}
.inner
{
background: rgba(237,237,237,1);
background: -moz-linear-gradient(top, rgba(237,237,237,1) 0%, rgba(246,246,246,1) 53%, rgba(255,255,255,1) 100%);
background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(237,237,237,1)), color-stop(53%, rgba(246,246,246,1)), color-stop(100%, rgba(255,255,255,1)));
background: -webkit-linear-gradient(top, rgba(237,237,237,1) 0%, rgba(246,246,246,1) 53%, rgba(255,255,255,1) 100%);
background: -o-linear-gradient(top, rgba(237,237,237,1) 0%, rgba(246,246,246,1) 53%, rgba(255,255,255,1) 100%);
background: -ms-linear-gradient(top, rgba(237,237,237,1) 0%, rgba(246,246,246,1) 53%, rgba(255,255,255,1) 100%);
background: linear-gradient(to bottom, rgba(237,237,237,1) 0%, rgba(246,246,246,1) 53%, rgba(255,255,255,1) 100%);
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ededed', endColorstr='#ffffff', GradientType=0 );
border:0px solid #999999;

}

.top-ticker
{
color:#000;
text-decoration:none;
}

.tab-link
{
color:#000;
text-decoration:none;
}
.tab-link:hover
{
text-decoration:underline;
}

.small
{
font-size:12px;}
.normal
{font-size:14px;}
.large
{font-size:16px;}
.large1
{font-size:18px;}
.large2
{font-size:22px;}

.newsbody
{
font-size:15px; font-family: Geneva, Arial, Helvetica, sans-serif; font-weight:normal;
}



.listhead
{
font-family:arial;
font-size:17px;
font-weight:bold;
color: #000000;
text-decoration:none;
}
.list:hover
{
text-decoration:underline;
}

.listbody
{
font-size:14px;
font-family: Geneva, Arial, Helvetica, sans-serif;
font-weight:normal;
text-align:justify;
}


.bclink
{
font-size:12px;
font-family:Arial, Helvetica, sans-serif;
font-weight:bold;
text-decoration:none;
color:#000000;
}
.bclink:hover
{
text-decoration:underline;
}


.tab2link
{
font-size:12px;
font-family:Arial, Helvetica, sans-serif;

text-decoration:none;
color:#000000;
}
.tab2link:hover
{
text-decoration:underline;
}

.vtoplnk
{
font-family:Arial;
font-size:12px;
font-weight:bold;
text-decoration:none;
color:#333333;
padding:2px 5px 2px 5px;
}
.vtoplnk:hover
{
text-decoration:underline;
}
.vftlnk
{
font-family:Arial;
font-size:12px;
font-weight:bold;
text-decoration:none;
color: #0099CC;
padding:2px 5px 2px 5px;
}
.vftlnk:hover
{
color:#999999;
text-decoration:underline;
}
.tdtop
{
border-top:1px solid #CCCCCC ;
}

.tdbt
{
border-bottom:1px solid #CCCCCC ;
}
.nbt
{
border-bottom:1px solid #CCCCCC;
height:115px;
vertical-align: top;
}
.ntp
{
border-top:1px solid #CCCCCC;
height:115px;
vertical-align: top;
}
.ebg
{
background-image:url(images/ebg.png);
background-repeat:repeat-x;
height:65px;
 
}


 div#left-sidebar{
  position:absolute;
  top:0px;
  left:0px;
  width:135px;
   
 
   
 }
 
  div#right-sidebar{
  position:absolute;
  top:0px;
  right:0px;
  width:135px;
     
   
 }
 div#footer{
  position:absolute;
  margin:0;
   
  bottom:0;
  left:0;
  width:100%;
  height:40px;
 }
 @media screen{
  body>div#left-sidebar
  {
   position:fixed;
  }
  body>div#right-sidebar{
   position:fixed;
  }
  body>div#footer{
   position: fixed;
  }
 
  }

-->
</style></head>
 <script src="js/jquery.js" type="text/javascript"></script>
  <link href="css/hdr.css" media="screen" rel="stylesheet" type="text/css" />

<body>
<table width="990" border="0" align="center" cellpadding="0" cellspacing="0">
 
 <!-- <tr>
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td></td>
        <td>&nbsp;</td>
      </tr>
    </table></td>
  </tr>-->
  <tr>
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td height="25" colspan="2" align="center" >
        
        
                <a href="http://www.mtnzambia.com" target="_blank"><img src="mediamanager/files/990x135-01.jpg" width="990" style="border:1px solid #CCCCCC" height="110" /></a>
        		
        
        
        </td>
      </tr>
      <tr>
        <td height="25" colspan="2" align="right" style="border-bottom:1px dotted #999999">
        
            
      <a href="login.php"   class="vtoplnk">Login</a>
      
            
      &nbsp;&nbsp;|&nbsp;&nbsp; <a href="archives.php" class="vtoplnk" >Archives</a> &nbsp;&nbsp;|&nbsp;&nbsp; <a href="cj.php" class="vtoplnk" >Citizen Journalism</a> &nbsp;&nbsp;|&nbsp;&nbsp; <a href="forum/" target="_blank" class="vtoplnk" >Discussion Forum</a> &nbsp;&nbsp;|&nbsp;&nbsp; <a href="msgboard.php" class="vtoplnk" >Message Board</a>
      &nbsp;&nbsp;|&nbsp;&nbsp; <a href="downloads.php" class="vtoplnk" >Downloads</a>   
      &nbsp;&nbsp;|&nbsp;&nbsp; <a href="feedback.php" class="vtoplnk" >Feedback</a>     </td>
        </tr>
      
      
      
       
      
      
      
    </table></td>
  </tr>
  <tr>
    <td style="background-image:url(images/hd-bar.png); background-repeat:repeat-x">
    
	
		
	
    <table width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="#2E3192"  style="border-bottom:2px solid #FFFFFF" >
      <tr>
        <td width="48%" height="126" align="center" valign="middle"> 
        
       <div id="mlogo">
        <a href="index.php"><img src='images/postlogo.png'  border='0'    /></a>
                 </div>
        
        
        </td>
        <td width="52%" align="center">
        
                <a href="http://www.japantradecar.com/" target="_blank">
        <img src="mediamanager/files/Cars_from_USD_80_Grey_475x100_V2.gif" width="475" style="border:1px solid #CCCCCC" height="100" />        </a>
        

         
        
                </td>
      </tr>
    </table>    </td>
  </tr>
  <tr>
    <td>
     
<link href="css/ldropdown-menu.css" media="screen" rel="stylesheet" type="text/css" />
 <script src="js/jquery.js" type="text/javascript"></script>


 


<ul id="navigation" class="nav-main">
	<li><a href="index.php">
            <img  border="0" title="" alt="" src="images/home-icon.png"></a></li>
    
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=70" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Home News</a>
     	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=2" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">World</a>
     	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=3" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Business</a>
     	
		<div>
     <div style="width:100px; float:left; border-right:1px solid #CCCCCC; margin-top:10px; margin-bottom:10px;">
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=105" onmouseover="javascript:show_submenu('submenu105','container3');" style="color:#000000; border-bottom:1px solid #F3F3F3">Financial Times</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu105" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=4434" style="font-size:15px; color:#000000">Anger and dismay as Russia scraps $50bn gas plan </a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3812" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Hedge funds pursue  alternative lending</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3811" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Strauss-Kahn investing firm collapses after apparent suicide of key partner</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3810" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Tech groups aiding  terror - UK spy chief</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3665" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Chinese renminbi’s place in the FX world</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=21" onmouseover="javascript:show_submenu('submenu21','container3');" style="color:#000000; border-bottom:1px solid #F3F3F3">Tourism</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu21" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/ARTITSTS-6564.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=2609" style="font-size:15px; color:#000000">ZAM calls on musicians  to aid tourism in Luapula</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=868" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Kasama airport upgrade will attract tourism - Nkunika</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=61" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">GOVT SEEKS MORE LOCAL PARTICIPANTS IN TOURISM</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
    	 </div>
    
    <div id="container3" style="width:340px; float:right; height:auto; background-color: #F5F5F5 ;border:0px solid #FFFFFF;">
   
  </div>
	</div>
	
	    
    </li>
      
   
   
    <li>
    
       <a href="sports.php">Sports</a>
    	
		<div>
     <div style="width:100px; float:left; border-right:1px solid #CCCCCC; margin-top:10px; margin-bottom:10px;">
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=18" onmouseover="javascript:show_submenu('submenu18','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Athletics</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu18" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/Samuel Matete.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=5044" style="font-size:15px; color:#000000">Mpondela team asks court to throw out Matete injunction</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4781" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Mpondela shouldn’t think ZAAA is his </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4519" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Zambian athletes  reach finals in Zim</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4382" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Kubombela opts not to  re-contest ZAAA position </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4374" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Mokola urges women to take  up leadership roles in sports</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=97" onmouseover="javascript:show_submenu('submenu97','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Badminton</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu97" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/badminton.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=1215" style="font-size:15px; color:#000000">Teen badminton  player reaps  gold, silver </a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=88" onmouseover="javascript:show_submenu('submenu88','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Basketball</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu88" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/basketball.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=4742" style="font-size:15px; color:#000000">Bullets keep dream of winning alive</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3799" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Zambia  to miss  Zone Six  basketball games</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3421" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">ZBA seeks K115,000 for Afrobasket qualifiers </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3205" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Kalipinde a doubt for Afrobasket qualifiers</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3130" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Spartans back in the hunt for top-four slot</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=100" onmouseover="javascript:show_submenu('submenu100','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Boxing</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu100" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/Esther Phiri relaxing.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=5130" style="font-size:15px; color:#000000">Give Esther more fights before going for a title - Chingangu</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=5058" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Esther returns to ring in April</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4518" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Esther thanks Mugabe for recognition</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4372" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">ZPBWCB clears Mwamba</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4217" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Bring quality boxers - Chilambe</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=91" onmouseover="javascript:show_submenu('submenu91','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Chess</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu91" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/akayom.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=4914" style="font-size:15px; color:#000000">Chess players need more exposure - Kayonde </a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4849" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Chola takes on SA’s Keegan </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4784" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Epah gains WIM title</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4736" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Epah finishes second at Africa Individual Chess Championships </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4626" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Epah confident of \'conquering\' Africa</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=13" onmouseover="javascript:show_submenu('submenu13','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Cricket</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu13" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=76" style="font-size:15px; color:#000000">world cup 2003</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=31" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Testing</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=103" onmouseover="javascript:show_submenu('submenu103','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Darts</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu103" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/darts-zambia.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=2369" style="font-size:15px; color:#000000">DAZ bemoans erratic payment of fees</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=39" onmouseover="javascript:show_submenu('submenu39','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Football</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu39" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/Kalaba new chipolopolo captain.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=5176" style="font-size:15px; color:#000000">Kalaba deserves to be captain - Chambeshi</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=5171" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Criticising Sunzu’s China move petty - Kilambe </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=5170" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Chipolopolo in Bafana Bafana test </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=5132" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Mpika Utd win Miles Sampa Christmas tournament</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=5109" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Mashaba names AfCON-bound team</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=106" onmouseover="javascript:show_submenu('submenu106','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">General</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu106" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=4376" style="font-size:15px; color:#000000">S/Africa to bid for 2024 Olympics</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3752" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Paljk aims for gold </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3073" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">NSCZ calls for  accountability</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=99" onmouseover="javascript:show_submenu('submenu99','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Golf</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu99" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=4741" style="font-size:15px; color:#000000">Norman salutes Nagle on 94th birthday</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3945" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Masisani seeks to lead ZLGU</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3301" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Barclays Life wins IAZ golf meet</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3016" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Zambia Open gets richer </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=2877" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Teenager Walya  targets PGA tour </a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=93" onmouseover="javascript:show_submenu('submenu93','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Handball</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu93" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=3420" style="font-size:15px; color:#000000">AHC suspends qualifiers over Ebola</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=2969" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">HAZ to  hold jubilee  championship </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=1326" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Lack of exposure cost  Zambia - handball coach</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=1164" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Handball Coach targets IHF finals</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=1078" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Handball teams in Zambia for Africa Challenge Trophy</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=92" onmouseover="javascript:show_submenu('submenu92','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Hockey</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu92" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=925" style="font-size:15px; color:#000000"></a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=17" onmouseover="javascript:show_submenu('submenu17','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Judokas</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu17" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/Judo-in-Zambia-51.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=3803" style="font-size:15px; color:#000000">Banda out of Region 5 judo games</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3620" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Mangaba must step down to retain respect </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3013" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Police promote Punza, Olga </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=2084" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">‘Zambia will be judo powerhouse’</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=1943" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">ZaMAA to honour fallen  heroes </a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=95" onmouseover="javascript:show_submenu('submenu95','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Motor Sports</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu95" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/Reeve David.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=5105" style="font-size:15px; color:#000000">Reeve ready for Dakar rally</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4917" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Reeve to ‘navigate’ Dakar Rally with caution</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=4223" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Jassy wins national rally </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3800" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Essa eyes Madagascar win</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3695" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Zambia is retaining  title - Essa</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=98" onmouseover="javascript:show_submenu('submenu98','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Netball</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu98" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/Netball National Team.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=5060" style="font-size:15px; color:#000000">NAZ names provisional World Cup team</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3387" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Chilonga win Kapeya final</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3269" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Kapeya tournament finals set for today</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3075" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Pound Stretcher netball  crown goes to John Laing </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3012" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Netball team to have expatriate coach </a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=96" onmouseover="javascript:show_submenu('submenu96','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Polo</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu96" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=1134" style="font-size:15px; color:#000000">Polo ladies beat Kenya</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=94" onmouseover="javascript:show_submenu('submenu94','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Pool</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu94" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/Pool-Game-Wallpapers6.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=3077" style="font-size:15px; color:#000000">Zambia’s pool team fails to  retain BlackBall championship</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=2915" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Pool team in Dar </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=1212" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Pool body warns indisciplined players</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=1131" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Great Mumana win national pool crown</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=104" onmouseover="javascript:show_submenu('submenu104','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Renault</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu104" style="display:none;">
                      
                                             
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=101" onmouseover="javascript:show_submenu('submenu101','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Rugby</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu101" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/Rugby Zambia.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=5011" style="font-size:15px; color:#000000">Diggers need to work hard next season - Mutale</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3656" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Chanda free to appeal - ZRU</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3302" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Chanda insists ZRU nominations still valid </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3088" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Sinkamba, Mwale in race for ZRU top slot</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=2965" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">ZRU puts off Super Eight Cup </a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=89" onmouseover="javascript:show_submenu('submenu89','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Tennis</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu89" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/EDGAR-Kazembe-.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=5131" style="font-size:15px; color:#000000">MiB Security sets aside K190,000 for Kazembe’s international games</a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=5100" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Wrist injury rules  Del Potro out of  Brisbane event</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3692" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Manda, Kalengo ready to retain Malawi Open </a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3621" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Golden Key donates  K2,000 for squash team’s Malawi trip</a></div> <br />
									  
									
									  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=3422" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">Banda wins C/belt badminton title</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=102" onmouseover="javascript:show_submenu('submenu102','container4');" style="color:#000000; border-bottom:1px solid #F3F3F3">Volleyball</a>
 
 
 
 
 
 <!--Submenu Code Start-->
     
                      <div id="submenu102" style="display:none;">
                      
                      								                                    <div style="float:left; padding:5px;"><img src="mediamanager/files/Volleyball.jpg" height="70" width="80" /></div>
                                  <div style="float:right; width:240px; padding:5px;">
                                  <a href="news.php?id=5007" style="font-size:15px; color:#000000">ZAVA to establish excellence centres </a>
                                  </div>
                                   <p style="margin-top:10px; float:left">
                                    
                                  								  									 <div style="float:left; width:95%;"> <a href="news.php?id=1768" style="background-image:url(images/arrow.png); background-position:left; background-repeat:no-repeat; padding-left:20px; color:#000000" class="toplnk">ZAVA set for Zone 6 games</a></div> <br />
									  
									
									                         
                      </p>
                      </div>
                              
    
    
    
    
    <!--Submenu Code End-->   
      
      
    	 </div>
    
    <div id="container4" style="width:340px; float:right; height:auto; background-color: #F5F5F5 ;border:0px solid #FFFFFF;">
   
  </div>
	</div>
	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=10" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Entertainment</a>
     	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=29" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Videos</a>
     	
		<div>
     <div style="width:100px; float:left; border-right:1px solid #CCCCCC; margin-top:10px; margin-bottom:10px;">
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=55" onmouseover="javascript:show_submenu('submenu55','container29');" style="color:#000000; border-bottom:1px solid #F3F3F3">Business</a>
 
 
 
 
 
 <!--Submenu Code Start-->
   	
             <div id="submenu55" style="display:none;">
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1012"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/9w4MoDkm_f8/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1011"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/_2VuFR9Qvn8/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1010"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/R9_kv5dnQXU/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1009"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/vKVJ5yvM1bY/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=960"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/JTaPV5LjqVk/1.jpg"  /></a>
              </div>
              
                             
  </p>
  </div>
	
	    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=51" onmouseover="javascript:show_submenu('submenu51','container29');" style="color:#000000; border-bottom:1px solid #F3F3F3">Celebs</a>
 
 
 
 
 
 <!--Submenu Code Start-->
   	
             <div id="submenu51" style="display:none;">
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1016"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/RL4UZXavJY4/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1015"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/PLeeqLg22DFsTeB0mjoAzzVUJnd0lJmb4x/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1014"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/juk9K9l7POw/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1013"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/ItW8o8F0ogk/1.jpg"  /></a>
              </div>
              
                             
  </p>
  </div>
	
	    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=44" onmouseover="javascript:show_submenu('submenu44','container29');" style="color:#000000; border-bottom:1px solid #F3F3F3">Entertainment</a>
 
 
 
 
 
 <!--Submenu Code Start-->
   	
             <div id="submenu44" style="display:none;">
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=961"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/JTaPV5LjqVk/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=538"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/LpZw0RsnhVM/1.jpg"  /></a>
              </div>
              
                             
  </p>
  </div>
	
	    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=52" onmouseover="javascript:show_submenu('submenu52','container29');" style="color:#000000; border-bottom:1px solid #F3F3F3">Lifestyle</a>
 
 
 
 
 
 <!--Submenu Code Start-->
   	
             <div id="submenu52" style="display:none;">
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1019"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/eeslO9hpejk/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1018"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/Aj_5SGdx7Xk/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1017"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/uysaeYjT0WE/1.jpg"  /></a>
              </div>
              
                             
  </p>
  </div>
	
	    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=32" onmouseover="javascript:show_submenu('submenu32','container29');" style="color:#000000; border-bottom:1px solid #F3F3F3">SPORTS</a>
 
 
 
 
 
 <!--Submenu Code Start-->
   	
             <div id="submenu32" style="display:none;">
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1023"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/CGD9xlXNlyc/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1022"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/NRblN58rCPg/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1021"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/B8JNfj2JuNc/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1020"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/UcxYzgtGzYo/1.jpg"  /></a>
              </div>
              
                             
  </p>
  </div>
	
	    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=54" onmouseover="javascript:show_submenu('submenu54','container29');" style="color:#000000; border-bottom:1px solid #F3F3F3">Technology</a>
 
 
 
 
 
 <!--Submenu Code Start-->
   	
             <div id="submenu54" style="display:none;">
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1026"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/wfiaVoshS5A/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1025"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/jH7Um0CD58/1.jpg"  /></a>
              </div>
              
                          
            
              <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
               <a href="news.php?id=1024"> 
               <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="http://i1.ytimg.com/vi/gkIe6MGA8zs/1.jpg"  /></a>
              </div>
              
                             
  </p>
  </div>
	
	    
    
    
    
    
    <!--Submenu Code End-->   
      
      
    	 </div>
    
    <div id="container29" style="width:340px; float:right; height:auto; background-color: #F5F5F5 ;border:0px solid #FFFFFF;">
   
  </div>
	</div>
	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=31" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Photos</a>
     	
		<div>
     <div style="width:100px; float:left; border-right:1px solid #CCCCCC; margin-top:10px; margin-bottom:10px;">
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=60" onmouseover="javascript:show_submenu('submenu60','container31');" style="color:#000000; border-bottom:1px solid #F3F3F3">Awards</a>
 
 
 
 
 
 <!--Submenu Code Start-->
               
            <!--Audio Code Start-->
            
            <div id="submenu60" style="display:none;">
                      
                      								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=1034"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/slap-d-300x300.jpg" height="90" width="120"  /></a>
  </div>
                                    
                                  								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=1032"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/roberto78-300x300.jpg" height="90" width="120"  /></a>
  </div>
                                    
                                  								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=1031"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/mampi.png" height="90" width="120"  /></a>
  </div>
                                    
                                  								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=1030"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/macky2.png" height="90" width="120"  /></a>
  </div>
                                    
                                  								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=1029"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/lulu-hangala-and-tivo-300x300.png" height="90" width="120"  /></a>
  </div>
                                    
                                                         
                      </p>
                      </div>
            
            <!--Audio Code End--->
            
            
			
			
			
			    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=58" onmouseover="javascript:show_submenu('submenu58','container31');" style="color:#000000; border-bottom:1px solid #F3F3F3">Beauty </a>
 
 
 
 
 
 <!--Submenu Code Start-->
               
            <!--Audio Code Start-->
            
            <div id="submenu58" style="display:none;">
                      
                                             
                      </p>
                      </div>
            
            <!--Audio Code End--->
            
            
			
			
			
			    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=57" onmouseover="javascript:show_submenu('submenu57','container31');" style="color:#000000; border-bottom:1px solid #F3F3F3">Celebs</a>
 
 
 
 
 
 <!--Submenu Code Start-->
               
            <!--Audio Code Start-->
            
            <div id="submenu57" style="display:none;">
                      
                      								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=1033"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/salma90-300x300.jpg" height="90" width="120"  /></a>
  </div>
                                    
                                                         
                      </p>
                      </div>
            
            <!--Audio Code End--->
            
            
			
			
			
			    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=64" onmouseover="javascript:show_submenu('submenu64','container31');" style="color:#000000; border-bottom:1px solid #F3F3F3">Events</a>
 
 
 
 
 
 <!--Submenu Code Start-->
               
            <!--Audio Code Start-->
            
            <div id="submenu64" style="display:none;">
                      
                      								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=477"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/mwata-k.jpg" height="90" width="120"  /></a>
  </div>
                                    
                                                         
                      </p>
                      </div>
            
            <!--Audio Code End--->
            
            
			
			
			
			    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=56" onmouseover="javascript:show_submenu('submenu56','container31');" style="color:#000000; border-bottom:1px solid #F3F3F3">Fashion</a>
 
 
 
 
 
 <!--Submenu Code Start-->
               
            <!--Audio Code Start-->
            
            <div id="submenu56" style="display:none;">
                      
                                             
                      </p>
                      </div>
            
            <!--Audio Code End--->
            
            
			
			
			
			    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=62" onmouseover="javascript:show_submenu('submenu62','container31');" style="color:#000000; border-bottom:1px solid #F3F3F3">News</a>
 
 
 
 
 
 <!--Submenu Code Start-->
               
            <!--Audio Code Start-->
            
            <div id="submenu62" style="display:none;">
                      
                      								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=964"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/734389_1549978451894664_1766045864_n.jpg" height="90" width="120"  /></a>
  </div>
                                    
                                  								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=963"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/carson_news.jpg" height="90" width="120"  /></a>
  </div>
                                    
                                  								  
                                    <div style="width:130px; height:100px; margin-right:15px; margin-bottom:15px; float:left">
   <a href="news.php?id=962"> 
   <img style="margin-right:10px;padding:5px 5px 5px 5px; border:1px solid #666;" src="mediamanager/files/2011.07.29-kalusha.jpg" height="90" width="120"  /></a>
  </div>
                                    
                                                         
                      </p>
                      </div>
            
            <!--Audio Code End--->
            
            
			
			
			
			    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=59" onmouseover="javascript:show_submenu('submenu59','container31');" style="color:#000000; border-bottom:1px solid #F3F3F3">Parties</a>
 
 
 
 
 
 <!--Submenu Code Start-->
               
            <!--Audio Code Start-->
            
            <div id="submenu59" style="display:none;">
                      
                                             
                      </p>
                      </div>
            
            <!--Audio Code End--->
            
            
			
			
			
			    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=61" onmouseover="javascript:show_submenu('submenu61','container31');" style="color:#000000; border-bottom:1px solid #F3F3F3">Sports</a>
 
 
 
 
 
 <!--Submenu Code Start-->
               
            <!--Audio Code Start-->
            
            <div id="submenu61" style="display:none;">
                      
                                             
                      </p>
                      </div>
            
            <!--Audio Code End--->
            
            
			
			
			
			    
    
    
    
    
    <!--Submenu Code End-->   
      
      
          
    
     
    <a href="search.php?cmd=subcategory&subcatid=63" onmouseover="javascript:show_submenu('submenu63','container31');" style="color:#000000; border-bottom:1px solid #F3F3F3">Technology</a>
 
 
 
 
 
 <!--Submenu Code Start-->
               
            <!--Audio Code Start-->
            
            <div id="submenu63" style="display:none;">
                      
                                             
                      </p>
                      </div>
            
            <!--Audio Code End--->
            
            
			
			
			
			    
    
    
    
    
    <!--Submenu Code End-->   
      
      
    	 </div>
    
    <div id="container31" style="width:340px; float:right; height:auto; background-color: #F5F5F5 ;border:0px solid #FFFFFF;">
   
  </div>
	</div>
	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=33" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Lifestyle</a>
     	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=38" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Columns</a>
     	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=65" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Court</a>
     	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=67" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Politics</a>
     	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=69" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Health</a>
     	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=16" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Editorial</a>
     	
	    
    </li>
      
   
   
    <li>
    
       <a href="search.php?cmd=category&catid=90" style="text-shadow:2px 1px 3px rgba(10, 10, 10, 1);">Weekend</a>
     	
	    
    </li>
    
     
   
    


   <li><a href="#">Others</a>
      <ul class="nav-sub">
        
    
    <!--<li><a href="search.php?cmd=photos">PHOTOS</a></li>
     <li><a href="search.php?cmd=audio">AUDIOS</a></li>
      <li><a href="search.php?cmd=blogs">BLOGS</a></li>
      -->
             <li><a href="search.php?cmd=category&catid=68">Cartoons</a>
       
       
       <!---subcategory-->
       
      <ul class="nav-sub2">     <li>
         
    <a href="search.php?cmd=subcategory&subcatid=85">Agony</a>
    
     </li>
         <li>
         
    <a href="search.php?cmd=subcategory&subcatid=84">Choklet</a>
    
     </li>
    </ul>       <!---subcate end--->
       
       
       </li>
             <li><a href="search.php?cmd=category&catid=71">Letters</a>
       
       
       <!---subcategory-->
       
      <ul class="nav-sub2">     <li>
         
    <a href="search.php?cmd=subcategory&subcatid=82">Post Bag</a>
    
     </li>
         <li>
         
    <a href="search.php?cmd=subcategory&subcatid=83">Post SMS</a>
    
     </li>
    </ul>       <!---subcate end--->
       
       
       </li>
            </ul>
   
   
   </li>

</ul>

 
<script language="javascript">

function show_submenu(x,y)
{
var f = document.getElementById(x);
      var s = document.getElementById(y);
      s.innerHTML = f.innerHTML;
//var $button = $('#'+x).clone();
 // $('#'+y).html($button);
//document.getElementById(y)="hello";
}
</script>    </td>
  </tr>
  
        
  <tr>
    <td  ><table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-bottom:1px solid #000000">
      <tr>
        <td width="20%"  >  <img src="images/breakingnews.jpg" width="199" height="38" />        </td>
        <td width="57%"  ><script type="text/javascript">
<!--
var tickercontent=new Array();
tickercontent[0]="<a class='top-ticker' href='news.php?id=4478'></a>";tickercontent[1]="<a class='top-ticker' href='news.php?id='></a>";tickercontent[2]="<a class='top-ticker' href='news.php?id='></a>";tickercontent[3]="<a class='top-ticker' href='news.php?id='></a>";tickercontent[4]="<a class='top-ticker' href='news.php?id='></a>";
//-->
</script>
</head>

 
 
<script type="text/javascript">
<!--
// Â© copyright 2009 - MRE Software / Author: Emery Wooten / www.mresoftware.com
var pause = false; // Boolean to trigger pause on mouseover event
var t1,t2,t3; // Timer ID variables.
var icnt = 0; // Outside loop counter
var currentChar=1; //Inside loop counter and pointer into characters of the lines.

// Write the forward and back arrows that allow the user to jump ahead and back.
//document.write('<img title="Previous" border="0" src="images/left.gif" onClick = "backup();" OnmouseOver="this.style.cursor=\'pointer\';">');
//document.write('<img title="Next" border="0" src="images/right.gif" onClick = "forward();" OnmouseOver="this.style.cursor=\'pointer\';">');

// The next code writes the div tag on the page complete with mouseover code.
document.write("<span id=\'tick1\' OnMouseOver=\'pause=tru</spannMouseOut=\'pause=false; t3=setTimeout(\"type()\",2000);\'></span>");

//
function backup(){
if (tickercontent.length > 1){
	icnt = icnt-2;
	if (icnt <  0){icnt = tickercontent.length + icnt;}
	type();
	}
}
function forward(){
icnt = icnt++;
if (icnt >= tickercontent.length){icnt = 0;}
type();
}

function type(){
clearTimeout(t1); //clear all timing
clearTimeout(t2); //clear all timing
clearTimeout(t3); //clear all timing

// The next code checks for mouseover pause and completes the line instantly if true.
if(pause && currentChar==1){return;}
else if (pause){currentChar=tickercontent[icnt].length-1;}

// The next code fast fills html tags by rapidly moving to the closing >.
if(tickercontent[icnt].charAt(currentChar-1)=='<'){
	while (tickercontent[icnt].charAt(currentChar-1)!='>'){
		currentChar++;
		if (currentChar>tickercontent[icnt].length){
		tickercontent[icnt]=tickercontent[icnt]+'>'; // correct for missing > overflow condition
		currentChar--;
		}
	}
}
// The next code types the textual part of the line and indexes to the next line
      document.getElementById('tick1').innerHTML=tickercontent[icnt].substr(0, currentChar);
      currentChar++
      if (currentChar>tickercontent[icnt].length)  // Are we at the last character in the line?
      {
        icnt++;
        if (icnt >= tickercontent.length){  // Are we at the last line in the array?
        icnt=0;
        }
        currentChar=1;
        t1=setTimeout("type()", 4400);  // This is the pause between lines in ms   
      }
      else
      {
     pause=false; 
     t2=setTimeout("type()", 10);  // This is the pause between typed characters in ms
      }
}
//
type();  // This runs it!
//-->
</script>
  </td>
        <td width="23%"  ><table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td>&nbsp;</td>
            <form name="frmsrch" method="post" action="search.php?cmd=search">
            <td align="right"><input type="text" name="sstr" style="border:2px solid #E5E5E5  ;border-radius:5px; padding:5px;" id="sstr" onclick="this.value='';" value="Search.." /></td>
            <td><img src="images/srch.png" width="29" height="27" onclick="document.frmsrch.submit();" /></td>
            </form>
          </tr>
        </table></td>
      </tr>
    </table></td>
  </tr>
  </table>

<style type="text/css">

.qttxt-left
{
border:2px solid #333333;
padding:5px;
width:200px;
margin:2px 5px 2px 0px;
font-size:16px;
color:#333333;
font-family: Georgia, "Times New Roman", Times, serif;
text-align:justify;
float:left;
border-top:8px solid #666666;
background-color:#F2F2F2;
}


.qttxt-right
{
border:2px solid #333333;
padding:5px;
width:200px;
margin:2px 0px 2px 5px;
font-size:16px;
color:#333333;
font-family: Georgia, "Times New Roman", Times, serif;
text-align:justify;
float:right;
border-top:8px solid #666666;
background-color:#F2F2F2;
}

</style>
 <link rel="stylesheet" type="text/css" href="js/thickbox.css" />
<script type='text/javascript' src="js/jquery.js"></script>
<script type='text/javascript' src="js/thickbox.js"></script>
<script language="javascript">
	$(document).ready(function()
	{
		 
		tb_init('a.thickbox, area.thickbox, input.thickbox');//pass where to apply thickbox

	imgLoader = new Image();// preload image

	imgLoader.src = tb_pathToImage;
	
	});
</script><table width="990" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td><table width="100%" height="21" border="0" cellpadding="2" cellspacing="0">
      <tr>
        <td height="21" align="left"   valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="7">
          
          <tr>
            <td height="33"><table width="100%" border="0" cellspacing="0" cellpadding="4">
              <tr>
                <td width="58%">You are here: <strong>Home</strong>&nbsp;&nbsp;&gt;&nbsp;&nbsp;<strong>Politics</strong></td>
                <td width="12%" align="center"> 
<script language="javascript">

var postid;
postid=5177
</script> 
 
 <script src="rating/starrating.js" type="text/javascript"></script>
<link href="rating/starrating.css" rel="stylesheet" type="text/css" media="screen" />
 
<ul class='star-rating'>
  <li class="current-rating" id="current-rating"><!-- will show current rating --></li>
  <span id="ratelinks">
  <li><a href="javascript:void(0)" title="1 star out of 5" class="one-star">1</a></li>
  <li><a href="javascript:void(0)" title="2 stars out of 5" class="two-stars">2</a></li>
  <li><a href="javascript:void(0)" title="3 stars out of 5" class="three-stars">3</a></li>
  <li><a href="javascript:void(0)" title="4 stars out of 5" class="four-stars">4</a></li>
  <li><a href="javascript:void(0)" title="5 stars out of 5" class="five-stars">5</a></li>
  </span>
</ul>
 </td>
                </tr>
            </table></td>
          </tr>
          
          <tr>
            <td height="52"><span style="font-size:28px; font-family: Geneva, Arial, Helvetica, sans-serif; font-weight:bold;">
            The race is tight - Simuusa            
            </span></td>
          </tr>
          
          <tr>
            <td height="30" align="left" valign="bottom">
             <span style="float:left">
                    By <strong style="color:#006699">Tilyenji Mwanza</strong>
             &nbsp;&nbsp;|&nbsp;&nbsp;
             Updated: 05 Jan,2015 ,12:53:17              &nbsp;&nbsp;|&nbsp;&nbsp;
              1262 Views
             &nbsp;&nbsp;|&nbsp;&nbsp;
              0 Comments             </span>
            
            
            <span style="float:right">
            <a class="top-ticker" href="javascript:fminus();">[ - ]</a> <a href="#" class="top-ticker" > </a> <a class="top-ticker"  href="javascript:fplus();">[ + ]</a>            </span>            </td>
          </tr>
          <tr>
            <td height="30" align="left" valign="bottom"><table style="border-top:1px solid #999999;background-color:#F0F0F0" width="100%" border="0" cellspacing="0" cellpadding="4" >
              <tr>
                <td valign="bottom">
                
                <iframe src="http://www.facebook.com/plugins/like.php?href=http://postzambia.com/news.php?id=5177&layout=standard&amp;show_faces=false&amp;width=450&amp;action=like&amp;colorscheme=light" scrolling="no" frameborder="0" allowtransparency="true" style="border:none; overflow:hidden; width:300px; height:30px;"></iframe>
                
                
                
                </td>
                <td width="4%" align="center"></td>
                <td width="5%" align="right"><img src="images/mail.png" border="0" /></td>
                <td width="6%" align="left">
                
                <a href="email.php?newsid=5177&TB_iframe=true&keepthis=true&width=230&height=170" title="Email this article" class="thickbox vtoplnk" target="_blank">Mail</a>
                
                
                
                </td>
                <td width="4%" align="center">&nbsp;</td>
                <td width="5%" align="right"><img src="images/printer.png" border="0" /></td>
                <td width="6%" align="left"><a href="print.php?id=5177" class="vtoplnk" target="_blank">Print</a></td>
                <td width="4%" align="right">&nbsp;</td>
                <td width="5%" align="right"><img src="images/rss.png" border="0" /></td>
                <td width="6%" align="left"><a href="rss.php?id=5177" class="vtoplnk" target="_blank">RSS</a></td>
              </tr>
              <tr>
                <td colspan="10" bgcolor="#FFFFFF">
                
                <script type="text/javascript" src="http://w.sharethis.com/button/buttons.js"></script>
<script type="text/javascript">stLight.options({publisher: "7697132a-81a9-4f2e-95fb-2e2df8984c84", doNotHash: false, doNotCopy: false, hashAddressBar: false});</script>

<span class='st_facebook_hcount' displayText='Facebook'></span>
<span class='st_twitter_hcount' displayText='Tweet'></span>
<span class='st_linkedin_hcount' displayText='LinkedIn'></span>
<span class='st_pinterest_hcount' displayText='Pinterest'></span>                
                </td>
                </tr>
            </table></td>
          </tr>
          <tr>
            <td align="right"></td>
          </tr>
          <tr>
            <td>
            
                        
                        <div>
            
                        <div style="width:220px; height:auto;border:1px solid #CCCCCC; float:left; margin-right:10px; color: #888; margin-bottom:10px;">
             <a  href="mediamanager/files/Maureen Mwanawasa Rally.jpg" title="" class="thickbox"><img src="mediamanager/files/Maureen Mwanawasa Rally.jpg"   width="220" height="220" title="Click on Image Enlarge"    /></a> <div style="margin-top:5px;"></div></div>
            			
            
            <div align="justify" id="newsbody" class="newsbody" >
              <p>WYLBUR Simuusa says the January 20 presidential race is tight and the PF needs the input of every member to win the election.</p>

<p>Reacting to Chishimba Kambwili’s remark that Geoffrey Mwamba was limited in thinking because of his low levels of education following the latter’s decision to support the UPND, Simuusa said the Patriotic Front cannot afford to lose its top leaders.</p>

<p>He said it was wrong for anyone in the PF to issue disparaging remarks against Sylvia Masebo and Mwamba simply because they have resolved to support the UPND.</p>

<p>“We need everybody, although I was very categorical on Guy Scott. And at one point, I said we need GBM and now I say we need Masebo too. We have a history with Sylvia and with GBM; we need those votes. And what we should be doing is not disparaging them. We should not disparage GBM and Masebo. We as PF may not agree, but insulting them and belittling them is not the way to go,” said Simuusa, who is agriculture minister and Nchanga PF member of parliament.</p>

<p>He said it would be naïve and untrue to say Mwamba and Masebo are not political factors just because they have chosen a different path.</p>

<p>“We need everyone. GBM has his following and it is a following that was developed with the PF. We as the PF need to work on reconciliation and realise that everybody matters, even Masebo. We worked with them before and they helped deliver PF, so it is unfair to say they do not matter, or begin to issue disparaging remarks,” Simuusa said.</p>

<p>He said UPND and other parties were campaigning hard and it would be unwise for PF to keep losing its members.</p>

<p>Simuusa called on PF leaders to instead find ways of recalling Mwamba and Masebo rather than pretend that the two are not a factor.</p>

<p>“The approach should be to take the colleagues of ours and see how we can keep them in the spirit of reconciliation. Disparaging them, calling them opportunists is not right,” said Simuusa.</p>

<p>Speaking in Matero on New Year’s Day, PF presidential candidate Edgar Lungu described Masebo as an opportunist who jumps at every opportunity she considers viable.</p>

<p>He added that Masebo was not a political factor as she had no following in Lusaka or Zambia at large.</p>
            </div>
            </div>            </td>
          </tr>
          <tr>
            <td><table width="100%" border="0" cellpadding="6">
              <tr>
                <td colspan="2" style="border-bottom:2px solid #666666;">Related Stories</td>
                </tr>
                


              <tr>
                <td width="88%">&nbsp;</td>
                <td width="12%">&nbsp;</td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <td>
            
            <form name="frmcom" id="frmcom"  action="news.php?id=5177&cmd=postcom" method="post"> 
            
            
            <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" bordercolor="#CCCC99">
  <tr>
    <td colspan="2" style="border-bottom:3px solid #2B3A3F" valign="top"><img src="images/comments.jpg"  /></td>
    </tr>
  <tr>
    <td width="131"   align="left" valign="middle">Name</td>
    <td width="347" valign="middle"><label>
      <input type="text" name="name" id="name" />
    </label></td>
  </tr>
  <tr>
    <td  align="left" valign="middle">Email</td>
    <td valign="middle"><input type="text" name="email" id="email" /></td>
  </tr>
  <tr>
    <td   align="left" valign="middle">Comments</td>
    <td valign="middle"><textarea name="comments" id="comments" cols="45" rows="5"></textarea></td>
  </tr>
  <tr>
    <td height="35" align="left" valign="middle">Enter Characters</td>
    <td><span style="margin-left:120px;">
      <script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6Ldvje4SAAAAAAar8pgZ9Vm6sGHVvX4PmwgbHIYA"></script>

	<noscript>
  		<iframe src="http://www.google.com/recaptcha/api/noscript?k=6Ldvje4SAAAAAAar8pgZ9Vm6sGHVvX4PmwgbHIYA" height="300" width="500" frameborder="0"></iframe><br/>
  		<textarea name="recaptcha_challenge_field" rows="3" cols="40"></textarea>
  		<input type="hidden" name="recaptcha_response_field" value="manual_challenge"/>
	</noscript>    </span></td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td><input type="submit" name="button" id="button" class="button" value="Submit"   /></td>
  </tr>
</table>
</form>            </td>
          </tr>
          <tr>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <td><img src="images/combar.jpg" width="625" height="39" /></td>
          </tr>
          <tr>
            <td>
            
            
                        </td>
          </tr>
        </table></td>
        <td width="212" valign="top"  ><table width="100%" border="0" cellspacing="0" cellpadding="4">
          <tr>
            <td>
            
			
                        <a href="www.pressdisplay.com/pressdisplay/viewer.aspx" target="_blank"><img src="mediamanager/files/6653_backpage.jpg"  width="285" />
            </a>
         
  
 <br />
 
             <br />
<b>Warning</b>:  Invalid argument supplied for foreach() in <b>/home/newpost/public_html/news.php</b> on line <b>427</b><br />
            <a href="" target="_blank"><img src=""  width="285" />
            </a>
         
  
 <br />
 
                         <a href="http://www.pressdisplay.com/pressdisplay/viewer.aspx" target="_blank"><img src="mediamanager/files/6652 Sun Life pdf.jpg"  width="285" />
            </a>
         
  
 <br />
 
                         <a href="" target="_blank"><img src="mediamanager/files/Agony 1.png"  width="285" />
            </a>
         
  
 <br />
 
                         <a href="" target="_blank"><img src="mediamanager/files/6594agony.jpg"  width="285" />
            </a>
         
  
 <br />
 
 
            
            
            
            </td>
          </tr>
          
          <tr>
            <td>&nbsp;</td>
          </tr>
        </table></td>
      </tr>
    </table></td>
  </tr>
  <tr>
    <td>&nbsp;</td>
  </tr>
  
  

  <!--block 2-->
  
  <!--block 2 ends-->
  
  
  
  
  <!--block 3-->
  
  <!--block 3 ends-->
  
  
  
  
   <!--block 4-->
  
  <!--block 4 ends-->
  <tr>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><style>

.fthd
{
font-family:Georgia, "Times New Roman", Times, serif;
font-size:14px;
color:#ffffff;
}

</style>

<table width="990" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td><table width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="#FFFFFF">
      
      <tr>
        <td colspan="2" align="center" style="border-bottom:1px solid #CCCCCC"><table width="100%" height="215" border="0" cellpadding="4" cellspacing="15" bgcolor="#000000">
          <tr>
            <td width="25%" height="32" class="tdbt"><span class="fthd">RECENTS COMMENTS</span></td>
            <td width="25%" class="tdbt"><span class="fthd">LATEST TWEETS</span></td>
            <td width="25%" class="tdbt"><span class="fthd">GROUP</span></td>
            <td width="25%" class="tdbt"><span class="fthd">RECENT PHOTOS</span></td>
          </tr>
          <tr>
            <td align="left" valign="top">


<table width="100%" border="0" cellpadding="4" cellspacing="0" bgcolor="#000000">
  <tr>
    <td width="4%"><img src="images/comment-icon.png"   /></td>
    <td width="96%" align="left" valign="top">
    
    <a  href="news.php?id=3358&#com416" style="color:#CCCCCC; text-decoration:none" title="After 50 years of the jubilee, some people are  still frustrating Government project, how can a country progress. These are the same people complaining that PF Government is not doing anything and yet they are the ones frustrating projects that could have employed several hundreds of Zambians. Please the minister of Commerce and other Government officials look into this matter and such person must be invistaged." ><strong>Joe Mwamba</strong> : After 50 years of th    </a> <br />   </td>
  </tr>
</table>



<table width="100%" border="0" cellpadding="4" cellspacing="0" bgcolor="#000000">
  <tr>
    <td width="4%"><img src="images/comment-icon.png"   /></td>
    <td width="96%" align="left" valign="top">
    
    <a  href="news.php?id=616&#com86" style="color:#CCCCCC; text-decoration:none" title="HELLO BA MPOMBO YOU INSPIRE ME WITH YOUR ENGLISH WORDS BUT BEEN A PRESIDENT OF A POLITICAL PARTY YOUR A JOKE.FORGET ABOUT IT POLITIC AND TEACH ENGLISH ZAMBIANS NEW GENERATION LIKE ME ONLY 21YRS" ><strong>GIDEON( AGOGO) TEMBO</strong> : HELLO BA MPOMBO YOU     </a> <br />   </td>
  </tr>
</table>



<table width="100%" border="0" cellpadding="4" cellspacing="0" bgcolor="#000000">
  <tr>
    <td width="4%"><img src="images/comment-icon.png"   /></td>
    <td width="96%" align="left" valign="top">
    
    <a  href="news.php?id=669&#com85" style="color:#CCCCCC; text-decoration:none" title="GOVT SHOULD ENSURE THAT THE DEAD ARE IN  ANYWAY BE RESPECTED BY PROVIDING GOOD COOLLING SYSTEMS THAT WILL NOT DAMAGE BODIES BEFORE BEEN COLLECTE BY RELATIVES.GOOD JOB BA MWANGO C." ><strong>GIDEON( AGOGO) TEMBO</strong> : GOVT SHOULD ENSURE T    </a> <br />   </td>
  </tr>
</table>



<table width="100%" border="0" cellpadding="4" cellspacing="0" bgcolor="#000000">
  <tr>
    <td width="4%"><img src="images/comment-icon.png"   /></td>
    <td width="96%" align="left" valign="top">
    
    <a  href="news.php?id=996&#com84" style="color:#CCCCCC; text-decoration:none" title="H H needs anger management" ><strong>Fred</strong> : H H needs anger mana    </a> <br />   </td>
  </tr>
</table>



<table width="100%" border="0" cellpadding="4" cellspacing="0" bgcolor="#000000">
  <tr>
    <td width="4%"><img src="images/comment-icon.png"   /></td>
    <td width="96%" align="left" valign="top">
    
    <a  href="news.php?id=1008&#com83" style="color:#CCCCCC; text-decoration:none" title="This is incompetence Minister Edger lungu. You should have had meetings with the board either weekly, biweekly or monthly to guide them on what you expected. This is village politicking. That report is for the taxpayers and not you." ><strong>Zamule</strong> : This is incompetence    </a> <br />   </td>
  </tr>
</table>
</td>
            <td align="left" valign="top"><a class="twitter-timeline" href="https://twitter.com/PostNewsZambia" data-widget-id="483612938641489920">Tweets by @PostNewsZambia</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script></td>
            <td align="left" valign="top"><img src="gpimg.png" width="235" height="357" border="0" usemap="#Map" /></td>
            <td align="left" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="4">
  
  <tr>  
  
    <td>
     
    <a href="news.php?id=3833"   ><img src="mediamanager/files/Bobby East and Ruth.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=1080"   ><img src="mediamanager/files/kazonga.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=1049"   ><img src="mediamanager/files/MUGABE.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
  </tr><tr>  
  
    <td>
     
    <a href="news.php?id=1044"   ><img src="mediamanager/files/energy.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=1043"   ><img src="mediamanager/files/Kunda-H.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=1040"   ><img src="mediamanager/files/pande.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
  </tr><tr>  
  
    <td>
     
    <a href="news.php?id=1039"   ><img src="mediamanager/files/zanaco-building-570x270.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=1038"   ><img src="mediamanager/files/anamel.JPG" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=1037"   ><img src="mediamanager/files/chenda.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
  </tr><tr>  
  
    <td>
     
    <a href="news.php?id=936"   ><img src="mediamanager/files/Earthmoving-Equipment.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=900"   ><img src="mediamanager/files/afghan govt.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=897"   ><img src="mediamanager/files/Marina_Silva_2007.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
  </tr><tr>  
  
    <td>
     
    <a href="news.php?id=896"   ><img src="mediamanager/files/oldies9.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=895"   ><img src="mediamanager/files/malama.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
    
  
    <td>
     
    <a href="news.php?id=894"   ><img src="mediamanager/files/hippofeed-01.jpg" width="70" height="60" /></a>    
    </td>
    
   
   
  </tr></table>
</td>
          </tr>
        </table></td>
        </tr>
      
      <tr>
        <td height="59" colspan="2" align="center" valign="middle" bgcolor="#333333"><span style="color:#ffffff"> For advertising, queries and enquiries please contact <a href="mailto:webmaster@postzambia.com" style="color:#FFF">webmaster@postzambia.com</a> <br />&copy;1991 - 2014 Post Newspapers Ltd. All rights reserved. POST NEWSPAPERS is not responsible for the content of external sites. <a href="terms.php"  style="color:#CCCCCC">Read more</a><br />
         <!-- Website designed &amp; maintained by <a href="http://uniaxialsoftware.com" style="color: #3399CC" target="_blank">Uniaxial Software.</a></span>
         -->
         
         </td>
        </tr>
      
    </table></td>
  </tr>
</table>

<map name="Map" id="Map"><area shape="rect" coords="6,8,227,86" target="_blank" href="http://www.postsangwapo.com" />
<area shape="rect" coords="5,90,227,175" target="_blank"  href="http://www.onlineshopping.co.zm" />
<area shape="rect" coords="5,181,227,260" target="_blank"  href="http://www.postisp.zm" />
<area shape="rect" coords="6,266,226,348" target="_blank"  href="http://www.postcourier.co.zm" />
</map>
</td>
  </tr>
</table>

<script language="javascript">
var fp=3;
function fminus()
{
//alert(fp);
if(fp>1)
{
fp--;
fontsize();
}
}
function fplus()
{//alert(fp);
if(fp<5)
{
fp++;
fontsize();
}
}
function fontsize()
{
identity=document.getElementById("newsbody");
if(fp==1){identity.className="small";}
if(fp==2){identity.className="normal";}
if(fp==3){identity.className="large";}
if(fp==4){identity.className="large1";}
if(fp==5){identity.className="large2";}
}

function popemail(nid,tb)
 {
var n= window.open("email.php?nid="+nid + "&tbl="+tb,nid,"HEIGHT=500,WIDTH=580,top=150,left=150,scrollbars=yes,resizable=0,toolbar=no")
 }

 function popprint(nid,tb)
 {
var n2= window.open("news_print.php?nid="+nid+ "&tbl="+tb,nid,"HEIGHT=500,WIDTH=700,top=0,left=0,scrollbars=yes,resizable=1,toolbar=no")
 }

function openw(x)
{
var n3=window.open("watch_video.php?Id=" + x,"mywindow","toolbar=no,status=0,scrollbars=1,width=630,height=360");
}

  function reloadCaptcha(imageName)
  {
    var randomnumber=Math.floor(Math.random()*1001); // generate a random number to add to image url to prevent caching
    document.images[imageName].src = document.images[imageName].src + '&amp;rand=' + randomnumber; // change image src to the same url but with the random number on the
  }

function valid()
{
if((document.frm.name.value=="")||(document.frm.location.value=="")||(document.frm.email.value=="")||(document.frm.msg.value=="")||(document.frm.captchacode.value==""))
{
alert("Please enter required fields");
return false;
}

if(checkemail(document.frm.email.value)==false)
{
alert("Invalid E-mail Address! Please re-enter.")
return false;
}


}

function checkemail(x)
{
	if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(x))
		{
		return true;
		}
	else
		{
		return false;
		}
}

//ajax
 	var xmlHttp;


	function sendc()
	{
		var name="";
		var email="";
		var msg="";
		var subject="";
		var nid="";

		nid=document.frmcom.nid.value;
		name=document.frmcom.name.value;
		email=document.frmcom.email.value;
		subject=document.frmcom.subject.value;
		msg=document.frmcom.msg.value;

		if((name=="")||(email=="")||(subject=="")||(msg==""))
		{
			alert("Please fill the required fields");
			return false;
		}
		if(!checkemail(email))
		{
			alert("Invalid Email Address");
			//document.frm.email.focus();
			return false;
		}


		xmlHttp=GetXmlHttpObject();
		if (xmlHttp==null)
		 {
			alert ("Browser does not support HTTP Request");
			return;
		 }

		//SJA Mods - must POST the data as need no length constraints - will need to URL decode the other side... encodeURIComponent() handles URL uncoding in JScript; decodeURIComponent() to decode
		var params="nid=" +nid + "&name="+name+"&email="+email+"&subject="+subject+"&msg="+msg;

		var url="postcomments.php?" + params + "&m"+ Math.random();

		xmlHttp.onreadystatechange=stateChanged ;
		xmlHttp.open("GET",url,true);
		xmlHttp.send(null);
			return false;

	}

	function stateChanged()
	{
		if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete")
		{
			//alert(xmlHttp.responseText);
			//alert("Thanks for the Comment!");
			//document.frm.email.value="";
			//document.frm.msg.value="";
			//document.frm.name.value="";

	        if (xmlHttp.status == 200) {
				document.getElementById("frmcom").innerHTML='<span style="color:#000000;">Thanks for the Comment!</span>' ;
				//document.getElementById("frmcom").className="msgc2";

            } else {
      	      alert('There was a problem sending your comment, please try again.');
            }
		}
		else
		{
			///uest_book.style["visibility"]="visible";
			document.getElementById("frmcom").innerHTML='<img src="images/loading.gif" border="0">' ;
		}
	}

	//wishlist code

	function GetXmlHttpObject()
	{
		var objXMLHttp=null;
		if (window.XMLHttpRequest)
		{
			objXMLHttp=new XMLHttpRequest();
		}
		else if (window.ActiveXObject)
		{
			objXMLHttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		return objXMLHttp;
	}


//-->
 </script>
 
 <!--
 <div   id="right-sidebar"> <a href="" target="_blank"><img src="" border="0"  width="125px"     /></a></div>
<div   id="left-sidebar">  <a href="" target="_blank"><img src="" border="0"  width="125px"     /></a></div>
-->
"""
        
        doc = Document()
        doc.url = 'http://postzambia.com/news.php?id=5177'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, 'The race is tight - Simuusa')
        self.assertIsNone(doc.summary)
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '05 01 2015')
        self.assertEqual(doc.author.name, 'Tilyenji Mwanza')
        self.assertEqual(doc.medium.name, 'Post Zambia')

        self.maxDiff = None
        self.assertEqual(doc.text, u'WYLBUR Simuusa says the January 20 presidential race is tight and the PF needs the input of every member to win the election.\n\nReacting to Chishimba Kambwili\xe2\u20ac\u2122s remark that Geoffrey Mwamba was limited in thinking because of his low levels of education following the latter\xe2\u20ac\u2122s decision to support the UPND, Simuusa said the Patriotic Front cannot afford to lose its top leaders.\n\nHe said it was wrong for anyone in the PF to issue disparaging remarks against Sylvia Masebo and Mwamba simply because they have resolved to support the UPND.\n\n\xe2\u20ac\u0153We need everybody, although I was very categorical on Guy Scott. And at one point, I said we need GBM and now I say we need Masebo too. We have a history with Sylvia and with GBM; we need those votes. And what we should be doing is not disparaging them. We should not disparage GBM and Masebo. We as PF may not agree, but insulting them and belittling them is not the way to go,\xe2\u20ac\x9d said Simuusa, who is agriculture minister and Nchanga PF member of parliament.\n\nHe said it would be na\xc3\xafve and untrue to say Mwamba and Masebo are not political factors just because they have chosen a different path.\n\n\xe2\u20ac\u0153We need everyone. GBM has his following and it is a following that was developed with the PF. We as the PF need to work on reconciliation and realise that everybody matters, even Masebo. We worked with them before and they helped deliver PF, so it is unfair to say they do not matter, or begin to issue disparaging remarks,\xe2\u20ac\x9d Simuusa said.\n\nHe said UPND and other parties were campaigning hard and it would be unwise for PF to keep losing its members.\n\nSimuusa called on PF leaders to instead find ways of recalling Mwamba and Masebo rather than pretend that the two are not a factor.\n\n\xe2\u20ac\u0153The approach should be to take the colleagues of ours and see how we can keep them in the spirit of reconciliation. Disparaging them, calling them opportunists is not right,\xe2\u20ac\x9d said Simuusa.\n\nSpeaking in Matero on New Year\xe2\u20ac\u2122s Day, PF presidential candidate Edgar Lungu described Masebo as an opportunist who jumps at every opportunity she considers viable.\n\nHe added that Masebo was not a political factor as she had no following in Lusaka or Zambia at large.')
        

class TestTimesZambiaCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = TimesZambiaCrawler()

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
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en"> <![endif]-->
<html lang="en-US">
<head>
	<!-- AMBRO HEADER -->
	<meta charset="utf-8" />
	<title>Times of Zambia   |  Scott’s case fails to take off</title>
			<link rel="alternate" type="application/rss+xml" title="Times of Zambia RSS Feed" href="http://feedburner.google.com/fb/a/mailverify?uri=TimesOfZambia&loc=en_US" /> 
			<meta name="description" content="">
	<meta name="author" content="">
	<!-- AMBRO FOR MOBILE -->
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" /> 
	<script type="text/javascript" src="http://www.times.co.zm/wp-content/themes/ambro/js/jquery.js"></script>
	<script type="text/javascript" src="http://www.times.co.zm/wp-content/themes/ambro/js/jcarousellite.js"></script>
		<link rel="alternate" type="application/rss+xml" title="Times of Zambia &raquo; Feed" href="http://www.times.co.zm/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Times of Zambia &raquo; Comments Feed" href="http://www.times.co.zm/?feed=comments-rss2" />
<link rel='stylesheet' id='scroller_css-css'  href='http://www.times.co.zm/wp-content/plugins/fp-news-scroller/css/scroller.css?ver=3.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='reset-css'  href='http://www.times.co.zm/wp-content/themes/ambro/css/reset.css?ver=3.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='format-css'  href='http://www.times.co.zm/wp-content/themes/ambro/css/format.css?ver=3.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='refindeslide-css'  href='http://www.times.co.zm/wp-content/themes/ambro/css/refineslide.css?ver=3.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='style-css'  href='http://www.times.co.zm/wp-content/themes/ambro/style.css?ver=3.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='superfishbase-css'  href='http://www.times.co.zm/wp-content/themes/ambro/css/superfish.css?ver=3.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='prettyPhoto-css'  href='http://www.times.co.zm/wp-content/themes/ambro/css/prettyPhoto.css?ver=3.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='responsive-css'  href='http://www.times.co.zm/wp-content/themes/ambro/css/responsive.css?ver=3.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='socialbox-css'  href='http://www.times.co.zm/wp-content/themes/ambro/includes/plugins/socialbox/css/socialbox.css?ver=1.3.2' type='text/css' media='screen' />
<link rel='stylesheet' id='notifications-css'  href='http://www.times.co.zm/wp-content/themes/ambro/includes/annoucements/css/notifications.css?ver=3.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='wpdreams-pslider-css'  href='http://www.times.co.zm/wp-content/plugins/polaroid-slider//css/pslider.css?ver=3.5.1' type='text/css' media='all' />
<script type='text/javascript' src='http://www.times.co.zm/wp-includes/js/jquery/jquery.js?ver=1.8.3'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/plugins/fp-news-scroller/js/jquery.webticker.js?ver=3.5.1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-includes/js/swfobject.js?ver=2.2-20120417'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/plugins/banner-manager/load.min.js?ver=3.5.1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/js/hoverIntent.js?ver=3.5.1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/js/superfish.js?ver=3.5.1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/js/supersubs.js?ver=3.5.1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/js/jquery-ui.js?ver=1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/js/jquery.refineslide.min.js?ver=1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/js/jquery.prettyPhoto.js?ver=1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/js/scrolltopcontrol.js?ver=1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/js/custom.js?ver=1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-includes/js/comment-reply.min.js?ver=3.5.1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/plugins/polaroid-slider/js/pslider.min.js?ver=3.5.1'></script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/includes/annoucements/js/jquery.cookie.js?ver=3.5.1'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var notices_ajax_script = {"ajaxurl":"http:\/\/www.times.co.zm\/wp-admin\/admin-ajax.php","logged_in":"no"};
/* ]]> */
</script>
<script type='text/javascript' src='http://www.times.co.zm/wp-content/themes/ambro/includes/annoucements/js/notifications.js?ver=3.5.1'></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://www.times.co.zm/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://www.times.co.zm/wp-includes/wlwmanifest.xml" /> 
<link rel='prev' title='13 Mkushi families left in the cold' href='http://www.times.co.zm/?p=47692' />
<link rel='next' title='Wife’s nude photos attract divorce' href='http://www.times.co.zm/?p=47699' />
<meta name="generator" content="WordPress 3.5.1" />
<link rel='canonical' href='http://www.times.co.zm/?p=47694' />
	<!-- AMBRO COLOR OPTIONS-->
	<style type="text/css" media="screen">
		body { background:#262525 
		url('http://www.times.co.zm/wp-content/uploads/2013/10/pattern-15.png') ;
		background-position: top;
		background-repeat:repeat;
		background-attachment:fixed;}
		.navigation { border-bottom:2px solid #fc0d0d;}  
		.sideg, .mgtopmenu li  > ul  {background-color: #403636;}
		.sidetw {background-color: #403636;}
		.votsignup {background-color:#fc0d0d;}
		.sidesub {background-color: #403636;}
		.search-block .search-button {  background: #fc0d0d url(http://www.times.co.zm/wp-content/themes/ambro/images/search.png) no-repeat center; } 
		.sf-menu li a:hover { color: #fc0d0d;} 
 .widget-magmag-title {
  background: -moz-linear-gradient(-45deg,  #fc0d0d 0%, #fc0d0d 50%, rgba(0,0,0,0) 51%, rgba(0,0,0,0) 100%);
  background: -webkit-gradient(linear, left top, right bottom, color-stop(0%,#fc0d0d), color-stop(50%,#fc0d0d), 
  color-stop(51%,rgba(0,0,0,0)), color-stop(100%,rgba(0,0,0,0)));				
  background: -webkit-linear-gradient(-45deg,  #fc0d0d 0%,#fc0d0d 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%);				
  background: -o-linear-gradient(-45deg,  #fc0d0d 0%,#fc0d0d 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%); 				
  background: -ms-linear-gradient(-45deg,  #fc0d0d 0%,#fc0d0d 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%); 				
  background: linear-gradient(135deg,  #fc0d0d 0%,#fc0d0d 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%);	
 
 }
.widget-magazine-line,.widget-lbg { background: #e3e3e3;}
.widget-box {
   background: -moz-linear-gradient(-45deg,  #383232 0%, #383232 50%, rgba(0,0,0,0) 51%, rgba(0,0,0,0) 100%);
  background: -webkit-gradient(linear, left top, right bottom, color-stop(0%,#383232), color-stop(50%,#383232), color-stop(51%,rgba(0,0,0,0)), color-stop(100%,rgba(0,0,0,0)));				
  background: -webkit-linear-gradient(-45deg,  #383232 0%,#383232 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%);				
  background: -o-linear-gradient(-45deg,  #383232 0%,#383232 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%); 				
  background: -ms-linear-gradient(-45deg,  #383232 0%,#383232 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%); 				
  background: linear-gradient(135deg,  #383232 0%,#383232 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%);	
 
}
.readmorebox {
  background-color:#383232;
}
.header-date-right p.date span {
 background:#383232;	
}
.widget-title {

  background: -moz-linear-gradient(-45deg,  #e61c1c 0%, #e61c1c 50%, rgba(0,0,0,0) 51%, rgba(0,0,0,0) 100%);
  background: -webkit-gradient(linear, left top, right bottom, color-stop(0%,#e61c1c), color-stop(50%,#e61c1c), color-stop(51%,rgba(0,0,0,0)), color-stop(100%,rgba(0,0,0,0)));				
  background: -webkit-linear-gradient(-45deg,  #e61c1c 0%,#e61c1c 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%);				
  background: -o-linear-gradient(-45deg,  #e61c1c 0%,#e61c1c 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%); 				
  background: -ms-linear-gradient(-45deg,  #e61c1c 0%,#e61c1c 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%); 				
  background: linear-gradient(135deg,  #e61c1c 0%,#e61c1c 50%,rgba(0,0,0,0) 51%,rgba(0,0,0,0) 100%);	
 }

		.top-wrap, .ticker, .top,.ticker-content,.ticker-swipe,.ticker-swipe span{}
		.flickr-widget .flickr_badge_image a:hover img{opacity:0.8; background:#fc0d0d;}
		.single-content blockquote, li.comment > div { border-left-color:#fc0d0d;}
	
		.sf-menu li.current-menu-item a { color:#fc0d0d;}
		.mag-box-small .small-desc .desc-title a:hover,.mag-box-small-noimage .desc-title a:hover {color:#f1f1f1;}
		.mag-box-small .small-desc .desc-title a:hover,.mag-box-small-noimage .desc-title a:hover, a:hover { color:#d92727;}
		.header-logo img, .mag-super-title h3, .readmore, h5.toggle, .single-content ul.tabs li:hover, .single-content ul.tabs li.active {  background: #fc0d0d;}
		.scrolltop:hover { background : url(http://www.times.co.zm/wp-content/themes/ambro/images/up.png) center center no-repeat #fc0d0d; }
		.navigation, .footer , .navigation-wrap,.footer-wrap, .top { background:#403636 url(http://www.times.co.zm/wp-content/themes/ambro/images/pattern.png);}
		.sf-menu li a:hover{ border-bottom:1px solid #403636;}
		.sf-menu .sub-menu { background:#3b3131;}
		.widget_calendar thead>tr>th {  background-color:#fc0d0d;}
		.rs-caption h1 a {  background-color:#fc0d0d;}
		.tagcloud ul li a:hover, .mag-super-title h3, .single-tags a:hover, .footer-widget .tagcloud a:hover,
		.related-post-title a:hover,.description-author span a:hover,.author-social, .single-nav a, #comments .navigation a:hover,
		.comment-post-title, .reply a, .pagination span,.pagination a:hover, .ambro_calendar thead>tr>th { background-color:#fc0d0d; }
		.footer-widget a:hover, .credits a:hover, .footer-widget.ambro_calendar tfoot>tr>td#prev a,
		.ambro_calendar tfoot>tr>td#next a { color:#fc0d0d; }
				</style>	<script type="text/javascript">
jQuery(document).ready(function(){
jQuery(".vote a").click(
function() {
var some = jQuery(this);
var thepost = jQuery(this).attr("post");
var theuser = jQuery(this).attr("user");
jQuery.post("http://www.times.co.zm/wp-content/themes/ambro/vote.php", {user: theuser, post: thepost}, 
function(data) {
var votebox = ".vote"+thepost+" span";
jQuery(votebox).text(data);
jQuery(some).replaceWith('<span class="voted">Voted</span>');
});
});
});	
</script>
	</head>
<body class="single single-post postid-47694 single-format-standard">
	<div class="top row">
	<!-- AMBRO SEARCH BLOCK -->
					<div class="search-block">
						<form method="get" id="searchform" action="http://www.times.co.zm/">
							<input class="search-button" type="submit" value="" />	
							<input type="text" id="s" name="s" value="Search..." onfocus="if (this.value == 'Search...') {this.value = '';}" onblur="if (this.value == '') {this.value = 'Search...';}"  />
						</form>
					</div>		
				<div class="ambrogrid_6 top-nav-wrapper">
				<ul id="menu-top-menu" class="mgtopmenu"><li id="menu-item-170" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-170"><a href="http://www.times.co.zm/?page_id=45">About us</a>
<ul class="sub-menu">
	<li id="menu-item-208" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-208"><a href="http://www.times.co.zm/?page_id=199">Org Structure</a></li>
	<li id="menu-item-207" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-207"><a href="http://www.times.co.zm/?page_id=201">History</a></li>
	<li id="menu-item-169" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-169"><a href="http://www.times.co.zm/?page_id=46">Contact us</a></li>
</ul>
</li>
<li id="menu-item-168" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-168"><a href="http://www.times.co.zm/?page_id=47">Rate Cards</a></li>
<li id="menu-item-206" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-206"><a href="http://www.times.co.zm/?page_id=204">Products &#038; Services</a>
<ul class="sub-menu">
	<li id="menu-item-236" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-236"><a href="http://www.times.co.zm/?page_id=233">Online Subscriptions</a></li>
</ul>
</li>
</ul>				</div>
		<div class="mgambrogrid_12 mobile-nav-wrapper">
			<div class="menu-top-menu-container"><select id="menu-top-menu-1" class="menu dropdown-menu"><option value="" class="blank">Select a Page</option><option class="menu-item menu-item-type-post_type menu-item-object-page menu-item-170 menu-item-depth-0" value="http://www.times.co.zm/?page_id=45">About us</option>	<option class="menu-item menu-item-type-post_type menu-item-object-page menu-item-208 menu-item-depth-1" value="http://www.times.co.zm/?page_id=199">- Org Structure</option>
	<option class="menu-item menu-item-type-post_type menu-item-object-page menu-item-207 menu-item-depth-1" value="http://www.times.co.zm/?page_id=201">- History</option>
	<option class="menu-item menu-item-type-post_type menu-item-object-page menu-item-169 menu-item-depth-1" value="http://www.times.co.zm/?page_id=46">- Contact us</option>

<option class="menu-item menu-item-type-post_type menu-item-object-page menu-item-168 menu-item-depth-0" value="http://www.times.co.zm/?page_id=47">Rate Cards</option>
<option class="menu-item menu-item-type-post_type menu-item-object-page menu-item-206 menu-item-depth-0" value="http://www.times.co.zm/?page_id=204">Products &#038; Services</option>	<option class="menu-item menu-item-type-post_type menu-item-object-page menu-item-236 menu-item-depth-1" value="http://www.times.co.zm/?page_id=233">- Online Subscriptions</option>

</select></div>	
		</div>
		</div>
	<!-- AMBRO HEADER -->
	<div class="header row">
		<!-- AMBRO LOGO -->
		<div class="header-logo">
						<a href='http://www.times.co.zm'><img src="http://www.times.co.zm/wp-content/themes/weekly/images/logo3.gif" alt="Times of Zambia" /></a>
		</div>
			<!-- AMBRO ADD -->
			<div class="header-pub">
				<a href="http://www.timesepaper.com">
<img src="http://www.times.co.zm/wp-content/uploads/2014/09/Timesad.jpg" />
</a>			</div>
			</div>
	<div class="navigation row">
				<!-- AMBRO MAIN MENU -->
					<div class="mgambrogrid_12 main-nav-wrapper">
			<ul id="menu-main-menu" class="sf-menu"><li id="menu-item-160" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-160"><a href="index.php">Home</a></li>
<li id="menu-item-163" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-163"><a href="http://www.times.co.zm/?cat=1">Latest News</a>
<ul class="sub-menu">
	<li id="menu-item-210" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-210"><a href="http://www.times.co.zm/?cat=16">Stories</a></li>
	<li id="menu-item-209" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-209"><a href="http://www.times.co.zm/?cat=15">Court News</a></li>
</ul>
</li>
<li id="menu-item-161" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-161"><a href="http://www.times.co.zm/?cat=2">Business</a>
<ul class="sub-menu">
	<li id="menu-item-213" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-213"><a href="http://www.times.co.zm/?cat=17">Stories</a></li>
	<li id="menu-item-212" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-212"><a href="http://www.times.co.zm/?cat=19">Money/Stock Exchange</a></li>
	<li id="menu-item-211" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-211"><a href="http://www.times.co.zm/?cat=18">Columns</a></li>
</ul>
</li>
<li id="menu-item-166" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-166"><a href="http://www.times.co.zm/?cat=4">Letters to the Editor</a></li>
<li id="menu-item-165" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-165"><a href="http://www.times.co.zm/?cat=5">Entertainment</a>
<ul class="sub-menu">
	<li id="menu-item-216" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-216"><a href="http://www.times.co.zm/?cat=20">Music</a></li>
	<li id="menu-item-218" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-218"><a href="http://www.times.co.zm/?cat=21">Theatre</a></li>
	<li id="menu-item-215" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-215"><a href="http://www.times.co.zm/?cat=22">Films</a></li>
	<li id="menu-item-217" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-217"><a href="http://www.times.co.zm/?cat=23">Others</a></li>
	<li id="menu-item-214" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-214"><a href="http://www.times.co.zm/?cat=24">Columns</a></li>
</ul>
</li>
<li id="menu-item-162" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-162"><a href="http://www.times.co.zm/?cat=6">Features</a></li>
<li id="menu-item-167" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-167"><a href="http://www.times.co.zm/?cat=7">Opinion</a></li>
<li id="menu-item-164" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164"><a href="http://www.times.co.zm/?cat=8">Sports</a>
<ul class="sub-menu">
	<li id="menu-item-224" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-224"><a href="http://www.times.co.zm/?cat=25">Stories</a></li>
	<li id="menu-item-221" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-221"><a href="http://www.times.co.zm/?cat=26">Football</a></li>
	<li id="menu-item-223" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-223"><a href="http://www.times.co.zm/?cat=29">Rugby</a></li>
	<li id="menu-item-219" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-219"><a href="http://www.times.co.zm/?cat=27">Boxing</a></li>
	<li id="menu-item-225" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-225"><a href="http://www.times.co.zm/?cat=28">Volleyball</a></li>
	<li id="menu-item-220" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-220"><a href="http://www.times.co.zm/?cat=31">Columns</a></li>
	<li id="menu-item-222" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-222"><a href="http://www.times.co.zm/?cat=30">Others</a></li>
</ul>
</li>
</ul><div class="header-date-right"><p class="date"><span>Last post on :</span> January 5, 2015&nbsp;&nbsp;</p></div>
</div>
		<div class="mgambrogrid_12 mobile-nav-wrapper">
			<div class="menu-main-menu-container"><select id="menu-main-menu-1" class="menu dropdown-menu"><option value="" class="blank">Select a Page</option><option class="menu-item menu-item-type-custom menu-item-object-custom menu-item-160 menu-item-depth-0" value="index.php">Home</option>
<option class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-163 menu-item-depth-0" value="http://www.times.co.zm/?cat=1">Latest News</option>	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-210 menu-item-depth-1" value="http://www.times.co.zm/?cat=16">- Stories</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-209 menu-item-depth-1" value="http://www.times.co.zm/?cat=15">- Court News</option>

<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-161 menu-item-depth-0" value="http://www.times.co.zm/?cat=2">Business</option>	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-213 menu-item-depth-1" value="http://www.times.co.zm/?cat=17">- Stories</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-212 menu-item-depth-1" value="http://www.times.co.zm/?cat=19">- Money/Stock Exchange</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-211 menu-item-depth-1" value="http://www.times.co.zm/?cat=18">- Columns</option>

<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-166 menu-item-depth-0" value="http://www.times.co.zm/?cat=4">Letters to the Editor</option>
<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-165 menu-item-depth-0" value="http://www.times.co.zm/?cat=5">Entertainment</option>	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-216 menu-item-depth-1" value="http://www.times.co.zm/?cat=20">- Music</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-218 menu-item-depth-1" value="http://www.times.co.zm/?cat=21">- Theatre</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-215 menu-item-depth-1" value="http://www.times.co.zm/?cat=22">- Films</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-217 menu-item-depth-1" value="http://www.times.co.zm/?cat=23">- Others</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-214 menu-item-depth-1" value="http://www.times.co.zm/?cat=24">- Columns</option>

<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-162 menu-item-depth-0" value="http://www.times.co.zm/?cat=6">Features</option>
<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-167 menu-item-depth-0" value="http://www.times.co.zm/?cat=7">Opinion</option>
<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-164 menu-item-depth-0" value="http://www.times.co.zm/?cat=8">Sports</option>	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-224 menu-item-depth-1" value="http://www.times.co.zm/?cat=25">- Stories</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-221 menu-item-depth-1" value="http://www.times.co.zm/?cat=26">- Football</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-223 menu-item-depth-1" value="http://www.times.co.zm/?cat=29">- Rugby</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-219 menu-item-depth-1" value="http://www.times.co.zm/?cat=27">- Boxing</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-225 menu-item-depth-1" value="http://www.times.co.zm/?cat=28">- Volleyball</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-220 menu-item-depth-1" value="http://www.times.co.zm/?cat=31">- Columns</option>
	<option class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-222 menu-item-depth-1" value="http://www.times.co.zm/?cat=30">- Others</option>

</select></div>	
		</div>
	</div>
<!-- AMBRO CONTENT -->
<div class="content row">		<div class="ambrogrid_81 single-post">
				<!-- AMBRO SINGLE TITLE -->
	<div class="single-title">
	<div class="widget-magazine-line"><div class="widget-magmag-title">Scott’s case fails to take off </div></div>	
				<div class="clear"></div>
	<div class="single-info">
		<span class="single-date"><strong>Published On </strong>January 5, 2015 &raquo; 33 Views&raquo; </span>	
		<span class="single-author">By Davies M.M Chanda &raquo; </span> 	
		<span class="single-category"><strong><a href="http://www.times.co.zm/?cat=1" title="View all posts in Latest News" rel="category">Latest News</a></strong></span>	
	</div>	
	<div class="clear"></div>
			</div>
<!-- AMBRO CONTENT -->
<div class="votpost"><div class="vote vote47694"><div class="star"></div>&nbsp;<span>0 stars</span></div><div class="votsignup"><a href="http://www.times.co.zm/wp-login.php?action=register">Register</a> to vote!</div></div>	<div class="single-content">
		<p><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle ga_headr"data-ad-client="ca-pub-6635048705194597"data-ad-slot="7449933923"></ins><script>(adsbygoogle=window.adsbygoogle||[]).push({});</script><div id="attachment_47695" class="wp-caption alignleft" style="width: 310px"><a href="http://www.times.co.zm/wp-content/uploads/2015/01/Scott.jpg"><img class="size-full wp-image-47695" alt="• ACTING President Guy Scott (with hands in pockets) views part of the youth resource centre under construction in Luanshya at a cost of K9.3 million. Looking on is Patriotic Front secretary general Davis Chama (right). Picture By JAMES KUNDA" src="http://www.times.co.zm/wp-content/uploads/2015/01/Scott.jpg" width="300" height="174" /></a><p class="wp-caption-text">• ACTING President Guy Scott (with hands in pockets) views part of the youth resource centre under construction in Luanshya at a cost of K9.3 million. Looking on is Patriotic Front secretary general Davis Chama (right). Picture By JAMES KUNDA</p></div></p>
<p>By JAMES KUNDA -<br />
THE case in which Acting President Guy Scott is challenging his demotion as vice-president in the Patriotic Front (PF) failed to take off in the Ndola High Court yesterday.<br />
Dr Scott obtained an injunction in the Ndola High Court, restraining the party from removing him from his position as vice-president.<br />
The Acting President also sought to restrain the defendant, either by himself, servants or agents or any superior or member of the PF from suspending or expelling or taking any action adverse to his position as party vice-president until the matter was determined.<br />
The matter was adjourned to yesterday but could not take off in Chambers as presiding Judge Anesi Banda Bobo was out of office attending a Judges Seminar that had commenced in Chisamba.<br />
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle ga_content"data-ad-client="ca-pub-6635048705194597"data-ad-slot="3278917434"></ins><script>(adsbygoogle=window.adsbygoogle||[]).push({});</script>The Court will now have to set a new date for the case to be heard as both parties pursue the probability of entering an ex-curia or case settlement outside Court.<br />
Dr Scott is being represented by Iven Mulenga of Iven Mulenga and Company, while the PF is being represented by Billingtone Mosha of Messers Mosha and Company.</p>
</div>
		<!-- AMBRO NAVIGATION -->
	<div class="single-nav">
	<div class="nav-left" ><a href="http://www.times.co.zm/?p=47692" rel="prev"><< Previous post</a> </div>
	<div class="nav-right" ><a href="http://www.times.co.zm/?p=47699" rel="next">Next post >></a></div>
	</div>
		<div class="widget-magazine-line"><div class="widget-magmag-title">Share this post</div> </div>
<div class="post-share-box">

<ul>
	 
<li class="facebook">
	<a title="Facebook" class="tooltip" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fwww.times.co.zm%2F%3Fp%3D47694&amp;t=Scott%E2%80%99s+case+fails+to+take+off"></a>
</li>

<li class="twitter">
<a title="Twitter" class="tooltip" href="http://twitthis.com/twit?url=http://www.times.co.zm/?p=47694"></a>
</li>

<li class="google">
<a title="Google +1" class="tooltip" href="http://google.com/bookmarks/mark?op=edit&amp;bkmk=http%3A%2F%2Fwww.times.co.zm%2F%3Fp%3D47694&amp;title=Scott%E2%80%99s+case+fails+to+take+off"></a>
</li>

<li class="tumblr">
<a title="Tumblr" class="tooltip" href="http://www.tumblr.com/share/link?url=http%3A%2F%2Fwww.times.co.zm%2F%3Fp%3D47694&amp;name=Scott%E2%80%99s+case+fails+to+take+off&amp;description=By+JAMES+KUNDA+-+THE+case+in+which+Acting+President+Guy+Scott+is+challenging+his+demotion+as+vice-president+in+the+Patriotic+Front+%28PF%29+failed+to+take+off+in+the+Ndola+High+Court+yesterday.+Dr+Scott+obtained+an+injunction+in+the+Ndola+High+Court%2C+restraining+the+party+from+removing+him+from+his+position+as+vice-president.+The+%5B...%5D"></a>
</li>

<li class="linkedin">
<a title="Linkedin" class="tooltip" href="http://linkedin.com/shareArticle?mini=true&amp;url=http%3A%2F%2Fwww.times.co.zm%2F%3Fp%3D47694&amp;title=Scott%E2%80%99s+case+fails+to+take+off"></a>
</li>

<li class="reddit">
<a title="Reddit" class="tooltip" href="http://reddit.com/submit?url=http%3A%2F%2Fwww.times.co.zm%2F%3Fp%3D47694&amp;title=Scott%E2%80%99s+case+fails+to+take+off"></a>
</li>

<li class="email">
<a title="Email" class="tooltip" href="mailto:?subject=Scott%E2%80%99s+case+fails+to+take+off&amp;body=http%3A%2F%2Fwww.times.co.zm%2F%3Fp%3D47694"></a>
</li>

	

</ul>
</div>		<div class="widget-magazine-line">
<div class="widget-magmag-title">Tags</div> </div>
	<p class="single-tags"></p>
	 		
		<!-- AMBRO RELATED -->
								<!-- AMBRO AUTHOR -->
	<div class="box-author">
	<div class="widget-magazine-line"><div class="widget-magmag-title">About The Author</div></div>
	<div class="author-description">
	<div class="author-base">
	<div class="author-pic"><a href="http://www.times.co.zm/?author=2"><img alt='' src='http://1.gravatar.com/avatar/376bfaf10b9921494e3ad3d8d6ba700e?s=109&amp;d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D109&amp;r=G' class='avatar avatar-109 photo' height='109' width='109' /></a></div>
			</div>
	<div class="description-author">
		<span><a href="http://www.times.co.zm/?author=2" title="Posts by Davies M.M Chanda" rel="author">Davies M.M Chanda</a></span><br/>
		<span></span>
	</div>
	</div>
	</div>
		<!-- COMMENTS -->
	<div class="single-comments">
		<div id="comments">
<p class="nocomments">Comments are closed.</p>
								</div>	</div>
			</div>
		<!-- AMBRO RIGHT SIDEBAR -->
	<div class="ambrogrid_4 sidebar">
		<div id="text-7" class="widget widget_text">			<div class="textwidget"><div align='center'><a href='http://www.hit-counts.com'><img src='http://www.hit-counts.com/counter.php?t=MTI4NjE4OA==' border='0' alt='Visitor Counter'></a><BR><a href='http://www.hit-counts.com'>Visits so far</a></div></div>
		</div><div id="ambro_popular_widget-2" class="widget ambro_popular_widget">		<!-- AMBRO BEGIN WIDGET -->
		<div class="widget-lbg"><div class="widget-title">Popular Posts</div></div>		
		
				<div class="mag-box-small no-margin">
								<div class="magmg-image small">
					<a class="link-format-icon" href='http://www.times.co.zm/?p=736' title='Govt unveils RDA Board'><img src="http://www.times.co.zm/wp-content/themes/ambro/images/thumbnails/image-small-mag.png" alt="no image" class="overlay"/></a>
					
				</div>
								<div class="small-desc">
					<h3 class="desc-title"><a href='http://www.times.co.zm/?p=736' title='Govt unveils RDA Board'>Govt unveils RDA Board</a></h3>
					<div class="magz-meta">December 27, 2013  |  127207 Views</div>
					By NAKUBIANA SHABONGO - GOVERNMENT has unveiled the...				</div>
		</div>
				<div class="mag-box-small ">
								<div class="magmg-image small">
					<a class="link-format-icon" href='http://www.times.co.zm/?p=2949' title='Preach Constitution, Oasis Forum urges churches'><img src="http://www.times.co.zm/wp-content/themes/ambro/images/thumbnails/image-small-mag.png" alt="no image" class="overlay"/></a>
					
				</div>
								<div class="small-desc">
					<h3 class="desc-title"><a href='http://www.times.co.zm/?p=2949' title='Preach Constitution, Oasis Forum urges churches'>Preach Constitution,...</a></h3>
					<div class="magz-meta">January 8, 2014  |  73567 Views</div>
					By FLAVIOR CHISHALA - THE Oasis Forum says...				</div>
		</div>
				<div class="mag-box-small ">
								<div class="magmg-image small">
					<a class="link-format-icon" href='http://www.times.co.zm/?p=7948' title='‘General’ Kanene convicted, locked up'><img width="80" height="80" src="http://www.times.co.zm/wp-content/uploads/2014/02/General-Kanene-prison-truck-80x80.jpg" class="overlay wp-post-image" alt="•CONTROVERSIAL singer Clifford Dimba popularly known as ‘General’ Kanene gets on a prison truck (Kasalanga) after he was found guilty of defilement by the Lusaka Magistrate’s Court yesterday. (Insert Above) Kanene before his conviction while his wife (below) carrying their child breaks down. Pictures by CLEVER ZULU" /></a>
					By PERPETUAL SICHIKWENKWE - LUSAKA-based musician Clifford Dimba,...				</div>
								<div class="small-desc">
					<h3 class="desc-title"><a href='http://www.times.co.zm/?p=7948' title='‘General’ Kanene convicted, locked up'>‘General’ Kanene...</a></h3>
					<div class="magz-meta">February 4, 2014  |  59491 Views</div>
					By PERPETUAL SICHIKWENKWE - LUSAKA-based musician Clifford Dimba,...				</div>
		</div>
				</div><div id="newsscrollerwidget-2" class="widget NewsscrollerWidget"><script type="text/javascript">
jQuery(document).ready(function($){
	$("#news_scroller").webTicker({
		duplicate:true,
		moving: true,  
		speed: 40, 
		direction: 'left', 
		startEmpty:false,		
		hoverpause:true		});
});
</script>

<ul id='news_scroller'><li class='scroll_item'><a href='http://www.times.co.zm/?p=47699'>Wife’s nude photos attract divorce</a></li><li class='scroll_item'><a href='http://www.times.co.zm/?p=47694'>Scott’s case fails to take off</a></li><li class='scroll_item'><a href='http://www.times.co.zm/?p=47692'>13 Mkushi families left in the cold</a></li><li class='scroll_item'><a href='http://www.times.co.zm/?p=47685'>Lupando urges  East to vote for Edgar</a></li><li class='scroll_item'><a href='http://www.times.co.zm/?p=47682'>Masaiti gets K50m boarding school</a></li></ul></div><div id="ambro_add300_widget-2" class="widget ambro_add300_widget">					<div class="adds300x250"><a href="http://www.timesepaper.com">
<img src="eTimes.jpeg" />
</a></div>
		</div><div id="text-3" class="widget widget_text"><div class="widget-lbg"><div class="widget-title">Twitter</div></div>			<div class="textwidget"><a class="twitter-timeline"  href="https://twitter.com/timesofzambia"  data-widget-id="391194578486697984">Tweets by @timesofzambia</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
</div>
		</div>	</div>
				</div></div>
	
<!-- AMBRO FOOTER WIDGET -->
	
<div class="footer-widget-block row">
<div id="wrapper-footer-on" style="margin-top: 0px;">
 
				<!-- AMBRO WIDGET 1 -->
				<div class="ambrogrid_3">
									</div>
				<!-- AMBRO WIDGET 2 -->
				<div class="ambrogrid_3">
									</div>
				<!-- AMBRO WIDGET 3 -->
				<div class="ambrogrid_3">
									</div>
				<!-- AMBRO WIDGET 4 -->
				<div class="ambrogrid_3">
									</div>
	</div> 
		
	<div class="footer footrow">	
						<!-- AMBRO CREDITS TEXT -->
		<div class="credits">
			© 2013 Times of Zambia.		</div>
								<!-- AMBRO SOCIAL ICONS -->
		<div class="social-footer-wrap">
			<div class="social-footer">
									<ul>
													<li class="social facebook"><a target="new" href="http://www.facebook.com/timesofzambia"></a></li>
																			<li class="social twitter"><a target="new" href="http://twitter.com/timesofzambia"></a></li>
																													
														
					</ul>			</div>
		</div>
			</div></div>
	
	
							
					<div id="notification-area" class=" hidden">
								<a class="remove-notice" href="#" id="remove-notice" rel="37363">X</a>
						<div class="cont"><img src="http://www.times.co.zm/wp-content/themes/ambro/images/not.png"></div>	
						<div class="texty"><p>By JUDITH NAMUTOWE  -<br />
THE Zambezi River Authority (ZRA) has said the feasibility study on the Batoka Hydropower Station has been reviewed.<br />
ZRA chief executive officer Munyaradzi Munodawafa said in an interview yesterday that the review on the demo structure, power house and capacity output on the project had been completed.<br />
Mr Munodawafa said the authority was currently waiting for the second phase of the Environmental Impact Assessment (EIA).<br />
‘‘We have reviewed the Batoka Hydropower Station feasibility study. The study on the demo structure, power house structure and the capacity output on the project has been completed,’’ Mr Munodawafa said.<br />
He said the finalisation of the study and the EIA was expected to be completed in the first quarter of 2015.<br />
Mr Munodawfa said consultants were currently working on other processes and thereafter the project committee which include senior Government officials , utilities and ZRA would visit the project this month.<br />
He said once all these processes were completed, ZRA would then be able to select the developer for the project, after which the authority would be able to come up with the actual value of the project.<br />
Zambia and Zimbabwe signed a Memorandum of Understanding (MoU) to team up and start the Batoka hydropower project which is estimated to cost about US$4 billion.<br />
The agreement was signed during the council of ministers held at Kariba in Siavonga recently.</p>
</div>
					</div>	
					<script>
		var getElementsByClassName=function(a,b,c){if(document.getElementsByClassName){getElementsByClassName=function(a,b,c){c=c||document;var d=c.getElementsByClassName(a),e=b?new RegExp("\\b"+b+"\\b","i"):null,f=[],g;for(var h=0,i=d.length;h<i;h+=1){g=d[h];if(!e||e.test(g.nodeName)){f.push(g)}}return f}}else if(document.evaluate){getElementsByClassName=function(a,b,c){b=b||"*";c=c||document;var d=a.split(" "),e="",f="http://www.w3.org/1999/xhtml",g=document.documentElement.namespaceURI===f?f:null,h=[],i,j;for(var k=0,l=d.length;k<l;k+=1){e+="[contains(concat(' ', @class, ' '), ' "+d[k]+" ')]"}try{i=document.evaluate(".//"+b+e,c,g,0,null)}catch(m){i=document.evaluate(".//"+b+e,c,null,0,null)}while(j=i.iterateNext()){h.push(j)}return h}}else{getElementsByClassName=function(a,b,c){b=b||"*";c=c||document;var d=a.split(" "),e=[],f=b==="*"&&c.all?c.all:c.getElementsByTagName(b),g,h=[],i;for(var j=0,k=d.length;j<k;j+=1){e.push(new RegExp("(^|\\s)"+d[j]+"(\\s|$)"))}for(var l=0,m=f.length;l<m;l+=1){g=f[l];i=false;for(var n=0,o=e.length;n<o;n+=1){i=e[n].test(g.className);if(!i){break}}if(i){h.push(g)}}return h}}return getElementsByClassName(a,b,c)},
			dropdowns = document.getElementsByTagName( 'select' );
		for ( i=0; i<dropdowns.length; i++ )
			if ( dropdowns[i].className.match( 'dropdown-menu' ) ) dropdowns[i].onchange = function(){ if ( this.value != '' ) window.location.href = this.value; }
	</script>
		</body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.times.co.zm/?p=47694'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, u'Scott\u2019s case fails to take off')
        self.assertIsNone(doc.summary)
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '05 01 2015')
        self.assertEqual(doc.author.name, 'JAMES KUNDA')
        self.assertEqual(doc.medium.name, 'Times of Zambia')

        self.assertEqual(doc.text, u'By JAMES KUNDA -\nTHE case in which Acting President Guy Scott is challenging his demotion as vice-president in the Patriotic Front (PF) failed to take off in the Ndola High Court yesterday.\nDr Scott obtained an injunction in the Ndola High Court, restraining the party from removing him from his position as vice-president.\nThe Acting President also sought to restrain the defendant, either by himself, servants or agents or any superior or member of the PF from suspending or expelling or taking any action adverse to his position as party vice-president until the matter was determined.\nThe matter was adjourned to yesterday but could not take off in Chambers as presiding Judge Anesi Banda Bobo was out of office attending a Judges Seminar that had commenced in Chisamba.\nThe Court will now have to set a new date for the case to be heard as both parties pursue the probability of entering an ex-curia or case settlement outside Court.\nDr Scott is being represented by Iven Mulenga of Iven Mulenga and Company, while the PF is being represented by Billingtone Mosha of Messers Mosha and Company.')
        
