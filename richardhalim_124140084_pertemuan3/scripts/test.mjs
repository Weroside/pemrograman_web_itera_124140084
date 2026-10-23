import { spawnSync } from "node:child_process";

// Node 25+ mengekspos web storage bawaan yang bertabrakan dengan jsdom.
const flags =
  Number(process.versions.node.split(".")[0]) >= 25
    ? ["--no-experimental-webstorage"]
    : [];
const result = spawnSync(
  process.execPath,
  [...flags, "node_modules/vitest/vitest.mjs", ...process.argv.slice(2)],
  { stdio: "inherit", env: { ...process.env, NODE_OPTIONS: [process.env.NODE_OPTIONS, ...flags].filter(Boolean).join(" ") } },
);
if (result.error) console.error(result.error.message);
process.exit(result.status ?? 1);
