odoo.define('heroes.component', function (require) {
    'use strict'

    var ajax = require('web.ajax');
    var rpc = require('web.rpc');
    let core = require('web.core');
    let Widget = require('web.Widget');

    var qweb = core.qweb;
    var _t = core._t;


    var Hero = Widget.extend({
        template: 'demo.heroes',
        xmlDependencies: ['/website_widget_demo/static/src/xml/heroes.xml'],
        init: function (el, heroes) {
            this._super(el, arguments);
            this.heroes = heroes
        },
        start: function () {

        },
        
    })

    $(function () {

        var get_hero = function() {
            return new Promise(function (resolve, reject) {
                var self = this;
                rpc.query({
                    route: '/get/heroes/',
                    method: 'post',
                    params: {}
                }).then(function (data) {
                    resolve(data.heroes);
                })
            });
        }

        let container = $('#my_heroes');
        if (container) {
            // DI 
            get_hero().then(function (heroes) {
                new Hero(this, heroes).appendTo(container);
            });
        }
    })

    return {
        Hero: Hero
    }
})