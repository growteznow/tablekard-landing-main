# Tablekard — Landing Page & Onboarding Website

## Background

Tablekard is a multi-tenant SaaS platform for restaurants that provides **QR-based contactless dine-in ordering**. Customers scan a table QR code, browse a digital menu, place orders, and pay — all from their phone, with zero app downloads. Restaurant admins manage menus, orders, tables, and staff from a real-time dashboard.

This plan covers:
1. **Marketing Landing Page** — to attract restaurant owners and convert them into sign-ups
2. **Restaurant Onboarding Flow** — a multi-step wizard that guides new restaurants through setup

---

## Proposed Changes

### New App: `apps/landing` (React + Vite)

A standalone app in the existing monorepo — keeps the marketing site decoupled from the admin/customer apps.

---

# PART 1 — LANDING PAGE SCRIPT & CONTENT

## Page Structure Overview

```
┌─────────────────────────────────────────┐
│  NAVBAR                                 │
├─────────────────────────────────────────┤
│  HERO SECTION                           │
├─────────────────────────────────────────┤
│  SOCIAL PROOF BAR                       │
├─────────────────────────────────────────┤
│  PROBLEM → SOLUTION                     │
├─────────────────────────────────────────┤
│  HOW IT WORKS (3 Steps)                 │
├─────────────────────────────────────────┤
│  FEATURES GRID                          │
├─────────────────────────────────────────┤
│  LIVE DEMO / PRODUCT SHOWCASE           │
├─────────────────────────────────────────┤
│  PRICING                                │
├─────────────────────────────────────────┤
│  TESTIMONIALS                           │
├─────────────────────────────────────────┤
│  FAQ                                    │
├─────────────────────────────────────────┤
│  FINAL CTA                              │
├─────────────────────────────────────────┤
│  FOOTER                                 │
└─────────────────────────────────────────┘
```

---

## Section 1 — Navbar

**Design:** Sticky, glassmorphism on scroll (frosted glass + subtle blur). Dark background.

| Element | Content |
|---------|---------|
| Logo | **Tablekard** (stylized wordmark, golden accent `#d9b550`) |
| Nav Links | Features · How It Works · Pricing · FAQ |
| CTA Button | **Get Started Free →** (golden gradient button) |

**Mobile:** Hamburger menu that slides in from right with a dark overlay.

---

## Section 2 — Hero

**Layout:** Split — left text, right floating product mockup (phone showing QR menu)

**Design:** Deep dark gradient background (`#0a0a0a → #1a1a2e`) with subtle grid pattern overlay and floating golden particle accents.

### Copy

**Badge/Chip:**
> 🚀 Trusted by 200+ restaurants across India

**Headline (H1):**
> Your Restaurant, One Scan Away.

**Sub-headline:**
> Turn every table into a self-service ordering station. Tablekard gives your guests a seamless QR-powered menu, instant ordering, and contactless payments — no app downloads, no hardware, no hassle.

**Primary CTA:**
> **Start Your Free Trial** (large golden button with shimmer animation)

**Secondary CTA:**
> **Watch Demo** (ghost button with play icon, opens a modal video)

**Below CTAs — trust note:**
> ✓ No credit card required &nbsp;&nbsp; ✓ Setup in under 10 minutes &nbsp;&nbsp; ✓ Cancel anytime

**Right Side:** 
A phone mockup showing the customer QR ordering interface with a floating QR code card and animated order notifications popping in.

---

## Section 3 — Social Proof Bar

**Design:** Horizontal scrolling ticker / static row on dark card background with soft border.

**Content:**
> "50,000+ orders processed" · "200+ restaurants onboarded" · "4.9★ average rating" · "₹2Cr+ revenue facilitated"

*If no real stats yet, use aspirational:*
> "Built for modern restaurants" · "Zero downtime guarantee" · "Sub-second order relay" · "Enterprise-grade security"

---

## Section 4 — Problem → Solution

**Design:** Two-column layout. Left = "Without Tablekard" (red/muted tones), Right = "With Tablekard" (green/golden tones). Animated transition on scroll.

### "Without Tablekard" Column
| Pain Point | Description |
|---|---|
| 📝 Paper Menus | Outdated, unhygienic, expensive to reprint |
| ⏳ Long Wait Times | Customers wait for a waiter to take orders |
| ❌ Order Errors | Verbal orders → kitchen mix-ups → angry customers |
| 💸 Expensive POS Systems | ₹50,000+ for hardware you don't need |
| 📊 No Insights | No idea which dishes sell, when peak hours are |

### "With Tablekard" Column
| Benefit | Description |
|---|---|
| 📱 Digital QR Menu | Update prices and items instantly from anywhere |
| ⚡ Instant Ordering | Guests order the moment they sit down |
| ✅ Zero Errors | Digital orders go straight to your dashboard |
| 🎯 Affordable SaaS | Start from ₹999/month — no hardware needed |
| 📈 Real-Time Analytics | Know your bestsellers, peak hours, and revenue in real-time |

---

## Section 5 — How It Works

**Design:** Horizontal stepper with animated connector lines. Each step has an icon, title, and description. Steps light up sequentially on scroll.

**Section Header:**
> **How It Works**
> Get your restaurant running on Tablekard in three simple steps.

### Step 1 — Sign Up & Setup
> **Icon:** 🏪 (or restaurant icon)
> 
> **Title:** Create Your Restaurant
> 
> **Description:** Sign up in 60 seconds. Add your restaurant name, upload your logo, and set your operating hours. Our guided setup wizard walks you through everything.

### Step 2 — Build Your Menu
> **Icon:** 📋 (or menu icon)
> 
> **Title:** Add Your Menu
> 
> **Description:** Add categories, menu items, prices, and photos. Mark items as veg/non-veg, set availability, and organize with drag-and-drop. Changes go live instantly.

### Step 3 — Print & Go Live
> **Icon:** 📲 (or QR code icon)
> 
> **Title:** Generate Table QR Codes
> 
> **Description:** Generate a unique QR code for each table. Print them, stick them on tables, and your customers can start ordering immediately. That's it — you're live!

**Below steps — small CTA:**
> **Ready to go?** [Start Free Trial →]

---

## Section 6 — Features Grid

**Design:** Bento grid layout (asymmetric cards of varying sizes). Dark cards with golden accent borders on hover. Subtle glow effects.

**Section Header:**
> **Everything Your Restaurant Needs**
> One platform. Zero complexity.

### Feature Cards

| Feature | Title | Description | Card Size |
|---|---|---|---|
| 🖥️ | **Real-Time Order Dashboard** | See every order the instant it's placed. Accept, prepare, and mark ready — all from one screen. No page refresh needed. | Large (2×1) |
| 📱 | **Mobile-First QR Menu** | Beautiful, responsive digital menus that work on any smartphone. Dark/light themes, smooth animations, instant load. | Medium |
| 🔔 | **Instant Notifications** | Audio alerts + visual notifications the moment a new order arrives. Never miss a single order during rush hour. | Medium |
| 🍽️ | **Table Management** | Assign QR codes to tables, track which tables are active, and manage seating capacity — all digitally. | Medium |
| 📊 | **Analytics & Reports** | Daily revenue, popular items, peak hours, order trends — actionable insights to grow your revenue. | Medium |
| 👨‍🍳 | **Staff Management** | Add chefs, waiters, and managers. Assign roles and permissions. Everyone sees only what they need to see. | Small |
| 🎨 | **Custom Branding** | Upload your logo, set your brand colors, and make the QR menu look like your own app. | Small |
| 💳 | **Razorpay Payments** | Accept UPI, cards, and net banking directly. Or let customers pay at the counter — their choice. | Small |
| 🔒 | **Multi-Tenant Security** | Every restaurant's data is completely isolated. Bank-grade Row Level Security on every database query. | Small |
| 🌐 | **No App Downloads** | Your customers just scan and order. Works on Chrome, Safari, Firefox — any browser, any phone. | Small |

---

## Section 7 — Live Product Showcase

**Design:** Full-width dark section with a browser/phone mockup carousel. Tabs to switch between views.

**Section Header:**
> **See It In Action**
> A beautiful experience for your customers and a powerful dashboard for you.

### Tab 1: Customer QR Experience
Show a phone mockup with screens:
1. QR Scan → Menu loads
2. Browse categories & items
3. Add to cart with customizations
4. Checkout & pay

### Tab 2: Restaurant Admin Dashboard
Show a browser mockup with:
1. Live order dashboard with real-time cards
2. Menu management interface
3. Analytics graphs

### Tab 3: Table QR Management
Show the admin generating and downloading QR codes for individual tables.

---

## Section 8 — Pricing

**Design:** Three pricing cards on a dark background. Middle card (recommended) is elevated with a golden glow border and "Most Popular" badge.

**Section Header:**
> **Simple, Transparent Pricing**
> No hidden fees. No per-order commissions. Just flat monthly plans.

### Plan 1: Starter — ₹999/mo
> **Best for:** Small cafés and single-outlet restaurants
> 
> - Up to 50 menu items
> - Up to 10 tables
> - QR ordering
> - Basic analytics
> - Email support
> - 1 admin account
> 
> **CTA:** Start Free Trial

### Plan 2: Pro — ₹2,499/mo ⭐ Most Popular
> **Best for:** Growing restaurants and multi-staff operations
> 
> - Unlimited menu items
> - Unlimited tables
> - QR ordering + online payments
> - Advanced analytics & reports
> - Priority support
> - 5 staff accounts
> - Custom branding
> - Real-time notifications
> 
> **CTA:** Start Free Trial

### Plan 3: Enterprise — Custom Pricing
> **Best for:** Restaurant chains and franchises
> 
> - Everything in Pro
> - Multi-outlet support
> - Dedicated account manager
> - Custom integrations
> - SLA guarantee
> - Unlimited staff accounts
> - API access
> - White-label option
> 
> **CTA:** Contact Sales

**Below pricing:**
> All plans include a **14-day free trial**. No credit card required.

> [!IMPORTANT]
> These are placeholder prices. Confirm final pricing before launch.

---

## Section 9 — Testimonials

**Design:** Horizontal carousel of testimonial cards with profile photos, name, restaurant name, and star rating. Soft golden quote marks.

**Section Header:**
> **Loved by Restaurant Owners**

### Testimonial 1
> "We cut our order-taking errors to zero overnight. Customers love scanning and ordering on their own — and our waiters now focus on hospitality, not scribbling orders."
> 
> — **Priya Sharma**, Owner, The Spice Route, Mumbai ⭐⭐⭐⭐⭐

### Testimonial 2
> "Setting up took less than 15 minutes. We went from paper menus to a fully digital ordering system the same day. The dashboard is incredibly easy to use."
> 
> — **Rahul Menon**, Manager, Café Mocha, Bangalore ⭐⭐⭐⭐⭐

### Testimonial 3
> "The analytics alone are worth the subscription. I finally know which dishes are my real bestsellers and when my restaurant is busiest. Game changer."
> 
> — **Amit Patel**, Owner, Saffron Kitchen, Pune ⭐⭐⭐⭐⭐

### Testimonial 4
> "We run a 40-table restaurant and during peak hours it was chaos. Now every order flows digitally to the kitchen. Our average service time dropped by 35%."
> 
> — **Deepika Nair**, Partner, The Coastal Table, Kochi ⭐⭐⭐⭐⭐

> [!NOTE]
> Replace these with real testimonials once available. If launching without real testimonials, consider showing the Problem/Solution section more prominently instead.

---

## Section 10 — FAQ

**Design:** Accordion-style FAQ cards. Smooth expand/collapse animation. Golden accent on active question.

**Section Header:**
> **Frequently Asked Questions**

| Question | Answer |
|---|---|
| **Do my customers need to download an app?** | No! That's the beauty of Tablekard. Customers simply scan the QR code on their table and the menu opens instantly in their phone's browser. Works on any smartphone — no downloads, no sign-ups required for browsing. |
| **What if I want to change my menu?** | You can update your menu anytime from the admin dashboard. Add items, change prices, mark items as unavailable, upload new photos — changes go live within seconds. No reprinting required. |
| **How do payments work?** | Tablekard integrates with Razorpay for secure online payments (UPI, cards, net banking). You can also let customers choose to pay at the counter. You receive payments directly to your bank account. |
| **Is my restaurant's data secure?** | Absolutely. We use Supabase with PostgreSQL and Row Level Security (RLS). This means every restaurant's data is completely isolated — no other restaurant can ever see your menu, orders, or customer data. |
| **Can I use Tablekard for multiple outlets?** | Yes! Our Enterprise plan supports multi-outlet management. You can manage all your locations from a single super-admin dashboard with separate analytics for each outlet. |
| **What happens after the free trial?** | After 14 days, you choose a plan that fits your restaurant. If you decide not to continue, your account is simply paused — no data is deleted for 30 days, so you can come back anytime. |
| **Do I need special hardware?** | No. All you need is a printer to print QR code stickers (any regular printer works) and a laptop/tablet/phone to manage your dashboard. That's it. |
| **Can I customize the look of my QR menu?** | Yes. You can upload your logo, set your brand's primary color, and the customer-facing menu will reflect your restaurant's identity. |

---

## Section 11 — Final CTA

**Design:** Full-width gradient section (dark purple to deep blue) with floating particle effects. Centered text.

### Copy

**Headline:**
> **Ready to Transform Your Restaurant?**

**Sub-headline:**
> Join hundreds of restaurants already using Tablekard to deliver faster service, eliminate errors, and delight their customers.

**CTA Button:**
> **Start Your Free 14-Day Trial →** (large golden button with glow)

**Below:**
> No credit card required · Setup in 10 minutes · Cancel anytime

---

## Section 12 — Footer

**Design:** Dark footer with four columns and a bottom bar.

### Column 1: Brand
- **Tablekard** logo
- "Smart QR ordering for modern restaurants."
- Social icons: Twitter/X · LinkedIn · Instagram · YouTube

### Column 2: Product
- Features
- Pricing
- How It Works
- Demo

### Column 3: Company
- About Us
- Blog (Coming Soon)
- Careers
- Contact

### Column 4: Support
- Help Center
- Documentation
- Status Page
- Privacy Policy
- Terms of Service

### Bottom Bar
> © 2026 Tablekard by growtez. All rights reserved.

---

---

# PART 2 — ONBOARDING FLOW SCRIPT & CONTENT

## Overview

After a restaurant owner clicks "Start Free Trial" on the landing page, they enter a **multi-step onboarding wizard**. The goal: get them from sign-up to live QR ordering in under 10 minutes.

## Onboarding Flow Structure

```
Sign Up → Restaurant Profile → Menu Setup → Table Setup → Go Live! 🎉
  (1)          (2)                (3)           (4)          (5)
```

---

## Step 1 — Sign Up / Create Account

**Route:** `/onboarding/signup`

**Design:** Clean centered card on dark background. Social login buttons prominently displayed.

### Copy

**Headline:**
> **Let's get your restaurant online.**

**Sub-headline:**
> Create your Tablekard account in seconds.

### Form Fields
| Field | Type | Required | Placeholder |
|---|---|---|---|
| Full Name | Text | ✅ | "Your full name" |
| Email | Email | ✅ | "you@restaurant.com" |
| Phone Number | Tel | ✅ | "+91 98765 43210" |
| Password | Password | ✅ | "Create a strong password" |

**Or sign up with:**
- [Continue with Google] (button)

**Below form:**
> By signing up, you agree to our [Terms of Service] and [Privacy Policy].

**CTA:**
> **Create Account →**

---

## Step 2 — Restaurant Profile

**Route:** `/onboarding/profile`

**Design:** Two-column layout. Left = form, Right = live preview of how the restaurant profile will look on the customer app.

### Copy

**Headline:**
> **Tell us about your restaurant.**

**Sub-headline:**
> This information will appear on your digital menu.

### Form Fields
| Field | Type | Required | Placeholder/Options |
|---|---|---|---|
| Restaurant Name | Text | ✅ | "e.g., The Spice Route" |
| Restaurant Slug | Auto-generated | ✅ | "the-spice-route" (editable) |
| Description | Textarea | ❌ | "A brief description of your restaurant..." |
| Cuisine Type | Multi-select chips | ✅ | North Indian, South Indian, Chinese, Italian, Continental, Café, Fast Food, Other |
| Logo | Image upload | ❌ | Drag & drop or click to upload (max 2MB) |
| Banner Image | Image upload | ❌ | Recommended: 1200×400px |
| Address | Text | ✅ | "Full restaurant address" |
| City | Text | ✅ | "City" |
| Phone | Tel | ✅ | "Restaurant phone number" |
| Operating Hours | Time picker grid | ✅ | Mon–Sun, Open/Close times |

**Live Preview Panel (Right):**
A phone-frame showing how the customer will see the restaurant header: logo, name, description, cuisine tags.

**CTA:**
> **Save & Continue →**

**Skip option:**
> "I'll complete this later" (small text link, saves defaults)

---

## Step 3 — Menu Setup

**Route:** `/onboarding/menu`

**Design:** Interactive menu builder. Left panel = category list, Right panel = items in selected category. Floating "Add Item" button.

### Copy

**Headline:**
> **Build your digital menu.**

**Sub-headline:**
> Add your first category and a few items to get started. You can always add more later.

### Category Creation
**Prompt:** 
> "Start by creating your first menu category."

**Quick-add suggestions (clickable chips):**
> Starters · Main Course · Biryani · Drinks · Desserts · Soups · Breads · Combos

### Item Creation (Modal/Drawer)
| Field | Type | Required |
|---|---|---|
| Item Name | Text | ✅ |
| Description | Textarea | ❌ |
| Price (₹) | Number | ✅ |
| Category | Dropdown | ✅ |
| Veg / Non-Veg | Toggle | ✅ |
| Item Photo | Image upload | ❌ |
| Available | Toggle (default: ON) | ✅ |

**Tip banner:**
> 💡 **Pro tip:** Restaurants with photos on menu items see 30% more orders. Add photos now or upload them later from your dashboard.

**CTA:**
> **Save & Continue →** (requires at least 1 category and 1 item)

**Skip option:**
> "I'll add my menu later" → takes to next step with an empty menu

---

## Step 4 — Table Setup

**Route:** `/onboarding/tables`

**Design:** Visual grid showing table cards. Each card shows table number and a mini QR preview. "Add Table" button to add more.

### Copy

**Headline:**
> **Set up your tables.**

**Sub-headline:**
> Tell us how many dine-in tables you have. We'll generate a unique QR code for each one.

### Quick Setup
**Prompt:**
> "How many tables does your restaurant have?"

**Input:** Number input with +/- buttons (default: 5, max: 100)

**OR manual add:**
> [+ Add Table] button → opens a form:
> - Table Number/Name (e.g., "Table 1", "T-01", "Patio 3")
> - Seating Capacity (dropdown: 2, 4, 6, 8)

### Generated Table Cards
After entering the count, show a grid of table cards:
```
┌──────────┐  ┌──────────┐  ┌──────────┐
│ Table 1  │  │ Table 2  │  │ Table 3  │
│ [QR]     │  │ [QR]     │  │ [QR]     │
│ 4 seats  │  │ 4 seats  │  │ 2 seats  │
└──────────┘  └──────────┘  └──────────┘
```

**Buttons below grid:**
> [📥 Download All QR Codes] (ZIP file)
> [🖨️ Print QR Sheet] (formatted PDF with table numbers)

**CTA:**
> **Save & Continue →**

---

## Step 5 — Go Live! (Success/Completion)

**Route:** `/onboarding/complete`

**Design:** Celebratory screen with confetti animation, golden accent elements, and a summary card.

### Copy

**Headline:**
> 🎉 **You're All Set!**

**Sub-headline:**
> Your restaurant is now live on Tablekard. Customers can start ordering by scanning the QR codes on your tables.

### Summary Card
| Item | Value |
|---|---|
| Restaurant | The Spice Route |
| Menu Items | 12 items in 3 categories |
| Tables | 8 tables with QR codes |
| QR Menu Link | `tablekard.com/r/the-spice-route` |

### Quick Actions
| Action | Description |
|---|---|
| [📊 Go to Dashboard →] | Primary CTA — takes to Restaurant Admin |
| [📥 Download QR Codes] | Download all table QR codes |
| [👀 Preview Your Menu] | Opens the customer-facing QR menu |
| [👥 Invite Staff] | Add your first team member |

### Helpful Tips Section
> **What's next?**
> 1. **Print your QR codes** and place them on each table
> 2. **Add photos** to your menu items for better engagement
> 3. **Enable online payments** in Settings → Payments
> 4. **Invite your staff** so they can manage orders too

---

## Design System

### Color Palette
| Token | Value | Usage |
|---|---|---|
| `--bg-primary` | `#0a0a0a` | Page background |
| `--bg-secondary` | `#111111` | Card/section backgrounds |
| `--bg-elevated` | `#1a1a1a` | Elevated cards, modals |
| `--accent-gold` | `#d9b550` | Primary accent, CTAs, highlights |
| `--accent-gold-light` | `#e8cc73` | Hover states |
| `--accent-gold-glow` | `rgba(217, 181, 80, 0.15)` | Glow effects |
| `--text-primary` | `#ffffff` | Headings, body text |
| `--text-secondary` | `#a0a0a0` | Muted text, descriptions |
| `--text-tertiary` | `#666666` | Subtle labels |
| `--border` | `#222222` | Card borders |
| `--success` | `#22c55e` | Success states, "With Tablekard" |
| `--error` | `#ef4444` | Error states, "Without Tablekard" |
| `--gradient-hero` | `linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%)` | Hero background |

### Typography
| Element | Font | Size | Weight |
|---|---|---|---|
| H1 (Hero) | Outfit | 56px / 3.5rem | 700 |
| H2 (Section) | Outfit | 40px / 2.5rem | 600 |
| H3 (Card title) | Inter | 20px / 1.25rem | 600 |
| Body | Inter | 16px / 1rem | 400 |
| Small / Label | Inter | 14px / 0.875rem | 400 |
| CTA Button | Inter | 16px / 1rem | 600 |

### Animations
- **Scroll reveal:** Sections fade-in + slide-up on scroll (Intersection Observer)
- **Hero particles:** Subtle floating golden dots using CSS keyframes
- **CTA shimmer:** Golden shine sweep across button background
- **FAQ accordion:** Smooth height transition with rotate on chevron
- **Stepper:** Steps animate in sequence with connector line fill
- **Confetti:** Canvas confetti on onboarding completion

---

## Verification Plan

### Manual Verification
1. Run `npm run dev` in the landing app and verify all sections render correctly
2. Test responsive design at 320px, 768px, 1024px, and 1440px breakpoints
3. Test all navigation links and smooth scrolling
4. Test the onboarding flow end-to-end (all 5 steps)
5. Verify animations and transitions are smooth
6. Test dark mode consistency across all sections
7. Lighthouse audit for performance and SEO scores

---

## Open Questions

> [!IMPORTANT]
> **1. Where should the landing page be hosted?**
> Should it be a new app in the monorepo (`apps/landing`) or a standalone project? I'm proposing `apps/landing` to keep it in the monorepo.

> [!IMPORTANT]
> **2. Real data vs. placeholder data for testimonials/stats?**
> The script includes placeholder testimonials and stats. Should we use these as-is for now, or do you have real data to plug in?

> [!IMPORTANT]
> **3. Pricing confirmation?**
> The pricing tiers (₹999/₹2,499/Custom) are suggestions. Please confirm the final pricing before I build the pricing section.

> [!IMPORTANT]
> **4. Onboarding backend integration?**
> Should the onboarding flow actually write to your Supabase database (creating real restaurant records), or should it be a static/demo flow for now?

> [!IMPORTANT]
> **5. Should I build this now?**
> Once you approve the content and structure, I'll build the full landing page + onboarding as a working React app with all the animations, responsive design, and content described above. Confirm and I'll start coding.
