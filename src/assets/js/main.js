/* AIEM: menu, language switcher, request form, language suggestion. No dependencies. */
(function () {
  "use strict";
  window.dataLayer = window.dataLayer || [];
  function track(ev, data) {
    var o = { event: ev, page: location.pathname };
    for (var k in data) o[k] = data[k];
    window.dataLayer.push(o);
  }

  // Mobile menu
  var btn = document.querySelector(".menu-btn");
  var nav = document.getElementById("nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Language switcher: close on outside click or Escape; remember the choice
  var lang = document.querySelector("details.lang");
  if (lang) {
    document.addEventListener("click", function (e) { if (!lang.contains(e.target)) lang.removeAttribute("open"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") lang.removeAttribute("open"); });
    lang.addEventListener("click", function (e) {
      var a = e.target.closest("a[data-lang]");
      if (a) { try { localStorage.setItem("aiem_lang", a.getAttribute("data-lang")); } catch (x) {} }
    });
  }

  // Capture campaign parameters so each request carries its source
  var params = new URLSearchParams(window.location.search);
  var attrib = {};
  ["utm_source", "utm_medium", "utm_campaign", "gclid"].forEach(function (k) {
    var v = params.get(k);
    try {
      if (v) sessionStorage.setItem("aiem_" + k, v);
      else v = sessionStorage.getItem("aiem_" + k);
    } catch (e) {}
    if (v) attrib[k] = v;
  });

  // Request form: posts to Google Apps Script, which emails the desk for the chosen service.
  // With no endpoint configured it falls back to opening the visitor's own email app.
  document.querySelectorAll("[data-req]").forEach(function (box) {
    var cfg;
    try { cfg = JSON.parse(box.getAttribute("data-req")); } catch (e) { return; }
    var form = box.querySelector("form");
    var status = box.querySelector(".req-status");
    var btn = form.querySelector("button[type=submit]");
    var started = Date.now(), began = false;

    form.elements.type.addEventListener("change", function () { track("support_type_selected", { support_type: form.elements.type.value }); });
    form.addEventListener("focusin", function () { if (!began) { began = true; track("form_start", { support_type: form.elements.type.value }); } });

    function say(t) { status.textContent = t; status.focus(); }
    function mark(el, bad) { if (bad) el.setAttribute("aria-invalid", "true"); else el.removeAttribute("aria-invalid"); }
    function ok(email, ref) {
      var done = document.createElement("div");
      done.className = "req-ok"; done.setAttribute("role", "status"); done.tabIndex = -1;
      var h = document.createElement("h3"); h.textContent = cfg.msgs.ok_title;
      var p = document.createElement("p"); p.textContent = cfg.msgs.ok_text.replace("{email}", email).replace("{ref}", ref || "");
      done.appendChild(h); done.appendChild(p);
      form.replaceWith(done); done.focus();
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.textContent = "";
      var f = form.elements;
      var name = f.name.value.trim(), email = f.email.value.trim(), country = f.country.value.trim(), message = f.message.value.trim();
      var bad = [
        [f.name, name.length < 2],
        [f.email, !/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(email)],
        [f.country, country.length < 2],
        [f.message, message.length < 40]
      ];
      var first = null;
      bad.forEach(function (b) { mark(b[0], b[1]); if (b[1] && !first) first = b[0]; });
      if (first) { first.focus(); return say(cfg.msgs.required); }
      if (!f.consent.checked) { f.consent.focus(); return say(cfg.msgs.consent); }

      var payload = {
        type: f.type.value, name: name, email: email, phone: f.phone.value.trim(), company: f.company.value.trim(), country: country,
        timeline: f.timeline.value, message: message,
        website: f.website.value, lang: cfg.lang, page: location.pathname, elapsed: Date.now() - started
      };
      for (var k in attrib) payload[k] = attrib[k];

      // No Apps Script endpoint yet: open the visitor's email app with the request filled in
      if (!cfg.endpoint) {
        var lines = [payload.message, "", cfg.labels[payload.type], "", name, email, payload.phone, payload.company, country, payload.timeline, cfg.langName]
          .filter(function (x, i) { return x || i < 2; });
        window.location.href = "mailto:" + (cfg.mail[payload.type] || "") + "?subject=" + encodeURIComponent("[" + cfg.labels[payload.type] + "] " + name) +
          "&body=" + encodeURIComponent(lines.join("\r\n"));
        track("generate_lead", { support_type: payload.type, lead_lang: cfg.lang, method: "mailto" });
        return say(cfg.msgs.fallback);
      }

      btn.disabled = true; btn.textContent = cfg.msgs.sending;
      function fail() {
        btn.disabled = false; btn.textContent = cfg.msgs.send;
        say(cfg.msgs.err);
        track("form_error", { support_type: payload.type });
      }
      // text/plain keeps this a "simple" request, so the browser sends no CORS preflight to Apps Script
      fetch(cfg.endpoint, { method: "POST", redirect: "follow", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify(payload) })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          if (!d || !d.ok) return fail();
          ok(email, d.ref);
          track("generate_lead", { support_type: payload.type, lead_lang: cfg.lang });
        })
        .catch(fail);
    });
  });

  // Root page: highlight the visitor's language (no forced redirect, so crawlers and users stay in control)
  var picker = document.querySelector(".langs");
  if (picker) {
    var want = [];
    try { want.push(localStorage.getItem("aiem_lang")); } catch (e) {}
    (navigator.languages || [navigator.language || ""]).forEach(function (l) { want.push((l || "").slice(0, 2).toLowerCase()); });
    for (var i = 0; i < want.length; i++) {
      var a = want[i] && picker.querySelector('a[data-lang="' + want[i] + '"]');
      if (a) { a.classList.add("suggested"); break; }
    }
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[data-track]");
    if (a) track(a.getAttribute("data-track"), { link_url: a.href });
  });
})();
