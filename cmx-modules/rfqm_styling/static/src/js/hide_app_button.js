odoo.define('custom_module.hide_app_button', function (require) {
    'use strict';

    const session = require('web.session');
    document.addEventListener('DOMContentLoaded', function () {
        session.user_has_group('base.group_system').then(function (isAdmin) {
            if (!isAdmin) {
                const appButton = document.querySelector('.o_navbar_apps_menu');
                if (appButton) {
                    appButton.style.display = 'none'; // Hide the App button for non-admins
                }
            }
        });
    });
});
