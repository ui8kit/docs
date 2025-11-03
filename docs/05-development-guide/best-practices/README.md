# Best Practices

## Overview

General guidelines and recommendations for using UI8Kit/Core components effectively.

## Component Usage

### 1. Prefer Variants Over className

```typescript
// Good - use variants from the system
<Button 
  padding="lg" 
  bgColor="blue" 
  rounded="md"
/>

// Less optimal - hardcoded classes
<Button className="p-6 bg-blue-600 rounded-md" />
```

Variants provide:
- Type safety
- Consistency across components
- Easy theme changes
- Better maintainability

### 2. Use Semantic HTML

```typescript
// Good - semantic elements
<header>
  <nav>Navigation</nav>
</header>
<main>
  <article>Content</article>
</main>
<footer>Footer</footer>

// Less semantic
<div>
  <div>Navigation</div>
</div>
<div>
  <div>Content</div>
</div>
<div>Footer</div>
```

Benefits:
- Better accessibility
- SEO friendly
- More maintainable code
- Clearer intent

### 3. Leverage Compound Components

```typescript
// Good - clear structure
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Content>Content</Card.Content>
  <Card.Footer>Actions</Card.Footer>
</Card>

// Less clear - generic wrapper
<Card header="Title" content="Content" footer="Actions" />
```

Advantages:
- Explicit structure
- Flexible composition
- Type-safe subcomponents
- Clear hierarchy

### 4. Use TypeScript Interfaces

```typescript
// Good - typed props
interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
}

const MyButton = (props: ButtonProps) => {
  // Implementation
};

// Less helpful - any type
const MyButton = (props: any) => {
  // Implementation
};
```

Benefits:
- IDE autocomplete
- Compile-time error checking
- Self-documenting code
- Easier refactoring

## Layout Best Practices

### 1. Use Layout Components

```typescript
// Good - use provided layout
<DashLayout sidebar={<Nav />} header={<Header />}>
  <DashLayout.Content>Content</DashLayout.Content>
</DashLayout>

// More work - manual layout
<div style={{ display: 'flex' }}>
  <aside>Nav</aside>
  <main>Content</main>
</div>
```

### 2. Responsive Design

```typescript
// Good - responsive
<Grid
  cols={{ base: 1, md: 2, lg: 3 }}
  gap="md"
>
  {items.map(item => <Card key={item.id}>{item}</Card>)}
</Grid>

// Fixed - not responsive
<Grid cols={3} gap="md">
  {items.map(item => <Card key={item.id}>{item}</Card>)}
</Grid>
```

### 3. Proper Spacing

```typescript
// Good - consistent spacing
<Card padding="lg" gap="md">
  <Box marginBottom="md">Section 1</Box>
  <Box marginBottom="md">Section 2</Box>
</Card>

// Inconsistent - manual spacing
<Card>
  <Box style={{ marginBottom: '20px' }}>Section 1</Box>
  <Box style={{ marginBottom: '10px' }}>Section 2</Box>
</Card>
```

## Performance

### 1. Minimize Re-renders

```typescript
// Good - memoized component
import { memo } from 'react';

const ItemCard = memo(({ item }: { item: Item }) => (
  <Card>{item.name}</Card>
));

// Less optimal - re-renders on parent change
function ItemCard({ item }: { item: Item }) {
  return <Card>{item.name}</Card>;
}
```

### 2. Use Keys in Lists

```typescript
// Good - stable keys
{items.map(item => (
  <Card key={item.id}>{item.name}</Card>
))}

// Bad - index keys
{items.map((item, index) => (
  <Card key={index}>{item.name}</Card>
))}
```

### 3. Lazy Load Components

```typescript
// Good - code splitting
import { lazy, Suspense } from 'react';

const HeavyComponent = lazy(() => import('./HeavyComponent'));

export function App() {
  return (
    <Suspense fallback={<Card>Loading...</Card>}>
      <HeavyComponent />
    </Suspense>
  );
}
```

## Accessibility

### 1. Use ARIA Labels

```typescript
// Good - accessible button
<Button 
  aria-label="Close dialog"
  onClick={handleClose}
>
  ✕
</Button>

// Less accessible
<Button onClick={handleClose}>✕</Button>
```

### 2. Keyboard Navigation

```typescript
// Good - keyboard support
<Button onClick={handleAction} onKeyDown={handleKeyDown}>
  Action
</Button>

// Verify tab order and focus management
<Card>
  <Button>First</Button>
  <Button>Second</Button>
</Card>
```

### 3. Color Contrast

```typescript
// Good - sufficient contrast
<Button bgColor="blue">High contrast text</Button>

// Check contrast ratios meet WCAG standards
```

## Semantic HTML

### 1. Use Correct Heading Hierarchy

```typescript
// Good - proper hierarchy
<>
  <h1>Page Title</h1>
  <h2>Section Title</h2>
  <h3>Subsection Title</h3>
</>

// Bad - skipped levels
<>
  <h1>Page Title</h1>
  <h3>Subsection Title</h3>
</>
```

### 2. List Elements for Lists

```typescript
// Good - semantic list
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

// Less semantic
<div>
  <div>Item 1</div>
  <div>Item 2</div>
</div>
```

### 3. Form Elements

```typescript
// Good - proper form structure
<form onSubmit={handleSubmit}>
  <label htmlFor="email">Email</label>
  <Input id="email" type="email" />
  <Button type="submit">Submit</Button>
</form>

// Less semantic
<div>
  <span>Email</span>
  <input type="email" />
  <button>Submit</button>
</div>
```

## State Management

### 1. Use Proper State Level

```typescript
// Good - state at right level
function Parent() {
  const [selected, setSelected] = useState<string | null>(null);

  return (
    <Grid cols={3}>
      {items.map(item => (
        <ItemCard
          key={item.id}
          selected={selected === item.id}
          onClick={() => setSelected(item.id)}
        />
      ))}
    </Grid>
  );
}
```

### 2. Avoid Prop Drilling

```typescript
// Good - use context for deeply nested props
const ThemeContext = createContext<Theme>('light');

export function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Layout />
    </ThemeContext.Provider>
  );
}

function DeeplyNestedComponent() {
  const theme = useContext(ThemeContext);
  return <Card>Using {theme} theme</Card>;
}
```

## Error Handling

### 1. Display Error States

```typescript
// Good - show errors clearly
function DataDisplay() {
  const { data, error, loading } = useData();

  if (loading) return <Alert type="info">Loading...</Alert>;
  if (error) return <Alert type="error">{error.message}</Alert>;

  return <Grid>{data.map(item => <Card key={item.id}>{item}</Card>)}</Grid>;
}
```

### 2. Validate Input

```typescript
// Good - validate before submit
function Form() {
  const [values, setValues] = useState({ email: '' });
  const [errors, setErrors] = useState<Record<string, string>>({});

  const validate = () => {
    const newErrors: Record<string, string> = {};
    if (!values.email) newErrors.email = 'Email required';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (validate()) {
      // Submit
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input value={values.email} onChange={(e) => setValues({ email: e.target.value })} />
      {errors.email && <p className="text-red-500">{errors.email}</p>}
      <Button type="submit">Submit</Button>
    </form>
  );
}
```

## Next Steps

- [Dark Mode](../dark-mode/README.md) - Theme implementation
- [Development Guide](../README.md) - Back to overview
- [API Reference](../../04-api-reference/README.md) - Component details
