/**
 * Creates a nested hash structure of the languages directory
 * @module hcaptcha-i18n
 * @type {Object}
 */
var requireDirectory = require('require-directory');
module.exports = requireDirectory(module, "./languages");