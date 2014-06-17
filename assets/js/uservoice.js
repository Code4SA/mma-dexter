// Include the UserVoice JavaScript SDK (only needed once on a page)
UserVoice=window.UserVoice||[];(function(){var uv=document.createElement('script');uv.type='text/javascript';uv.async=true;uv.src='//widget.uservoice.com/qGPIRwFbJsjxVpWBc7cZ1g.js';var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(uv,s)})();

// Set colors
UserVoice.push(['set', {
  accent_color: '#448dd6',
  trigger_color: 'white',
  trigger_background_color: 'rgba(46, 49, 51, 0.6)'
}]);

// Add default trigger to the bottom-right corner of the window:
UserVoice.push(['addTrigger', { mode: 'contact', trigger_position: 'bottom-right' }]);

(function () {
  var $body = $('body');
  if ($body.hasClass('loggedin')) {
    UserVoice.push(['identify', {
      email: $body.data('user-email'),
      name: $body.data('user-name'),
      id: $body.data('user-id'),
    }]);
  }
})();
