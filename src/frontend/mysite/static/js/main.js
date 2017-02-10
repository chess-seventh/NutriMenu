"use strict";

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };

function swap(x, y) {
    if (x != y) {
        var old = x;
        var _tmp = x;
        x = y;
        y = _tmp;
    }

    console.log(typeof old === "undefined" ? "undefined" : _typeof(old)); // number
    console.log(typeof tmp === "undefined" ? "undefined" : _typeof(tmp)); // undefined
}
//# sourceMappingURL=main.js.map
