import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [symptoms, setSymptoms] = useState([]);
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [search, setSearch] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [symptomsLoading, setSymptomsLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("https://health-sense-ai-1.onrender.com/symptoms")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Unable to load symptoms.");
        }
        return response.json();
      })
      .then((data) => setSymptoms(data.symptoms))
      .catch((err) => setError(err.message))
      .finally(() => setSymptomsLoading(false));
  }, []);

  const filteredSymptoms = symptoms.filter((symptom) =>
    symptom.replaceAll("_", " ").toLowerCase().includes(search.toLowerCase())
  );

  const handleSymptomChange = (symptom) => {
    setSelectedSymptoms((previous) =>
      previous.includes(symptom)
        ? previous.filter((item) => item !== symptom)
        : [...previous, symptom]
    );

    setResults([]);
    setError("");
  };

  const clearSymptoms = () => {
    setSelectedSymptoms([]);
    setResults([]);
    setError("");
    setSearch("");
  };

  const handlePredict = async () => {
    setError("");
    setResults([]);

    if (selectedSymptoms.length === 0) {
      setError("Please select at least one symptom.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("https://health-sense-ai-1.onrender.com/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          symptoms: selectedSymptoms
        })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Prediction failed.");
      }

      setResults(data.predictions);
    } catch (err) {
      setError(err.message || "Unable to connect to backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">

      {/* Sidebar */}
      <aside className="sidebar">

        <div className="brand">
          <div className="brand-icon">✚</div>
          <span>HealthSense AI</span>
        </div>

        <p className="menu-heading">MENU</p>

        <nav>
          <a className="nav-link active" href="#dashboard">
            <span>▦</span> Dashboard
          </a>

          <a className="nav-link" href="#symptoms">
            <span>♡</span> Symptom Checker
          </a>

          <a className="nav-link" href="#results">
            <span>▤</span> Predictions
          </a>
        </nav>

        <div className="sidebar-bottom">
          <div className="help-icon">?</div>
          <div>
            <strong>Need help?</strong>
            <p>Contact a healthcare professional for medical guidance.</p>
          </div>
        </div>

      </aside>

      {/* Main Area */}
      <div className="main-area">

        {/* Topbar */}
        <header className="topbar">
          <div>
            <p className="breadcrumb">Home / Dashboard</p>
          </div>

          <div className="profile">
            <div className="profile-icon">U</div>
            <span>Guest User</span>
          </div>
        </header>

        <main className="content" id="dashboard">

          {/* Welcome Banner */}
          <section className="welcome-banner">
            <div>
              <p className="welcome-label">
                YOUR HEALTH, OUR PRIORITY
              </p>

              <h1>Welcome to HealthSense AI</h1>

              <a href="#symptoms" className="banner-button">
                Check Symptoms →
              </a>
            </div>

            <div className="banner-art">✚</div>
          </section>

          {/* Medical Disclaimer */}
          <div className="safety-notice">
            <strong>Medical Disclaimer:</strong>
            <p>
              For educational purposes only. Not a substitute
              for professional medical advice.
            </p>
          </div>

          {/* Information Cards */}
          <section className="info-cards">

            <div className="info-card">
              <div className="card-icon blue">♡</div>
              <div>
                <p>Available symptoms</p>
                <h2>{symptoms.length || "--"}</h2>
              </div>
            </div>

            <div className="info-card">
              <div className="card-icon green">✓</div>
              <div>
                <p>Selected symptoms</p>
                <h2>{selectedSymptoms.length}</h2>
              </div>
            </div>

            <div className="info-card">
              <div className="card-icon purple">✦</div>
              <div>
                <p>Model predictions</p>
                <h2>{results.length}</h2>
              </div>
            </div>

          </section>

          {/* Symptom Checker */}
          <section className="checker-section" id="symptoms">

            <div className="section-heading">
              <div>
                <p className="section-label">SYMPTOM ANALYSIS</p>
                <h2>Check Your Symptoms</h2>
                <p>Select the symptoms you are experiencing.</p>
              </div>

              <span className="step-label">STEP 01 / 02</span>
            </div>

            {/* Search */}
            <div className="search-box">
              <span>⌕</span>

              <input
                type="text"
                placeholder="Search symptoms..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
            </div>

            {/* Selection Information */}
            <div className="selection-info">
              <span>
                {selectedSymptoms.length} symptoms selected
              </span>

              <button
                className="clear-button"
                onClick={clearSymptoms}
              >
                Clear all
              </button>
            </div>

            {/* Selected Symptoms */}
            <div className="selected-panel">
              <h3>Selected Symptoms</h3>

              {selectedSymptoms.length === 0 ? (
                <p className="empty-selection">
                  No symptoms selected yet. Choose symptoms below.
                </p>
              ) : (
                <div className="selected-list">
                  {selectedSymptoms.map((symptom) => (
                    <button
                      type="button"
                      className="selected-chip"
                      key={symptom}
                      onClick={() => handleSymptomChange(symptom)}
                    >
                      {symptom.replaceAll("_", " ")}
                      <span>×</span>
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* Symptoms List */}
            {symptomsLoading ? (
              <p className="loading-text">Loading symptoms...</p>
            ) : (
              <div className="symptom-grid">
                {filteredSymptoms.map((symptom) => (
                  <label
                    key={symptom}
                    className={`symptom-card ${
                      selectedSymptoms.includes(symptom)
                        ? "selected"
                        : ""
                    }`}
                  >
                    <input
                      type="checkbox"
                      checked={selectedSymptoms.includes(symptom)}
                      onChange={() => handleSymptomChange(symptom)}
                    />

                    <span className="custom-check">✓</span>

                    <span className="symptom-name">
                      {symptom.replaceAll("_", " ")}
                    </span>
                  </label>
                ))}
              </div>
            )}

            {!symptomsLoading && filteredSymptoms.length === 0 && (
              <p className="loading-text">
                No matching symptoms found.
              </p>
            )}

            {/* Predict Button */}
            <div className="predict-area">
              <p>
                Selected: <strong>{selectedSymptoms.length}</strong>
              </p>

              <button
                className="predict-button"
                onClick={handlePredict}
                disabled={
                  loading ||
                  symptomsLoading ||
                  symptoms.length === 0
                }
              >
                {loading ? "Analyzing..." : "Analyze Symptoms →"}
              </button>
            </div>

            {error && (
              <p className="error-message">{error}</p>
            )}

          </section>

          {/* Prediction Results */}
          {results.length > 0 && (
            <section className="results-section" id="results">

              <div className="section-heading">
                <div>
                  <p className="section-label">MODEL OUTPUT</p>
                  <h2>Prediction Results</h2>
                  <p>Top three categories predicted by the model.</p>
                </div>

                <span className="result-count">
                  {results.length} Results
                </span>
              </div>

              <div className="result-grid">
                {results.map((item, index) => (
                  <div
                    className="prediction-card"
                    key={item.condition}
                  >
                    <span className="rank">
                      0{index + 1}
                    </span>

                    <h3>
                      {item.condition.replaceAll("_", " ")}
                    </h3>

                    <p>Model score</p>

                    <strong>{item.model_score}%</strong>
                  </div>
                ))}
              </div>

              <div className="disclaimer">
                <strong>Important medical disclaimer</strong>
                <p>
                  These are educational model outputs, not
                  clinically validated predictions. Do not use
                  them to make treatment decisions. Consult a
                  qualified healthcare professional.
                </p>
              </div>

            </section>
          )}

          {/* Footer */}
          <footer>
            HealthSense AI · Educational Project · Not for clinical use
          </footer>

        </main>
      </div>
    </div>
  );
}

export default App;
