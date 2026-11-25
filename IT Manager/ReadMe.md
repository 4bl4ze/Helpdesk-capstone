# DESKTRACE — COMPLETE UI DESIGN SYSTEM
## Colours, Typography, CSS Architecture and Role-Based Visual Identity

I want you to establish a complete, consistent and implementation-ready design system for my application:

**Product:** DeskTrace – Campus IT Helpdesk & Asset Tracker

**Application type:** Institutional IT Helpdesk and Asset Management Progressive Web Application (PWA).

**Design objective:** Create one professional, modern, consistent application with four distinct role-based workspaces.

The four roles are:

1. Requester (University Staff/Lecturer)
2. Technician
3. IT Manager / Administrator
4. Asset Officer

IMPORTANT:

Each role must have its own identifiable colour theme and visual character. However, all four workspaces must clearly look like parts of the same software application.

Do not create four completely different design systems.

Use one shared foundation for typography, spacing, layout, components, buttons, tables, forms, navigation, borders and interaction states. Apply different role-specific colour themes on top of this foundation.

---

# SECTION 1 — GLOBAL DESIGN FOUNDATION

This section applies to ALL FOUR ROLES.

## 1.1 Overall design philosophy

Use a modern enterprise SaaS design language.

The interface should be:

- Professional and institutional.
- Clean and uncluttered.
- Easy to navigate.
- Consistent across all screens.
- Responsive across desktop, tablet and mobile.
- Accessible and readable.
- Suitable for prolonged daily use.

Avoid:
- Excessive gradients.
- Excessive shadows.
- Unnecessary decorative elements.
- Oversized dashboard cards.
- Inconsistent spacing.
- Too many competing accent colours.
- Excessive rounded elements.
- Unnecessary animations.
- Generic dashboard templates that do not reflect the actual purpose of DeskTrace.

Prioritise information hierarchy and usability over decoration.

## 1.2 Shared neutral colour palette

Use these colours as the foundation across all four workspaces.

| Purpose | Colour | Hex |
|---|---|---|
| Main application background | Light Grey | #F5F7FA |
| Primary surface | White | #FFFFFF |
| Secondary surface | Very Light Grey | #F8FAFC |
| Primary text | Dark Slate | #1F2937 |
| Secondary text | Slate Grey | #64748B |
| Muted text | Light Slate | #94A3B8 |
| Main borders | Light Border | #E2E8F0 |
| Strong borders | Medium Border | #CBD5E1 |
| Disabled elements | Disabled Grey | #E5E7EB |

Use white as the primary surface colour for content areas.

Use light grey for the overall page background.

Do not use the role-specific accent colour as the background of every card or section.

## 1.3 Typography system

Use **Inter** as the primary font family throughout DeskTrace.

Use the following fallback stack:

Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif.

Typography should be consistent across every role.

Recommended typography scale:

| Element | Font size | Weight |
|---|---:|---:|
| Main page heading | 28px | 700 |
| Section heading | 20px | 600 |
| Subsection heading | 16px | 600 |
| Card heading | 15px | 600 |
| Body text | 14px | 400 |
| Secondary text | 13px | 400 |
| Labels | 13px | 500 |
| Button text | 14px | 600 |
| Small metadata | 12px | 400 |
| Large KPI value | 28–32px | 700 |

Typography rules:

- Use sentence case for headings.
- Avoid unnecessary uppercase text.
- Use consistent line heights.
- Maintain sufficient contrast.
- Do not make body text unnecessarily small.
- Use tabular numbers for ticket references, timestamps, SLA countdowns and numerical statistics where appropriate.
- Ensure long ticket descriptions remain comfortable to read.

## 1.4 Spacing system

Use a consistent 4px-based spacing scale.

| Token | Value | Typical use |
|---|---:|---|
| space-1 | 4px | Very small gaps |
| space-2 | 8px | Icon and text spacing |
| space-3 | 12px | Compact component spacing |
| space-4 | 16px | Standard internal spacing |
| space-5 | 20px | Component separation |
| space-6 | 24px | Card padding and section gaps |
| space-8 | 32px | Major section separation |
| space-10 | 40px | Large layout gaps |
| space-12 | 48px | Page-level spacing |

Use 16px as a common internal component spacing value and 24px as a common card padding value.

Do not allow components to appear cramped or randomly spaced.

## 1.5 Border radius system

Use consistent corner radii:

- Small inputs and buttons: 6px.
- Standard cards: 10px.
- Large panels and dialogs: 12px.
- Pills and status labels: fully rounded.

Avoid excessive rounding.

DeskTrace should look professional rather than playful.

## 1.6 Shadows and elevation

Use subtle shadows only where they communicate hierarchy.

Recommended:

- Standard card: 0 1px 3px rgba(15, 23, 42, 0.06).
- Floating dropdown: 0 4px 12px rgba(15, 23, 42, 0.08).
- Modal: 0 12px 32px rgba(15, 23, 42, 0.12).

Use light borders as the primary method of separating sections.

Do not give every element a shadow.

## 1.7 Shared status colour system

These colours MUST remain consistent across every role.

They represent operational status, not role identity.

| Status | Colour | Hex |
|---|---|---|
| Success / Resolved | Green | #16A36A |
| Warning / Approaching SLA | Amber | #F0A52B |
| Critical / SLA Breached | Red | #DC4545 |
| Informational | Blue | #3478F6 |
| Neutral / Pending | Slate | #64748B |

Apply these colours consistently to:
- Ticket status badges.
- SLA indicators.
- Notifications.
- Validation messages.
- Asset condition indicators.
- Work completion states.

Do not change these status colours between roles just because their accent colours differ.

---

# SECTION 2 — REQUESTER WORKSPACE DESIGN SYSTEM

## 2.1 Role identity

Role: Requester (University Staff/Lecturer).

The Requester workspace is intended for people who need to report IT problems and monitor their own support requests.

Its visual character should be:

- Approachable.
- Calm.
- Friendly.
- Simple.
- Reassuring.
- Easy to understand for non-technical users.

The interface should not feel like a complicated technical administration system.

## 2.2 Requester colour palette

Use the following exact palette.

| Purpose | Colour | Hex |
|---|---|---|
| Primary role colour | Teal | #176B87 |
| Primary hover | Dark Teal | #12576F |
| Soft accent background | Pale Blue | #EAF4F7 |
| Selected navigation | Light Teal | #DCEEF2 |
| Main text | Dark Slate | #253746 |
| Secondary text | Slate | #64748B |
| Borders | Light Grey | #E2E8F0 |
| Main background | #F5F7FA |
| Cards | White | #FFFFFF |

## 2.3 Colour application

Use Teal (#176B87) for:
- Primary buttons.
- Report a Fault action.
- Selected sidebar navigation.
- Important links.
- Focus indicators.
- Selected form controls.

Use Pale Blue (#EAF4F7) for:
- Subtle highlighted sections.
- Selected states.
- Informational panels.

Use white and neutral grey for the majority of the interface.

Do not make the entire requester dashboard blue or teal.

## 2.4 Typography emphasis

Maintain the global Inter typography system.

For this role:
- Use clear and readable headings.
- Keep descriptions concise.
- Use accessible form labels.
- Make primary actions easy to identify.
- Avoid technical jargon.

Prioritise the visibility of the Report a Fault button.

## 2.5 Component styling

Buttons:
- Primary: Teal background with white text.
- Secondary: White background with Teal border and text.
- Destructive: Red.
- Disabled: Neutral grey.

Forms:
- White input surfaces.
- Clear labels above inputs.
- Subtle borders.
- Visible focus states.
- Helpful validation messages.

Ticket lists:
- Clean and readable.
- Clear status labels.
- Minimal unnecessary columns.

Navigation:
- Simple and approachable.
- Teal selected-state indicator.
- Consistent sidebar dimensions.

## 2.6 Role-specific CSS theme

Implement this role using CSS custom properties.

Theme class: .theme-requester

Suggested variables:

--role-primary: #176B87;
--role-primary-hover: #12576F;
--role-primary-soft: #EAF4F7;
--role-selected-bg: #DCEEF2;
--role-text: #253746;

The Requester theme must reuse the shared global design tokens rather than defining an entirely separate CSS system.

---

# SECTION 3 — TECHNICIAN WORKSPACE DESIGN SYSTEM

## 3.1 Role identity

Role: Technician.

This workspace is used by IT technicians who receive automatically assigned work orders, diagnose faults, inspect equipment and record repairs.

Its visual character should be:

- Technical.
- Operational.
- Focused.
- Efficient.
- Structured.
- Professional.

The technician should be able to identify urgent work and take action quickly.

## 3.2 Technician colour palette

Use the following exact palette.

| Purpose | Colour | Hex |
|---|---|---|
| Primary role colour | Technical Blue | #2457C5 |
| Primary hover | Dark Blue | #1D46A1 |
| Soft accent background | Pale Blue | #EEF3FC |
| Selected navigation | Light Blue | #DCE7FA |
| Main text | Charcoal | #1F2937 |
| Secondary text | Slate | #64748B |
| Borders | Light Grey | #E2E8F0 |
| Main background | #F5F7FA |
| Cards | White | #FFFFFF |

## 3.3 Colour application

Use Technical Blue (#2457C5) for:
- Primary work actions.
- Start Work.
- Acknowledge Job.
- Selected navigation.
- Important operational links.
- Focus states.

Use Pale Blue (#EEF3FC) for:
- Selected work sections.
- Subtle information panels.
- Technical metadata grouping.

Continue to use the global red, amber and green status colours for SLA and ticket conditions.

Do not use blue to represent every status.

## 3.4 Typography emphasis

Maintain the global Inter typography system.

For technicians:
- Make ticket titles easy to scan.
- Make SLA countdowns prominent.
- Use tabular numbers for countdowns and working hours.
- Make work instructions comfortable to read.
- Use clear distinctions between primary actions and secondary information.

Prioritise readability during prolonged operational use.

## 3.5 Component styling

Work order cards:
- Clear priority indicator.
- Ticket reference.
- Fault title.
- Location.
- Estimated effort.
- SLA countdown.
- Status.

SLA indicators:
- Green: healthy.
- Amber: approaching deadline.
- Red: critical or breached.

Buttons:
- Primary: Technical Blue.
- Secondary: White with Blue border.
- Resolve: Green.
- Request Reassignment: Clearly visible secondary action.
- Destructive: Red.

Tables:
- Compact but readable.
- Clear column alignment.
- Consistent row spacing.
- Visible hover and selection states.

Forms:
- Structured diagnosis and resolution fields.
- Clear labels.
- Comfortable text areas.
- Evidence upload previews.

## 3.6 Role-specific CSS theme

Theme class: .theme-technician

Suggested variables:

--role-primary: #2457C5;
--role-primary-hover: #1D46A1;
--role-primary-soft: #EEF3FC;
--role-selected-bg: #DCE7FA;
--role-text: #1F2937;

Use the shared global CSS foundation.

Do not create an independent typography, spacing or component system.

---

# SECTION 4 — IT MANAGER WORKSPACE DESIGN SYSTEM

## 4.1 Role identity

Role: IT Manager / Administrator.

This workspace controls the institution's IT support operation.

The manager oversees:
- All support tickets.
- Automatic technician assignment.
- Technician workload.
- Technician skills and performance.
- Reassignment requests.
- SLA policies.
- Operational analytics.
- Escalations.

The visual character should be:

- Authoritative.
- Professional.
- Analytical.
- Organised.
- Trustworthy.
- Information-rich without being cluttered.

This should look like a professional IT operations control centre.

## 4.2 IT Manager colour palette

Use the following exact palette.

| Purpose | Colour | Hex |
|---|---|---|
| Primary role colour | Deep Navy | #172B4D |
| Primary action accent | Executive Blue | #3478F6 |
| Primary hover | Dark Blue | #245CC5 |
| Soft accent background | Cool Grey | #F4F6FA |
| Selected navigation | Pale Blue | #E8EFFB |
| Main text | Dark Charcoal | #1F2937 |
| Secondary text | Slate | #64748B |
| Borders | Light Grey | #E2E8F0 |
| Main background | #F5F7FA |
| Cards | White | #FFFFFF |

## 4.3 Colour application

Use Deep Navy (#172B4D) for:
- Main navigation identity.
- Selected sidebar indicators.
- Important section headings.
- Manager workspace identity.

Use Executive Blue (#3478F6) for:
- Primary management actions.
- Assignment controls.
- Selected data visualisations.
- Important links.
- Interactive elements.

Use neutral backgrounds for dashboards and tables.

Use red, amber and green exclusively for their shared operational status meanings.

Do not use navy as the background of every dashboard card.

## 4.4 Typography emphasis

Maintain the global Inter typography system.

For the manager:
- Use strong page headings.
- Use readable KPI values.
- Use tabular numbers for operational statistics.
- Ensure charts have clear labels.
- Use concise descriptions.
- Distinguish important alerts from normal information.

The manager needs to process considerable information, so visual hierarchy is especially important.

## 4.5 Component styling

Dashboard summaries:
- Compact KPI components.
- Clear numerical values.
- Small descriptive labels.
- Minimal decorative elements.

Data tables:
- Strong header hierarchy.
- Consistent column spacing.
- Readable row density.
- Clear filtering controls.

Charts:
- Use consistent typography.
- Keep axes and labels readable.
- Avoid unnecessary chart decorations.
- Use the shared status colours when representing operational conditions.

Assignment & Workforce Control:
- Make workload utilisation visually clear.
- Show assigned effort hours versus available hours.
- Use horizontal capacity indicators.
- Use timelines for dispatch schedules.
- Show why a technician was automatically selected.
- Make reassignment requests easy to review.

Buttons:
- Primary: Executive Blue.
- Secondary: White with Blue border.
- Critical intervention: Red.
- Approval: Green.
- Neutral administrative actions: Slate.

## 4.6 Role-specific CSS theme

Theme class: .theme-manager

Suggested variables:

--role-primary: #172B4D;
--role-action: #3478F6;
--role-primary-hover: #245CC5;
--role-primary-soft: #F4F6FA;
--role-selected-bg: #E8EFFB;
--role-text: #1F2937;

Use navy as the manager's identity colour and blue as its interactive accent.

Do not replace the global status palette with role-specific status colours.

---

# SECTION 5 — ASSET OFFICER WORKSPACE DESIGN SYSTEM

## 5.1 Role identity

Role: Asset Officer.

This workspace is responsible for managing the institution's IT equipment and inventory.

Responsibilities include:
- Registering equipment.
- Updating asset records.
- Managing asset location and custodians.
- Monitoring device condition.
- Tracking warranties.
- Generating and printing QR labels.
- Maintaining software licence records.

The visual character should be:

- Organised.
- Reliable.
- Structured.
- Practical.
- Calm.
- Focused on inventory management.

## 5.2 Asset Officer colour palette

Use the following exact palette.

| Purpose | Colour | Hex |
|---|---|---|
| Primary role colour | Forest Green | #176B52 |
| Primary hover | Dark Green | #125740 |
| Soft accent background | Pale Green | #EAF4EF |
| Selected navigation | Light Green | #D9ECE2 |
| Main text | Dark Green Grey | #34443C |
| Secondary text | Slate | #64748B |
| Borders | Light Grey | #E2E8F0 |
| Main background | #F5F7FA |
| Cards | White | #FFFFFF |

## 5.3 Colour application

Use Forest Green (#176B52) for:
- Primary buttons.
- Register Equipment action.
- QR generation actions.
- Selected navigation.
- Important asset management links.

Use Pale Green (#EAF4EF) for:
- Subtle asset information sections.
- Selected navigation states.
- Inventory status groupings where appropriate.

Use the shared global status colours for asset conditions and operational warnings.

Do not use green as the background of the entire inventory interface.

## 5.4 Typography emphasis

Maintain the global Inter typography system.

For the Asset Officer:
- Make asset tags easy to identify.
- Use tabular numbers for serial numbers and asset identifiers where appropriate.
- Keep inventory tables readable.
- Make form labels clear.
- Use distinct section headings for asset identification, ownership, location and maintenance.

## 5.5 Component styling

Inventory tables:
- Clear column headings.
- Readable row spacing.
- Search and filter controls.
- Clear asset status indicators.

Asset forms:
- Clearly separated form sections.
- Consistent field heights.
- Logical grouping.
- Helpful validation messages.
- Clear save and update actions.

QR management:
- Large QR previews.
- Clear printable label layout.
- Proper alignment.
- Asset identification labels.
- Print-friendly layout.

Warranty:
- Green for valid warranties.
- Amber for approaching expiry.
- Red for expired warranties.

Buttons:
- Primary: Forest Green.
- Secondary: White with Green border.
- Destructive: Red.
- Neutral: Slate.

## 5.6 Role-specific CSS theme

Theme class: .theme-asset-officer

Suggested variables:

--role-primary: #176B52;
--role-primary-hover: #125740;
--role-primary-soft: #EAF4EF;
--role-selected-bg: #D9ECE2;
--role-text: #34443C;

Reuse the global design foundation.

Do not create separate spacing, typography or component rules.

---

# SECTION 6 — CSS ARCHITECTURE AND IMPLEMENTATION SYSTEM

This section is very important.

I want the design system to be organised in a way that can later be implemented cleanly using React and CSS.

Do not create four completely independent stylesheets with duplicated components.

Use a shared design token system with role-specific theme overrides.

## 6.1 Recommended CSS architecture

Use:

1. CSS custom properties (CSS variables) for design tokens.
2. A shared global stylesheet for foundational styles.
3. Shared component styles for common UI elements.
4. CSS Modules for component-level style isolation.
5. Role-specific theme classes for colour overrides.

Suggested project organisation:

src/
  styles/
    tokens.css
    global.css
    typography.css
    themes.css
    utilities.css

  components/
    Button/
    Card/
    Input/
    Select/
    Badge/
    Table/
    Modal/
    Sidebar/
    Topbar/
    Notification/

  layouts/
    AppLayout/
    RequesterLayout/
    TechnicianLayout/
    ManagerLayout/
    AssetOfficerLayout/

  features/
    requester/
    technician/
    manager/
    asset-officer/

The precise file structure can be adapted to the existing application architecture. Do not unnecessarily restructure an existing project merely to follow this example.

## 6.2 Global CSS tokens

Define reusable CSS custom properties for:

- Global colours.
- Typography.
- Font weights.
- Font sizes.
- Spacing.
- Border radii.
- Borders.
- Shadows.
- Layout dimensions.
- Responsive breakpoints where appropriate.

Example:

:root {
  --font-family-base: "Inter", sans-serif;

  --font-size-xs: 12px;
  --font-size-sm: 13px;
  --font-size-base: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 20px;
  --font-size-2xl: 28px;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;

  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  --color-background: #F5F7FA;
  --color-surface: #FFFFFF;
  --color-text: #1F2937;
  --color-text-secondary: #64748B;
  --color-border: #E2E8F0;

  --color-success: #16A36A;
  --color-warning: #F0A52B;
  --color-danger: #DC4545;
  --color-info: #3478F6;
}

## 6.3 Role-specific CSS variables

Implement the role themes using CSS classes.

Example:

.theme-requester {
  --role-primary: #176B87;
  --role-primary-hover: #12576F;
  --role-primary-soft: #EAF4F7;
  --role-selected-bg: #DCEEF2;
  --role-text: #253746;
}

.theme-technician {
  --role-primary: #2457C5;
  --role-primary-hover: #1D46A1;
  --role-primary-soft: #EEF3FC;
  --role-selected-bg: #DCE7FA;
  --role-text: #1F2937;
}

.theme-manager {
  --role-primary: #172B4D;
  --role-action: #3478F6;
  --role-primary-hover: #245CC5;
  --role-primary-soft: #F4F6FA;
  --role-selected-bg: #E8EFFB;
  --role-text: #1F2937;
}

.theme-asset-officer {
  --role-primary: #176B52;
  --role-primary-hover: #125740;
  --role-primary-soft: #EAF4EF;
  --role-selected-bg: #D9ECE2;
  --role-text: #34443C;
}

Shared components must consume these variables.

For example, a primary button should use the active role's primary colour rather than having four duplicated button implementations.

## 6.4 Shared component rules

Create one reusable component system for:

- Primary buttons.
- Secondary buttons.
- Inputs.
- Dropdowns.
- Search fields.
- Cards.
- Tables.
- Status badges.
- Tabs.
- Modals.
- Notifications.
- Navigation items.
- Pagination.
- Empty states.
- Loading states.
- Tooltips.

The same component should maintain its dimensions, typography, spacing, interaction states and basic structure across all roles.

Only the active theme colours and necessary role-specific behaviour should change.

Do not duplicate components just to change their colours.

## 6.5 Responsive CSS system

Use a consistent responsive layout.

Recommended breakpoints:

| Device | Width |
|---|---|
| Small mobile | Below 480px |
| Mobile / large phone | 480px–767px |
| Tablet | 768px–1023px |
| Desktop | 1024px–1439px |
| Large desktop | 1440px and above |

Responsive requirements:

Desktop:
- Persistent or collapsible sidebar.
- Full topbar.
- Main content workspace.
- Tables and dashboard sections displayed comfortably.

Tablet:
- Collapsible sidebar.
- Reduced spacing.
- Responsive grid layouts.
- Tables may allow horizontal scrolling or switch to compact layouts.

Mobile:
- Compact navigation or bottom navigation where appropriate.
- Single-column layouts.
- Touch-friendly controls.
- Forms stacked vertically.
- Important actions easy to access.
- Tables adapted into readable cards or horizontally scrollable structures.

Do not simply shrink desktop screens to fit mobile.

Redesign the layout appropriately for smaller screens.

## 6.6 Accessibility requirements

Apply:
- Sufficient colour contrast.
- Visible keyboard focus states.
- Clear labels.
- Accessible button sizes.
- Consistent interaction feedback.
- Readable text.
- Colour-independent status indicators.

Never communicate a ticket status using colour alone. Include text labels or icons alongside the colour.

## 6.7 Design consistency requirements

All four roles must share:
- The same typography.
- The same spacing scale.
- The same component dimensions.
- The same input styling.
- The same button structure.
- The same table conventions.
- The same modal behaviour.
- The same notification pattern.
- The same offline and sync indicators.
- The same global status colours.

Only the role-specific accent colours and role-specific layouts should differ.

---

# SECTION 7 — FINAL DESIGN SYSTEM DELIVERABLES

I want the final output to include:

1. A global DeskTrace colour palette.
2. A separate colour palette for each of the four roles.
3. Typography specifications.
4. Spacing and layout specifications.
5. Border radius and shadow specifications.
6. Shared component styling rules.
7. Role-specific component colour rules.
8. CSS custom properties and theme definitions.
9. Responsive breakpoint specifications.
10. Accessibility guidelines.

Present each role's design system in a clearly separated section with distinct headings.

Do not mix the four role palettes together.

Make it easy for a developer to identify which colours, typography rules, tokens and component behaviours are global and which belong to a specific role.

### FINAL INSTRUCTION

Treat this as the official DeskTrace design system.

All future screens, components, dashboards, forms, tables and navigation elements must follow these specifications.

Do not introduce new colours, font families, spacing scales or component styles without a clear reason.

The result must be visually consistent, technically organised and ready to guide the implementation of DeskTrace using React, CSS and a responsive PWA architecture.