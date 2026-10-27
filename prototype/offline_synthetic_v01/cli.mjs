#!/usr/bin/env node
// Run: node cli.mjs sample.json output.json
// Offline, no dependencies, no network, no production export.
import { readFileSync, writeFileSync } from "node:fs";
import { evaluate } from "./engine.mjs";

try {
  const input = process.argv[2];
  if (!input) {
    process.stderr.write("Usage: node cli.mjs INPUT.json [OUTPUT.json]\n");
    process.exitCode = 3;
  } else {
    const doc = JSON.parse(readFileSync(input, "utf8"));
    const result = evaluate(doc);
    const output = JSON.stringify(result, null, 2) + "\n";
    if (process.argv[3]) {
      writeFileSync(process.argv[3], output, "utf8");
      process.stdout.write("Local synthetic diagnostics written.\n");
    } else {
      process.stdout.write(output);
    }
    process.exitCode = result.status === "RESEARCH_ONLY_TERMINAL" ? 0 : 2;
  }
} catch (error) {
  process.stderr.write("Input/output failure: " + String(error.message) + "\n");
  process.exitCode = 3;
}
