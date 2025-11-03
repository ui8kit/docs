# Package Structure

## Overview

The Package Structure defines how UI8Kit/Core is configured, packaged, and distributed through `package.json`. It supports multiple integration formats and distribution methods.

## Package.json Configuration

### Main Entry Points

The library configures multiple entry points for different use cases:

```json
{
  "main": "dist/index.js",
  "module": "dist/index.es.js",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.es.js",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  }
}
```

### Export Points

Different export patterns enable various integration scenarios:

```json
{
  "exports": {
    ".": {
      "import": "./dist/index.es.js",
      "require": "./dist/index.js"
    },
    "./button": {
      "import": "./dist/components/ui/button/index.es.js",
      "require": "./dist/components/ui/button/index.js"
    },
    "./card": {
      "import": "./dist/components/ui/card/index.es.js",
      "require": "./dist/components/ui/card/index.js"
    }
  }
}
```

## Distribution Formats

### 1. CommonJS (CJS)
For Node.js and older module systems:

```
dist/index.js
dist/components/ui/button/index.js
dist/components/ui/card/index.js
```

Usage:
```javascript
const { Button } = require('ui8kit-core');
```

### 2. ES Modules (ESM)
For modern JavaScript environments:

```
dist/index.es.js
dist/components/ui/button/index.es.js
dist/components/ui/card/index.es.js
```

Usage:
```javascript
import { Button } from 'ui8kit-core';
import Button from 'ui8kit-core/button';
```

### 3. TypeScript Definitions
Type definitions for full type safety:

```
dist/index.d.ts
dist/components/ui/button/index.d.ts
dist/components/ui/card/index.d.ts
```

## Dependencies

### Runtime Dependencies

Core dependencies that are required:

```json
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "class-variance-authority": "^0.7.0",
    "classnames": "^2.3.0"
  }
}
```

- **react** - React library for component rendering
- **react-dom** - React DOM utilities
- **class-variance-authority** - CVA variant system
- **classnames** - Class name utility (cx function)

### Development Dependencies

Tools for building and testing:

```json
{
  "devDependencies": {
    "typescript": "^5.0.0",
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0",
    "tailwindcss": "^3.0.0"
  }
}
```

- **typescript** - TypeScript compiler
- **@types/react** - React TypeScript definitions
- **@types/react-dom** - React DOM TypeScript definitions
- **tailwindcss** - Tailwind CSS framework

## Build Scripts

Common build scripts in `package.json`:

```json
{
  "scripts": {
    "build": "tsc && tailwindcss build",
    "build:ts": "tsc",
    "build:types": "tsc --declaration",
    "dev": "tsc --watch",
    "test": "jest",
    "lint": "eslint src/",
    "prepublishOnly": "npm run build"
  }
}
```

## Integration Formats

### 1. NPM Installation
Standard package manager installation:

```bash
npm install ui8kit-core
```

Usage:
```javascript
import { Button, Card } from 'ui8kit-core';
```

### 2. Per-Component Installation
Install individual components via CLI:

```bash
npx buildy-ui add button
npx buildy-ui add card
```

### 3. JSON Registry
Component metadata for programmatic access:

```json
{
  "components": [
    {
      "name": "Button",
      "path": "components/ui/button",
      "description": "Primary button component"
    }
  ]
}
```

### 4. Git Submodule
For monorepo integration:

```bash
git submodule add https://github.com/org/ui8kit-core libs/ui8kit-core
```

### 5. Source Integration
Direct source file usage:

```typescript
import { Button } from '../path/to/ui8kit-core/src/components/ui/button';
```

## Version Management

### Semantic Versioning

Follow semantic versioning (semver):

```
MAJOR.MINOR.PATCH
3.2.1
│ │ └─ Patch (bug fixes)
│ └─── Minor (new features, backward compatible)
└───── Major (breaking changes)
```

### Changelog

Maintain a `CHANGELOG.md` documenting releases:

```markdown
## [3.2.0] - 2024-01-15

### Added
- New Flex layout component
- Button size variant

### Fixed
- Card border radius issue

### Changed
- Updated TypeScript to 5.3
```

## Publishing to NPM

### Authentication

```bash
npm login
npm whoami
```

### Publishing

```bash
npm publish
```

### Pre-publish Scripts

Run tests and build before publishing:

```bash
npm run test
npm run build
npm publish
```

## Best Practices

### 1. Semantic Export Names
```json
{
  "exports": {
    "./button": "./dist/components/ui/button/index.js",
    "./card": "./dist/components/ui/card/index.js"
  }
}
```

### 2. Include Type Definitions
```json
{
  "types": "dist/index.d.ts"
}
```

### 3. Manage Dependencies Carefully
- List all required dependencies
- Pin dev dependencies to prevent breaking builds
- Use peer dependencies for flexible integration

### 4. Clear Entry Points
```json
{
  "main": "dist/index.js",
  "module": "dist/index.es.js"
}
```

## Next Steps

- [Build System](../build-system/README.md) - Learn how to build the package
- [Component Registry](../component-registry/README.md) - Understand component metadata
- [TypeScript Configuration](../typescript-configuration/README.md) - Review type setup
