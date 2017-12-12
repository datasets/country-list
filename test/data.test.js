const test = require('ava')
const originalData = require('../data.json');

const countries = require('../index.js')

originalData.map (obj => {
  test(`${obj.Name}`, async t => {
    const outCode = await countries.getCode(obj.Name)
    const outName = await countries.getName(obj.Code)
    t.is(outCode, obj.Code)
    t.is(outName, obj.Name)
  })
})

test('All names and codes', async t => {
  const outCodes = await countries.getCodes()
  const outNames = await countries.getNames()
  t.is(outNames[0], 'Afghanistan')
  t.is(outCodes[1], 'AX')
})