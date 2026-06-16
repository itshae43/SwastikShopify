import * as tools from 'file:///C:/Users/Acer/AppData/Local/npm-cache/_npx/e91237b7ba36707d/node_modules/@shopify/dev-mcp/dist/tools.js';

async function test() {
  try {
    const result = await tools.validateThemeToolDef().handler({
      absoluteThemePath: 'c:\\Users\\Acer\\Dev\\swastik-shopify',
      filesCreatedOrUpdated: [
        { path: 'locales/en.default.json' },
        { path: 'sections/gold-collection-showcase.liquid' },
        { path: 'templates/index.json' }
      ]
    });
    console.log("Validation Result:", JSON.stringify(result, null, 2));
  } catch (err) {
    console.error("Error running validation:", err);
  }
}

test();








