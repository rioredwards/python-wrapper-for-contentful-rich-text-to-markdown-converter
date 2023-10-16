const {
  convertRichTextToMarkdown,
} = require("./node-contentful-rich-text-to-markdown-converter/dist/index.js");

const rawRichText = process.argv[2];
if (!rawRichText || typeof rawRichText !== "string") {
  console.error("Please provide a rich text entry as an argument.");
  process.exit(1);
}

function main() {
  const document = JSON.parse(rawRichText);
  const result = convertRichTextToMarkdown(document);

  if (result === undefined) {
    console.error("Could not convert rich text to markdown.");
    process.exit(1);
  }

  // Log converted rich text to console (to be used in python script)
  console.log(result);
  process.exit(0);
}

main();
