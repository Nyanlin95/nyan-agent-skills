pen.dev CLI harness reading pack
================================

Installed package
-----------------

Package: @pen.dev/cli
Version: 0.3.2
Executable: C:\Users\nyanl\AppData\Roaming\npm\pen.cmd
Package root: C:\Users\nyanl\AppData\Roaming\npm\node_modules\@pen.dev\cli

What is readable
----------------

The npm package includes these readable first-party files:

- README.md: CLI commands, authentication, interactive mode, and examples.
- SKILL.md: agent instructions for using the CLI.
- package.json: package metadata, entry point, dependencies, and build scripts.
- dist/node_modules/@highagency/pencil-wasm/pencil.d.ts: editor engine type declarations.
- dist/node_modules/@highagency/pencil-wasm/enums.gen.d.ts: editor enum declarations.

The package does not include the original TypeScript harness source or source maps.
The harness implementation is compiled into large JavaScript modules in dist/.
The main entry point is dist/index.mjs. AgentHarness-related runtime code also
appears in dist/dist-BEo0Z8Vf.mjs. These files are text, but production bundling,
minification, and short identifiers make them difficult to read.

Published package metadata provides a tarball URL but no source repository or
homepage field. The tarball mirrors the installed npm package, so downloading it
does not provide uncompiled source.

Files in this reading pack
--------------------------

- interactive-harness.txt: readable interface exposed by `pen interactive`.
- package-layout.txt: important first-party package files and what they contain.
- design-agent-harness.md: recovered prompt assembly, design intelligence, tools,
  and verification loop.
- guides/: recovered task-specific design guidance.
- styles/: the style-archetype catalog and one resolved style example.

Original readable files
-----------------------

C:\Users\nyanl\AppData\Roaming\npm\node_modules\@pen.dev\cli\README.md
C:\Users\nyanl\AppData\Roaming\npm\node_modules\@pen.dev\cli\SKILL.md
C:\Users\nyanl\AppData\Roaming\npm\node_modules\@pen.dev\cli\package.json

Security note
-------------

The stored login session is not included. Do not copy or publish files from
%USERPROFILE%\.pencil that contain session credentials.
