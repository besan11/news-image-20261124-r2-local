// Entry for news-image-20261124 (Node 22, standard library only).
// The image is rendered by render.py and shipped as entry.png beside this
// file; this program copies it to the output directory, unchanged.
// Run locally: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
