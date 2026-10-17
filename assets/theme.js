/* Theme runs separately so an unrelated page feature cannot disable it. */
(function () {
  'use strict';
  var root = document.documentElement;
  var media = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  var selected = null;
  try { selected = localStorage.getItem('sir-theme'); } catch (_) {}
  if (selected !== 'light' && selected !== 'dark') selected = null;
  function current() { return root.dataset.theme; }
  function labels() {
    document.querySelectorAll('[data-theme]').forEach(function (button) {
      var dark = current() === 'dark';
      button.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
      button.setAttribute('title', dark ? 'Switch to light theme' : 'Switch to dark theme');
      button.setAttribute('aria-pressed', String(dark));
      var text = button.querySelector('[data-theme-label]');
      var icon = button.querySelector('[data-theme-icon]');
      if (text) text.textContent = dark ? 'Light' : 'Dark';
      if (icon) icon.textContent = dark ? '☀' : '☾';
    });
  }
  function set(value, persist) {
    root.dataset.theme = value;
    root.style.colorScheme = value;
    if (persist) {
      selected = value;
      try { localStorage.setItem('sir-theme', value); } catch (_) {}
    }
    labels();
  }
  set(selected || (media && media.matches ? 'dark' : 'light'), false);
  function bind() {
    document.querySelectorAll('[data-theme]').forEach(function (button) {
      button.addEventListener('click', function () { set(current() === 'dark' ? 'light' : 'dark', true); });
    });
    labels();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bind, { once: true });
  else bind();
  if (media && media.addEventListener) media.addEventListener('change', function (event) {
    if (!selected) set(event.matches ? 'dark' : 'light', false);
  });
})();
