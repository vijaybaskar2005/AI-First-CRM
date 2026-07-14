import React from "react";

/*
 * Detect whether the assistant message is
 * a follow-up email.
 */
const isEmailMessage = (text) => {
  return text.trim().startsWith("Subject:");
};

const renderEmail = (text) => {
  const lines = text.split("\n");

  const subject = lines[0].replace("Subject:", "").trim();

  const body = lines.slice(1).join("\n").trim();

  return (
    <div className="email-card">

      <div className="email-card__header">
        📧 <strong>Follow-up Email</strong>
      </div>

      <div className="email-card__subject">
        <strong>Subject</strong>
        <div>{subject}</div>
      </div>

      <hr />

      <div
        className="email-card__body"
        style={{
          whiteSpace: "pre-line",
          lineHeight: "1.7",
        }}
      >
        {body}
      </div>

    </div>
  );
};

const ChatMessage = ({
  sender = "assistant",
  text = "",
  timestamp = "",
}) => {

  const bubbleClass =
    sender === "user"
      ? "chat-bubble chat-bubble--user"
      : sender === "success"
      ? "chat-bubble chat-bubble--success"
      : "chat-bubble chat-bubble--assistant";

  const rowClass =
    sender === "user"
      ? "chat-row chat-row--right"
      : "chat-row chat-row--left";

  return (
    <div className={rowClass}>

      <div className={bubbleClass}>

        {sender === "success" && (
          <span
            className="chat-bubble__icon"
            aria-hidden="true"
          >
            ✓
          </span>
        )}

        {
          sender === "assistant" &&
          isEmailMessage(text)

            ? renderEmail(text)

            : (
              <p
                className="chat-bubble__text"
                style={{
                  whiteSpace: "pre-line",
                }}
              >
                {text}
              </p>
            )
        }

        {
          timestamp &&
          (
            <span className="chat-bubble__time">
              {timestamp}
            </span>
          )
        }

      </div>

    </div>
  );
};

export default ChatMessage;