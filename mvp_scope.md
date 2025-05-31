## **MVP Feature Set – Core vs. Postponed**

The **Minimum Viable Product (MVP)** for Zedger should deliver the core value (fractional Kelly bankroll tracking) with no frills. Below is a breakdown of what features are **included in the MVP** and which are **cut or postponed** for later iterations. This ensures development stays focused on what truly matters in the first 8 weeks.

### **Core MVP Features (Essential for Launch)**

- **User Accounts & Basic Security:** A simple registration/login system so users can securely save their data. (Use email + password or OAuth if easy, but no need for multi-factor auth at MVP unless easily provided by framework.) Basic privacy: users’ bet data should only be accessible to them – this builds trust given the anonymous nature of the founder.

- **Manual Bet Entry:** A form for users to input bet details:

  - Sport/Event and Bet description (optional or free text for their reference).

  - Odds (allow entry in American, decimal, or fraction – or just one format MVP; decimal might simplify calculations internally).

  - Stake (the tool will suggest this, but user might input their own if they want to track non-Kelly bets too).

  - **User’s Win Probability (Edge):** a field for the user’s estimated probability of winning the bet. This is crucial for the Kelly calculation.

  - Result of the bet (win/lose/push) – for MVP, user can update this after the game manually.

- **Fractional Kelly Stake Calculator:** The algorithm to compute suggested stake as a fraction of current bankroll. Allow the user to set a global “Kelly fraction” (e.g., 25% Kelly, 50% Kelly) either in their profile or assume a default (like half-Kelly) for MVP simplicity. When a bet is entered, the app instantly shows how much to stake on it according to the Kelly criterion, given their current bankroll and input edge. This can be displayed before they confirm the bet entry, so they know how much to wager.

- **Bankroll Tracking & Adjustment:** Maintain a running bankroll value for the user. When they record a bet outcome, update the bankroll accordingly (win adds profit, loss subtracts stake). The app should store each bet’s data and outcome so users can see history.

- **Basic Performance Metrics:** On the dashboard, show a few key stats that matter to sharps:

  - Total Profit/Loss and ROI (return on investment) or growth of bankroll (%) since start.

  - Perhaps Win rate vs. expected win probability (to help users see if their estimations are over/underconfident).

  - Possibly a simple chart of bankroll over time (if time permits, a basic line chart). If charting is too time-consuming, skip it and just show numeric trends or a table of historical bets for now.

  - **Single bankroll-over-time sparkline** – a tiny chart from Chart.js/Recharts can be done in an hour and makes the dashboard feel alive.

- **Simple Onboarding & Help:** A minimal onboarding tutorial or help notes so users understand how to use Zedger. This could be as basic as a welcome message on first login (“Remember to input your true win probability for each bet – Zedger uses it to calculate optimal stakes using Kelly criterion.”). Also provide info on what fractional Kelly means (since even sharps might vary in their use of it). Keep it brief and maybe link to a blog or FAQ for those who want more theory.

- **Monetization Hooks:** MVP should include the ability to **convert users to paying customers** quickly:

  - If using a time-based free trial: have a system to track trial start date and restrict access or prompt upgrade after 14 days.

  - If using a free tier with limits: implement those limits (e.g., “Free tier: up to 20 bets logged” – the app counts bets per account and once the threshold is hit, it prompts upgrade for more).

  - **Payment Processing:** Integrate with Stripe or another service to handle subscription or one-time payments. For MVP, a simple monthly subscription plan (e.g., $20/month) can be offered. The UI needs a page for upgrading where users can enter card info securely (hosted checkout or at least a minimal form). Ensure this is working by launch – it’s okay if it’s not perfectly polished (e.g., manual refresh needed after payment), as long as it charges and upgrades the account status.

- **Analytics & Logging:** Invisible to the user, but include basic analytics so you can track usage (page views, sign-ups, etc., perhaps via Google Analytics) and logs for errors (so you can fix issues quickly). This is important for iterating after launch.

These core features are the **minimal set** that delivers the primary value proposition: letting a sports bettor track their bets and get staking guidance based on their edge, with results feeding back to adjust their strategy. Everything above should be achievable within the part-time 8-week build by leveraging simple implementations and existing tools (for example, using a UI library for forms, a chart library if charts are included, etc.).

### **Features to Cut or Postpone (Beyond MVP)**

- **Automatic Betslip Import/Integration:** While importing betslips from sportsbooks or email would be convenient, it’s technically complex (requires APIs or screen-scraping for numerous bookmakers). This is **postponed**. MVP will use manual entry or CSV import at best. Later, once core is stable and if users demand it, you might integrate with popular books or use services that provide betting history APIs.

- **Real-Time Odds or Scores Feed:** Some competitors show live scores or real-time bet grading. Zedger MVP will not include live score tracking or automatic grading of bets. Users will manually mark bets as win/lose. Real-time features can be data-intensive and costly (need API subscriptions), so defer these. Focus on the analytics rather than being a live score app.

- **Advanced Analytics & Charts:** Defer any complex analytics beyond the basics. For instance, things like **closing line value (CLV) tracking**, odds shopping comparisons, or detailed breakdowns by sport/league can be added later. Sharps might love these, but each requires more data input and UI. Keep MVP stats lean. If a chart of bankroll over time is too time-consuming, postpone it (a table of history can suffice initially). More sophisticated graphs, distribution of bet sizes, or simulations of bankroll growth can all wait.

- **Social or Community Features:** Though connecting with other bettors or sharing picks might be engaging, that’s out of scope. No need for friend lists, leaderboards, or public profiles in MVP – it complicates development (and raises potential anonymity/privacy issues). Zedger will start as a single-user private tool. Social sharing of results (like “share my ROI on Twitter”) can be considered later as a marketing growth feature, but not for initial build.

- **Mobile App (Native):** The focus is a web app. A native iOS/Android app is not feasible in 8 weeks part-time. Ensure the web app is mobile-friendly via responsive design, but postpone any native app development or publishing to app stores. If substantial demand is proven, you could build a native wrapper or a true app later or use something like React Native post-MVP.

- **Multi-Currency or Crypto Support:** If targeting international bettors or those using crypto for betting, currency handling can be complex. MVP can assume a default currency (e.g., USD) for simplicity. Users can mentally adapt if needed. Adding multi-currency tracking or crypto wallets integration can come later if a lot of users request it.

- **AI or Edge Calculation for Users:** An idea could be to help users estimate win probability (edge) by pulling odds and calculating implied probabilities or providing suggestions. This is **beyond MVP**. Initially, assume the user provides their edge. Any fancy machine learning or odds feed to auto-calc edge would be a phase 2 feature at best.

- **Polished Branding and Design:** While a professional look is important, spending time on custom design or an expensive logo is not priority. Use a simple logo (even just a styled text) and a basic clean UI theme. Fancy design elements, animations, or UX perfection can be improved later. The MVP just needs to be clean and functional. Users will forgive plain visuals if the utility is high, especially early adopters.

- **Scalability/Infrastructure Overkill:** Avoid over-engineering the backend for massive scale in MVP. With a handful to a few hundred users expected initially, a simple setup on a modest server or cloud function is fine. Don’t invest time now in complex microservices or load balancers – those are “nice problems” to tackle once you have the user load and revenue to justify them.

By cutting the above, you **maximize focus on delivering value quickly**. This disciplined scope will help avoid delays because “features keep changing” – a common startup pitfall[linkedin.com](https://www.linkedin.com/posts/muhammad-usman-khaan_an-mvp-only-takes-8-weeks-to-build-but-activity-7290200810490138624-Uc13#:~:text=roadmap%3A%20,wireframes%2C%20user%20flows%20%E2%86%92%20Plan). Post-launch, you can reassess these ideas based on user feedback and revenue, adding the most demanded ones that will drive growth or justify higher pricing.
