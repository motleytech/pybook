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
    
    function toPy(jsobj, ident, cb) {
        var kernel = IPython.notebook.kernel;
        var jsdata = JSON.stringify(jsobj)
        var code_input = "import json; ";
        var code_input = code_input + ident + " = json.loads('" + jsdata + "')";
        var callbacks = undefined;
        if (cb) {
            callbacks = { 'iopub' : {'output' : cb}};
        }
        
        var msg_id = kernel.execute(code_input, callbacks);
    };

    function toJs(pyIdent, cb) {
        var kernel = IPython.notebook.kernel;
        function callback(out){
            var res = null;
            
            // if output is a print statement
            if(out.msg_type == "stream"){
                res = out.content.text;
                res = JSON.parse(res);
            }
            
            // if output is a python object
            else if(out.msg_type === "pyout"){
                res = out.content.data["text/plain"];
                res = JSON.parse(res);
            }
            
            // if output is executing result
            else if(out.msg_type === "execute_result"){
                res = out.content.data["text/plain"];
                res = JSON.parse(res);
            }
            
            // if output is a python error
            else if(out.msg_type == "pyerr"){
                res = out.content.ename + ": " + out.content.evalue;
            }
            
            // if output is something we haven't thought of
            else{
                res = "[out type not implemented]";  
            }
            
            if (cb) {
                cb(res);
            }
            
        }
        
        var callbacks = { 'iopub' : {'output' : callback}};
        var code_input = "import json; print json.dumps(" + pyIdent + ")";
        var msg_id = kernel.execute(code_input, callbacks, {silent:false});
    };
    
    function loadJs(jsPath, cb) {
        require(jsPath, function(lib) {
            cb(lib);
        });
    };
    
    function log(mesg, elem) {
        if (elem) {
            elem.append("<p>" + mesg + "</p>");
        } else {
            console.log(mesg);
        }
    };
    

    var load_ipython_extension = function() {
        console.log("loaded custom.js file");
        load_css("/nbextensions/custom/custom.css")

        if (!window.nbvars) {
            window.nbvars = {};
        }
        
        window.nbvars['toPy'] = toPy;
        window.nbvars['toJs'] = toJs;
        window.nbvars['load'] = loadJs;
        window.nbvars['log'] = log;
        
    };

    var extension = {
        load_ipython_extension : load_ipython_extension
    };
    return extension;
});
