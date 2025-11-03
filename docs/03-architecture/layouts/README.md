# Layouts

## Overview

Layouts are complex page template systems located in `src/layouts/`. They represent the "organisms" in atomic design, composing UI components to create complete page structures for common scenarios: landing pages, dashboards, websites, and admin panels.

## Key Characteristics

- **Composition of components** - Built from UI and core components
- **Pre-built structures** - Common layout patterns ready to use
- **Template flexibility** - Customizable through props and children
- **Responsive design** - Mobile-friendly by default
- **Semantic HTML** - Proper document structure

## Common Layout Types

### 1. DashLayout
Vertical dashboard layout with sidebar navigation:

```typescript
<DashLayout
  sidebar={<NavMenu />}
  header={<TopBar />}
>
  <DashLayout.Content>
    Page content
  </DashLayout.Content>
</DashLayout>
```

Use cases:
- Admin dashboards
- Application interfaces
- Complex web applications

### 2. SplitBlock
Two-column split layout:

```typescript
<SplitBlock 
  left={<Sidebar />}
  right={<MainContent />}
  ratio="1:2"
/>
```

Use cases:
- Content with sidebar
- Two-panel interfaces
- Master-detail views

### 3. LayoutBlock
Flexible container for general layouts:

```typescript
<LayoutBlock
  padding="lg"
  maxWidth="6xl"
>
  Flexible content
</LayoutBlock>
```

Use cases:
- General page containers
- Responsive wrappers
- Content sections

### 4. Grid
Advanced grid layout system:

```typescript
<Grid
  cols={3}
  gap="md"
>
  {items.map(item => <Card key={item.id}>{item}</Card>)}
</Grid>
```

Use cases:
- Product grids
- Card layouts
- Dashboard widgets

### 5. Flex
Flexbox layout container:

```typescript
<Flex
  direction="row"
  justifyContent="between"
  alignItems="center"
  gap="md"
>
  Content items
</Flex>
```

Use cases:
- Navigation bars
- Button groups
- Flexible arrangements

## Composition Patterns

### Pattern 1: Simple Container
```typescript
export const MainLayout = ({ children }) => (
  <LayoutBlock padding="lg" maxWidth="6xl">
    <Header />
    {children}
    <Footer />
  </LayoutBlock>
);
```

### Pattern 2: Dashboard Layout
```typescript
export const AdminLayout = ({ children }) => (
  <DashLayout sidebar={<Sidebar />} header={<NavBar />}>
    <DashLayout.Content>
      {children}
    </DashLayout.Content>
  </DashLayout>
);
```

### Pattern 3: Two-Column Split
```typescript
export const BlogLayout = ({ post, sidebar }) => (
  <LayoutBlock>
    <SplitBlock
      left={<ArticleContent post={post} />}
      right={sidebar}
      ratio="2:1"
    />
  </LayoutBlock>
);
```

## Responsive Considerations

All layouts include responsive features:

- **Mobile first** - Base styles for mobile devices
- **Breakpoints** - Tailwind responsive prefixes (sm:, md:, lg:, xl:)
- **Stack on small** - Layouts collapse to single column on mobile
- **Touch targets** - Appropriate sizing for touch devices

## Layout Construction Strategies

### For Landing Pages
```typescript
<LayoutBlock>
  <Hero />
  <Features />
  <Testimonials />
  <CTA />
  <Footer />
</LayoutBlock>
```

### For Dashboards
```typescript
<DashLayout sidebar={<Navigation />}>
  <DashLayout.Content>
    <Grid cols={3} gap="md">
      <StatCard />
      <ChartCard />
      <TableCard />
    </Grid>
  </DashLayout.Content>
</DashLayout>
```

### For Websites
```typescript
<LayoutBlock>
  <Header />
  <SplitBlock left={<Sidebar />} right={<MainContent />} />
  <Footer />
</LayoutBlock>
```

### For Admin Panels
```typescript
<DashLayout sidebar={<AdminMenu />} header={<AdminBar />}>
  <Grid cols={2} gap="lg">
    <UserTable />
    <LogsWidget />
  </Grid>
</DashLayout>
```

## Best Practices

### 1. Compose Layouts from UI Components
```typescript
// ✓ Good
<Grid cols={3} gap="md">
  {items.map(item => <Card key={item.id}>{item}</Card>)}
</Grid>

// ✗ Avoid - low-level styling
<div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)' }}>
```

### 2. Use Semantic HTML
```typescript
// ✓ Good
<header><NavBar /></header>
<main><Content /></main>
<footer><Footer /></footer>

// ✗ Avoid - non-semantic
<div><NavBar /></div>
<div><Content /></div>
<div><Footer /></div>
```

### 3. Leverage Responsive Design
```typescript
// ✓ Good - responsive
<Grid cols={{base: 1, md: 2, lg: 3}} gap="md">

// ✗ Avoid - fixed layouts
<Grid cols={3} gap="md">
```

## Next Steps

- [Architecture Overview](../README.md) - Review the full architecture
- [UI Components](../ui-components/README.md) - See components used in layouts
- [API Reference - Layout Components](../../04-api-reference/layout-components/README.md) - Complete layout documentation
