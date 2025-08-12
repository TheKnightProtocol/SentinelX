  app = Flask(__name__)  

  @app.route('/')      
  def dashboard():
      # In a real app, you'd fetch dynamic data from your database here.
      # For now, placeholder data:
      dashboard_data = {
          'total_anomalies_24h': 45,
          'high_severity_alerts': 8,
          'network_threats': {'DoS': 5, 'Port Scan': 10},
          'endpoint_threats': {'Malware': 3, 'Suspicious Login': 5},
          'threat_sources': {'External TI': 60, 'Internal Detection': 40}
      }
      return render_template('dashboard.html', data=dashboard_data)

  if __name__ == '__main__':
      app.run(debug=True) # Set debug=False for production
  ```
  * **`templates/dashboard.html` (Simplified Structure):**
      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>SENTINELX Security Dashboard</title>
          <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
      </head>
      <body>
          <header>
              <h1>SENTINELX: Proactive Threat Monitor</h1>
          </header>
          <main>
              <section class="overview">
                  <h2>System Overview</h2>
                  <p>Total Anomalies (Last 24h): <strong>{{ data.total_anomalies_24h }}</strong></p>
                  <p>High Severity Alerts: <strong>{{ data.high_severity_alerts }}</strong></p>
                  </section>

              <section class="threat-breakdown">
                  <h2>Threat Categories</h2>
                  <div class="chart-container">
                      <canvas id="networkThreatsChart"></canvas>
                  </div>
                  <div class="chart-container">
                      <canvas id="endpointThreatsChart"></canvas>
                  </div>
              </section>
          </main>
          <footer>
              <p>&copy; 2025 SENTINELX Project</p>
          </footer>

          <script>
              // JavaScript for Chart.js
              const networkCtx = document.getElementById('networkThreatsChart').getContext('2d');
              new Chart(networkCtx, {
                  type: 'bar',
                  data: {
                      labels: Object.keys({{ data.network_threats | tojson }}),
                      datasets: [{
                          label: 'Network Threat Counts',
                          data: Object.values({{ data.network_threats | tojson }}),
                          backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)'],
                      }]
                  }
                  // Add more chart configurations
              });

              // Similar Chart.js code for endpointThreatsChart
          </script>
      </body>
      </html>
      ```
  
