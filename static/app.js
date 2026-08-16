/* ==========================================================================
   Frontend Application Script
   App: Contract Risk Agent
   ========================================================================== */

let activeMode = 'b2b'; // 'b2b', 'eula', or 'sow'
let currentContract = null;
let currentTab = 'risks';
let chatHistory = [];

document.addEventListener('DOMContentLoaded', () => {
  fetchContractData(activeMode);
});

async function fetchContractData(mode) {
  try {
    const res = await fetch(`/api/contract/${mode}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    currentContract = await res.json();
    renderAll();
  } catch (err) {
    showToast('Failed to load contract data', 'error');
  }
}

function switchMode(mode) {
  activeMode = mode;
  document.getElementById('btn-mode-b2b').classList.toggle('active', mode === 'b2b');
  document.getElementById('btn-mode-eula').classList.toggle('active', mode === 'eula');
  document.getElementById('btn-mode-sow').classList.toggle('active', mode === 'sow');

  const subtitleText = document.getElementById('mode-subtitle-text');
  if (mode === 'b2b') {
    subtitleText.innerHTML = `<i class="fa-solid fa-building g-blue"></i> <strong>B2B Mode:</strong> Find risks and negotiate commercially reasonable middle ground.`;
    document.getElementById('tab-mode-feature-title').innerText = 'Win-Win Negotiation Engine';
    document.getElementById('footer-tagline').innerText = 'Find the agreement both sides can live with.';
  } else if (mode === 'eula') {
    subtitleText.innerHTML = `<i class="fa-solid fa-user-shield g-green"></i> <strong>EULA Mode:</strong> Understand what you're agreeing to and challenge provisions that undermine choice, transparency, privacy, property, or autonomy.`;
    document.getElementById('tab-mode-feature-title').innerText = 'Rights & Principles Lens';
    document.getElementById('footer-tagline').innerText = 'Understand what you\'re giving up before you agree.';
  } else {
    subtitleText.innerHTML = `<i class="fa-solid fa-compass-drafting g-purple"></i> <strong>SOW Mode:</strong> Translate Statement of Work (SOW) commitments into an actionable engineering delivery roadmap, milestone checklist, tech stack risks, and acceptance criteria.`;
    document.getElementById('tab-mode-feature-title').innerText = 'SOW Engineering Delivery Roadmap';
    document.getElementById('footer-tagline').innerText = 'Know exactly what needs to be built, tested, and delivered for project success.';
  }

  fetchContractData(mode);
}

function switchTab(tab) {
  currentTab = tab;
  document.getElementById('tab-btn-risks').classList.toggle('active', tab === 'risks');
  document.getElementById('tab-btn-feature').classList.toggle('active', tab === 'feature');
  document.getElementById('tab-btn-challenge').classList.toggle('active', tab === 'challenge');
  document.getElementById('tab-btn-text').classList.toggle('active', tab === 'text');

  document.getElementById('tab-content-risks').style.display = tab === 'risks' ? 'block' : 'none';
  document.getElementById('tab-content-feature').style.display = tab === 'feature' ? 'block' : 'none';
  document.getElementById('tab-content-challenge').style.display = tab === 'challenge' ? 'block' : 'none';
  document.getElementById('tab-content-text').style.display = tab === 'text' ? 'block' : 'none';

  if (tab === 'challenge') {
    loadChallengeNext();
  }
}

// Master Render
function renderAll() {
  if (!currentContract) return;

  renderContractMetadata();
  renderAgentActivity();
  renderHealthScore();
  renderTopIssues();
  renderRiskCards('all');
  renderModeSpecificFeature();
  renderFullContractText();
  updateBadges();
}

// 1. Ingestion Metadata
function renderContractMetadata() {
  const meta = currentContract.metadata || {};
  document.getElementById('contract-doc-title').innerText = currentContract.title || 'Contract Document';

  const grid = document.getElementById('doc-meta-grid');
  grid.innerHTML = `
    <div class="doc-meta-item"><i class="fa-solid fa-tag g-blue"></i> <strong>Type:</strong> ${meta.type || 'N/A'}</div>
    <div class="doc-meta-item"><i class="fa-solid fa-building g-purple"></i> <strong>Parties:</strong> ${meta.parties || 'N/A'}</div>
    <div class="doc-meta-item"><i class="fa-solid fa-scale-balanced g-green"></i> <strong>Law:</strong> ${meta.jurisdiction || 'N/A'}</div>
    <div class="doc-meta-item"><i class="fa-solid fa-file-lines g-yellow"></i> <strong>Length:</strong> ${meta.length || 'N/A'}</div>
    <div class="doc-meta-item"><i class="fa-solid fa-calendar g-blue"></i> <strong>Date:</strong> ${meta.date || 'N/A'}</div>
    <div class="doc-meta-item"><i class="fa-solid fa-dollar-sign g-green"></i> <strong>Value:</strong> ${meta.annual_value || 'N/A'}</div>
  `;
}

// 2. Agent Activity Panel
function renderAgentActivity() {
  const steps = currentContract.agent_activity || [];
  const container = document.getElementById('agent-steps-list');
  container.innerHTML = steps.map(s => `
    <div class="agent-step-item">
      <i class="fa-solid fa-circle-check g-green"></i>
      <span>${s.text}</span>
    </div>
  `).join('');
}

// 3. Health Score & Score Card
function renderHealthScore() {
  const health = currentContract.health || { score: 60, status_label: '60/100', reasonable_count: 10, discuss_count: 5, high_risk_count: 2, counsel_questions_count: 1 };
  document.getElementById('health-score-num').innerText = health.score;
  document.getElementById('health-status-label').innerText = health.status_label;

  const circle = document.getElementById('health-circle');
  let color = 'var(--g-green)';
  if (health.score < 50) color = 'var(--g-red)';
  else if (health.score < 70) color = 'var(--g-yellow)';

  circle.style.background = `conic-gradient(${color} 0% ${health.score}%, var(--g-gray-200) ${health.score}% 100%)`;

  const pills = document.getElementById('health-breakdown-pills');
  pills.innerHTML = `
    <span class="badge badge-success">🟢 ${health.reasonable_count} Reasonable</span>
    <span class="badge badge-warning">🟡 ${health.discuss_count} To Discuss</span>
    <span class="badge badge-danger">🔴 ${health.high_risk_count} High Risk</span>
    <span class="badge badge-info">🔵 ${health.counsel_questions_count} Counsel</span>
  `;

  // Leverage vs Impact vs Engineering Score Card
  const box = document.getElementById('score-meta-box');
  if (activeMode === 'b2b') {
    const neg = currentContract.negotiation_score || { position: 'Customer Position', leverage: 70, risk_score: 50, compromise_potential: 80, walkaway_consideration: 'N/A' };
    box.innerHTML = `
      <div style="font-weight:700; margin-bottom:6px; color:var(--g-blue);"><i class="fa-solid fa-handshake"></i> ${neg.position}</div>
      <div style="display:flex; justify-content:space-between; margin-bottom:8px; font-size:13px;">
        <span>Leverage: <strong>${neg.leverage}%</strong></span>
        <span>Exposure: <strong>${neg.risk_score}%</strong></span>
        <span>Compromise: <strong>${neg.compromise_potential}%</strong></span>
      </div>
      <div style="font-size:12px; color:var(--g-gray-700); background:var(--g-gray-50); padding:8px; border-radius:var(--radius-sm);">
        <strong>Walk-Away Note:</strong> ${neg.walkaway_consideration}
      </div>
    `;
  } else if (activeMode === 'eula') {
    const imp = currentContract.user_impact_score || { impact_level: 'High Consumer Rights Impact', transparency: 'Standard Form', ability_to_negotiate: 'Adhesion Contract', recommended_action: 'Opt out of binding arbitration.' };
    box.innerHTML = `
      <div style="font-weight:700; margin-bottom:6px; color:var(--g-green);"><i class="fa-solid fa-user-shield"></i> ${imp.impact_level}</div>
      <div style="font-size:13px; margin-bottom:6px;">Negotiability: <strong>${imp.ability_to_negotiate}</strong></div>
      <div style="font-size:12px; color:var(--g-gray-700); background:var(--g-gray-50); padding:8px; border-radius:var(--radius-sm);">
        <strong>Recommended Action:</strong> ${imp.recommended_action}
      </div>
    `;
  } else {
    const eng = currentContract.engineering_score || { readiness_level: 'Engineering Execution Ready', milestone_count: 4, deliverable_count: 10, acceptance_criteria_count: 8, scope_creep_risk: 'Medium' };
    box.innerHTML = `
      <div style="font-weight:700; margin-bottom:6px; color:var(--g-purple);"><i class="fa-solid fa-compass-drafting"></i> ${eng.readiness_level}</div>
      <div style="display:flex; justify-content:space-between; margin-bottom:8px; font-size:13px;">
        <span>Milestones: <strong>${eng.milestone_count}</strong></span>
        <span>Deliverables: <strong>${eng.deliverable_count}</strong></span>
        <span>Criteria: <strong>${eng.acceptance_criteria_count}</strong></span>
      </div>
      <div style="font-size:12px; color:var(--g-gray-700); background:var(--g-gray-50); padding:8px; border-radius:var(--radius-sm);">
        <strong>Scope Risk:</strong> ${eng.scope_creep_risk}
      </div>
    `;
  }
}

// 4. Top Issues
function renderTopIssues() {
  const container = document.getElementById('top-issues-list');
  const issues = currentContract.top_issues || [];

  if (!issues.length) {
    container.innerHTML = `<span style="font-size:12px; color:var(--g-gray-500);">No critical issues flagged.</span>`;
    return;
  }

  container.innerHTML = issues.map(iss => `
    <div class="top-issue-item" style="display:flex; justify-content:space-between; align-items:center; font-size:12px; background:var(--g-gray-50); padding:6px 10px; border-radius:4px; cursor:pointer;" onclick="scrollToClause('${iss.id}')">
      <span style="font-weight:600; color:var(--g-gray-900);">${iss.title}</span>
      <span class="badge ${iss.severity === 'High' ? 'badge-danger' : 'badge-warning'}">${iss.severity}</span>
    </div>
  `).join('');
}

// 5. Risk Cards Matrix
function renderRiskCards(filter = 'all') {
  const container = document.getElementById('risk-cards-container');
  let clauses = currentContract.clauses || [];

  if (filter !== 'all') {
    clauses = clauses.filter(c => c.risk_level.toLowerCase() === filter.toLowerCase());
  }

  if (!clauses.length) {
    container.innerHTML = `<div class="dash-card" style="text-align:center; padding:32px; color:var(--g-gray-500);">No clauses match the selected filter.</div>`;
    return;
  }

  container.innerHTML = clauses.map(c => {
    let riskClass = 'risk-card';
    if (c.risk_level === 'High') riskClass += ' high-risk';
    else if (c.risk_level === 'Medium') riskClass += ' med-risk';
    else riskClass += ' low-risk';

    return `
      <div class="${riskClass}" id="clause-card-${c.id}">
        <div class="risk-card-header">
          <div>
            <span class="section-kicker">${c.category} · ${c.section_ref}</span>
            <h3 class="risk-card-title">${c.title}</h3>
          </div>
          <div style="display:flex; gap:8px; align-items:center;">
            <span class="badge ${c.risk_level === 'High' ? 'badge-danger' : c.risk_level === 'Medium' ? 'badge-warning' : 'badge-success'}">
              ${c.risk_level} Risk (${c.risk_score || 50}/100)
            </span>
            <button class="btn-action" onclick="openSimForClause('${c.id}')" title="Simulate Negotiation">
              <i class="fa-solid fa-comments g-blue"></i>
            </button>
          </div>
        </div>

        <div class="quote-box">
          <i class="fa-solid fa-quote-left" style="color:var(--g-gray-400); margin-right:4px;"></i> "${c.contract_quote}"
        </div>

        <div class="analysis-grid">
          <div class="analysis-box">
            <div class="analysis-box-title"><i class="fa-solid fa-circle-info g-blue"></i> Plain English Meaning</div>
            <p>${c.plain_english}</p>
          </div>
          <div class="analysis-box">
            <div class="analysis-box-title"><i class="fa-solid fa-triangle-exclamation g-red"></i> Why It Matters</div>
            <p>${c.why_it_matters}</p>
          </div>
        </div>

        <div class="analysis-grid">
          <div class="analysis-box">
            <div class="analysis-box-title"><i class="fa-solid fa-scale-balanced g-green"></i> Legal / Market Context</div>
            <p>${c.law_may_say}</p>
          </div>
          <div class="analysis-box">
            <div class="analysis-box-title"><i class="fa-solid fa-lightbulb g-yellow"></i> Negotiation Recommendation</div>
            <p>${c.negotiation_recommendation}</p>
          </div>
        </div>

        ${c.diff ? `
          <div class="diff-container">
            <div style="font-size:12px; font-weight:700; text-transform:uppercase; margin-bottom:8px; color:var(--g-gray-700);">
              <i class="fa-solid fa-code-compare g-purple"></i> Proposed Balanced Redline
            </div>
            <div class="diff-original"><strong>- Original:</strong> ${c.diff.original}</div>
            <div class="diff-proposed"><strong>+ Proposed Redline:</strong> ${c.diff.proposed}</div>
            <div style="font-size:12px; color:var(--g-gray-700); margin-top:6px;"><strong>Rationale:</strong> ${c.diff.explanation}</div>
          </div>
        ` : ''}

      </div>
    `;
  }).join('');
}

function filterRiskCards(filter) {
  renderRiskCards(filter);
}

function scrollToClause(clauseId) {
  switchTab('risks');
  setTimeout(() => {
    const el = document.getElementById(`clause-card-${clauseId}`);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      el.style.boxShadow = '0 0 0 3px var(--g-blue)';
      setTimeout(() => el.style.boxShadow = '', 2000);
    }
  }, 100);
}

// 6. Mode Specific Features
function renderModeSpecificFeature() {
  const container = document.getElementById('mode-specific-feature-container');

  if (activeMode === 'b2b') {
    renderB2BWinWinFeature(container);
  } else if (activeMode === 'eula') {
    renderEULARightsFeature(container);
  } else {
    renderSOWRoadmapFeature(container);
  }
}

function renderB2BWinWinFeature(container) {
  const clauses = currentContract.clauses || [];
  container.innerHTML = `
    <div class="dash-card" style="margin-bottom:20px;">
      <h2 style="font-size:18px; font-weight:700; margin-bottom:12px;"><i class="fa-solid fa-handshake g-blue"></i> Win-Win Commercial Negotiation Matrix</h2>
      <p style="font-size:13px; color:var(--g-gray-700); margin-bottom:16px;">
        Maps your legitimate concerns against the counterparty's operational priorities to uncover balanced middle-ground positions.
      </p>
      <div style="display:flex; flex-direction:column; gap:16px;">
        ${clauses.map(c => c.middle_ground ? `
          <div style="background:var(--g-gray-50); border:1px solid var(--g-gray-200); border-radius:var(--radius-sm); padding:16px;">
            <h3 style="font-size:15px; font-weight:700; margin-bottom:10px;">${c.title}</h3>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:13px; margin-bottom:12px;">
              <div style="background:#fff; padding:10px; border-radius:4px; border-left:3px solid var(--g-blue);">
                <strong>Your Concern:</strong> ${c.middle_ground.your_concern}
              </div>
              <div style="background:#fff; padding:10px; border-radius:4px; border-left:3px solid var(--g-purple);">
                <strong>Their Likely Concern:</strong> ${c.middle_ground.their_concern}
              </div>
            </div>
            <div style="background:var(--g-green-light); padding:12px; border-radius:4px; font-size:13px; margin-bottom:10px; color:#166534;">
              <strong><i class="fa-solid fa-circle-check"></i> Reasonable Compromise:</strong> ${c.middle_ground.compromise_proposal}
            </div>
            <div style="background:#fff; padding:12px; border-radius:4px; font-size:13px; border:1px dashed var(--g-gray-300);">
              <strong>Ready-to-Send Email Draft:</strong>
              <p style="font-style:italic; margin-top:4px; color:var(--g-gray-700);">${c.middle_ground.suggested_response}</p>
            </div>
          </div>
        ` : '').join('')}
      </div>
    </div>
  `;
}

function renderEULARightsFeature(container) {
  const principles = currentContract.rights_principles || [];
  const optOut = currentContract.arbitration_opt_out || {};

  container.innerHTML = `
    <div class="dash-card" style="margin-bottom:20px;">
      <h2 style="font-size:18px; font-weight:700; margin-bottom:12px;"><i class="fa-solid fa-landmark g-green"></i> Rights & Principles Lens</h2>
      <p style="font-size:13px; color:var(--g-gray-700); margin-bottom:16px;">
        Evaluates consumer adhesion contracts through the principles of autonomy, meaningful consent, property, and procedural fairness.
      </p>
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:16px; margin-bottom:24px;">
        ${principles.map(p => `
          <div style="background:var(--g-gray-50); border:1px solid var(--g-gray-200); border-radius:var(--radius-sm); padding:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="font-weight:700; font-size:14px;">${p.principle}</span>
              <span class="badge ${p.assessment === 'Violated' || p.assessment === 'Deprived' ? 'badge-danger' : 'badge-warning'}">${p.assessment}</span>
            </div>
            <div style="font-size:12px; color:var(--g-gray-500); margin-bottom:8px;"><strong>Source:</strong> ${p.source}</div>
            <p style="font-size:13px; color:var(--g-gray-700);">${p.detail}</p>
          </div>
        `).join('')}
      </div>

      <div style="background:var(--g-yellow-light); border:1px solid var(--g-yellow); border-radius:var(--radius-sm); padding:20px;">
        <h3 style="font-size:16px; font-weight:700; color:#b06000; margin-bottom:8px;">
          <i class="fa-solid fa-envelope-open-text"></i> 30-Day Binding Arbitration Opt-Out Guide
        </h3>
        <p style="font-size:13px; margin-bottom:12px;">${optOut.instructions}</p>
        <div style="font-size:13px; background:#fff; padding:12px; border-radius:4px; margin-bottom:12px;">
          <div><strong>Physical Notice Address:</strong> ${optOut.opt_out_address}</div>
          <div><strong>Email Notice:</strong> ${optOut.email_opt_out}</div>
        </div>
        <button class="btn-action btn-primary" onclick="copyOptOutLetter()">
          <i class="fa-solid fa-copy"></i> Copy Formal Opt-Out Letter
        </button>
      </div>
    </div>
  `;
}

function renderSOWRoadmapFeature(container) {
  const milestones = currentContract.milestones || [];

  container.innerHTML = `
    <div class="dash-card" style="margin-bottom:20px;">
      <h2 style="font-size:18px; font-weight:700; margin-bottom:12px;"><i class="fa-solid fa-compass-drafting g-purple"></i> SOW Technical Milestone Delivery Matrix</h2>
      <p style="font-size:13px; color:var(--g-gray-700); margin-bottom:16px;">
        Translates contractual commitments into structured engineering phases, leads, and verifiable acceptance criteria.
      </p>

      <!-- SOW Copilot Q&A Bar -->
      <div style="background:var(--g-purple-light); padding:16px; border-radius:var(--radius-sm); margin-bottom:24px; border:1px solid #d8b4fe;">
        <div style="font-size:13px; font-weight:700; color:var(--g-purple); margin-bottom:8px;">
          <i class="fa-solid fa-robot"></i> Ask SOW Copilot
        </div>
        <div style="display:flex; gap:8px;">
          <input type="text" id="sow-qa-input" placeholder="Ask e.g. 'What is the penalty for missing cutover SLA?' or 'What are the Phase 1 deliverables?'" style="flex:1; padding:8px 14px; border:1px solid var(--g-gray-300); border-radius:var(--radius-sm); font-size:13px; outline:none;" onkeydown="if(event.key==='Enter') askSowQuestion()">
          <button class="btn-action btn-primary" onclick="askSowQuestion()">
            <i class="fa-solid fa-paper-plane"></i> Ask
          </button>
        </div>
        <div id="sow-qa-answer-box" style="display:none; margin-top:12px; background:#fff; padding:12px; border-radius:4px; font-size:13px;"></div>
      </div>

      <!-- Milestone Phases -->
      <div style="display:flex; flex-direction:column; gap:16px;">
        ${milestones.map((m, pIdx) => `
          <div style="background:#fff; border:1px solid var(--g-gray-200); border-radius:var(--radius-sm); padding:20px; box-shadow:var(--shadow-sm);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <div>
                <span class="badge badge-purple" style="margin-bottom:4px;">${m.weeks} · Fee: ${m.fee}</span>
                <h3 style="font-size:16px; font-weight:700;">${m.title}</h3>
                <span style="font-size:12px; color:var(--g-gray-500);"><i class="fa-solid fa-user-gear"></i> Assigned Lead: <strong>${m.lead}</strong></span>
              </div>
            </div>

            <div style="margin-bottom:14px;">
              <strong style="font-size:13px; text-transform:uppercase; color:var(--g-gray-700);">Key Deliverables:</strong>
              <ul style="margin-left:20px; font-size:13px; margin-top:4px; color:var(--g-gray-700);">
                ${m.deliverables.map(d => `<li>${d}</li>`).join('')}
              </ul>
            </div>

            <div>
              <strong style="font-size:13px; text-transform:uppercase; color:var(--g-gray-700);">Acceptance Criteria Checklist:</strong>
              <div style="display:flex; flex-direction:column; gap:8px; margin-top:6px;">
                ${m.acceptance_criteria.map((c, cIdx) => `
                  <div style="display:flex; justify-content:space-between; align-items:center; background:var(--g-gray-50); padding:8px 12px; border-radius:4px; font-size:13px;">
                    <span>${c.text}</span>
                    <button class="btn-action" style="padding:4px 10px; font-size:11px;" onclick="toggleAcceptance(${pIdx}, ${cIdx})">
                      ${c.status === 'Passed' ? '🟢 Passed' : c.status === 'In Testing' ? '🟡 In Testing' : '⚪ Pending'}
                    </button>
                  </div>
                `).join('')}
              </div>
            </div>

          </div>
        `).join('')}
      </div>

    </div>
  `;
}

function toggleAcceptance(pIdx, cIdx) {
  if (!currentContract.milestones) return;
  const item = currentContract.milestones[pIdx].acceptance_criteria[cIdx];
  if (item.status === 'Pending') item.status = 'In Testing';
  else if (item.status === 'In Testing') item.status = 'Passed';
  else item.status = 'Pending';
  renderModeSpecificFeature();
}

async function askSowQuestion() {
  const input = document.getElementById('sow-qa-input');
  const query = input.value.trim();
  if (!query) return;

  const box = document.getElementById('sow-qa-answer-box');
  box.style.display = 'block';
  box.innerHTML = `<i class="fa-solid fa-spinner fa-spin g-purple"></i> Analyzing SOW text...`;

  try {
    const res = await fetch('/api/sow-ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: query })
    });
    const data = await res.json();
    box.innerHTML = `
      <div style="font-weight:700; color:var(--g-purple); margin-bottom:4px;"><i class="fa-solid fa-robot"></i> SOW Copilot Answer:</div>
      <p style="margin-bottom:8px;">${data.answer}</p>
      ${data.sources && data.sources.length ? `<div style="font-size:11px; color:var(--g-gray-500);"><strong>Sources:</strong> ${data.sources.join(', ')}</div>` : ''}
    `;
  } catch (err) {
    box.innerHTML = `<span style="color:var(--g-red);">Failed to fetch answer.</span>`;
  }
}

// 7. Full Text & Global Challenge
function renderFullContractText() {
  document.getElementById('full-contract-raw-text').innerText = currentContract.full_text || 'No raw contract text loaded.';
}

async function loadChallengeNext() {
  const container = document.getElementById('challenge-next-card-content');
  container.innerHTML = `<div style="text-align:center; padding:20px;"><i class="fa-solid fa-spinner fa-spin g-blue"></i> Computing priority...</div>`;

  try {
    const res = await fetch('/api/next-challenge', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ type: activeMode })
    });
    const data = await res.json();
    container.innerHTML = `
      <div style="background:var(--g-gray-50); border:1px solid var(--g-gray-200); border-radius:var(--radius-sm); padding:20px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <h3 style="font-size:18px; font-weight:700; color:var(--g-gray-900);">${data.title}</h3>
          <span class="badge badge-danger">Priority Score: ${data.priority_score}/100</span>
        </div>
        <div class="quote-box" style="margin-bottom:14px;">"${data.contract_quote}"</div>
        <div style="margin-bottom:12px; font-size:13px;"><strong>Why Challenge This First:</strong> ${data.why_challenge_now}</div>
        <div style="background:#fff; padding:14px; border-radius:var(--radius-sm); border:1px solid var(--g-gray-300); margin-bottom:16px;">
          <strong style="font-size:13px; color:var(--g-blue);"><i class="fa-solid fa-envelope"></i> Recommended Challenge Message:</strong>
          <p style="font-size:13px; font-style:italic; margin-top:4px;">${data.ready_to_send_proposal}</p>
        </div>
        <button class="btn-action btn-primary" onclick="scrollToClause('${data.clause_id}')">
          <i class="fa-solid fa-arrow-right"></i> View Full Redline Diff
        </button>
      </div>
    `;
  } catch (err) {
    container.innerHTML = `<span style="color:var(--g-red);">Failed to calculate challenge.</span>`;
  }
}

function updateBadges() {
  const count = (currentContract.clauses || []).length;
  document.getElementById('badge-risk-count').innerText = count;
}

// 8. Modal & Paste Handler
function openPasteModal() {
  document.getElementById('paste-modal').classList.add('open');
  document.getElementById('paste-contract-mode').value = activeMode;
}

function closePasteModal() {
  document.getElementById('paste-modal').classList.remove('open');
}

async function submitPastedContract() {
  const textarea = document.getElementById('paste-textarea');
  const modeSelect = document.getElementById('paste-contract-mode');
  const text = textarea.value.trim();
  const selectedMode = modeSelect.value;

  if (!text) {
    showToast('Please paste some contract text first', 'error');
    return;
  }

  const btn = document.getElementById('btn-analyze-paste');
  const originalBtnHtml = btn.innerHTML;
  btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...`;
  btn.disabled = true;

  try {
    const res = await fetch('/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text, type: selectedMode })
    });

    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      throw new Error(errData.detail || `Server returned ${res.status}`);
    }

    const analyzedContract = await res.json();
    currentContract = analyzedContract;
    activeMode = analyzedContract.mode || selectedMode;

    // Update Mode Switcher UI
    document.getElementById('btn-mode-b2b').classList.toggle('active', activeMode === 'b2b');
    document.getElementById('btn-mode-eula').classList.toggle('active', activeMode === 'eula');
    document.getElementById('btn-mode-sow').classList.toggle('active', activeMode === 'sow');

    renderAll();
    closePasteModal();
    textarea.value = '';
    showToast('Contract analyzed successfully!', 'success');
  } catch (err) {
    showToast(`Failed to analyze pasted contract: ${err.message}`, 'error');
  } finally {
    btn.innerHTML = originalBtnHtml;
    btn.disabled = false;
  }
}

async function handleFileUpload(event) {
  const file = event.target.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append('file', file);
  formData.append('contract_type', activeMode);

  showToast('Uploading and parsing contract...', 'info');

  try {
    const res = await fetch(`/api/upload?contract_type=${activeMode}`, {
      method: 'POST',
      body: formData
    });
    if (!res.ok) throw new Error('Upload failed');
    currentContract = await res.json();
    renderAll();
    showToast('File analyzed successfully!', 'success');
  } catch (err) {
    showToast('Failed to analyze uploaded file', 'error');
  }
}

// 9. Negotiation Simulator Drawer
function openSimulatorDrawer() {
  document.getElementById('simulator-drawer').classList.add('open');
}

function closeSimulatorDrawer() {
  document.getElementById('simulator-drawer').classList.remove('open');
}

function openSimForClause(clauseId) {
  openSimulatorDrawer();
  const clause = (currentContract.clauses || []).find(c => c.id === clauseId);
  if (clause) {
    const input = document.getElementById('sim-chat-input');
    input.value = `Regarding ${clause.title}: Would you agree to make this liability cap mutual at 12 months fees?`;
  }
}

async function sendSimMessage() {
  const input = document.getElementById('sim-chat-input');
  const msg = input.value.trim();
  if (!msg) return;

  const chatContainer = document.getElementById('sim-chat-messages');

  // Add User Bubble
  chatContainer.innerHTML += `<div class="chat-bubble user">${msg}</div>`;
  input.value = '';
  chatContainer.scrollTop = chatContainer.scrollHeight;

  // Add Loading Bubble
  const loadingId = `load-${Date.now()}`;
  chatContainer.innerHTML += `<div class="chat-bubble counterparty" id="${loadingId}"><i class="fa-solid fa-spinner fa-spin"></i> Legal counsel evaluating...</div>`;
  chatContainer.scrollTop = chatContainer.scrollHeight;

  try {
    const res = await fetch('/api/counterparty-simulate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: msg, type: activeMode, history: chatHistory })
    });
    const data = await res.json();

    const loadEl = document.getElementById(loadingId);
    if (loadEl) loadEl.remove();

    chatContainer.innerHTML += `
      <div class="chat-bubble counterparty">
        <div style="font-size:11px; font-weight:700; margin-bottom:4px;">${data.status_badge}</div>
        <p>${data.reply}</p>
        <div style="font-size:11px; color:var(--g-gray-500); margin-top:4px;"><strong>Suggested Move:</strong> ${data.recommended_action}</div>
      </div>
    `;
    chatHistory.push({ user: msg, counterparty: data.reply });
    chatContainer.scrollTop = chatContainer.scrollHeight;
  } catch (err) {
    const loadEl = document.getElementById(loadingId);
    if (loadEl) loadEl.innerHTML = `<span style="color:var(--g-red);">Simulation error.</span>`;
  }
}

// 10. Utilities & Reset
async function resetToDefaults() {
  try {
    await fetch('/api/reset', { method: 'POST' });
    fetchContractData(activeMode);
    showToast('Reset to default reference contracts', 'success');
  } catch (err) {
    showToast('Failed to reset', 'error');
  }
}

function copyOptOutLetter() {
  const letter = `To: NovaSmart Technologies Corp., Attn: Legal Arbitration Opt-Out
Date: ${new Date().toLocaleDateString()}

RE: FORMAL NOTICE OF ARBITRATION OPT-OUT

I hereby give formal written notice pursuant to Section 21 of the NovaSmart Terms of Service that I opt out of and reject the mandatory binding arbitration agreement and class action waiver.

Account Email: user@example.com
Sincerely,
[Your Name]`;
  navigator.clipboard.writeText(letter);
  showToast('Opt-out letter copied to clipboard!', 'success');
}

function showToast(message, type = 'info') {
  const container = document.getElementById('toast-container');
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<i class="fa-solid ${type === 'error' ? 'fa-circle-xmark' : type === 'success' ? 'fa-circle-check' : 'fa-circle-info'}"></i> <span>${message}</span>`;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
}
