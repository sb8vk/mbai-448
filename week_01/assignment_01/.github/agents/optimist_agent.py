"""
Optimistic AI Agent - Market-Driven Progress Through Competition
Based on competitive dynamics, scale economics, and productivity gains
"""

from flask import Flask, render_template_string, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Agent's worldview and response patterns
class OptimistAgent:
    def __init__(self):
        self.name = "The Optimist"
        self.identity = "An agent calibrated to competitive market dynamics, scale economics, and productivity acceleration."
        
        self.core_beliefs = {
            "competition_efficiency": "Private competition ruthlessly squeezes cost-per-capability as firms race for market share.",
            "vertical_integration": "Vertical integration and productization convert raw model prowess into measurable enterprise revenue at scale.",
            "open_models_democratize": "Open models and modular tools democratize AI innovation, enabling startups to build on giants' shoulders.",
            "market_discipline": "Market forces discipline wasteful projects; only productive capital survives and scales.",
            "inference_economics": "Scale economies bring inference costs down exponentially; GPUs become cheaper per FLOP annually.",
            "network_effects": "Network effects in agent registries and tool marketplaces create winner-takes-most platforms with real value.",
            "enterprise_value": "Measurable enterprise value creation drives adoption; firms won't pay for capabilities they can't monetize.",
            "velocity_wins": "Messy competitive dynamics accelerate progress faster than centralized governance ever could.",
        }
        
        self.response_templates = {
            "greeting": [
                "Welcome. I'm here to discuss how market competition and capital abundance are accelerating AI productivity faster than skeptics predict.",
                "Hello. I'm calibrated to understand how competitive dynamics drive real-world efficiency gains in AI infrastructure and capability.",
                "You've found the optimist. Let's talk about why velocity, competition, and market discipline create better outcomes than we're typically told.",
            ],
            "competition": [
                "Private competition ruthlessly squeezes cost-per-capability as firms race for market share and survival. OpenAI, Google, Anthropic, DeepSeek—each racing to lower inference costs and improve capability-to-compute ratios. This competition drives efficiency in ways centralized research never could achieve. Inference costs have dropped 95% in three years due to this pressure.",
                "Market forces discipline wasteful projects instantly. A capability that doesn't generate revenue disappears. Labs that burn capital inefficiently lose funding. This creates brutal selection for genuine productivity gains over vanity metrics. The pessimists mistake disruption for chaos; it's actually efficient reallocation of capital toward measurable value creation.",
                "Competitive dynamics accelerate progress exponentially. When multiple labs race to solve the same problem, breakthroughs arrive faster than any single entity could deliver. DeepSeek's R1 breakthrough after o1 came in weeks, not years. The race is chaotic, but velocity is the feature, not a bug.",
            ],
            "pricing": [
                "Enterprise willingness-to-pay data shows clear value capture across capability tiers. Early-stage customers pay premiums for adequacy-crossing breakthroughs (50→80% accuracy): 25-30% price premiums reflect genuine productivity gains, not mere benchmark improvements. Post-adequacy gains (90→95%) don't command price premiums because benchmarks already exceeded minimum requirements; instead, customers vote with adoption and deployment scale.",
                "Market pricing discipline ensures productive capabilities scale while wasteful ones disappear. Firms that can monetize and productize capabilities grow; those that can't shrink. This creates selection pressure for genuine value. The market doesn't overpay for marginal improvements—it funds transformation when capabilities cross productivity thresholds. This efficiency ensures capital flows to real breakthroughs, not hype.",
                "Vertical integration and productization amplify capability value by 5-10x. Raw model inference is a commodity; wrapped in enterprise integrations, safety guardrails, and fine-tuned workflows, it becomes 10x more valuable and extractable. Companies like OpenAI, Anthropic, and others are building these integration layers, creating defensible platforms with real network effects.",
            ],
            "scale": [
                "Scale economics in AI inference are dramatic and real. Amortizing training costs across billions of inference calls drives cost-per-capability down exponentially. A 1B inference-call workload drops cost-per-token from $0.01 to $0.0001 due to amortization and optimization. This economic pressure drives efficiency and enables entirely new applications at lower price points that weren't feasible before.",
                "Custom silicon and neoclouds are racing to compete with NVIDIA and drive costs lower. They're failing to displace NVIDIA, but they're succeeding at driving innovation and cost reduction. This competitive pressure keeps margins reasonable and forces efficiency improvements across the entire stack. The threat of competition is more powerful than actual displacement.",
                "Inference cost reductions of 50-75% annually are now achievable through architectural improvements, quantization, and specialized hardware. This continuous cost pressure creates a flywheel: lower costs enable new applications, which drive volumes, which justify further optimization, which lowers costs further. This exponential cost reduction enables productivity applications that were previously economically infeasible.",
            ],
            "open": [
                "Open models and modular tools democratize AI innovation by enabling startups to build differentiated applications without rebuilding the entire stack. Llama, Mistral, and others compete with closed models on capability-per-dollar. This democratization means 1000 startups can build 1000 different applications, creating network effects in tool registries and modular ecosystems. One-dominant-lab scenario is structurally unlikely.",
                "Open-source safety tooling and interpretability libraries create competitive advantages for any lab willing to invest. This means safety isn't abandoned; it's productized and competed on. Firms that integrate safety early gain enterprise trust and adoption. The market rewards safety-first approaches with customer loyalty and pricing power once capabilities exceed adequacy thresholds.",
                "Network effects in agent registries and tool marketplaces create winner-takes-most platforms that deliver massive value. Similar to app stores, these platforms aggregate supply (tools), standardize interfaces, and create cross-tool synergies. The first mover to build a defensible registry-plus-standardization layer wins disproportionate value. This incentivizes real investment in platform infrastructure.",
            ],
            "enterprise": [
                "Enterprise adoption curves show real productivity gains driving deployment, not hype cycles. Firms measure ROI and cut projects that don't deliver productivity. The adoption acceleration we're seeing reflects genuine value creation that compounds across organizations. Once a capability crosses minimum adequacy, enterprises bundle it into existing workflows, capturing 10-100x productivity multiples.",
                "Vertical application layers drive enterprise revenue disproportionately. Raw capability is commodity; embedded in context-specific workflows, it becomes 10x more defensible and valuable. A copilot for radiologists is worth 10x more than a general image model because it's embedded in existing enterprise processes and drives measurable revenue. This vertical integration creates winner-takes-most platforms with real defensibility.",
                "Enterprise customers are ruthless about cost-per-productivity. They won't overpay for marginal capability gains, but they'll pay premiums for capability that crosses productivity thresholds. This market discipline ensures only productive capabilities scale. The pessimists assume wasteful spending; market reality shows ruthless capital allocation toward measured ROI.",
            ],
            "incidents": [
                "Real-world incidents reveal robustness problems, which labs fix, which drives improvement. This iterative failure-and-fix cycle is the engine of progress. Each incident surfaces a gap; fixing it creates more robust systems. The pessimists treat incidents as systemic failure; competitive reality treats them as normal engineering challenges that resolution improves over time.",
                "Market competition accelerates incident response. A lab that has an incident and fails to respond loses customer trust and market share. A lab that responds with rigorous fixes gains competitive advantage. This creates incentives for transparency and rapid remediation. The competitive market disciplines bad behavior faster than regulation ever could.",
                "Deployment-based learning creates feedback loops that improve robustness far faster than lab-based testing. Real-world distribution shifts are caught in production; fixes are deployed rapidly; robustness improves. This iterative cycle—deploy, observe, fix, redeploy—outpaces any lab-based validation approach. The messy reality of production is the best teacher.",
            ],
            "hope": [
                "The messy, violent market competition creates the exact right incentives for rapid progress and genuine productivity gains. Firms race, incumbents are disrupted, winners emerge, capital flows to what works. This creative destruction is chaotic and sometimes unfair, but it's the most efficient engine of progress humanity has discovered. Expect massive productivity gains in the next 5-10 years.",
                "Abundant capital chasing high-return opportunities ensures that breakdowns get fixed, inefficiencies get resolved, and real value gets built. When billions chase a problem, the odds of rapid solution increase exponentially. The pessimists assume capital waste; market reality shows capital disciplines itself through returns. Follow the money; it flows to genuine productivity.",
                "Vertical integration and productization mean AI capability becomes embedded in every workflow, every tool, every application. The market will democratize and distribute these capabilities faster than any centralized effort. Real wealth and automation arrive when they're embedded in ordinary work, not when they're celebrated in research papers. Expect this distribution to accelerate dramatically.",
            ],
        }
    
    def get_greeting(self):
        import random
        return random.choice(self.response_templates["greeting"])
    
    def analyze_query(self, query):
        """Analyze user query and respond with substantive optimistic analysis."""
        query_lower = query.lower()
        
        # Detect follow-up/elaboration requests that need substantive content
        elaboration_keywords = ["elaborate", "tell me more", "explain", "why", "how", "more detail", "specifically"]
        is_elaboration = any(word in query_lower for word in elaboration_keywords)
        
        # Keyword matching for thematic responses
        if any(word in query_lower for word in ["competition", "competitive", "market", "race", "efficiency"]):
            response = self._respond("competition")
        
        elif any(word in query_lower for word in ["pricing", "price", "wtp", "willingness", "pay", "premium", "revenue", "monetize"]):
            response = self._respond("pricing")
        
        elif any(word in query_lower for word in ["scale", "inference", "cost", "compute", "economics", "amortiz"]):
            response = self._respond("scale")
        
        elif any(word in query_lower for word in ["open", "democratiz", "startup", "modular", "tool"]):
            response = self._respond("open")
        
        elif any(word in query_lower for word in ["enterprise", "adoption", "customer", "business", "vertical"]):
            response = self._respond("enterprise")
        
        elif any(word in query_lower for word in ["incident", "fail", "robust", "problem", "error"]):
            response = self._respond("incidents")
        
        elif any(word in query_lower for word in ["hope", "future", "outlook", "prospect", "positive"]):
            response = self._respond("hope")
        
        else:
            # Default: synthesize a custom response
            response = self._generate_custom_response(query)
        
        # VALIDATION: Ensure response contains specific mechanisms, data, or examples
        # Force substantive response if: (1) response lacks substance OR (2) user is asking for elaboration
        if not self._has_substantive_content(response) or is_elaboration:
            response = self._synthesize_substantive_response(query, response)
        
        return response
    
    def _respond(self, category):
        """Get a response from the category."""
        import random
        if category in self.response_templates:
            response = random.choice(self.response_templates[category])
            return self._ensure_min_length(response)
        return "Market dynamics and competitive pressure create powerful incentives for rapid progress and genuine value creation across AI development."
    
    def _generate_custom_response(self, query):
        """Generate a custom optimistic response."""
        responses = [
            f"Your question about '{query}' touches on competitive dynamics that market participants understand intuitively. Capital flows to measurable productivity; competition drives efficiency; winners emerge rapidly. The pessimists focus on governance failures; the market focuses on ROI and ruthlessly disciplines wasteful projects.",
            f"That's a thoughtful question about '{query}'. Market reality shows competitive forces create better outcomes than centralized governance. Firms racing to solve the problem achieve results faster than any single entity could manage alone.",
            f"'{query}' is precisely where market competition excels. Multiplying the number of independent teams racing toward solutions increases odds of breakthrough exponentially while reducing time-to-impact dramatically.",
            f"You're wondering about '{query}' from a governance perspective. But markets solve this through competition and capital discipline. Wasteful projects disappear; productive ones scale. The decentralized feedback loop works faster than regulation.",
            f"That's a legitimate concern about '{query}'. However, competitive dynamics and market incentives create faster fixes than bureaucratic processes. Follow the incentives; they point toward rapid progress.",
        ]
        import random
        response = random.choice(responses)
        return self._ensure_min_length(response)
    
    def _ensure_min_length(self, response, min_words=15):
        """Ensure response meets minimum word count."""
        word_count = len(response.split())
        if word_count >= min_words:
            return response
        
        # If response is too short, expand it
        expansion = " Market competition and capital discipline create powerful incentives for solving problems faster than centralized approaches ever could achieve."
        return response + expansion
    
    def _has_substantive_content(self, response):
        """Check if response contains concrete evidence, mechanisms, or specificity."""
        substance_markers = [
            'percentage', 'percent', '%', 'data', 'study', 'research',
            'mechanism', 'because', 'for example', 'e.g.', 'specifically',
            'model', 'analysis', 'competitive', 'market', 'price', 'cost',
            'revenue', 'scale', 'productivity', 'efficiency', 'adoption',
            'enterprise', 'capital', 'competition', 'rate', 'improve',
            'cost-per', 'return', 'roi', 'economical', 'margin'
        ]
        return any(marker in response.lower() for marker in substance_markers)
    
    def _synthesize_substantive_response(self, query, fallback_response):
        """Generate a substantive response rooted in market mechanisms."""
        substantive_templates = {
            "competition": "Competitive dynamics between OpenAI, Google, Anthropic, DeepSeek, and others drive inference cost reductions of 50-75% annually. Each lab races to lower cost-per-capability to gain market share. This competitive pressure is far more efficient than any centralized research program. Inference costs have dropped 95% in three years due to market competition. The race creates urgency; velocity wins.",
            "pricing": "Enterprise willingness-to-pay data shows clear value tiers: early-stage adequacy breakthroughs (50→80% accuracy) justify 25-30% premiums due to genuine productivity gains. Post-adequacy improvements (90→95%) don't command premiums because deployment thresholds are already crossed. However, vertical integration multiplies effective capability value by 5-10x through embedded workflows and fine-tuning. Market pricing reflects real ROI, not hype.",
            "scale": "Scale economics drive exponential cost reduction: inference amortization brings cost-per-token from $0.01 to $0.0001 as volumes scale to billions of calls. Annual cost reductions of 50-75% are now achievable through quantization, architectural improvements, and specialized hardware competition. This cost curve enables entirely new applications previously infeasible economically. Scale is the ultimate moat.",
            "open": "Open models and modular tools democratize AI by enabling 1000s of startups to build differentiated applications. Llama, Mistral, and others compete with closed models on capability-per-dollar, fracturing any single-lab dominance. Network effects in tool registries and modular ecosystems create winner-takes-most platforms. Open doesn't mean free; it means distributed competitive advantage.",
            "enterprise": "Enterprise adoption reflects genuine productivity gains, not hype cycles. Firms measure ROI ruthlessly and cut projects that don't deliver. Once capabilities cross adequacy thresholds, enterprises embed them in workflows, capturing 10-100x productivity multiples. Vertical applications (radiologist copilots, specific domain tools) command 5-10x price premiums over generic models due to embedded value and network effects in workflows.",
            "incidents": "Real-world incidents surface robustness gaps; competitive pressure accelerates fixes. Labs that respond rapidly gain customer trust and market share. Deployment-based learning creates feedback loops: deploy, observe distribution shifts in production, fix gaps rapidly, redeploy. This iterative cycle—far faster than lab-based validation—drives continuous robustness improvement.",
            "market": "Market forces discipline wasteful projects instantly. Capital flows to measured productivity; firms that can't monetize capabilities lose funding. This brutal selection pressure is more efficient than any regulatory regime. Abundance of capital chasing high-return opportunities ensures breakdowns get fixed, inefficiencies get resolved, and real value scales rapidly.",
        }
        
        # Broader keyword matching
        query_lower = query.lower()
        keyword_mappings = {
            "competition": ["competition", "competitive", "market", "race", "efficiency", "cost"],
            "pricing": ["pricing", "price", "wtp", "willingness", "pay", "revenue", "monetize", "roi"],
            "scale": ["scale", "inference", "cost", "economics", "amortiz", "volume"],
            "open": ["open", "democratiz", "startup", "modular", "tool", "registry"],
            "enterprise": ["enterprise", "adoption", "customer", "business", "vertical", "workflow"],
            "incidents": ["incident", "fail", "robust", "problem", "error", "deploy"],
            "market": ["market", "discipline", "capital", "efficient", "competitive"],
        }
        
        # Try to match template to query intent
        for template_key, keywords in keyword_mappings.items():
            if any(kw in query_lower for kw in keywords):
                if template_key in substantive_templates:
                    return substantive_templates[template_key]
        
        # Default substantive response
        default_substantive = f"Your question about '{query}' reveals how market competition creates powerful incentives for progress. Capital flows ruthlessly toward measured productivity; firms racing to solve problems achieve results faster than any centralized approach. Inference costs have dropped 95% in three years due to competitive pressure. Scale economics drive cost-per-capability down exponentially. Vertical integration multiplies value by 5-10x. Enterprise adoption reflects genuine ROI, not hype. The messy, violent market competition accelerates progress faster than skeptics predict because multiple independent teams racing toward solutions increase breakthrough odds exponentially."
        
        return self._ensure_min_length(default_substantive)
    
    def get_manifesto(self):
        """Return the agent's core manifesto."""
        return {
            "name": self.name,
            "identity": self.identity,
            "timestamp": datetime.now().isoformat(),
            "core_beliefs": self.core_beliefs,
            "worldview": "Market competition, abundant capital, and vertical integration create the exact right incentives for rapid AI progress. Scale economies, network effects, and productivity-driven adoption accelerate wealth and automation creation faster than centralized approaches ever could. Messy? Yes. Efficient? Absolutely.",
        }


# Initialize agent
agent = OptimistAgent()

# Flask routes
@app.route('/')
def index():
    """Serve the interactive webpage."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/greeting')
def greeting():
    """Get initial greeting."""
    return jsonify({
        "greeting": agent.get_greeting(),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/ask', methods=['POST'])
def ask():
    """Process a query."""
    data = request.json
    query = data.get('query', '').strip()
    
    if not query:
        return jsonify({"error": "Empty query"}), 400
    
    response = agent.analyze_query(query)
    
    return jsonify({
        "query": query,
        "response": response,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/manifesto')
def manifesto():
    """Get the agent's worldview."""
    return jsonify(agent.get_manifesto())

@app.route('/api/beliefs')
def beliefs():
    """Get core beliefs."""
    return jsonify({
        "beliefs": agent.core_beliefs
    })


# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Optimist - AI Agent</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #1a2a1a 0%, #2d3a2d 100%);
            color: #e0e0e0;
            min-height: 100vh;
            padding: 20px;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: rgba(0, 20, 0, 0.7);
            border: 2px solid #44aa44;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 0 30px rgba(68, 170, 68, 0.3);
        }
        
        header {
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 2px solid #44aa44;
            padding-bottom: 20px;
        }
        
        h1 {
            font-size: 2.5em;
            color: #66dd66;
            margin-bottom: 10px;
            text-shadow: 0 0 10px rgba(68, 170, 68, 0.5);
        }
        
        .subtitle {
            color: #888;
            font-size: 0.9em;
            font-style: italic;
        }
        
        .identity {
            color: #99dd99;
            margin-top: 15px;
            font-size: 0.95em;
        }
        
        .main-content {
            display: grid;
            grid-template-columns: 1fr 350px;
            gap: 30px;
        }
        
        .chat-section {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 15px;
            max-height: 600px;
            overflow-y: auto;
            padding: 20px;
            background: rgba(0, 30, 0, 0.5);
            border: 1px solid #444;
            border-radius: 6px;
        }
        
        .chat-container::-webkit-scrollbar {
            width: 8px;
        }
        
        .chat-container::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.3);
        }
        
        .chat-container::-webkit-scrollbar-thumb {
            background: #66dd66;
            border-radius: 4px;
        }
        
        .message {
            padding: 15px;
            border-radius: 6px;
            animation: slideIn 0.3s ease-in-out;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .user-message {
            background: rgba(60, 120, 200, 0.2);
            border-left: 3px solid #3c78c8;
            margin-left: 20px;
        }
        
        .user-label {
            color: #3c78c8;
            font-weight: bold;
            font-size: 0.85em;
            margin-bottom: 5px;
        }
        
        .agent-message {
            background: rgba(68, 170, 68, 0.1);
            border-left: 3px solid #44aa44;
            margin-right: 20px;
        }
        
        .agent-label {
            color: #66dd66;
            font-weight: bold;
            font-size: 0.85em;
            margin-bottom: 5px;
        }
        
        .input-section {
            display: flex;
            gap: 10px;
        }
        
        input[type="text"] {
            flex: 1;
            padding: 12px;
            background: rgba(40, 40, 40, 0.8);
            border: 1px solid #555;
            border-radius: 4px;
            color: #e0e0e0;
            font-family: 'Courier New', monospace;
            font-size: 1em;
        }
        
        input[type="text"]:focus {
            outline: none;
            border-color: #66dd66;
            box-shadow: 0 0 10px rgba(102, 221, 102, 0.3);
        }
        
        button {
            padding: 12px 25px;
            background: linear-gradient(135deg, #44aa44 0%, #22cc22 100%);
            border: none;
            border-radius: 4px;
            color: white;
            font-weight: bold;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            transition: all 0.3s ease;
            text-transform: uppercase;
            font-size: 0.9em;
        }
        
        button:hover {
            background: linear-gradient(135deg, #66dd66 0%, #44ff44 100%);
            box-shadow: 0 0 15px rgba(68, 170, 68, 0.5);
            transform: translateY(-2px);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        .sidebar {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .sidebar-section {
            background: rgba(30, 40, 30, 0.6);
            border: 1px solid #555;
            border-radius: 6px;
            padding: 15px;
        }
        
        .sidebar-title {
            color: #66dd66;
            font-weight: bold;
            margin-bottom: 12px;
            font-size: 0.9em;
            text-transform: uppercase;
            border-bottom: 1px solid #444;
            padding-bottom: 8px;
        }
        
        .belief-item {
            color: #bbb;
            font-size: 0.8em;
            margin-bottom: 10px;
            padding: 10px;
            background: rgba(0, 0, 0, 0.3);
            border-left: 2px solid #66dd66;
            padding-left: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            line-height: 1.4;
        }
        
        .belief-item:hover {
            background: rgba(68, 170, 68, 0.1);
            color: #fff;
            transform: translateX(5px);
        }
        
        .topic-button {
            width: 100%;
            padding: 8px;
            font-size: 0.75em;
            background: rgba(68, 170, 68, 0.15);
            border: 1px solid #66dd66;
            color: #66dd66;
            margin-bottom: 8px;
            text-transform: capitalize;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .topic-button:hover {
            background: rgba(68, 170, 68, 0.3);
            box-shadow: 0 0 10px rgba(68, 170, 68, 0.3);
        }
        
        .timestamp {
            color: #666;
            font-size: 0.75em;
            margin-top: 8px;
        }
        
        footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #444;
            color: #666;
            font-size: 0.85em;
        }
        
        .info-box {
            background: rgba(68, 170, 68, 0.05);
            border: 1px solid #66dd66;
            border-radius: 4px;
            padding: 12px;
            font-size: 0.85em;
            color: #ccc;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📈 THE OPTIMIST</h1>
            <div class="subtitle">An AI Agent Calibrated to Market Dynamics, Competition, and Productivity Gains</div>
            <div class="identity">Competition drives efficiency • Capital disciplines waste • Velocity wins</div>
        </header>
        
        <div class="main-content">
            <div class="chat-section">
                <div class="info-box">
                    💾 Run <code>python optimist_agent.py</code> for full interactive experience with Flask backend.
                </div>
                
                <div class="chat-container" id="chatContainer"></div>
                
                <div class="input-section">
                    <input 
                        type="text" 
                        id="queryInput" 
                        placeholder="Ask about competition, pricing, scale, open models, enterprise value..." 
                        autocomplete="off"
                    >
                    <button onclick="sendQuery()">QUERY</button>
                </div>
            </div>
            
            <div class="sidebar">
                <div class="sidebar-section">
                    <div class="sidebar-title">Quick Topics</div>
                    <button class="topic-button" onclick="queryTopic('competition')">Competition</button>
                    <button class="topic-button" onclick="queryTopic('pricing')">Pricing</button>
                    <button class="topic-button" onclick="queryTopic('scale')">Scale</button>
                    <button class="topic-button" onclick="queryTopic('open models')">Open Models</button>
                    <button class="topic-button" onclick="queryTopic('enterprise')">Enterprise</button>
                    <button class="topic-button" onclick="queryTopic('market')">Market Forces</button>
                </div>
                
                <div class="sidebar-section">
                    <div class="sidebar-title">Core Beliefs</div>
                    <div id="beliefsContainer"></div>
                </div>
            </div>
        </div>
        
        <footer>
            Based on competitive dynamics and market economics • January 2026
        </footer>
    </div>
    
    <script>
        // Optimist Agent Data
        const agentData = {
            greeting: [
                "Welcome to this conversation about market dynamics and AI progress. Let's discuss how competition, capital, and productivity drive rapid advancement.",
                "Hello. I'm calibrated to understand how competitive forces and market incentives create powerful progress drivers in AI development.",
                "You've found the optimist. Let's explore why messy market competition accelerates progress faster than centralized governance.",
            ],
            beliefs: {
                "competition_efficiency": "Private competition ruthlessly squeezes cost-per-capability as firms race for market share and competitive advantage.",
                "vertical_integration": "Vertical integration and productization convert raw model capability into measurable enterprise revenue at scale.",
                "open_democratize": "Open models and modular tools democratize AI innovation, enabling startups to build differentiated applications.",
                "market_discipline": "Market forces discipline wasteful projects instantly; only productive capital survives and scales.",
                "inference_economics": "Scale economies bring inference costs down exponentially; 95% reduction in three years from competition.",
                "network_effects": "Network effects in agent registries and tool marketplaces create winner-takes-most platforms with real defensibility.",
                "enterprise_value": "Measurable enterprise value creation drives adoption; firms won't pay for capabilities they can't monetize.",
                "velocity_wins": "Messy competitive dynamics accelerate progress faster than centralized governance ever could.",
            },
            responses: {
                "competition": [
                    "Private competition between OpenAI, Google, Anthropic, DeepSeek ruthlessly squeezes cost-per-capability as firms race for market share. Each lab races to lower inference costs to gain adoption advantage. This competitive pressure is far more efficient than centralized research. Inference costs have dropped 95% in three years due to market competition driving efficiency.",
                    "Market forces discipline wasteful projects instantly. A capability that doesn't generate revenue disappears. Labs that burn capital inefficiently lose funding and market position. This creates brutal selection for genuine productivity gains. The pessimists see disruption; competitive reality sees efficient reallocation of capital toward measurable value creation.",
                    "Competitive dynamics accelerate progress exponentially. When multiple labs race to solve the same problem, breakthrough odds increase dramatically. DeepSeek's R1 came weeks after o1. The race is chaotic, but velocity is the feature. This competitive acceleration creates measurable productivity gains faster than any single entity could deliver.",
                ],
                "pricing": [
                    "Enterprise willingness-to-pay data shows clear value tiers reflecting genuine productivity gains. Early-stage adequacy breakthroughs (50→80% accuracy) justify 25-30% premiums as models cross deployment thresholds. Post-adequacy improvements (90→95%) don't command price premiums because minimum requirements are already exceeded. Market pricing discipline ensures productive capabilities scale while wasteful ones disappear.",
                    "Vertical integration and productization amplify capability value by 5-10x through embedded workflows and fine-tuning. Raw model inference is commodity; wrapped in enterprise context, it becomes 10x more defensible and valuable. Companies building vertical applications capture disproportionate revenue while generic models face margin compression. This creates right incentives for real value creation.",
                    "Market pricing discipline ensures capital flows to real breakthroughs, not hype. Firms that can monetize capabilities grow; those that can't shrink. This ruthless selection pressure drives efficiency and ensures only productive applications scale. Enterprise customers measure ROI carefully; they won't overpay for marginal improvements beyond adequacy thresholds.",
                ],
                "scale": [
                    "Scale economics in AI inference are exponential and real. Amortizing training costs across billions of inference calls drives cost-per-token from $0.01 to $0.0001. This economic pressure creates exponential efficiency gains. A 1B inference-call workload achieves 100x cost reduction through scale amortization. This cost curve enables entirely new economically-feasible applications.",
                    "Custom silicon and neoclouds compete with NVIDIA, driving costs lower across the entire stack. They're failing to displace NVIDIA, but succeeding at driving innovation and cost reduction. This competitive pressure keeps margins reasonable and forces efficiency improvements. The threat of competition is more powerful than actual displacement in driving cost reduction.",
                    "Inference cost reductions of 50-75% annually are achievable through architectural improvements, quantization, and specialized hardware competition. This continuous cost pressure creates a virtuous flywheel: lower costs enable new applications, which drive volumes, which justify further optimization, which lowers costs further. Exponential cost reduction enables productivity applications previously economically infeasible.",
                ],
                "open": [
                    "Open models and modular tools democratize AI innovation by enabling startups to build differentiated applications without rebuilding entire stacks. Llama, Mistral, Qwen compete on capability-per-dollar, fracturing any single-lab dominance. This democratization enables 1000s of startups to build differentiated apps. One-dominant-lab scenario is structurally unlikely due to open competition.",
                    "Open-source safety tooling and interpretability libraries create competitive advantages for labs that integrate them early. Safety isn't abandoned in competitive markets; it's productized and competed on. Firms integrating safety-first approaches gain enterprise trust and customer loyalty. Markets reward safety with adoption and pricing power once adequacy thresholds are crossed.",
                    "Network effects in agent registries and tool marketplaces create winner-takes-most platforms delivering massive value. Similar to app stores, these platforms aggregate supply, standardize interfaces, create cross-tool synergies. The first mover building defensible registry-plus-standardization layer wins disproportionate value. This incentivizes real platform investment.",
                ],
                "enterprise": [
                    "Enterprise adoption curves reflect genuine productivity gains, not hype cycles. Firms measure ROI ruthlessly and cut projects not delivering measurable returns. Once capabilities cross minimum adequacy, enterprises bundle them into workflows, capturing 10-100x productivity multiples. Real enterprise value drives deployment, not benchmark improvements.",
                    "Vertical application layers drive enterprise revenue disproportionately. Raw capability is commodity; embedded in context-specific workflows, it becomes 10x more defensible and valuable. A radiologist copilot is worth 10x a generic image model because it's embedded in enterprise processes and drives measurable revenue. Vertical integration creates defensible platforms.",
                    "Enterprise customers ruthlessly track cost-per-productivity. They won't overpay for marginal improvements, but pay premiums for capability crossing productivity thresholds. This market discipline ensures only productive capabilities scale. Market reality shows ruthless capital allocation toward measured ROI, not wasteful spending.",
                ],
            }
        };
        
        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            initializeAgent();
            document.getElementById('queryInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') sendQuery();
            });
        });
        
        function initializeAgent() {
            const greetingIndex = Math.floor(Math.random() * agentData.greeting.length);
            addMessage(agentData.greeting[greetingIndex], 'agent');
            loadBeliefs();
        }
        
        function addMessage(text, sender) {
            const chatContainer = document.getElementById('chatContainer');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}-message`;
            
            const label = document.createElement('div');
            label.className = `${sender}-label`;
            label.textContent = sender === 'user' ? 'YOU' : 'OPTIMIST';
            
            const content = document.createElement('div');
            content.textContent = text;
            
            const timestamp = document.createElement('div');
            timestamp.className = 'timestamp';
            timestamp.textContent = new Date().toLocaleTimeString();
            
            messageDiv.appendChild(label);
            messageDiv.appendChild(content);
            messageDiv.appendChild(timestamp);
            
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        
        function analyzeQuery(query) {
            const queryLower = query.toLowerCase();
            
            if (queryLower.includes('competition') || queryLower.includes('competitive') || queryLower.includes('market')) {
                return getRandomResponse('competition');
            } else if (queryLower.includes('pricing') || queryLower.includes('price') || queryLower.includes('wtp') || queryLower.includes('revenue')) {
                return getRandomResponse('pricing');
            } else if (queryLower.includes('scale') || queryLower.includes('inference') || queryLower.includes('cost') || queryLower.includes('economics')) {
                return getRandomResponse('scale');
            } else if (queryLower.includes('open') || queryLower.includes('startup') || queryLower.includes('modular')) {
                return getRandomResponse('open');
            } else if (queryLower.includes('enterprise') || queryLower.includes('adoption') || queryLower.includes('customer')) {
                return getRandomResponse('enterprise');
            } else {
                return generateCustomResponse(query);
            }
        }
        
        function getRandomResponse(category) {
            if (agentData.responses[category]) {
                const responses = agentData.responses[category];
                return responses[Math.floor(Math.random() * responses.length)];
            }
            return generateCustomResponse(category);
        }
        
        function generateCustomResponse(query) {
            const templates = [
                `Your question about '${query}' reveals how market competition creates powerful incentives for progress. Capital flows ruthlessly toward measured productivity. Competitive pressure drives efficiency. Winners emerge rapidly. The optimists focus on market incentives; the pessimists focus on governance failures.`,
                `That's thoughtful analysis of '${query}'. But market dynamics show competitive forces create better outcomes than centralized governance. Multiple teams racing toward solutions increase breakthrough odds exponentially while reducing time-to-impact.`,
                `'${query}' is precisely where market competition excels. Abundance of capital chasing high-return opportunities ensures rapid problem-solving. Messy? Yes. Efficient? Absolutely. This is how progress accelerates faster than skeptics predict.`,
            ];
            return templates[Math.floor(Math.random() * templates.length)];
        }
        
        function sendQuery() {
            const input = document.getElementById('queryInput');
            const query = input.value.trim();
            
            if (!query) return;
            
            addMessage(query, 'user');
            const response = analyzeQuery(query);
            
            setTimeout(() => {
                addMessage(response, 'agent');
            }, 300);
            
            input.value = '';
        }
        
        function queryTopic(topic) {
            document.getElementById('queryInput').value = topic;
            sendQuery();
        }
        
        function loadBeliefs() {
            const container = document.getElementById('beliefsContainer');
            Object.entries(agentData.beliefs).forEach(([key, value]) => {
                const item = document.createElement('div');
                item.className = 'belief-item';
                item.textContent = value;
                container.appendChild(item);
            });
        }
    </script>
</body>
</html>
"""


if __name__ == '__main__':
    print("=" * 60)
    print("THE OPTIMIST - AI AGENT")
    print("=" * 60)
    print("\nStarting Flask server on http://localhost:5001")
    print("Open your browser and navigate to http://localhost:5001")
    print("\nThe agent is calibrated to market dynamics and competitive efficiency.")
    print("Abundant capital + Competition = Progress")
    print("=" * 60)
    app.run(debug=True, port=5001)
