# Layout Components API

Comprehensive guide to UI8Kit layout components - Container, Stack, Group, Grid and their usage.

## 📦 Container

Responsive container with preset maximum widths.

### Usage

```tsx
import { Container } from '@ui8kit/core'

<Container size="lg" centered px="md">
  <Block py="xl">
    Your content here
  </Block>
</Container>
```

### Props

```tsx
interface ContainerProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps {
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl'
  centered?: boolean
}
```

### Container Sizes

| Size | Max Width | Breakpoint |
|------|-----------|------------|
| `xs` | 640px  | - |
| `sm` | 768px  | `@media (min-width: 640px)` |
| `md` | 1024px | `@media (min-width: 768px)` |
| `lg` | 1280px | `@media (min-width: 1024px)` |
| `xl` | 1536px | `@media (min-width: 1280px)` |

### Examples

#### Basic Container
```tsx
<Container>
  <Text>Content is limited by max width</Text>
</Container>
```

#### Centered Container
```tsx
<Container centered>
  <Card w="full" maxW="md">
    <Text>This content is horizontally centered</Text>
  </Card>
</Container>
```

#### Responsive Container
```tsx
<Container size="lg" px={{ base: "md", md: "lg" }}>
  <Grid cols="1-2-3" gap="lg">
    <Card>Column 1</Card>
    <Card>Column 2</Card>
    <Card>Column 3</Card>
  </Grid>
</Container>
```

## 📚 Stack

Vertical stack of elements with gap control.

### Usage

```tsx
import { Stack } from '@ui8kit/core'

<Stack gap="lg" align="center" p="md">
  <Title>Heading</Title>
  <Text>Description</Text>
  <Button>Action</Button>
</Stack>
```

### Props

```tsx
interface StackProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps,
  Pick<VariantFlexProps, 'gap' | 'align'> {
  // Inherits spacing and flex props
}
```

### Examples

#### Basic Stack
```tsx
<Stack gap="md">
  <Title size="lg">Section Heading</Title>
  <Text>Section description with some text</Text>
  <Group gap="sm">
    <Button variant="outline">Cancel</Button>
    <Button>Save</Button>
  </Group>
</Stack>
```

#### Stack with Alignment
```tsx
<Stack gap="xl" align="center" ta="center">
  <Icon lucideIcon={CheckCircle} size="xl" c="success" />
  <Title>Success!</Title>
  <Text c="muted">Operation completed</Text>
  <Button size="lg">Continue</Button>
</Stack>
```

#### Stack with Dividers
```tsx
<Stack gap="lg">
  <Block>
    <Title size="md">Section 1</Title>
    <Text>Content of the first section</Text>
  </Block>

  <Block borderTop="default" pt="lg">
    <Title size="md">Section 2</Title>
    <Text>Content of the second section</Text>
  </Block>
</Stack>
```

## 🎯 Group

Horizontal stack with alignment and wrap control.

### Usage

```tsx
import { Group } from '@ui8kit/core'

<Group gap="md" align="center" justify="between">
  <Button variant="outline">Cancel</Button>
  <Button>Save</Button>
</Group>
```

### Props

```tsx
interface GroupProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps,
  Pick<VariantFlexProps, 'gap' | 'align' | 'justify' | 'wrap'> {
  // Inherits spacing and flex props
}
```

### Examples

#### Action Buttons
```tsx
<Group gap="sm" justify="end">
  <Button variant="outline">Cancel</Button>
  <Button variant="destructive">Delete</Button>
  <Button>Save</Button>
</Group>
```

#### Navigation with Icons
```tsx
<Group gap="lg" align="center">
  <Icon lucideIcon={Home} />
  <Text fw="medium">Home</Text>
  <Icon lucideIcon={ChevronRight} size="sm" />
  <Text c="muted">Current page</Text>
</Group>
```

#### Responsive Group
```tsx
<Group gap="md" wrap="wrap" justify="center">
  <Badge>React</Badge>
  <Badge>TypeScript</Badge>
  <Badge>Tailwind</Badge>
  <Badge>UI8Kit</Badge>
</Group>
```

## 🔲 Grid

CSS Grid with responsive column presets.

### Usage

```tsx
import { Grid, GridCol } from '@ui8kit/core'

<Grid cols="1-2-3" gap="lg">
  <GridCol span={2}>Wide column</GridCol>
  <GridCol>Regular column</GridCol>
  <GridCol>Regular column</GridCol>
</Grid>
```

### Props Grid

```tsx
interface GridProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps,
  VariantGridProps {
  cols?: string  // Format: "1-2-3" (mobile-tablet-desktop)
}
```

### Props GridCol

```tsx
interface GridColProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps {
  span?: number    // How many columns it spans
  start?: number   // Starting line
  end?: number     // Ending line
}
```

### Column Presets

| Preset | Mobile | Tablet | Desktop |
|--------|-----------|---------|---------|
| `"1"` | 1 column | 1 column | 1 column |
| `"1-2"` | 1 | 2 | 2 |
| `"1-2-3"` | 1 | 2 | 3 |
| `"1-2-4"` | 1 | 2 | 4 |
| `"1-3-6"` | 1 | 3 | 6 |

### Examples

#### Simple Grid
```tsx
<Grid cols="1-2-3" gap="md">
  <Card>Item 1</Card>
  <Card>Item 2</Card>
  <Card>Item 3</Card>
</Grid>
```

#### Grid with Different Column Sizes
```tsx
<Grid cols="3" gap="lg">
  <GridCol span={2}>
    <Card p="lg">
      <Title>Wide content</Title>
      <Text>This column spans 2/3 width</Text>
    </Card>
  </GridCol>
  <GridCol>
    <Card p="lg">
      <Title>Sidebar</Title>
      <Text>Narrow column</Text>
    </Card>
  </GridCol>
</Grid>
```

#### Asymmetric Grid
```tsx
<Grid cols="4" gap="md">
  <GridCol span={1} start={1}>1</GridCol>
  <GridCol span={2} start={2}>2-3</GridCol>
  <GridCol span={1} start={4}>4</GridCol>
</Grid>
```

#### Card Grid
```tsx
<Grid cols="1-2-3-4" gap="lg" p="lg">
  {items.map((item) => (
    <Card key={item.id} p="md" rounded="lg" shadow="md">
      <Image src={item.image} aspect="video" rounded="md" />
      <Stack gap="sm" mt="md">
        <Title size="lg">{item.title}</Title>
        <Text c="muted">{item.description}</Text>
        <Group justify="between" mt="sm">
          <Text fw="bold">{item.price}</Text>
          <Button size="sm">Buy</Button>
        </Group>
      </Stack>
    </Card>
  ))}
</Grid>
```

## 🏗️ Advanced Patterns

### Holy Grail Layout

```tsx
<Container minH="screen">
  <Stack gap="0">
    {/* Header */}
    <Block bg="primary" c="primary-foreground" p="md">
      <Group justify="between" align="center">
        <Title>Logo</Title>
        <Group gap="lg">
          <Button variant="ghost">Home</Button>
          <Button variant="ghost">About</Button>
          <Button variant="ghost">Contact</Button>
        </Group>
      </Group>
    </Block>

    {/* Main Content */}
    <Grid cols="1-4" gap="lg" p="lg" flex="grow">
      {/* Sidebar */}
      <GridCol span={1}>
        <Stack gap="md">
          <Card p="md">
            <Title size="md">Navigation</Title>
            {/* Navigation links */}
          </Card>
          <Card p="md">
            <Title size="md">Filters</Title>
            {/* Filters */}
          </Card>
        </Stack>
      </GridCol>

      {/* Content */}
      <GridCol span={3}>
        <Stack gap="lg">
          <Title>Main Content</Title>
          <Grid cols="1-2-3" gap="md">
            {/* Content cards */}
          </Grid>
        </Stack>
      </GridCol>
    </Grid>

    {/* Footer */}
    <Block bg="muted" c="muted-foreground" p="md" mt="auto">
      <Group justify="between" align="center">
        <Text>© 2024 UI8Kit</Text>
        <Group gap="md">
          <Button variant="link" size="sm">Policy</Button>
          <Button variant="link" size="sm">Terms</Button>
        </Group>
      </Group>
    </Block>
  </Stack>
</Container>
```

### Dashboard Layout

```tsx
<Container minH="screen" bg="background">
  <Grid cols="12" minH="screen">
    {/* Sidebar */}
    <GridCol span={2} bg="muted" p="lg">
      <Stack gap="lg">
        <Title size="lg">Dashboard</Title>
        <Stack gap="sm">
          <Button variant="ghost" w="full" justify="start">
            <Icon lucideIcon={Home} mr="sm" />
            Home
          </Button>
          <Button variant="ghost" w="full" justify="start">
            <Icon lucideIcon={Users} mr="sm" />
            Users
          </Button>
          <Button variant="ghost" w="full" justify="start">
            <Icon lucideIcon={Settings} mr="sm" />
            Settings
          </Button>
        </Stack>
      </Stack>
    </GridCol>

    {/* Main Content */}
    <GridCol span={10} p="lg">
      <Stack gap="lg">
        {/* Header */}
        <Group justify="between" align="center">
          <Title>Analytics</Title>
          <Group gap="sm">
            <Button variant="outline">Export</Button>
            <Button>Create Report</Button>
          </Group>
        </Group>

        {/* Stats Grid */}
        <Grid cols="1-2-4" gap="md">
          <Card p="md" bg="primary" c="primary-foreground">
            <Title size="2xl">1,234</Title>
            <Text>Users</Text>
          </Card>
          <Card p="md" bg="secondary" c="secondary-foreground">
            <Title size="2xl">567</Title>
            <Text>Orders</Text>
          </Card>
          <Card p="md" bg="accent" c="accent-foreground">
            <Title size="2xl">$89,012</Title>
            <Text>Revenue</Text>
          </Card>
          <Card p="md" bg="muted" c="foreground">
            <Title size="2xl">94.2%</Title>
            <Text>Conversion</Text>
          </Card>
        </Grid>

        {/* Charts and Tables */}
        <Grid cols="1-2" gap="lg">
          <Card p="lg">
            <Title size="lg" mb="md">Sales Chart</Title>
            {/* Chart component */}
          </Card>
          <Card p="lg">
            <Title size="lg" mb="md">Recent Orders</Title>
            {/* Table component */}
          </Card>
        </Grid>
      </Stack>
    </GridCol>
  </Grid>
</Container>
```

## 📱 Responsive Patterns

### Mobile-First Grid

```tsx
<Grid cols="1-2-3-4" gap="md">
  {/* Automatically: 1 column on mobile, 4 on desktop */}
  {Array.from({ length: 8 }, (_, i) => (
    <Card key={i} p="md">
      Item {i + 1}
    </Card>
  ))}
</Grid>
```

### Responsive Stack/Group

```tsx
{/* Stack on mobile, Group on desktop */}
<Box display={{ base: "flex", md: "block" }} flexDirection={{ base: "column", md: "row" }} gap="md">
  <Card>Item 1</Card>
  <Card>Item 2</Card>
  <Card>Item 3</Card>
</Box>
```

## 🔧 Customization

### Theming Layout Components

```tsx
const theme = {
  rounded: {
    container: "xl",
    card: "lg"
  },
  spacing: {
    section: "xl",
    card: "lg"
  }
}

// Usage in components
<Container rounded={theme.rounded.container} p={theme.spacing.section}>
  <Card rounded={theme.rounded.card} p={theme.spacing.card}>
    Content
  </Card>
</Container>
```

### Creating Custom Layout Components

```tsx
const PageLayout = ({ children, sidebar, header, footer }) => (
  <Container minH="screen">
    <Stack gap="0">
      {header && <Block as="header">{header}</Block>}
      <Group gap="0" flex="grow">
        {sidebar && (
          <Block w="64" minH="screen">
            {sidebar}
          </Block>
        )}
        <Block flex="grow" p="lg">
          {children}
        </Block>
      </Group>
      {footer && <Block as="footer">{footer}</Block>}
    </Stack>
  </Container>
)
```
