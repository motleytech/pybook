// Restrict output in a codecell to a maximum length

define([
    'jquery',
], function($) {
    "use strict";

    var load_css = function(name) {
        var link = document.createElement("link");
        link.type = "text/css";
        link.rel = "stylesheet";
        link.href = require.toUrl(name);
        //link.href = name;
        document.getElementsByTagName("head")[0].appendChild(link);

    };

    var load_ipython_extension = function() {
        console.log("loaded custom.js file");
        load_css("/nbextensions/custom/custom.css")
    };

    var extension = {
        load_ipython_extension : load_ipython_extension
    };
    return extension;
});
