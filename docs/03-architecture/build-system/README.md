# Build System

## Overview

The Build System handles TypeScript compilation, type definition generation, and output preparation for distribution. It ensures the library is properly compiled and ready for NPM publication.

## Build Process

### Stage 1: TypeScript Compilation

TypeScript source files are compiled to JavaScript:

```bash
npm run build:ts
```

Process:
1. Read TypeScript configuration from `tsconfig.json`
2. Compile `.ts` and `.tsx` files to `.js`
3. Output to `dist/` directory
4. Generate source maps for debugging

### Stage 2: Type Definition Generation

TypeScript declarations are generated for type safety:

```bash
npm run build:types
```

Process:
1. Extract type information from source files
2. Generate `.d.ts` declaration files
3. Create type maps for IDE support
4. Output to `dist/` directory

### Stage 3: Output Processing

Final outputs are prepared:

```bash
npm run build
```

Complete process:
1. Clean previous build artifacts
2. Compile TypeScript to CommonJS
3. Compile TypeScript to ES Modules
4. Generate type definitions
5. Copy asset files
6. Verify output structure

## Build Configuration

### TypeScript Configuration

Main compiler settings in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM"],
    "declaration": true,
    "declarationMap": true,
    "outDir": "./dist",
    "strict": true,
    "moduleResolution": "node",
    "paths": {
      "@core/*": ["./src/core/*"],
      "@components/*": ["./src/components/*"],
      "@layouts/*": ["./src/layouts/*"]
    }
  }
}
```

Key settings:
- **target** - Output JavaScript version (ES2020)
- **module** - Module system (ESNext for flexibility)
- **declaration** - Generate `.d.ts` files
- **strict** - Strict type checking enabled
- **paths** - Import path aliases

### Build Scripts

Standard build scripts in `package.json`:

```json
{
  "scripts": {
    "build": "npm run build:clean && npm run build:ts && npm run build:types",
    "build:clean": "rm -rf dist/",
    "build:ts": "tsc --project tsconfig.json",
    "build:types": "tsc --project tsconfig.json --declaration --emitDeclarationOnly",
    "dev": "tsc --watch --project tsconfig.json",
    "prepublishOnly": "npm run build && npm run test"
  }
}
```

## Output Structure

After building, the `dist/` directory contains:

```
dist/
├── index.js                    # CommonJS main export
├── index.es.js                # ES module main export
├── index.d.ts                 # TypeScript declarations
├── core/
│   ├── ui/
│   │   ├── button/
│   │   │   ├── index.js
│   │   │   ├── index.es.js
│   │   │   └── index.d.ts
│   │   └── box/
│   │       ├── index.js
│   │       ├── index.es.js
│   │       └── index.d.ts
│   └── variants/
│       ├── index.js
│       ├── index.es.js
│       └── index.d.ts
├── components/
│   └── ui/
│       ├── card/
│       │   ├── index.js
│       │   ├── index.es.js
│       │   └── index.d.ts
│       └── ...
└── layouts/
    ├── index.js
    ├── index.es.js
    └── index.d.ts
```

## Build Commands

### Development Build

Continuous compilation while developing:

```bash
npm run dev
```

Features:
- Watches source files for changes
- Incremental compilation
- Fast rebuild times
- Useful for development workflow

### Production Build

Complete build for distribution:

```bash
npm run build
```

Process:
1. Cleans previous build
2. Compiles all TypeScript
3. Generates type definitions
4. Validates output
5. Ready for NPM publication

### Pre-publish Build

Automatic build before NPM publish:

```bash
npm publish
```

This triggers `prepublishOnly` script:
1. Runs build
2. Runs tests
3. Publishes to NPM

## Distribution Formats

### CommonJS Output

For Node.js and older environments:

```javascript
// dist/index.js
exports.Button = Button;
exports.Card = Card;
```

### ES Module Output

For modern JavaScript environments:

```javascript
// dist/index.es.js
export { Button };
export { Card };
```

### Type Definitions

For TypeScript support:

```typescript
// dist/index.d.ts
export declare const Button: React.ForwardRefExoticComponent<...>;
export declare const Card: React.ForwardRefExoticComponent<...>;
```

## Optimization Strategies

### 1. Tree-Shaking
Enable dead code elimination:

```json
{
  "sideEffects": false,
  "type": "module"
}
```

### 2. Code Splitting
Organize by functionality:

```
dist/
├── core/        # Core primitives
├── components/  # UI components
└── layouts/     # Layout systems
```

### 3. Type Definitions
Include `.d.ts` maps for better IDE support:

```typescript
"declarationMap": true
```

## Best Practices

### 1. Always Build Before Publishing
```bash
npm run build
npm publish
```

### 2. Verify Build Output
Check `dist/` directory:
- All files present
- Correct naming conventions
- Type definitions generated

### 3. Use Strict Mode
```typescript
"strict": true
```

### 4. Clean Before Building
```bash
rm -rf dist/
npm run build
```

## Troubleshooting

### Build Fails

Check:
1. TypeScript configuration
2. Syntax errors in source
3. Missing type definitions
4. Path aliases configuration

### Type Definition Issues

Verify:
1. `declaration: true` in tsconfig
2. Export statements are correct
3. Types are properly defined

### Module Resolution Errors

Check:
1. Import paths are correct
2. Path aliases in tsconfig match
3. Files exist in expected locations

## Next Steps

- [Package Structure](../package-structure/README.md) - Understand distribution formats
- [TypeScript Configuration](../typescript-configuration/README.md) - Deep dive into TypeScript setup
- [Component Registry](../component-registry/README.md) - Learn about component metadata
