const sendPaymentRequestToApi = require('./3-payment');
const chai = require('chai');
const expect = chai.expect;
const Utils = require('./utils');
const sinon = require('sinon');

describe('sendPaymentRequestToApi', function() {
  it('validate the usage of the Utils function', function() {
    sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20)
    expect(Utils.calculateNumber.calledOnce).to.be.true;
  })
})
