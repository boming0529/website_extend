odoo.define('heroes.component', function (require) {
    'use strict'

    var ajax = require('web.ajax');
    var rpc = require('web.rpc');
    let core = require('web.core');
    let Widget = require('web.Widget');
    let Detail = require('heroes.component.detail');

    var qweb = core.qweb;
    var _t = core._t;


    var Hero = Widget.extend({
        template: 'demo.heroes',
        xmlDependencies: ['/website_widget_demo/static/src/xml/heroes.xml'],
        events: {
            'click li': '_onSelect'
        },
        init: function (heroes) {
            this._super.apply(this, arguments);
            this.heroes = heroes;
            this.selectedHero = heroes[0].id;
            this.detailwidget = undefined;
        },
        start: function () {
            let $firstli = this.$el.find('li:eq(0)');
            this.select_toggle($firstli);
            let $detailContainer = $('div.heroes_detail');
            this.detail_toggle($detailContainer);
        },
        _onSelect(ev) {
            let $target = $(ev.currentTarget);
            this.select_toggle($target);

            let $detail = $('div.heroes_detail');
            this.detail_toggle($detail);
        },
        select_toggle: function ($target) {
            this.$el.find('li').removeClass('selected');
            $target.addClass('selected');
            this.selectedHero = $target.data('hero');
        },
        detail_toggle: function ($detail) {
            if (this.detailwidget) this.detailwidget.destroy();
            let hero = _.find(this.heroes, (item) => item.id == this.selectedHero);
            this.detailwidget = new Detail(hero);
            this.detailwidget.appendTo($detail);
        },
    })

    $(function () {

        var get_hero = function () {
            return new Promise(function (resolve, reject) {
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
                new Hero(heroes).appendTo(container);
            });
        }
    })

    return {
        Hero: Hero
    }
})