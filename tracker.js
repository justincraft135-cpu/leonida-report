/* Completion trackers. Lists come from tracker-data.js; progress is saved in the visitor's browser. */
(function () {
  var done = {};
  try { done = JSON.parse(localStorage.getItem("lr-tracker") || "{}"); } catch (e) {}
  function persist() { try { localStorage.setItem("lr-tracker", JSON.stringify(done)); } catch (e) {} }

  var tabs = document.getElementById("tabs"), box = document.getElementById("tracker"), search = document.getElementById("t-search");
  var current = TRACKERS[0].id;
  var fromHash = location.hash.slice(1);
  if (TRACKERS.some(function (t) { return t.id === fromHash; })) current = fromHash;

  function count(t) { return t.items.filter(function (i) { return done[t.id + ":" + i.id]; }).length; }

  function renderTabs() {
    tabs.innerHTML = "";
    TRACKERS.forEach(function (t) {
      var b = document.createElement("button");
      b.type = "button"; b.setAttribute("role", "tab");
      b.setAttribute("aria-selected", t.id === current ? "true" : "false");
      b.innerHTML = t.title + ' <span class="num">' + count(t) + "/" + t.items.length + "</span>";
      b.onclick = function () { current = t.id; search.value = ""; history.replaceState(null, "", "#" + t.id); render(); };
      tabs.appendChild(b);
    });
  }

  function render() {
    renderTabs();
    var t = TRACKERS.filter(function (x) { return x.id === current; })[0];
    var q = search.value.trim().toLowerCase();
    var pct = t.items.length ? Math.round(count(t) / t.items.length * 100) : 0;
    var html = "<p>" + t.intro + "</p>";
    if (!t.items.length) {
      html += '<div class="panel empty"><strong>Full list coming at launch.</strong><p>We will add every ' + t.title.toLowerCase() +
        ' entry after GTA 6 comes out on November 19, 2026. Your ticks will save here as you play.</p></div>';
      box.innerHTML = html; return;
    }
    html += '<div class="progress" role="progressbar" aria-valuenow="' + pct + '" aria-valuemin="0" aria-valuemax="100" aria-label="' + t.title + ' progress">' +
      '<span style="--w:' + pct + '%"></span></div><p class="note num">' + count(t) + " of " + t.items.length + " done (" + pct + "%)</p><ul class=\"tlist\">";
    t.items.forEach(function (i) {
      if (q && (i.name + " " + (i.note || "") + " " + (i.area || "")).toLowerCase().indexOf(q) < 0) return;
      var key = t.id + ":" + i.id, id = "t-" + t.id + "-" + i.id;
      html += '<li><input type="checkbox" id="' + id + '" data-key="' + key + '"' + (done[key] ? " checked" : "") + '>' +
        '<label for="' + id + '"><strong>' + i.name + "</strong>" + (i.area ? ' <span class="note">' + i.area + "</span>" : "") +
        (i.note ? "<br><small>" + i.note + "</small>" : "") + "</label></li>";
    });
    box.innerHTML = html + "</ul>";
  }

  box.addEventListener("change", function (e) {
    var k = e.target.getAttribute("data-key"); if (!k) return;
    if (e.target.checked) done[k] = 1; else delete done[k];
    persist(); render();
    var el = document.getElementById(e.target.id); if (el) el.focus();
  });
  search.addEventListener("input", render);
  render();
})();
