import * as tools from 'file:///C:/Users/Acer/AppData/Local/npm-cache/_npx/e91237b7ba36707d/node_modules/@shopify/dev-mcp/dist/tools.js';

console.log("validateThemeToolDef source:");
console.log(tools.validateThemeToolDef.toString());

try {
  const result = tools.validateThemeToolDef();
  console.log("Called validateThemeToolDef():", typeof result, result);
} catch (e) {
  console.error("Error calling validateThemeToolDef():", e);
}
