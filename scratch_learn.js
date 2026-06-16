import { getEnabledAPIsForLearning, getAPIInstructions } from 'file:///C:/Users/Acer/AppData/Local/npm-cache/_npx/e91237b7ba36707d/node_modules/@shopify/dev-mcp/dist/tools.js';

try {
  const apis = getEnabledAPIsForLearning();
  
  for (const api of apis) {
    if (api.name === 'liquid') {
      console.log(`\n--- Learning API: ${api.name} ---`);
      const instructions = getAPIInstructions(api.name);
      console.log(instructions);
    }
  }
} catch (e) {
  console.error("Error running learn:", e);
}
