const esbuild = require("esbuild");

esbuild
  .build({
    entryPoints: ["adapter.js"], // Your entry file
    bundle: true,
    outfile: "adapter.bundle.js", // Output bundled file
    platform: "node", // Target platform
    minify: true, // Minify the code
    format: "cjs",
  })
  .catch(() => process.exit(1));
