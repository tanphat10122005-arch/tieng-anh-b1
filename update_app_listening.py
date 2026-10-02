# -*- coding: utf-8 -*-
with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace renderListeningPartsForUnit and renderListeningPartsFromTestData
start_marker = "  function renderListeningPartsForUnit(unit) {"
end_marker = "  // ========================================================\n  // 4. WRITING STUDIO"

start_idx = code.find(start_marker)
end_idx = code.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers!", start_idx, end_idx)
    exit(1)

new_listening_code = '''  function renderListeningPartsForUnit(unit) {
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

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
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
                <div class="options-group" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem;">
                  ${['A','B','C'].map(opt => `
                    <div class="option-item ${currentAns === opt ? 'selected' : ''}" data-qkey="${qKey}" data-opt="${opt}">
                      <div class="option-key">${opt}</div>
                      <div class="option-text">${opt}</div>
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
            ${part.notesContext.replace(/\\n/g, '<br>')}
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
'''

code = code[:start_idx] + new_listening_code + "\n\n  " + code[end_idx:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated app.js with full digital listening and grading!")
