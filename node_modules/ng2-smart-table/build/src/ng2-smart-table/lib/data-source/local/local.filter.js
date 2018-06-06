"use strict";
var LocalFilter = (function () {
    function LocalFilter() {
    }
    LocalFilter.filter = function (data, field, search, customFilter) {
        var filter = customFilter ? customFilter : this.FILTER;
        return data.filter(function (el) {
            var value = typeof el[field] === 'undefined' || el[field] === null ? '' : el[field];
            return filter.call(null, value.toString().toLowerCase(), search.toString().toLowerCase());
        });
    };
    LocalFilter.FILTER = function (value, search) {
        return value.includes(search);
    };
    return LocalFilter;
}());
exports.LocalFilter = LocalFilter;
