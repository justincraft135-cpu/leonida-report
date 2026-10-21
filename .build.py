import sys, pathlib
out = pathlib.Path(sys.argv[1])
SITE = "ViceHub"
DOMAIN = "https://vicehub.city"
NAV = [("index.html","Home"),("news.html","News"),("preorder.html","Preorder"),("fan-zone.html","Fan zone"),("trackers.html","Trackers"),("faq.html","FAQ")]

def page(fname, title, desc, body, hero="", scripts=""):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a>' for h,t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}/{'' if fname=='index.html' else fname}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bungee&family=Work+Sans:wght@400;600;700&display=swap">
<link rel="stylesheet" href="style.css">
<!-- ADSENSE: after approval, paste your AdSense <script> tag here. -->
</head>
<body>
<header class="top"><div class="wrap">
<a class="logo" href="index.html">Vice<span>Hub</span></a>
<nav class="nav" aria-label="Main">{nav}</nav>
</div></header>
{hero}
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">
<nav aria-label="Footer"><a href="release-date.html">Release date</a><a href="launch-checklist.html">Launch checklist</a><a href="about.html">About</a><a href="privacy.html">Privacy policy</a><a href="faq.html">FAQ</a></nav>
<p>{SITE} is an unofficial fan site. It is not affiliated with, endorsed by, or sponsored by Rockstar Games or Take-Two Interactive. Grand Theft Auto and GTA are trademarks of Take-Two Interactive. Some links may be affiliate links, which means we may earn a small commission at no cost to you.</p>
</div></footer>
{scripts}
</body>
</html>
'''

AD = '<div class="ad">Ad space &middot; paste your ad unit code here</div>'
AFF = '''<aside class="affiliate">
<p><strong>Not pre-ordered yet?</strong> Compare prices on the standard edition for PS5 and Xbox Series X|S.</p>
<a class="btn" href="#" rel="sponsored nofollow">Check today's price</a><br>
<small>Replace the # with your Amazon Associates (or other store) affiliate link.</small>
</aside>'''

COUNT_JS = '''<script>
(function () {
  var target = new Date(2026, 10, 19, 0, 0, 0); // Nov 19, 2026, midnight in the visitor's time zone
  var ids = ["d", "h", "m", "s"];
  function tick() {
    var left = Math.max(0, target - new Date());
    var v = [Math.floor(left / 864e5), Math.floor(left / 36e5) % 24, Math.floor(left / 6e4) % 60, Math.floor(left / 1e3) % 60];
    ids.forEach(function (id, i) { var el = document.getElementById("cd-" + id); if (el) el.textContent = String(v[i]).padStart(2, "0"); });
    if (left === 0) { var t = document.getElementById("cd-note"); if (t) t.textContent = "GTA 6 is out now."; }
  }
  tick(); setInterval(tick, 1000);
})();
</script>'''

HERO = '''<section class="hero"><div class="wrap">
<p class="eyebrow">Countdown to launch</p>
<h1>GTA 6 launches November 19, 2026</h1>
<p class="lede" id="cd-note">Release date, preload times, platforms and everything you should do before launch day, in one place.</p>
<ul class="countdown" aria-label="Time until launch">
<li><b id="cd-d">--</b><small>Days</small></li>
<li><b id="cd-h">--</b><small>Hours</small></li>
<li><b id="cd-m">--</b><small>Minutes</small></li>
<li><b id="cd-s">--</b><small>Seconds</small></li>
</ul>
</div></section>''' + COUNT_JS

pages = {}
pages["index.html"] = page("index.html", "GTA 6 Release Date Countdown & Launch Guide | ViceHub",
 "GTA 6 releases November 19, 2026 on PS5 and Xbox Series X|S. Live countdown, preload date, platforms and a launch-day checklist.",
 f'''<p class="updated">Updated October 20, 2026</p>
<h2>Key facts</h2>
<dl class="facts">
<dt>Release date</dt><dd>Thursday, November 19, 2026</dd>
<dt>Preload</dt><dd>Digital preloads open November 12, 2026</dd>
<dt>Platforms</dt><dd>PlayStation 5 and Xbox Series X|S. No PC date announced yet.</dd>
<dt>Setting</dt><dd>The state of Leonida, including Vice City</dd>
<dt>Main characters</dt><dd>Lucia and Jason</dd>
<dt>Online</dt><dd>Reports say online multiplayer will not be part of launch day</dd>
</dl>
{AD}
<h2>Guides</h2>
<ul class="cards">
<li><a href="release-date.html">GTA 6 release date and delay history</a><p>Every date Rockstar has announced, and what changed.</p></li>
<li><a href="launch-checklist.html">Launch-day checklist</a><p>Storage, preloading, editions and settings to sort out now.</p></li>
<li><a href="faq.html">GTA 6 FAQ</a><p>PC version, online mode, price and more.</p></li>
</ul>
{AFF}
<h2>Latest news</h2>
<ul class="timeline">
<li><time datetime="2026-10-15">October 15, 2026</time>Rockstar releases the official launch trailer and confirms the November 19 date.</li>
<li><time datetime="2026-10-12">Preloads</time>Digital preloads are set to start one week before launch, on November 12.</li>
</ul>
{AD}''', HERO)

pages["release-date.html"] = page("release-date.html", "When Does GTA 6 Come Out? Release Date & Delays | ViceHub",
 "GTA 6 comes out November 19, 2026. Here is the full delay history, preload date and what time it may unlock.",
 f'''<h1>When does GTA 6 come out?</h1>
<p class="updated">Updated October 20, 2026</p>
<p><strong>GTA 6 comes out on Thursday, November 19, 2026</strong> for PlayStation 5 and Xbox Series X|S. Rockstar confirmed the date with the launch trailer on October 15, 2026. Digital preloads open on November 12.</p>
{AD}
<h2>Delay history</h2>
<ul class="timeline">
<li><time>December 2023</time>First trailer released, with a 2025 release window.</li>
<li><time>May 2025</time>Release moved to May 26, 2026.</li>
<li><time>November 2025</time>Release moved again to November 19, 2026.</li>
<li><time>October 15, 2026</time>Launch trailer confirms November 19, 2026.</li>
</ul>
<h2>What time will GTA 6 unlock?</h2>
<p>Rockstar has not posted unlock times yet. Big console launches often unlock at midnight local time for digital copies. We will update this page when official times are announced.</p>
<h2>Is there a PC release date?</h2>
<p>No. Rockstar has only announced console versions. Some reports suggest a PC version in early 2027, but nothing is confirmed.</p>
{AFF}''')

pages["launch-checklist.html"] = page("launch-checklist.html", "GTA 6 Launch Day Checklist: Storage, Preload & Settings | ViceHub",
 "Get ready for GTA 6 on November 19. Free up storage, set up preloading, pick your edition and prepare your console.",
 f'''<h1>GTA 6 launch-day checklist</h1>
<p class="updated">Updated October 20, 2026</p>
<p>Do these things before November 19 so you can start playing the minute the game unlocks.</p>
<ul class="check">
<li><strong>Free up storage.</strong> Final file size is not confirmed. Clear plenty of space on your console's internal drive or a fast expansion drive.</li>
<li><strong>Turn on automatic downloads.</strong> Preloads open November 12. Leave your console in rest mode so it downloads overnight.</li>
<li><strong>Check your subscription.</strong> If online features arrive later, you will likely need PlayStation Plus or Xbox Game Pass Core.</li>
<li><strong>Pick your edition.</strong> Compare what each edition includes before you buy. Physical copies may still need a day-one download.</li>
<li><strong>Update your console.</strong> Install system updates the day before launch to avoid waiting on launch night.</li>
<li><strong>Clear your schedule.</strong> Servers and stores tend to be busy on launch night, so give yourself extra time.</li>
</ul>
{AD}
<h2>Gear worth having</h2>
<p>A larger SSD and a comfortable headset make a long open-world game more enjoyable.</p>
<aside class="affiliate">
<p><strong>Need more space?</strong> A 2TB console SSD gives you room for GTA 6 and the rest of your library.</p>
<a class="btn" href="#" rel="sponsored nofollow">See SSD deals</a><br>
<small>Replace the # with your affiliate link.</small>
</aside>''')

pages["faq.html"] = page("faq.html", "GTA 6 FAQ: PC, Online, Price, Map | ViceHub",
 "Quick answers to the most asked GTA 6 questions: PC version, online mode, platforms, map and characters.",
 f'''<h1>GTA 6 FAQ</h1>
<p class="updated">Updated October 20, 2026</p>
<details open><summary>When is GTA 6 coming out?</summary><p>November 19, 2026, on PS5 and Xbox Series X|S. See the <a href="release-date.html">release date page</a>.</p></details>
<details><summary>Is GTA 6 coming to PC?</summary><p>Not at launch. No PC date has been announced.</p></details>
<details><summary>Is GTA 6 on PS4 or Xbox One?</summary><p>No. It is only announced for current-generation consoles.</p></details>
<details><summary>Will GTA 6 have online multiplayer at launch?</summary><p>Reports say online will not be available on day one. Rockstar has not shared an online release date.</p></details>
<details><summary>Where is GTA 6 set?</summary><p>In the fictional state of Leonida, which is based on Florida and includes Vice City.</p></details>
<details><summary>Who are the main characters?</summary><p>Lucia and Jason, a criminal duo.</p></details>
<details><summary>When can I preload GTA 6?</summary><p>Digital preloads open November 12, 2026.</p></details>
{AD}''')

pages["about.html"] = page("about.html", "About | ViceHub",
 "About ViceHub, an unofficial GTA 6 fan site.",
 '''<h1>About ViceHub</h1>
<p>ViceHub is an independent fan site that collects GTA 6 news, release info and guides in one easy place. We are fans, not Rockstar.</p>
<p>All facts are checked against public reports and Rockstar's own announcements, and each page shows when it was last updated.</p>
<h2>Contact</h2>
<p>Email: <strong>you@example.com</strong> (replace with your address)</p>''')

pages["privacy.html"] = page("privacy.html", "Privacy Policy | ViceHub",
 "Privacy policy for ViceHub.",
 '''<h1>Privacy policy</h1>
<p class="updated">Effective October 20, 2026</p>
<p>This site does not ask you to create an account or submit personal information.</p>
<h2>Advertising</h2>
<p>We may use third-party advertising companies, such as Google AdSense, to show ads. These companies may use cookies to show ads based on your visits to this and other websites. Google's use of advertising cookies lets it and its partners serve ads based on your visits. You can opt out of personalized advertising at <a href="https://adssettings.google.com">Google Ad Settings</a>.</p>
<h2>Affiliate links</h2>
<p>Some links are affiliate links. If you buy through them we may earn a commission at no extra cost to you. As an Amazon Associate we earn from qualifying purchases.</p>
<h2>Analytics</h2>
<p>We may use privacy-friendly analytics to count visits. This data is not used to identify you.</p>
<h2>Contact</h2>
<p>Questions? Email you@example.com.</p>''')


# ---- Verified announcements ----
SRC_RS = "https://www.rockstargames.com/newswire"
NEWS = [
 ("2026-10-15", "October 15, 2026", "Launch trailer released. Rockstar confirms November 19, 2026 and digital preloads from November 12.", "Official", "https://www.fox10tv.com/2026/10/16/gta-6-locks-nov-19-release-date-after-delays/", "Fox10 report"),
 ("2026-06-25", "June 25, 2026", "Preorders open. Standard Edition reported at $79.99 and Ultimate Edition at $99.99 in the US.", "Reported", "https://games.gg/news/gta-6-release-date-preorder-ps5/", "games.gg"),
 ("2025-11-06", "November 6, 2025", "Release moved from May 26, 2026 to November 19, 2026.", "Official", SRC_RS, "Rockstar Newswire"),
 ("2025-05-06", "May 6, 2025", "Second trailer released, introducing Jason and Lucia in more detail.", "Official", SRC_RS, "Rockstar Newswire"),
 ("2025-05-02", "May 2, 2025", "Release moved from fall 2025 to May 26, 2026.", "Official", SRC_RS, "Rockstar Newswire"),
 ("2023-12-05", "December 2023", "First trailer released with a 2025 release window.", "Official", SRC_RS, "Rockstar Newswire"),
]
def news_items(limit=None):
    rows = NEWS[:limit] if limit else NEWS
    return "".join(
        f'<li><time datetime="{d}">{label}</time>{text} '
        f'<span class="tag tag-{kind.lower()}">{kind}</span> <a class="src" href="{url}" rel="noopener">Source: {sname}</a></li>'
        for d, label, text, kind, url, sname in rows)

pages["news.html"] = page("news.html", "GTA 6 News: Verified Announcements Timeline | ViceHub",
 "Every confirmed GTA 6 announcement in one timeline, with a source link for each: trailers, delays, preorders and launch date.",
 f'''<h1>Verified GTA 6 announcements</h1>
<p class="updated">Updated October 20, 2026</p>
<p>We only list news that Rockstar announced or that several major outlets reported. Each entry links to its source. <strong>Official</strong> means it came from Rockstar. <strong>Reported</strong> means it comes from trusted outlets but not Rockstar directly.</p>
<ul class="timeline">{news_items()}</ul>
{AD}''')

pages["index.html"] = page("index.html", "GTA 6 Release Date Countdown & Launch Guide | ViceHub",
 "GTA 6 releases November 19, 2026 on PS5 and Xbox Series X|S. Live countdown, verified news, preorder prices, fan polls and launch trackers.",
 f'''<p class="updated">Updated October 20, 2026</p>
<h2>Key facts</h2>
<dl class="facts">
<dt>Release date</dt><dd>Thursday, November 19, 2026</dd>
<dt>Preload</dt><dd>Digital preloads open November 12, 2026</dd>
<dt>Platforms</dt><dd>PlayStation 5 and Xbox Series X|S. No PC date announced yet.</dd>
<dt>Price</dt><dd>$79.99 Standard, $99.99 Ultimate (reported US prices). <a href="preorder.html">Compare stores</a></dd>
<dt>Setting</dt><dd>The state of Leonida, including Vice City</dd>
<dt>Main characters</dt><dd>Lucia and Jason</dd>
</dl>
{AD}
<h2>Latest verified news</h2>
<ul class="timeline">{news_items(3)}</ul>
<p><a href="news.html">See every announcement</a></p>
<h2>Explore</h2>
<ul class="cards">
<li><a href="preorder.html">Preorder comparison</a><p>Editions, prices and where to buy.</p></li>
<li><a href="fan-zone.html">Fan zone</a><p>Vote in polls, lock in predictions and rank what you are most hyped for.</p></li>
<li><a href="trackers.html">Completion trackers</a><p>Tick off missions, vehicles, collectibles and locations.</p></li>
<li><a href="launch-checklist.html">Launch-day checklist</a><p>Storage, preloading and settings to sort out now.</p></li>
</ul>
{AFF}''', HERO)

# ---- Preorder comparison ----
STORES = [
 ("Amazon", "Physical, digital code", "amazon"),
 ("Best Buy", "Physical, digital code", "bestbuy"),
 ("Walmart", "Physical", "walmart"),
 ("GameStop", "Physical, digital code", "gamestop"),
 ("PlayStation Store", "Digital (PS5)", "psstore"),
 ("Microsoft Store", "Digital (Xbox)", "xboxstore"),
]
store_rows = "".join(
 f'<tr><th scope="row">{n}</th><td>{f}</td><td><a class="btn btn-sm" href="#" data-aff="{k}" rel="sponsored nofollow noopener">Check price</a></td></tr>'
 for n, f, k in STORES)
pages["preorder.html"] = page("preorder.html", "GTA 6 Preorder: Prices, Editions & Where to Buy | ViceHub",
 "Compare GTA 6 Standard and Ultimate editions and see where to preorder for PS5 and Xbox Series X|S.",
 f'''<h1>GTA 6 preorder comparison</h1>
<p class="updated">Updated October 20, 2026. Prices change, so confirm at checkout.</p>
<h2>Editions</h2>
<div class="table-scroll"><table>
<thead><tr><th scope="col">Edition</th><th scope="col">US price</th><th scope="col">What's included</th></tr></thead>
<tbody>
<tr><th scope="row">Standard</th><td class="num">$79.99</td><td>Base game. Preorder bonus reported: Vintage Vice City Pack.</td></tr>
<tr><th scope="row">Ultimate</th><td class="num">$99.99</td><td>Base game plus extra vehicles, weapons and story content. Preorder bonus reported: Vintage Vice City Pack.</td></tr>
</tbody></table></div>
<p class="note">Prices and bonuses are as reported by <a href="https://games.gg/news/gta-6-release-date-preorder-ps5/" rel="noopener">games.gg</a> and <a href="https://www.vice.com/en/article/gta-6-pre-order-bonuses-and-price-confirmed-all-ultimate-edition-rewards/" rel="noopener">VICE</a>. Some physical copies may come as a download code in a box, so check the listing if you want a disc.</p>
{AD}
<h2>Where to preorder</h2>
<div class="table-scroll"><table>
<thead><tr><th scope="col">Store</th><th scope="col">Formats</th><th scope="col"><span class="sr">Link</span></th></tr></thead>
<tbody>{store_rows}</tbody></table></div>
<p class="note">Links marked "Check price" may be affiliate links. We may earn a small commission if you buy, at no extra cost to you.</p>
<h2>Digital or physical?</h2>
<p><strong>Digital</strong> lets you preload on November 12 and play at unlock. <strong>Physical</strong> can be resold later, but delivery may arrive after launch day unless the store offers release-day delivery.</p>
{AFF}''')

# ---- Fan zone ----
pages["fan-zone.html"] = page("fan-zone.html", "GTA 6 Fan Polls, Predictions & Rankings | ViceHub",
 "Vote in GTA 6 fan polls, make your launch predictions and rank the features you are most excited about.",
 f'''<h1>Fan zone</h1>
<p>Vote, predict and rank. Your picks are saved in this browser so you can come back and change them.</p>
<p class="note" id="fan-mode"></p>
<h2>Polls</h2>
<div id="polls" class="stack"></div>
{AD}
<h2>Predictions</h2>
<form id="predict" class="panel stack">
<label for="p-score">Metacritic score <output id="p-score-out" class="num">95</output></label>
<input type="range" id="p-score" name="score" min="70" max="100" value="95">
<label for="p-sales">Copies sold in the first week (millions)</label>
<input type="number" id="p-sales" name="sales" min="0" max="200" step="1" value="25" inputmode="numeric">
<label for="p-online">When will GTA 6 Online launch?</label>
<select id="p-online" name="online">
<option>Before end of 2026</option><option>Early 2027</option><option>Mid 2027</option><option>Late 2027 or later</option>
</select>
<label for="p-pc">When will the PC version come out?</label>
<select id="p-pc" name="pc">
<option>Early 2027</option><option>Late 2027</option><option>2028 or later</option>
</select>
<button type="submit" class="btn">Lock in my predictions</button>
<p id="predict-msg" class="note" role="status"></p>
</form>
<h2>Community ranking: most hyped feature</h2>
<p>Put these in order, top is the one you care about most.</p>
<ol id="rank" class="rank"></ol>
<p id="rank-msg" class="note" role="status"></p>
<div id="rank-results"></div>''', scripts='<script src="fan.js?v=2"></script>')

# ---- Trackers ----
pages["trackers.html"] = page("trackers.html", "GTA 6 Trackers: Missions, Vehicles, Collectibles & Locations | ViceHub",
 "Track your GTA 6 progress. Check off missions, vehicles, collectibles and locations. Progress saves in your browser.",
 f'''<h1>GTA 6 completion trackers</h1>
<p>Tick items off as you play. Progress saves in this browser. Full lists go up after launch on November 19, 2026.</p>
<div class="tabs" role="tablist" id="tabs"></div>
<label for="t-search" class="sr">Search this list</label>
<input type="search" id="t-search" placeholder="Search this list">
<div id="tracker"></div>
{AD}''', scripts='<script src="tracker-data.js"></script>\n<script src="tracker.js"></script>')

for name, html in pages.items():
    (out / name).write_text(html)
(out / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
urls = "".join(f"  <url><loc>{DOMAIN}/{'' if n=='index.html' else n}</loc><lastmod>2026-10-20</lastmod></url>\n" for n in pages)
(out / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
(out / "ads.txt").write_text("# After AdSense approval, replace this line with the ads.txt line Google gives you, e.g.:\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")
