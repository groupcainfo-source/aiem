/* AIEM: menu, language switcher, email support desk, language suggestion. No dependencies. */
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

  // Support desk: builds the email links for the chosen support type
  function enc(s) { return encodeURIComponent(s); }
  document.querySelectorAll("[data-desk]").forEach(function (d) {
    var cfg;
    try { cfg = JSON.parse(d.getAttribute("data-desk")); } catch (e) { return; }
    var sel = d.querySelector("select");
    var out = d.querySelector(".desk-email");
    var mail = d.querySelector("[data-desk-mail]");
    var gm = d.querySelector("[data-desk-gmail]");
    var ol = d.querySelector("[data-desk-outlook]");
    var cp = d.querySelector("[data-desk-copy]");
    function cur() {
      for (var i = 0; i < cfg.types.length; i++) if (cfg.types[i].id === sel.value) return cfg.types[i];
      return cfg.types[0];
    }
    function update() {
      var t = cur();
      var subject = cfg.subject.replace(/\{type\}/g, t.label);
      var body = cfg.body.replace(/\{type\}/g, t.label).replace(/\{lang\}/g, cfg.lang).replace(/\n/g, "\r\n");
      var s = enc(subject), b = enc(body), to = enc(t.email);
      out.textContent = t.email;
      mail.href = "mailto:" + t.email + "?subject=" + s + "&body=" + b;
      gm.href = "https://mail.google.com/mail/?view=cm&fs=1&to=" + to + "&su=" + s + "&body=" + b;
      ol.href = "https://outlook.office.com/mail/deeplink/compose?to=" + to + "&subject=" + s + "&body=" + b;
    }
    sel.addEventListener("change", function () { update(); track("support_type_selected", { support_type: cur().id }); });
    [[mail, "mailto"], [gm, "gmail"], [ol, "outlook"]].forEach(function (p) {
      p[0].addEventListener("click", function () { track("support_email_click", { method: p[1], support_type: cur().id }); });
    });
    if (cp) {
      cp.addEventListener("click", function () {
        var t = cur();
        function ok() { cp.textContent = cfg.copied; setTimeout(function () { cp.textContent = cfg.copy; }, 1800); track("support_email_click", { method: "copy", support_type: t.id }); }
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t.email).then(ok, function () {});
        else { var ta = document.createElement("textarea"); ta.value = t.email; document.body.appendChild(ta); ta.select(); try { document.execCommand("copy"); ok(); } catch (e) {} document.body.removeChild(ta); }
      });
    }
    update();
  });


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

  // Request form: posts to Google Apps Script, which emails the desk for the chosen support type
  document.querySelectorAll("[data-req]").forEach(function (box) {
    var cfg;
    try { cfg = JSON.parse(box.getAttribute("data-req")); } catch (e) { return; }
    var form = box.querySelector("form");
    var status = box.querySelector(".req-status");
    var btn = form.querySelector("button[type=submit]");
    var mailSel = box.querySelector(".alt-mail select");
    var alt = box.querySelector(".alt-mail");
    var started = Date.now(), began = false;

    form.elements.type.addEventListener("change", function () {
      if (mailSel) { mailSel.value = form.elements.type.value; mailSel.dispatchEvent(new Event("change")); }
      track("support_type_selected", { support_type: form.elements.type.value });
    });
    form.addEventListener("focusin", function () { if (!began) { began = true; track("form_start", { support_type: form.elements.type.value }); } });

    function say(t) { status.textContent = t; status.focus(); }
    function mark(el, bad) { if (bad) el.setAttribute("aria-invalid", "true"); else el.removeAttribute("aria-invalid"); }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.textContent = "";
      var f = form.elements;
      var name = f.name.value.trim(), email = f.email.value.trim(), message = f.message.value.trim();
      var okName = name.length >= 2, okMail = /^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(email), okMsg = message.length >= 10;
      mark(f.name, !okName); mark(f.email, !okMail); mark(f.message, !okMsg);
      if (!okName || !okMail || !okMsg) { (!okName ? f.name : !okMail ? f.email : f.message).focus(); return say(cfg.msgs.required); }
      if (!f.consent.checked) { f.consent.focus(); return say(cfg.msgs.consent); }

      var payload = {
        type: f.type.value, name: name, email: email, company: f.company.value.trim(), message: message,
        website: f.website.value, lang: cfg.lang, page: location.pathname, elapsed: Date.now() - started
      };
      for (var k in attrib) payload[k] = attrib[k];

      btn.disabled = true; btn.textContent = cfg.msgs.sending;
      function fail() {
        btn.disabled = false; btn.textContent = cfg.msgs.send;
        if (alt) alt.open = true;
        say(cfg.msgs.err);
        track("form_error", { support_type: payload.type });
      }
      // text/plain keeps this a "simple" request, so the browser sends no CORS preflight to Apps Script
      fetch(cfg.endpoint, { method: "POST", redirect: "follow", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify(payload) })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          if (!d || !d.ok) return fail();
          var done = document.createElement("div");
          done.className = "req-ok"; done.setAttribute("role", "status"); done.tabIndex = -1;
          var h = document.createElement("h3"); h.textContent = cfg.msgs.ok_title;
          var p = document.createElement("p"); p.textContent = cfg.msgs.ok_text.replace("{email}", email).replace("{ref}", d.ref || "");
          done.appendChild(h); done.appendChild(p);
          form.replaceWith(done); if (alt) alt.remove(); done.focus();
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
