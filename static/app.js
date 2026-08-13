/* ==========================================================================
   Frontend Application Script
   App: Contract Risk Agent
   ========================================================================== */

let activeMode = 'b2b'; // 'b2b' or 'eula'
let currentContract = null;
let currentTab = 'risks';
let demoTourActive = false;
let currentDemoStep = 1;
const TOTAL_DEMO_STEPS = 11;

let chatHistory = [];

document.addEventListener('DOMContentLoaded', () => {
  fetchContractData(activeMode);
});

async function fetchContractData(mode) {
  try {
    const res = await fetch(`/api/contract/${mode}`);
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

  const subtitleText = document.getElementById('mode-subtitle-text');
  if (mode === 'b2b') {
    subtitleText.innerHTML = `<i class="fa-solid fa-building g-blue"></i> <strong>B2B Mode:</strong> Find risks and negotiate commercially reasonable middle ground.`;
    document.getElementById('tab-mode-feature-title').innerText = 'Win-Win Negotiation Engine';
    document.getElementById('footer-tagline').innerText = 'Find the agreement both sides can live with.';
  } else {
    subtitleText.innerHTML = `<i class="fa-solid fa-user-shield g-green"></i> <strong>EULA Mode:</strong> Understand what you're agreeing to and challenge provisions that undermine choice, transparency, privacy, property, or autonomy.`;
    document.getElementById('tab-mode-feature-title').innerText = 'Rights & Principles Lens';
    document.getElementById('footer-tagline').innerText = 'Understand what you\'re giving up before you agree.';
  }

  fetchContractData(mode);
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
  const meta = currentContract.metadata;
  document.getElementById('contract-doc-title').innerText = currentContract.title;

  const grid = document.getElementById('doc-meta-grid');
  grid.innerHTML = `
    <span><i class="fa-solid fa-tag"></i> ${meta.type}</span>
    <span><i class="fa-solid fa-building"></i> ${meta.parties}</span>
    <span><i class="fa-solid fa-scale-balanced"></i> ${meta.jurisdiction}</span>
    <span><i class="fa-solid fa-file-lines"></i> ${meta.length}</span>
    <span><i class="fa-solid fa-calendar"></i> ${meta.date}</span>
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
  const health = currentContract.health;
  document.getElementById('health-score-num').innerText = health.score;
  document.getElementById('health-status-label').innerText = health.status_label;

  const circle = document.getElementById('health-circle');
  circle.style.background = `conic-gradient(var(--g-green) 0% ${health.score}%, var(--g-gray-200) ${health.score}% 100%)`;

  const pills = document.getElementById('health-breakdown-pills');
  pills.innerHTML = `
    <span class="badge badge-success">🟢 ${health.reasonable_count} Reasonable</span>
    <span class="badge badge-warning">🟡 ${health.discuss_count} To Discuss</span>
    <span class="badge badge-danger">🔴 ${health.high_risk_count} High Risk</span>
    <span class="badge badge-info">🔵 ${health.counsel_questions_count} Counsel Questions</span>
  `;

  // Leverage vs Impact Score Card
  const box = document.getElementById('score-meta-box');
  if (activeMode === 'b2b') {
    const neg = currentContract.negotiation_score;
    box.innerHTML = `
      <div style="font-weight:700; margin-bottom:4px;"><i class="fa-solid fa-handshake g-blue"></i> ${neg.position}</div>
      <div style="display:flex; gap:12px; margin-bottom:6px;">
        <span>Leverage: <strong>${neg.leverage}%</strong></span>
        <span>Risk Exposure: <strong>${neg.risk_score}%</strong></span>
        <span>Compromise: <strong>${neg.compromise_potential}%</strong></span>
      </div>
      <div class="sub-text"><strong>Walk-Away Note:</strong> ${neg.walkaway_consideration}</div>
    `;
  } else {
    const imp = currentContract.user_impact_score;
    box.innerHTML = `
      <div style="font-weight:700; margin-bottom:4px;"><i class="fa-solid fa-user-shield g-green"></i> ${imp.impact_level}</div>
      <div style="margin-bottom:4px;">Transparency: <strong>${imp.transparency}</strong> | Direct Negotiation: <strong>${imp.ability_to_negotiate}</strong></div>
      <div class="sub-text"><strong>Recommended Action:</strong> ${imp.recommended_action}</div>
    `;
  }
}

// 4. Top Issues
function renderTopIssues() {
  const container = document.getElementById('top-issues-list');
  const issues = currentContract.top_issues || [];

  container.innerHTML = issues.map(iss => `
    <div class="top-issue-item" onclick="scrollToClause('${iss.id}')">
      <span>${iss.title}</span>
      <span class="badge badge-danger">${iss.severity} Risk</span>
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

  container.innerHTML = clauses.map(c => {
    let cardClass = 'risk-card';
    if (c.risk_level === 'Medium') cardClass += ' med-risk';
    if (c.risk_level === 'Reasonable') cardClass += ' low-risk';

    return `
      <div class="${cardClass}" id="clause-card-${c.id}">
        <div class="risk-card-header">
          <div>
            <span class="section-kicker">${c.category.toUpperCase()} · ${c.section_ref}</span>
            <h3 class="risk-card-title">${c.title}</h3>
          </div>
          <span class="badge ${c.risk_level === 'High' ? 'badge-danger' : c.risk_level === 'Medium' ? 'badge-warning' : 'badge-success'}">
            Risk: ${c.risk_level}
          </span>
        </div>

        <p style="font-size:13px; font-weight:600; color:var(--g-gray-900); margin-top:6px;">
          ${c.plain_english}
        </p>

        <!-- Risk Allocation Bar -->
        <div class="risk-allocation-bar">
          <div class="allocation-track">
            <div class="alloc-you" style="width: ${c.allocation.you}%;"></div>
            <div class="alloc-cp" style="width: ${c.allocation.counterparty}%;"></div>
          </div>
          <div class="allocation-labels">
            <span>You: ${c.allocation.you}% Risk</span>
            <span>Counterparty: ${c.allocation.counterparty}% Risk</span>
          </div>
        </div>

        <p class="sub-text" style="margin-bottom:8px;"><strong>Why It Matters:</strong> ${c.why_it_matters}</p>

        <div class="clause-quote-box">
          <i class="fa-solid fa-quote-left"></i> Contract Quote: "${c.contract_quote}"
        </div>

        <div class="risk-card-actions">
          ${activeMode === 'b2b' ? `
            <button class="btn btn-sm btn-primary" onclick="openMakeFairModal('${c.id}')">
              <i class="fa-solid fa-scale-unbalanced-flip"></i> Make This Fair
            </button>
            <button class="btn btn-sm btn-secondary" onclick="openDiffModal('${c.id}')">
              <i class="fa-solid fa-code-compare"></i> Redline Compromise
            </button>
            <button class="btn btn-sm btn-outline" onclick="openSimulateDrawer('${c.id}')">
              <i class="fa-solid fa-comments"></i> Simulate Negotiation
            </button>
          ` : `
            <button class="btn btn-sm btn-primary" onclick="switchTab('mode-feature')">
              <i class="fa-solid fa-scale-unbalanced"></i> View Rights Lens
            </button>
            <button class="btn btn-sm btn-secondary" onclick="openDiffModal('${c.id}')">
              <i class="fa-solid fa-file-pen"></i> Consumer Counter
            </button>
            <button class="btn btn-sm btn-outline" onclick="askCounselAction()">
              <i class="fa-solid fa-user-doctor"></i> Ask Counsel
            </button>
          `}
        </div>
      </div>
    `;
  }).join('');
}

function filterRiskCards(filter, btn) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderRiskCards(filter);
}

function scrollToClause(clauseId) {
  switchTab('risks');
  const elem = document.getElementById(`clause-card-${clauseId}`);
  if (elem) {
    elem.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
}

// 6. Render Mode-Specific Feature (Win-Win Negotiation OR Rights Lens)
function renderModeSpecificFeature() {
  const container = document.getElementById('mode-feature-container');

  if (activeMode === 'b2b') {
    const clauses = currentContract.clauses.filter(c => c.middle_ground);
    container.innerHTML = clauses.map(c => `
      <div class="feature-card" style="margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <h3><i class="fa-solid fa-handshake g-blue"></i> ${c.title}</h3>
          <span class="badge badge-info">Win-Win Middle Ground</span>
        </div>

        <div class="winwin-grid">
          <div><strong>Your Concern:</strong> ${c.middle_ground.your_concern}</div>
          <div><strong>Their Likely Concern:</strong> ${c.middle_ground.their_concern}</div>
          <div style="grid-column: span 2;"><strong>Shared Objective:</strong> ${c.middle_ground.shared_objective}</div>
        </div>

        <div class="suggested-response-box">
          <strong>Suggested Response:</strong>
          <p style="margin-top:4px;">${c.middle_ground.suggested_response}</p>
        </div>
      </div>
    `).join('');
  } else {
    const clauses = currentContract.clauses.filter(c => c.principles_lens);
    container.innerHTML = clauses.map(c => `
      <div class="feature-card" style="margin-bottom:16px; border-left: 4px solid #a855f7;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <h3><i class="fa-solid fa-landmark g-purple"></i> ${c.title}</h3>
          <span class="principles-badge">${c.principles_lens.principle} Lens</span>
        </div>

        <p style="font-size:12px; color:var(--g-gray-700); margin:8px 0;">
          <strong>Historical Source Material Context:</strong> ${c.principles_lens.historical_context}
        </p>

        <div style="background-color:#f3e8ff; padding:12px; border-radius:8px; font-size:13px; margin:8px 0; color:#581c87;">
          <strong>Rights & Principles Analysis:</strong> ${c.principles_lens.analysis}
        </div>

        <div style="background-color:var(--g-gray-100); padding:8px 12px; border-radius:6px; font-size:11px; color:var(--g-gray-700);">
          <i class="fa-solid fa-circle-info"></i> ${c.principles_lens.disclaimer}
        </div>
      </div>
    `).join('');
  }
}

// 7. Full Contract Text Viewer
function renderFullContractText() {
  const container = document.getElementById('contract-full-text-body');
  const clauses = currentContract.clauses || [];

  container.innerHTML = `
    <div style="font-family: var(--font-mono); font-size:12px; line-height:1.6; color: var(--g-gray-800);">
      <h4>${currentContract.title.toUpperCase()}</h4>
      <p style="margin-bottom:16px;">This Agreement is entered into by and between the parties identified herein...</p>

      ${clauses.map(c => `
        <div style="margin-bottom:20px; padding:10px; background-color: var(--g-gray-50); border-left: 3px solid var(--g-blue);">
          <strong>${c.section_ref.toUpperCase()} — ${c.title.toUpperCase()}</strong>
          <p style="margin-top:6px; font-style:italic;">"${c.contract_quote}"</p>
        </div>
      `).join('')}
    </div>
  `;
}

function updateBadges() {
  document.getElementById('tab-badge-risks').innerText = currentContract.clauses.length;
}

// Tab Switching
function switchTab(tabId) {
  currentTab = tabId;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelector(`.tab-btn[data-tab="${tabId}"]`)?.classList.add('active');

  document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
  document.getElementById(`tab-${tabId}`)?.classList.add('active');
}

// MODAL: Make This Fair (8-Point Balance Evaluation)
async function openMakeFairModal(clauseId) {
  try {
    const res = await fetch('/api/make-fair', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ clause_id: clauseId, mode: activeMode })
    });
    const data = await res.json();
    const evalData = data.fairness_evaluation;

    const body = document.getElementById('make-fair-body');
    body.innerHTML = `
      <h3 style="font-size:16px; margin-bottom:12px;">Clause: ${evalData.clause_title}</h3>
      <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:16px;">
        ${evalData.questions.map(item => `
          <div style="background-color: var(--g-gray-50); padding:10px; border-radius:8px; font-size:13px;">
            <strong style="color:var(--g-blue);">${item.q}</strong>
            <p style="margin-top:4px;">${item.a}</p>
          </div>
        `).join('')}
      </div>

      <div class="suggested-response-box">
        <strong>Recommended Compromise:</strong>
        <p style="margin-top:4px; font-weight:600;">${evalData.recommended_compromise}</p>
        <p style="margin-top:8px; font-style:italic;">Suggested text: "${evalData.suggested_response}"</p>
      </div>
    `;

    document.getElementById('modal-make-fair').classList.remove('hidden');
  } catch (err) {
    showToast('Failed to evaluate clause fairness', 'error');
  }
}

function closeMakeFairModal() {
  document.getElementById('modal-make-fair').classList.add('hidden');
}

function copySuggestedCompromise() {
  showToast('Suggested response copied to clipboard!', 'success');
  closeMakeFairModal();
}

// MODAL: Clause Comparison Diff View
function openDiffModal(clauseId) {
  const clause = currentContract.clauses.find(c => c.id === clauseId) || currentContract.clauses[0];
  if (!clause || !clause.diff) return;

  document.getElementById('diff-original-text').innerText = clause.diff.original;
  document.getElementById('diff-proposed-text').innerText = clause.diff.proposed;
  document.getElementById('diff-explanation-text').innerText = clause.diff.explanation;

  document.getElementById('modal-diff').classList.remove('hidden');
}

function closeDiffModal() {
  document.getElementById('modal-diff').classList.add('hidden');
}

// DRAWER: Counterparty Negotiation Simulator
function openSimulateDrawer(clauseId) {
  const drawer = document.getElementById('sim-drawer');
  drawer.classList.add('open');

  const clause = currentContract.clauses.find(c => c.id === clauseId) || currentContract.clauses[0];
  chatHistory = [
    { sender: 'counterparty', text: `Hello! I am the Provider's contract agent. Regarding '${clause.title}', what specific adjustment would you like to request?` }
  ];
  renderChatHistory();
}

function closeSimulateDrawer() {
  document.getElementById('sim-drawer').classList.remove('open');
}

function renderChatHistory() {
  const body = document.getElementById('sim-chat-body');
  body.innerHTML = chatHistory.map(m => `
    <div class="chat-msg ${m.sender === 'user' ? 'chat-user' : 'chat-counterparty'}">
      ${m.text}
    </div>
  `).join('');
  body.scrollTop = body.scrollHeight;
}

async function sendSimMessage() {
  const input = document.getElementById('sim-user-input');
  const text = input.value.trim();
  if (!text) return;

  chatHistory.push({ sender: 'user', text: text });
  input.value = '';
  renderChatHistory();

  try {
    const res = await fetch('/api/counterparty-simulate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ history: chatHistory, message: text, mode: activeMode })
    });
    const data = await res.json();
    const sim = data.simulation;

    chatHistory.push({ sender: 'counterparty', text: sim.reply });
    renderChatHistory();

    document.getElementById('sim-status-indicator').innerText = sim.status_label;
    document.getElementById('sim-next-move-text').innerText = sim.next_move;
  } catch (err) {
    showToast('Simulation error', 'error');
  }
}

// MODAL: Next Challenge Prioritization
async function triggerNextChallenge() {
  try {
    const res = await fetch('/api/next-challenge', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mode: activeMode })
    });
    const data = await res.json();
    const chal = data.challenge;

    const body = document.getElementById('next-challenge-body');
    body.innerHTML = `
      <h3 style="font-size:18px; font-weight:700; color:var(--g-gray-900); margin-bottom:8px;">${chal.title}</h3>
      <p style="font-size:13px; color:var(--g-gray-800); margin-bottom:12px;"><strong>Why This Matters:</strong> ${chal.why}</p>
      
      <div style="background-color:var(--g-blue-light); padding:12px; border-radius:8px; font-size:13px; margin-bottom:12px;">
        <strong>Principle Involved:</strong> ${chal.principle_involved}<br>
        <strong>Practical Consequence:</strong> ${chal.practical_consequence}
      </div>

      <div class="suggested-response-box">
        <strong>Reasonable Challenge Proposal:</strong>
        <p style="margin-top:4px;">${chal.reasonable_challenge}</p>
      </div>
    `;

    document.getElementById('modal-next-challenge').dataset.targetId = chal.target_clause_id;
    document.getElementById('modal-next-challenge').classList.remove('hidden');
  } catch (err) {
    showToast('Failed to rank challenges', 'error');
  }
}

function closeNextChallengeModal() {
  document.getElementById('modal-next-challenge').classList.add('hidden');
}

function executeChallengeFromModal() {
  const clauseId = document.getElementById('modal-next-challenge').dataset.targetId;
  closeNextChallengeModal();
  openMakeFairModal(clauseId);
}

// MODAL: Paste Contract
function openPasteModal() {
  document.getElementById('modal-paste').classList.remove('hidden');
}

function closePasteModal() {
  document.getElementById('modal-paste').classList.add('hidden');
}

async function submitPastedContract() {
  const text = document.getElementById('paste-text-area').value.trim();
  if (!text) return;

  try {
    const res = await fetch('/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text, mode: activeMode })
    });
    const data = await res.json();
    currentContract = data.contract;
    renderAll();
    closePasteModal();
    showToast('Pasted contract analyzed successfully!', 'success');
  } catch (err) {
    showToast('Failed to analyze pasted contract', 'error');
  }
}

// Drag and Drop Upload
function handleFileUpload(evt) {
  const file = evt.target.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append('file', file);

  fetch(`/api/upload?mode=${activeMode}`, {
    method: 'POST',
    body: formData
  }).then(res => res.json()).then(data => {
    currentContract = data.contract;
    renderAll();
    showToast(`Uploaded and analyzed ${data.filename}`, 'success');
  }).catch(() => showToast('Upload failed', 'error'));
}

// Final Action Footer Buttons
function askCounselAction() {
  showToast('Questions flagged for Legal Counsel review.', 'info');
}

function acceptRiskAction() {
  showToast('Contract terms accepted with logged risk profile.', 'success');
}

// Demo Tour Machine
function toggleDemoTour() {
  demoTourActive = !demoTourActive;
  const banner = document.getElementById('demo-tour-banner');
  if (demoTourActive) {
    banner.classList.remove('hidden');
    currentDemoStep = 1;
    executeDemoStep();
  } else {
    banner.classList.add('hidden');
  }
}

function executeDemoStep() {
  document.getElementById('demo-step-number').innerText = `Step ${currentDemoStep} / ${TOTAL_DEMO_STEPS}`;

  const titles = [
    'Step 1: Open Contract Analysis',
    'Step 2: Multi-Step Agentic Reasoning',
    'Step 3: Contract Health Score & Leverage',
    'Step 4: Inspect Priority Risk Card',
    'Step 5: Make This Fair (8-Point Evaluation)',
    'Step 6: Win-Win Negotiation Middle Ground',
    'Step 7: Clause Comparison Redline Diff',
    'Step 8: Simulate Counterparty Negotiation',
    'Step 9: Interactive Multi-Turn Agreement',
    'Step 10: Rank "What Should I Challenge Next?"',
    'Step 11: Final Decision & Action Bar'
  ];

  const descs = [
    'Review contract ingestion metadata and core terms.',
    'Inspect Gemini agentic reasoning pipeline from jurisdiction to risks.',
    'View health score (68/100) and negotiation leverage assessment.',
    'Examine exact clause quote, plain English, and 85% risk allocation.',
    'Click "Make This Fair" to run the 8-point balance evaluation.',
    'Explore your concern vs their concern vs shared objective.',
    'View proposed clause redline diff converting uncapped to mutual cap.',
    'Open Counterparty Simulator to test negotiation pushback.',
    'Watch AI reach a 2x super-cap compromise agreement live.',
    'Trigger Next Challenge to rank single highest priority issue.',
    'Select final decision: Negotiate, Challenge, Accept, or Ask Counsel.'
  ];

  document.getElementById('demo-step-title').innerText = titles[currentDemoStep - 1];
  document.getElementById('demo-step-desc').innerText = descs[currentDemoStep - 1];

  if (currentDemoStep === 4) scrollToClause('b2b-cl-1');
  else if (currentDemoStep === 5) openMakeFairModal('b2b-cl-1');
  else if (currentDemoStep === 6) { closeMakeFairModal(); switchTab('mode-feature'); }
  else if (currentDemoStep === 7) openDiffModal('b2b-cl-1');
  else if (currentDemoStep === 8) { closeDiffModal(); openSimulateDrawer('b2b-cl-1'); }
  else if (currentDemoStep === 10) { closeSimulateDrawer(); triggerNextChallenge(); }
}

function nextDemoStep() {
  if (currentDemoStep < TOTAL_DEMO_STEPS) {
    currentDemoStep++;
    executeDemoStep();
  } else {
    toggleDemoTour();
    showToast('Demo tour completed!', 'success');
  }
}

function prevDemoStep() {
  if (currentDemoStep > 1) {
    currentDemoStep--;
    executeDemoStep();
  }
}

// Reset State
async function resetDemoState() {
  try {
    const res = await fetch('/api/reset', { method: 'POST' });
    await res.json();
    fetchContractData(activeMode);
    showToast('Demo state reset to baseline', 'info');
  } catch (err) {
    showToast('Failed to reset', 'error');
  }
}

function showToast(message, type = 'info') {
  const container = document.getElementById('toast-container');
  const toast = document.createElement('div');
  toast.className = 'toast';
  
  let icon = 'fa-info-circle';
  if (type === 'success') icon = 'fa-circle-check';
  if (type === 'error') icon = 'fa-triangle-exclamation';

  toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => { toast.remove(); }, 3500);
}
