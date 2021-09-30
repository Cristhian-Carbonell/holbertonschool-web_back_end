const sendPaymentRequestToApi = require('./3-payment');
const assert = require('assert');
const Utils = require('./utils');
const sinon = require('sinon');

describe('sendPaymentRequestToApi', function() {
  it('validate the usage of the Utils function', function() {
    const spy = sinon.spy(sendPaymentRequestToApi(100, 20));
    const spyUtils = sinon.spy(Utils, 'calculateNumber');
  })
})
