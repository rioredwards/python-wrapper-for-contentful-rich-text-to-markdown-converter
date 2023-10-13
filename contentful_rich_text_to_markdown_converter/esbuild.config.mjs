import * as esbuild from "esbuild";

esbuild
  .build({
    entryPoints: ["adapter.mjs"], // Your entry file
    bundle: true,
    outfile: "adapter.bundle.js", // Output bundled file
    platform: "node", // Target platform
    minify: false, // Minify the code
  })
  .catch(() => process.exit(1));
