import React from "react";

const INTERACTION_TYPES = [
  "Face-to-Face Visit",
  "Video Call",
  "Phone Call",
  "Conference / Event",
  "Email",
  "Meeting"
];

const SENTIMENTS = [
  { value: "positive", label: "Positive" },
  { value: "neutral", label: "Neutral" },
  { value: "negative", label: "Negative" },
];

const LogInteractionForm = ({
  formData,
  setFormData,
  onSearchHcp = () => {},
  onSave = () => {},
}) => {
  

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(formData);
  };

  return (
    <section className="form-card">
      <h1 className="form-card__title">Log HCP Interaction</h1>

      <form className="interaction-form" onSubmit={handleSubmit}>
        <div className="form-field form-field--with-action">
          <label htmlFor="hcpName">HCP Name</label>

          <div className="form-field__row">
            <input
              id="hcpName"
              type="text"
              value={formData.hcpName}
              readOnly
            />
          </div>
        </div>

        <div className="form-grid">
          <div className="form-field">
            <label htmlFor="interactionType">Interaction Type</label>

            <select
              id="interactionType"
              value={formData.interactionType}
              disabled
            >
              <option value="">Select type</option>

              {INTERACTION_TYPES.map((type) => (
                <option key={type} value={type}>
                  {type}
                </option>
              ))}
            </select>
          </div>

          <div className="form-field">
            <label htmlFor="attendees">Venu/Hospital</label>

            <input
              id="attendees"
              type="text"
              value={formData.attendees}
              readOnly
            />
          </div>

          <div className="form-field">
            <label htmlFor="date">Date</label>

            <input
              id="date"
              type="date"
              value={formData.date}
              readOnly
            />
          </div>

          <div className="form-field">
            <label htmlFor="time">Time</label>

            <input
              id="time"
              type="time"
              value={formData.time}
              readOnly
            />
          </div>
        </div>

        <div className="form-field">
          <label htmlFor="topicsDiscussed">Topics Discussed</label>

          <textarea
            id="topicsDiscussed"
            rows={3}
            placeholder="Summarize the key topics covered during the interaction"
            value={formData.topicsDiscussed}
            readOnly
          />
        </div>

        <div className="form-grid">
          <div className="form-field">
            <label htmlFor="materialsShared">Materials Shared</label>

            <input
              id="materialsShared"
              type="text"
              value={formData.materialsShared}
              readOnly
            />
          </div>

          <div className="form-field">
            <label htmlFor="samplesDistributed">Samples Distributed</label>

            <input
              id="samplesDistributed"
              type="text"
              placeholder="e.g. Product A x2"
              value={formData.samplesDistributed}
              readOnly
            />
          </div>
        </div>

        <div className="form-field">
          <span className="form-field__label-text">
            HCP Sentiment
          </span>

          <div className="sentiment-group">
            {SENTIMENTS.map((s) => (
              <button
                key={s.value}
                type="button"
                className={`sentiment-pill sentiment-pill--${s.value} ${
                  formData.sentiment === s.value ? "is-selected" : ""
                }`}
                disabled
              >
                {s.label}
              </button>
            ))}
          </div>
        </div>

        <div className="form-field">
          <label htmlFor="outcomes">Outcomes</label>

          <textarea
            id="outcomes"
            rows={3}
            placeholder="Note next steps, commitments, or decisions made"
            value={formData.outcomes}
            readOnly
          />
        </div>

        <div className="form-field form-field--narrow">
          <label htmlFor="followUpDate">Follow-up Date</label>

          <input
            id="followUpDate"
            type="date"
            value={formData.followUpDate}
            readOnly
          />
        </div>

        <div className="form-actions">
          <button className="btn btn--primary" type="submit">
            Save Interaction
          </button>
        </div>
      </form>
    </section>
  );
};

export default LogInteractionForm;