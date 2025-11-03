# TypeScript Configuration

## Overview

TypeScript Configuration in UI8Kit/Core provides full type safety, strict checking, and developer experience features through comprehensive `tsconfig.json` setup.

## Complete TypeScript Configuration

### Main Configuration File

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM"],
    "jsx": "react-jsx",
    "declaration": true,
    "declarationMap": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "paths": {
      "@core/*": ["./src/core/*"],
      "@components/*": ["./src/components/*"],
      "@layouts/*": ["./src/layouts/*"],
      "@types/*": ["./src/types/*"]
    }
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist", "**/*.test.ts", "**/*.test.tsx"]
}
```

## Configuration Options Explained

### Target and Module

```typescript
{
  "target": "ES2020",        // Output JavaScript version
  "module": "ESNext",        // Module system
  "lib": ["ES2020", "DOM"]   // Available APIs
}
```

- **target**: Controls JavaScript output version (ES2020 supports modern features)
- **module**: ESNext allows tooling to handle module transformation
- **lib**: Includes ES2020 and DOM APIs for React development

### JSX Configuration

```typescript
{
  "jsx": "react-jsx"  // Use new JSX transform (React 17+)
}
```

No need to import React in every file using JSX.

### Declaration Files

```typescript
{
  "declaration": true,       // Generate .d.ts files
  "declarationMap": true     // Generate source maps for declarations
}
```

Enables TypeScript definitions and better IDE support.

### Output Configuration

```typescript
{
  "outDir": "./dist",   // Output directory
  "rootDir": "./src"    // Input directory
}
```

Maps source files to distribution output.

### Strict Type Checking

```typescript
{
  "strict": true  // Enables all strict type checking options
}
```

Enables:
- `noImplicitAny` - Error on implicitly any types
- `strictNullChecks` - Strict null/undefined checking
- `strictFunctionTypes` - Strict function type checking
- `strictBindCallApply` - Strict bind/call/apply checking
- `strictPropertyInitialization` - Strict property initialization
- `noImplicitThis` - Error on implicit 'this' type

### Module Resolution

```typescript
{
  "moduleResolution": "node",   // Use Node.js style resolution
  "esModuleInterop": true       // Interop between CommonJS and ES modules
}
```

Ensures compatibility with npm packages and modern tooling.

### Path Aliases

```typescript
{
  "paths": {
    "@core/*": ["./src/core/*"],
    "@components/*": ["./src/components/*"],
    "@layouts/*": ["./src/layouts/*"]
  }
}
```

Enable clean imports:
```typescript
// Instead of
import { Button } from '../../../src/components/ui/button';

// Use
import { Button } from '@components/ui/button';
```

### Other Important Options

```typescript
{
  "skipLibCheck": true,                    // Skip type checking of .d.ts files
  "forceConsistentCasingInFileNames": true, // Enforce consistent file names
  "resolveJsonModule": true,               // Allow importing JSON
  "isolatedModules": true,                 // Each file transpiles independently
  "noEmit": true                           // Don't emit output (for IDE checking)
}
```

## Type Definitions

### Component Types

Well-typed component interfaces:

```typescript
// src/components/ui/button/index.tsx
import { forwardRef } from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', loading = false, ...props }, ref) => {
    return <button ref={ref} {...props} />;
  }
);

Button.displayName = 'Button';
```

### Variant Types

Type-safe variants:

```typescript
// src/core/variants/spacing.ts
import { cva, type VariantProps } from 'class-variance-authority';

const spacing = cva('', {
  variants: {
    padding: {
      xs: 'p-1',
      sm: 'p-2',
      md: 'p-4',
      lg: 'p-6',
      xl: 'p-8',
    },
    margin: {
      xs: 'm-1',
      sm: 'm-2',
      md: 'm-4',
      lg: 'm-6',
      xl: 'm-8',
    },
  },
});

export type SpacingVariants = VariantProps<typeof spacing>;
```

### Extending Types

Compose component types:

```typescript
// src/components/ui/card/index.tsx
import { forwardRef } from 'react';
import type { SpacingVariants } from '@core/variants';

interface CardProps 
  extends React.HTMLAttributes<HTMLDivElement>,
          SpacingVariants {
  bgColor?: 'white' | 'gray' | 'blue';
  shadow?: 'none' | 'sm' | 'md' | 'lg';
}

export const Card = forwardRef<HTMLDivElement, CardProps>(
  (props, ref) => {
    // Component implementation
  }
);
```

## IDE and Editor Support

### IntelliSense

TypeScript configuration enables:

```typescript
<Button 
  variant="primary"  // Autocomplete shows valid options
  size="lg"          // Type checking ensures valid values
  onClick={() => {}} // Type inference works correctly
/>
```

### Type Checking

Real-time error detection:

```typescript
<Button variant="invalid" /> // TypeScript Error: Type '"invalid"' is not assignable to type '"primary" | "secondary" | "danger"'
```

### Ref Type Safety

```typescript
const buttonRef = useRef<HTMLButtonElement>(null);
<Button ref={buttonRef} /> // Ref type is validated

// Later
if (buttonRef.current) {
  buttonRef.current.click(); // Method exists on HTMLButtonElement
}
```

## Build and Compilation

### Development Build

Watch mode for development:

```bash
tsc --watch
```

Recompiles on file changes, useful during development.

### Production Build

Full compilation for distribution:

```bash
tsc
```

Generates all output files, declarations, and source maps.

### Emit Only Declarations

Generate only `.d.ts` files:

```bash
tsc --declaration --emitDeclarationOnly
```

## Testing Configuration

### Jest TypeScript Support

```typescript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  moduleNameMapper: {
    '^@core/(.*)$': '<rootDir>/src/core/$1',
    '^@components/(.*)$': '<rootDir>/src/components/$1',
  },
};
```

### Test File Types

```typescript
// src/components/ui/button/__tests__/button.test.tsx
import { render, screen } from '@testing-library/react';
import { Button } from '../';

describe('Button', () => {
  it('renders correctly', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button')).toBeInTheDocument();
  });
});
```

## Best Practices

### 1. Use Strict Mode
```typescript
"strict": true
```

Enables comprehensive type checking from the start.

### 2. Use Path Aliases
```typescript
"paths": {
  "@core/*": ["./src/core/*"]
}
```

Makes imports cleaner and refactoring easier.

### 3. Define Return Types
```typescript
// ✓ Good
function getButtonClasses(variant: string): string {
  // Implementation
}

// ✗ Avoid
function getButtonClasses(variant: string) {
  // Implicit return type
}
```

### 4. Export Interfaces
```typescript
// ✓ Good
export interface ButtonProps {
  variant?: 'primary' | 'secondary';
}

// ✗ Avoid
interface ButtonProps {
  variant?: 'primary' | 'secondary';
}
```

Users can import and extend your types.

### 5. Use forwardRef with Types
```typescript
// ✓ Good
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (props, ref) => <button ref={ref} {...props} />
);

// Type-safe ref usage
const ref = useRef<HTMLButtonElement>(null);
<Button ref={ref} />
```

## Troubleshooting

### Type Not Found

Check:
- `typeRoots` and `types` configuration
- `@types` packages installed
- Path aliases configured correctly

### Cannot Find Module

Verify:
- Import paths match file structure
- Path aliases in tsconfig
- Module resolution settings

### Ref Type Errors

Use correct generic types:

```typescript
// ✓ Good
const ref = useRef<HTMLButtonElement>(null);

// ✗ Wrong
const ref = useRef<HTMLElement>(null);
```

## Next Steps

- [Build System](../build-system/README.md) - Learn TypeScript compilation
- [Package Structure](../package-structure/README.md) - Type definition distribution
- [API Reference](../../04-api-reference/README.md) - View typed components
