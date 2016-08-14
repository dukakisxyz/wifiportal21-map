# wifiportal21-map BETA
This is an aggregator and map service for bitcoin payable wifi hotspots.

<h3> Scope </h3>
If you are using the 21.co bitcoin computer and [wifiportal21] (https://github.com/aantonop/wifiportal21) to sell wifi minutes for bitcoin,
or if you are somebody looking to purchase wifi minutes in exchange for bitcoin, then the obvious questions are:
<li> How do I inform my prospective buyers about my service? </li>
<li> How do I know as a buyer, in which locations are such services available?</li>

<h3> How it works </h3>

<p>This service allows wifi sellers to register their hotspots in exchange for bitcoin. Currently the registration cost is at 10.000 satoshi.</p>
<p>To register you need to run the purchase command (shown below), providing a description of your service up to 250 characters and the location’s coordinates.</p>

<pre><code>21 buy 10.244.183.245:5000/register --data '{"description":"This is a sample description. SSID:XXX-Verizon. My rates are 0.001 BTC per minute.","latitude":"22.2722612","longitude":"114.1826218"}'
</code></pre>

You can view all the registered locations for free at http://10.244.183.245:5000/map 

<p>Requirements:</p>
1. A  <a href="https://21.co">21 Bitcoin Computer</a> or 21 installed on AWS or MacOS
2. You need to be connected to the 21 Network 
