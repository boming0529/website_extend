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
            var self = this;
            this.get_hero().then(function (datas) { 
                self.heroes = datas
            });
            return ajax.loadXML('/website_widget_demo/static/src/xml/heroes.xml', qweb);
        },
        start: function () {

        },
        get_hero: function () {
            return new Promise(function (resolve, reject) {
                var datas = {
                    'jsonrpc': '2.0',
                    'method': 'call',
                    'params': {},
                    'id': Math.floor(Math.random() * 1000 * 1000 * 1000)
                }
                $.ajax({
                    type: 'POST',
                    url: '/get/heroes/',
                    dataType: 'json',
                    data: JSON.stringify(datas),
                    async: true,
                    contentType: "application/json; charset=utf-8",
                }).done(function (data) {
                    var jsondata = JSON.parse(data.result);
                    resolve(jsondata.heroes);
                })
            });
        }
    })

    $(function () {
        let container = $('#my_heroes');
        if (container) {
            new Hero(this).appendTo(container);
        }
    })

    return {
        Hero: Hero
    }
})