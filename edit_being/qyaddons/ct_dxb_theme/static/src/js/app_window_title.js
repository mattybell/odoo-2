odoo.define('app_system_name', function (require) {
"use strict";

var WebClient = require('web.WebClient');

WebClient.include({
    init: function() {
        this._super.apply(this, arguments);
        this.set('title_part', {"zopenerp": '店小宝'});
    }
});
});