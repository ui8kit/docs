# Development Guide

## Overview

The Development Guide provides practical workflows, patterns, and best practices for using UI8Kit/Core in your applications.

## Sections

### 1. Basic Workflow
Common development patterns and usage examples for typical scenarios.

[View Basic Workflow →](./basic-workflow/README.md)

Topics:
- Component setup
- Common patterns
- Typical use cases

### 2. Advanced Workflow
Handling edge cases where standard components are insufficient.

[View Advanced Workflow →](./advanced-workflow/README.md)

Topics:
- Custom forms
- Component composition
- Advanced patterns

### 3. Best Practices
General guidelines and recommendations for using components and building layouts.

[View Best Practices →](./best-practices/README.md)

Topics:
- Component usage
- Layout patterns
- Performance optimization
- Accessibility
- Semantic HTML

### 4. Dark Mode
Implementation, toggle functionality, and persistence.

[View Dark Mode →](./dark-mode/README.md)

Topics:
- Theme configuration
- Dark mode setup
- Toggle implementation
- Persistence

## Quick Start

### Step 1: Install
```bash
npm install ui8kit-core
```

### Step 2: Basic Import
```typescript
import { Button, Card } from 'ui8kit-core';

export function App() {
  return (
    <Card>
      <Card.Header>Welcome</Card.Header>
      <Card.Content>
        <Button>Click me</Button>
      </Card.Content>
    </Card>
  );
}
```

### Step 3: Use Variants
```typescript
<Button 
  padding="lg" 
  bgColor="blue"
  rounded="md"
>
  Customized Button
</Button>
```

## Development Philosophy

UI8Kit/Core follows these principles:

### 1. Minimalism
Use the simplest component that solves your problem. Most interfaces can be built with core and UI components without custom styling.

### 2. Composition
Combine components rather than creating complex monolithic components. This increases flexibility and reusability.

### 3. Type Safety
Leverage TypeScript for better developer experience and fewer runtime errors.

### 4. Consistency
Follow established patterns for prop naming, data-class attributes, and component structure.

### 5. Accessibility
All components prioritize semantic HTML and ARIA attributes for accessibility.

## Common Workflows

### Building a Form

```typescript
import { Card, Button, Input } from 'ui8kit-core';
import { useState } from 'react';

function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <Card maxWidth="md">
      <Card.Header>Login</Card.Header>
      <Card.Content>
        <Input 
          type="email" 
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
        />
        <Input 
          type="password" 
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
        />
      </Card.Content>
      <Card.Footer>
        <Button variant="primary">Sign In</Button>
      </Card.Footer>
    </Card>
  );
}
```

### Building a Dashboard

```typescript
import { DashLayout, Grid, Card } from 'ui8kit-core';

function Dashboard() {
  return (
    <DashLayout sidebar={<NavMenu />} header={<TopBar />}>
      <DashLayout.Content>
        <Grid cols={3} gap="md">
          <StatCard title="Users" value="1,234" />
          <StatCard title="Revenue" value="$45,678" />
          <StatCard title="Orders" value="789" />
        </Grid>
      </DashLayout.Content>
    </DashLayout>
  );
}
```

### Building a Layout

```typescript
import { LayoutBlock, Flex, SplitBlock } from 'ui8kit-core';

function BlogPage() {
  return (
    <LayoutBlock maxWidth="6xl" padding="lg">
      <header>
        <h1>My Blog</h1>
      </header>
      
      <SplitBlock
        left={<ArticleContent />}
        right={<Sidebar />}
        ratio="2:1"
      />
      
      <footer>
        <Flex justify="between" gap="md">
          <p>&copy; 2024</p>
          <nav>{/* Footer links */}</nav>
        </Flex>
      </footer>
    </LayoutBlock>
  );
}
```

## Component Patterns

### Pattern: Controlled Component
```typescript
const [value, setValue] = useState('');

<Input 
  value={value}
  onChange={(e) => setValue(e.target.value)}
/>
```

### Pattern: Ref Access
```typescript
const ref = useRef<HTMLButtonElement>(null);

<Button ref={ref}>Click me</Button>

// Later: ref.current?.click()
```

### Pattern: Compound Component
```typescript
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Content>Content</Card.Content>
  <Card.Footer>Actions</Card.Footer>
</Card>
```

### Pattern: With Variants
```typescript
<Button
  variant="primary"
  size="lg"
  padding="md"
  bgColor="blue"
>
  Click me
</Button>
```

## TypeScript Support

All components are fully typed:

```typescript
import { Button, Card } from 'ui8kit-core';
import type { ButtonProps, CardProps } from 'ui8kit-core';

interface MyButtonProps extends ButtonProps {
  customProp?: string;
}

function MyButton(props: MyButtonProps) {
  return <Button {...props} />;
}
```

## Next Steps

- [Basic Workflow](./basic-workflow/README.md) - Learn common patterns
- [Advanced Workflow](./advanced-workflow/README.md) - Handle edge cases
- [Best Practices](./best-practices/README.md) - Follow recommendations
- [Dark Mode](./dark-mode/README.md) - Implement themes
- [API Reference](../04-api-reference/README.md) - View component API
