# Basic Workflow

## Overview

Basic Workflow covers common development patterns and typical usage scenarios for UI8Kit/Core components.

## Pattern 1: Component Setup

### Step 1: Import
```typescript
import { Button, Card, Input } from 'ui8kit-core';
```

### Step 2: Use in JSX
```typescript
function MyComponent() {
  return (
    <Card>
      <Card.Header>Title</Card.Header>
      <Card.Content>
        <Button>Click me</Button>
      </Card.Content>
    </Card>
  );
}
```

## Pattern 2: Simple List Display

Display a list of items using Grid:

```typescript
import { Grid, Card } from 'ui8kit-core';

interface Item {
  id: string;
  title: string;
  description: string;
}

function ItemList({ items }: { items: Item[] }) {
  return (
    <Grid cols={3} gap="md">
      {items.map(item => (
        <Card key={item.id}>
          <Card.Header>{item.title}</Card.Header>
          <Card.Content>{item.description}</Card.Content>
        </Card>
      ))}
    </Grid>
  );
}
```

## Pattern 3: Form Building

Create a user-friendly form:

```typescript
import { Card, Button, Input } from 'ui8kit-core';
import { useState } from 'react';

function ContactForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log({ name, email, message });
    // Submit form logic
  };

  return (
    <Card padding="lg" maxWidth="md">
      <Card.Header>Contact Us</Card.Header>
      <Card.Content>
        <form onSubmit={handleSubmit}>
          <Input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Your Name"
          />
          <Input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Your Email"
          />
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Your Message"
          />
          <Button type="submit" variant="primary">
            Send
          </Button>
        </form>
      </Card.Content>
    </Card>
  );
}
```

## Pattern 4: Modal Usage

Show modal dialogs:

```typescript
import { Modal, Button, Card } from 'ui8kit-core';
import { useState } from 'react';

function DeleteConfirmation() {
  const [open, setOpen] = useState(false);

  const handleDelete = () => {
    // Delete logic
    setOpen(false);
  };

  return (
    <>
      <Button variant="danger" onClick={() => setOpen(true)}>
        Delete Item
      </Button>

      {open && (
        <Modal onClose={() => setOpen(false)}>
          <Modal.Header>Confirm Deletion</Modal.Header>
          <Modal.Content>
            Are you sure you want to delete this item?
          </Modal.Content>
          <Modal.Footer>
            <Button onClick={() => setOpen(false)}>Cancel</Button>
            <Button variant="danger" onClick={handleDelete}>
              Delete
            </Button>
          </Modal.Footer>
        </Modal>
      )}
    </>
  );
}
```

## Pattern 5: Conditional Rendering

Show/hide content based on state:

```typescript
import { Card, Alert, Button } from 'ui8kit-core';
import { useState } from 'react';

function ConditionalContent() {
  const [showAlert, setShowAlert] = useState(false);

  return (
    <Card>
      <Card.Header>Conditional Rendering</Card.Header>
      <Card.Content>
        {showAlert && (
          <Alert type="info">
            This alert is now visible!
          </Alert>
        )}
        <Button onClick={() => setShowAlert(!showAlert)}>
          Toggle Alert
        </Button>
      </Card.Content>
    </Card>
  );
}
```

## Pattern 6: Layout Composition

Combine layout components:

```typescript
import { LayoutBlock, SplitBlock, Card } from 'ui8kit-core';

function PageLayout() {
  return (
    <LayoutBlock maxWidth="6xl" padding="lg" centered>
      <header>
        <h1>My App</h1>
      </header>

      <SplitBlock
        left={
          <Card>
            <Card.Header>Sidebar</Card.Header>
            <Card.Content>Side content</Card.Content>
          </Card>
        }
        right={
          <Card>
            <Card.Header>Main Content</Card.Header>
            <Card.Content>Main content goes here</Card.Content>
          </Card>
        }
        ratio="1:2"
      />

      <footer>
        <p>&copy; 2024 My App</p>
      </footer>
    </LayoutBlock>
  );
}
```

## Pattern 7: Navigation Menu

Build navigation:

```typescript
import { Flex, Button } from 'ui8kit-core';

function NavBar() {
  const [active, setActive] = useState('home');

  return (
    <Flex
      direction="row"
      justify="between"
      align="center"
      gap="md"
      padding="md"
    >
      <h1>Logo</h1>
      <Flex gap="md">
        <Button
          variant={active === 'home' ? 'primary' : 'secondary'}
          onClick={() => setActive('home')}
        >
          Home
        </Button>
        <Button
          variant={active === 'about' ? 'primary' : 'secondary'}
          onClick={() => setActive('about')}
        >
          About
        </Button>
        <Button
          variant={active === 'contact' ? 'primary' : 'secondary'}
          onClick={() => setActive('contact')}
        >
          Contact
        </Button>
      </Flex>
    </Flex>
  );
}
```

## Pattern 8: Data Display Table

Display tabular data:

```typescript
import { Card, Grid, Box } from 'ui8kit-core';

interface User {
  id: string;
  name: string;
  email: string;
  status: string;
}

function UserTable({ users }: { users: User[] }) {
  return (
    <Card>
      <Card.Header>Users</Card.Header>
      <Card.Content>
        <Box className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {users.map(user => (
                <tr key={user.id}>
                  <td>{user.name}</td>
                  <td>{user.email}</td>
                  <td>{user.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </Box>
      </Card.Content>
    </Card>
  );
}
```

## Component Usage Tips

### Use Variants for Styling
```typescript
// Good - use variants
<Button padding="lg" bgColor="blue" rounded="md">Click</Button>

// Avoid - use className
<Button className="p-6 bg-blue-600 rounded-md">Click</Button>
```

### Use Compound Components for Structure
```typescript
// Good - semantic structure
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Content>Content</Card.Content>
  <Card.Footer>Actions</Card.Footer>
</Card>

// Less semantic
<div><div>Title</div><div>Content</div><div>Actions</div></div>
```

### ForwardRef for Direct Access
```typescript
// When you need direct DOM access
const buttonRef = useRef<HTMLButtonElement>(null);
<Button ref={buttonRef} onClick={() => buttonRef.current?.focus()} />
```

## Next Steps

- [Advanced Workflow](../advanced-workflow/README.md) - Handle complex scenarios
- [Best Practices](../best-practices/README.md) - Follow recommendations
- [API Reference](../../04-api-reference/README.md) - View component APIs
