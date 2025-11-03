# UI Components API

## Overview

UI Components are composite components built from core primitives, located in `src/components/ui/`. They add higher-level functionality and include the prop forwarding API for variant integration.

## Components List

Main UI components:

- **Card** - Container with header, content, footer
- **Button** - Enhanced button with variants
- **Input** - Text input with variants
- **Select** - Dropdown selection
- **Modal** - Dialog/modal component
- **Alert** - Notification/alert component

## Component Structure

Each UI Component includes:

1. **Overview** - Purpose and use cases
2. **Props Interface** - TypeScript interface with variant props
3. **Props Table** - Detailed prop documentation
4. **Variants** - Available variant props
5. **Type Safety** - TypeScript and ref support
6. **Examples** - Usage patterns
7. **Compound Components** - Subcomponent patterns

## Card Component

### Overview
Flexible container component with header, content, and footer subcomponents.

### Props Interface
```typescript
interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  padding?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  bgColor?: 'white' | 'gray' | 'blue';
  shadow?: 'none' | 'sm' | 'md' | 'lg';
  rounded?: 'none' | 'sm' | 'md' | 'lg';
}
```

### Props Table

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `padding` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'md'` | Padding variant |
| `bgColor` | `'white' \| 'gray' \| 'blue'` | `'white'` | Background color |
| `shadow` | `'none' \| 'sm' \| 'md' \| 'lg'` | `'md'` | Shadow effect |
| `rounded` | `'none' \| 'sm' \| 'md' \| 'lg'` | `'md'` | Border radius |
| `...rest` | `HTMLAttributes` | - | All HTML div attributes |

### Compound Components

The Card component has subcomponents:

```typescript
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Content>Content</Card.Content>
  <Card.Footer>Footer</Card.Footer>
</Card>
```

#### Card.Header
Container for card title/header content.

```typescript
interface CardHeaderProps extends React.HTMLAttributes<HTMLDivElement> {}

<Card.Header data-class="card-header">
  Header Content
</Card.Header>
```

#### Card.Content
Main content area of the card.

```typescript
interface CardContentProps extends React.HTMLAttributes<HTMLDivElement> {}

<Card.Content data-class="card-content">
  Main Content
</Card.Content>
```

#### Card.Footer
Footer content area.

```typescript
interface CardFooterProps extends React.HTMLAttributes<HTMLDivElement> {}

<Card.Footer data-class="card-footer">
  Footer Content
</Card.Footer>
```

### Usage Example

```typescript
import { Card } from 'ui8kit-core';

<Card padding="lg" bgColor="white" shadow="md">
  <Card.Header>User Profile</Card.Header>
  <Card.Content>
    <p>Name: John Doe</p>
    <p>Email: john@example.com</p>
  </Card.Content>
  <Card.Footer>
    <button>Edit</button>
    <button>Delete</button>
  </Card.Footer>
</Card>
```

## Button Component (Enhanced)

### Overview
Enhanced button component with variant support.

### Props Interface
```typescript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  padding?: 'xs' | 'sm' | 'md' | 'lg';
  bgColor?: 'blue' | 'gray' | 'red';
  loading?: boolean;
}
```

### Props Table

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `'primary' \| 'secondary' \| 'danger'` | `'primary'` | Button style variant |
| `size` | `'sm' \| 'md' \| 'lg'` | `'md'` | Button size |
| `padding` | `'xs' \| 'sm' \| 'md' \| 'lg'` | `'md'` | Padding variant |
| `bgColor` | `'blue' \| 'gray' \| 'red'` | - | Custom background color |
| `loading` | `boolean` | `false` | Show loading state |
| `disabled` | `boolean` | `false` | Disable button |
| `...rest` | `HTMLAttributes` | - | All HTML button attributes |

### Usage Examples

```typescript
import { Button } from 'ui8kit-core';

// Primary button
<Button variant="primary">Primary</Button>

// Secondary button
<Button variant="secondary">Secondary</Button>

// Large danger button
<Button variant="danger" size="lg">Delete</Button>

// With custom color
<Button bgColor="blue" padding="lg">Custom</Button>

// Loading state
<Button loading>Processing...</Button>
```

## Input Component

### Overview
Text input with variant support.

### Props Interface
```typescript
interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  size?: 'sm' | 'md' | 'lg';
  variant?: 'default' | 'outline' | 'filled';
  error?: boolean;
  disabled?: boolean;
}
```

### Usage Example

```typescript
import { Input } from 'ui8kit-core';

<Input 
  type="text" 
  placeholder="Enter text"
  size="md"
  variant="outline"
/>
```

## Select Component

### Overview
Dropdown selection component.

### Usage Example

```typescript
import { Select } from 'ui8kit-core';

<Select>
  <option value="">Select an option</option>
  <option value="1">Option 1</option>
  <option value="2">Option 2</option>
</Select>
```

## Modal Component

### Overview
Dialog/modal for displaying content in an overlay.

### Usage Example

```typescript
import { Modal } from 'ui8kit-core';
import { useState } from 'react';

function MyComponent() {
  const [open, setOpen] = useState(false);

  return (
    <>
      <button onClick={() => setOpen(true)}>Open Modal</button>
      {open && (
        <Modal onClose={() => setOpen(false)}>
          <Modal.Header>Modal Title</Modal.Header>
          <Modal.Content>Modal content here</Modal.Content>
          <Modal.Footer>
            <button onClick={() => setOpen(false)}>Close</button>
          </Modal.Footer>
        </Modal>
      )}
    </>
  );
}
```

## Alert Component

### Overview
Notification/alert component for user messages.

### Props Interface
```typescript
interface AlertProps extends React.HTMLAttributes<HTMLDivElement> {
  type?: 'info' | 'success' | 'warning' | 'error';
  closeable?: boolean;
  onClose?: () => void;
}
```

### Usage Example

```typescript
import { Alert } from 'ui8kit-core';

<Alert type="success">
  Operation completed successfully!
</Alert>

<Alert type="error" closeable onClose={() => {}}>
  An error occurred
</Alert>
```

## Ref Forwarding

All UI Components support ref forwarding:

```typescript
import { useRef } from 'react';
import { Card, Button } from 'ui8kit-core';

const cardRef = useRef<HTMLDivElement>(null);
const buttonRef = useRef<HTMLButtonElement>(null);

<Card ref={cardRef}>
  <Button ref={buttonRef}>Click me</Button>
</Card>
```

## Data-Class Attributes

All UI Components use data-class for identification:

```typescript
<Card data-class="card">
  <Card.Header data-class="card-header" />
  <Card.Content data-class="card-content" />
  <Card.Footer data-class="card-footer" />
</Card>

<Button data-class="button-primary" />
```

## Next Steps

- [Layout Components](../layout-components/README.md) - Learn about layout systems
- [API Reference](../README.md) - Back to API overview
- [Architecture](../../03-architecture/ui-components/README.md) - Understand UI component concepts
