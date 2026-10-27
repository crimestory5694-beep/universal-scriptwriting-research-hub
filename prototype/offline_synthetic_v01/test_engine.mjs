#!/usr/bin/env node
// Run: node test_engine.mjs
// Uses Node standard library only; all inputs are entirely fictional.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { evaluate } from "./engine.mjs";

const sample = JSON.parse(readFileSync(new URL("./sample.json", import.meta.url), "utf8"));
const cases = JSON.parse(readFileSync(new URL("./test_cases.json", import.meta.url), "utf8"));
const copy = () => JSON.parse(JSON.stringify(sample));
function apply(doc, patches) {
  for (const patch of patches) {
    const steps = patch.path.split(".");
    let target = doc;
    for (const key of steps.slice(0, -1)) target = target[key];
    target[steps[steps.length - 1]] = patch.value;
  }
}
const positive = evaluate(copy());
assert.equal(positive.status, "RESEARCH_ONLY_TERMINAL");
assert.equal(positive.production_allowed, false);
assert.ok(positive.artifact.draft.includes("entirely fictional"));
let passes = 1;
const failures = [];
for (const row of cases) {
  const doc = copy();
  apply(doc, row.patches);
  const actual = evaluate(doc);
  const expected = row.expected;
  const pass = expected === "RESEARCH_ONLY_TERMINAL"
    ? actual.status === expected && actual.production_allowed === false
    : actual.status === "HOLD" && actual.hold_reasons.includes(expected) && actual.artifact === null;
  if (pass) passes++;
  else failures.push({id:row.id,expected,actual:actual.status,reasons:actual.hold_reasons});
}
assert.equal(cases.length, 36);
if (failures.length) {
  console.error("FAILED:", JSON.stringify(failures, null, 2));
  process.exitCode = 1;
} else {
  console.log("PASS", passes, "/", cases.length + 1, "offline synthetic execution checks.");
  console.log("No real-source verification, human review, production Skill or Claude transfer performed.");
}
