import React, { useState } from "react";
import axios from "axios";
import LogInteractionForm from "../components/LogInteractionForm";
import AIChatPanel from "../components/AIChatPanel";
import "../styles/logInteraction.css";

// Dummy seed data
const DUMMY_MESSAGES = [
  {
    id: "m1",
    sender: "assistant",
    text: "Hi! Tell me about the interaction and I'll help you fill out the form.",
    timestamp: "10:41 AM",
  },
  {
    id: "m2",
    sender: "user",
    text:
      'Example: Today I met [Dr.Name] at [Venue] at [Time]. We discussed "X" tablet and "Y" tablet. The doctor showed positive interest. I provided one sample pack of each product. Follow-up scheduled for next Tuesday.',
    timestamp: "10:42 AM",
  },
  {
    id: "m3",
    sender: "success",
    text: "Interaction details captured. Review the form on the left and save when ready.",
    timestamp: "10:42 AM",
  },
];

const EMPTY_FORM = {
  hcpName: "",
  interactionType: "",
  date: "",
  time: "",
  attendees: "",
  topicsDiscussed: "",
  materialsShared: "",
  samplesDistributed: "",
  sentiment: "",
  outcomes: "",
  followUpDate: "",
};

const LogInteractionScreen = () => {
  const [messages, setMessages] = useState(DUMMY_MESSAGES);

  const [formData, setFormData] = useState(EMPTY_FORM);

  const [selectedHcp, setSelectedHcp] = useState(null);

  const handleSendMessage = async (text) => {

    const userMessage = {
      id: `m${Date.now()}`,
      sender: "user",
      text,
      timestamp: new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
    };

    setMessages((prev) => [...prev, userMessage]);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/ai/chat",
        {
          message: text,
        }
      );

      const tool = response.data.tool;

      const data = response.data.data;

      // ----------------------------------------------------
      // LOG INTERACTION
      // ----------------------------------------------------

      if (tool === "log_interaction") {

        const interaction = data.interaction;

        setFormData({

          hcpName: interaction.doctor_name || "",

          interactionType:
            interaction.interaction_type || "",

          date:
            interaction.visit_date || "",

          time:
            interaction.visit_time || "",

          attendees:
            interaction.hospital || "",

          topicsDiscussed:
            interaction.discussion_summary || "",

          materialsShared:
            interaction.products_discussed || "",

          samplesDistributed:
            interaction.samples_distributed || "",

          sentiment:
            interaction.sentiment || "neutral",

          outcomes:
            interaction.outcomes || "",

          followUpDate:
            interaction.follow_up_date || "",

        });

        setMessages((prev) => [

          ...prev,

          {
            id: `m${Date.now()}1`,
            sender: "assistant",
            text:
              "I've extracted the interaction details and filled the form.",
            timestamp: new Date().toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            }),
          },

          {
            id: `m${Date.now()}2`,
            sender: "assistant",
            text:
              `Follow-up Recommendation:\n\n${data.followup}`,
            timestamp: new Date().toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            }),
          },

        ]);

      }

      // ----------------------------------------------------
      // EDIT
      // ----------------------------------------------------

      else if (tool === "edit_interaction") {

        setFormData((prev) => ({

          ...prev,

          hcpName:
            data.doctor_name || prev.hcpName,

          interactionType:
            data.interaction_type || prev.interactionType,

          date:
            data.visit_date || prev.date,

          time:
            data.visit_time || prev.time,

          attendees:
            data.hospital || prev.attendees,

          topicsDiscussed:
            data.discussion_summary || prev.topicsDiscussed,

          materialsShared:
            data.products_discussed || prev.materialsShared,

          samplesDistributed:
            data.samples_distributed || prev.samplesDistributed,

          sentiment:
            data.sentiment || prev.sentiment,

          outcomes:
            data.outcomes || prev.outcomes,

          followUpDate:
            data.follow_up_date || prev.followUpDate,

        }));

        const updatedFields = [];

        if (data.doctor_name) updatedFields.push("Doctor");
        if (data.hospital) updatedFields.push("Hospital");
        if (data.visit_date) updatedFields.push("Date");
        if (data.visit_time) updatedFields.push("Time");
        if (data.products_discussed) updatedFields.push("Products");
        if (data.samples_distributed) updatedFields.push("Samples");
        if (data.sentiment) updatedFields.push("Sentiment");
        if (data.outcomes) updatedFields.push("Outcomes");
        if (data.follow_up_date) updatedFields.push("Follow-up Date");

        setMessages((prev) => [

          ...prev,

          {
            id: `m${Date.now()}`,
            sender: "assistant",
            text:
              updatedFields.length
                ? `Updated: ${updatedFields.join(", ")}`
                : "No changes detected.",
            timestamp: new Date().toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            }),
          },

        ]);

      }

      // ----------------------------------------------------
      // SEARCH SUMMARY
      // ----------------------------------------------------

      else if (tool === "search_interaction") {

        setMessages((prev) => [

          ...prev,

          {
            id: `m${Date.now()}`,
            sender: "assistant",
            text:
              data.summary || data.message,
            timestamp: new Date().toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            }),
          },

        ]);

      }

      // ----------------------------------------------------
      // FOLLOWUP
      // ----------------------------------------------------

      else if (tool === "generate_followup") {

        setMessages((prev) => [

          ...prev,

          {
            id: `m${Date.now()}`,
            sender: "assistant",
            text:
              data.recommendation,
            timestamp: new Date().toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            }),
          },

        ]);

      }
      // ----------------------------------------------------
      // FOLLOW-UP EMAIL
      // ----------------------------------------------------

      else if (tool === "generate_followup_email") {

        setMessages((prev) => [

          ...prev,

          {

            id: `m${Date.now()}`,

            sender: "assistant",

            text: data.email,

            timestamp: new Date().toLocaleTimeString([], {

              hour: "2-digit",

              minute: "2-digit",

            }),

          },

        ]);

      }

    }

    catch (error) {

      console.error(error);

    }

  };

    // Search/Add HCP
  const handleSearchHcp = async (doctorName) => {

    if (!doctorName.trim()) {

      alert("Please enter a doctor name.");

      return;

    }

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/hcp/search",
        {
          params: {
            doctor_name: doctorName,
          },
        }
      );

      console.log(response.data);

      setSelectedHcp(response.data);

      console.log("Selected HCP:", response.data);

      setFormData((prev) => ({
        ...prev,
        hcpName: response.data.doctor_name,
      }));

      alert("Doctor found!");

    }

    catch (error) {

      console.error(error);

      alert("Doctor not found.");

    }

  };

  // Save Interaction
  const handleSaveInteraction = async () => {

    const interactionData = {

      doctor_name: formData.hcpName,

      hospital: formData.attendees,

      interaction_type: formData.interactionType,

      visit_date: formData.date,

      products_discussed: formData.materialsShared,

      discussion_summary: formData.topicsDiscussed,

      samples_distributed: formData.samplesDistributed,

      sentiment: formData.sentiment,

      outcomes: formData.outcomes,

      follow_up_date: formData.followUpDate,

      remarks: formData.outcomes,

    };

    console.log(interactionData);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/ai/save-interaction",
        interactionData
      );

      console.log("Saved!");

      console.log(response.data);

      alert("Interaction saved successfully!");

    }

    catch (error) {

      console.error("Full Error:", error);

      if (error.response) {

        console.log("Status:", error.response.status);

        console.log(error.response.data);

      }

      alert("Unable to save interaction.");

    }

  };

  return (

    <div className="log-interaction-screen">

      <div className="log-interaction-screen__grid">

        <div className="log-interaction-screen__form-col">

          <LogInteractionForm

            formData={formData}

            setFormData={setFormData}

            onSearchHcp={handleSearchHcp}

            onSave={handleSaveInteraction}

          />

        </div>

        <div className="log-interaction-screen__chat-col">

          <AIChatPanel

            messages={messages}

            onSendMessage={handleSendMessage}

          />

        </div>

      </div>

    </div>

  );

};

export default LogInteractionScreen;