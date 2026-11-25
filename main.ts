// news-image-20261124 — entry point (Node 22, standard library only).
//
// render.py paints the whole collage and saves it as entry.png beside this
// file. This program does nothing creative: it hands that finished PNG to
// the harness. Before copying, it checks the file really is a PNG — the
// first four bytes must be the PNG signature 89 50 4E 47 — and refuses to
// copy anything else, so a broken render can never slip through silently.
//
// Run it locally like this:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { closeSync, copyFileSync, openSync, readSync } from 'node:fs';
import { join } from 'node:path';

const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47]);

const source = new URL('./entry.png', import.meta.url);
const handle = openSync(source, 'r');
const head = Buffer.alloc(4);
readSync(handle, head, 0, 4, 0);
closeSync(handle);
if (!head.equals(PNG_SIGNATURE)) {
  throw new Error('entry.png is not a PNG file (bad magic bytes)');
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
copyFileSync(source, join(outDir, 'entry.png'));
