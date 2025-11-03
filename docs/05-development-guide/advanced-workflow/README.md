# Advanced Workflow

## Overview

Advanced Workflow covers edge cases and complex scenarios where standard components may need customization or composition.

## Scenario 1: Custom Form Components

When form-specific components are absent, compose from Block + Box:

```typescript
import { Card, Block, Box, Button, Input } from 'ui8kit-core';

interface FormFieldProps {
  label: string;
  error?: string;
  children: React.ReactNode;
}

function FormField({ label, error, children }: FormFieldProps) {
  return (
    <Block marginBottom="md">
      <label className="block text-sm font-medium mb-2">
        {label}
      </label>
      {children}
      {error && (
        <Box className="text-red-500 text-sm mt-1">
          {error}
        </Box>
      )}
    </Block>
  );
}

function AdvancedForm() {
  const [values, setValues] = useState({ name: '', email: '' });
  const [errors, setErrors] = useState<Record<string, string>>({});

  const handleChange = (field: string, value: string) => {
    setValues(v => ({ ...v, [field]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Validation logic
  };

  return (
    <Card>
      <Card.Header>Advanced Form</Card.Header>
      <Card.Content>
        <form onSubmit={handleSubmit}>
          <FormField label="Name" error={errors.name}>
            <Input
              value={values.name}
              onChange={(e) => handleChange('name', e.target.value)}
              className={errors.name ? 'border-red-500' : ''}
            />
          </FormField>

          <FormField label="Email" error={errors.email}>
            <Input
              type="email"
              value={values.email}
              onChange={(e) => handleChange('email', e.target.value)}
              className={errors.email ? 'border-red-500' : ''}
            />
          </FormField>

          <Button type="submit" variant="primary">
            Submit
          </Button>
        </form>
      </Card.Content>
    </Card>
  );
}
```

## Scenario 2: Nested Composition

Build complex interfaces through composition:

```typescript
import { DashLayout, Grid, Card, SplitBlock, Flex } from 'ui8kit-core';

function ComplexDashboard() {
  return (
    <DashLayout 
      sidebar={<AdvancedSidebar />} 
      header={<AdvancedHeader />}
    >
      <DashLayout.Content>
        <Grid cols={2} gap="lg">
          {/* Left column */}
          <div>
            <Card>
              <Card.Header>Key Metrics</Card.Header>
              <Card.Content>
                <Grid cols={2} gap="md">
                  <MetricCard title="Total Users" value="1,234" />
                  <MetricCard title="Revenue" value="$45,678" />
                </Grid>
              </Card.Content>
            </Card>
          </div>

          {/* Right column */}
          <div>
            <SplitBlock
              left={<ChartCard />}
              right={<AnalyticsCard />}
              ratio="1:1"
            />
          </div>
        </Grid>
      </DashLayout.Content>
    </DashLayout>
  );
}

function MetricCard({ title, value }: { title: string; value: string }) {
  return (
    <Card padding="md">
      <div className="text-center">
        <div className="text-gray-500 text-sm">{title}</div>
        <div className="text-2xl font-bold mt-2">{value}</div>
      </div>
    </Card>
  );
}
```

## Scenario 3: Controlled Component State Management

Managing complex form state:

```typescript
import { Card, Input, Button, Alert } from 'ui8kit-core';
import { useState, useCallback } from 'react';

interface FormData {
  username: string;
  password: string;
  confirmPassword: string;
}

interface FormErrors {
  [key: string]: string;
}

function ComplexForm() {
  const [formData, setFormData] = useState<FormData>({
    username: '',
    password: '',
    confirmPassword: '',
  });

  const [errors, setErrors] = useState<FormErrors>({});
  const [submitted, setSubmitted] = useState(false);

  const validate = useCallback((data: FormData): FormErrors => {
    const newErrors: FormErrors = {};

    if (!data.username) {
      newErrors.username = 'Username is required';
    } else if (data.username.length < 3) {
      newErrors.username = 'Username must be at least 3 characters';
    }

    if (!data.password) {
      newErrors.password = 'Password is required';
    } else if (data.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }

    if (data.password !== data.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }

    return newErrors;
  }, []);

  const handleChange = (field: keyof FormData, value: string) => {
    setFormData(prev => ({
      ...prev,
      [field]: value,
    }));
    // Clear error for this field
    setErrors(prev => ({
      ...prev,
      [field]: '',
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    const newErrors = validate(formData);
    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      setSubmitted(true);
      // Submit logic
    }
  };

  return (
    <Card padding="lg" maxWidth="md">
      <Card.Header>Registration Form</Card.Header>
      <Card.Content>
        {submitted && (
          <Alert type="success" className="mb-4">
            Registration successful!
          </Alert>
        )}

        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2">
              Username
            </label>
            <Input
              value={formData.username}
              onChange={(e) => handleChange('username', e.target.value)}
              className={errors.username ? 'border-red-500' : ''}
            />
            {errors.username && (
              <p className="text-red-500 text-sm mt-1">{errors.username}</p>
            )}
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium mb-2">
              Password
            </label>
            <Input
              type="password"
              value={formData.password}
              onChange={(e) => handleChange('password', e.target.value)}
              className={errors.password ? 'border-red-500' : ''}
            />
            {errors.password && (
              <p className="text-red-500 text-sm mt-1">{errors.password}</p>
            )}
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium mb-2">
              Confirm Password
            </label>
            <Input
              type="password"
              value={formData.confirmPassword}
              onChange={(e) => handleChange('confirmPassword', e.target.value)}
              className={errors.confirmPassword ? 'border-red-500' : ''}
            />
            {errors.confirmPassword && (
              <p className="text-red-500 text-sm mt-1">{errors.confirmPassword}</p>
            )}
          </div>

          <Button type="submit" variant="primary">
            Register
          </Button>
        </form>
      </Card.Content>
    </Card>
  );
}
```

## Scenario 4: Ref Forwarding with Custom Logic

Accessing DOM for special interactions:

```typescript
import { Card, Button, Input } from 'ui8kit-core';
import { useRef } from 'react';

function SearchWithFocus() {
  const searchRef = useRef<HTMLInputElement>(null);
  const cardRef = useRef<HTMLDivElement>(null);

  const handleQuickSearch = () => {
    searchRef.current?.focus();
  };

  const handleClear = () => {
    if (searchRef.current) {
      searchRef.current.value = '';
      searchRef.current.focus();
    }
  };

  return (
    <Card ref={cardRef} padding="md">
      <Card.Header>Advanced Search</Card.Header>
      <Card.Content>
        <div className="flex gap-2">
          <Input
            ref={searchRef}
            type="text"
            placeholder="Search..."
          />
          <Button onClick={handleQuickSearch}>Focus</Button>
          <Button onClick={handleClear}>Clear</Button>
        </div>
      </Card.Content>
    </Card>
  );
}
```

## Scenario 5: Custom Hooks Integration

Using custom hooks with components:

```typescript
import { useState, useCallback, useEffect } from 'react';
import { Card, Grid, Button, Alert } from 'ui8kit-core';

function useAsync<T>(asyncFunction: () => Promise<T>, immediate = true) {
  const [status, setStatus] = useState<'idle' | 'pending' | 'success' | 'error'>('idle');
  const [value, setValue] = useState<T | null>(null);
  const [error, setError] = useState<Error | null>(null);

  const execute = useCallback(async () => {
    setStatus('pending');
    setValue(null);
    setError(null);
    try {
      const response = await asyncFunction();
      setValue(response);
      setStatus('success');
      return response;
    } catch (error) {
      setError(error as Error);
      setStatus('error');
    }
  }, [asyncFunction]);

  useEffect(() => {
    if (immediate) {
      execute();
    }
  }, [execute, immediate]);

  return { execute, status, value, error };
}

function DataDisplay() {
  const { execute, status, value, error } = useAsync(
    async () => {
      const response = await fetch('/api/data');
      return response.json();
    },
    false
  );

  return (
    <Card>
      <Card.Header>Async Data</Card.Header>
      <Card.Content>
        {status === 'pending' && <Alert type="info">Loading...</Alert>}
        {status === 'error' && (
          <Alert type="error">Error: {error?.message}</Alert>
        )}
        {status === 'success' && (
          <Grid cols={3} gap="md">
            {Array.isArray(value) && value.map((item, i) => (
              <Card key={i}>{JSON.stringify(item)}</Card>
            ))}
          </Grid>
        )}
        <Button onClick={() => execute()} className="mt-4">
          Fetch Data
        </Button>
      </Card.Content>
    </Card>
  );
}
```

## Best Practices for Advanced Scenarios

1. **Keep Components Focused** - Each component should have a single responsibility
2. **Use TypeScript** - Leverage types for complex logic
3. **Extract Custom Hooks** - Reuse state logic across components
4. **Validate at Component Level** - Validate data before rendering
5. **Use Composition** - Build complex UIs from simple components

## Next Steps

- [Best Practices](../best-practices/README.md) - General guidelines
- [Dark Mode](../dark-mode/README.md) - Theme implementation
- [API Reference](../../04-api-reference/README.md) - Component API details
