# ViceCityHub: GTA 6 fan site

Plain HTML + CSS. No build step. Edit any `.html` file in a text editor.

## Before you go live (5 min)
1. Links in the pages and `sitemap.xml` point to the GitHub Pages address. When you buy a domain, find and replace `justincraft135-cpu.github.io/leonida-report` with it.
2. Replace `you@example.com` in `about.html` and `privacy.html`.
3. Replace each `href="#"` that has `rel="sponsored"` with your affiliate link. On `preorder.html` each store button has a label like `data-aff="amazon"` so you know which link goes where.

## Features
- **Countdown + verified news:** `index.html`, `news.html`. Each news item is tagged Official or Reported and links its source. Add new items at the top of the list.
- **Fan zone** (`fan-zone.html`, `fan.js`): polls, predictions, ranking. Works right away, but votes are saved only in each visitor's browser. To show shared results from all visitors, see "Shared votes" below.
- **Preorder comparison** (`preorder.html`): editions, reported prices with sources, six stores with affiliate buttons.
- **Trackers** (`trackers.html`): missions, vehicles, collectibles and locations with progress bars. Locations are filled in already. After launch, add items in `tracker-data.js`.

## Shared votes (optional, free)
1. Create a free project at supabase.com.
2. In its SQL editor, run:
```sql
create table votes (
  voter text not null, kind text not null, question text not null, answer text not null,
  created_at timestamptz default now(),
  primary key (voter, kind, question)
);
alter table votes enable row level security;
create policy "read" on votes for select using (true);
create policy "vote" on votes for insert with check (length(answer) < 60);
create policy "change vote" on votes for update using (true) with check (length(answer) < 60);
```
3. Copy the Project URL and the anon public key into the top of `fan.js`.
This is fine for a small fan site. People who clear their browser can vote again.

## Affiliate programs to join
Amazon Associates, plus Best Buy, Walmart and GameStop (all through Impact.com). Join one or two to start.

## Host it free
- **Netlify (easiest):** go to app.netlify.com/drop and drag this folder in. Done.
- **GitHub Pages:** create a public repo, upload these files, then Settings → Pages → deploy from `main`.
- **Custom domain:** buy one (~$10/yr) and connect it in Netlify or GitHub Pages settings. Ad networks approve custom domains more easily.

## Make money
1. **Amazon Associates** (start now): sign up, get links for GTA 6 editions, console SSDs, headsets. Paste them into the buttons.
2. **Google AdSense** (after ~15–20 useful pages and some traffic): apply, paste their script where the `ADSENSE` comment is in each page's `<head>`, put ad units in the `.ad` boxes, and paste their line into `ads.txt`.
3. **Get traffic:** submit `sitemap.xml` in Google Search Console. Post a new guide every few days once the game launches (money, map, cheats, missions, best cars). Share on Reddit/X where allowed.

## Reality check
Most new sites earn little or nothing for the first few months. Income comes from steady traffic, which comes from many helpful pages. GTA 6 launch is Nov 19, 2026, so the next 4–8 weeks are the best time to publish.

## Stay safe legally
Keep the "unofficial fan site" footer. Don't use Rockstar's logo, box art, or trailer screenshots without permission. Write your own text.
