import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import uuid

st.set_page_config(page_title="INVIQ — Virtual Oil Lamp", page_icon="🪔", layout="wide")

# ---------- Minimal top UI ----------
st.markdown("""
<style>
.block-container { padding-top: 1.2rem; max-width: 1200px; }
.small { opacity: .85; }
.hr { height:1px; background:rgba(255,255,255,.12); margin: 1rem 0; }
.badge { display:inline-block; padding:.25rem .6rem; border-radius:999px;
         border:1px solid rgba(255,255,255,.18); background:rgba(255,255,255,.04); }
</style>
""", unsafe_allow_html=True)

# ---------- Session state ----------
if "lit" not in st.session_state:
    st.session_state.lit = False
if "ceremony_id" not in st.session_state:
    st.session_state.ceremony_id = str(uuid.uuid4())[:8]
if "who" not in st.session_state:
    st.session_state.who = ""
if "intention" not in st.session_state:
    st.session_state.intention = ""
if "lit_time" not in st.session_state:
    st.session_state.lit_time = None

# ---------- Header ----------
c1, c2 = st.columns([1.2, 1])
with c1:
    st.title("🪔 Virtual Oil Lamp Ceremony")
    st.caption("A cinematic, tech-inspired ritual to officially begin your startup journey.")
with c2:
    st.markdown(
        f"<div style='text-align:right; margin-top: 0.3rem;'>"
        f"<span class='badge'>Ceremony ID: {st.session_state.ceremony_id}</span>"
        f"</div>",
        unsafe_allow_html=True
    )

st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

# ---------- Controls ----------
left, right = st.columns([0.9, 1.1], gap="large")
with left:
    st.subheader("Start the Ceremony")
    st.session_state.who = st.text_input("Your name / brand name", value=st.session_state.who, placeholder="e.g., INVIQ Systems / Shanika")
    st.session_state.intention = st.text_area(
        "Your intention (short & meaningful)",
        value=st.session_state.intention,
        placeholder="e.g., Build with integrity. Create value. Help others.",
        height=110
    )

    colA, colB = st.columns(2)
    with colA:
        if st.button("✨ Light the Lamp", use_container_width=True):
            st.session_state.lit = True
            st.session_state.lit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with colB:
        if st.button("↺ Reset", use_container_width=True):
            st.session_state.lit = False
            st.session_state.lit_time = None

    st.markdown("**Tip:** After lighting, take a screenshot of the Blessing Card and post it on Facebook/LinkedIn. 📸")
    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    st.subheader("Share Links")
    st.write("Add these under the ceremony for a premium touch:")
    st.markdown("- 🌐 Website: https://inviqsystems.com/")
    st.markdown("- 💼 LinkedIn: https://www.linkedin.com/company/112145054/")
    st.markdown("- 📘 Facebook: https://web.facebook.com/profile.php?id=61587397293512")

with right:
    st.markdown("<h3 style='text-align: center;'>The Lamp</h3>", unsafe_allow_html=True)
    lit = "true" if st.session_state.lit else "false"

    # ---------- HTML/CSS/JS lamp ----------
    html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  :root {{
    --bg1: #070A12;
    --bg2: #0A0F1F;
    --gold1: #f6d48f;
    --gold2: #b77b2f;
    --metal: rgba(255,255,255,.12);
    --text: rgba(255,255,255,.9);
  }}
  body {{
    margin:0; padding:0;
    background: radial-gradient(1200px 700px at 70% 20%, rgba(255,175,70,.12), transparent 55%),
                radial-gradient(900px 600px at 30% 80%, rgba(100,150,255,.10), transparent 55%),
                linear-gradient(160deg, var(--bg1), var(--bg2));
    font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
    color: var(--text);
  }}
  .wrap {{
    position: relative;
    border-radius: 22px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,.12);
    background: rgba(255,255,255,.03);
    box-shadow: 0 18px 60px rgba(0,0,0,.45);
    padding: 24px;
    min-height: 520px;
  }}
  .topline {{
    display:flex; justify-content:space-between; align-items:center;
    margin-bottom: 10px;
  }}
  .title {{
    font-weight: 700; letter-spacing: .5px;
  }}
  .status {{
    font-size: 13px; opacity: .9;
    padding: 6px 10px; border-radius: 999px;
    border: 1px solid rgba(255,255,255,.15);
    background: rgba(255,255,255,.04);
  }}
  .sound-ctrl {{
    position: absolute; top: 20px; right: 20px; z-index: 10;
    cursor: pointer; opacity: 0.7; transition: opacity 0.2s;
    background: rgba(255,255,255,0.1); border-radius: 50%; padding: 8px;
    width: 24px; height: 24px; display: flex; align-items: center; justify-content: center;
    font-size: 16px; user-select: none;
  }}
  .sound-ctrl:hover {{ opacity: 1; background: rgba(255,255,255,0.2); }}
  }}
  .stage {{
    position: relative;
    height: 430px;
    display:flex;
    justify-content:center;
    align-items:flex-end;
    margin-top: 8px;
  }}
  @media (max-width: 520px) {{
    .stage {{ transform: scale(0.7); transform-origin: bottom center; margin-bottom: -30px; }}
    .wrap {{ padding: 10px; }}
  }}

  /* Lamp base (stylized) */
  .lamp {{
    position: relative;
    width: 100%;
    max-width: 460px;
    height: 360px;
    transform: translateY(2px);
    filter: drop-shadow(0 20px 25px rgba(0,0,0,.55));
  }}

  /* Crossbar for 3 branches */
  .crossbar {{
    position:absolute; bottom: 155px; left: 50%;
    width: 260px; height: 30px;
    transform: translateX(-50%);
    border-radius: 99px;
    background: linear-gradient(90deg, rgba(183,123,47,.2), rgba(246,212,143,.3), rgba(183,123,47,.2));
    border: 1px solid rgba(255,255,255,.12);
  }}

  .plate {{
    position:absolute; bottom: 0; left: 50%;
    width: 340px; height: 62px;
    transform: translateX(-50%);
    border-radius: 999px;
    background: radial-gradient(160px 40px at 50% 30%, rgba(255,255,255,.18), transparent 55%),
                linear-gradient(180deg, rgba(246,212,143,.20), rgba(183,123,47,.18));
    border: 1px solid rgba(255,255,255,.14);
  }}

  .stem {{
    position:absolute; bottom: 36px; left: 50%;
    width: 110px; height: 170px;
    transform: translateX(-50%);
    border-radius: 26px;
    background: radial-gradient(90px 120px at 35% 30%, rgba(255,255,255,.22), transparent 55%),
                linear-gradient(180deg, rgba(246,212,143,.22), rgba(183,123,47,.20));
    border: 1px solid rgba(255,255,255,.14);
  }}

  .bowl {{
    position:absolute; bottom: 170px; left: 50%; z-index: 2;
    width: 260px; height: 110px;
    transform: translateX(-50%);
    border-radius: 999px 999px 120px 120px;
    background: radial-gradient(140px 70px at 45% 35%, rgba(255,255,255,.26), transparent 60%),
                linear-gradient(180deg, rgba(246,212,143,.28), rgba(183,123,47,.22));
    border: 1px solid rgba(255,255,255,.16);
    overflow:hidden;
  }}
  .bowl:after {{
    content:"";
    position:absolute; left: 10%; top: 16%;
    width: 80%; height: 30%;
    border-radius: 999px;
    background: rgba(0,0,0,.18);
    filter: blur(0.5px);
    opacity: .55;
  }}

  /* Wick */
  .wick {{
    position:absolute; bottom: 246px; left: 50%; z-index: 2;
    width: 16px; height: 36px;
    transform: translateX(-50%);
    border-radius: 10px;
    background: linear-gradient(180deg, rgba(240,240,240,.70), rgba(80,80,80,.55));
    border: 1px solid rgba(255,255,255,.12);
  }}

  /* Flame */
  .flame {{
    position:absolute; bottom: 275px; left: 50%; z-index: 3;
    width: 54px; height: 86px;
    transform: translateX(-50%);
    border-radius: 60% 60% 60% 60%;
    background: radial-gradient(18px 22px at 50% 65%, rgba(255,255,255,.85), transparent 70%),
                radial-gradient(26px 40px at 50% 70%, rgba(255,200,70,.95), transparent 72%),
                radial-gradient(40px 60px at 50% 75%, rgba(255,120,30,.70), transparent 74%),
                radial-gradient(60px 80px at 50% 85%, rgba(255,70,10,.35), transparent 76%);
    filter: blur(.2px) saturate(1.25);
    opacity: 0;
  }}

  /* Glow around flame */
  .glow {{
    position:absolute; bottom: 250px; left: 50%; z-index: 3;
    width: 220px; height: 220px;
    transform: translateX(-50%);
    border-radius: 999px;
    background: radial-gradient(circle, rgba(255,170,50,.22), transparent 65%);
    opacity: 0;
  }}

  /* Side Lamp Adjustments (Left & Right) */
  .left {{ left: calc(50% - 110px); }}
  .right {{ left: calc(50% + 110px); }}
  .side.bowl  {{ bottom: 140px; transform: translateX(-50%) scale(0.75); z-index: 1; }}
  .side.wick  {{ bottom: 200px; transform: translateX(-50%) scale(0.75); z-index: 1; }}
  .side.flame {{ bottom: 225px; transform: translateX(-50%) scale(0.75); z-index: 3; }}
  .side.glow  {{ bottom: 200px; transform: translateX(-50%) scale(0.75); z-index: 3; }}

  /* Sparks canvas */
  canvas {{
    position:absolute; left:0; top:0;
    width:100%; height:100%;
    pointer-events:none;
  }}

  /* Animate only when lit */
  .lit .flame {{ opacity: 1; animation: flicker 1.8s infinite ease-in-out; }}
  .lit .glow  {{ opacity: 1; animation: pulse 2.6s infinite ease-in-out; }}

  @keyframes flicker {{
    0%   {{ transform: translateX(-50%) rotate(-2deg) scale(1.00); }}
    25%  {{ transform: translateX(-50%) rotate(2deg)  scale(1.03); }}
    50%  {{ transform: translateX(-50%) rotate(-1deg) scale(0.98); }}
    75%  {{ transform: translateX(-50%) rotate(1deg)  scale(1.02); }}
    100% {{ transform: translateX(-50%) rotate(-2deg) scale(1.00); }}
  }}
  @keyframes pulse {{
    0% {{ transform: translateX(-50%) scale(0.95); opacity:.55; }}
    50% {{ transform: translateX(-50%) scale(1.05); opacity:1; }}
    100% {{ transform: translateX(-50%) scale(0.95); opacity:.55; }}
  }}

  .note {{
    margin-top: 14px;
    padding: 12px 18px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,.12);
    background: rgba(0,0,0,.18);
    line-height: 1.45;
    max-width: 420px;
    margin-left: auto;
    margin-right: auto;
  }}
  .note b {{ color: rgba(255,255,255,.95); }}
  .hint {{
    opacity:.85; font-size: 13px;
    margin-top: 8px;
  }}
</style>
</head>
<body>
  <div class="wrap { "lit" if st.session_state.lit else "" }" id="wrap">
    <div class="topline">
      <div class="title">INVIQ • Virtual Lamp Lighting</div>
      <div class="status" id="status">{ "🟡 Ready to light" if not st.session_state.lit else "🟢 Lamp is lit" }</div>
      <div class="sound-ctrl" id="soundBtn" title="Toggle Sound">🔇</div>
    </div>

    <div class="stage">
      <canvas id="sparks"></canvas>

      <div class="lamp">
        <div class="crossbar"></div>

        <!-- Left Branch -->
        <div class="glow side left"></div>
        <div class="flame side left"></div>
        <div class="wick side left"></div>
        <div class="bowl side left"></div>

        <!-- Right Branch -->
        <div class="glow side right"></div>
        <div class="flame side right"></div>
        <div class="wick side right"></div>
        <div class="bowl side right"></div>

        <!-- Center Branch -->
        <div class="glow"></div>
        <div class="flame"></div>
        <div class="wick"></div>
        <div class="bowl"></div>

        <div class="stem"></div>
        <div class="plate"></div>
      </div>
    </div>

    <div class="note">
      <div><b>Ceremony ID:</b> {st.session_state.ceremony_id}</div>
      <div><b>Lit by:</b> {st.session_state.who if st.session_state.who.strip() else "—"}</div>
      <div><b>Intention:</b> {st.session_state.intention if st.session_state.intention.strip() else "—"}</div>
      <div><b>Time:</b> {st.session_state.lit_time if st.session_state.lit_time else "—"}</div>
      <div class="hint">Tip: take a screenshot of this card and share it as your official “startup begins” moment.</div>
    </div>

    <audio id="bgm" loop>
      <source src="https://cdn.pixabay.com/audio/2022/05/27/audio_1808fbf07a.mp3" type="audio/mpeg">
    </audio>
  </div>

<script>
  const lit = {lit};

  const audio = document.getElementById("bgm");
  const btn = document.getElementById("soundBtn");

  function toggleSound() {{
    if(!audio) return;
    if(audio.paused) {{
      audio.play();
      btn.innerHTML = "🔊";
    }} else {{
      audio.pause();
      btn.innerHTML = "🔇";
    }}
  }}
  btn.addEventListener("click", toggleSound);

  if(lit && audio) {{
    audio.volume = 0.5;
    // Try to play automatically. If browser blocks it, user can click the button.
    audio.play().then(() => {{ btn.innerHTML = "🔊"; }}).catch(e => {{ console.log("Autoplay blocked, waiting for user interaction"); }});
  }}

  const canvas = document.getElementById("sparks");
  const wrap = document.getElementById("wrap");
  const ctx = canvas.getContext("2d");

  function resize() {{
    const r = wrap.getBoundingClientRect();
    canvas.width = Math.floor(r.width * devicePixelRatio);
    canvas.height = Math.floor(r.height * devicePixelRatio);
  }}
  window.addEventListener("resize", resize);
  resize();

  const sparks = [];
  function spawnSpark() {{
    const r = wrap.getBoundingClientRect();
    
    // Randomly choose source (Left, Center, Right)
    const rand = Math.random();
    let dx = 0; let dy = 0;
    if (rand < 0.3) {{ dx = -110; dy = 30; }}      // Left lamp
    else if (rand > 0.7) {{ dx = 110; dy = 30; }}  // Right lamp

    const x = (r.width/2 + dx) * devicePixelRatio;
    const y = (r.height - 260 + dy) * devicePixelRatio;

    sparks.push({{
      x, y,
      vx: (Math.random()*12 - 6) * devicePixelRatio, // Wide spread
      vy: (Math.random()*-10 - 2) * devicePixelRatio, // Fly high
      life: Math.random()*80 + 60
    }});
  }}

  function tick() {{
    ctx.clearRect(0,0,canvas.width, canvas.height);

    if(lit) {{
      // spawn
      for(let k=0; k<3; k++) {{ if (Math.random() < 0.6) spawnSpark(); }}

      // glow overlay
      ctx.save();
      ctx.globalCompositeOperation = "lighter";
      // draw sparks
      for(let i=sparks.length-1;i>=0;i--) {{
        const s = sparks[i];
        s.x += s.vx;
        s.y += s.vy;
        s.vy += 0.05 * devicePixelRatio; // gravity
        s.vx *= 0.96; // air resistance
        s.life -= 1;

        const alpha = Math.max(0, Math.min(1, s.life/80));
        const radius = (Math.random()*3 + 1.5) * devicePixelRatio;

        // warm spark
        ctx.beginPath();
        ctx.fillStyle = `rgba(255, 170, 60, ${{alpha}})`;
        ctx.arc(s.x, s.y, radius, 0, Math.PI*2);
        ctx.fill();

        // hot core
        ctx.beginPath();
        ctx.fillStyle = `rgba(255, 255, 220, ${{alpha*0.7}})`;
        ctx.arc(s.x, s.y, radius*0.55, 0, Math.PI*2);
        ctx.fill();

        if(s.life <= 0) sparks.splice(i,1);
      }}
      ctx.restore();
    }}

    requestAnimationFrame(tick);
  }}
  tick();
</script>
</body>
</html>
"""
    components.html(html, height=560)

# ---------- Blessing card (shareable text) ----------
st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
st.subheader("📜 Shareable Caption (auto-generated)")
who = st.session_state.who.strip() or "My startup"
intent = st.session_state.intention.strip() or "Build with purpose. Create value. Keep going."
time_txt = st.session_state.lit_time or datetime.now().strftime("%Y-%m-%d")

caption = f"""🪔 Today, I officially began a new journey.

✨ Lamp Lit: {time_txt}
🔖 Intention: {intent}

This is the start — built with focus, courage, and consistency. 🚀
🌐 https://inviqsystems.com/
"""

st.text_area("Copy & post this (Facebook / LinkedIn)", caption, height=140)

st.caption("If you want: I can add background music, a countdown, a confetti reveal, and a downloadable certificate image.")