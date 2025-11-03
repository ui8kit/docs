# Troubleshooting

## Overview

Solutions for common problems, frequently asked questions, and debugging guides for UI8Kit/Core.

## Installation Issues

### Module Not Found Error

**Problem**: `Cannot find module 'ui8kit-core'`

**Solutions**:
1. Verify installation:
```bash
npm list ui8kit-core
```

2. Reinstall if needed:
```bash
npm uninstall ui8kit-core
npm install ui8kit-core
```

3. Check package.json:
```json
{
  "dependencies": {
    "ui8kit-core": "^3.0.0"
  }
}
```

4. Clear npm cache:
```bash
npm cache clean --force
npm install
```

### Tailwind CSS Not Applied

**Problem**: Styles don't appear on components

**Solutions**:
1. Verify Tailwind CSS is installed:
```bash
npm list tailwindcss
```

2. Check `tailwind.config.js` includes UI8Kit:
```javascript
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./node_modules/ui8kit-core/dist/**/*.{js,jsx,ts,tsx}",
  ],
  // ... rest of config
};
```

3. Import Tailwind CSS in your main CSS file:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

4. Verify CSS is imported in your app entry point:
```typescript
import './styles.css'; // or tailwind.css
```

## Component Issues

### Component Not Rendering

**Problem**: Component appears in code but doesn't show in browser

**Solutions**:
1. Check import statement:
```typescript
// Correct
import { Button } from 'ui8kit-core';

// Wrong
import Button from 'ui8kit-core'; // Named export, not default
```

2. Verify component is exported:
```typescript
// Check if using correct export
import { Card } from 'ui8kit-core';
```

3. Check for console errors and fix them

### Ref Not Working

**Problem**: `ref` prop not forwarding properly

**Solutions**:
1. Use `useRef` correctly:
```typescript
const buttonRef = useRef<HTMLButtonElement>(null);
<Button ref={buttonRef} />
```

2. Access ref properly:
```typescript
if (buttonRef.current) {
  buttonRef.current.click(); // Button has click method
}
```

3. Check ref type matches component:
```typescript
// Good - button ref type
const ref = useRef<HTMLButtonElement>(null);

// Bad - wrong type
const ref = useRef<HTMLElement>(null); // Too generic
```

### TypeScript Errors

**Problem**: Type errors with component props

**Solutions**:
1. Import types:
```typescript
import { Button, type ButtonProps } from 'ui8kit-core';
```

2. Extend component props:
```typescript
interface MyButtonProps extends ButtonProps {
  customProp?: string;
}
```

3. Check variant values are correct:
```typescript
// Good - valid variant
<Button variant="primary" />

// Bad - invalid variant
<Button variant="invalid" />
```

## Layout Issues

### Layout Not Responsive

**Problem**: Layout doesn't change on different screen sizes

**Solutions**:
1. Use responsive props:
```typescript
// Good - responsive
<Grid cols={{ base: 1, md: 2, lg: 3 }} />

// Bad - fixed
<Grid cols={3} />
```

2. Add viewport meta tag:
```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

3. Test with browser dev tools mobile view

### Grid/Flex Not Aligning

**Problem**: Items not aligned as expected

**Solutions**:
1. Check alignment props:
```typescript
<Flex
  justify="between"    // Space-between
  align="center"       // Vertical center
  direction="row"      // Horizontal layout
/>
```

2. Verify gap property:
```typescript
<Grid gap="md" /> // Use variant gaps, not custom values
```

3. Inspect computed CSS in dev tools

## State Management Issues

### State Not Updating

**Problem**: Component doesn't update when state changes

**Solutions**:
1. Check useState usage:
```typescript
// Good
const [value, setValue] = useState('');
setValue(newValue); // Direct call updates state

// Bad - doesn't update state
value = newValue; // Direct assignment doesn't work in React
```

2. For objects, create new reference:
```typescript
// Good - new object reference
setValues({ ...values, name: 'John' });

// Bad - mutating original
values.name = 'John';
setValues(values);
```

3. Check dependency arrays in useEffect:
```typescript
useEffect(() => {
  // This runs when dependencies change
}, [dependency1, dependency2]);
```

## Form Issues

### Form Submission Not Working

**Problem**: Form doesn't submit when button clicked

**Solutions**:
1. Use correct button type:
```typescript
<Button type="submit">Submit</Button>
```

2. Wrap button in form:
```typescript
<form onSubmit={handleSubmit}>
  <Input {...} />
  <Button type="submit">Submit</Button>
</form>
```

3. Prevent default properly:
```typescript
const handleSubmit = (e: React.FormEvent) => {
  e.preventDefault(); // Stop default form submission
  // Your logic here
};
```

### Input Not Capturing Value

**Problem**: Input field doesn't update or lose focus

**Solutions**:
1. Use controlled component pattern:
```typescript
const [value, setValue] = useState('');

<Input
  value={value}
  onChange={(e) => setValue(e.target.value)}
/>
```

2. Check onChange handler:
```typescript
// Good
onChange={(e) => setValue(e.target.value)}

// Bad - missing e.target.value
onChange={() => setValue('')}
```

3. Verify input type is correct:
```typescript
<Input type="email" /> // For email inputs
<Input type="password" /> // For passwords
```

## Performance Issues

### Slow Component Rendering

**Problem**: Application feels sluggish

**Solutions**:
1. Memoize components:
```typescript
const Item = memo(({ item }) => (
  <Card>{item.name}</Card>
));
```

2. Use proper keys in lists:
```typescript
// Good - stable unique keys
{items.map(item => (
  <Card key={item.id}>{item}</Card>
))}

// Bad - index keys cause re-renders
{items.map((item, index) => (
  <Card key={index}>{item}</Card>
))}
```

3. Lazy load heavy components:
```typescript
const HeavyComponent = lazy(() => import('./Heavy'));

<Suspense fallback={<Card>Loading...</Card>}>
  <HeavyComponent />
</Suspense>
```

## Dark Mode Issues

### Theme Not Persisting

**Problem**: Theme resets on page refresh

**Solutions**:
1. Wrap with ThemeProvider:
```typescript
<ThemeProvider>
  <App />
</ThemeProvider>
```

2. Check localStorage is enabled
3. Verify provider wraps entire app
4. Check browser console for errors

### Flash of Wrong Theme

**Problem**: Page loads with wrong theme briefly

**Solutions**:
1. Add theme loading script in HTML head:
```html
<script>
  const theme = localStorage.getItem('theme') || 'light';
  document.documentElement.classList.add(theme);
</script>
```

2. Set initial theme in provider:
```typescript
<ThemeProvider defaultTheme="light">
  <App />
</ThemeProvider>
```

## Build Issues

### TypeScript Compilation Errors

**Problem**: Build fails with TypeScript errors

**Solutions**:
1. Check TypeScript version:
```bash
npm list typescript
```

2. Update tsconfig.json:
```json
{
  "compilerOptions": {
    "strict": true,
    "esModuleInterop": true
  }
}
```

3. Fix type errors in code

### Bundle Size Too Large

**Problem**: Built bundle is too large

**Solutions**:
1. Enable tree-shaking:
```json
{
  "sideEffects": false,
  "type": "module"
}
```

2. Code splitting:
```typescript
import { lazy } from 'react';
const Component = lazy(() => import('./Component'));
```

3. Check imports are correct:
```typescript
// Good - tree-shakeable
import { Button } from 'ui8kit-core';

// Less efficient - might include everything
import * as UI from 'ui8kit-core';
```

## Browser Compatibility

### Styles Not Working in Older Browsers

**Problem**: Styles work in modern browsers but not in older ones

**Solutions**:
1. Check target in tsconfig.json:
```json
{
  "compilerOptions": {
    "target": "ES2020"
  }
}
```

2. Add polyfills if needed
3. Test with browser compatibility matrix

## Getting Help

### When You're Stuck

1. **Check documentation** - Review API Reference and examples
2. **Search issues** - Check GitHub issues for similar problems
3. **Check console** - Read browser console for error messages
4. **Verify setup** - Double-check installation and configuration
5. **Simplify** - Create minimal reproduction case
6. **Ask for help** - Create issue with reproduction steps

### Creating a Reproduction Case

```typescript
// Minimal example that reproduces the issue
import { Button } from 'ui8kit-core';

export function TestCase() {
  return <Button>Click me</Button>;
}
```

Include:
- Versions of dependencies
- Steps to reproduce
- Expected behavior
- Actual behavior
- Minimal code example

## FAQ

### Q: How do I customize component colors?

**A**: Use variant props:
```typescript
<Button bgColor="blue" padding="lg">Custom Button</Button>
```

### Q: Can I use custom className?

**A**: Yes, but variants are preferred:
```typescript
<Button className="custom-class" padding="lg">
  Button with custom class
</Button>
```

### Q: How do I extend components?

**A**: Create wrapper components:
```typescript
function MyButton(props) {
  return <Button variant="primary" {...props} />;
}
```

### Q: Does it work with Next.js?

**A**: Yes, it works with both App and Pages routers.

### Q: Do I need all components?

**A**: No, use only what you need. Tree-shaking removes unused code.

## Next Steps

- [API Reference](../04-api-reference/README.md) - Component documentation
- [Development Guide](../05-development-guide/README.md) - Usage guides
- [Architecture](../03-architecture/README.md) - System overview
- [Getting Started](../02-getting-started/README.md) - Setup guide
