#!/usr/bin/perl -T

use strict;
use CGI;
use URI::Escape qw/uri_escape uri_unescape/;


open my($file3), '<', '/usr/lib/maddash/maddash-webui/temp.txt' or die "Couldn't open /etc/password : $!\n";

sub sanitize_input {
    my $input = shift;
    $input =~ s/\+/ /g;#get rid of any spaces encoded as + signs
    return uri_escape(uri_unescape($input));
}


my $cgi = new CGI();

print $cgi->header;

my $dashParam = sanitize_input($cgi->param("dashboard"));
my $gridParam = sanitize_input($cgi->param("grid"));
my $refreshParam = sanitize_input($cgi->param("refresh"));

#handle refresh time
my $refreshTime = "0";
if($refreshParam && $refreshParam =~ /\d+/){
    $refreshTime = $refreshParam;
}

my $type = "null";
my $name = "null";
if($dashParam && $gridParam){
	print "<h1>You cannot provide both a <i>dashboard</i> and <i>grid</i> parameter. Please only specify one.</h1>";
}elsif($dashParam){
	$type = "\"dashboard\"";
	$name = "\"$dashParam\"";
	print_page($type,$name);
}elsif($gridParam){
	$type = "\"grid\"";
	$name = "\"$gridParam\"";
	print_page($type,$name);
}else{
    print_page($type,$name);
}

sub print_page(){
my($type,$name) = @_;

print <<EOF;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>MaDDash - Monitoring and Debugging Dashboard</title>
		<link rel="stylesheet" href="lib/dojo/dijit/themes/claro/claro.css" media="screen">
		<link rel="stylesheet" href="style/maddash-webui.css" media="screen">
		<link rel="stylesheet" href="style/maddash.css" media="screen">
		<link rel="stylesheet" href="style/tipsy.css" />
        <link rel="stylesheet" href="style/jquery.fancybox-1.3.4.css" />
	
	    <script src="lib/jquery.min.js"></script>
        <script src="lib/jquery-ui.min.js"></script>
        <script type="text/javascript" src="lib/jquery.tipsy.js"></script>
		<script src="lib/dojo/dojo/dojo.js" data-dojo-config="parseOnLoad: true"></script>
		<script src="lib/dojo/dojo/dojo-maddash.js"></script>
		<script src="lib/d3.v2.js"></script>
		<script type="text/javascript" src="lib/maddash.js"></script>
		<script type="text/javascript" src="lib/maddash-webui.js"></script>
		<script>
			require(["dijit/TitlePane","dijit/MenuBar","dijit/PopupMenuBarItem","dijit/MenuSeparator","dijit/DropDownMenu","dijit/MenuItem","dijit/layout/ContentPane","dojo/parser"]);
			
			function loadDashWidgets(){
			    var configDS = new MaDDashDataSource("etc/config.json", false);
			    var config = new MadDashConfig();
			    configDS.connect(config);
			    configDS.render();
                            var titlePane = new MadDashTitleSpan('maddashTitle', 'index.cgi', 'upec.png');
EOF
print <<EOF;
	
			    titlePane.render(config.data);
			    var privacyPolicy = new MadDashPrivacyPolicy("maddashPrivacyPolicy");
			    privacyPolicy.render(config.data);
                
			    //set custom click handler
			    var handleClick = function(d){
			        var href = "details.cgi?uri=" + d.uri;
                     window.open( href );
                }
			    var gs = new MaDDashDataSource("/maddash/grids"); 
				var ds = new MaDDashDataSource("/maddash/dashboards"); 
				var mnuds = new MaDDashDataSource("/maddash/dashboards"); 
				var refreshSource = null;
				var userConfig = {};
				if($type == "grid"){
				    gs.connect(new MaDDashDashboardPane("maddashDashboardPane", $type, $name, config.data, userConfig, handleClick));
				    refreshSource = gs;
				}else{
				    ds.connect(new MaDDashDashboardPane("maddashDashboardPane", $type, $name, config.data, userConfig, handleClick));
				    refreshSource = ds;
				}
				var navMenu = new MadDashNavMenu("maddashMenuBar", "index.cgi", config, userConfig, gs, refreshSource);
				mnuds.connect(navMenu);
				refreshSource.connect(new MaDDashRefreshLabel("maddashRefreshStatus"));
				navMenu.setPageRefresh($refreshTime);
                
				mnuds.render();
				ds.render();
			}
		</script>
	</head>
	<body class="claro" style="font-family:sans-serif" marginheight="0" marginwidth="0" onload="loadDashWidgets()">
		<div id="maddashTitle" class="maddashTitle"></div>
		<div id="maddashMenuBar"></div>
		<div id="maddashRefreshStatus"></div>
		<div id="maddashDashboardPane">
		    <img style='position:relative;left:49%;top:49%' height='20' width='20' class='loader' src='images/loader.gif'/>
		</div>
EOF
print "<div style='' class='grid-container'><p style='font-size: 18px;'>Etat des sites<p>";     
open my($file), '<', '/etc/maddash/maddash-server/temp.txt' or die "Couldn't open /etc/password : $!\n";
while (my $word = <$file> ) {
    chomp $word;
    print "<h4><span>Etat de ".$word." : </span>";
    open my($file2), '<', '/usr/lib/maddash/maddash-webui/states_hosts/'.$word.'.state' or die "Couldn't open /etc/password : $!\n";
    while (my $word2 = <$file2> ) {
    	chomp $word2;
	if ( $word2 eq "UP" ) {
                print "<span style='color: green;'>UP</span></h4></span>";
        }else {
                print "<span style='color: red;'>DOWN</span></h4></span>";
        }
    }
}
print <<EOF;

		</div>
		
		<!-- add space for mouseover -->
	        <div id="footer" class="maddashFooter">
                </div>
                <div class="maddashFooterMoreInfo">
                  <br>
                  <hr width="90%">
                  More information on MaDDash available <a target="newwindow" href="https://docs.perfsonar.net">here</a>
                  <div id="maddashPrivacyPolicy"></div>
                </div>
	</body>
</html>
EOF
my $output = `php test.php`;
print $output;


}

