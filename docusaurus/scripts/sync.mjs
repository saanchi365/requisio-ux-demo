// Before each build: reuse the files the MkDocs version already uses, so there is only one copy of each.
// - the three "Users" pages from ../docs
// - the flowchart diagrams from ../flowcharts (only the part between the [start:flow] and [end:flow] markers)
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const site = path.join(here, '..');
const repo = path.join(site, '..');

const users = path.join(site, 'docs/users');
fs.mkdirSync(users, {recursive: true});
['user-understanding', 'journey-map', 'use-cases'].forEach((name, i) => {
  const text = fs.readFileSync(path.join(repo, 'docs', `${name}.md`), 'utf8');
  fs.writeFileSync(path.join(users, `${name}.md`), `---\nsidebar_position: ${i + 1}\n---\n\n${text}`);
});

const data = JSON.parse(fs.readFileSync(path.join(site, 'src/data/requisio.json'), 'utf8'));
const flows = {};
for (const feature of data.features) {
  for (const {file} of feature.flows) {
    const text = fs.readFileSync(path.join(repo, file), 'utf8');
    const part = text.split('[start:flow]')[1].split('[end:flow]')[0];
    flows[file] = part.match(/```mermaid\r?\n([\s\S]*?)```/)[1].trim();
  }
}
fs.writeFileSync(path.join(site, 'src/data/flows.json'), JSON.stringify(flows, null, 2));
console.log(`synced 3 user pages and ${Object.keys(flows).length} flowcharts`);
