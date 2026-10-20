/* Fan zone: polls, predictions and a ranking.
 *
 * Without setup, votes are saved only in the visitor's browser.
 * To show shared results from all visitors, create a free Supabase project,
 * run supabase-setup.sql from the README, then fill in the two values below.
 */
var SUPABASE_URL = "";      // e.g. "https://abcd1234.supabase.co"
var SUPABASE_ANON_KEY = ""; // the public "anon" key, safe to put in the page

var POLLS = [
  { id: "protagonist", q: "Who are you more excited to play as?", a: ["Lucia", "Jason", "Both equally"] },
  { id: "dayone", q: "How are you getting GTA 6?", a: ["Digital preorder", "Physical copy", "Waiting for reviews", "Waiting for PC"] },
  { id: "edition", q: "Which edition are you buying?", a: ["Standard", "Ultimate", "Not sure yet"] },
  { id: "first", q: "First thing you will do in Leonida?", a: ["Start the story", "Explore Vice City", "Steal the fastest car", "Cause chaos"] }
];
var FEATURES = ["Story and characters", "The map", "Vehicles", "Wildlife and nature", "Side activities", "GTA 6 Online"];

var shared = !!(SUPABASE_URL && SUPABASE_ANON_KEY);

function load(key, fallback) {
  try { var v = localStorage.getItem("lr-" + key); return v ? JSON.parse(v) : fallback; } catch (e) { return fallback; }
}
function save(key, val) {
  try { localStorage.setItem("lr-" + key, JSON.stringify(val)); } catch (e) {}
}
function voterId() {
  var id = load("voter", null);
  if (!id) { id = Math.random().toString(36).slice(2) + Date.now().toString(36); save("voter", id); }
  return id;
}
function api(path, opts) {
  opts = opts || {};
  opts.headers = Object.assign({ apikey: SUPABASE_ANON_KEY, Authorization: "Bearer " + SUPABASE_ANON_KEY, "Content-Type": "application/json" }, opts.headers || {});
  return fetch(SUPABASE_URL + "/rest/v1/" + path, opts).then(function (r) { if (!r.ok) throw new Error(r.status); return r.status === 204 || r.status === 201 ? null : r.json(); });
}
// One row per voter per question; voting again replaces the old answer.
function sendVote(kind, question, answer) {
  if (!shared) return Promise.resolve();
  return api("votes?on_conflict=voter,kind,question", {
    method: "POST",
    headers: { Prefer: "resolution=merge-duplicates" },
    body: JSON.stringify({ voter: voterId(), kind: kind, question: question, answer: String(answer) })
  }).catch(function () {});
}
function fetchVotes(kind) {
  if (!shared) return Promise.resolve(null);
  return api("votes?select=question,answer&kind=eq." + kind).catch(function () { return null; });
}

document.getElementById("fan-mode").textContent = shared
  ? "Results show votes from every visitor."
  : "Your votes are saved in your browser. Shared results from all fans are coming soon.";

/* Polls */
var mine = load("polls", {});
function renderPolls(rows) {
  var box = document.getElementById("polls");
  box.innerHTML = "";
  POLLS.forEach(function (p) {
    var counts = {}, total = 0;
    (rows || []).forEach(function (r) { if (r.question === p.id) { counts[r.answer] = (counts[r.answer] || 0) + 1; total++; } });
    var fs = document.createElement("fieldset");
    fs.className = "panel poll";
    fs.innerHTML = "<legend>" + p.q + "</legend>";
    p.a.forEach(function (ans, i) {
      var id = "poll-" + p.id + "-" + i;
      var pct = total ? Math.round((counts[ans] || 0) / total * 100) : null;
      var row = document.createElement("div");
      row.className = "choice";
      row.innerHTML = '<input type="radio" name="' + p.id + '" id="' + id + '" value="' + ans + '"' + (mine[p.id] === ans ? " checked" : "") + '>' +
        '<label for="' + id + '">' + ans + "</label>" +
        (pct === null ? "" : '<span class="pct num">' + pct + '%</span><span class="bar" style="--w:' + pct + '%"></span>');
      fs.appendChild(row);
    });
    if (total) { var t = document.createElement("small"); t.className = "note"; t.textContent = total + " votes"; fs.appendChild(t); }
    fs.addEventListener("change", function (e) {
      mine[p.id] = e.target.value; save("polls", mine);
      sendVote("poll", p.id, e.target.value).then(refreshPolls);
    });
    box.appendChild(fs);
  });
}
function refreshPolls() { fetchVotes("poll").then(renderPolls); }
renderPolls(null); refreshPolls();

/* Predictions */
var form = document.getElementById("predict");
var score = document.getElementById("p-score"), scoreOut = document.getElementById("p-score-out");
var saved = load("predict", null);
if (saved) Object.keys(saved).forEach(function (k) { if (form.elements[k]) form.elements[k].value = saved[k]; });
scoreOut.textContent = score.value;
score.addEventListener("input", function () { scoreOut.textContent = score.value; });
form.addEventListener("submit", function (e) {
  e.preventDefault();
  var data = { score: score.value, sales: form.elements.sales.value, online: form.elements.online.value, pc: form.elements.pc.value };
  save("predict", data);
  Object.keys(data).forEach(function (k) { sendVote("predict", k, data[k]); });
  document.getElementById("predict-msg").textContent = "Saved. Come back after launch to see how close you were.";
});

/* Ranking */
var order = load("rank", FEATURES.slice());
if (order.length !== FEATURES.length) order = FEATURES.slice();
function renderRank() {
  var ol = document.getElementById("rank");
  ol.innerHTML = "";
  order.forEach(function (f, i) {
    var li = document.createElement("li");
    li.innerHTML = '<span class="rank-name">' + f + "</span>" +
      '<button type="button" aria-label="Move ' + f + ' up"' + (i === 0 ? " disabled" : "") + ">&#9650;</button>" +
      '<button type="button" aria-label="Move ' + f + ' down"' + (i === order.length - 1 ? " disabled" : "") + ">&#9660;</button>";
    var b = li.querySelectorAll("button");
    b[0].onclick = function () { move(i, -1, 0); };
    b[1].onclick = function () { move(i, 1, 1); };
    ol.appendChild(li);
  });
}
function move(i, d, btn) {
  var j = i + d; if (j < 0 || j >= order.length) return;
  var t = order[i]; order[i] = order[j]; order[j] = t;
  save("rank", order); renderRank();
  var target = document.querySelectorAll("#rank li")[j].querySelectorAll("button")[btn];
  (target.disabled ? document.querySelectorAll("#rank li")[j].querySelector("button:not([disabled])") : target).focus();
  clearTimeout(move.t);
  move.t = setTimeout(function () {
    order.forEach(function (f, k) { sendVote("rank", f, k + 1); });
    document.getElementById("rank-msg").textContent = "Ranking saved.";
    refreshRank();
  }, 800);
}
// Community ranking = average position across all voters (lower is better).
function refreshRank() {
  fetchVotes("rank").then(function (rows) {
    var box = document.getElementById("rank-results");
    if (!rows || !rows.length) { box.innerHTML = ""; return; }
    var sum = {}, n = {};
    rows.forEach(function (r) { sum[r.question] = (sum[r.question] || 0) + Number(r.answer); n[r.question] = (n[r.question] || 0) + 1; });
    var avg = FEATURES.map(function (f) { return { f: f, a: n[f] ? sum[f] / n[f] : 99 }; }).sort(function (x, y) { return x.a - y.a; });
    box.innerHTML = "<h3>What all fans picked</h3><ol>" + avg.map(function (x) { return "<li>" + x.f + "</li>"; }).join("") + "</ol>";
  });
}
renderRank(); refreshRank();
