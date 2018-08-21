let countryList = require('./data.json');

// prepare data structures
let
    codeToName = new Object(),
    nameToCode = new Object(),
    names = new Array(),
    codes = new Array();

countryList.map( obj => {
    codeToName[obj.Code] = obj.Name;
    nameToCode[obj.Name] = obj.Code;

    names.push(obj.Name);
    codes.push(obj.Code);
});

module.exports = {
    getName : (code) => codeToName[code],
    getCode : (name) => nameToCode[name],
    getNames : () => names,
    getCodes : () => codes,
    getNameList : () => nameToCode,
    getCodeList : () => codeToName
};