import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { REMOVED, redactPersonal } from "../privacy";

const clean = (text: string) => redactPersonal(text).text;

describe("redactPersonal", () => {
  it("removes Pakistani and international phone numbers", () => {
    for (const phone of [
      "0300 1234567",
      "0300-1234567",
      "03001234567",
      "+92 300 1234567",
      "+923001234567",
      "0092 300 1234567",
      "92 300 1234567",
      "300 1234567",
      "(042) 3576-1234",
      "۰۳۰۰۱۲۳۴۵۶۷",
    ]) {
      assert.equal(clean(`call ${phone} now`), `call ${REMOVED.phone} now`, phone);
    }
    assert.deepEqual(redactPersonal("0300 1234567").removed, ["phone"]);
  });

  it("removes emails, links and ID card numbers", () => {
    assert.equal(clean("mail ali.khan@gmail.com"), `mail ${REMOVED.email}`);
    assert.equal(clean("ali (at) gmail (dot) com"), REMOVED.email);
    assert.equal(clean("ali at gmail dot com"), REMOVED.email);
    assert.equal(clean("see www.facebook.com/ali"), `see ${REMOVED.link}`);
    assert.equal(clean("https://wa.me/923001234567"), REMOVED.link);
    assert.equal(clean("35202-1234567-1"), REMOVED.id);
  });

  it("removes addresses in English, Roman Urdu and Urdu", () => {
    assert.equal(
      clean("I live in house no 12 street 5 mohalla Islampura"),
      `I live in ${REMOVED.address} ${REMOVED.address} ${REMOVED.address}`,
    );
    assert.equal(clean("gali number 3"), REMOVED.address);
    assert.equal(clean("makan # 45-B"), REMOVED.address);
    assert.equal(clean("plot no 7"), REMOVED.address);
    const urdu = clean("مکان نمبر ۱۲ گلی نمبر 3");
    assert.equal(urdu, `${REMOVED.address} ${REMOVED.address}`);
  });

  it("keeps maths and science answers as they are", () => {
    for (const answer of [
      "x = 12",
      "3/4 = 0.75",
      "1/2 + 1/4 = 3/4",
      "0.5 0.25 0.125 0.0625",
      "10 20 30 40 50 60",
      "05 10 15 20 25",
      "1 2 3 4 5 6 7 8 9 10 11 12",
      "2x + 3 = 11 so x = 4",
      "1000000 is a million",
      "area = 12345 cm2",
      "plot 3 points on the graph",
      "the sector 2 has angle 60",
      "2H2 + O2 -> 2H2O",
      "2023 2024 2025",
      "ہر روٹی کے دو آدھے، تو 3 روٹیوں کے 6 آدھے",
    ]) {
      assert.deepEqual(redactPersonal(answer), { text: answer, removed: [] }, answer);
    }
  });
});
