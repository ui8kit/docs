# TypeScript Configuration

UI8Kit is built with a TypeScript-first approach. This documentation explains how to configure TypeScript for maximum efficiency when working with the library.

## 📋 Recommended Configuration

### tsconfig.json for Applications

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@/components": ["src/components"],
      "@/lib/*": ["src/lib/*"],
      "@/hooks/*": ["src/hooks/*"],
      "@/providers/*": ["src/providers/*"],
      "@/types/*": ["src/types/*"],
      "@/utils/*": ["src/utils/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### tsconfig.json for Libraries

```json
{
  "extends": "../../tsconfig.json",
  "compilerOptions": {
    "outDir": "dist",
    "declaration": true,
    "declarationMap": true,
    "emitDeclarationOnly": false,
    "noEmit": false,
    "isolatedModules": false
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "**/*.test.ts", "**/*.test.tsx", "dist"]
}
```

## 🔧 Key Options

### Target and Lib
```json
{
  "target": "ES2020",
  "lib": ["ES2020", "DOM", "DOM.Iterable"]
}
```
- **ES2020**: Modern JS features
- **DOM**: Browser APIs
- **DOM.Iterable**: for...of for DOM collections

### Module Resolution
```json
{
  "module": "ESNext",
  "moduleResolution": "bundler"
}
```
- **ESNext**: Modern ES modules
- **bundler**: For Vite/Rollup/Webpack

### JSX
```json
{
  "jsx": "react-jsx"
}
```
Automatic React import for JSX.

### Strict Mode
```json
{
  "strict": true,
  "noUnusedLocals": true,
  "noUnusedParameters": true,
  "noFallthroughCasesInSwitch": true
}
```
Maximum strictness for code quality.

### Path Mapping
```json
{
  "baseUrl": ".",
  "paths": {
    "@/*": ["src/*"],
    "@/components": ["src/components"]
  }
}
```
Short imports for better DX.

## 🎯 UI8Kit TypeScript API

### Component Types

All components export their types:

```tsx
import type {
  ButtonProps,
  CardProps,
  BlockProps,
  BoxProps
} from '@ui8kit/core'
```

### Universal Props

```tsx
interface UniversalProps extends
  VariantSpacingProps,
  ColorProps,
  RoundedProps,
  ShadowProps,
  BorderProps {}
```

### Theming

```tsx
import type { ThemeBase } from '@/providers/theme'

interface CustomTheme extends ThemeBase {
  brandColors: {
    primary: string
    secondary: string
  }
}
```

## 🛠️ Advanced Patterns

### Conditional Types

```tsx
// Type for polymorphic components
type ComponentProps<T extends ElementType> = {
  component?: T
} & React.ComponentPropsWithoutRef<T>

// Usage
interface ButtonProps<T extends ElementType = 'button'> extends
  ComponentProps<T> {
  variant?: 'primary' | 'secondary'
  loading?: boolean
}
```

### Template Literal Types

```tsx
// For CSS classes
type SpacingScale = 'xs' | 'sm' | 'md' | 'lg' | 'xl'
type SpacingClass = `p-${SpacingScale}` | `m-${SpacingScale}`

// Result: "p-xs" | "p-sm" | "p-md" | "p-lg" | "p-xl" | "m-xs" | ...
```

### Utility Types

```tsx
// Required props
type RequiredProps<T, K extends keyof T> = T & Required<Pick<T, K>>

// Optional props
type OptionalProps<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>

// Conditional props
type ConditionalProps<T, Condition> = Condition extends true
  ? T & { requiredProp: string }
  : T & { optionalProp?: string }
```

## 🔍 Type Inference

### Auto-completion

```tsx
// Full autocompletion
<Button
  variant="primary"     // ✅ Autocompletion
  size="lg"            // ✅ Autocompletion
  rounded="md"         // ✅ Autocompletion
  onClick={handleClick} // ✅ Typed callback
/>

// Compilation errors
<Button
  variant="invalid"    // ❌ Error: not in union type
  size="huge"         // ❌ Error: not in union type
/>
```

### IntelliSense for Themes

```tsx
const theme = useTheme()

// Autocompletion for theme.rounded
<Block rounded={theme.rounded.default} />  // ✅

// Autocompletion for theme.buttonSize
<Button size={theme.buttonSize.icon} />   // ✅
```

## 🧪 Testing with TypeScript

### Test Setup

```tsx
// jest.config.js
export default {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/test-setup.ts'],
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/src/$1'
  }
}
```

### Typed Tests

```tsx
// components/__tests__/Button.test.tsx
import { render, screen } from '@/test-utils'
import { Button } from '../Button'

describe('Button', () => {
  it('accepts valid props', () => {
    render(
      <Button
        variant="primary"
        size="lg"
        onClick={jest.fn()}
      >
        Test
      </Button>
    )

    expect(screen.getByRole('button')).toBeInTheDocument()
  })

  it('rejects invalid props', () => {
    // @ts-expect-error - invalid variant
    render(<Button variant="invalid">Test</Button>)
  })
})
```

## 🚀 Type Performance

### Type-checking Optimizations

```json
{
  "skipLibCheck": true,        // Skip .d.ts file checking
  "incremental": true,         // Incremental compilation
  "tsBuildInfoFile": "dist/tsbuildinfo"
}
```

### Selective Type Checking

```tsx
// types/hot.ts - for quick checking
export type ButtonVariant = 'primary' | 'secondary'
export type ButtonSize = 'sm' | 'md' | 'lg'

// types/cold.ts - for full checking
export interface ButtonProps {
  variant: ButtonVariant
  size: ButtonSize
  children: ReactNode
  onClick?: () => void
}
```

## 🐛 Troubleshooting

### Common Errors

#### 1. Module not found
```
Cannot find module '@ui8kit/core'
```
**Solution:**
- Check package installation: `npm install @ui8kit/core`
- Check tsconfig paths

#### 2. Type errors in components
```
Type 'string' is not assignable to type 'RoundedProps'
```
**Solution:**
- Use union types: `rounded: "md" as const`
- Or configure `strict: false` for specific files

#### 3. IntelliSense not working
**Solution:**
- Restart TypeScript language server
- Check that .d.ts files are generated
- Ensure tsconfig.json is correct

### Debug Types

```tsx
// utils/debug.ts
export type DebugType<T> = T extends (...args: any[]) => any
  ? T
  : T extends abstract new (...args: any[]) => any
  ? T
  : {
      [K in keyof T]: T[K]
    }

// Usage
type ButtonDebug = DebugType<ButtonProps>
// Shows expanded type structure
```

## 📚 Additional Resources

### Official Documentation
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)

### Tools
- [TypeScript Playground](https://www.typescriptlang.org/play)
- [Type Challenges](https://github.com/type-challenges/type-challenges)
- [Total TypeScript](https://www.totaltypescript.com/)

### Configurations
- [Awesome TypeScript](https://github.com/dzharii/awesome-typescript)
- [TypeScript ESLint](https://typescript-eslint.io/)

## 🎯 Best Practices

1. **Always use strict mode**
2. **Configure path mapping** for clean imports
3. **Export types** from components
4. **Use generic constraints** for flexibility
5. **Document complex types** with JSDoc
6. **Regularly update** TypeScript to latest version
7. **Configure IDE** for better autocompletion

With proper configuration, TypeScript will become your best ally in developing with UI8Kit! 🚀
