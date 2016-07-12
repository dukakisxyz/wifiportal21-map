# wifiportal21-map BETA
This is an aggregator and map service for bitcoin payable wifi hotspots.

<h3> Scope </h3>
If you are using the 21.co bitcoin computer and [wifiportal21] (https://github.com/aantonop/wifiportal21) to sell wifi minutes for bitcoin,
or if you are somebody looking to purchuse wifi minutes in exchange for bitcoin, then the obvious question is:
<li> How do I inform my prospective buyers about my service? </li>
<li> How do I know as a buyer, in which locations are such services available?</li>

<h3> How it works </h3>

<p>This service allows wifi sellers to register their hotspots in exchange for bitcoin.</p>
<p>You only need to submit a description of your service (up to 120 characters) and your location data (latitude & longitude) as in the example below:</p>

<pre><code>21 buy url http://10.244.183.245:5000/register/<description>/<latitude>/<longitude>/
</code></pre>

For example:
<pre><code>21 buy url http://10.244.183.245:5000/register/This is my wifi hotspot! My rates are 100000 Satoshis per minute./37.4418627/-122.2130599/
</code></pre>

You can view all the registered locations for free at http://10.244.183.245:5000/map 

<p>Requirements:</p>
1. A  <a href="https://21.co">21 Bitcoin Computer</a> or 21 installed on AWS or MacOS
2. You need to be connected to the 21 Network 
