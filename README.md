# UI8Kit Documentation

**UI8Kit** - современная React UI библиотека с TypeScript-first подходом, utility-first стилизацией и полиморфными компонентами.

## 📚 Документация

### Быстрый старт
- **[Overview](overview.md)** - Общий обзор библиотеки
- **[Getting Started](getting-started.md)** - Установка и настройка

### API Reference
- **[Components](api-reference/components.md)** - Справочник всех компонентов
- **[Core UI](api-reference/core-ui.md)** - Система вариантов и утилит
- **[Layouts](api-reference/layouts.md)** - Лейаут компоненты (Container, Stack, Grid)

### Архитектура
- **[Architecture Overview](architecture/overview.md)** - Общая архитектура
- **[Variant System](architecture/variant-system.md)** - Система вариантов (CVA)
- **[Package Structure](architecture/package-structure.md)** - Структура пакетов
- **[TypeScript Configuration](architecture/typescript-configuration.md)** - Настройка TS
- **[Build System](architecture/build-system.md)** - Система сборки

### Разработка
- **[Development Guide](development-guide/development-guide.md)** - Основное руководство
- **[Basic Workflow](development-guide/basic-workflow.md)** - Пошаговый workflow
- **[Best Practices](development-guide/best-practices.md)** - Лучшие практики
- **[Dark Mode](development-guide/dark-mode.md)** - Реализация тем

### Решение проблем
- **[Troubleshooting](troubleshooting.md)** - Решение распространенных проблем

## 🚀 Ключевые возможности

- **TypeScript-first**: Полная типизация с автодополнением
- **Utility-first**: Все стили через пропы компонентов
- **Полиморфные компоненты**: Любой HTML элемент через `component` проп
- **Система вариантов**: Консистентная стилизация через CVA
- **Dark mode**: Встроенная поддержка тем
- **Tree shaking**: Автоматическое удаление неиспользуемого кода
- **Accessibility**: ARIA атрибуты и keyboard navigation

## 📦 Установка

```bash
npm install @ui8kit/core
```

## 🎯 Пример использования

```tsx
import { Button, Block, Container, Stack, Card } from '@ui8kit/core'
import { ThemeProvider } from './providers/theme'

function App() {
  return (
    <ThemeProvider theme={defaultTheme}>
      <Container>
        <Stack gap="lg" align="center">
          <Block py="xl" ta="center">
            <Title size="4xl">Welcome to UI8Kit</Title>
            <Text c="muted">Modern React UI Library</Text>
          </Block>

          <Card p="lg" rounded="xl">
            <Stack gap="md">
              <Text fw="bold">Getting Started</Text>
              <Button variant="primary" size="lg">
                Learn More
              </Button>
            </Stack>
          </Card>
        </Stack>
      </Container>
    </ThemeProvider>
  )
}
```

## 🏗️ Архитектура

```
USER LEVEL               COMPOSITE LEVEL           PRIMITIVE LEVEL
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ <Button         │────▶│ components/ui/Button │────▶│ core/ui/Button    │
│   variant="primary"│     │ + buttonVariants   │     │ (no styles)     │
│   size="lg"     │     │ + spacingVariants │     │                 │
│   rounded="md"  │     │ = Beautiful API  │     │                 │
│ />              │     │                  │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## 📊 Performance

- **Bundle size**: ~15KB gzipped (весь core)
- **Tree shaking**: Автоматическое удаление неиспользуемого кода
- **Zero runtime**: Стили компилируются в CSS
- **Stable references**: Нет ненужных ре-рендеров

## 🤝 Сообщество

- **GitHub**: [github.com/ui8kit/core](https://github.com/ui8kit/core)
- **Issues**: Для баг репортов и фич реквестов
- **Discussions**: Для вопросов и обсуждений

## 📄 Лицензия

GPL-3.0

---

**Начните разработку с [Getting Started](getting-started.md)!** 🚀