/* AIEM — menu, lead forms, tracking hooks. No dependencies. */
(function () {
  "use strict";

  // Mobile menu
  var btn = document.querySelector(".menu-btn");
  var nav = document.getElementById("nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Capture UTM / click ids for CRO attribution
  var params = new URLSearchParams(window.location.search);
  var attrib = {};
  ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "fbclid"].forEach(function (k) {
    var v = params.get(k);
    if (v) { attrib[k] = v; try { sessionStorage.setItem("aiem_" + k, v); } catch (e) {} }
    else { try { var s = sessionStorage.getItem("aiem_" + k); if (s) attrib[k] = s; } catch (e) {} }
  });

  window.dataLayer = window.dataLayer || [];

  // Lead forms
  document.querySelectorAll("form[data-lead]").forEach(function (form) {
    var msg = form.querySelector(".form-msg");
    var sel = form.querySelector("select[name=service]");
    var pre = form.getAttribute("data-service");
    if (sel && pre) sel.value = pre;

    var en = form.getAttribute("data-lang") === "en";
    var T = en ? {
      name: "Enter your name.", contact: "Enter a phone number or email so we can reach you.",
      mail: "The email looks wrong. Check its format.", consent: "Accept the privacy policy to continue.",
      sending: "Sending…", error: "Sending failed. Try again or write to us by email or WhatsApp (links in the footer).",
      cfg: "The form is not connected to a mailbox yet. See README.md."
    } : {
      name: "Shkruani emrin tuaj.", contact: "Shkruani telefonin ose emailin që t'ju kontaktojmë.",
      mail: "Emaili duket i pasaktë. Kontrolloni formatin.", consent: "Pranoni politikën e privatësisë për të vazhduar.",
      sending: "Po dërgohet…", error: "Dërgimi nuk u krye. Provoni përsëri ose na shkruani me email ose WhatsApp (lidhjet në fund të faqes).",
      cfg: "Formulari nuk është lidhur ende me një pritës emaili. Shih README.md."
    };
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (msg) msg.textContent = "";
      var fd = new FormData(form);
      if (fd.get("website")) return; // honeypot
      var name = (fd.get("name") || "").toString().trim();
      var phone = (fd.get("phone") || "").toString().trim();
      var email = (fd.get("email") || "").toString().trim();
      if (!name) return fail(T.name);
      if (!phone && !email) return fail(T.contact);
      if (email && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return fail(T.mail);
      if (!form.querySelector("[name=consent]").checked) return fail(T.consent);

      var payload = {};
      fd.forEach(function (v, k) { if (k !== "website") payload[k] = v; });
      payload.page = location.pathname;
      payload.submitted_at = new Date().toISOString();
      Object.keys(attrib).forEach(function (k) { payload[k] = attrib[k]; });

      var submit = form.querySelector("button[type=submit]");
      var label = submit.textContent;
      submit.disabled = true; submit.textContent = T.sending;
      var endpoint = form.getAttribute("action");

      function done() {
        window.dataLayer.push({ event: "generate_lead", lead_service: payload.service || "", lead_page: payload.page });
        window.location.href = form.getAttribute("data-thanks") || "/multumim/";
      }
      function fallback() {
        submit.disabled = false; submit.textContent = label;
        fail(T.error);
      }

      if (!endpoint || endpoint === "#") { // not configured yet: show clear dev message
        submit.disabled = false; submit.textContent = label;
        return fail(T.cfg);
      }
      fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(payload) })
        .then(function (r) { if (r.ok) done(); else fallback(); })
        .catch(fallback);
    });

    function fail(t) { if (msg) { msg.textContent = t; msg.focus && msg.focus(); } return false; }
  });

  // Track CTA clicks (GA4 / GTM via dataLayer)
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[data-track]");
    if (a) window.dataLayer.push({ event: a.getAttribute("data-track"), link_url: a.href });
  });
})();
