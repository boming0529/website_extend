odoo.define('heroes.component', function (require) {
    'use strict'

    var ajax = require('web.ajax');
    let core = require('web.core');
    let Widget = require('web.Widget');
    
    var qweb = core.qweb;
    var _t = core._t;


    var Hero = Widget.extend({
        template: 'demo.heroes',
        init: function (el) {
            this._super(el, arguments);
            this.heroes = []
        },
        willStart: function () {
            this.heroes = [{
                'id': 11,
                'name': _t('Mr.Nice')
            }, {
                'id': 12,
                'name': _t('Narco')
            }]
            return ajax.loadXML('/website_widget_demo/static/src/xml/heroes.xml', qweb);
        },
        start: function () {
            
        },
    })

    $(function() {
        let container = $('#my_heroes');
        console.log(container)
        new Hero(this).appendTo(container);
    })

    return {
        Hero: Hero
    }
})