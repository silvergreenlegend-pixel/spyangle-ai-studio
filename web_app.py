import streamlit as st
from groq import Groq
import hashlib

# =========================================================================
# APPLICATION INITIALIZATION & THEME CONFIGURATION
# Configures a wide-screen immersive layout with custom workspace geometry.
# =========================================================================
st.set_page_config(
    page_title="SpyAngle AI Studio",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize production environment configuration keys safely from cloud secrets
try:
    api_key = st.secrets["GROQ_API_KEY"]
except KeyError:
    st.error("❌ OPERATIONAL HALT: Secure Environment Key Missing. Please register 'GROQ_API_KEY' inside your environment config secrets file.")
    st.stop()

# =========================================================================
# LIVE PRODUCTION STRIPE PAYWALL CONFIGURATION
# Define your live payment link URL and your secure system license passkeys.
# =========================================================================
# Your live verified Stripe checkout link node
STRIPE_PAYMENT_URL = "https://buy.stripe.com/test_4gMfZi3v66jv7VcgbDeEo00"

# Production Cryptographic Database Mapping:
# Instead of storing raw user passwords, you store the SHA-256 hash of your paying clients' email addresses.
# FIXED: We use Python to dynamically compute the hashes at runtime to guarantee an exact match.
VALID_SUBSCRIBER_HASHES = [
    hashlib.sha256("test@domain.com".encode()).hexdigest(),   # Dynamically hashes "test@domain.com"
    hashlib.sha256("admin@domain.com".encode()).hexdigest()   # Dynamically hashes "admin@domain.com"
]

# Initialize clean native session state parameters persistently
if "is_authenticated_user" not in st.session_state:
    st.session_state.is_authenticated_user = False
if "verified_email" not in st.session_state:
    st.session_state.verified_email = ""

# Custom high-end dark styling injects to construct custom gradient nodes and glassmorphism cards
st.markdown("""
    <style>
        /* Base application canvas refinement */
        .main { background-color: #0f172a; }
        
        /* Metric dashboard card layouts */
        .metric-card {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid #334155;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
            margin-bottom: 16px;
        }
        
        /* High-contrast headings */
        h1, h2, h3 {
            font-family: 'Inter', sans-serif !important;
            font-weight: 700 !important;
            color: #ffffff !important;
        }
        
        /* Action buttons with high-end digital agency gradients */
        .stButton>button {
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%) !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 12px 28px !important;
            font-weight: 600 !important;
            border: none !important;
            width: 100% !important;
            box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.3) !important;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        .stButton>button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 20px 0 rgba(168, 85, 247, 0.4) !important;
            opacity: 0.95 !important;
        }
        
        /* Input window structural accents */
        .stTextArea textarea {
            background-color: #020617 !important;
            border: 1px solid #1e293b !important;
            color: #e2e8f0 !important;
            border-radius: 12px !important;
        }
        .stTextArea textarea:focus {
            border-color: #6366f1 !important;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# APPLICATION SIDEBAR CONTROL CENTER
# Manages user session state status indicators and displays account tags.
# =========================================================================
with st.sidebar:
    st.markdown("### 🔐 Client Access Console")
    
    if not st.session_state.is_authenticated_user:
        user_email_input = st.text_input(
            "Enter Registered Account Email:",
            placeholder="user@example.com"
        )
        click_verify = st.button("Verify Account Access")
        
        if click_verify:
            if user_email_input:
                clean_email = user_email_input.replace(" ", "").replace("\n", "").replace("\r", "").strip().lower()
                input_hash = hashlib.sha256(clean_email.encode()).hexdigest()
                
                if input_hash in VALID_SUBSCRIBER_HASHES:
                    st.session_state.is_authenticated_user = True
                    st.session_state.verified_email = clean_email
                    st.success("Access Granted! Unlocking...")
                    st.rerun()
                else:
                    st.error("❌ NO ACTIVE SUBSCRIPTION FOUND")
            else:
                st.warning("🔒 ENTER EMAIL TO ACCESS ENGINE")
    else:
        st.success(f"Verified Active Pro Profile:\n\n{st.session_state.verified_email}")
        if st.button("Logout Profile"):
            st.session_state.is_authenticated_user = False
            st.session_state.verified_email = ""
            st.rerun()

    st.divider()
    st.markdown("### ⚙️ Engine Control Node")
    st.caption("Deployment Tier: Live Public Web App Cluster")
    
    if st.session_state.is_authenticated_user:
        st.metric(label="API Key Handshake", value="AUTHORIZED", delta="Active Session Node")
    else:
        st.metric(label="API Key Handshake", value="LOCKED", delta="Authentication Required", delta_color="inverse")
        
    st.metric(label="Core LLM Infrastructure", value="Qwen 3.6 27B", delta="Groq Pipeline")
    
    st.divider()
    st.markdown("### 💸 Automation Strategy")
    st.info("""
    **SaaS Administration Loop:**
    When a brand-new customer subscribes to your platform via Stripe, compute the SHA-256 hash of their email and drop it into the `VALID_SUBSCRIBER_HASHES` array within your repository file code structure to authorize them dynamically.
    """)

# =========================================================================
# WORKSPACE HEADER ZONE
# Distinctive modern banner introducing application context.
# =========================================================================
st.markdown("""
    <div style="background: linear-gradient(90deg, #1e1b4b 0%, #0f172a 100%); padding: 32px; border-radius: 20px; border: 1px solid #1e293b; margin-bottom: 32px;">
        <span style="background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%); padding: 4px 12px; border-radius: 20px; text-transform: uppercase; font-size: 11px; font-weight: 600; tracking-wide: 1px;">AI Copywriting Intelligence Node</span>
        <h1 style="margin-top: 12px; margin-bottom: 8px; font-size: 36px;">SpyAngle AI Enterprise Studio</h1>
        <p style="color: #94a3b8; margin: 0; font-size: 15px; max-width: 800px;">
            Deconstruct competitive market positions, extract subconscious customer psychological friction points, and output ready-to-launch high-performance direct-response social media ad blueprints.
        </p>
    </div>
""", unsafe_allow_html=True)

# =========================================================================
# VALUE PROP / TOOL USAGE BENEFITS ROW
# Interactive structured framework detailing explicit utility metrics.
# =========================================================================
st.markdown("## ⚡ Core Operational Leverage Metrics")
b1, b2, b3 = st.columns(3)

with b1:
    st.markdown("""
        <div class="metric-card">
            <h3 style="font-size: 16px; margin: 0 0 8px 0; color: #6366f1 !important;">⏱️ Velocity Arbitrage</h3>
            <p style="font-size: 24px; font-weight: 700; margin: 0; color: white;">Save 4+ Hours / Site</p>
            <p style="font-size: 12px; color: #64748b; margin: 8px 0 0 0; line-height: 1.4;">
                Eliminates the requirement for manual competitor deep-dives or messy review tracking sheets. Instantly processes complex landing pages into clean strategic text summaries in under 10 seconds.
            </p>
        </div>
    """, unsafe_allow_html=True)

with b2:
    st.markdown("""
        <div class="metric-card">
            <h3 style="font-size: 16px; margin: 0 0 8px 0; color: #a855f7 !important;">🧠 Subconscious Targeting</h3>
            <p style="font-size: 24px; font-weight: 700; margin: 0; color: white;">Psychological Mapping</p>
            <p style="font-size: 12px; color: #64748b; margin: 8px 0 0 0; line-height: 1.4;">
                Bypasses generic keyword search scraping. Isolates the core human driving forces behind transactions—uncovering specific user fears, lifestyle aspirations, and competitive friction points.
            </p>
        </div>
    """, unsafe_allow_html=True)

with b3:
    st.markdown("""
        <div class="metric-card">
            <h3 style="font-size: 16px; margin: 0 0 8px 0; color: #10b981 !important;">🚀 Ready-To-Launch Assets</h3>
            <p style="font-size: 24px; font-weight: 700; margin: 0; color: white;">3X Meta/TikTok Ad Scripts</p>
            <p style="font-size: 12px; color: #64748b; margin: 8px 0 0 0; line-height: 1.4;">
                Automatically drafts three hyper-tailored social ad variations. Each variations generates a unique hook variation, full ad caption body structure, and crisp visual direction frames for immediate production.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================================================================
# CORE WORKSPACE FUNCTIONAL ROUTING
# Evaluates authorization credentials before serving functional workspace interfaces.
# =========================================================================
if st.session_state.is_authenticated_user:
    # Active Session Core Workspace Grid Layout
    col_input, col_output = st.columns([1, 1.3], gap="large")

    with col_input:
        st.markdown("### 📥 Competitor Source Data")
        st.caption("Paste competitor text payloads, landing assets, or product structures below:")
        
        competitor_payload = st.text_area(
            label="Input Field Container:",
            label_visibility="collapsed",
            height=320,
            placeholder="Example: The Ridge wallet sells minimal titanium cardholder options. Their marketing emphasizes discarding old bulky leather bifold wallets that damage posture and compromise card data privacy via RFID scanning..."
        )
        
        run_processing_node = st.button("Execute Core Intelligence Extraction")

    with col_output:
        st.markdown("### 📊 Extracted Strategic Dossier")
        
        if run_processing_node:
            if not competitor_payload.strip() or len(competitor_payload) < 10:
                st.error("Operational Halt: Input dataset payload length is insufficient for analysis.")
            else:
                with st.spinner("Securing API pipeline channels. Extracting psychological angles..."):
                    try:
                        client = Groq(api_key=api_key)
                        
                        system_instruction = "You are a world-class conversion rate optimization specialist and master copywriter."
                        analysis_instruction = f"Analyze the following raw context text from a competitor's storefront assets and extract their core operational architecture blueprint data:\n\nRaw Context Payload:\n{competitor_payload}\n\nPlease provide a sharp breakdown containing:\n1. THE PRIMARY HOOK\n2. CORE PAIN POINT AGITATION\n3. MARKET POSITIONING FRAMEWORK\n4. COUNTER-ATTACK CAMPAIGN BLUEPRINT\n5. HIGH-CONVERSION SOCIAL ADS SCRIPTS."
                        
                        response = client.chat.completions.create(
                            model="qwen/qwen3.6-27b",
                            messages=[
                                {"role": "system", "content": system_instruction},
                                {"role": "user", "content": analysis_instruction}
                            ],
                            temperature=0.3,
                            max_tokens=4096
                        )
                        
                        st.success("Handshake Successful. Intelligence Compiled Below:")
                        st.markdown(response.choices[0].message.content)
                        
                    except Exception as e:
                        st.error(f"❌ CONNECTION FAILURE UNHANDLED OUTBOUND THREAD:\n\n{str(e)}")
        else:
            st.info("System Idle: Awaiting data inputs. Paste competitor sales text on the left workspace window and run the dashboard extractor engine.")

else:
    # 🌟 Fully Operational, Clean Native Streamlit Paywall UI Interface Container
    with st.container(border=True):
        st.write("")
        st.markdown("<h2 style='text-align: center; margin-top: 0px; color: white;'>🔒 Unlock the SpyAngle Enterprise Studio</h2>", unsafe_allow_html=True)
        st.write("")
        
        # Native Layout Alignment Columns for Badges
        p_col1, p_col2 = st.columns(2)
        with p_col1:
            st.metric(label="Global Plan Pricing", value="$29 / Month", delta="PRO ACCESS")
        with p_col2:
            st.metric(label="South African Rate (Approx)", value="R470 / Month", delta="Local Node")
            
        st.divider()
        
        # High-converting motivational pillars styled flawlessly without text breaks
        st.markdown("### **Stop Burning Ad Budget on Blind Angle Testing. Reverse-Engineer What is Already Printing Cash.**")
        st.write(
            "In high-velocity digital advertising, launching campaigns blindly is financial suicide. "
            "Your top competitors spend thousands of dollars optimizing hooks, uncovering specific customer fears, "
            "and isolating psychological angles so you don't have to. SpyAngle AI Studio reverse-engineers "
            "their underlying sales frameworks and outputs three hyper-tailored variations of direct-response social "
            "ad scripts in under 10 seconds. Secure your unfair arbitrage edge. One single winning ad creative pays "
            "for this platform for an entire year."
        )
        
        st.write("")
        
        # Beautiful, Clean Native Interactive Stripe Linking Button
        st.link_button(
            label="🚀 Start Your Premium Subscription Now",
            url=STRIPE_PAYMENT_URL,
            use_container_width=True
        )
        
        st.caption("Secure sub-second transaction routing handled via Stripe Infrastructure • Cancel or pause anytime with 1-click.")
