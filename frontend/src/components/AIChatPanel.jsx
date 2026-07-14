import React, { useEffect, useRef, useState } from 'react';
import ChatMessage from './ChatMessage';

/**
 * AIChatPanel
 * Right-hand assistant panel. Presentational only — no API calls, no AI logic.
 * The parent owns the message list and the send handler so this component
 * stays a pure, reusable UI shell.
 *
 * Props:
 * - messages: Array<{ id, sender, text, timestamp }>
 * - onSendMessage: (text: string) => void — called when the user submits a chat message
 * - isSending: boolean — optional, disables input while a message is "in flight"
 */
const AIChatPanel = ({ messages = [], onSendMessage = () => {}, isSending = false }) => {
  const [draft, setDraft] = useState('');
  const historyRef = useRef(null);

  useEffect(() => {
    if (historyRef.current) {
      historyRef.current.scrollTop = historyRef.current.scrollHeight;
    }
  }, [messages]);

  const handleSend = () => {
    const trimmed = draft.trim();
    if (!trimmed) return;
    onSendMessage(trimmed);
    setDraft('');
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <aside className="ai-panel" aria-label="AI Assistant">
      <header className="ai-panel__header">
        <div className="ai-panel__title-row">
          <span className="ai-panel__avatar" aria-hidden="true">
            🤖
          </span>
          <h2 className="ai-panel__title">AI Assistant</h2>
          <span className="ai-panel__status" aria-hidden="true" />
        </div>
        <p className="ai-panel__subtitle">Log interaction details here via chat</p>
      </header>

      <div className="ai-panel__history" ref={historyRef}>
        {messages.length === 0 ? (
          <div className="ai-panel__empty">
            <p>No messages yet. Describe the interaction and I’ll help fill in the form.</p>
          </div>
        ) : (
          messages.map((msg) => (
            <ChatMessage
              key={msg.id}
              sender={msg.sender}
              text={msg.text}
              timestamp={msg.timestamp}
            />
          ))
        )}
      </div>

      <div className="ai-panel__composer">
        <textarea
          className="ai-panel__textarea"
          placeholder= {`Example:
            Today I met Dr. Gokul at Vijaya Hospital at 11:30 AM. We discussed GlucoCare diabetes tablets and Dicomet pain relief tablets. The doctor showed positive interest, so I provided one sample pack of each product. Follow-up scheduled for next Tuesday.`}
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          onKeyDown={handleKeyDown}
          rows={3}
          disabled={isSending}
        />
        <button
          type="button"
          className="ai-panel__send-btn"
          onClick={handleSend}
          disabled={isSending || !draft.trim()}
        >
          {isSending ? 'Sending…' : 'Send'}
        </button>
      </div>
    </aside>
  );
};

export default AIChatPanel;
