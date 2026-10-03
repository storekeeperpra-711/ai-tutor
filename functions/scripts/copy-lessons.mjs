// Copies the lesson files into the functions folder before each build, so
// the deployed server has its own copy: prompts are built from the lesson
// on the server, never from text the app sends.
import { cpSync, mkdirSync, readdirSync, rmSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const from = join(here, "..", "..", "content", "lessons");
const to = join(here, "..", "lessons");

rmSync(to, { recursive: true, force: true });
mkdirSync(to, { recursive: true });
const files = readdirSync(from).filter((f) => f.endsWith(".json"));
for (const file of files) cpSync(join(from, file), join(to, file));
console.log(`Copied ${files.length} lessons to functions/lessons/`);
