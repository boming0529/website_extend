odoo.define('heroes.component.detail', function (require) { 
    'use strict'

    let Widget = require('web.Widget');

    var Detail = Widget.extend({
        template: 'demo.heroes.detail',
        xmlDependencies: ['/website_widget_demo/static/src/xml/heroes_detail.xml'],
        init: function (hero) {
            this._super.apply(this, arguments);
            this.hero = hero;
            this.title = hero.name + ' details!';
        }
    })

    return Detail;
})