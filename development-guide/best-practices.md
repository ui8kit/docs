# Best Practices

Recommendations and patterns for efficient development with UI8Kit. Follow these practices to create maintainable and scalable code.

## 🎯 General Principles

### 1. Use Semantic Props

```tsx
// ✅ Good - semantic props
<Block bg="primary" c="primary-foreground" p="md">
  Primary section
</Block>

// ❌ Bad - hardcoded classes
<div className="bg-blue-500 text-white p-4">
  Primary section
</div>
```

### 2. Follow Design System

```tsx
// ✅ Good - use design tokens
<Button variant="primary" size="lg" rounded="md">
  Primary Action
</Button>

// ❌ Bad - custom styles
<Button className="bg-blue-500 text-white px-6 py-3 rounded-lg">
  Primary Action
</Button>
```

### 3. Be Consistent in API

```tsx
// ✅ Good - consistent usage
<Stack gap="lg">
  <Title size="xl">Header</Title>
  <Text>Content</Text>
  <Group gap="md">
    <Button>Cancel</Button>
    <Button variant="primary">Save</Button>
  </Group>
</Stack>

// ❌ Bad - mixing approaches
<div className="space-y-6">
  <h1 className="text-3xl">Header</h1>
  <p>Content</p>
  <div className="flex gap-4">
    <Button>Cancel</Button>
    <button className="bg-blue-500">Save</button>
  </div>
</div>
```

## 🧩 Component Patterns

### Polymorphic Components

Use the `component` prop for semantic markup:

```tsx
// ✅ Good - semantic markup
<Block component="section" py="xl">
  <Block component="h1">Title</Block>
  <Text component="p">Content</Text>
</Block>

// ✅ Good - accessibility
<Button component="a" href="/dashboard">
  Go to Dashboard
</Button>

// ❌ Bad - incorrect semantics
<div>
  <div>Page Title</div>
  <span>Content</span>
</div>
```

### Compound Components

Use compound components for complex UI:

```tsx
// ✅ Good - compound pattern
<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Card description</CardDescription>
  </CardHeader>
  <CardContent>
    Main content
  </CardContent>
  <CardFooter>
    <Button>Action</Button>
  </CardFooter>
</Card>

// ❌ Bad - flat structure
<div className="card">
  <div className="card-header">
    <h3>Card Title</h3>
    <p>Card description</p>
  </div>
  <div className="card-content">
    Main content
  </div>
  <div className="card-footer">
    <button>Action</button>
  </div>
</div>
```

## 🎨 Styling

### Spacing System

```tsx
// ✅ Good - use spacing scale
<Stack gap="lg">
  <Block p="md">Content</Block>
  <Block py="xl">Large padding</Block>
</Stack>

// ❌ Bad - magic numbers
<Stack style={{ gap: '24px' }}>
  <Block style={{ padding: '12px' }}>Content</Block>
  <Block style={{ paddingTop: '48px', paddingBottom: '48px' }}>Large padding</Block>
</Stack>
```

### Color System

```tsx
// ✅ Good - semantic colors
<Button variant="primary">Primary</Button>
<Button variant="destructive">Delete</Button>
<Text c="muted">Muted text</Text>

// ❌ Bad - hardcoded colors
<Button className="bg-blue-500">Primary</Button>
<Button className="bg-red-500">Delete</Button>
<Text className="text-gray-500">Muted text</Text>
```

### Responsive Design

```tsx
// ✅ Good - mobile-first
<Grid cols="1-2-3" gap="md">
  <Card>Responsive content</Card>
</Grid>

// ✅ Good - responsive spacing
<Block p={{ base: "md", md: "lg", xl: "xl" }}>
  Responsive padding
</Block>

// ❌ Bad - multiple conditions
{isMobile ? (
  <div className="p-4">Mobile</div>
) : (
  <div className="p-8">Desktop</div>
)}
```

## 🔧 Performance

### Avoid Unnecessary Re-renders

```tsx
// ✅ Good - memoized callbacks
const handleClick = useCallback(() => {
  // handle click
}, [])

// ✅ Good - stable references
const theme = useMemo(() => ({ /* theme */ }), [])

// ❌ Bad - new objects on every render
<Button onClick={() => setCount(c => c + 1)}>
  Click
</Button>
```

### Tree Shaking

```tsx
// ✅ Good - import only what you need
import { Button, Card } from '@ui8kit/core'

// ❌ Bad - import everything
import * as UI from '@ui8kit/core'
```

### Bundle Analysis

Regularly analyze bundle size:

```bash
# Use bundle analyzer
npm run build
npx vite-bundle-analyzer dist
```

## ♿ Accessibility

### Semantic Markup

```tsx
// ✅ Good - correct semantics
<Block component="main">
  <Block component="nav" aria-label="Main navigation">
    <Group component="ul" role="menubar">
      <Block component="li" role="none">
        <Button component="a" href="/">Home</Button>
      </Block>
    </Group>
  </Block>
  <Block component="section" aria-labelledby="main-heading">
    <Title id="main-heading">Main Content</Title>
  </Block>
</Block>

// ❌ Bad - incorrect semantics
<div>
  <div>
    <div>
      <button>Home</button>
    </div>
  </div>
  <div>
    <h1>Main Content</h1>
  </div>
</div>
```

### Focus Management

```tsx
// ✅ Good - correct focus flow
<Modal>
  <ModalContent>
    <ModalHeader>
      <ModalTitle>Modal Title</ModalTitle>
    </ModalHeader>
    <ModalBody>
      <form onSubmit={handleSubmit}>
        <input autoFocus />
        {/* form fields */}
        <Button type="submit">Submit</Button>
      </form>
    </ModalBody>
  </ModalContent>
</Modal>
```

### ARIA Attributes

```tsx
// ✅ Good - ARIA for complex components
<Button
  aria-expanded={isOpen}
  aria-controls="menu"
  aria-haspopup="menu"
>
  Menu
</Button>

// ✅ Good - screen reader content
<Text className="sr-only">
  Screen reader description
</Text>
```

## 🧪 Testing

### Component Unit Tests

```tsx
// ✅ Good - test behavior
describe('Button', () => {
  it('calls onClick when clicked', () => {
    const handleClick = jest.fn()
    render(<Button onClick={handleClick}>Click me</Button>)

    fireEvent.click(screen.getByRole('button'))
    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('shows loading spinner when loading', () => {
    render(<Button loading>Loading</Button>)

    expect(screen.getByRole('button')).toBeDisabled()
    expect(screen.getByClass('animate-spin')).toBeInTheDocument()
  })
})
```

### Visual Regression Tests

```tsx
// ✅ Good - visual snapshots
describe('Button variants', () => {
  it('renders primary variant correctly', () => {
    const { container } = render(<Button variant="primary">Primary</Button>)
    expect(container.firstChild).toMatchSnapshot()
  })
})
```

### E2E Tests

```tsx
// ✅ Good - end-to-end flows
it('completes user registration', () => {
  cy.visit('/register')
  cy.findByLabelText('Email').type('user@example.com')
  cy.findByLabelText('Password').type('password123')
  cy.findByRole('button', { name: 'Register' }).click()
  cy.url().should('include', '/dashboard')
})
```

## 📁 Project Structure

### File Organization

```
src/
├── components/          # Reusable components
│   ├── ui/             # Basic UI components
│   ├── forms/          # Forms
│   └── layout/         # Layout components
├── hooks/              # Custom hooks
├── lib/                # Utilities
├── providers/          # Context providers
├── styles/             # Global styles
└── types/              # TypeScript types
```

### Component Naming

```tsx
// ✅ Good - PascalCase, descriptive names
export function UserProfileCard() { /* ... */ }
export function DataTable() { /* ... */ }
export function ThemeToggle() { /* ... */ }

// ❌ Bad - unclear names
export function Card() { /* ... */ }      // Too generic
export function Btn() { /* ... */ }       // Abbreviations
export function component1() { /* ... */ } // Low-level
```

### Barrel Exports

```tsx
// ✅ Good - barrel exports for convenient imports
// components/index.ts
export { Button } from './ui/Button'
export { Card } from './ui/Card'
export { Input } from './forms/Input'

// Usage
import { Button, Card, Input } from '@/components'

// ❌ Bad - deep imports
import Button from '@/components/ui/Button/Button'
import Card from '@/components/ui/Card/Card'
```

## 🔄 Working with Themes

### Component Theming

```tsx
// ✅ Good - use theme context
function ThemedButton({ variant, ...props }) {
  const { rounded } = useTheme()

  return (
    <Button
      variant={variant}
      rounded={rounded.button}
      {...props}
    />
  )
}

// ❌ Bad - hardcoded values
function ThemedButton({ variant, ...props }) {
  return (
    <Button
      variant={variant}
      rounded="md"
      {...props}
    />
  )
}
```

### Custom Themes

```tsx
// ✅ Good - extend base theme
const customTheme = {
  ...baseTheme,
  colors: {
    ...baseTheme.colors,
    brand: '#ff6b6b'
  }
}

// ❌ Bad - overwrite everything
const badTheme = {
  primary: '#ff6b6b',
  // missing other required properties
}
```

## 🚀 Optimization

### Code Splitting

```tsx
// ✅ Good - lazy loading modals
const Modal = lazy(() => import('./Modal'))

function App() {
  const [showModal, setShowModal] = useState(false)

  return (
    <div>
      <Button onClick={() => setShowModal(true)}>Open Modal</Button>
      {showModal && (
        <Suspense fallback={<div>Loading...</div>}>
          <Modal onClose={() => setShowModal(false)} />
        </Suspense>
      )}
    </div>
  )
}
```

### Memoization

```tsx
// ✅ Good - memoize heavy computations
const filteredItems = useMemo(() =>
  items.filter(item => item.status === 'active'),
  [items]
)

// ✅ Good - memoize components
const UserCard = memo(function UserCard({ user }) {
  return (
    <Card>
      <Text>{user.name}</Text>
      <Text c="muted">{user.email}</Text>
    </Card>
  )
})
```

## 📝 Documentation

### Component Documentation

```tsx
// ✅ Good - document API
interface ButtonProps extends
  React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** Button style variant */
  variant?: 'default' | 'primary' | 'destructive' | 'outline' | 'secondary' | 'ghost' | 'link'
  /** Button size */
  size?: 'xs' | 'sm' | 'default' | 'md' | 'lg' | 'xl' | 'icon'
  /** Loading state */
  loading?: boolean
  /** Left section content */
  leftSection?: ReactNode
  /** Right section content */
  rightSection?: ReactNode
}

export function Button({ variant = 'default', size = 'default', ...props }: ButtonProps) {
  // implementation
}
```

### README файлы

```markdown
# Component Name

Brief description of what this component does.

## Usage

```tsx
import { ComponentName } from './ComponentName'

// Basic usage
<ComponentName prop="value" />

// Advanced usage
<ComponentName
  prop="value"
  onChange={handleChange}
>
  Children
</ComponentName>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| prop | string | - | Description of prop |
```

## 🔍 Debugging

### Development Tools

```tsx
// ✅ Good - development helpers
if (process.env.NODE_ENV === 'development') {
  // Debug logging
  console.log('Component state:', state)

  // Visual indicators
  return (
    <div data-debug="component-name">
      {/* component content */}
    </div>
  )
}
```

### Error Boundaries

```tsx
// ✅ Good - error boundaries for components
class ErrorBoundary extends Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true }
  }

  componentDidCatch(error, errorInfo) {
    console.error('Component error:', error, errorInfo)
  }

  render() {
    if (this.state.hasError) {
      return <Text c="destructive">Something went wrong</Text>
    }

    return this.props.children
  }
}
```

## 🎯 Final Recommendations

1. **Follow Design System** - use semantic props instead of custom classes
2. **Write Accessible Code** - correct semantics and ARIA attributes
3. **Test Thoroughly** - unit, integration and e2e tests
4. **Optimize Performance** - memoization and code splitting
5. **Document API** - JSDoc and README for components
6. **Use TypeScript** - strict typing for reliability
7. **Be Consistent** - unified code style and patterns
8. **Plan for Scalability** - modular architecture
