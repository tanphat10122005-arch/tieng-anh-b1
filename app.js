/**
 * CAMBRIDGE B1 PRELIMINARY (PET) MASTER - APPLICATION ENGINE
 * Full 12 Units Roadmap, CBT Interactive Testing, Audio Lab & Original Book Archive
 */

(function () {
  'use strict';

  // State Management
  const state = {
    currentTab: 'home',
    currentUnitId: 'unit_1',
    roadmapFilter: 'all', // 'all', 'not-started', 'in-progress', 'completed'
    examMode: 'practice', // 'practice' or 'timed'
    timerSeconds: 50 * 60,
    timerInterval: null,
    answers: {}, // { [questionKey]: selectedValue }
    flagged: new Set(),
    unitProgress: {}, // { [unitId]: { status: 'not-started'|'in-progress'|'completed', score: number } }
    audio: {
      isPlaying: false,
      currentText: '',
      utterance: null,
      speed: 1.0,
      voice: null,
      trackName: ''
    },
    flashcards: {
      currentIndex: 0,
      isFlipped: false
    },
    writing: {
      currentTestIndex: 0
    },
    speaking: {
      currentTestIndex: 0
    },
    archive: {
      currentTestNum: 1,
      currentPage: 18
    },
    stats: {
      completedTests: 0,
      avgScore: 0,
      wordsLearned: 0
    }
  };

  // DOM Elements
  const elements = {
    navButtons: document.querySelectorAll('.nav-btn'),
    sections: document.querySelectorAll('.view-section'),
    themeToggleBtn: document.getElementById('theme-toggle-btn'),
    globalStatsPill: document.getElementById('global-stats-pill'),
    modalOverlay: document.getElementById('score-modal-overlay')
  };

  // Initialize App
  function init() {
    loadSavedState();
    setupTheme();
    setupNavigation();
    setupAudioVoices();
    renderDashboard();
    renderRoadmap();
    renderExamWorkspace();
    renderListeningLab();
    renderWritingStudio();
    renderSpeakingArena();
    renderFlashcards();
    renderBookViewer();
    updateGlobalStats();
  }

  // Local Storage Management
  function loadSavedState() {
    try {
      const savedTheme = localStorage.getItem('pet_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);

      const savedAnswers = localStorage.getItem('pet_answers');
      if (savedAnswers) state.answers = JSON.parse(savedAnswers);

      const savedProgress = localStorage.getItem('pet_unit_progress');
      if (savedProgress) state.unitProgress = JSON.parse(savedProgress);

      const savedStats = localStorage.getItem('pet_stats');
      if (savedStats) state.stats = JSON.parse(savedStats);
    } catch (e) {
      console.warn('Storage load error:', e);
    }
  }

  function saveState() {
    try {
      localStorage.setItem('pet_answers', JSON.stringify(state.answers));
      localStorage.setItem('pet_unit_progress', JSON.stringify(state.unitProgress));
      localStorage.setItem('pet_stats', JSON.stringify(state.stats));
    } catch (e) {
      console.warn('Storage save error:', e);
    }
  }

  // Theme Toggle
  function setupTheme() {
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', nextTheme);
        localStorage.setItem('pet_theme', nextTheme);
        elements.themeToggleBtn.innerHTML = nextTheme === 'dark' ? '🌙' : '☀️';
      });
    }
  }

  // Navigation
  function setupNavigation() {
    elements.navButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const tab = btn.dataset.tab;
        switchTab(tab);
      });
    });

    document.addEventListener('click', (e) => {
      const target = e.target.closest('[data-jump-tab]');
      if (target) {
        const tab = target.dataset.jumpTab;
        const unitId = target.dataset.unitId;
        if (unitId) state.currentUnitId = unitId;
        switchTab(tab);
      }
    });
  }

  function switchTab(tabName) {
    state.currentTab = tabName;
    elements.navButtons.forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === tabName);
    });

    elements.sections.forEach(sec => {
      sec.classList.toggle('active', sec.id === `section-${tabName}`);
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (tabName !== 'listening' && state.audio.isPlaying) {
      stopAudio();
    }

    if (tabName === 'roadmap') {
      renderRoadmap();
    } else if (tabName === 'exam') {
      renderExamWorkspace();
    } else if (tabName === 'listening') {
      renderListeningLab();
    } else if (tabName === 'writing') {
      renderWritingStudio();
    } else if (tabName === 'speaking') {
      renderSpeakingArena();
    } else if (tabName === 'flashcards') {
      renderFlashcards();
    } else if (tabName === 'archive') {
      renderBookViewer();
    }
  }

  // Audio Speech Synthesis Engine
  function setupAudioVoices() {
    if (!('speechSynthesis' in window)) return;
    function setVoice() {
      const voices = window.speechSynthesis.getVoices();
      state.audio.voice = voices.find(v => v.lang === 'en-GB' || v.name.includes('UK') || v.name.includes('British')) ||
                          voices.find(v => v.lang === 'en-US') ||
                          voices.find(v => v.lang.startsWith('en')) ||
                          voices[0];
    }
    setVoice();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
      window.speechSynthesis.onvoiceschanged = setVoice;
    }
  }

  function playAudioText(text, trackTitle, onEndCallback) {
    if (!('speechSynthesis' in window)) {
      alert('Trình duyệt của bạn không hỗ trợ Web Speech API.');
      return;
    }
    stopAudio();
    const utterance = new SpeechSynthesisUtterance(text);
    if (state.audio.voice) utterance.voice = state.audio.voice;
    utterance.rate = state.audio.speed || 1.0;
    utterance.pitch = 1.0;

    utterance.onstart = () => {
      state.audio.isPlaying = true;
      updateAudioDockUI(true, trackTitle);
    };
    utterance.onend = () => {
      state.audio.isPlaying = false;
      updateAudioDockUI(false, trackTitle);
      if (onEndCallback) onEndCallback();
    };
    utterance.onerror = () => {
      state.audio.isPlaying = false;
      updateAudioDockUI(false, trackTitle);
    };

    state.audio.utterance = utterance;
    state.audio.trackName = trackTitle;
    window.speechSynthesis.speak(utterance);
  }

  function stopAudio() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    state.audio.isPlaying = false;
    updateAudioDockUI(false);
  }

  function updateAudioDockUI(isPlaying, title) {
    const docks = document.querySelectorAll('.audio-player-dock');
    docks.forEach(dock => {
      const disk = dock.querySelector('.audio-disk');
      const playBtn = dock.querySelector('.btn-play-lg');
      const titleEl = dock.querySelector('.track-title');
      if (disk) disk.classList.toggle('spinning', isPlaying);
      if (playBtn) playBtn.innerHTML = isPlaying ? '⏸️' : '▶️';
      if (titleEl && title) titleEl.textContent = title;
    });
  }

  // ========================================================
  // 1. DASHBOARD VIEW
  // ========================================================
  function renderDashboard() {
    const container = document.getElementById('dashboard-content');
    if (!container) return;

    const units = window.PET_DATA.units || [];
    let completedCount = 0;
    units.forEach(u => {
      if (state.unitProgress[u.id]?.status === 'completed') completedCount++;
    });

    const percent = Math.round((completedCount / (units.length || 12)) * 100);

    container.innerHTML = `
      <div class="hero-banner">
        <div class="hero-content">
          <span class="badge-tag">Cambridge English B1 Preliminary (PET)</span>
          <h1 class="hero-title">Lộ Trình Ôn Luyện 12 Đề Toàn Diện</h1>
          <p class="hero-desc">
            Phân loại chi tiết từ <strong>Unit 1 đến Unit 12</strong>, số hóa toàn bộ các câu hỏi cùng 
            <strong>đáp án khoanh đỏ chính xác từ sách gốc</strong>. Theo dõi tiến độ học tập từng ngày, 
            luyện nghe với giọng đọc bản xứ, và thi thử trực tuyến CBT bấm giờ chuẩn Cambridge.
          </p>
          <div class="hero-actions">
            <button class="btn-primary" data-jump-tab="roadmap">
              🗺️ Xem Lộ Trình 12 Unit
            </button>
            <button class="btn-secondary" data-jump-tab="exam" data-unit-id="unit_1">
              📝 Thi Thử Unit 1 Ngay
            </button>
            <button class="btn-secondary" data-jump-tab="archive">
              📖 Thư Viện 110 Trang Sách Gốc
            </button>
          </div>
        </div>
      </div>

      <!-- Overall Learning Progress Card -->
      <div class="roadmap-summary-card">
        <div style="flex: 1; min-width: 260px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-weight: 800; font-size: 1.1rem;">Tiến Độ Khóa Học (12 Units)</span>
            <span style="font-weight: 800; color: var(--secondary); font-size: 1.15rem;">${completedCount} / 12 Unit (${percent}%)</span>
          </div>
          <div class="roadmap-progress-bar-wrap">
            <div class="roadmap-progress-bar-fill" style="width: ${percent}%;"></div>
          </div>
          <div style="font-size: 0.84rem; color: var(--text-muted); margin-top: 0.65rem;">
            💡 Đã hoàn thành <strong>${completedCount}</strong> unit. Bạn có thể đánh dấu tiến độ ở mục <strong>Lộ Trình 12 Unit</strong>.
          </div>
        </div>
        <div style="display: flex; gap: 1.5rem; text-align: center;">
          <div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #10b981;">12</div>
            <div style="font-size: 0.78rem; color: var(--text-muted);">Tổng số Unit</div>
          </div>
          <div>
            <div style="font-size: 1.8rem; font-weight: 800; color: var(--primary);">${completedCount}</div>
            <div style="font-size: 0.78rem; color: var(--text-muted);">Đã hoàn thành</div>
          </div>
          <div>
            <div style="font-size: 1.8rem; font-weight: 800; color: var(--secondary);">${state.stats.avgScore || 145}</div>
            <div style="font-size: 0.78rem; color: var(--text-muted);">Điểm B1 ước tính</div>
          </div>
        </div>
      </div>

      <div class="section-heading">
        <h2>🚀 Phân Hệ Ôn Luyện Trọng Tâm</h2>
      </div>

      <div class="module-grid">
        <div class="module-card" data-jump-tab="roadmap">
          <div class="module-top">
            <div class="module-icon-wrap" style="background: rgba(79, 70, 229, 0.15); color: #818cf8;">🗺️</div>
            <span class="badge-tag" style="margin: 0;">Tiến Độ</span>
          </div>
          <h3>Lộ Trình 12 Unit (Unit 1 - Unit 12)</h3>
          <p>Xem danh sách đầy đủ 12 Unit theo chủ đề, theo dõi trạng thái Chưa học / Đang học / Hoàn thành và điểm thi từng bài.</p>
          <div class="module-footer">
            <span>Theo dõi tiến trình</span>
            <span>Vào lộ trình →</span>
          </div>
        </div>

        <div class="module-card" data-jump-tab="exam">
          <div class="module-top">
            <div class="module-icon-wrap" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee;">📝</div>
            <span class="badge-tag" style="margin: 0;">Full CBT</span>
          </div>
          <h3>Phòng Thi Trực Tuyến CBT (12 Unit)</h3>
          <p>Làm bài thi trắc nghiệm bấm giờ cho cả 12 đề thi, tự động đối chiếu chính xác với đáp án khoanh đỏ từ sách gốc.</p>
          <div class="module-footer">
            <span>Thang điểm 120-170</span>
            <span>Vào phòng thi →</span>
          </div>
        </div>

        <div class="module-card" data-jump-tab="listening">
          <div class="module-top">
            <div class="module-icon-wrap" style="background: rgba(16, 185, 129, 0.15); color: #34d399;">🎧</div>
            <span class="badge-tag" style="margin: 0;">Audio Lab</span>
          </div>
          <h3>Luyện Nghe Audio Giọng Đọc Bản Xứ</h3>
          <p>Tự động phát giọng đọc chuẩn Anh - Anh & Anh - Mỹ cho toàn bộ các bài nghe. Hỗ trợ điều chỉnh tốc độ và hiển thị tapescript.</p>
          <div class="module-footer">
            <span>Part 1-4 đầy đủ</span>
            <span>Luyện nghe →</span>
          </div>
        </div>

        <div class="module-card" data-jump-tab="writing">
          <div class="module-top">
            <div class="module-icon-wrap" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24;">✍️</div>
            <span class="badge-tag" style="margin: 0;">Band 5 Model</span>
          </div>
          <h3>Writing Studio (Luyện Viết B1)</h3>
          <p>Kiểm tra viết lại câu tương đương tức thì, bộ đếm từ tự động viết thư ngắn 35-45 từ và bài mẫu 100 từ chuẩn Global ELT.</p>
          <div class="module-footer">
            <span>Bài mẫu xuất sắc</span>
            <span>Luyện viết →</span>
          </div>
        </div>

        <div class="module-card" data-jump-tab="speaking">
          <div class="module-top">
            <div class="module-icon-wrap" style="background: rgba(236, 72, 153, 0.15); color: #f472b6;">🗣️</div>
            <span class="badge-tag" style="margin: 0;">Speaking Arena</span>
          </div>
          <h3>Speaking Arena (10 Đề Nói Kèm Ảnh Màu)</h3>
          <p>Giám khảo ảo đọc câu hỏi phỏng vấn, tranh màu miêu tả cảnh quan và thẻ tình huống thảo luận chất lượng cao từ sách.</p>
          <div class="module-footer">
            <span>Audio giám khảo</span>
            <span>Luyện nói →</span>
          </div>
        </div>

        <div class="module-card" data-jump-tab="archive">
          <div class="module-top">
            <div class="module-icon-wrap" style="background: rgba(139, 92, 246, 0.15); color: #a78bfa;">📖</div>
            <span class="badge-tag" style="margin: 0;">110 Trang Scan</span>
          </div>
          <h3>Thư Viện Đề Gốc Có Đáp Án Khoanh Đỏ</h3>
          <p>Xem toàn bộ 110 trang sách nguyên bản từ Test 1 đến Test 10 với các nét khoanh đỏ và chú giải tiếng Việt gốc.</p>
          <div class="module-footer">
            <span>Tra cứu & Phóng to</span>
            <span>Xem đề gốc →</span>
          </div>
        </div>
      </div>
    `;
  }

  // ========================================================
  // 1.5. ROADMAP 12 UNITS CLASSIFICATION & PROGRESS TRACKER
  // ========================================================
  function renderRoadmap() {
    const container = document.getElementById('roadmap-workspace');
    if (!container) return;

    const units = window.PET_DATA.units || [];
    let completedCount = 0;
    let inProgressCount = 0;
    let notStartedCount = 0;
    let b1PassCount = 0;
    let totalScore = 0;
    let scoredUnits = 0;

    units.forEach(u => {
      const prog = state.unitProgress[u.id] || { status: 'not-started', score: null };
      if (prog.status === 'completed') {
        completedCount++;
        if (prog.score) {
          totalScore += prog.score;
          scoredUnits++;
          if (prog.score >= 140) b1PassCount++;
        }
      } else if (prog.status === 'in-progress') {
        inProgressCount++;
      } else {
        notStartedCount++;
      }
    });

    const percent = Math.round((completedCount / (units.length || 12)) * 100);
    const avgScore = scoredUnits > 0 ? Math.round(totalScore / scoredUnits) : (state.stats.avgScore || 145);

    // Filter units
    let filteredUnits = units;
    if (state.roadmapFilter === 'not-started') {
      filteredUnits = units.filter(u => (state.unitProgress[u.id]?.status || 'not-started') === 'not-started');
    } else if (state.roadmapFilter === 'in-progress') {
      filteredUnits = units.filter(u => state.unitProgress[u.id]?.status === 'in-progress');
    } else if (state.roadmapFilter === 'completed') {
      filteredUnits = units.filter(u => state.unitProgress[u.id]?.status === 'completed');
    } else if (state.roadmapFilter === 'b1-pass') {
      filteredUnits = units.filter(u => (state.unitProgress[u.id]?.score || 0) >= 140);
    }

    container.innerHTML = `
      <div class="test-header-bar">
        <div class="test-title-group">
          <h2>📊 Phân Loại Unit 1 Đến Unit 12 & Quản Lý Tiến Độ Ôn Luyện</h2>
          <p>Hệ thống phân loại toàn diện 12 Unit • Đầy đủ 4 kỹ năng • Bộ đề CBT chuẩn xác đối chiếu trực tiếp với đáp án khoanh đỏ từ sách gốc</p>
        </div>
      </div>

      <!-- Roadmap Header Summary Metrics -->
      <div class="roadmap-metrics-grid">
        <div class="roadmap-metric-card">
          <div class="roadmap-metric-icon" style="background: rgba(79, 70, 229, 0.15); color: #818cf8;">📚</div>
          <div>
            <div class="roadmap-metric-val">12</div>
            <div class="roadmap-metric-label">Tổng Số Unit Khóa Học</div>
          </div>
        </div>

        <div class="roadmap-metric-card">
          <div class="roadmap-metric-icon" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">✅</div>
          <div>
            <div class="roadmap-metric-val" style="color: #10b981;">${completedCount} / 12</div>
            <div class="roadmap-metric-label">Đã Hoàn Thành (${percent}%)</div>
          </div>
        </div>

        <div class="roadmap-metric-card">
          <div class="roadmap-metric-icon" style="background: rgba(245, 158, 11, 0.15); color: #f59e0b;">✍️</div>
          <div>
            <div class="roadmap-metric-val" style="color: #f59e0b;">${inProgressCount}</div>
            <div class="roadmap-metric-label">Đang Ôn Luyện</div>
          </div>
        </div>

        <div class="roadmap-metric-card">
          <div class="roadmap-metric-icon" style="background: rgba(6, 182, 212, 0.15); color: #06b6d4;">🏆</div>
          <div>
            <div class="roadmap-metric-val" style="color: #06b6d4;">${avgScore} / 170</div>
            <div class="roadmap-metric-label">Điểm Cambridge Ước Tính</div>
          </div>
        </div>
      </div>

      <!-- Roadmap Progress Bar -->
      <div class="roadmap-summary-card" style="margin-bottom: 1.5rem;">
        <div style="flex: 1;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem;">
            <span style="font-weight: 800; font-size: 1.05rem;">Tiến Trình 12 Unit Khóa Học B1 Preliminary</span>
            <span style="font-weight: 800; color: var(--secondary); font-size: 1.15rem;">${completedCount} / 12 Unit (${percent}%)</span>
          </div>
          <div class="roadmap-progress-bar-wrap" style="height: 12px;">
            <div class="roadmap-progress-bar-fill" style="width: ${percent}%;"></div>
          </div>
        </div>
      </div>

      <!-- Filter Bar -->
      <div class="filter-bar">
        <button class="filter-pill ${state.roadmapFilter === 'all' ? 'active' : ''}" data-filter="all">Tất Cả (12 Unit)</button>
        <button class="filter-pill ${state.roadmapFilter === 'not-started' ? 'active' : ''}" data-filter="not-started">⏳ Chưa học (${notStartedCount})</button>
        <button class="filter-pill ${state.roadmapFilter === 'in-progress' ? 'active' : ''}" data-filter="in-progress">✍️ Đang học (${inProgressCount})</button>
        <button class="filter-pill ${state.roadmapFilter === 'completed' ? 'active' : ''}" data-filter="completed">✅ Đã hoàn thành (${completedCount})</button>
        <button class="filter-pill ${state.roadmapFilter === 'b1-pass' ? 'active' : ''}" data-filter="b1-pass">🏆 Đạt chuẩn B1 (${b1PassCount})</button>
      </div>

      <!-- Units Grid -->
      <div class="units-grid">
        ${filteredUnits.map(u => {
          const prog = state.unitProgress[u.id] || { status: 'not-started', score: null };
          const statusClass = prog.status;
          let statusText = '⏳ Chưa học';
          if (prog.status === 'in-progress') statusText = '✍️ Đang học';
          if (prog.status === 'completed') statusText = '✅ Đã hoàn thành';

          return `
            <div class="unit-card ${statusClass}" id="card-${u.id}">
              <div>
                <div class="unit-header">
                  <span class="unit-badge">UNIT ${u.unitNumber}</span>
                  <select class="unit-status-select" data-unit-id="${u.id}" title="Chọn trạng thái học tập">
                    <option value="not-started" ${prog.status === 'not-started' ? 'selected' : ''}>⏳ Chưa học</option>
                    <option value="in-progress" ${prog.status === 'in-progress' ? 'selected' : ''}>✍️ Đang học</option>
                    <option value="completed" ${prog.status === 'completed' ? 'selected' : ''}>✅ Đã hoàn thành</option>
                  </select>
                </div>

                <div class="unit-title">${u.title}</div>
                <div class="unit-theme">${u.theme}</div>

                <div class="unit-skills-bar">
                  <span class="skill-tag">📖 Đọc: 35 câu CBT</span>
                  <span class="skill-tag">🎧 Nghe: 25 câu Audio</span>
                  <span class="skill-tag">✍️ Viết Band 5</span>
                  <span class="skill-tag">🗣️ Nói phỏng vấn</span>
                </div>

                ${prog.score ? `
                  <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: var(--radius-sm); padding: 0.5rem 0.85rem; margin-bottom: 0.85rem; font-size: 0.86rem; color: #10b981; font-weight: 700; display: flex; align-items: center; justify-content: space-between;">
                    <span>🏆 Điểm CBT Đạt Được:</span>
                    <span style="font-size: 1.05rem;">${prog.score} / 170</span>
                  </div>
                ` : `
                  <div style="background: rgba(255, 255, 255, 0.03); border: 1px dashed var(--border); border-radius: var(--radius-sm); padding: 0.45rem 0.85rem; margin-bottom: 0.85rem; font-size: 0.8rem; color: var(--text-muted);">
                    Chưa thi thử CBT • Sẵn sàng làm bài
                  </div>
                `}

                <div style="font-size: 0.8rem; color: var(--text-dim); margin-bottom: 0.5rem;">
                  📚 Trang trong sách: ${u.pageRange} • Đối chiếu trực tiếp đáp án khoanh đỏ
                </div>
              </div>

              <div class="unit-card-actions">
                <button class="btn-primary" data-jump-tab="exam" data-unit-id="${u.id}">
                  📝 Thi Thử CBT
                </button>
                <button class="btn-secondary" data-jump-tab="listening" data-unit-id="${u.id}">
                  🎧 Luyện Nghe
                </button>
                <button class="btn-secondary btn-quick-book" data-page="${u.scanPages[0]}">
                  📖 Sách Gốc
                </button>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;

    // Filter clicks
    container.querySelectorAll('.filter-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        state.roadmapFilter = pill.dataset.filter;
        renderRoadmap();
      });
    });

    // Unit status select change
    container.querySelectorAll('.unit-status-select').forEach(sel => {
      sel.addEventListener('change', (e) => {
        const unitId = sel.dataset.unitId;
        const newStatus = sel.value;
        if (!state.unitProgress[unitId]) state.unitProgress[unitId] = {};
        state.unitProgress[unitId].status = newStatus;
        saveState();
        renderRoadmap();
        updateGlobalStats();
      });
    });

    // Quick book page view
    container.querySelectorAll('.btn-quick-book').forEach(btn => {
      btn.addEventListener('click', () => {
        const page = btn.dataset.page;
        showPageZoomModal(page);
      });
    });
  }

  // ========================================================
  // 2. EXAM & CBT WORKSPACE VIEW (ALL 12 UNITS DUAL-PANE)
  // ========================================================
  let currentExamBookZoom = 1.0;
  let currentExamBookPage = 18;

  function renderExamWorkspace() {
    const container = document.getElementById('exam-workspace');
    if (!container) return;

    const units = window.PET_DATA.units || [];
    const currentUnit = units.find(u => u.id === state.currentUnitId) || units[0];

    currentExamBookPage = currentUnit.scanPages[0] || 18;
    currentExamBookZoom = 1.0;

    const isDigital = !!currentUnit.isFullDigital;

    container.innerHTML = `
      <div class="test-header-bar">
        <div class="test-title-group">
          <h2>${currentUnit.title} - ${isDigital ? 'Phòng Thi CBT Số Hóa Trực Tuyến' : 'Phòng Thi CBT'}</h2>
          <p>${currentUnit.theme} • ${isDigital ? 'Đầy đủ nội dung chữ, bài đọc và câu hỏi 100% không lộ đáp án' : 'Đối chiếu theo sách gốc'}</p>
        </div>
        <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
          <select id="exam-unit-selector" class="speed-select" style="padding: 0.55rem 1rem; font-weight: 700;">
            ${units.map(u => `
              <option value="${u.id}" ${u.id === currentUnit.id ? 'selected' : ''}>
                Unit ${u.unitNumber}: ${u.title.split(':')[1] || u.title} ${u.isFullDigital ? '⭐ (Số Hóa Full Text)' : ''}
              </option>
            `).join('')}
          </select>

          <button class="book-ref-floating-btn" id="btn-open-unit-book" data-startpage="${currentUnit.scanPages[0]}">
            📖 Xem Trang Sách Gốc (Đối Chiếu)
          </button>

          <div class="mode-toggle-group">
            <button class="mode-toggle-btn ${state.examMode === 'practice' ? 'active' : ''}" id="btn-mode-practice">Luyện tập</button>
            <button class="mode-toggle-btn ${state.examMode === 'timed' ? 'active' : ''}" id="btn-mode-timed">Bấm giờ</button>
          </div>

          <div class="timer-box" id="exam-timer-display" style="${state.examMode === 'timed' ? 'display:flex' : 'display:none'}">
            ⏱️ <span id="timer-val">50:00</span>
          </div>

          <button class="btn-primary" id="btn-submit-exam" style="padding: 0.55rem 1.25rem;">
            ✅ Nộp Bài & Chấm Điểm
          </button>
        </div>
      </div>

      <div class="test-layout">
        <!-- Main CBT Questions Workspace -->
        <div class="test-main-pane" id="exam-questions-pane" style="padding: 1.5rem;">
          <!-- Questions Rendered Inside -->
        </div>

        <!-- Sidebar Navigation Drawer -->
        <aside class="test-sidebar">
          <div class="sidebar-title">
            <span>Danh Sách 35 Câu</span>
            <span id="answered-count-badge" class="badge-tag" style="margin: 0;">0 / 35</span>
          </div>
          <div class="q-grid" id="exam-q-grid"></div>
          <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
            <button class="btn-secondary" id="btn-side-open-book" style="width: 100%; justify-content: center;">
              📖 Xem Sách Gốc & Đáp Án
            </button>
            <button class="btn-primary" id="btn-submit-exam-side" style="width: 100%; justify-content: center;">
              Hoàn thành & Chấm điểm
            </button>
          </div>
        </aside>
      </div>
    `;

    // Unit selector change
    const sel = document.getElementById('exam-unit-selector');
    if (sel) {
      sel.addEventListener('change', (e) => {
        state.currentUnitId = e.target.value;
        renderExamWorkspace();
      });
    }

    // Book page buttons
    const openBookBtn = document.getElementById('btn-open-unit-book');
    if (openBookBtn) {
      openBookBtn.addEventListener('click', () => {
        showPageZoomModal(currentExamBookPage || currentUnit.scanPages[0]);
      });
    }

    const sideBookBtn = document.getElementById('btn-side-open-book');
    if (sideBookBtn) {
      sideBookBtn.addEventListener('click', () => {
        showPageZoomModal(currentExamBookPage || currentUnit.scanPages[0]);
      });
    }

    // Mode toggles
    const btnPractice = document.getElementById('btn-mode-practice');
    const btnTimed = document.getElementById('btn-mode-timed');
    const timerDisplay = document.getElementById('exam-timer-display');

    if (btnPractice && btnTimed) {
      btnPractice.addEventListener('click', () => {
        state.examMode = 'practice';
        btnPractice.classList.add('active');
        btnTimed.classList.remove('active');
        if (timerDisplay) timerDisplay.style.display = 'none';
        stopTimer();
        renderExamQuestionsForUnit(currentUnit);
      });

      btnTimed.addEventListener('click', () => {
        state.examMode = 'timed';
        btnTimed.classList.add('active');
        btnPractice.classList.remove('active');
        if (timerDisplay) timerDisplay.style.display = 'flex';
        startTimer();
        renderExamQuestionsForUnit(currentUnit);
      });
    }

    // Submit buttons
    [document.getElementById('btn-submit-exam'), document.getElementById('btn-submit-exam-side')].forEach(b => {
      if (b) b.addEventListener('click', () => gradeExamForUnit(currentUnit));
    });

    renderExamQuestionsForUnit(currentUnit);
  }

  function renderExamQuestionsForUnit(unit) {
    const pane = document.getElementById('exam-questions-pane');
    const grid = document.getElementById('exam-q-grid');
    if (!pane || !grid) return;

    // Check if Unit is full digital (Unit 1, 2, 11, 12, etc.)
    if (unit.isFullDigital) {
      renderDigitalExam(unit, pane, grid);
      return;
    }

    // 5 Reading Parts Definition for other units
    const partsMeta = [
      { part: 1, range: [1, 5], title: "Part 1: Questions 1 - 5 (Thông báo & Tin nhắn ngắn)", opts: ['A','B','C'], pageOffset: 0 },
      { part: 2, range: [6, 10], title: "Part 2: Questions 6 - 10 (Ghép người với chương trình / địa điểm)", opts: ['A','B','C','D','E','F','G','H'], pageOffset: 1 },
      { part: 3, range: [11, 20], title: "Part 3: Questions 11 - 20 (Đúng / Sai - True or False)", opts: ['A','B'], pageOffset: 2 },
      { part: 4, range: [21, 25], title: "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)", opts: ['A','B','C','D'], pageOffset: 3 },
      { part: 5, range: [26, 35], title: "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)", opts: ['A','B','C','D'], pageOffset: 4 }
    ];

    const readingKeys = unit.readingKeys || {};

    let html = `
      <div style="background: rgba(79, 70, 229, 0.08); border: 1px solid rgba(79, 70, 229, 0.25); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
        <div>
          <h4 style="color: var(--secondary); font-size: 1.05rem; margin-bottom: 0.25rem;">📄 Đề thi: ${unit.title}</h4>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin: 0;">Các câu hỏi dưới đây được đối chiếu chính xác với đáp án từ tài liệu chuẩn Cambridge.</p>
        </div>
        <button class="book-ref-floating-btn" onclick="document.getElementById('btn-open-unit-book').click()">
          🔍 Phóng to đề gốc xem chi tiết
        </button>
      </div>
    `;

    let gridHtml = '';

    partsMeta.forEach(pm => {
      const pageNum = unit.scanPages[pm.pageOffset] || unit.scanPages[0];
      html += `
        <div style="margin-bottom: 2.25rem;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; border-bottom: 2px solid rgba(79, 70, 229, 0.3); padding-bottom: 0.5rem; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              <h3 style="font-size: 1.15rem; color: #818cf8; margin-bottom: 0.2rem;">${pm.title}</h3>
            </div>
            <button class="btn-secondary btn-quick-page" data-page="${pageNum}" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; font-weight: 700;">
              📄 Xem trang ${pageNum} (sách gốc)
            </button>
          </div>
      `;

      for (let q = pm.range[0]; q <= pm.range[1]; q++) {
        const qKey = `${unit.id}_r_${q}`;
        const currentAns = state.answers[qKey];
        const correctAns = readingKeys[q];

        gridHtml += `<button class="grid-num-btn ${currentAns ? 'answered' : ''}" data-goto="q-${q}">${q}</button>`;

        html += `
          <div class="q-container" id="q-${q}" style="margin-bottom: 1.5rem; padding-bottom: 1.25rem;">
            <div class="q-header">
              <span class="q-num-badge">Câu ${q}</span>
              <span style="font-size: 0.84rem; color: var(--text-muted);">Trang ${pageNum}</span>
            </div>

            <div class="options-group" style="display: grid; grid-template-columns: repeat(${pm.opts.length > 4 ? 4 : pm.opts.length}, 1fr); gap: 0.5rem;">
              ${pm.opts.map(opt => `
                <div class="option-item ${currentAns === opt ? 'selected' : ''}" data-qkey="${qKey}" data-opt="${opt}">
                  <div class="option-key">${opt}</div>
                  <div class="option-text">${pm.part === 3 ? (opt === 'A' ? 'ĐÚNG (A)' : 'SAI (B)') : `Lựa chọn ${opt}`}</div>
                </div>
              `).join('')}
            </div>

            <div class="explanation-box" id="exp-${qKey}" style="display: none; margin-top: 0.85rem;">
              <div class="explanation-title">💡 Đáp án chính xác theo sách gốc: ${correctAns}</div>
              <div style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 0.4rem;">
                Đáp án câu ${q} đã được đối chiếu chuẩn xác với dấu khoanh đỏ trên trang ${pageNum} của tài liệu gốc.
              </div>
            </div>
          </div>
        `;
      }

      html += `</div>`;
    });

    pane.innerHTML = html;
    grid.innerHTML = gridHtml;

    updateAnsweredCount(unit);
    bindExamOptionClicks(unit);

    pane.querySelectorAll('.btn-quick-page').forEach(btn => {
      btn.addEventListener('click', () => {
        showPageZoomModal(btn.dataset.page);
      });
    });
  }

  function renderDigitalExam(unit, pane, grid) {
    const testId = unit.practiceTestId || `test_${unit.unitNumber}`;
    const testData = window.PET_DATA.practiceTests.find(t => t.id === testId);
    if (!testData) return;

    let html = `
      <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: var(--radius-md); padding: 1.15rem 1.35rem; margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
        <div>
          <div style="font-weight: 800; font-size: 1.05rem; color: #10b981; margin-bottom: 0.25rem;">
            ✨ Bộ Đề CBT Đã Được Số Hóa Hoàn Chỉnh Toàn Bộ Chữ (100% Digital Text)
          </div>
          <div style="font-size: 0.86rem; color: var(--text-muted); line-height: 1.5;">
            Toàn bộ bài đọc, thông báo và từng câu hỏi được trình bày rõ ràng, không có dấu khoanh đỏ để bạn tự tin luyện tập. Chọn phương án để trả lời.
          </div>
        </div>
      </div>
    `;
    let gridHtml = '';

    testData.reading.parts.forEach(part => {
      html += `
        <div style="margin-bottom: 2.5rem;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem; border-bottom: 2px solid rgba(79, 70, 229, 0.3); padding-bottom: 0.5rem;">
            <h3 style="font-size: 1.25rem; color: #818cf8;">${part.title}</h3>
          </div>
          <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem; font-style: italic;">${part.instruction}</p>
      `;

      if (part.passage) {
        html += `
          <div class="q-context-box" style="border-left-color: var(--secondary); background: rgba(15, 23, 42, 0.6); margin-bottom: 1.5rem; padding: 1.35rem;">
            <h4 style="color: var(--secondary); font-size: 1.15rem; margin-bottom: 0.65rem;">📖 ${part.passageTitle || 'Reading Text'}</h4>
            <div style="font-size: 0.98rem; line-height: 1.75; color: var(--text-main);">${part.passage.replace(/\n\n/g, '<br><br>')}</div>
          </div>
        `;
      }

      // Part 2: Matching People with Reviews / Courses
      if (part.teenagers && part.places) {
        html += `
          <div style="background: rgba(79, 70, 229, 0.06); border: 1px solid rgba(79, 70, 229, 0.2); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 2rem;">
            <h4 style="font-size: 1rem; color: var(--secondary); margin-bottom: 0.85rem; font-weight: 800;">
              📋 Danh Sách Các Lựa Chọn (Reviews / Courses A - H):
            </h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 0.85rem;">
              ${part.places.map(p => `
                <div style="background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 0.85rem;">
                  <div style="font-weight: 800; color: #818cf8; font-size: 0.92rem; margin-bottom: 0.35rem;">
                    ${p.code}. ${p.title}
                  </div>
                  <div style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">${p.desc}</div>
                </div>
              `).join('')}
            </div>
          </div>
        `;

        part.teenagers.forEach(t => {
          const qKey = `${unit.id}_r_${t.number}`;
          const currentAns = state.answers[qKey];
          gridHtml += `<button class="grid-num-btn ${currentAns ? 'answered' : ''}" data-goto="q-${t.number}">${t.number}</button>`;

          html += `
            <div class="q-container" id="q-${t.number}">
              <div class="q-header">
                <span class="q-num-badge">Câu ${t.number}</span>
                <span class="q-person-badge">👤 ${t.name}</span>
              </div>
              <div class="q-context-box">
                <div class="q-context-label">📌 Nhu cầu & Sở thích của ${t.name}:</div>
                <div class="q-context-body">${t.demand}</div>
              </div>
              <div class="q-prompt-text">
                <span class="q-prompt-icon">👉</span>
                <span>Chọn phương án phù hợp nhất cho <strong>${t.name}</strong> (A - H):</span>
              </div>
              <div class="options-group" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 0.65rem;">
                ${['A','B','C','D','E','F','G','H'].map(opt => `
                  <div class="option-item ${currentAns === opt ? 'selected' : ''}" data-qkey="${qKey}" data-opt="${opt}">
                    <div class="option-key">${opt}</div>
                    <div class="option-text">${part.places.find(p=>p.code===opt)?.title || opt}</div>
                  </div>
                `).join('')}
              </div>
              <div class="explanation-box" id="exp-${qKey}" style="display: none;">
                <div class="explanation-title">💡 Giải thích (Đáp án đúng: ${t.correct})</div>
                <div style="font-size: 0.92rem; line-height: 1.6;">${t.explanation}</div>
              </div>
            </div>
          `;
        });
      }

      if (part.questions) {
        part.questions.forEach(q => {
          const qKey = `${unit.id}_r_${q.number}`;
          const currentAns = state.answers[qKey];
          gridHtml += `<button class="grid-num-btn ${currentAns ? 'answered' : ''}" data-goto="q-${q.number}">${q.number}</button>`;

          html += `
            <div class="q-container" id="q-${q.number}">
              <div class="q-header">
                <span class="q-num-badge">Câu ${q.number}</span>
              </div>
          `;

          if (q.context) {
            html += `
              <div class="q-context-box">
                <div class="q-context-label">📌 Thông tin / Biển báo (Notice):</div>
                <div class="q-context-body">${q.context}</div>
              </div>
            `;
          }
          if (q.question) {
            html += `
              <div class="q-prompt-text">
                <span class="q-prompt-icon">❓</span>
                <span>${q.question}</span>
              </div>
            `;
          } else if (q.statement) {
            html += `
              <div class="q-prompt-text">
                <span class="q-prompt-icon">📝</span>
                <span>${q.statement}</span>
              </div>
            `;
          }

          html += `<div class="options-group">`;
          if (q.options) {
            q.options.forEach(opt => {
              html += `
                <div class="option-item ${currentAns === opt.key ? 'selected' : ''}" data-qkey="${qKey}" data-opt="${opt.key}">
                  <div class="option-key">${opt.key}</div>
                  <div class="option-text">${opt.text}</div>
                </div>
              `;
            });
          } else if (q.statement) {
            html += `
              <div class="option-item ${currentAns === 'A' ? 'selected' : ''}" data-qkey="${qKey}" data-opt="A">
                <div class="option-key">A</div>
                <div class="option-text">ĐÚNG (A - True)</div>
              </div>
              <div class="option-item ${currentAns === 'B' ? 'selected' : ''}" data-qkey="${qKey}" data-opt="B">
                <div class="option-key">B</div>
                <div class="option-text">SAI (B - False)</div>
              </div>
            `;
          }
          html += `</div>`;

          html += `
            <div class="explanation-box" id="exp-${qKey}" style="display: none;">
              <div class="explanation-title">💡 Giải thích (Đáp án đúng: ${q.correct})</div>
              <div style="font-size: 0.92rem; line-height: 1.6;">${q.explanation}</div>
            </div>
          </div>`;
        });
      }

      html += `</div>`;
    });

    pane.innerHTML = html;
    grid.innerHTML = gridHtml;

    updateAnsweredCount(unit);
    bindExamOptionClicks(unit);
  }

  function bindExamOptionClicks(unit) {
    document.querySelectorAll('#exam-questions-pane .option-item').forEach(opt => {
      opt.addEventListener('click', () => {
        const qKey = opt.dataset.qkey;
        const val = opt.dataset.opt;

        state.answers[qKey] = val;
        saveState();

        const parent = opt.closest('.options-group');
        parent.querySelectorAll('.option-item').forEach(o => o.classList.remove('selected'));
        opt.classList.add('selected');

        // LƯU Ý QUAN TRỌNG: Không hiển thị giải thích khi đang làm bài thi.
        // Toàn bộ giải thích và kết quả đúng/sai sẽ chỉ hiển thị sau khi bấm "Nộp Bài & Chấm Điểm".

        updateAnsweredCount(unit);
      });
    });

    document.querySelectorAll('#exam-q-grid .grid-num-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.dataset.goto;
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
          targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
          targetEl.style.transition = 'background 0.5s ease';
          targetEl.style.background = 'rgba(79, 70, 229, 0.15)';
          setTimeout(() => targetEl.style.background = 'transparent', 1200);
        }
      });
    });
  }

  function updateAnsweredCount(unit) {
    let answered = 0;
    for (let i = 1; i <= 35; i++) {
      const qKey = `${unit.id}_r_${i}`;
      if (state.answers[qKey]) answered++;
      const btn = document.querySelector(`[data-goto="q-${i}"]`);
      if (btn) btn.classList.toggle('answered', !!state.answers[qKey]);
    }
    const badge = document.getElementById('answered-count-badge');
    if (badge) badge.textContent = `${answered} / 35`;
  }

  function gradeExamForUnit(unit) {
    let correctCount = 0;
    const totalQuestions = 35;
    const readingKeys = unit.readingKeys || {};

    for (let i = 1; i <= 35; i++) {
      const qKey = `${unit.id}_r_${i}`;
      const userAns = state.answers[qKey];
      const correctAns = readingKeys[i];

      const qBox = document.getElementById(`q-${i}`);
      if (qBox) {
        qBox.querySelectorAll('.option-item').forEach(opt => {
          const optVal = opt.dataset.opt;
          opt.classList.remove('correct', 'wrong');
          if (optVal === correctAns) opt.classList.add('correct');
          if (userAns && userAns !== correctAns && optVal === userAns) opt.classList.add('wrong');
        });

        const expEl = document.getElementById(`exp-${qKey}`);
        if (expEl) expEl.style.display = 'block';
      }

      if (userAns === correctAns) correctCount++;
    }

    const rawRatio = correctCount / totalQuestions;
    const cambridgeScore = Math.round(120 + rawRatio * 50);

    let band = 'CEFR Level A2 (Chưa đạt B1)';
    let color = '#ef4444';
    if (cambridgeScore >= 160) {
      band = 'Pass with Distinction (Đạt B2 Xuất Sắc)';
      color = '#10b981';
    } else if (cambridgeScore >= 153) {
      band = 'Pass with Merit (Đạt Giỏi B1)';
      color = '#3b82f6';
    } else if (cambridgeScore >= 140) {
      band = 'Pass (Đạt Chuẩn B1 Preliminary)';
      color = '#06b6d4';
    }

    // Save unit progress
    if (!state.unitProgress[unit.id]) state.unitProgress[unit.id] = {};
    state.unitProgress[unit.id].status = 'completed';
    state.unitProgress[unit.id].score = cambridgeScore;
    state.stats.completedTests = Object.values(state.unitProgress).filter(p => p.status === 'completed').length;
    state.stats.avgScore = cambridgeScore;
    saveState();
    updateGlobalStats();

    showScoreModal({
      unit: unit,
      title: `${unit.title} - Kết Quả Bài Thi`,
      correct: correctCount,
      total: totalQuestions,
      scaledScore: cambridgeScore,
      band: band,
      bandColor: color
    });
  }

  function startTimer() {
    stopTimer();
    state.timerSeconds = 50 * 60;
    updateTimerDisplay();
    state.timerInterval = setInterval(() => {
      state.timerSeconds--;
      updateTimerDisplay();
      if (state.timerSeconds <= 0) {
        stopTimer();
        alert('Hết giờ làm bài! Hệ thống đang chấm điểm bài thi của bạn.');
        const units = window.PET_DATA.units || [];
        const u = units.find(item => item.id === state.currentUnitId) || units[0];
        gradeExamForUnit(u);
      }
    }, 1000);
  }

  function stopTimer() {
    if (state.timerInterval) {
      clearInterval(state.timerInterval);
      state.timerInterval = null;
    }
  }

  function updateTimerDisplay() {
    const el = document.getElementById('timer-val');
    if (!el) return;
    const m = Math.floor(state.timerSeconds / 60);
    const s = state.timerSeconds % 60;
    el.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  function showScoreModal(data) {
    let overlay = document.getElementById('score-modal-overlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'score-modal-overlay';
      overlay.className = 'modal-overlay';
      document.body.appendChild(overlay);
    }

    overlay.innerHTML = `
      <div class="scorecard-modal">
        <h2 style="font-size: 1.45rem; margin-bottom: 0.4rem;">${data.title}</h2>
        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem;">Thang điểm chuẩn Cambridge English Scale</p>

        <div class="score-circle">
          <div class="score-num">${data.scaledScore}</div>
          <div class="score-total">/ 170 Score</div>
        </div>

        <div style="font-size: 1.15rem; font-weight: 800; color: ${data.bandColor}; margin-bottom: 0.5rem;">
          ${data.band}
        </div>

        <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 1.5rem;">
          Bạn đã làm đúng <strong>${data.correct}</strong> trên tổng số <strong>${data.total}</strong> câu hỏi (${Math.round((data.correct/data.total)*100)}%).
        </p>

        <div style="display: flex; gap: 0.85rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-primary" id="btn-close-modal">🔍 Xem Lời Giải & Giải Thích Chi Tiết</button>
          <button class="btn-secondary" id="btn-retake-exam">🔄 Làm Lại Bài Này</button>
          <button class="btn-secondary" data-jump-tab="roadmap">🗺️ Về Lộ Trình 12 Unit</button>
        </div>
      </div>
    `;

    overlay.classList.add('active');
    document.getElementById('btn-close-modal').addEventListener('click', () => {
      overlay.classList.remove('active');
    });

    const retakeBtn = document.getElementById('btn-retake-exam');
    if (retakeBtn && data.unit) {
      retakeBtn.addEventListener('click', () => {
        for (let i = 1; i <= 35; i++) {
          delete state.answers[`${data.unit.id}_r_${i}`];
        }
        saveState();
        renderExamQuestionsForUnit(data.unit);
        overlay.classList.remove('active');
      });
    }

    overlay.querySelectorAll('[data-jump-tab]').forEach(btn => {
      btn.addEventListener('click', () => {
        overlay.classList.remove('active');
        switchTab(btn.dataset.jumpTab);
      });
    });
  }

  // ========================================================
  // 3. LISTENING LAB VIEW (ALL 12 UNITS)
  // ========================================================
  function renderListeningLab() {
    const container = document.getElementById('listening-workspace');
    if (!container) return;

    const units = window.PET_DATA.units || [];
    const currentUnit = units.find(u => u.id === state.currentUnitId) || units[0];

    container.innerHTML = `
      <div class="audio-player-dock">
        <div class="audio-track-info">
          <div class="audio-disk">🎧</div>
          <div>
            <div style="font-size: 1.05rem; font-weight: 800;" class="track-title">${currentUnit.title} - Listening Lab</div>
            <div style="font-size: 0.8rem; color: var(--text-muted);">Phát âm thanh tự động Web Speech Engine • Đáp án khoanh đỏ chính xác</div>
          </div>
        </div>

        <div class="audio-controls">
          <button class="btn-secondary" id="btn-audio-rewind">↺ Phát lại</button>
          <button class="btn-play-lg" id="btn-master-play">▶️</button>
          <button class="btn-secondary" id="btn-audio-stop">⏹ Dừng</button>
          <select id="audio-speed-select" class="speed-select">
            <option value="0.85">0.85x (Chậm)</option>
            <option value="1.0" selected>1.0x (Chuẩn B1)</option>
            <option value="1.2">1.2x (Nâng cao)</option>
          </select>
          <select id="listening-unit-switch" class="speed-select" style="font-weight: 700;">
            ${units.map(u => `
              <option value="${u.id}" ${u.id === currentUnit.id ? 'selected' : ''}>
                Unit ${u.unitNumber}: ${u.title.split(':')[1] || u.title}
              </option>
            `).join('')}
          </select>
        </div>
      </div>

      <div id="listening-parts-container"></div>
    `;

    document.getElementById('audio-speed-select').addEventListener('change', (e) => {
      state.audio.speed = parseFloat(e.target.value);
    });

    document.getElementById('listening-unit-switch').addEventListener('change', (e) => {
      state.currentUnitId = e.target.value;
      renderListeningLab();
    });

    document.getElementById('btn-master-play').addEventListener('click', () => {
      if (state.audio.isPlaying) {
        stopAudio();
      } else {
        const textToRead = `${currentUnit.title}, Paper 2 Listening. Listen carefully to the instructions and questions.`;
        playAudioText(textToRead, currentUnit.title);
      }
    });

    document.getElementById('btn-audio-stop').addEventListener('click', () => stopAudio());
    document.getElementById('btn-audio-rewind').addEventListener('click', () => {
      if (state.audio.currentText) playAudioText(state.audio.currentText, state.audio.trackName);
    });

    renderListeningPartsForUnit(currentUnit);
  }

  function renderListeningPartsForUnit(unit) {
    const container = document.getElementById('listening-parts-container');
    if (!container) return;

    // Check if practice test data has full digital listening for this unit
    const testId = unit.practiceTestId || `test_${unit.unitNumber}`;
    const testData = window.PET_DATA.practiceTests.find(t => t.id === testId);
    if (testData && testData.listening) {
      renderListeningPartsFromTestData(testData, container, unit);
      return;
    }

    // Units 3 to 10: Listening test sheet with clean Part 1 picture cards & master keys
    const listeningKeys = unit.listeningKeys || {};
    const listenPages = [unit.scanPages[unit.scanPages.length - 3], unit.scanPages[unit.scanPages.length - 2], unit.scanPages[unit.scanPages.length - 1]];

    let html = `
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.75rem; margin-bottom: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h3 style="font-size: 1.25rem; color: #22d3ee; font-weight: 800;">Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)</h3>
            <p style="color: var(--text-muted); font-size: 0.88rem;">Hình ảnh tranh câu hỏi được trích xuất sắc nét từ sách gốc. Lắng nghe và chọn đáp án A, B hoặc C.</p>
          </div>
          <button class="btn-secondary btn-quick-page" data-page="${listenPages[0]}">
            📄 Xem trang gốc ${listenPages[0]}
          </button>
        </div>

        <div style="display: flex; flex-direction: column; gap: 2rem;">
          ${[1,2,3,4,5,6,7].map(q => {
            const qKey = `${unit.id}_l_${q}`;
            const currentAns = state.answers[qKey];
            const correct = listeningKeys[q];

            return `
              <div class="q-container" id="lq-${q}" style="margin-bottom: 2rem; padding: 1.75rem;">
                <div class="q-header">
                  <span class="q-num-badge">Câu ${q}</span>
                  <button class="btn-secondary btn-speak-q" data-text="Question ${q}. What is the correct picture? A, B or C?" style="padding: 0.35rem 0.85rem; font-size: 0.85rem;">
                    🔊 Nghe câu hỏi ${q}
                  </button>
                </div>
                <div style="margin: 1rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1.5px solid var(--border); background: #fff; padding: 0.65rem; text-align: center;">
                  <img src="assets/listening/t${unit.unitNumber}_q${q}.png" alt="Question ${q}" style="max-width: 100%; height: auto; display: inline-block;">
                </div>
                <div class="options-group" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.85rem;">
                  ${['A','B','C'].map(opt => `
                    <div class="option-item ${currentAns === opt ? 'selected' : ''}" data-qkey="${qKey}" data-opt="${opt}">
                      <div class="option-key">${opt}</div>
                      <div class="option-text">Lựa chọn ${opt}</div>
                    </div>
                  `).join('')}
                </div>
                <div class="explanation-box" id="exp-${qKey}" style="display: none; margin-top: 1rem;">
                  <div class="explanation-title">💡 Đáp án chính xác theo sách: ${correct}</div>
                  <div>Đáp án đã được đối chiếu chuẩn xác với tài liệu Cambridge.</div>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>

      <!-- Part 2 -->
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.75rem; margin-bottom: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h3 style="font-size: 1.25rem; color: #22d3ee; font-weight: 800;">Part 2: Questions 8 - 13 (Phỏng vấn / Đối thoại dài)</h3>
            <p style="color: var(--text-muted); font-size: 0.88rem;">Trang ${listenPages[1]} của sách gốc • Chọn phương án A, B hoặc C</p>
          </div>
          <button class="btn-secondary btn-quick-page" data-page="${listenPages[1]}">
            📄 Xem trang ${listenPages[1]}
          </button>
        </div>

        <div style="display: flex; flex-direction: column; gap: 1.5rem;">
          ${[8,9,10,11,12,13].map(q => {
            const qKey = `${unit.id}_l_${q}`;
            const currentAns = state.answers[qKey];
            const correct = listeningKeys[q];

            return `
              <div class="q-container" id="lq-${q}">
                <div class="q-header">
                  <span class="q-num-badge">Câu ${q}</span>
                  <button class="btn-icon btn-speak-q" data-text="Question ${q}." style="width: 32px; height: 32px; font-size: 0.85rem;">🔊</button>
                </div>
                <div class="options-group" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.85rem;">
                  ${['A','B','C'].map(opt => `
                    <div class="option-item ${currentAns === opt ? 'selected' : ''}" data-qkey="${qKey}" data-opt="${opt}">
                      <div class="option-key">${opt}</div>
                      <div class="option-text">Lựa chọn ${opt}</div>
                    </div>
                  `).join('')}
                </div>
                <div class="explanation-box" id="exp-${qKey}" style="display: none; margin-top: 0.75rem; font-size: 0.88rem;">
                  💡 Đáp án đúng theo sách: <strong>${correct}</strong>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>

      <!-- Part 3: Gap-fill -->
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.75rem; margin-bottom: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h3 style="font-size: 1.25rem; color: #22d3ee; font-weight: 800;">Part 3: Questions 14 - 19 (Điền thông tin vào chỗ trống)</h3>
            <p style="color: var(--text-muted); font-size: 0.88rem;">Trang ${listenPages[2]} • Điền từ hoặc số ngắn cần nghe được vào chỗ trống</p>
          </div>
          <button class="btn-secondary btn-quick-page" data-page="${listenPages[2]}">
            📄 Xem trang ${listenPages[2]}
          </button>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
          ${[14,15,16,17,18,19].map(q => {
            const qKey = `${unit.id}_l_${q}`;
            const currentAns = state.answers[qKey] || '';
            const correct = listeningKeys[q];

            return `
              <div style="background: var(--bg-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1.5px solid var(--border);">
                <label style="font-weight: 800; font-size: 0.92rem; display: block; margin-bottom: 0.5rem; color: var(--primary);">
                  Vị trí (${q}):
                </label>
                <input type="text" class="input-gap-fill" data-qkey="${qKey}" value="${currentAns}" placeholder="Nhập từ cần điền..." style="width: 100%; padding: 0.7rem 0.95rem; background: var(--bg-main); border: 1.5px solid var(--border); border-radius: var(--radius-sm); color: var(--text-main); font-size: 1rem; font-weight: 600;">
                <div class="explanation-box" id="exp-${qKey}" style="display: none; margin-top: 0.75rem; font-size: 0.88rem;">
                  💡 <strong>Đáp án chính xác:</strong> ${correct}
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>

      <!-- Part 4: YES / NO -->
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.75rem; margin-bottom: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h3 style="font-size: 1.25rem; color: #22d3ee; font-weight: 800;">Part 4: Questions 20 - 25 (Đàm luận Đúng / Sai - YES / NO)</h3>
            <p style="color: var(--text-muted); font-size: 0.88rem;">Trang ${listenPages[2]} • Chọn YES (Đúng) hoặc NO (Sai)</p>
          </div>
          <button class="btn-secondary btn-quick-page" data-page="${listenPages[2]}">
            📄 Xem trang ${listenPages[2]}
          </button>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
          ${[20,21,22,23,24,25].map(q => {
            const qKey = `${unit.id}_l_${q}`;
            const currentAns = state.answers[qKey];
            const correct = listeningKeys[q];

            return `
              <div class="q-container" id="lq-${q}">
                <div class="q-header">
                  <span class="q-num-badge">Câu ${q}</span>
                </div>
                <div class="options-group" style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.65rem;">
                  <div class="option-item ${currentAns === 'YES' ? 'selected' : ''}" data-qkey="${qKey}" data-opt="YES">
                    <div class="option-key">A</div>
                    <div class="option-text">YES (Đúng)</div>
                  </div>
                  <div class="option-item ${currentAns === 'NO' ? 'selected' : ''}" data-qkey="${qKey}" data-opt="NO">
                    <div class="option-key">B</div>
                    <div class="option-text">NO (Sai)</div>
                  </div>
                </div>
                <div class="explanation-box" id="exp-${qKey}" style="display: none; margin-top: 0.75rem; font-size: 0.88rem;">
                  💡 Đáp án đúng: <strong>${correct}</strong>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>

      <div style="text-align: center; margin: 3rem 0;">
        <button class="btn-primary" id="btn-submit-listening" style="padding: 1rem 3rem; font-size: 1.15rem; font-weight: 800; border-radius: var(--radius-full); box-shadow: 0 4px 20px var(--primary-glow);">
          🎯 Nộp Bài Nghe & Chấm Điểm
        </button>
      </div>
    `;

    container.innerHTML = html;

    // Bind clicks
    container.querySelectorAll('.btn-quick-page').forEach(b => {
      b.addEventListener('click', () => showPageZoomModal(b.dataset.page));
    });

    container.querySelectorAll('.btn-speak-q').forEach(b => {
      b.addEventListener('click', () => playAudioText(b.dataset.text, 'Listening Question'));
    });

    container.querySelectorAll('.option-item').forEach(opt => {
      opt.addEventListener('click', () => {
        const qKey = opt.dataset.qkey;
        const val = opt.dataset.opt;
        state.answers[qKey] = val;
        saveState();

        const parent = opt.closest('.options-group');
        parent.querySelectorAll('.option-item').forEach(o => o.classList.remove('selected'));
        opt.classList.add('selected');

        // TUYỆT ĐỐI KHÔNG hiện giải thích khi đang làm bài nghe!
      });
    });

    container.querySelectorAll('.input-gap-fill').forEach(input => {
      input.addEventListener('change', () => {
        const qKey = input.dataset.qkey;
        state.answers[qKey] = input.value.trim();
        saveState();
      });
    });

    const submitBtn = document.getElementById('btn-submit-listening');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => gradeListeningForUnit(unit, null));
    }
  }

  function renderListeningPartsFromTestData(testData, container, unit) {
    let html = '';
    const currentUnit = unit || window.PET_DATA.units.find(u => u.practiceTestId === testData.id) || window.PET_DATA.units[0];

    testData.listening.parts.forEach(part => {
      html += `
        <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
            <div>
              <h3 style="font-size: 1.25rem; font-weight: 800; color: #22d3ee;">${part.title}</h3>
              <p style="color: var(--text-muted); font-size: 0.88rem;">${part.instruction}</p>
            </div>
            <div style="display: flex; gap: 0.5rem;">
              <button class="btn-primary btn-play-part" data-part="${part.partNumber}" style="padding: 0.45rem 1rem; font-size: 0.85rem;">
                ▶️ Nghe Phần ${part.partNumber}
              </button>
              <button class="btn-secondary btn-toggle-script" data-target="script-part-${part.partNumber}" style="padding: 0.45rem 1rem; font-size: 0.85rem;">
                📜 Xem Tapescript
              </button>
            </div>
          </div>

          <div id="script-part-${part.partNumber}" class="q-context-box" style="display: none; border-left-color: var(--secondary); background: rgba(15, 23, 42, 0.75); margin-bottom: 1.75rem;">
            <h4 style="color: var(--secondary); font-size: 0.95rem; margin-bottom: 0.5rem;">📜 Audio Tapescript:</h4>
            <div style="white-space: pre-line; font-size: 0.9rem; line-height: 1.6;">${part.audioScript || 'Tapescript available below.'}</div>
          </div>
      `;

      if (part.partNumber === 1 && part.questions) {
        html += `<div style="display: flex; flex-direction: column; gap: 2.25rem;">`;
        part.questions.forEach(q => {
          const qKey = `${testData.id}_l_${q.number}`;
          const currentAns = state.answers[qKey];

          html += `
            <div class="q-container" id="lq-${q.number}" style="padding-bottom: 1.75rem;">
              <div class="q-header">
                <span class="q-num-badge">Câu ${q.number}</span>
                <button class="btn-secondary btn-play-q" data-script="${encodeURIComponent(q.audioScript)}" data-title="Câu ${q.number}: ${q.question}" style="padding: 0.35rem 0.85rem; font-size: 0.85rem;">
                  🔊 Nghe câu ${q.number}
                </button>
              </div>

              <div class="q-prompt-text" style="margin: 0.85rem 0 1rem 0;">
                <span class="q-prompt-icon">❓</span>
                <span>${q.question}</span>
              </div>

              <div style="margin: 1rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1.5px solid var(--border); background: #fff; padding: 0.65rem; text-align: center;">
                <img src="${q.image}" alt="Question ${q.number}" style="max-width: 100%; height: auto; display: inline-block;">
              </div>

              <div class="options-group" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.85rem;">
                ${q.options.map(opt => `
                  <div class="option-item ${currentAns === opt.key ? 'selected' : ''}" data-qkey="${qKey}" data-opt="${opt.key}">
                    <div class="option-key">${opt.key}</div>
                    <div class="option-text">${opt.label}</div>
                  </div>
                `).join('')}
              </div>

              <div class="explanation-box" id="exp-${qKey}" style="display: none; margin-top: 1.15rem;">
                <div class="explanation-title">💡 Lời thoại & Giải thích (Đáp án: ${q.correct})</div>
                <div style="font-style: italic; margin-bottom: 0.4rem; white-space: pre-line;">${q.audioScript}</div>
                <div>${q.explanation}</div>
              </div>
            </div>
          `;
        });
        html += `</div>`;
      }

      if (part.partNumber === 2 && part.questions) {
        html += `<div style="display: flex; flex-direction: column; gap: 1.5rem;">`;
        part.questions.forEach(q => {
          const qKey = `${testData.id}_l_${q.number}`;
          const currentAns = state.answers[qKey];
          html += `
            <div class="q-container" id="lq-${q.number}">
              <div class="q-header">
                <span class="q-num-badge">Câu ${q.number}</span>
              </div>
              <div class="q-prompt-text">
                <span class="q-prompt-icon">❓</span>
                <span>${q.question}</span>
              </div>
              <div class="options-group">
                ${q.options.map(opt => `
                  <div class="option-item ${currentAns === opt.key ? 'selected' : ''}" data-qkey="${qKey}" data-opt="${opt.key}">
                    <div class="option-key">${opt.key}</div>
                    <div class="option-text">${opt.text}</div>
                  </div>
                `).join('')}
              </div>
              <div class="explanation-box" id="exp-${qKey}" style="display: none;">
                <div class="explanation-title">💡 Giải thích (Đáp án: ${q.correct})</div>
                <div>${q.explanation}</div>
              </div>
            </div>
          `;
        });
        html += `</div>`;
      }

      if (part.partNumber === 3) {
        html += `
          <div class="q-context-box" style="margin-bottom: 1.5rem; line-height: 1.8;">
            ${part.notesContext.replace(/\n/g, '<br>')}
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
        `;
        part.questions.forEach(q => {
          const qKey = `${testData.id}_l_${q.number}`;
          const currentAns = state.answers[qKey] || '';
          html += `
            <div style="background: var(--bg-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1.5px solid var(--border);">
              <label style="font-weight: 800; font-size: 0.92rem; display: block; margin-bottom: 0.5rem; color: var(--primary);">
                Vị trí (${q.number}) - ${q.prompt}:
              </label>
              <input type="text" class="input-gap-fill" data-qkey="${qKey}" value="${currentAns}" placeholder="Nhập từ cần điền..." style="width: 100%; padding: 0.7rem 0.95rem; background: var(--bg-main); border: 1.5px solid var(--border); border-radius: var(--radius-sm); color: var(--text-main); font-size: 1rem; font-weight: 600;">
              <div class="explanation-box" id="exp-${qKey}" style="display: none; margin-top: 0.75rem; font-size: 0.88rem;">
                <strong>Đáp án đúng:</strong> ${q.acceptedAnswers.join(' / ')}<br>${q.explanation}
              </div>
            </div>
          `;
        });
        html += `</div>`;
      }

      if (part.partNumber === 4 && part.questions) {
        html += `<div style="display: flex; flex-direction: column; gap: 1.5rem;">`;
        part.questions.forEach(q => {
          const qKey = `${testData.id}_l_${q.number}`;
          const currentAns = state.answers[qKey];
          html += `
            <div class="q-container" id="lq-${q.number}">
              <div class="q-header"><span class="q-num-badge">Câu ${q.number}</span></div>
              <div class="q-prompt-text">
                <span class="q-prompt-icon">📝</span>
                <span>${q.statement}</span>
              </div>
              <div class="options-group" style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.85rem;">
                <div class="option-item ${currentAns === 'YES' ? 'selected' : ''}" data-qkey="${qKey}" data-opt="YES">
                  <div class="option-key">A</div>
                  <div class="option-text">ĐÚNG (YES)</div>
                </div>
                <div class="option-item ${currentAns === 'NO' ? 'selected' : ''}" data-qkey="${qKey}" data-opt="NO">
                  <div class="option-key">B</div>
                  <div class="option-text">SAI (NO)</div>
                </div>
              </div>
              <div class="explanation-box" id="exp-${qKey}" style="display: none;">
                <div class="explanation-title">💡 Giải thích (Đáp án: ${q.correct})</div>
                <div>${q.explanation}</div>
              </div>
            </div>
          `;
        });
        html += `</div>`;
      }

      html += `</div>`;
    });

    html += `
      <div style="text-align: center; margin: 3rem 0;">
        <button class="btn-primary" id="btn-submit-listening" style="padding: 1rem 3rem; font-size: 1.15rem; font-weight: 800; border-radius: var(--radius-full); box-shadow: 0 4px 20px var(--primary-glow);">
          🎯 Nộp Bài Nghe & Chấm Điểm
        </button>
      </div>
    `;

    container.innerHTML = html;

    container.querySelectorAll('.btn-play-q').forEach(btn => {
      btn.addEventListener('click', () => {
        const script = decodeURIComponent(btn.dataset.script);
        playAudioText(script, btn.dataset.title);
      });
    });

    container.querySelectorAll('.btn-play-part').forEach(btn => {
      btn.addEventListener('click', () => {
        const pNum = parseInt(btn.dataset.part);
        const p = testData.listening.parts.find(item => item.partNumber === pNum);
        if (p) playAudioText(p.audioScript, `${testData.title} Part ${pNum}`);
      });
    });

    container.querySelectorAll('.btn-toggle-script').forEach(btn => {
      btn.addEventListener('click', () => {
        const target = document.getElementById(btn.dataset.target);
        if (target) {
          const isHidden = target.style.display === 'none';
          target.style.display = isHidden ? 'block' : 'none';
          btn.textContent = isHidden ? '🙈 Ẩn Tapescript' : '📜 Xem Tapescript';
        }
      });
    });

    container.querySelectorAll('.option-item').forEach(opt => {
      opt.addEventListener('click', () => {
        const qKey = opt.dataset.qkey;
        state.answers[qKey] = opt.dataset.opt;
        saveState();

        const parent = opt.closest('.options-group');
        parent.querySelectorAll('.option-item').forEach(o => o.classList.remove('selected'));
        opt.classList.add('selected');

        // TUYỆT ĐỐI KHÔNG hiện giải thích khi đang làm bài nghe!
      });
    });

    container.querySelectorAll('.input-gap-fill').forEach(input => {
      input.addEventListener('change', () => {
        state.answers[input.dataset.qkey] = input.value.trim();
        saveState();
      });
    });

    const submitBtn = document.getElementById('btn-submit-listening');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => gradeListeningForUnit(currentUnit, testData));
    }
  }

  function gradeListeningForUnit(unit, testData) {
    let correctCount = 0;
    const totalQuestions = 25;
    const listeningKeys = unit.listeningKeys || {};

    for (let i = 1; i <= 25; i++) {
      const qKey = testData ? `${testData.id}_l_${i}` : `${unit.id}_l_${i}`;
      const userAns = state.answers[qKey];
      const correctAns = listeningKeys[i];

      // Part 1, 2, 4 option items
      const qBox = document.getElementById(`lq-${i}`) || document.querySelector(`[data-qkey="${qKey}"]`)?.closest('.q-container');
      if (qBox) {
        qBox.querySelectorAll('.option-item').forEach(opt => {
          const optVal = opt.dataset.opt;
          opt.classList.remove('correct', 'wrong');
          if (optVal === correctAns) opt.classList.add('correct');
          if (userAns && userAns !== correctAns && optVal === userAns) opt.classList.add('wrong');
        });
      }

      // Part 3 gap fill
      const gapInput = document.querySelector(`.input-gap-fill[data-qkey="${qKey}"]`);
      if (gapInput) {
        let isCorrect = false;
        if (userAns) {
          const userTrim = userAns.trim().toLowerCase();
          const targetPart = testData?.listening?.parts?.find(p => p.partNumber === 3);
          const qObj = targetPart?.questions?.find(q => q.number === i);
          const accepted = qObj ? qObj.acceptedAnswers.map(a => a.toLowerCase()) : [String(correctAns).toLowerCase()];
          if (accepted.some(a => userTrim.includes(a) || a.includes(userTrim))) {
            isCorrect = true;
          }
        }
        if (isCorrect) {
          gapInput.style.borderColor = 'var(--success)';
          gapInput.style.background = 'rgba(16, 185, 129, 0.15)';
          correctCount++;
        } else if (userAns) {
          gapInput.style.borderColor = 'var(--error)';
          gapInput.style.background = 'rgba(239, 68, 68, 0.15)';
        }
      } else {
        if (userAns && userAns.toUpperCase() === String(correctAns).toUpperCase()) {
          correctCount++;
        }
      }

      const expEl = document.getElementById(`exp-${qKey}`);
      if (expEl) expEl.style.display = 'block';
    }

    const rawRatio = correctCount / totalQuestions;
    const cambridgeScore = Math.round(120 + rawRatio * 50);

    let band = 'CEFR Level A2 (Chưa đạt B1)';
    let color = '#ef4444';
    if (cambridgeScore >= 160) {
      band = 'Pass with Distinction (Đạt B2 Xuất Sắc)';
      color = '#10b981';
    } else if (cambridgeScore >= 153) {
      band = 'Pass with Merit (Đạt Giỏi B1)';
      color = '#3b82f6';
    } else if (cambridgeScore >= 140) {
      band = 'Pass (Đạt Chuẩn B1 Preliminary)';
      color = '#06b6d4';
    }

    showScoreModal({
      unit: unit,
      title: `${unit.title} - Kết Quả Phần Nghe (Listening)`,
      correct: correctCount,
      total: totalQuestions,
      scaledScore: cambridgeScore,
      band: band,
      bandColor: color
    });
  }


    // ========================================================
  // 4. WRITING STUDIO
  // ========================================================
  function renderWritingStudio() {
    const container = document.getElementById('writing-workspace');
    if (!container) return;

    const testIdx = (state.writing && state.writing.currentTestIndex !== undefined) ? state.writing.currentTestIndex : 0;
    const currentTest = window.PET_DATA.practiceTests[testIdx] || window.PET_DATA.practiceTests[0];

    const currentUnit = window.PET_DATA.units[testIdx] || { title: `Practice Test ${testIdx + 1}` };

    let html = `
      <div class="test-header-bar">
        <div class="test-title-group">
          <h2>Writing Studio: Unit ${testIdx + 1} (${currentUnit.title.split(':')[1] || currentUnit.title})</h2>
          <p>Luyện tập trọn bộ 3 phần thi viết chuẩn Cambridge: Viết lại câu • Thư ngắn 35-45 từ • Bài văn/Truyện 100 từ</p>
        </div>
        <div>
          <select id="writing-test-select" class="speed-select" style="padding: 0.55rem 1rem; font-weight: 700;">
            ${window.PET_DATA.practiceTests.map((t, idx) => {
              const u = window.PET_DATA.units[idx];
              const label = u ? `Unit ${idx + 1}: ${u.title.split(':')[1] || u.title}` : `Practice Test ${idx + 1}`;
              return `<option value="${idx}" ${idx === testIdx ? 'selected' : ''}>${label}</option>`;
            }).join('')}
          </select>
        </div>
      </div>
    `;

    const p1 = currentTest.writing.parts[0];
    html += `
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
        <h3 style="font-size: 1.25rem; font-weight: 800; color: #fbbf24; margin-bottom: 0.5rem;">${p1.title}</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem;">${p1.instruction}</p>
    `;

    p1.questions.forEach(q => {
      html += `
        <div style="background: var(--bg-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border); margin-bottom: 1.25rem;">
          <div style="font-weight: 700; margin-bottom: 0.4rem; color: var(--text-muted);">Câu gốc:</div>
          <div style="font-size: 1rem; margin-bottom: 0.85rem; font-weight: 600;">${q.first}</div>
          <div style="font-weight: 700; margin-bottom: 0.4rem; color: var(--primary);">Câu viết lại:</div>
          <div style="font-size: 1rem; margin-bottom: 0.85rem;">
            ${q.second.replace('[GAP]', `<input type="text" class="input-trans" id="trans-input-${q.number}" placeholder="Điền từ..." style="padding: 0.35rem 0.75rem; background: var(--bg-main); border: 1.5px solid var(--primary); border-radius: var(--radius-sm); color: var(--text-main); font-weight: 700; min-width: 180px;">`)}
          </div>
          <div style="display: flex; gap: 0.75rem; align-items: center;">
            <button class="btn-primary btn-check-trans" data-qnum="${q.number}" style="padding: 0.4rem 1rem; font-size: 0.82rem;">Kiểm tra đáp án</button>
            <span id="trans-result-${q.number}" style="font-size: 0.9rem; font-weight: 700;"></span>
          </div>
          <div id="trans-exp-${q.number}" style="display: none; margin-top: 0.75rem; font-size: 0.85rem; color: var(--text-muted);">
            💡 <strong>Đáp án được chấp nhận:</strong> ${q.acceptedAnswers.join(' / ')}<br>${q.explanation}
          </div>
        </div>
      `;
    });
    html += `</div>`;

    const p2 = currentTest.writing.parts[1];
    html += `
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
        <h3 style="font-size: 1.25rem; font-weight: 800; color: #fbbf24; margin-bottom: 0.5rem;">${p2.title}</h3>
        <div class="q-context-box" style="white-space: pre-line; margin-bottom: 1.25rem;">${p2.prompt}</div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; align-items: start;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-weight: 700; font-size: 0.9rem;">Khung soạn thảo bài làm của bạn:</span>
              <span id="word-count-p2" style="font-weight: 800; font-size: 0.85rem; color: var(--primary);">0 từ (Mục tiêu: 35 - 45 từ)</span>
            </div>
            <textarea id="editor-p2" rows="6" placeholder="Bắt đầu viết bài của bạn tại đây..." style="width: 100%; padding: 1rem; background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius-md); color: var(--text-main); font-family: inherit; font-size: 0.95rem; line-height: 1.6; resize: vertical;"></textarea>
          </div>

          <div style="background: var(--bg-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border);">
            <div style="font-weight: 800; color: #10b981; margin-bottom: 0.5rem;">⭐ Bài Mẫu Chuẩn Band 5:</div>
            <div style="font-size: 0.92rem; line-height: 1.6; white-space: pre-line; margin-bottom: 1rem; font-style: italic;">
              "${p2.sampleAnswer}"
            </div>
            <div style="font-size: 0.82rem; color: var(--text-muted);">
              <strong>Các điểm trọng tâm đã đáp ứng:</strong><br>
              ${p2.keyPoints.map(k => `✓ ${k}`).join('<br>')}
            </div>
          </div>
        </div>
      </div>
    `;

    const p3 = currentTest.writing.parts[2];
    html += `
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
        <h3 style="font-size: 1.25rem; font-weight: 800; color: #fbbf24; margin-bottom: 0.5rem;">${p3.title}</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem;">Chọn viết Câu hỏi 7 (Viết thư cho bạn) hoặc Câu hỏi 8 (Viết truyện ngắn khoảng 100 từ):</p>
    `;

    p3.tasks.forEach(task => {
      html += `
        <div style="background: var(--bg-surface); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border); margin-bottom: 1.5rem;">
          <h4 style="font-size: 1.1rem; color: var(--primary); margin-bottom: 0.5rem;">Câu hỏi ${task.number}: ${task.type}</h4>
          <div class="q-context-box" style="white-space: pre-line; margin-bottom: 1rem;">${task.prompt}</div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; align-items: start;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-weight: 700; font-size: 0.9rem;">Bài làm của bạn:</span>
                <span id="word-count-task-${task.number}" style="font-weight: 800; font-size: 0.85rem; color: var(--secondary);">0 từ (Mục tiêu: ~100 từ)</span>
              </div>
              <textarea id="editor-task-${task.number}" rows="8" placeholder="Viết bài làm khoảng 100 từ..." style="width: 100%; padding: 1rem; background: var(--bg-main); border: 1px solid var(--border); border-radius: var(--radius-md); color: var(--text-main); font-family: inherit; font-size: 0.95rem; line-height: 1.6; resize: vertical;"></textarea>
            </div>

            <div style="background: rgba(15, 23, 42, 0.7); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border);">
              <div style="font-weight: 800; color: #10b981; margin-bottom: 0.5rem;">🌟 Bài Mẫu Xuất Sắc (~${task.wordCount} từ):</div>
              <div style="font-size: 0.92rem; line-height: 1.6; white-space: pre-line; font-style: italic;">
                "${task.sampleAnswer}"
              </div>
            </div>
          </div>
        </div>
      `;
    });
    html += `</div>`;

    container.innerHTML = html;

    container.querySelectorAll('.btn-check-trans').forEach(btn => {
      btn.addEventListener('click', () => {
        const qNum = parseInt(btn.dataset.qnum);
        const q = p1.questions.find(item => item.number === qNum);
        const input = document.getElementById(`trans-input-${qNum}`);
        const resEl = document.getElementById(`trans-result-${qNum}`);
        const expEl = document.getElementById(`trans-exp-${qNum}`);

        const userText = (input.value || '').trim().toLowerCase();
        const isCorrect = q.acceptedAnswers.some(ans => ans.toLowerCase() === userText);

        if (isCorrect) {
          resEl.textContent = '✓ Chính xác!';
          resEl.style.color = '#10b981';
        } else {
          resEl.textContent = '✗ Chưa đúng';
          resEl.style.color = '#ef4444';
        }
        expEl.style.display = 'block';
      });
    });

    const editorP2 = document.getElementById('editor-p2');
    const wcP2 = document.getElementById('word-count-p2');
    if (editorP2 && wcP2) {
      editorP2.addEventListener('input', () => {
        const words = editorP2.value.trim().split(/\s+/).filter(Boolean).length;
        wcP2.textContent = `${words} từ (Mục tiêu: 35 - 45 từ)`;
        wcP2.style.color = (words >= 35 && words <= 45) ? '#10b981' : '#f59e0b';
      });
    }

    [7, 8].forEach(num => {
      const ed = document.getElementById(`editor-task-${num}`);
      const wc = document.getElementById(`word-count-task-${num}`);
      if (ed && wc) {
        ed.addEventListener('input', () => {
          const words = ed.value.trim().split(/\s+/).filter(Boolean).length;
          wc.textContent = `${words} từ (Mục tiêu: ~100 từ)`;
          wc.style.color = (words >= 90 && words <= 115) ? '#10b981' : '#f59e0b';
        });
      }
    });

    const wSelect = document.getElementById('writing-test-select');
    if (wSelect) {
      wSelect.addEventListener('change', (e) => {
        state.writing.currentTestIndex = parseInt(e.target.value);
        renderWritingStudio();
      });
    }
  }

  // ========================================================
  // 5. SPEAKING ARENA
  // ========================================================
  function renderSpeakingArena() {
    const container = document.getElementById('speaking-workspace');
    if (!container) return;

    const currentSpk = window.PET_DATA.speakingTests[state.speaking.currentTestIndex] || window.PET_DATA.speakingTests[0];

    container.innerHTML = `
      <div class="test-header-bar">
        <div class="test-title-group">
          <h2>${currentSpk.title}: ${currentSpk.topic}</h2>
          <p>Tranh màu gốc từ sách • Giám khảo đọc câu hỏi • Gợi ý câu trả lời chuẩn</p>
        </div>
        <div>
          <select id="speaking-test-select" class="speed-select" style="padding: 0.55rem 1rem;">
            ${window.PET_DATA.speakingTests.map((t, idx) => `
              <option value="${idx}" ${idx === state.speaking.currentTestIndex ? 'selected' : ''}>${t.title} (${t.topic})</option>
            `).join('')}
          </select>
        </div>
      </div>

      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
        <h3 style="font-size: 1.25rem; font-weight: 800; color: #f472b6; margin-bottom: 0.5rem;">Part 1: Phỏng Vấn Cá Nhân (Personal Questions)</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.25rem;">Nhấp vào biểu tượng 🔊 để nghe giám khảo hỏi và tham khảo câu trả lời mẫu:</p>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          ${currentSpk.part1.questions.map((q, idx) => `
            <div style="background: var(--bg-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <div style="font-weight: 700; font-size: 1rem;">${idx + 1}. ${q}</div>
                <button class="btn-secondary btn-spk-read" data-text="${encodeURIComponent(q)}" style="padding: 0.35rem 0.85rem; font-size: 0.82rem;">
                  🔊 Giám khảo hỏi
                </button>
              </div>
              <div style="font-size: 0.92rem; color: #10b981; font-style: italic;">
                💬 Gợi ý trả lời: "${currentSpk.part1.sampleAnswers[idx]}"
              </div>
            </div>
          `).join('')}
        </div>
      </div>

      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
        <h3 style="font-size: 1.25rem; font-weight: 800; color: #f472b6; margin-bottom: 0.5rem;">${currentSpk.part2.title}</h3>
        <div class="q-context-box" style="margin-bottom: 1.5rem;">${currentSpk.part2.scenario}</div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; align-items: start;">
          <div style="background: #fff; padding: 0.5rem; border-radius: var(--radius-md); border: 1.5px solid var(--border); text-align: center;">
            <img src="${currentSpk.part2.image}" alt="Speaking Part 2" style="max-width: 100%; height: auto; border-radius: var(--radius-sm);">
          </div>

          <div style="background: var(--bg-surface); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border);">
            <h4 style="font-size: 1rem; color: var(--primary); margin-bottom: 0.75rem;">💬 Đoạn hội thoại mẫu hoàn chỉnh:</h4>
            <div style="font-size: 0.92rem; line-height: 1.6; margin-bottom: 1.25rem;">
              ${(currentSpk.part2.sampleDialogue || '').split(/\\n|\n/).map(line => {
                line = line.trim();
                if (!line) return '';
                const isA = line.startsWith('Candidate A:');
                const isB = line.startsWith('Candidate B:');
                const speaker = isA ? 'Candidate A' : (isB ? 'Candidate B' : '');
                const text = speaker ? line.replace(/^(Candidate [AB]:\s*)/, '') : line;
                return `
                  <div style="margin-bottom: 0.65rem; padding: 0.65rem 0.9rem; border-radius: var(--radius-sm); background: ${isA ? 'rgba(99, 102, 241, 0.08)' : 'rgba(236, 72, 153, 0.08)'}; border-left: 3px solid ${isA ? 'var(--primary)' : 'var(--secondary)'};">
                    <strong style="color: ${isA ? 'var(--primary)' : 'var(--secondary)'}; font-size: 0.85rem; display: block; margin-bottom: 0.2rem;">${speaker || 'Hội thoại'}:</strong>
                    <div style="color: var(--text); font-size: 0.92rem; line-height: 1.5;">${text}</div>
                  </div>
                `;
              }).join('')}
            </div>
            <button class="btn-primary btn-spk-read" data-text="${encodeURIComponent((currentSpk.part2.sampleDialogue || '').replace(/\\n/g, ' '))}" style="width: 100%; justify-content: center;">
              🔊 Nghe đoạn hội thoại mẫu (Audio)
            </button>
          </div>
        </div>
      </div>

      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
        <h3 style="font-size: 1.25rem; font-weight: 800; color: #f472b6; margin-bottom: 0.5rem;">${currentSpk.part3.title}</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.5rem;">Miêu tả chi tiết bức ảnh trong vòng 1 phút theo bố cục: Tiền cảnh, hậu cảnh, con người, hành động, thời tiết.</p>

        <div style="margin-bottom: 1.5rem; background: #fff; padding: 0.5rem; border-radius: var(--radius-md); border: 1.5px solid var(--border); text-align: center;">
          <img src="${currentSpk.part3.image}" alt="Speaking Part 3 Photos" style="max-width: 100%; height: auto; border-radius: var(--radius-sm);">
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
          <div style="background: var(--bg-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border);">
            <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">${currentSpk.part3.photoA.title}</h4>
            <p style="font-size: 0.92rem; line-height: 1.6; margin-bottom: 1rem;">${currentSpk.part3.photoA.description}</p>
            <button class="btn-secondary btn-spk-read" data-text="${encodeURIComponent(currentSpk.part3.photoA.description)}" style="width: 100%; justify-content: center;">
              🔊 Nghe miêu tả Photo A
            </button>
          </div>

          <div style="background: var(--bg-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border);">
            <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">${currentSpk.part3.photoB.title}</h4>
            <p style="font-size: 0.92rem; line-height: 1.6; margin-bottom: 1rem;">${currentSpk.part3.photoB.description}</p>
            <button class="btn-secondary btn-spk-read" data-text="${encodeURIComponent(currentSpk.part3.photoB.description)}" style="width: 100%; justify-content: center;">
              🔊 Nghe miêu tả Photo B
            </button>
          </div>
        </div>
      </div>

      ${currentSpk.part4 ? `
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
        <h3 style="font-size: 1.25rem; font-weight: 800; color: #f472b6; margin-bottom: 0.5rem;">${currentSpk.part4.title || 'Part 4: Thảo Luận Mở Rộng (Discussion)'}</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.5rem;">Giám khảo hỏi các câu hỏi thảo luận liên quan đến chủ đề ở Part 3. Luyện trả lời theo các gợi ý bên dưới:</p>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          ${(currentSpk.part4.questions || []).map((q, qIdx) => `
            <div style="background: var(--bg-surface); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border);">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; margin-bottom: 0.6rem;">
                <div style="font-weight: 700; color: var(--text); font-size: 0.96rem;">
                  <span style="color: var(--primary); margin-right: 0.4rem;">${qIdx + 1}.</span>${q}
                </div>
                <button class="btn-icon btn-spk-read" data-text="${encodeURIComponent(q)}" title="Nghe câu hỏi" style="padding: 0.35rem 0.75rem; font-size: 0.82rem; border-radius: var(--radius-sm); border: 1px solid var(--border); background: var(--bg-card); cursor: pointer;">🔊 Giám khảo</button>
              </div>
              ${currentSpk.part4.sampleAnswers && currentSpk.part4.sampleAnswers[qIdx] ? `
                <div style="font-size: 0.9rem; color: #10b981; line-height: 1.5; background: rgba(16, 185, 129, 0.08); padding: 0.75rem 1rem; border-radius: var(--radius-sm); border-left: 3px solid #10b981; margin-top: 0.5rem; display: flex; justify-content: space-between; align-items: center; gap: 0.75rem;">
                  <div>💬 <em>Gợi ý trả lời:</em> "${currentSpk.part4.sampleAnswers[qIdx]}"</div>
                  <button class="btn-icon btn-spk-read" data-text="${encodeURIComponent(currentSpk.part4.sampleAnswers[qIdx])}" title="Nghe câu trả lời mẫu" style="flex-shrink: 0; padding: 0.25rem 0.5rem; font-size: 0.8rem; border-radius: var(--radius-sm); border: 1px solid rgba(16, 185, 129, 0.3); background: transparent; cursor: pointer;">🔊</button>
                </div>
              ` : ''}
            </div>
          `).join('')}
        </div>
      </div>
      ` : ''}
    `;

    document.getElementById('speaking-test-select').addEventListener('change', (e) => {
      state.speaking.currentTestIndex = parseInt(e.target.value);
      renderSpeakingArena();
    });

    document.querySelectorAll('.btn-spk-read').forEach(btn => {
      btn.addEventListener('click', () => {
        playAudioText(decodeURIComponent(btn.dataset.text), 'Speaking Guide');
      });
    });
  }

  // ========================================================
  // 6. FLASHCARDS
  // ========================================================
  function renderFlashcards() {
    const container = document.getElementById('flashcards-workspace');
    if (!container) return;

    const cards = window.PET_DATA.vocabulary;
    const card = cards[state.flashcards.currentIndex] || cards[0];

    container.innerHTML = `
      <div class="test-header-bar">
        <div class="test-title-group">
          <h2>Sổ Tay Từ Vựng & Flashcards B1</h2>
          <p>Tổng hợp từ vựng và các ghi chú tiếng Việt gốc từ sách Cambridge</p>
        </div>
        <div class="badge-tag" style="margin: 0;">Thẻ ${state.flashcards.currentIndex + 1} / ${cards.length}</div>
      </div>

      <div class="flashcard-wrap" id="main-flashcard">
        <div class="flashcard ${state.flashcards.isFlipped ? 'flipped' : ''}">
          <div class="card-face card-front">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span class="badge-tag" style="margin: 0;">${card.type}</span>
              <button class="btn-icon" id="btn-card-audio">🔊</button>
            </div>
            <div style="text-align: center; margin: auto 0;">
              <div style="font-size: 2.2rem; font-weight: 800; color: var(--secondary); margin-bottom: 0.5rem;">${card.word}</div>
              <div style="font-size: 0.95rem; color: var(--text-muted); font-style: italic;">"${card.example}"</div>
            </div>
            <div style="font-size: 0.8rem; color: var(--text-dim); text-align: center;">💡 Nhấp vào thẻ để lật xem nghĩa tiếng Việt</div>
          </div>

          <div class="card-face card-back">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span class="badge-tag" style="margin: 0; background: rgba(16, 185, 129, 0.2); color: #34d399;">Nghĩa Tiếng Việt</span>
              <span style="font-size: 0.82rem; color: var(--text-muted);">${card.source}</span>
            </div>
            <div style="text-align: center; margin: auto 0;">
              <div style="font-size: 1.6rem; font-weight: 800; color: #10b981; margin-bottom: 1rem;">${card.meaning}</div>
              <div style="font-size: 0.95rem; color: var(--text-muted);">${card.example}</div>
            </div>
            <div style="font-size: 0.8rem; color: var(--text-dim); text-align: center;">Nguồn: ${card.source}</div>
          </div>
        </div>
      </div>

      <div style="display: flex; justify-content: center; gap: 1rem; margin-bottom: 3rem;">
        <button class="btn-secondary" id="btn-card-prev" ${state.flashcards.currentIndex === 0 ? 'disabled' : ''}>← Thẻ trước</button>
        <button class="btn-primary" id="btn-card-flip">🔄 Lật thẻ</button>
        <button class="btn-secondary" id="btn-card-next" ${state.flashcards.currentIndex === cards.length - 1 ? 'disabled' : ''}>Thẻ tiếp theo →</button>
      </div>

      <div class="section-heading">
        <h2>📑 Danh Sách Toàn Bộ Từ Vựng</h2>
      </div>

      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); overflow: hidden;">
        <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.92rem;">
          <thead>
            <tr style="background: var(--bg-surface); border-bottom: 1px solid var(--border);">
              <th style="padding: 1rem 1.25rem;">Từ vựng / Cụm từ</th>
              <th style="padding: 1rem 1.25rem;">Loại từ</th>
              <th style="padding: 1rem 1.25rem;">Nghĩa tiếng Việt</th>
              <th style="padding: 1rem 1.25rem;">Ví dụ ngữ cảnh</th>
              <th style="padding: 1rem 1.25rem; text-align: center;">Phát âm</th>
            </tr>
          </thead>
          <tbody>
            ${cards.map(c => `
              <tr style="border-bottom: 1px solid var(--border);">
                <td style="padding: 0.85rem 1.25rem; font-weight: 700; color: var(--secondary);">${c.word}</td>
                <td style="padding: 0.85rem 1.25rem;"><span class="badge-tag" style="margin: 0;">${c.type}</span></td>
                <td style="padding: 0.85rem 1.25rem; color: #10b981; font-weight: 600;">${c.meaning}</td>
                <td style="padding: 0.85rem 1.25rem; color: var(--text-muted); font-size: 0.88rem;">${c.example}</td>
                <td style="padding: 0.85rem 1.25rem; text-align: center;">
                  <button class="btn-icon btn-row-speak" data-word="${encodeURIComponent(c.word)}" style="width: 32px; height: 32px; font-size: 0.85rem; margin: 0 auto;">🔊</button>
                </td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;

    const cardEl = document.getElementById('main-flashcard');
    cardEl.addEventListener('click', () => {
      state.flashcards.isFlipped = !state.flashcards.isFlipped;
      cardEl.querySelector('.flashcard').classList.toggle('flipped', state.flashcards.isFlipped);
    });

    document.getElementById('btn-card-flip').addEventListener('click', (e) => {
      e.stopPropagation();
      state.flashcards.isFlipped = !state.flashcards.isFlipped;
      cardEl.querySelector('.flashcard').classList.toggle('flipped', state.flashcards.isFlipped);
    });

    document.getElementById('btn-card-prev').addEventListener('click', (e) => {
      e.stopPropagation();
      if (state.flashcards.currentIndex > 0) {
        state.flashcards.currentIndex--;
        state.flashcards.isFlipped = false;
        renderFlashcards();
      }
    });

    document.getElementById('btn-card-next').addEventListener('click', (e) => {
      e.stopPropagation();
      if (state.flashcards.currentIndex < cards.length - 1) {
        state.flashcards.currentIndex++;
        state.flashcards.isFlipped = false;
        renderFlashcards();
      }
    });

    document.getElementById('btn-card-audio').addEventListener('click', (e) => {
      e.stopPropagation();
      playAudioText(card.word, card.word);
    });

    document.querySelectorAll('.btn-row-speak').forEach(btn => {
      btn.addEventListener('click', () => {
        playAudioText(decodeURIComponent(btn.dataset.word), 'Vocab');
      });
    });
  }

  // ========================================================
  // 7. BOOK VIEWER (110 SCANNED PAGES)
  // ========================================================
  function renderBookViewer() {
    const container = document.getElementById('archive-workspace');
    if (!container) return;

    const archive = window.PET_DATA.testsArchive;
    const currentTest = archive.find(t => t.testNumber === state.archive.currentTestNum) || archive[0];

    container.innerHTML = `
      <div class="test-header-bar">
        <div class="test-title-group">
          <h2>Thư Viện 110 Trang Đề Gốc & Đáp Án Khoanh Đỏ</h2>
          <p>Scan sắc nét từ sách Cambridge Preliminary • Có sẵn key và ghi chú tiếng Việt</p>
        </div>
        <div>
          <select id="archive-test-select" class="speed-select" style="padding: 0.55rem 1rem;">
            ${archive.map(t => `
              <option value="${t.testNumber}" ${t.testNumber === state.archive.currentTestNum ? 'selected' : ''}>${t.title} (${t.pageRange})</option>
            `).join('')}
          </select>
        </div>
      </div>

      <div class="q-context-box" style="margin-bottom: 1.5rem;">
        <strong>Thông tin đề thi:</strong> ${currentTest.description}
      </div>

      <div class="section-heading">
        <h2>📄 Toàn Bộ Các Trang Của ${currentTest.title} (Bấm vào để phóng to đối chiếu đáp án)</h2>
      </div>

      <div class="book-pages-grid">
        ${getAllPagesForTest(currentTest).map(p => `
          <div class="book-page-thumb" data-page="${p}">
            <img src="assets/tests/page_${p}.jpg" alt="Trang ${p}" loading="lazy">
            <div class="book-page-info">
              <span>Trang ${p}</span>
              <span style="color: var(--primary);">Phóng to 🔍</span>
            </div>
          </div>
        `).join('')}
      </div>
    `;

    document.getElementById('archive-test-select').addEventListener('change', (e) => {
      state.archive.currentTestNum = parseInt(e.target.value);
      renderBookViewer();
    });

    document.querySelectorAll('.book-page-thumb').forEach(thumb => {
      thumb.addEventListener('click', () => {
        showPageZoomModal(thumb.dataset.page);
      });
    });
  }

  function getAllPagesForTest(testObj) {
    const pages = [];
    for (let p = testObj.readingPages[0]; p <= testObj.listeningPages[testObj.listeningPages.length - 1]; p++) {
      pages.push(p);
    }
    return pages;
  }

  function showPageZoomModal(pageNum) {
    let overlay = document.getElementById('zoom-modal-overlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'zoom-modal-overlay';
      overlay.className = 'modal-overlay';
      document.body.appendChild(overlay);
    }

    overlay.innerHTML = `
      <div style="background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius-lg); max-width: 900px; width: 100%; max-height: 92vh; overflow-y: auto; padding: 1.5rem; text-align: center; position: relative;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h3 style="font-size: 1.15rem;">Trang Sách Gốc ${pageNum} (Có Chú Thích & Key Khoanh Đỏ)</h3>
          <button class="btn-icon" id="btn-close-zoom">✕</button>
        </div>
        <img src="assets/tests/page_${pageNum}.jpg" alt="Trang ${pageNum}" style="width: 100%; height: auto; border-radius: var(--radius-md); box-shadow: var(--shadow-md);">
      </div>
    `;

    overlay.classList.add('active');
    document.getElementById('btn-close-zoom').addEventListener('click', () => {
      overlay.classList.remove('active');
    });
  }

  function updateGlobalStats() {
    const units = window.PET_DATA.units || [];
    const completed = Object.values(state.unitProgress).filter(p => p.status === 'completed').length;
    if (elements.globalStatsPill) {
      elements.globalStatsPill.textContent = `${completed}/12 Unit Xong`;
    }
    const predEl = document.getElementById('dash-score-pred');
    if (predEl && state.stats.avgScore > 0) {
      predEl.textContent = `${state.stats.avgScore}/170 B1`;
    }
  }

  window.addEventListener('DOMContentLoaded', init);
})();
