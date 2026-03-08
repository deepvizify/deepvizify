DeepVizify Admin
Overview
Bug Fix
Pipeline
Features
Priority
Admin Panel Complete Workflow Pipeline
ADMIN
PANEL
DEEPVIZIFY · FULL WORKFLOW
Ye document Claude Opus 4.6 ke liye banaya gaya hai — Admin Panel ka har feature, har connection, har missing piece clearly explain kiya gaya hai taake AI exactly samjhe aur implement kare. Frontend ko Admin se control karne ka complete system yahan hai.

React + Vite Frontend
Node.js Backend
Admin: localhost:8080
App: localhost:5173
Supabase DB
Anthropic API
🔴
CRITICAL BUG — Frontend Crash: "Something went wrong" (Screenshot 1)
localhost:8080/dashboard par "Something went wrong — Please reload the page" error aa raha hai. Ye React Error Boundary trigger ho raha hai — matlab koi unhandled JavaScript error hai frontend mein. Admin panel (localhost:8080/admin) kaam kar raha hai lekin main user dashboard crash ho raha hai.

Root Cause (likely): Global state store missing hai — koi component undefined data access karne ki koshish kar raha hai. Ya router configuration galat hai. Ya backend API calls fail ho rahi hain aur error handling nahi hai.

Pehle ye fix karo Claude se: App ke root component mein proper Error Boundary + fallback UI add karo. Console errors dekhne ke liye browser DevTools (F12) → Console tab kholo aur exact error message Claude ko batao.

01
System Architecture — Poora System Kaise Connect Hoga
3-Layer System
🖥️ Frontend (User App)
React + Vite — localhost:5173
Dashboard, Charts, Cleaning
Analytics, Reports, SQL Lab
Zustand Global State Store
Auth Guard (missing)
API Client / Axios (missing)
⟷
⚙️ Backend API
Node.js + Express — port 8080
Admin Panel — /admin routes
REST API — /api/v1/* routes
JWT Authentication (missing)
File Upload Handler (missing)
WebSocket (real-time, missing)
⟷
🗄️ Database + Services
Supabase (PostgreSQL)
Supabase Auth
Supabase Storage (files)
Anthropic Claude API
Stripe (billing, missing)
Google APIs (GA4, GSC)
02
Admin Panel — Har Section Ka Status
15 Screens Analyzed
🏠 Admin Dashboard
UI OK · Data Fake
Admin dashboard exist karta hai (screenshot 2). Stats dikhte hain lekin sab 0 hain — Total Users: 0, Active Subscriptions: 0, Monthly Revenue: $0, Total Datasets: 0. System Health bars dikh rahi hain.
Stats = 0 — DB se real data connect nahi
System Health — CPU 42%, Memory 68% (real ya fake?)
Recent Activity — "No recent activity logged"
Online Users / Active Chats / API Req — all "—"
Quick Actions buttons — UI only, kaam nahi karte
👥 Users Management
Empty · No Users
User Management page exist karta hai (screenshot 3). "0 total users" dikh raha hai — koi user nahi kyunki Auth implement nahi hua. Table columns hain: User, Role, Plan, Status, Signup Date, Last Login, Actions.
No authentication = no users in DB
Search, Plan filter, Status filter — UI only
Create User button — kaam nahi karta
Role assignment (Admin/User) — not implemented
Ban/Suspend user action — not implemented
📝 Content (CMS)
UI Good · Save Broken
CMS section kafi complete dikhta hai (screenshots 4, 5). Pages (6), Blog (4), Documentation (4) tabs hain. Page Editor bhi hai with title, URL slug, meta fields, WYSIWYG editor, Publish/Draft/Preview buttons.
Pages list exist karta hai (Homepage, About, Pricing...)
Page editor UI complete hai
Publish button — DB mein save nahi hota
WYSIWYG editor — placeholder text only
Frontend se CMS content fetch nahi ho raha
Image upload — not working
💰 Billing & Subscriptions
Plans Exist · Stripe Missing
Billing page mein 3 plans hain (screenshot 6): Starter $0/month, Professional $49/month, Enterprise $149/month. MRR $0, ARR $0, Active Subs: 0. Plans ka "Edit" button bhi hai.
3 plans define hain with prices
Stripe integration missing — no real payments
Subscriptions tab — empty (no users)
MRR/ARR calculation — not real
Plan upgrade from frontend — not connected
📢 Ads Management
UI Detailed · AdSense Fake
Ads Management bahut detailed hai (screenshot 7). Publisher ID field, Auto Ads toggle, Revenue $409.20, Impressions 105.7K, Clicks 2,586, RPM $3.87. Ad Units table with Header Banner, Sidebar Rectangle shown.
UI complete aur detailed hai
All numbers hardcoded — not real AdSense data
AdSense API not connected
Publisher ID field — saves nowhere
Ad code not injected into frontend pages
🔍 SEO Tools
Good UI · Not Saving
SEO Management detailed hai (screenshots 8, 9). Meta Tags tab: Global defaults, Page-level meta tags table. JSON-LD structured data editor. Sitemap & Robots tab, Redirects tab.
Meta title/description for each page shown
Char count indicator (46/60) working
"Save Defaults" — saves nowhere
JSON-LD not actually injected in frontend
Sitemap auto-generation — not implemented
📊 Google Search Console
UI Good · Data Hardcoded
Search Console page impressive hai (screenshots 10, 11). Total Clicks 12,450, Impressions 345K, Avg CTR 3.6%, Avg Position 8.2. Top Queries table. Index Coverage. Core Web Vitals. INP "Needs Improvement".
UI extremely detailed aur realistic
All data hardcoded — GSC API not connected
"Sync Data" button — doesn't do anything
Core Web Vitals — static values, not real measurements
📈 Google Analytics
Detailed UI · Fake Data
Analytics page very detailed (screenshots 12, 13). Active Users 142, Page Views 1,240, Events 3,450, Conversions 28. Traffic Sources breakdown. Top Pages. Devices. Top Countries.
G-XXXXXXXXXX placeholder — needs real Measurement ID
GA4 API not connected — all fake data
"Connected" badge misleading — not actually connected
Real-time users — static number
🌐 Multi-Language (i18n)
Detailed · Save Missing
Languages page bahut detailed hai (screenshots 14, 15). English 100%, Spanish 95%, French 90%, German 85%, Arabic 79%, Chinese 50%. Translation Keys table with Missing/Partial status. RTL Support toggle.
Language list with progress bars — nice UI
Translation keys table with status
"Auto-translate" — not implemented
Frontend language switching — not working
RTL (Arabic) — not actually applied
Import/Export JSON — not working
03
Implementation Pipeline — Step by Step Kya Banana Hai
Claude Opus 4.6 ke liye
1
🔴 Frontend Crash Fix — PEHLE YE KARO
BLOCKING
~2 hours
Problem: localhost:8080/dashboard "Something went wrong" — Error Boundary trigger ho raha hai.

Fix 1 — Error Boundary check karo: App.jsx ya main.jsx mein ErrorBoundary component dhundo. Usmein console.error add karo taake exact error pata chale.

Fix 2 — Global State check karo: Zustand ya Context store mein initial state undefined nahi honi chahiye. Har property ka default value hona chahiye.

Fix 3 — Router check karo: /dashboard route properly define ho. Lazy loaded component ho toh Suspense fallback hona chahiye.

// App.jsx mein ye add karo — Error Boundary
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null }
  
  static getDerivedStateFromError(error) {
    return { hasError: true, error }
  }
  
  componentDidCatch(error, info) {
    console.error('Dashboard Error:', error, info) // Error dekhne ke liye
  }
  
  render() {
    if (this.state.hasError) {
      return <div>Error: {this.state.error?.message}</div>
    }
    return this.props.children
  }
}

// Zustand store mein safe defaults:
const useStore = create((set) => ({
  datasets: [],      // Never undefined
  currentDataset: null,
  columns: [],
  isLoading: false,
  error: null,
}))
Browser DevTools F12
React Error Boundary
Zustand defaults
React Suspense
2
🔑 Backend API Layer + Authentication
CRITICAL
~3-5 days
Bina backend ke koi bhi feature properly work nahi karega. Ek proper Express.js REST API banana zaroori hai jo Admin panel ke sare actions handle kare aur Frontend ko data serve kare.

Authentication Strategy: Supabase Auth use karo — instant auth with JWT tokens. Admin role check karo har admin route par. Frontend mein protected routes add karo.

// Backend file structure jo banana hai:
backend/
├── server.js          // Express app entry point
├── middleware/
│   ├── auth.js        // JWT verify middleware
│   ├── adminOnly.js   // Admin role check
│   └── upload.js      // Multer file upload
├── routes/
│   ├── admin/
│   │   ├── users.js   // GET/POST/DELETE users
│   │   ├── content.js // CMS CRUD
│   │   ├── billing.js // Plans management
│   │   ├── settings.js// Site settings
│   │   ├── seo.js     // Meta tags, sitemap
│   │   └── i18n.js    // Language keys
│   └── api/
│       ├── datasets.js // File upload + parse
│       ├── cleaning.js // Data cleaning
│       ├── insights.js // AI analytics
│       └── reports.js  // PDF generation
└── db/
    └── supabase.js     // Supabase client

// Admin middleware example:
const adminOnly = async (req, res, next) => {
  const { data: user } = await supabase.auth.getUser(token)
  if (user?.role !== 'admin') return res.status(403).json({ error: 'Unauthorized' })
  next()
}
Express.js
Supabase Auth
JWT Middleware
CORS config
Multer (file upload)
3
🗄️ Supabase Database Schema
CRITICAL
~1-2 days
Admin panel ka har section ek ya zyada database tables se data leta hai. Ye sare tables Supabase mein banana zaroori hai. Ye schema Claude ko de do exact SQL ke saath.

-- 1. User Profiles (Supabase auth se extend)
CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users,
  email TEXT, role TEXT DEFAULT 'user',
  plan TEXT DEFAULT 'starter', status TEXT DEFAULT 'active',
  datasets_count INT DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Datasets
CREATE TABLE datasets (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES profiles(id),
  name TEXT, file_url TEXT, file_type TEXT,
  row_count INT, column_count INT,
  columns_meta JSONB, status TEXT DEFAULT 'active',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. CMS Content
CREATE TABLE cms_pages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT UNIQUE, title TEXT, content TEXT,
  meta_title TEXT, meta_desc TEXT, featured_image TEXT,
  type TEXT DEFAULT 'page',  -- page | blog | doc
  status TEXT DEFAULT 'draft', author_id UUID,
  published_at TIMESTAMPTZ, updated_at TIMESTAMPTZ
);

-- 4. Site Settings (key-value store)
CREATE TABLE site_settings (
  key TEXT PRIMARY KEY, value JSONB,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. AI Insights
CREATE TABLE ai_insights (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  dataset_id UUID REFERENCES datasets(id),
  user_id UUID, insight_type TEXT,
  content JSONB, created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 6. Subscription Plans
CREATE TABLE plans (
  id TEXT PRIMARY KEY, name TEXT,
  price_monthly DECIMAL, price_yearly DECIMAL,
  features JSONB, is_active BOOLEAN DEFAULT true
);

-- 7. Activity Log
CREATE TABLE activity_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID, action TEXT, entity_type TEXT,
  entity_id TEXT, metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
Supabase SQL Editor
Row Level Security (RLS)
PostgreSQL
Supabase Storage
4
📡 Admin Panel → Backend API Connections
HIGH PRIORITY
~4-6 days
Admin panel ke har button, form, aur action ko backend API se connect karna hai. Abhi sab UI-only hai. Niche har admin section ke liye exact API endpoints define kiye gaye hain.

Admin Section	Action	API Endpoint	Method	Status
Dashboard	Stats load karo	/api/admin/stats	GET	Missing
Dashboard	Recent activity	/api/admin/activity	GET	Missing
Dashboard	System health	/api/admin/system-health	GET	Missing
Users	Users list karo	/api/admin/users	GET	Missing
Users	User create karo	/api/admin/users	POST	Missing
Users	User suspend/delete	/api/admin/users/:id	PATCH/DELETE	Missing
Users	Role change	/api/admin/users/:id/role	PATCH	Missing
CMS	Pages list	/api/admin/cms/pages	GET	Missing
CMS	Page save/publish	/api/admin/cms/pages/:id	PUT	Missing
CMS	New page create	/api/admin/cms/pages	POST	Missing
Billing	Plans list	/api/admin/billing/plans	GET	Missing
Billing	Plan edit	/api/admin/billing/plans/:id	PUT	Missing
SEO	Meta defaults save	/api/admin/seo/defaults	PUT	Missing
SEO	Page meta save	/api/admin/seo/pages/:slug	PUT	Missing
SEO	Sitemap generate	/api/admin/seo/sitemap	POST	Missing
Settings	Settings save	/api/admin/settings	PUT	Missing
Languages	Keys list	/api/admin/i18n/keys	GET	Missing
Languages	Key update	/api/admin/i18n/keys/:key	PUT	Missing
Languages	Auto-translate	/api/admin/i18n/auto-translate	POST	Missing
axios / fetch
React Query / SWR
Toast notifications
Loading states
5
🎛️ Admin → Frontend Control System
CORE GOAL
~3-4 days
Ye sabse important feature hai — Admin panel se Frontend ko control karna. Matlab Admin mein jo bhi change karo (CMS content, SEO, settings, plans, languages) wo automatically Frontend par reflect ho.

Pattern: Admin → Save to DB → Frontend fetches from DB on load → Changes live ho jayein.

Admin Controls → Frontend Effect
CMS page content edit → /about, /pricing pages update
SEO meta edit → <head> tags update
Billing plan prices change → Pricing page update
Language switch → App language change
Site settings → Logo, colors, footer update
Ads toggle → AdSense code inject/remove
User ban → User session expire (WebSocket)
Announcement → Toast notification to all users
// Frontend mein settings fetch karo:
const useSiteSettings = () => {
  return useQuery({
    queryKey: ['settings'],
    queryFn: () => fetch('/api/settings')
      .then(r => r.json()),
    staleTime: 5 * 60 * 1000
  })
}

// App.jsx mein use karo:
const { data: settings } = useSiteSettings()
const metaTitle = 
  settings?.meta_title || 'DeepVizify'

// CMS page content fetch:
const page = await supabase
  .from('cms_pages')
  .select('*')
  .eq('slug', 'about')
  .single()
React Query (caching)
Supabase Realtime
Dynamic <head> tags
i18n library (react-i18next)
6
💳 Stripe Billing Integration
HIGH
~3-4 days
Admin Billing tab mein 3 plans hain — Starter ($0), Professional ($49), Enterprise ($149). In plans ko actual Stripe se connect karna hai taake real payments ho sakein.

Flow: User "Upgrade to Pro" click kare → Stripe Checkout open ho → Payment complete → Supabase mein plan update → Admin mein subscription dikh jaye.

// Backend: Stripe checkout session create karo
app.post('/api/billing/checkout', auth, async (req, res) => {
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    mode: 'subscription',
    customer_email: req.user.email,
    line_items: [{
      price: 'price_XXXXXXXX', // Stripe Price ID
      quantity: 1
    }],
    success_url: `${FRONTEND_URL}/dashboard?upgraded=true`,
    cancel_url: `${FRONTEND_URL}/pricing`,
    metadata: { user_id: req.user.id }
  })
  res.json({ url: session.url })
})

// Webhook: Payment success par Supabase update karo
app.post('/api/billing/webhook', async (req, res) => {
  const event = stripe.webhooks.constructEvent(req.body, sig, secret)
  if (event.type === 'checkout.session.completed') {
    await supabase.from('profiles')
      .update({ plan: 'professional' })
      .eq('id', event.data.object.metadata.user_id)
  }
})
Stripe SDK
Stripe Checkout
Webhook Handler
Plan Gates (Pro features)
7
🤖 AI Integration + Real Analytics
PRO FEATURE
~4-5 days
Admin Analytics tab mein Google Analytics + Search Console data hardcoded hai. Real data ke liye Google APIs connect karne honge. Saath hi Frontend ka AI Chart Bot Anthropic API se connect hoga.

Auto-translate feature Languages tab mein: Claude API se missing translations automatically generate karo.

// Claude API — AI Insights generate karo
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY })

app.post('/api/insights/generate', auth, async (req, res) => {
  const { datasetSummary } = req.body
  
  const message = await anthropic.messages.create({
    model: 'claude-opus-4-6',    // Anthropic ka latest model
    max_tokens: 1024,
    messages: [{
      role: 'user',
      content: `Analyze this dataset summary and provide:
1. Key insights (2-3 bullet points)
2. Anomalies detected
3. Actionable recommendations
4. Growth trend direction

Dataset: ${JSON.stringify(datasetSummary)}`
    }]
  })
  
  res.json({ insights: message.content[0].text })
})

// Auto-translate ke liye:
const translated = await anthropic.messages.create({
  model: 'claude-opus-4-6',
  messages: [{ role: 'user', content: 
    `Translate "${text}" to ${language}. Return ONLY translation.`
  }]
})
Anthropic SDK (claude-opus-4-6)
Google Analytics Data API
Google Search Console API
Service Account Auth
8
🌐 i18n + RTL + Multi-Language
MEDIUM
~2-3 days
Admin Languages tab mein 6 languages hain (English, Spanish, French, German, Arabic, Chinese). Frontend mein actual language switching implement karna hai. Arabic ke liye RTL support bhi zaroori hai.

// react-i18next setup karo:
import i18n from 'i18next'
import { initReactI18next } from 'react-i18next'

// Translations DB se load karo (not static files):
const loadTranslations = async (lang) => {
  const { data } = await supabase
    .from('i18n_keys')
    .select(`key, ${lang}`)
  return data.reduce((obj, row) => {
    obj[row.key] = row[lang]; return obj
  }, {})
}

// RTL support (Arabic):
const setLanguage = (lang) => {
  i18n.changeLanguage(lang)
  document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr'
  document.documentElement.lang = lang
}

// Component mein use karo:
const { t } = useTranslation()
return <button>{t('auth.login')}</button>
react-i18next
RTL CSS (dir="rtl")
Browser language detect
Supabase i18n table
04
Admin Features — Full Table with Status
Complete Reference
Admin Section	Feature	Current Status	What to Do	Priority
Dashboard	Real-time stats (Users, Revenue, Datasets)	Hardcoded 0	DB query karo, stats return karo	🔴 P1
Dashboard	System Health (CPU, RAM)	Unknown	os module se real metrics ya uptime API	🟡 P2
Dashboard	Recent Activity log	Empty	activity_log table se last 10 events	🔴 P1
Dashboard	Quick Actions (Create User, Export CSV)	UI Only	Each button ko API call se connect karo	🟡 P2
Users	Users list with search/filter	No users	Auth implement karo, profiles table se fetch	🔴 P1
Users	Create / Edit / Ban user	UI Only	CRUD APIs + Supabase admin methods	🔴 P1
Users	Plan change from admin	Not built	PATCH /api/admin/users/:id plan field	🟡 P2
CMS	Save / Publish pages	Doesn't save	PUT API + Supabase cms_pages upsert	🔴 P1
CMS	WYSIWYG editor (real)	Placeholder	TipTap ya Quill editor integrate karo	🔴 P1
CMS	Image upload	Not working	Supabase Storage + presigned URL	🟡 P2
CMS	Frontend content fetch	Not connected	Frontend /about etc. pages API se content le	🔴 P1
Billing	Real payment processing	No Stripe	Stripe Checkout + Webhook implement karo	🔴 P1
Billing	Plan edit from admin	UI Only	plans table mein price update karo	🟡 P2
Billing	Subscription list	Empty	Stripe subscriptions fetch karo	🟡 P2
Ads	Real AdSense data	Hardcoded	AdSense API ya data manual enter + store	🔵 P3
Ads	Publisher ID save + inject	Not saved	site_settings mein save, frontend <head> mein inject	🟡 P2
SEO	Meta defaults save	Not saved	site_settings mein save karo	🔴 P1
SEO	Frontend <head> update	Not connected	react-helmet-async se dynamic <head>	🔴 P1
SEO	Sitemap generation	Not built	sitemap.xml auto-generate + serve karo	🟡 P2
Search Console	Real GSC data	Hardcoded	Google Search Console API v3 connect karo	🔵 P3
Analytics	Real GA4 data	Hardcoded	GA4 Data API + service account auth	🔵 P3
Languages	Frontend language switch	Not working	react-i18next + translations DB se	🔴 P1
Languages	Auto-translate (Claude API)	Not built	Claude API se missing keys translate karo	🟡 P2
Languages	RTL support (Arabic)	Not applied	dir="rtl" toggle on language change	🟡 P2
Email System	Email send karo	Not visible	Resend ya SendGrid API integrate karo	🟡 P2
Security & Logs	Audit logs	Not visible	activity_log table se read karo	🟡 P2
API Management	API key generate/revoke	Not visible	api_keys table + key generation	🔵 P3
05
Priority Roadmap — Claude Opus 4.6 Ko Ye Order Batao
Sequence Matters
1
🔴 Frontend Crash Fix — Error Boundary + Safe Defaults
Pehle dashboard working karo. Browser F12 → Console mein exact error dekho, Claude ko batao. Zustand store mein har property ka default value set karo. Bina is ke kuch test nahi ho sakta.
2
🗄️ Supabase DB Setup — Tables Create Karo
Upar diya gaya SQL Supabase SQL Editor mein run karo. 7 tables: profiles, datasets, cms_pages, site_settings, ai_insights, plans, activity_log. Row Level Security bhi lagao.
3
🔑 Supabase Auth + User Registration
Login/Signup page banao. Supabase Auth use karo. Pehle user register karo, uski profile mein role='admin' set karo. Frontend mein ProtectedRoute component add karo.
4
⚙️ Express Backend + Admin API Routes
backend/ folder mein server.js banao. Admin routes add karo: /api/admin/stats, users, cms, settings. JWT middleware lagao. Frontend ke saath CORS configure karo.
5
📡 Admin Dashboard Stats — Real Data Connect
Admin dashboard mein Total Users, Total Datasets, Monthly Revenue, Activity Log — sab DB se real data aaye. Counting queries + response format define karo.
6
📝 CMS Save/Publish + Frontend Fetch
CMS pages admin se save hon. TipTap editor add karo. Frontend /about, /pricing etc. pages DB se content le kar render karein. Ye Admin → Frontend control ka core hai.
7
🔍 SEO Meta Tags → Frontend <head>
Admin SEO settings save karein. react-helmet-async install karo. Frontend mein har page par dynamic meta title/description/og tags inject hon. Sitemap.xml auto-generate karo.
8
📥 File Upload + Data Processing (Frontend Core)
CSV/Excel upload API banao (Multer). File ko parse karo (PapaParse backend mein ya frontend mein). Dataset Supabase Storage mein store karo. Metadata DB mein save karo.
9
🤖 Anthropic API — AI Insights + Auto-translate
claude-opus-4-6 model se dataset analysis karo. Frontend Analytics tab mein real AI insights show karo. Admin Languages tab mein Auto-translate button Claude se missing keys fill kare.
10
💳 Stripe Billing + Plan Gates
Stripe Checkout implement karo. Webhook se plan update karo. Frontend mein plan-based feature gates lagao — Pro features Pro users ko hi milein.
11
🌐 i18n Frontend + RTL + Language Switch
react-i18next setup karo. Translations DB se dynamic load karo. Language selector add karo header mein. Arabic ke liye dir="rtl" toggle karo automatically.
12
📊 Google APIs + Real Analytics (Optional)
GA4 Data API + Google Search Console API service account se connect karo. Real data admin mein show karo. Optional — sirf tab zaroori hai jab real traffic ho.
06
Claude Opus 4.6 Ko Exactly Ye Prompt Do
Effective Prompting
💡
Best Prompt Strategy for Claude Opus 4.6
Step by Step ek kaam karo:

1. Meri DeepVizify app mein frontend crash ho raha hai localhost:8080/dashboard par — "Something went wrong" error aa raha hai. Pehle Error Boundary check karo aur console mein exact error dhundo. Mere App.jsx ka code ye hai: [paste code]

2. Ab mujhe Supabase mein ye 7 tables banana hai: [upar wala SQL]. Supabase SQL editor mein run karne ke liye complete SQL do.

3. Ab Express backend banao — /api/admin/stats endpoint jo Supabase se real users count, datasets count, revenue return kare. Mera supabase.js file ye hai: [paste]

4. Admin CMS mein Publish button click hone par ye data save hona chahiye Supabase mein. Frontend ke /about page par ye content fetch ho. Mera current CMS component ka code ye hai: