window.init = window.init || {};

init = {
	console: function() {
		var method;
		var noop = function noop() {};
		var methods = [
			'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
			'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
			'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
			'timeStamp', 'trace', 'warn'
		];
		var length = methods.length;
		var console = (window.console = window.console || {});

		while (length--) {
			method = methods[length];
			if (!console[method]) {
				console[method] = noop;
			}
		}
	},
	basic: function() {
		jQuery('html').removeClass('no-js');
	},
	showHide: function() {
		jQuery('.home .news-posts .post:first .read-more').addClass('hidden');
		jQuery('.home .news-posts .body').not('.body:first').addClass('hidden');
		jQuery('.read-more a').on('click', function(event) {
			event.preventDefault();
			var anchor = jQuery(this),
				body = anchor.closest('.post').find('.body').not(':animated'),
				txt = anchor.hasClass('point-down') ? 'Close' : 'Read More';
			anchor.toggleClass('point-down point-up').text(txt);
			body.slideToggle('fast', 'linear');
		});
	},
	documentationSelect: function() {
		jQuery('#latest-documentation').on('change', function() {
			var url = jQuery(this).val();
			if (url) {
				window.location = url;
			}
			return false;
		});
	}
};

/* jQuery functions to run after page is loaded */
jQuery(document).ready(function() {
	jQuery.each(init,
		function(i, item) {
			item();
		}
	);
	if (window.location.href.indexOf('product') > -1 || window.location.href.indexOf('product.html') > -1) {
		jQuery('.menu-item-28').addClass('current-menu-item');
		jQuery('.section-head').first().hide();
	}
	else if (window.location.href.indexOf('documentation') > -1 || window.location.href.indexOf('documentation.html') > -1) {
		jQuery('.menu-item-25').addClass('current-menu-item');
	}
	else if (window.location.href.indexOf('community') > -1 || window.location.href.indexOf('community.html') > -1) {
		jQuery('.menu-item-24').addClass('current-menu-item');
	}
	else if (window.location.href.indexOf('download') > -1 || window.location.href.indexOf('thank') > -1 || window.location.href.indexOf('download.html') > -1 || window.location.href.indexOf('thank.html') > -1 ) {

	}
	else {
		jQuery('.menu-item-27').addClass('current-menu-item');
	}
});


//Product page
jQuery(document).ready(function () {
  jQuery('#features-link').click(function () {
        jQuery('.features-posts').show();
        jQuery('.overview-tab').hide();
        jQuery('.resources').hide();
        jQuery('#menu-item-69').removeClass('current-menu-item');
        jQuery('#menu-item-68').addClass('current-menu-item');
  });
  jQuery('#overview-link').click(function () {
        jQuery('.features-posts').hide();
        jQuery('.overview-tab').show();
        jQuery('.resources').show();
        jQuery('#menu-item-69').addClass('current-menu-item');
        jQuery('#menu-item-68').removeClass('current-menu-item');
  });
});


//Google analytics1
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-45382226-1']);
_gaq.push(['_trackPageview']);
(function() {
	var ga = document.createElement('script');
	ga.type = 'text/javascript';
	ga.async = true;
	ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
	var s = document.getElementsByTagName('script')[0];
	s.parentNode.insertBefore(ga, s);
})();