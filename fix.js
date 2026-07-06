const fs = require('fs');
const path = require('path');

const dir = 'i:\\02_Projects\\tablekard-landing-main';
const files = fs.readdirSync(dir);

const regex = /<script>\s*\(\s*function\s*\(\)\s*\{\s*var\s+btn\s*=\s*document\.getElementById\('nav-hamburger'\);[\s\S]*?\}\)\(\);\s*<\/script>/g;

files.forEach(file => {
  if (file.endsWith('.html')) {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');
    const matches = [...content.matchAll(regex)];
    
    if (matches.length > 1) {
      console.log('Fixing', file);
      // Remove the last match
      const lastMatch = matches[matches.length - 1];
      content = content.slice(0, lastMatch.index) + content.slice(lastMatch.index + lastMatch[0].length);
      fs.writeFileSync(filePath, content, 'utf8');
      console.log('Fixed', file);
    }
  }
});
