# Layout Components API

## Overview

Layout Components are complex page template systems located in `src/layouts/`. They compose UI components to create complete page structures for common scenarios.

## Components List

Main layout components:

- **DashLayout** - Dashboard layout with sidebar
- **SplitBlock** - Two-column split layout
- **LayoutBlock** - Flexible container layout
- **Grid** - Advanced grid layout (layout version)
- **Flex** - Flexbox layout container

## DashLayout Component

### Overview
Vertical dashboard layout with sidebar navigation and top header.

### Props Interface
```typescript
interface DashLayoutProps extends React.HTMLAttributes<HTMLDivElement> {
  sidebar?: React.ReactNode;
  header?: React.ReactNode;
  sidebarWidth?: string;
  collapsed?: boolean;
  onToggleSidebar?: () => void;
}
```

### Usage Example

```typescript
import { DashLayout } from 'ui8kit-core';

<DashLayout
  sidebar={<NavMenu />}
  header={<TopBar />}
>
  <DashLayout.Content>
    <h1>Dashboard Content</h1>
  </DashLayout.Content>
</DashLayout>
```

### Subcomponents

#### DashLayout.Content
Main content area of the dashboard.

```typescript
<DashLayout.Content>
  Dashboard content here
</DashLayout.Content>
```

### Use Cases

- Admin dashboards
- Application interfaces
- Complex web applications with navigation

## SplitBlock Component

### Overview
Two-column split layout for side-by-side content.

### Props Interface
```typescript
interface SplitBlockProps extends React.HTMLAttributes<HTMLDivElement> {
  left?: React.ReactNode;
  right?: React.ReactNode;
  ratio?: string;  // e.g., "1:2", "2:1"
  gap?: string;
  responsive?: boolean;
}
```

### Props Table

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `left` | `ReactNode` | - | Left panel content |
| `right` | `ReactNode` | - | Right panel content |
| `ratio` | `string` | `'1:1'` | Column ratio (e.g., "1:2") |
| `gap` | `string` | `'md'` | Gap between columns |
| `responsive` | `boolean` | `true` | Stack on mobile |

### Usage Example

```typescript
import { SplitBlock } from 'ui8kit-core';

<SplitBlock
  left={<Sidebar />}
  right={<MainContent />}
  ratio="1:2"
  gap="lg"
/>
```

### Use Cases

- Content with sidebar
- Two-panel interfaces
- Master-detail views
- Blog layouts (article + sidebar)

## LayoutBlock Component

### Overview
Flexible container for general page layouts.

### Props Interface
```typescript
interface LayoutBlockProps extends React.HTMLAttributes<HTMLDivElement> {
  padding?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  maxWidth?: 'sm' | 'md' | 'lg' | 'xl' | '6xl';
  centered?: boolean;
}
```

### Props Table

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `padding` | spacing values | `'md'` | Container padding |
| `maxWidth` | width values | `'6xl'` | Maximum width |
| `centered` | `boolean` | `true` | Center content |

### Usage Example

```typescript
import { LayoutBlock } from 'ui8kit-core';

<LayoutBlock padding="lg" maxWidth="6xl" centered>
  <Header />
  <MainContent />
  <Footer />
</LayoutBlock>
```

### Use Cases

- General page containers
- Responsive wrappers
- Content sections
- Landing pages

## Grid Component (Layout Version)

### Overview
Advanced grid layout system for arranging multiple items.

### Props Interface
```typescript
interface GridProps extends React.HTMLAttributes<HTMLDivElement> {
  cols?: number | { base?: number; md?: number; lg?: number };
  gap?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  autoFit?: boolean;
}
```

### Props Table

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `cols` | `number \| object` | `1` | Number of columns |
| `gap` | spacing values | `'md'` | Gap between items |
| `autoFit` | `boolean` | `false` | Auto-fit columns |

### Usage Examples

```typescript
import { Grid } from 'ui8kit-core';

// Fixed 3 columns
<Grid cols={3} gap="md">
  <Card>Item 1</Card>
  <Card>Item 2</Card>
  <Card>Item 3</Card>
</Grid>

// Responsive columns
<Grid 
  cols={{ base: 1, md: 2, lg: 3 }}
  gap="lg"
>
  {items.map(item => <Card key={item.id}>{item}</Card>)}
</Grid>

// Auto-fitting columns
<Grid cols={3} gap="md" autoFit>
  {items.map(item => <Card key={item.id}>{item}</Card>)}
</Grid>
```

### Use Cases

- Product grids
- Card layouts
- Dashboard widgets
- Gallery layouts

## Flex Component

### Overview
Flexbox layout container for flexible arrangements.

### Props Interface
```typescript
interface FlexProps extends React.HTMLAttributes<HTMLDivElement> {
  direction?: 'row' | 'col';
  justify?: 'start' | 'center' | 'between' | 'end';
  align?: 'start' | 'center' | 'end' | 'stretch';
  gap?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  wrap?: boolean;
}
```

### Props Table

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `direction` | `'row' \| 'col'` | `'row'` | Flex direction |
| `justify` | justify values | `'start'` | Main axis alignment |
| `align` | align values | `'center'` | Cross axis alignment |
| `gap` | spacing values | `'md'` | Gap between items |
| `wrap` | `boolean` | `false` | Allow wrapping |

### Usage Examples

```typescript
import { Flex } from 'ui8kit-core';

// Navigation bar
<Flex direction="row" justify="between" align="center" gap="md">
  <Logo />
  <NavItems />
  <UserMenu />
</Flex>

// Button group
<Flex gap="md" justify="center">
  <Button>Cancel</Button>
  <Button variant="primary">Save</Button>
</Flex>

// Vertical stack with spacing
<Flex direction="col" gap="lg">
  <Card>Card 1</Card>
  <Card>Card 2</Card>
  <Card>Card 3</Card>
</Flex>

// Wrapping items
<Flex wrap justify="between" gap="md">
  {items.map(item => <Tag key={item.id}>{item}</Tag>)}
</Flex>
```

### Use Cases

- Navigation bars
- Button groups
- Flexible arrangements
- Centered content
- Spaced lists

## Layout Composition Patterns

### Landing Page Pattern

```typescript
<LayoutBlock maxWidth="6xl">
  <DashLayout sidebar={null}>
    <DashLayout.Content>
      <Hero />
      <Features />
      <Testimonials />
      <CTA />
      <Footer />
    </DashLayout.Content>
  </DashLayout>
</LayoutBlock>
```

### Dashboard Pattern

```typescript
<DashLayout sidebar={<AdminNav />} header={<AdminBar />}>
  <DashLayout.Content>
    <Grid cols={3} gap="md">
      <StatCard />
      <ChartCard />
      <TableCard />
    </Grid>
  </DashLayout.Content>
</DashLayout>
```

### Article Layout Pattern

```typescript
<LayoutBlock maxWidth="4xl">
  <SplitBlock
    left={<ArticleContent />}
    right={<SidebarWidget />}
    ratio="2:1"
  />
</LayoutBlock>
```

## Responsive Considerations

All layout components include responsive features:

- **Mobile first** - Base styles for mobile
- **Breakpoints** - Responsive props for different sizes
- **Stack on small** - Layouts adapt for small screens
- **Touch targets** - Appropriate sizing

## Styling

Layout components accept standard styling:

```typescript
<LayoutBlock 
  className="custom-class"
  style={{ backgroundColor: '#f5f5f5' }}
>
  Content
</LayoutBlock>
```

## Next Steps

- [UI Components](../ui-components/README.md) - Learn about component building blocks
- [Architecture Layouts](../../03-architecture/layouts/README.md) - Understand layout concepts
- [Development Guide](../../05-development-guide/README.md) - Practical usage patterns
